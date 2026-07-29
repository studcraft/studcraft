#!/usr/bin/env python3
"""Archive every fully-applied OpenSpec change in one batch.

Archiving one change per PR would mean one archive PR per merged
proposal — with several proposal branches landing concurrently (see
system/workflow.md, Versioning), that's a lot of PR churn for a
mechanical step. Mirrors release_cut.py's approach instead: walk every
directory under openspec/changes/ (excluding archive/), archive each
one whose tasks.md has no remaining unchecked boxes, and land all of
them in a single commit/PR.

Changes with incomplete tasks are left alone (reported, not archived) —
archiving is only safe once a proposal's docs/*.md edits have actually
landed on main.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CHANGES_DIR = REPO_ROOT / "openspec" / "changes"

UNCHECKED = "- [ ]"


def pending_changes() -> list[str]:
    if not CHANGES_DIR.exists():
        return []
    return sorted(
        p.name for p in CHANGES_DIR.iterdir()
        if p.is_dir() and p.name != "archive"
    )


def is_fully_applied(name: str) -> bool:
    tasks_file = CHANGES_DIR / name / "tasks.md"
    if not tasks_file.exists():
        return False
    return UNCHECKED not in tasks_file.read_text()


def main() -> None:
    archived = []
    skipped = []

    for name in pending_changes():
        if is_fully_applied(name):
            subprocess.run(
                ["openspec", "archive", name, "--yes"],
                cwd=REPO_ROOT,
                check=True,
            )
            archived.append(name)
        else:
            skipped.append(name)

    if not archived:
        sys.exit("Nothing to archive: no change has a fully-checked tasks.md.")

    print("Archived:", ", ".join(archived))
    if skipped:
        print("Skipped (tasks.md still has unchecked items):", ", ".join(skipped))


if __name__ == "__main__":
    main()
