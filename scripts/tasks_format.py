#!/usr/bin/env python3
"""How a `tasks.md` is written, read by one parser instead of two.

`system/delegating-to-agents.md` ("Give the replacement text verbatim") fixes
the shape every edit task in this repository takes:

    - [ ] 2.1 In `AAA-001`, replace this anchor — the whole rule body:

    ```
    the text as it stands
    ```

    with:

    ```
    the text it becomes
    ```

That is a patch format. It carries no prose to interpret: the anchor is an
exact substring that occurs once, and the replacement is what takes its place.
`check_task_anchors.py` reads it to count anchors and `apply_tasks.py` reads it
to perform the replacement, and the argument `repo.py` already makes applies
here — *"a second copy of that would drift from the first, and the drift would
be silent."* A parser that disagreed with the checker about which block is an
anchor would apply an edit nobody had checked.

Import it the way the other scripts import `repo`:

    sys.path.insert(0, str(Path(__file__).resolve().parent))

    from tasks_format import blocks, edits  # noqa: E402
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from repo import REPO_ROOT  # noqa: E402

FENCE_RE = re.compile(r"^```")
TASK_LINE_RE = re.compile(r"^\s*- \[[ xX]\]")
TASK_DONE_RE = re.compile(r"^\s*- \[[xX]\]")
# A section may carry a letter suffix — `13c.1`, `22b.4`. Changes here grow an
# audit section after the tasks below it are already numbered, and inserting
# `13c` rather than renumbering is what keeps every reference to task 14 true.
TASK_NUMBER_RE = re.compile(r"^(\s*- \[)([ xX])(\]\s*)(\d+[a-z]*\.\d+)\s")
HEADING_RE = re.compile(r"^#{1,4} ")

# Any path a task can name, not only one under docs/. It was `docs/` only, and a
# task targeting `.claude/agents/ruleset-auditor.md` then resolved to whichever
# docs/ file a previous section happened to name — which reports a missing anchor
# at best and silently checks the wrong file at worst. A change is allowed to
# touch more than the ruleset, so the parser has to be.
#
# A repository-root file has no `/` to require: `TODO.md` and `CODE_OF_DESIGN.md`
# are targets too, and a version that demanded a directory component could not see
# them (#126 worked around it with `./TODO.md`). This is for a task line, which
# names an edit target by construction — that is what the line is for.
TARGET_PATH_RE = re.compile(r"`((?:[\w.-]+/)*[\w.-]+\.(?:md|py|json|ya?ml))`")

# A heading is a section title, not a task, and may name any file it discusses
# in passing — "### Two `skip` lines from `apply_tasks.py` that are correct"
# names a script it is *talking about*, not editing. Every heading this
# repository has used as a real target names a `docs/…` path, so the directory
# component is still required here; only the task-line pattern above drops it.
HEADING_TARGET_RE = re.compile(r"`((?:[\w.-]+/)+[\w.-]+\.(?:md|py|json|ya?ml))`")

# What every change calls itself, never what it edits. Excluded by the full
# matched path, not by basename — `openspec/changes/foo/tasks.md` is a real
# target and only a bare `tasks.md` is the change talking about itself.
NOT_A_TARGET = frozenset({"design.md", "proposal.md", "tasks.md"})


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


def owning_task(lines: list[str], upto: int) -> tuple[int, str, bool] | None:
    """The task owning whatever sits above line `upto`, as (index, number, ticked).

    The index is into `lines`, so a caller that ticks a box knows which line to
    rewrite. A block that no task precedes — one in a file's preamble — returns
    None rather than being attributed to nothing.
    """
    for back in range(upto - 1, -1, -1):
        if not TASK_LINE_RE.match(lines[back]):
            continue
        number = TASK_NUMBER_RE.match(lines[back])
        return back, (number.group(4) if number else ""), bool(TASK_DONE_RE.match(lines[back]))
    return None


def task_is_done(lines: list[str], upto: int) -> bool:
    """Whether the task owning the block above line `upto` is already ticked.

    This is what separates the two readings of a zero-match anchor. A ticked
    task has been applied, so its anchor is *supposed* to be gone and saying so
    is noise — on a fully applied change it is thirty-five lines of noise, which
    is how a real finding gets missed. An unticked task's missing anchor is the
    finding `check_task_anchors.py` exists for.
    """
    owner = owning_task(lines, upto)
    return bool(owner and owner[2])


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

    A task line and a heading are read with different patterns. A task line
    names its own edit target, so a bare filename resolves; a heading is a
    section title free to mention any file in passing, so it still needs a
    directory component — without that, "### ... from `apply_tasks.py` ..."
    would resolve as if the heading were editing `apply_tasks.py`.
    """
    for back in range(upto - 1, -1, -1):
        if TASK_LINE_RE.match(lines[back]):
            pattern = TARGET_PATH_RE
        elif HEADING_RE.match(lines[back]):
            pattern = HEADING_TARGET_RE
        else:
            continue
        for match in pattern.finditer(lines[back]):
            if match.group(1) not in NOT_A_TARGET:
                return match.group(1)
    return None


def resolve(path: str, change_dir: Path) -> Path | None:
    """The file a task's path names, in the repository or in its own change dir.

    A spec delta is written as `specs/<capability>/spec.md`, relative to the
    change directory. A path that resolves to neither is not an error here: a
    `tasks.md` is allowed to mention a file it does not edit.
    """
    for candidate in (REPO_ROOT / path, change_dir / path):
        if candidate.is_file():
            return candidate
    return None


class Edit:
    """One anchor-and-replacement pair, and the file it edits.

    `path` is as the task wrote it, `target` is where that resolves, and
    `task_line` is the index of the checkbox to tick once the edit lands.
    """

    def __init__(
        self,
        task: str,
        task_line: int,
        ticked: bool,
        path: str | None,
        target: Path | None,
        anchor: str,
        replacement: str,
        line: int,
    ):
        self.task = task
        self.task_line = task_line
        self.ticked = ticked
        self.path = path
        self.target = target
        self.anchor = anchor
        self.replacement = replacement
        self.line = line

    @property
    def where(self) -> str:
        return f"task {self.task}" if self.task else f"tasks.md:{self.line}"


def edits(lines: list[str], change_dir: Path) -> list[Edit]:
    """Every anchor-and-replacement pair in a `tasks.md`, in file order.

    **File order is the applying order**, and it is not an implementation
    detail. A change whose later sections repair what its earlier sections wrote
    anchors those tasks against post-change text — `construction-components`
    says so in its own preamble — so an anchor is only guaranteed to match after
    everything above it has landed.

    A fenced block that no `with:` follows is not an edit. Preambles quote
    example blocks, and a spec delta is a fenced block with no replacement; both
    are skipped rather than guessed at.
    """
    found: list[Edit] = []
    parsed = blocks(lines)

    for index, (line_no, lead, body) in enumerate(parsed):
        if not lead.endswith("with:") or index == 0:
            continue

        anchor_line, anchor_lead, anchor = parsed[index - 1]
        if anchor_lead.endswith("with:") or not anchor.strip():
            continue

        owner = owning_task(lines, anchor_line - 1)
        path = target_for(lines, anchor_line - 1)

        found.append(Edit(
            task=owner[1] if owner else "",
            task_line=owner[0] if owner else -1,
            ticked=bool(owner and owner[2]),
            path=path,
            target=resolve(path, change_dir) if path else None,
            anchor=anchor,
            replacement=body,
            line=anchor_line,
        ))

    return found
