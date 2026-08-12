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

sys.path.insert(0, str(Path(__file__).resolve().parent))

from repo import CHANGES_DIR, REPO_ROOT, unarchived_changes  # noqa: E402

UNCHECKED = "- [ ]"


def tasks_file(name: str) -> Path:
    return CHANGES_DIR / name / "tasks.md"


def is_fully_applied(name: str) -> bool:
    return UNCHECKED not in tasks_file(name).read_text()


def main() -> int:
    """Archive what can be archived, and say exactly what happened either way.

    `openspec archive` can refuse one change in the middle of a batch — deltas
    that disagree with the living spec are the usual reason
    (`system/workflow.md`, Archiving). The ones before it in the run have
    already been archived on disk at that point, so the report has to name them:
    stopping without one leaves whoever picks it up guessing which directories
    moved.
    """
    archived: list[str] = []
    unfinished: list[str] = []
    untracked: list[str] = []
    failure: tuple[str, str] | None = None

    for name in unarchived_changes():
        if not tasks_file(name).is_file():
            untracked.append(name)
            continue
        if not is_fully_applied(name):
            unfinished.append(name)
            continue

        proc = subprocess.run(
            ["openspec", "archive", name, "--yes"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        if proc.returncode != 0:
            failure = (name, (proc.stdout + proc.stderr).strip())
            break
        archived.append(name)

    if archived:
        print("Archived:", ", ".join(archived))
    if unfinished:
        print("Skipped (tasks.md still has unchecked items):", ", ".join(unfinished))
    if untracked:
        print("Skipped (no tasks.md, so nothing says it was applied):", ", ".join(untracked))

    if failure:
        name, output = failure
        print(f"\nSTOPPED on {name}:\n{output}", file=sys.stderr)
        print(
            f"{len(archived)} change(s) were archived before it and are already "
            f"moved on disk. Fix this delta against docs/ and run the batch again.",
            file=sys.stderr,
        )
        return 1

    if not archived:
        print("Nothing to archive: no change has a fully-checked tasks.md.")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
