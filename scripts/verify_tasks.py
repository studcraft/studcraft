#!/usr/bin/env python3
"""Run the verification commands a `tasks.md` already contains.

Every well-written change in this repository ends with a section of tasks that
are not edits: `grep -c "per Unit Base" docs/09-transport.md` — before **2**,
after **0**. They are the change's own proof that it did what it said. They are
written down, they are exact, and nobody runs them as a batch — each gets run
by hand, if at all, in the middle of applying something else.

This runs all of them and prints, for each, the command, what the task said to
expect, and what the command actually printed. It does **not** decide whether
they agree: the expectation is prose ("before: **2**, after: **0**"), and which
half applies depends on whether the change has been applied yet — something the
file cannot tell you. Judging it is the reader's job, and this is the tool that
puts both halves on the same screen.

**Only read-only commands are executed.** A `tasks.md` is a text file that
anyone can open a pull request against, and running arbitrary commands out of
one because it is "the repository's own file" is how a checked-in file becomes
a way to execute code. The allowlist below is the whole of what runs; anything
else is printed and skipped, which is also how a task asking for something odd
gets noticed.

Usage:

    python3 scripts/verify_tasks.py                    every unarchived change
    python3 scripts/verify_tasks.py <change-name>      one of them
"""

from __future__ import annotations

import re
import shlex
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from repo import CHANGES_DIR, REPO_ROOT, unarchived_changes  # noqa: E402

TASK_RE = re.compile(r"^\s*- \[([ xX])\]\s*(\d+\.\d+)\s+(.*)$")
CODE_RE = re.compile(r"`([^`]+)`")

# Read-only verbs only, and for the two that can write, the exact read-only
# form. `python3` is restricted to this repository's own scripts by the check
# in `is_runnable`, never to a bare interpreter.
ALLOWED = {
    "grep", "rg", "wc", "ls", "find", "head", "tail", "cat", "sort", "uniq", "diff",
}
ALLOWED_PAIRS = {
    ("git", "status"), ("git", "diff"), ("git", "log"), ("git", "show"),
    ("git", "branch"), ("git", "ls-files"), ("git", "rev-parse"),
    ("openspec", "validate"), ("openspec", "list"), ("openspec", "show"),
}


def is_runnable(command: str) -> tuple[bool, str]:
    """Whether this command is on the allowlist, and why not when it is not."""
    try:
        tokens = shlex.split(command)
    except ValueError:
        return False, "does not parse as a shell command"

    if not tokens:
        return False, "empty"

    for operator in ("&&", "||", "|", ";", ">", ">>", "<", "$("):
        if operator in command:
            return False, f"contains {operator!r}; only a single plain command is run"

    if tokens[0] == "python3":
        if len(tokens) >= 2 and tokens[1].startswith("scripts/") and tokens[1].endswith(".py"):
            return True, ""
        return False, "python3 is only run against this repository's own scripts/"

    if tokens[0] in ALLOWED:
        return True, ""

    if len(tokens) >= 2 and (tokens[0], tokens[1]) in ALLOWED_PAIRS:
        return True, ""

    return False, f"{tokens[0]!r} is not on the read-only allowlist"


def looks_like_command(text: str) -> bool:
    """A first-inline-code span that is a command rather than a filename or ID."""
    head = text.split()[0] if text.split() else ""
    return head in ALLOWED or head == "python3" or head in {"git", "openspec"}


def tasks_with_commands(text: str) -> list[tuple[str, bool, str, str]]:
    """(task number, ticked, command, the expectation prose after it).

    A task wraps across several indented lines, and the number that matters is
    as often on the second as on the first — "before: **2** (TRN-005's sentence
    ...), after: **0**". Reading only the first line truncates the expectation
    exactly where it stops being useful, so continuation lines are folded in.
    """
    lines = text.splitlines()
    found: list[tuple[str, bool, str, str]] = []

    for index, line in enumerate(lines):
        match = TASK_RE.match(line)
        if not match:
            continue

        body = match.group(3)
        for following in lines[index + 1:]:
            if not following.strip() or TASK_RE.match(following) or not following.startswith(" "):
                break
            body += " " + following.strip()

        code = CODE_RE.search(body)
        if not code or not looks_like_command(code.group(1)):
            continue

        expectation = re.sub(r"\s+", " ", body[code.end():].lstrip(" —-").strip())
        found.append((match.group(2), match.group(1).lower() == "x", code.group(1), expectation))

    return found


def run(command: str) -> str:
    try:
        proc = subprocess.run(
            shlex.split(command), cwd=REPO_ROOT, capture_output=True, text=True, timeout=120
        )
    except FileNotFoundError:
        return "(command not found on PATH)"
    except subprocess.TimeoutExpired:
        return "(timed out after 120s)"

    output = (proc.stdout + proc.stderr).strip()
    lines = output.splitlines()
    if len(lines) > 12:
        lines = lines[:12] + [f"... {len(output.splitlines()) - 12} more line(s)"]
    return "\n".join(lines) + f"\n(exit {proc.returncode})" if lines else f"(no output, exit {proc.returncode})"


def verify(change: str) -> int:
    tasks_file = CHANGES_DIR / change / "tasks.md"
    if not tasks_file.is_file():
        print(f"{change}: no tasks.md", file=sys.stderr)
        return 1

    entries = tasks_with_commands(tasks_file.read_text())
    if not entries:
        print(f"{change}: no verification commands found in tasks.md.")
        return 0

    print(f"\n=== {change} — {len(entries)} verification command(s) ===")
    skipped = 0

    for number, ticked, command, expectation in entries:
        mark = "x" if ticked else " "
        print(f"\n[{mark}] {number}  $ {command}")
        if expectation:
            print(f"      says: {expectation}")

        runnable, why = is_runnable(command)
        if not runnable:
            skipped += 1
            print(f"      NOT RUN: {why}")
            continue

        for line in run(command).splitlines():
            print(f"      {line}")

    if skipped:
        print(f"\n{skipped} command(s) were not run — see NOT RUN above.")
    print("\nNothing here is a pass or a fail. Compare what each task says with what it printed.")
    return 0


def main(argv: list[str]) -> int:
    if not CHANGES_DIR.is_dir():
        print("No openspec/changes/ directory.")
        return 0

    names = argv or unarchived_changes()

    status = 0
    for change in names:
        status |= verify(change)
    return status


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
