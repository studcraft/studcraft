#!/usr/bin/env python3
"""Write the OpenSpec change that places a drawn image. One command, three files.

The `add-image` skill made every step of a placement mechanical except one:
writing `proposal.md`, `design.md` and `tasks.md`. Two placements have shipped
and their artifacts are the same documents with three nouns changed — the rule,
the document, the filename. Everything else was retyped, and the retyping is
where the wrong expected value comes from: a `tasks.md` that says a command
prints `358 passed` is stale the day a test is added, and an auditor comparing
the two has to decide whether the mismatch matters.

So the numbers this writes are the ones that hold. Where an expectation is
computable and stable — the embed line, the line it follows, how many entries
the index has and how many are drawn — it is computed. Where it would be a
snapshot of something unrelated to images, the task asserts an exit code
instead. `scripts/apply_tasks.py` and `scripts/verify_tasks.py` already treat a
task as a command plus what it should print; this fills that in from the index
rather than from memory.

## What it does not write

**The maintainer's reading of the image against its entry.** That is the one
judgement in the whole flow — the `add-image` skill's step 3, decided at step 4
— and no script has seen the image. `tasks.md` gets a marked placeholder, this
prints it as the work remaining, and `proposal-auditor`'s brief asks about that
entry, so a placeholder that survives to the audit is a finding rather than a
merge.

## What it refuses

It writes under `openspec/changes/`, and `.claude/rules/tooling.md` is explicit
that a `PreToolUse` hook sees `Write` and `Edit` but not a script writing
through `Bash`. So it restates the branch rule for itself, the same one
`insert_images.py --write` keeps: the branch must be named for the change, which
is what `openspec/config.yaml` requires and the only mechanical check of it. It
also refuses to overwrite a change directory that exists.

Usage:

    python3 scripts/propose_placement.py <change-name>

Exit code 0 when the three files were written, 1 otherwise.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import images_index  # noqa: E402
from insert_images import embed_line, own_region, resolve  # noqa: E402
from repo import CHANGES_DIR, DOCS_DIR, git  # noqa: E402
from ruleset_ast import parse_text  # noqa: E402

ARTIFACTS = ("proposal.md", "design.md", "tasks.md")

# The one thing a person still writes. Deliberately loud and deliberately not a
# sentence anyone would leave in by accident.
PLACEHOLDER = "TO BE WRITTEN BY THE MAINTAINER — see below"


PROPOSAL = """\
# {title}

## Why

`assets/IMAGES.md` carries an entry for `{anchor}` specifying an image, and the
file — `{path}` — has been drawn. The entry named that
path when it was written; nothing has placed it.

`scripts/insert_images.py` exists for exactly this. It reads the index, resolves
the entry to its section in `docs/`, and writes the embed. It costs one command.

## What Changes

### `docs/{doc}`: `{anchor}` gains its image

One line, at the end of the rule's body, written by
`scripts/insert_images.py --write`:

```
{embed}
```

**No rule text changes. No `assets/IMAGES.md` entry changes.** This proposal
states no rule, retires no ID, moves no citation and does not touch the index.
It places one image the index already specified, where a reader of the rule will
see it.

### `{path}` — the drawn file

Carries the name the index has given the entry since the entry was written. It
is the only non-`docs/` file this branch adds besides its own change directory.

## Non-Goals

- **Every other specified image.** {undrawn} entr(ies) stay specified and
  undrawn. Each is its own change.
- **Any change to `{anchor}`'s entry.** The maintainer read the drawn image
  against the entry and accepted it, so the entry stands unchanged.
  `design.md`, Decision 2.
- **Any rule change.** See above.
"""


DESIGN = """\
# Design — {title}

## Decision 1 — The embed is placed by the script, not typed

`scripts/insert_images.py --write` writes it. Which rule, which file, which
line: every answer is already in `assets/IMAGES.md`, so placing it is
transcription, and transcription is what this repository removes rather than
delegates.

`--write` runs on this branch because it edits `docs/`. The script is told
nothing about which change it serves — it reads the index and acts on what it
finds — so the only thing it can check is that the branch names some unarchived
change. This branch is named `{change}`, which satisfies that and is what
`openspec/config.yaml` requires anyway.

## Decision 2 — The entry is left unchanged, and that is the maintainer's call

`assets/IMAGES.md` puts a maintainer's reading between the drawn file and the
proposal, and the `add-image` skill states what the answer settles: an accepted
image does not change its entry. The *What it must show* column was the
instruction given to whoever drew the image; it stays as the record of what was
asked for.

The reading itself is `tasks.md`, task 3.1.

## Decision 3 — The non-`docs/` file this branch carries

`{path}` — the drawn image. It is the only
non-`docs/` path this branch adds besides its own change directory.
`system/repository-strategy.md` ("Branch Naming") requires a ruleset branch to
name such a file and say why: this one cannot be placed without being present,
and placing it is the whole change.

## Decision 4 — The change is named for its outcome

`{change}`. `openspec/config.yaml` requires one dedicated branch per proposal,
and a name matching the change directory is the only mechanical check of that.
"""


TASKS = """\
# Tasks — {title}

## How to read this file

**The embed is not typed.** `scripts/insert_images.py --write` writes it; the
applier runs the command and verifies the result. There are no anchor pairs and
no `docs/` edit to transcribe.

The fenced block under task 1.3 is **the line the command must have written**,
not an anchor to paste. `scripts/check_task_anchors.py` cannot tell the two
apart and reports it as a note.

### If a command disagrees with what a task expects

**Stop and report it.** Never edit a document to make a verification pass — that
is the one failure mode this machinery exists to remove.

---

## 1. `docs/{doc}` — {anchor} gains its image

- [ ] 1.1 Run `python3 scripts/insert_images.py --write` from the repository
      root, on this branch. **Do not type the embed by hand**, and do not edit
      `docs/{doc}` in any other way.

      It must report writing **one** document, `{doc}`. More than one
      is a mismatch: only `{filename}` is newly drawn. Stop and report it.

      **If it refuses**, the branch is wrong — the branch and the change
      directory must both be `{change}`. Report it; do not work around it.

- [ ] 1.2 `git diff --stat docs/` — **one file, `docs/{doc}`, two
      lines added, none removed.** More than one file is a mismatch: report it
      and stage nothing.

- [ ] 1.3 `grep -n "assets/images" docs/{doc}` — the embed is present
      exactly once, as:

```
{embed}
```

      It sits directly after `{anchor}`'s last line — `{last_line}` — and before
      the `---` that closes the rule. If it is under the next rule, stop and
      report it.

- [ ] 1.4 `ls -la {path}` — present, and under the 3 MB
      cap `assets/IMAGES.md` sets. Its path and `docs/{doc}` are the two
      paths handed to `git-operator`; **the image is committed with the embed**,
      or `docs/` points at a file that is not in the repository.

## 2. Verification

- [ ] 2.1 `python3 scripts/insert_images.py --check` — must **exit 0** and
      report `{total} image entr(ies), {drawn} drawn`. This is the run CI makes.

- [ ] 2.2 `python3 scripts/insert_images.py --write` a second time — must exit 0
      and print no `Wrote` line at all. A second write that changes something is
      a defect, not a no-op.

- [ ] 2.3 `python3 scripts/check_image_change.py` — must **exit 0** and report
      `1 image file(s), 1 embed line(s) in {doc}`. It is the check that
      refuses a placement which did anything else, `assets/IMAGES.md` first.

- [ ] 2.4 `python3 scripts/lint_ruleset.py` — must **exit 0**, and report the
      same as it does on `main`. An embed is not a citation and not a heading.

- [ ] 2.5 `python3 scripts/check_id_stability.py` — must **exit 0**: no rule is
      added, retired or renumbered by this change.

- [ ] 2.6 `python3 scripts/rule.py show {anchor}` — the body now ends with the
      embed line. Nothing else about the rule changed.

- [ ] 2.7 `.venv/bin/pytest -q` — must **exit 0**, the same as `main`. This
      change touches no script and no test.

- [ ] 2.8 `python3 scripts/preflight.py` — all checks PASS.

- [ ] 2.9 `git status --short` — modified: `docs/{doc}`. Untracked:
      `{path}` and this change directory, both to be
      staged by `git-operator` by name. **`CHANGELOG.md` and every
      `**Version:**` header are untouched, deliberately** — both belong to the
      Release cut. Anything else is a mismatch: report it and stage nothing.

---

## 3. The reading no command makes

- [ ] 3.1 **`{path}` read against the `{anchor}` entry.**
      Decided by the maintainer, which is the only place this decision can be
      made: `insert_images.py` checks that a file exists, never what is in it.

      {placeholder}

      Write here what the entry's *What it must show* column asked for, what the
      drawn image actually shows, and the maintainer's verdict — accepted, in
      which case **the entry is not changed**, or redrawn, in which case this
      proposal does not exist yet.

---

## Coverage

| What changes | Task | File |
|---|---|---|
| {anchor}'s image | 1.1 | `docs/{doc}` |
| The drawn file is present and committed | 1.4 | `{path}` |
| The image against its own entry | 3.1 | (no file — the maintainer's reading) |
"""


class Refusal(Exception):
    """Something that must be true before anything is written, and is not."""


def pending(entries: list[images_index.Entry]) -> list[images_index.Entry]:
    """Every entry whose image is drawn and whose embed is not in `docs/` yet.

    The path is what identifies an embed, matching `insert_images.EMBED_RE` —
    alt text is generated from the entry and may be rewritten, so it cannot be
    the identity here either.
    """
    found = []
    for entry in entries:
        if not entry.exists:
            continue
        document = DOCS_DIR / entry.doc
        if not document.is_file():
            continue
        if f"](../{entry.path})" not in document.read_text():
            found.append(entry)
    return found


def last_body_line(entry: images_index.Entry) -> str:
    """The rule's own last line, which the embed must land directly after.

    Computed rather than described, because "after the rule's last line" is the
    one placement error that leaves a valid-looking document: an embed under the
    following rule illustrates the wrong rule and breaks nothing.
    """
    document = DOCS_DIR / entry.doc
    parsed = parse_text(entry.doc, document.read_text())
    section = resolve(parsed, entry.anchor)
    if section is None:
        return "the rule's last line"

    start, end = own_region(section)
    lines = document.read_text().splitlines()[start - 1:end]
    for line in reversed(lines):
        stripped = line.strip()
        if stripped and stripped != "---":
            return stripped
    return "the rule's last line"


def title_for(entry: images_index.Entry) -> str:
    """What the proposal is called, in this repository's own register."""
    return f"An image reaches {entry.anchor}"


def branch_refusal(change: str) -> str | None:
    """Why this branch must not carry this change, or None."""
    code, branch = git("rev-parse", "--abbrev-ref", "HEAD")
    if code != 0:
        return "could not read the current branch"

    if branch in ("main", "develop"):
        return (
            f"on {branch}. No document change anywhere in this repository is "
            f"committed to {branch} directly — system/workflow.md (Git Workflow)."
        )

    if branch != change:
        return (
            f"on branch {branch}, which is not {change}. A proposal lives on its "
            f"own branch and takes the change's name so the two cannot drift — "
            f"system/repository-strategy.md (Branch Naming)."
        )

    return None


def render(change: str, entry: images_index.Entry, entries: list[images_index.Entry]) -> dict[str, str]:
    """The three artifacts, as text."""
    drawn = sum(1 for other in entries if other.exists)
    fields = {
        "change": change,
        "title": title_for(entry),
        "anchor": entry.anchor,
        "doc": entry.doc,
        "path": entry.path,
        "filename": entry.path[len("assets/images/"):],
        "embed": embed_line(entry),
        "last_line": last_body_line(entry),
        "total": len(entries),
        "drawn": drawn,
        "undrawn": len(entries) - drawn,
        "placeholder": PLACEHOLDER,
    }
    return {
        "proposal.md": PROPOSAL.format(**fields),
        "design.md": DESIGN.format(**fields),
        "tasks.md": TASKS.format(**fields),
    }


def plan(change: str) -> tuple[images_index.Entry, dict[str, str]]:
    """What would be written, or the reason nothing can be."""
    refusal = branch_refusal(change)
    if refusal:
        raise Refusal(refusal)

    change_dir = CHANGES_DIR / change
    existing = [name for name in ARTIFACTS if (change_dir / name).is_file()]
    if existing:
        raise Refusal(
            f"openspec/changes/{change} already holds {', '.join(existing)}. This "
            f"writes a proposal; it does not rewrite one."
        )

    entries = images_index.entries()
    waiting = pending(entries)

    if not waiting:
        raise Refusal(
            "no image is drawn and unplaced. Every entry whose file exists is "
            "already embedded, so there is no placement to propose. "
            "python3 scripts/insert_images.py --check says what the tree looks like."
        )

    if len(waiting) > 1:
        names = ", ".join(entry.path for entry in waiting)
        raise Refusal(
            f"{len(waiting)} images are drawn and unplaced ({names}). One "
            f"placement per proposal: place them one at a time, or say in "
            f"design.md why these belong together and write the change by hand."
        )

    return waiting[0], render(change, waiting[0], entries)


def main(argv: list[str]) -> int:
    if len(argv) != 1:
        print(__doc__.split("Usage:")[1].strip(), file=sys.stderr)
        return 2

    change = argv[0]

    try:
        entry, artifacts = plan(change)
    except Refusal as refusal:
        print(f"Refusing: {refusal}", file=sys.stderr)
        return 1

    change_dir = CHANGES_DIR / change
    change_dir.mkdir(parents=True, exist_ok=True)
    for name, text in artifacts.items():
        (change_dir / name).write_text(text)

    print(f"Wrote openspec/changes/{change}/: {', '.join(ARTIFACTS)}")
    print(f"  {entry.anchor} in docs/{entry.doc}, image {entry.path}")
    print()
    print("One thing is left, and no script can write it: task 3.1, the image")
    print("read against its entry. It carries a placeholder until you do —")
    print(f"  grep -n \"{PLACEHOLDER}\" openspec/changes/{change}/tasks.md")
    print("and proposal-auditor is briefed to ask about that entry, so a")
    print("placeholder reaching the audit is a finding rather than a merge.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
