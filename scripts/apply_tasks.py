#!/usr/bin/env python3
"""Apply the edits an OpenSpec `tasks.md` already states, without a model.

`system/delegating-to-agents.md` records the finding this script is built on:
*"across every delegated change so far, every defect found afterwards was in
the proposal, not in the execution."* Execution was never the risky half. And
once a task carries its replacement text verbatim — which the same document
requires, and `check_task_anchors.py` enforces — applying it is a substring
replacement with a uniqueness check. That is a script's job.

What this changes about the split: the applier stops transcribing and starts
supervising. It runs `--check`, reads what the script refuses, runs `--write`,
and then does the part no script can — the tasks that are not anchor pairs, and
the verification tasks whose expectations someone has to judge. The second
reader the split exists to provide is unchanged: `proposal-auditor` reads the
proposal before this runs, `ruleset-auditor` reads the applied text after.

**This script will not edit a document to make anything pass.** It has nothing
to make pass: it runs no verification and reads no expectation. An anchor that
does not match exactly once stops the run with the count it found, which is the
same report an applier is required to make and the one thing a tiring reader
skips.

## What it refuses, and why each one is here

The refusals are not defensive programming. A `tasks.md` is a file anyone can
open a pull request against, and this script writes files:

  - **A target outside the repository.** A path is resolved and checked; the
    same argument `verify_tasks.py` makes about running commands out of a
    checked-in file applies to writing them.
  - **`openspec/specs/`.** Shared state, written only by the Archive cut
    (`system/workflow.md`, Archiving). The `PreToolUse` hook refuses it for
    `Edit` and `Write`; a script reached through `Bash` bypasses that hook, so
    it has to refuse for itself.
  - **`CHANGELOG.md` and any `**Version:**` header.** The Release cut owns
    both (`system/documentation-standards.md`, Versioning).
  - **`main` and `develop`,** and a branch not named for the change when the
    change edits `docs/*.md`. Both mirror the gates `preflight.py` mirrors —
    same reason as `openspec/specs/`: the hook cannot see a `Bash` write.

## Order matters and is not negotiable

Edits are applied in `tasks.md` order, each against the result of the ones
above it. Changes in this repository anchor later sections against post-change
text on purpose — `construction-components-state-only-what-they-own` says so in
its own preamble — so an anchor is only guaranteed to match once everything
above it has landed. Nothing is written to disk until every edit has been
resolved against that running text, so a run that stops leaves no half-applied
file.

Usage:

    python3 scripts/apply_tasks.py --check <change-name>    report, write nothing
    python3 scripts/apply_tasks.py --write <change-name>    apply and tick

`--check` is the allowlisted form. `--write` is deliberately not: writing the
ruleset should interrupt the maintainer once, the same way `gh` is listed
subcommand by subcommand in `.claude/settings.json` rather than broadly.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from repo import CHANGES_DIR, REPO_ROOT, git  # noqa: E402
from tasks_format import TASK_NUMBER_RE, edits  # noqa: E402

SPECS_PREFIX = "openspec/specs/"
VERSION_HEADER = "**Version:**"

APPLY, DONE, SKIP, BLOCKED = "apply", "done", "skip", "BLOCKED"


class Outcome:
    """One edit, and what this run would do with it."""

    def __init__(self, edit, verdict: str, detail: str):
        self.edit = edit
        self.verdict = verdict
        self.detail = detail


def branch_refusal(change: str, targets: set[str]) -> str | None:
    """Why this branch must not apply this change, or None.

    A mirror of `preflight.check_branch_name`, and deliberately no stricter: a
    change touching no `docs/*.md` file may be applied from any working branch,
    because that is what the gate allows.
    """
    code, branch = git("rev-parse", "--abbrev-ref", "HEAD")
    if code != 0:
        return "could not read the current branch"

    if branch in ("main", "develop"):
        return (
            f"on {branch}. No document change anywhere in this repository is committed "
            f"to {branch} directly — system/workflow.md (Git Workflow)."
        )

    if any(path.startswith("docs/") for path in targets) and branch != change:
        return (
            f"on branch {branch}, applying {change}. A change that edits docs/*.md lives "
            f"on a branch named for it, so the two cannot drift — "
            f"system/repository-strategy.md (Branch Naming). Switch to {change}."
        )

    return None


def plan(change: str) -> tuple[list[Outcome], dict[Path, str], list[int]]:
    """Resolve every edit against a running copy of each file it touches.

    Returns the outcomes, the new text of each file that would change, and the
    `tasks.md` line indexes whose checkbox would be ticked.
    """
    tasks_file = CHANGES_DIR / change / "tasks.md"
    lines = tasks_file.read_text().splitlines()

    outcomes: list[Outcome] = []
    texts: dict[Path, str] = {}
    tick: list[int] = []

    for edit in edits(lines, tasks_file.parent):
        if edit.path is None or edit.target is None:
            # Ticked, so nothing here would be written either way. A change that
            # deleted a document leaves every earlier task pointing at a file
            # that is gone, and that is the applied state rather than a defect.
            outcomes.append(Outcome(
                edit, SKIP if edit.ticked else BLOCKED,
                f"names {edit.path or 'no file'}, which is neither in the repository "
                f"nor in this change directory. A task that does not say which "
                f"existing file it edits cannot be applied mechanically.",
            ))
            continue

        resolved = edit.target.resolve()
        if not resolved.is_relative_to(REPO_ROOT):
            outcomes.append(Outcome(
                edit, BLOCKED, f"{edit.path} resolves outside the repository.",
            ))
            continue

        relative = resolved.relative_to(REPO_ROOT).as_posix()

        if relative.startswith(SPECS_PREFIX):
            outcomes.append(Outcome(
                edit, BLOCKED,
                f"{relative} is under {SPECS_PREFIX}, which only the Archive cut writes "
                f"— system/workflow.md (Archiving).",
            ))
            continue

        if relative == "CHANGELOG.md":
            outcomes.append(Outcome(
                edit, BLOCKED,
                "CHANGELOG.md is written only by the Release cut — "
                "system/documentation-standards.md (Versioning).",
            ))
            continue

        if VERSION_HEADER in edit.anchor or VERSION_HEADER in edit.replacement:
            outcomes.append(Outcome(
                edit, BLOCKED,
                f"the anchor or its replacement carries a {VERSION_HEADER} header. "
                f"Version headers belong to the Release cut alone.",
            ))
            continue

        if resolved not in texts:
            texts[resolved] = resolved.read_text()

        count = texts[resolved].count(edit.anchor)

        # An additive edit repeats its anchor inside its replacement as a
        # landmark — "the `Dead` bullet is repeated unchanged; the new paragraph
        # goes below it". Applying one leaves the anchor still matching, so the
        # count alone says nothing, and re-applying would add the new text a
        # second time. What settles it is whether the replacement is already
        # there.
        if edit.anchor in edit.replacement and edit.replacement in texts[resolved]:
            outcomes.append(Outcome(
                edit, DONE,
                f"already applied to {relative} — an additive edit whose replacement "
                f"is in place.",
            ))
            continue

        if count > 1:
            outcomes.append(Outcome(
                edit, BLOCKED,
                f"anchor occurs {count} times in {relative}. Replacing one of them "
                f"leaves the rest — a silent wrong edit. Extend the anchor in tasks.md "
                f"until it is unique.",
            ))
            continue

        if count == 0 and edit.ticked:
            outcomes.append(Outcome(edit, DONE, f"already applied to {relative}."))
            continue

        if count == 0:
            outcomes.append(Outcome(
                edit, BLOCKED,
                f"anchor is not in {relative} and its task is not ticked. Either the "
                f"anchor is wrong, or an earlier task this run has not applied changes "
                f"the same lines. Report it — do not adjust the document to fit.",
            ))
            continue

        # A ticked task is never applied. Its anchor surviving is not by itself
        # a defect — a later task in the same change can put the pre-change text
        # back, which is exactly what happens when an audit section supersedes
        # an earlier edit. It is worth a reader's eye and nothing more, because
        # the one thing that could go wrong here, re-applying it, is refused.
        if edit.ticked:
            outcomes.append(Outcome(
                edit, SKIP,
                f"ticked, and its pre-change anchor is still in {relative}. Not "
                f"applied. Either a later task restored the text, or the tick is "
                f"wrong — a reader decides, this script will not guess.",
            ))
            continue

        texts[resolved] = texts[resolved].replace(edit.anchor, edit.replacement, 1)
        outcomes.append(Outcome(edit, APPLY, f"{relative}."))
        if edit.task_line >= 0 and not edit.ticked:
            tick.append(edit.task_line)

    unchanged = [
        path for path, text in texts.items() if text == path.read_text()
    ]
    for path in unchanged:
        del texts[path]

    return outcomes, texts, tick


def tick_boxes(lines: list[str], indexes: list[int]) -> list[str]:
    """Tick the checkbox of every task this run applied, and no other.

    Verification tasks stay unticked on purpose. Their expectations need
    someone to compare against what the command prints, and `archive_cut.py`
    reads unticked boxes to decide a change is not finished — which, until
    somebody has judged them, it is not.
    """
    ticked = list(lines)
    for index in indexes:
        match = TASK_NUMBER_RE.match(ticked[index])
        if match and match.group(2) == " ":
            ticked[index] = (
                match.group(1) + "x" + match.group(3) + ticked[index][match.end(3):]
            )
    return ticked


def report(change: str, outcomes: list[Outcome], texts: dict[Path, str], tick: list[int],
           write: bool) -> int:
    blocked = [o for o in outcomes if o.verdict == BLOCKED]
    applying = [o for o in outcomes if o.verdict == APPLY]
    done = [o for o in outcomes if o.verdict == DONE]

    print(f"\n=== {change} — {len(outcomes)} anchor/replacement pair(s) ===\n")

    for outcome in outcomes:
        if outcome.verdict == DONE and not blocked:
            continue
        print(f"  {outcome.verdict:<7} {outcome.edit.where:<12} {outcome.detail}")

    if done and not blocked:
        print(f"  {DONE:<7} {len(done)} pair(s) already in place, not listed.")

    print()

    if blocked:
        print(
            f"{len(blocked)} pair(s) blocked. Nothing was written — the whole run stops "
            f"so that no file is left half-applied. Each blocker above is a defect in "
            f"tasks.md, not in the ruleset: fix the proposal, never the document."
        )
        return 1

    if not applying:
        print(f"Nothing to apply. {len(done)} pair(s) are already in place.")
        return 0

    if not write:
        files = ", ".join(sorted(p.relative_to(REPO_ROOT).as_posix() for p in texts))
        print(
            f"{len(applying)} pair(s) would be applied across {len(texts)} file(s): "
            f"{files}.\nRe-run with --write to apply them and tick their boxes."
        )
        return 0

    for path, text in texts.items():
        path.write_text(text)

    tasks_file = CHANGES_DIR / change / "tasks.md"
    source = tasks_file.read_text()
    trailing = "\n" if source.endswith("\n") else ""
    tasks_file.write_text("\n".join(tick_boxes(source.splitlines(), tick)) + trailing)

    print(
        f"Applied {len(applying)} pair(s) across {len(texts)} file(s) and ticked "
        f"{len(tick)} task(s).\nVerification tasks are untouched: run "
        f"`python3 scripts/verify_tasks.py {change}` and judge them, then read the "
        f"applied text."
    )
    return 0


def main(argv: list[str]) -> int:
    if len(argv) != 2 or argv[0] not in ("--check", "--write"):
        print(
            "usage: python3 scripts/apply_tasks.py --check <change-name>\n"
            "       python3 scripts/apply_tasks.py --write <change-name>\n"
            "\nThe mode is required. A command that writes the ruleset says so.",
            file=sys.stderr,
        )
        return 2

    mode, change = argv
    tasks_file = CHANGES_DIR / change / "tasks.md"
    if not tasks_file.is_file():
        print(f"{change}: no tasks.md at {tasks_file}", file=sys.stderr)
        return 1

    outcomes, texts, tick = plan(change)

    refusal = branch_refusal(change, {
        o.edit.target.resolve().relative_to(REPO_ROOT).as_posix()
        for o in outcomes
        if o.verdict == APPLY and o.edit.target is not None
    })
    if refusal and (mode == "--write" or any(o.verdict == APPLY for o in outcomes)):
        if mode == "--write":
            print(f"\nRefusing: {refusal}", file=sys.stderr)
            return 1
        print(f"\n--write would refuse: {refusal}", file=sys.stderr)

    return report(change, outcomes, texts, tick, write=(mode == "--write"))


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
