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

# Verbs that cannot write or execute anything, whatever flags they carry.
#
# `sort` and `uniq` were here and are not any more: both write a file when given
# the right operands (`sort -o`, `uniq in out`), and with no pipe to feed them —
# a pipe is refused below — neither has a use in a verification line anyway.
ALLOWED = {"grep", "wc", "ls", "head", "tail", "cat", "diff"}

# Verbs that read, unless carrying the flag that makes them run another program.
# `find -exec` and `rg --pre` are full command execution, out of a file anyone
# can propose by pull request, which is the whole thing this allowlist exists to
# stop.
CONDITIONAL = {
    "find": ("-exec", "-execdir", "-ok", "-okdir", "-delete",
             "-fprint", "-fprint0", "-fprintf", "-fls"),
    "rg": ("--pre", "--pre-glob", "--hostname-bin", "--search-zip", "-z"),
}

ALLOWED_PAIRS = {
    ("git", "status"), ("git", "diff"), ("git", "log"), ("git", "show"),
    ("git", "branch"), ("git", "ls-files"), ("git", "rev-parse"),
    ("openspec", "validate"), ("openspec", "list"), ("openspec", "show"),
}

# `python3 scripts/<anything>.py` was accepted by prefix, which covered
# `release_cut.py` (rewrites every **Version:** header), `archive_cut.py` and
# `open_pr.py` (commits and pushes). Only these read.
#
# `build_index.py` writes `.studcraft/index.json`, and `preflight.py` runs it.
# That file is a gitignored cache of `docs/`, regenerated on demand and never a
# source of truth, so a task that runs either changes nothing that is reviewed.
# `verify_tasks.py` is absent deliberately: a task naming it would recurse.
READ_ONLY_SCRIPTS = {
    "build_index.py",
    "check_delta_coverage.py",
    "check_id_stability.py",
    "check_task_anchors.py",
    "check_todo_quotes.py",
    "lint_ruleset.py",
    "preflight.py",
    "rule.py",
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
        script = tokens[1] if len(tokens) >= 2 else ""
        if script.startswith("scripts/") and script[len("scripts/"):] in READ_ONLY_SCRIPTS:
            return True, ""
        return False, (
            "python3 runs only this repository's read-only scripts: "
            + ", ".join(sorted(READ_ONLY_SCRIPTS))
        )

    if tokens[0] in ALLOWED:
        return True, ""

    if tokens[0] in CONDITIONAL:
        for token in tokens[1:]:
            flag = token.split("=", 1)[0]
            if flag in CONDITIONAL[tokens[0]]:
                return False, f"{tokens[0]} {flag} runs or writes; only its reading form is allowed"
        return True, ""

    if len(tokens) >= 2 and (tokens[0], tokens[1]) in ALLOWED_PAIRS:
        return True, ""

    return False, f"{tokens[0]!r} is not on the read-only allowlist"


def looks_like_command(text: str) -> bool:
    """A first-inline-code span that is a command rather than a filename or ID."""
    head = text.split()[0] if text.split() else ""
    # CONDITIONAL is in here too, so a `find -delete` in a tasks.md is reported
    # as NOT RUN rather than mistaken for prose and skipped silently.
    return head in ALLOWED or head in CONDITIONAL or head == "python3" or head in {"git", "openspec"}


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
