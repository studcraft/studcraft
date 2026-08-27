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

    python3 scripts/archive_cut.py            archive what can be archived
    python3 scripts/archive_cut.py --check    report only, write nothing

`--check` answers the question the batch used to answer by running: which
changes are ready, and what is holding the rest back.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from repo import CHANGES_DIR, REPO_ROOT, unarchived_changes  # noqa: E402
from tasks_format import unchecked_tasks  # noqa: E402


def tasks_file(name: str) -> Path:
    return CHANGES_DIR / name / "tasks.md"


def blocking_tasks(name: str) -> list[tuple[int, str]]:
    """The unticked tasks holding a change back, fenced blocks excluded.

    A `tasks.md` quotes the edits it makes, so a fenced block can hold a line
    shaped exactly like a task. This read a bare `- [ ]` substring and counted
    two such quotations as real work, which kept a fully-applied change out of
    the archive and reported nothing a reader could act on.

    `tasks_format` is the parser every other reader of a `tasks.md` uses, and
    one parser is the whole point — its own docstring is where that argument is
    written down.
    """
    return unchecked_tasks(tasks_file(name).read_text().splitlines())


def check() -> int:
    """Report what the batch would do, and write nothing.

    The precondition used to be a grep somebody wrote by hand, which anchored
    at column 0 and missed an indented task. Asking the script that decides is
    the only version that cannot disagree with the decision.
    """
    ready: list[str] = []
    blocked: list[tuple[str, list[tuple[int, str]]]] = []
    untracked: list[str] = []

    for name in unarchived_changes():
        if not tasks_file(name).is_file():
            untracked.append(name)
            continue
        holding = blocking_tasks(name)
        if holding:
            blocked.append((name, holding))
        else:
            ready.append(name)

    if ready:
        print("Ready to archive:", ", ".join(ready))
    for name, holding in blocked:
        print(f"\nBlocked — {name}, {len(holding)} unticked task(s):")
        for number, text in holding:
            print(f"  openspec/changes/{name}/tasks.md:{number}: {text.strip()}")
    if untracked:
        print("\nNo tasks.md, so nothing says it was applied:", ", ".join(untracked))

    if not ready and not blocked and not untracked:
        print("No unarchived changes.")

    return 0


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
        if blocking_tasks(name):
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
    argv = sys.argv[1:]
    if argv == ["--check"]:
        sys.exit(check())
    if argv:
        print(__doc__.strip(), file=sys.stderr)
        sys.exit(2)
    sys.exit(main())
