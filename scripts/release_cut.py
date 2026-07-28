#!/usr/bin/env python3
"""Compute the next version from CHANGELOG [Unreleased] bump markers and apply it.

Reads **Bump:** major|minor|patch entries accumulated under the
[Unreleased] section of CHANGELOG.md, picks the most severe one, bumps
the version from the latest `v*` git tag, rewrites CHANGELOG.md, and
updates the **Version:** header of every docs/*.md file. Prints the new
version to stdout on success.
"""

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
CHANGELOG_VERSION_RE = re.compile(r"^# \[(\d+\.\d+\.\d+)\]", re.MULTILINE)
DOC_VERSION_RE = re.compile(r"(\*\*Version:\*\*\s*)(\d+\.\d+\.\d+)(.*)$", re.MULTILINE)

SEVERITY_RANK = {"patch": 1, "minor": 2, "major": 3}


def latest_tag_version() -> str:
    result = subprocess.run(
        ["git", "tag", "--list", "v*", "--sort=-v:refname"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    tags = result.stdout.strip().splitlines()
    if tags:
        return tags[0].lstrip("v")

    match = CHANGELOG_VERSION_RE.search(CHANGELOG.read_text())
    if match:
        return match.group(1)
    return "0.0.0"


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
    text = CHANGELOG.read_text()
    if UNRELEASED_HEADER not in text:
        sys.exit("No [Unreleased] section found in CHANGELOG.md")

    before, body, tail = split_unreleased(text)
    bumps = BUMP_RE.findall(body)
    if not bumps:
        sys.exit("Nothing to release: [Unreleased] has no **Bump:** entries.")

    severity = max(bumps, key=lambda b: SEVERITY_RANK[b])
    current_version = latest_tag_version()
    next_version = bump_version(current_version, severity)
    today = date.today().isoformat()

    new_text = (
        before
        + f"{UNRELEASED_HEADER}\n\n---\n\n# [{next_version}] - {today}"
        + body
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
