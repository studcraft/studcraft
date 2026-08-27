# An image reaches the rule that asked for it

## Why

`assets/IMAGES.md` has specified example images since `Add assets/IMAGES.md and
TODO.md` (#45). It says which rules need one, what each must show, and why the
prose cannot carry the fact alone. **Twenty images are specified and none had
been drawn.** The first one arrived as `assets/images/core-001-unit-base.png`,
untracked in the working tree, and there was nothing in this repository that put
it anywhere.

The index specifies. Nothing places. Closing that gap by hand is the defect
class this repository already pays scripts to avoid: `scripts/apply_tasks.py`
exists because a human transcribing a mechanical edit is where the errors come
from, not the deciding. Placing an image is mechanical in exactly the same way —
which rule, which file, which line — and the answer is already written down.

There is a second reader. **The images are drawn elsewhere**, by a process
outside this repository, and that process needs a machine-readable answer to
four questions: which rule, what to draw, under what filename, and where the
result lands. `.studcraft/index.json` answers the fourth today (`doc` plus the
rule's span) and none of the first three, because it has never read
`assets/IMAGES.md`.

Nothing mechanical connects the three places an image lives, either. `docs/`,
`assets/images/` and `assets/IMAGES.md` can disagree in every direction and
`scripts/lint_ruleset.py` sees none of it: `check_image_index` validates the
index against `docs/`, and never looks at the disk. `three image entries
describe rules that moved on` (#141) found its three by reading, which is the
only way there was.

## What Changes

### `docs/02-core-rules.md`: `CORE-001` gains its image

One line, at the end of the rule's body:

```
![CORE-001 — unit base volume](../assets/images/core-001-unit-base-volume.png)
```

**No rule text changes.** This proposal states no rule, retires no ID and moves
no citation. It is the only reason it touches `docs/` at all, and the reason it
is a proposal rather than a branch.

### `scripts/insert_images.py` — new

The placement process. Reads `assets/IMAGES.md`, resolves each entry to a
section in `docs/`, and makes the embeds agree with it.

One rule governs the whole script:

> An embed exists in `docs/` exactly when the file exists in `assets/images/`
> **and** `assets/IMAGES.md` lists it for that section.

Anything else is deriva, in one of three directions, and the script names it:
a file on disk with no entry, an entry whose file is drawn but not embedded, an
embed whose file or entry is gone.

Two modes:

- `--check` — reports, writes nothing, exits non-zero on any disagreement. The
  default, and what CI runs. It is green exactly when `--write` is a no-op: a
  rewrite nothing reported is itself reported, so the gate cannot be quiet about
  an edit the writer would make.
- `--write` — makes the change. Run by hand, on a proposal branch, because the
  files it edits are under `docs/`.

`--check` prints the remedy, not only the complaint. For an embed with no entry
it prints the `assets/IMAGES.md` row ready to paste, and says so when the rule
sits in that file's rejected list.

### `scripts/images_index.py` — new, and the only parser of the index

`assets/IMAGES.md` had one reader and now has three. Its parsing moves out of
`scripts/lint_ruleset.py` into a module the three share, so that what an entry
*is* has one definition — the argument `scripts/repo.py` makes about the rule-ID
pattern and `scripts/tasks_format.py` about the anchor format.

`lint_ruleset.py` keeps the checking, which was always its half. `check_image_index`
is unchanged in what it reports.

### `scripts/build_index.py` — the index carries what the images need

Every document gains an `images` list: `anchor`, `path`, `exists`, `must_show`
and `why` per entry, in table order. Every rule that has one gains an `images`
list of paths.

The document carries the prose because an entry may name a heading (`# Terrain`)
rather than a rule, and there is no rule to hang it on. The rule carries paths
only, because a second copy of the two prose columns is a second thing to keep
true.

That is what the drawing process consumes: clone, run
`python3 scripts/build_index.py`, read `.studcraft/index.json`.

### `scripts/preflight.py` — `--check` joins the local mirror

Thirteen checks instead of twelve. A push should not be the first thing to
report a disagreement the working tree already has.

### `.claude/rules/assets.md` — the rule states the new process

That file names which script checks the index and says to run it. There are two
commands now, and one of them writes.

### `.github/workflows/docs-ruleset-linter.yml` — one step

`python3 scripts/insert_images.py --check`, added to the existing
`Docs ruleset linter` job. **No new required check** — a new one has to be
enabled in branch protection to block anything, and a required check that never
fires blocks a merge forever (`system/ci-gates.md`).

### `assets/`

- `core-001-unit-base.png` is renamed to `core-001-unit-base-volume.png`, the
  path the index has named since `Add assets/IMAGES.md and TODO.md` (#45).
- The line saying none of the listed files exist yet stops being true with the
  first one. It is replaced by the placement rule itself — including that an
  embed with no entry is removed, which is the behaviour a contributor placing
  one by hand meets, in the file they are reading. `.claude/rules/assets.md`
  points at it rather than restating it.
- The paragraph closing "Both were stale" now closes a list of five.
- **The four steps an image goes through** are written down: check, read the
  image against its entry, ask the maintainer, then propose. The order is the
  point — this change got it wrong, and the section says so.
- **`CORE-001`'s entry narrows to the image that was drawn.** It asked for three
  panels; the render is one — the volume, its three dimensions, and the two
  measures laid beside it. The entry now asks for that, and its *Why* column
  argues for it rather than for panels nobody drew. What the narrowing costs is
  recorded in the file: two facts, the base inside the volume and the footprint
  arithmetic, are prose-only from here. `design.md`, Decision 14.

### `tests/`

`tests/test_insert_images.py` is new — nineteen cases covering all three
directions of deriva, both modes, several images on one section, a section whose
heading is not a rule ID, both refusals, and the two document shapes that made
an earlier version write documents nobody asked it to.
`tests/test_images_index.py` is new and takes the three parser cases that were
in `tests/test_lint_ruleset.py`, plus the two kinds of entry and the alt text.
`tests/test_lint_ruleset.py` gains eight cases for `check_image_index`, which
had none. `tests/test_build_index.py` gains the `images` key.

## Non-Goals

- **The other nineteen images.** They stay specified and undrawn. This change
  builds the road and drives one thing down it.
- **`check_image_files` in `scripts/lint_ruleset.py`.** An earlier draft added
  one. `--check` proves the same facts, and two checkers of one property drift
  apart silently — the argument `scripts/repo.py` already makes. What
  `lint_ruleset.py` checks is unchanged: `check_image_index` still validates the
  index against `docs/`, which is a different property. Only where it gets its
  entries from moves.
- **A `--prune` flag** to gate deletion. `design.md`, Decision 6.
- **Any rule change.** See above.
