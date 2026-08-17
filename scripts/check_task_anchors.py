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

Three more defect classes are checked here because a script can settle them,
and every minute an auditor spends re-deriving what a script already proved is
a minute it did not spend on whether the change is *right*:

**A task that announces an anchor and carries no fenced pair.** It described an
edit instead of stating it, and the applier would have to compose the
replacement.

**A coverage-table row naming a task that does not exist.** Tasks get
renumbered and the table does not follow.

**A task that *instructs* anyone to edit `CHANGELOG.md` or a `**Version:**`
header.** Both belong to the Release cut alone, both turn the pull request red,
and both are the proposal's defect rather than the applier's — see
`system/documentation-standards.md` (Versioning). Only task lines and headings
count as instructions; a `tasks.md` that lists `CHANGELOG.md` under "untouched,
deliberately" is doing exactly the right thing and must not be flagged for it.

The format itself is parsed by `scripts/tasks_format.py`, shared with
`scripts/apply_tasks.py` so that the checker and the applier cannot disagree
about which fenced block is an anchor.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from repo import CHANGES_DIR, REPO_ROOT, unarchived_changes  # noqa: E402
from tasks_format import (  # noqa: E402
    FENCE_RE,
    HEADING_RE,
    TASK_LINE_RE,
    TASK_NUMBER_RE,
    blocks,
    edits,
    target_for,
    task_is_done,
)

CHANGELOG_RE = re.compile(r"\bCHANGELOG\.md\b")
VERSION_RE = re.compile(r"\*\*Version:\*\*")

# A coverage-table row, and the cells inside it that are nothing but task
# numbers: "1.1", "18.4, 18.5", "20.2, 20.3".
TABLE_ROW_RE = re.compile(r"^\|(.+)\|\s*$")
TASK_CELL_RE = re.compile(r"^\d+[a-z]*\.\d+(\s*[,–—-]\s*\d+[a-z]*\.\d+)*$")
TASK_REF_RE = re.compile(r"\d+[a-z]*\.\d+")

# How every edit task in this repository announces itself: "replace this
# anchor", "replace this block", "replace the paragraph added by task 1.1 —
# this anchor". A task matching this and carrying no fenced pair has described
# an edit instead of stating it.
REPLACE_ANNOUNCE_RE = re.compile(r"replace .{0,60}?this (anchor|block)", re.IGNORECASE)


class Finding:
    def __init__(self, severity: str, where: str, message: str):
        self.severity = severity
        self.where = where
        self.message = message


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


def check_edit_tasks_carry_a_block(change: str, tasks: Path) -> list[Finding]:
    """A task that says it replaces an anchor must carry both fenced blocks.

    `system/delegating-to-agents.md` puts "give the replacement text verbatim"
    first, and `.claude/agents/proposal-auditor.md` asks the auditor to judge it
    by reading. The half that needs no reading is this one: a task announcing an
    anchor, with no anchor-and-`with:` pair under it, has described an edit
    instead of stating it. The applier then has to compose the replacement,
    which is the one thing it must never do.

    Only the announced form is checked. A task that says "Run `grep …`" or
    "verify" carries no block by design, and a task mentioning
    `check_task_anchors.py` is talking about the checker rather than announcing
    an edit.
    """
    text = tasks.read_text()
    lines = text.splitlines()
    findings: list[Finding] = []

    carried = {edit.task for edit in edits(lines, tasks.parent) if edit.task}

    for number, line in enumerate(lines, start=1):
        match = TASK_NUMBER_RE.match(line)
        if not match or not REPLACE_ANNOUNCE_RE.search(line):
            continue
        if match.group(4) in carried:
            continue
        findings.append(Finding(
            "error", f"{change}/tasks.md:{number}",
            f"task {match.group(4)} announces an anchor but carries no fenced "
            f"anchor-and-`with:` pair. The applier would have to compose the "
            f"replacement — state it verbatim instead.",
        ))

    return findings


def check_coverage_table(change: str, tasks: Path) -> list[Finding]:
    """Every task a coverage table names must exist.

    A coverage table maps each item in `proposal.md` to the task that carries
    it, and `system/delegating-to-agents.md` warns that counts stated in prose
    go stale. So does a row: tasks get renumbered, sections get inserted, and
    the table keeps pointing at a number nobody wrote. Whether the mapping is
    *right* still needs a reader; whether it points at something that exists
    does not.

    Only cells that are nothing but task numbers are read. A cell of prose that
    happens to contain "2.1" is not a reference, and treating it as one would
    turn a sentence about a measurement into an error.
    """
    lines = tasks.read_text().splitlines()
    findings: list[Finding] = []

    existing = {
        match.group(4)
        for match in (TASK_NUMBER_RE.match(line) for line in lines)
        if match
    }
    if not existing:
        return findings

    for number, line in enumerate(lines, start=1):
        row = TABLE_ROW_RE.match(line)
        if not row:
            continue
        for cell in row.group(1).split("|"):
            cleaned = cell.replace("`", "").strip()
            if not TASK_CELL_RE.match(cleaned):
                continue
            missing = [ref for ref in TASK_REF_RE.findall(cleaned) if ref not in existing]
            if missing:
                findings.append(Finding(
                    "error", f"{change}/tasks.md:{number}",
                    f"a coverage-table row names task(s) {', '.join(missing)}, which "
                    f"this file does not contain. Either the task was renumbered and "
                    f"the table did not follow, or the item has no task at all.",
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
        names = unarchived_changes()

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
        findings += check_edit_tasks_carry_a_block(change, tasks)
        findings += check_coverage_table(change, tasks)
        findings += check_version_instructions(change, tasks)

    errors = [f for f in findings if f.severity == "error"]
    others = [f for f in findings if f.severity != "error"]

    for finding in errors:
        print(f"::error::{finding.where}: {finding.message}")
    for finding in others:
        print(f"  {finding.severity}: {finding.where}: {finding.message}")

    if errors:
        print(f"\n{len(errors)} proposal defect(s) across {checked} change(s).")
        return 1

    print(
        f"\nChecked {checked} change(s). No anchor matches more than once, every task "
        f"announcing an anchor carries one, every coverage-table row names a task that "
        f"exists, and no task instructs a CHANGELOG.md or **Version:** edit."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
