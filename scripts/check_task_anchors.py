#!/usr/bin/env python3
"""Check the anchors in an OpenSpec `tasks.md` before anyone applies them.

`system/delegating-to-agents.md` records that across every delegated change in
this repository, *every defect found afterwards was in the proposal, not in the
execution*. The single sharpest instance is an anchor that matches twice: the
applier replaces one of them, the file ends up half-changed, and nothing about
the result looks wrong. `.claude/agents/ruleset-auditor.md` tells the auditor to
check this with `grep -cF`. That is a script's job, so here it is.

Two things are checked, and they mean different things:

**An anchor matching more than once is a defect, always.** It produces a silent
wrong edit whenever the change is applied, and no later reading catches it.
This fails.

**An anchor matching zero times is ambiguous, and this tool will not pretend
otherwise.** An anchor is pre-change text: before the change is applied it must
match exactly once, and after it is applied it must match zero times, because
the text it named is gone. So zero is reported, with which of the two it is
left to the reader — the one thing the script cannot know is whether the change
has been applied yet.

Also checked: a `tasks.md` that *instructs* anyone to edit `CHANGELOG.md` or a
`**Version:**` header. Both belong to the Release cut alone, both turn the pull
request red, and both are the proposal's defect rather than the applier's — see
`system/documentation-standards.md` (Versioning). Only task lines and headings
count as instructions; a `tasks.md` that lists `CHANGELOG.md` under "untouched,
deliberately" is doing exactly the right thing and must not be flagged for it.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CHANGES_DIR = REPO_ROOT / "openspec" / "changes"

FENCE_RE = re.compile(r"^```")
TASK_LINE_RE = re.compile(r"^\s*- \[[ xX]\]")
TASK_DONE_RE = re.compile(r"^\s*- \[[xX]\]")
HEADING_RE = re.compile(r"^#{1,4} ")
# Any path a task can name, not only one under docs/. It was `docs/` only, and a
# task targeting `.claude/agents/ruleset-auditor.md` then resolved to whichever
# docs/ file a previous section happened to name — which reports a missing anchor
# at best and silently checks the wrong file at worst. A change is allowed to
# touch more than the ruleset, so the checker has to be.
#
# **At least one `/` is required.** A first attempt without that matched the bare
# `design.md`, `proposal.md` and `tasks.md` that every change mentions in its own
# prose, resolved them against the repository root where no such files exist, and
# turned nine harmless sentences into errors. A directory component is what
# separates "the file this task edits" from "a document this task talks about".
TARGET_PATH_RE = re.compile(r"`((?:[\w.-]+/)+[\w.-]+\.(?:md|py|json|ya?ml))`")
CHANGELOG_RE = re.compile(r"\bCHANGELOG\.md\b")
VERSION_RE = re.compile(r"\*\*Version:\*\*")


class Finding:
    def __init__(self, severity: str, where: str, message: str):
        self.severity = severity
        self.where = where
        self.message = message


def blocks(lines: list[str]) -> list[tuple[int, str, str]]:
    """Every fenced block, as (line number, lead-in text, body).

    The lead-in is the nearest preceding non-empty line, which is what says
    whether the block is an anchor or the text replacing it: this repository
    writes "Replace this anchor ...:" then the anchor, then "with:" then the
    replacement.
    """
    found: list[tuple[int, str, str]] = []
    index = 0

    while index < len(lines):
        if not FENCE_RE.match(lines[index]):
            index += 1
            continue

        start = index
        index += 1
        body: list[str] = []
        while index < len(lines) and not FENCE_RE.match(lines[index]):
            body.append(lines[index])
            index += 1
        index += 1

        lead = ""
        for back in range(start - 1, -1, -1):
            if lines[back].strip():
                lead = lines[back].strip()
                break

        found.append((start + 1, lead, "\n".join(body)))

    return found


def task_is_done(lines: list[str], upto: int) -> bool:
    """Whether the task owning the block above line `upto` is already ticked.

    This is what separates the two readings of a zero-match anchor. A ticked
    task has been applied, so its anchor is *supposed* to be gone and saying so
    is noise — on a fully applied change it is thirty-five lines of noise, which
    is how a real finding gets missed. An unticked task's missing anchor is the
    finding this script exists for.
    """
    for back in range(upto - 1, -1, -1):
        if TASK_LINE_RE.match(lines[back]):
            return bool(TASK_DONE_RE.match(lines[back]))
    return False


def target_for(lines: list[str], upto: int) -> str | None:
    """Which file the anchor above line `upto` belongs to.

    Taken from the nearest preceding line that names one — a section heading
    ("## 2. `docs/09-transport.md` — ...") or the task line itself. A block whose
    target is a spec delta, or a task that never says which file it edits, names
    no path and is reported as unresolved rather than guessed at.

    The path may be anywhere in the repository. Restricting it to `docs/` meant a
    task naming `.claude/agents/ruleset-auditor.md` fell through to whichever
    ruleset document a previous section had named, and was then checked against
    the wrong file.
    """
    for back in range(upto - 1, -1, -1):
        match = TARGET_PATH_RE.search(lines[back])
        if match and (HEADING_RE.match(lines[back]) or TASK_LINE_RE.match(lines[back])):
            return match.group(1)
    return None


def check_anchors(change: str, tasks: Path) -> list[Finding]:
    lines = tasks.read_text().splitlines()
    findings: list[Finding] = []
    cache: dict[str, str] = {}
    applied = 0

    for line_no, lead, body in blocks(lines):
        if lead.endswith("with:") or not body.strip():
            continue

        where = f"{change}/tasks.md:{line_no}"
        path = target_for(lines, line_no - 1)
        if path is None:
            findings.append(Finding(
                "unresolved", where,
                "block names no file — a spec delta, or a task that does not say "
                "which file it edits",
            ))
            continue

        # A task may name a file in the repository, or one inside its own change
        # directory — a spec delta is written as `specs/<capability>/spec.md`.
        # Try both before concluding anything, and treat a path that resolves to
        # neither as unresolved rather than as an error: a `tasks.md` is allowed
        # to mention a file it does not edit.
        target = REPO_ROOT / path
        if not target.is_file():
            target = tasks.parent / path
        if not target.is_file():
            findings.append(Finding(
                "unresolved", where,
                f"names {path}, which is neither in the repository nor in this change "
                f"directory — a block that talks about a file rather than editing one",
            ))
            continue

        if path not in cache:
            cache[path] = target.read_text()

        count = cache[path].count(body)
        if count > 1:
            findings.append(Finding(
                "error", where,
                f"anchor occurs {count} times in {path}. Applying it replaces one of "
                f"them and leaves the rest — a silent wrong edit. Extend the anchor "
                f"until it is unique.",
            ))
        elif count == 0 and not task_is_done(lines, line_no - 1):
            findings.append(Finding(
                "note", where,
                f"anchor is not in {path}, and its task is not ticked. Either the "
                f"anchor is wrong, or the task was applied without being marked.",
            ))
        elif count == 0:
            applied += 1

    if applied:
        findings.append(Finding(
            "info", change,
            f"{applied} anchor(s) already gone from their target, each on a ticked "
            f"task — the expected state for an applied change.",
        ))

    return findings


def check_replacement_format(change: str, tasks: Path) -> list[Finding]:
    """Replacement text must be fenced, not quoted.

    Both conventions exist in this repository's history, and the switch was an
    improvement rather than drift: every change up to 2026-08-07 wrapped
    replacement text in a `> ` blockquote, and every change from 2026-08-10
    fences it. A blockquote forces a `> ` onto every line of the replacement,
    including the blank ones and the rows of a markdown table, and each of those
    prefixes is a character the applier has to strip correctly. A fence has no
    per-line prefix to get wrong.

    What makes this worth a check rather than a preference is that
    `.claude/agents/proposal-applier.md` described the blockquote form for
    several changes after the convention had already moved. Nothing broke,
    because each `tasks.md` explains its own convention in its preamble and the
    file wins — but an applier reading one format in its instructions and
    another in the file it is given is the exact situation a weaker model is
    least able to recover from.

    Archived changes legitimately use the old form. Only unarchived changes are
    checked unless one is named explicitly.
    """
    lines = tasks.read_text().splitlines()
    findings: list[Finding] = []

    fenced = sum(1 for line in lines if FENCE_RE.match(line))

    # A run of quoted lines long enough to be a replacement body, rather than a
    # single quoted motto such as "> **Every Brick Matters.**" being discussed.
    runs: list[int] = []
    run_start = None
    for number, line in enumerate(lines, start=1):
        if line.startswith(">"):
            run_start = run_start if run_start is not None else number
        elif run_start is not None:
            if number - run_start >= 3:
                runs.append(run_start)
            run_start = None

    if runs:
        findings.append(Finding(
            "error", f"{change}/tasks.md:{runs[0]}",
            f"{len(runs)} block(s) of replacement text are written as a `> ` "
            f"blockquote. The convention is a triple-backtick fence, which has no "
            f"per-line prefix for the applier to strip and does not force a `>` onto "
            f"the blank lines and table rows inside the replacement. Convert them, and "
            f"state in the preamble that the fence is not part of the text.",
        ))

    if runs and fenced:
        findings.append(Finding(
            "error", f"{change}/tasks.md",
            "the file mixes both replacement conventions. One file, one convention — "
            "an applier told which form to expect must find only that form.",
        ))

    return findings


def check_version_instructions(change: str, tasks: Path) -> list[Finding]:
    findings: list[Finding] = []

    for number, line in enumerate(tasks.read_text().splitlines(), start=1):
        if not (TASK_LINE_RE.match(line) or HEADING_RE.match(line)):
            continue
        where = f"{change}/tasks.md:{number}"
        if CHANGELOG_RE.search(line):
            findings.append(Finding(
                "error", where,
                "a task or heading names CHANGELOG.md. It is written only by the "
                "Release cut — 'Docs must not edit CHANGELOG.md directly' is a "
                "required check, and this makes the pull request red.",
            ))
        if VERSION_RE.search(line):
            findings.append(Finding(
                "error", where,
                "a task or heading names a **Version:** header. Version headers belong "
                "to the Release cut alone; docs/*.md changes default to a minor bump.",
            ))

    return findings


def main(argv: list[str]) -> int:
    if not CHANGES_DIR.is_dir():
        print("No openspec/changes/ directory. Nothing to check.")
        return 0

    if argv:
        names = argv
    else:
        names = [
            path.name
            for path in sorted(CHANGES_DIR.iterdir())
            if path.is_dir() and path.name != "archive"
        ]

    findings: list[Finding] = []
    checked = 0

    for change in names:
        tasks = CHANGES_DIR / change / "tasks.md"
        if not tasks.is_file():
            print(f"{change}: no tasks.md", file=sys.stderr)
            continue
        checked += 1
        findings += check_anchors(change, tasks)
        findings += check_replacement_format(change, tasks)
        findings += check_version_instructions(change, tasks)

    errors = [f for f in findings if f.severity == "error"]
    others = [f for f in findings if f.severity != "error"]

    for finding in errors:
        print(f"::error::{finding.where}: {finding.message}")
    for finding in others:
        print(f"  {finding.severity}: {finding.where}: {finding.message}")

    if errors:
        print(f"\n{len(errors)} anchor/version issue(s) across {checked} change(s).")
        return 1

    print(
        f"\nChecked {checked} change(s). No anchor matches more than once, and no task "
        f"instructs a CHANGELOG.md or **Version:** edit."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
