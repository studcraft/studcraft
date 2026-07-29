#!/usr/bin/env python3
"""Compute the next version from commit-message bump markers and apply it.

Every merged PR is a single squash commit on `main` (this repo always
squash-merges). Instead of requiring PRs to hand-edit CHANGELOG.md's
[Unreleased] section — which made two concurrent PRs collide on the same
insertion point — the **Bump:** major|minor|patch marker lives in a
commit message instead. This script:

1. Finds the last release tag (`v*`), the anchor for "since last release".
2. Walks `git log <last-tag>..HEAD` to collect every commit merged since.
3. Picks the most severe **Bump:** marker across those commits.
4. Bumps the version, rewrites CHANGELOG.md with an auto-generated entry
   built from the commit subjects, and updates every docs/*.md
   **Version:** header.

No individual PR ever touches CHANGELOG.md; only this script does, and it
only runs as part of the separate, serialized release-cut workflow.
Prints the new version to stdout on success.
"""

from __future__ import annotations

import re
import subprocess
import sys
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CHANGELOG = REPO_ROOT / "CHANGELOG.md"
DOCS_DIR = REPO_ROOT / "docs"

UNRELEASED_HEADER = "# [Unreleased]"
BUMP_RE = re.compile(r"^\*\*Bump:\*\*\s*(major|minor|patch)\s*$", re.MULTILINE)
DOC_VERSION_RE = re.compile(r"(\*\*Version:\*\*\s*)(\d+\.\d+\.\d+)(.*)$", re.MULTILINE)

SEVERITY_RANK = {"patch": 1, "minor": 2, "major": 3}

RECORD_SEP = "\x1e"
FIELD_SEP = "\x1f"


def latest_tag() -> str | None:
    result = subprocess.run(
        ["git", "tag", "--list", "v*", "--sort=-v:refname"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    tags = result.stdout.strip().splitlines()
    return tags[0] if tags else None


def commits_since(tag: str | None) -> list[tuple[str, str, str]]:
    rev_range = f"{tag}..HEAD" if tag else "HEAD"
    result = subprocess.run(
        ["git", "log", rev_range, f"--format=%H{FIELD_SEP}%s{FIELD_SEP}%b{RECORD_SEP}"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    commits = []
    for record in result.stdout.split(RECORD_SEP):
        record = record.strip("\n")
        if not record:
            continue
        parts = record.split(FIELD_SEP)
        sha = parts[0]
        subject = parts[1] if len(parts) > 1 else ""
        body = parts[2] if len(parts) > 2 else ""
        commits.append((sha, subject, body))
    return commits


def bump_version(version: str, severity: str) -> str:
    major, minor, patch = (int(part) for part in version.split("."))
    if severity == "major":
        return f"{major + 1}.0.0"
    if severity == "minor":
        return f"{major}.{minor + 1}.0"
    return f"{major}.{minor}.{patch + 1}"


def split_unreleased(text: str) -> tuple[str, str, str]:
    start = text.index(UNRELEASED_HEADER)
    after = start + len(UNRELEASED_HEADER)
    rest = text[after:]
    next_header = re.search(r"\n# \[", rest)
    body_end = next_header.start() if next_header else len(rest)
    return text[:start], rest[:body_end], rest[body_end:]


def main() -> None:
    tag = latest_tag()
    commits = commits_since(tag)
    if not commits:
        sys.exit("Nothing to release: no commits since the last release tag.")

    bumps = []
    for _, subject, body in commits:
        bumps.extend(BUMP_RE.findall(f"{subject}\n{body}"))

    if not bumps:
        sys.exit("Nothing to release: no commit since the last release tag has a **Bump:** marker.")

    severity = max(bumps, key=lambda b: SEVERITY_RANK[b])
    current_version = tag.lstrip("v") if tag else "0.0.0"
    next_version = bump_version(current_version, severity)
    today = date.today().isoformat()

    changes = "\n".join(f"- {subject}" for _, subject, _ in reversed(commits))

    text = CHANGELOG.read_text()
    if UNRELEASED_HEADER not in text:
        sys.exit("No [Unreleased] section found in CHANGELOG.md")

    before, _, tail = split_unreleased(text)
    new_text = (
        before
        + f"{UNRELEASED_HEADER}\n\n---\n\n# [{next_version}] - {today}\n\n{changes}\n"
        + tail
    )
    CHANGELOG.write_text(new_text)

    for doc in sorted(DOCS_DIR.glob("*.md")):
        doc_text = doc.read_text()
        updated, count = DOC_VERSION_RE.subn(rf"\g<1>{next_version}\3", doc_text)
        if count:
            doc.write_text(updated)

    print(next_version)


if __name__ == "__main__":
    main()
