#!/usr/bin/env python3
"""Compute the next version purely from git history and apply it.

No commit or PR is required to declare anything. This script:

1. Finds the last release tag (`v*`), the anchor for "since last release".
2. Checks whether any `docs/*.md` file changed since that tag. If not,
   there is nothing to release.
3. Picks a bump severity with zero required human/agent input:
   - Default: "minor" — any docs/*.md change warrants a release.
   - Auto-escalated to "major" if any commit message since the last tag
     happens to contain a `**Bump:** major` marker (fully optional; a
     commit can flag itself as breaking, but nothing requires it to).
   - Overridable at release-cut time via the RELEASE_SEVERITY env var
     (set from the `Release cut` workflow's `severity` input), for the
     rare case where the person cutting the release knows better than
     the default.
4. Bumps the version, rewrites CHANGELOG.md with an auto-generated entry
   built from the commit subjects since the last tag, and updates every
   docs/*.md **Version:** header.

No individual PR ever touches CHANGELOG.md; only this script does, and it
only runs as part of the separate, serialized release-cut workflow.
Prints the new version to stdout on success.
"""

from __future__ import annotations

import os
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from repo import RULE_HEADER_RE  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent
CHANGELOG = REPO_ROOT / "CHANGELOG.md"
DOCS_DIR = REPO_ROOT / "docs"

UNRELEASED_HEADER = "# [Unreleased]"
BUMP_RE = re.compile(r"^\*\*Bump:\*\*\s*(major|minor|patch)\s*$", re.MULTILINE)
DOC_VERSION_RE = re.compile(r"(\*\*Version:\*\*\s*)(\d+\.\d+\.\d+)(.*)$", re.MULTILINE)

DEFAULT_SEVERITY = "minor"
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


def docs_changed_since(tag: str | None) -> bool:
    rev_range = f"{tag}..HEAD" if tag else "HEAD"
    result = subprocess.run(
        ["git", "diff", "--name-only", rev_range, "--", "docs/"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    return bool(result.stdout.strip())


def resolve_severity(commits: list[tuple[str, str, str]]) -> str:
    override = os.environ.get("RELEASE_SEVERITY", "auto").strip().lower()
    if override in SEVERITY_RANK:
        return override

    bumps = []
    for _, subject, body in commits:
        bumps.extend(BUMP_RE.findall(f"{subject}\n{body}"))
    if "major" in bumps:
        return "major"
    return DEFAULT_SEVERITY


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


def unreleased_content(section: str) -> str:
    """Whatever somebody wrote under `# [Unreleased]`, ignoring the furniture.

    A cut leaves the section holding a `---` rule and blank lines, which is not
    content. Anything else is text this script would otherwise replace without
    saying so.
    """
    kept = [
        line for line in section.splitlines()
        if line.strip() and line.strip() != "---"
    ]
    return "\n".join(kept)


def main() -> None:
    tag = latest_tag()

    if not docs_changed_since(tag):
        sys.exit("Nothing to release: no docs/*.md changes since the last release tag.")

    commits = commits_since(tag)
    severity = resolve_severity(commits)
    current_version = tag.lstrip("v") if tag else "0.0.0"
    next_version = bump_version(current_version, severity)
    today = date.today().isoformat()

    changes = "\n".join(f"- {subject}" for _, subject, _ in reversed(commits))

    text = CHANGELOG.read_text()
    if UNRELEASED_HEADER not in text:
        sys.exit("No [Unreleased] section found in CHANGELOG.md")

    before, unreleased, tail = split_unreleased(text)
    if unreleased_content(unreleased):
        # The entry below is built from commit subjects, and this section is
        # rewritten empty. Anything written here by hand would be discarded
        # silently, which is how a hand-written note disappears at the next cut.
        # `Docs must not edit CHANGELOG.md directly` only fires on a pull request
        # that also touches docs/*.md, so one that touches neither can land text
        # here; stop rather than delete it.
        sys.exit(
            "CHANGELOG.md's [Unreleased] section is not empty:\n\n"
            f"{unreleased_content(unreleased)}\n\n"
            "That text was written by hand, and this script would replace it. "
            "Nobody edits CHANGELOG.md directly — system/documentation-standards.md "
            "(Versioning). Move whatever belongs in the release into the commit "
            "subjects it is built from, empty the section, and run the cut again."
        )

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
            continue

        # A document added between two cuts has no header to rewrite, and nothing
        # else may write one — the PreToolUse hook and scripts/apply_tasks.py both
        # refuse it, and scripts/lint_ruleset.py requires it. This is the only
        # place that closes that loop, so the cut supplies the line rather than
        # skipping the file.
        #
        # Exactly one line is inserted, directly below the title. The release
        # branch's exemption in `Docs require OpenSpec proposal` is constrained by
        # content: every added or removed line in the docs/*.md diff that is not
        # the header itself fails the check, and a blank line is one of them.
        lines = doc_text.splitlines(keepends=True)
        if lines and RULE_HEADER_RE.search(doc_text):
            lines.insert(1, f"**Version:** {next_version}\n")
            doc.write_text("".join(lines))

    print(next_version)


if __name__ == "__main__":
    main()
