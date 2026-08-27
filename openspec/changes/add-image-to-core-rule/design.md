# Design — An image reaches the rule that asked for it

## Decision 1 — One branch, carrying thirteen files outside `docs/`

`system/repository-strategy.md` (Branch Naming) allows it and states the
condition: *"A ruleset branch may also carry a non-`docs/` file only if its
`design.md` says which and why."* It also says what the alternative costs —
*"Shipping a pointer the change knows is broken so the file set stays pure is
worse, and nobody has chosen it."*

The files, and why each has to be here:

| File | Why it cannot wait |
|---|---|
| `scripts/insert_images.py` | It produces the embed. Without it the `docs/` edit is a hand transcription, which is the thing this change exists to remove. |
| `scripts/images_index.py` | The index gets two more readers here, so its parsing has to stop belonging to one of them. Decision 12. |
| `scripts/lint_ruleset.py` | Loses that parser and imports it. Its checks are unchanged. |
| `scripts/build_index.py` | The `images` key. It is what the drawing process reads, and it reads `assets/IMAGES.md`, which this change edits. |
| `scripts/preflight.py` | The local mirror gains `--check`. `.claude/rules/tooling.md`: editing a workflow means checking the mirror against it. |
| `.github/workflows/docs-ruleset-linter.yml` | The `--check` step. A checker landing a release later than the thing it checks is a window where deriva is invisible. |
| `.claude/rules/assets.md` | It names the script that checks images and says to run it. There are two commands now, one of which writes. |
| `AGENTS.md` | One row routing to `assets/IMAGES.md`. The image flow starts with a file appearing in `assets/images/` — a `git status` line, not an edit — so the path-triggered rule above never fires for it, and `AGENTS.md` is the only thing always loaded. It routes; it does not restate. |
| `assets/IMAGES.md` | Its statement that no listed file exists is falsified by this change. |
| `assets/images/core-001-unit-base-volume.png` | The image itself. |
| `tests/test_insert_images.py`, `tests/test_images_index.py`, `tests/test_build_index.py`, `tests/test_lint_ruleset.py` | `Tests` is a required check, and `.claude/rules/tooling.md` puts a script's test in the same commit as the script. |

**The split was considered first and is broken, not merely tidier.** Two pull
requests — machinery on a kebab-case branch, the embed on a proposal branch —
puts the rename and the new checker in the first one and the embed in the
second. The first therefore contains a drawn file, listed in the index, with no
embed in `docs/`: exactly the state its own new check reports as a failure. The
machinery PR goes red on itself. Purity of the file set bought a red gate.

## Decision 2 — The embed goes in `docs/`, not only in the index

The alternative: leave `docs/` untouched, let `assets/IMAGES.md` remain the only
record, and let whatever renders the ruleset elsewhere pair them up.

Rejected on the index's own terms. `assets/IMAGES.md:26` says the *Why text
alone is not enough* column is *"what a reviewer checks when deciding whether the
entry belongs at all"* — the entry's whole justification is that a reader of the
rule cannot picture the fact. A reader of the rule is a reader of `docs/`. An
image that reader has to know about and open by hand does not serve them.

It also leaves nothing to check. With the embed, three artifacts must agree and
a script can say when they do not. Without it there are two, and the second is
optional.

## Decision 3 — `--check` by default, `--write` by hand

The script edits `docs/`, and `system/workflow.md` is unconditional: every
change to a `docs/*.md` file goes through a proposal first. A script that
rewrites `docs/` wherever it runs is a way around that rule, and it would be
used as one.

So the writing mode is explicit and manual, and the mode that runs everywhere
only reports. CI gets the detection; the proposal branch keeps the authority to
edit. `.claude/hooks/guard_repo_edits.py` does not close this — it intercepts an
agent's edit tools, not a Python process writing a file. **The protection is the
branch and the gate, not the script**, which is what `.claude/rules/tooling.md`
already says about local checks generally.

**The branch check is weaker than `apply_tasks.py`'s, and knowingly.** That
script is handed the change it is applying and can require the branch to be that
change. This one is handed nothing — it reads `assets/IMAGES.md` and acts on
whatever it finds — so it can only ask whether the branch names *some* unarchived
change. Running it from an unrelated proposal's branch therefore places images
into that proposal's pull request.

What keeps that small is Decision 13: the script writes a document only when it
places or removes an image in it, so the blast radius is the images the index
lists and nothing else. The rest is the pull-request diff, which is where a
change carrying an edit it never proposed is meant to be caught.

## Decision 4 — An embed exists exactly when file and entry both do

The single biconditional in `proposal.md`. Both halves matter and they fail
differently:

- **File drawn, entry present, no embed** — the image exists and nobody sees it.
  This is today's state, for one file.
- **Embed present, file gone** — a broken image in the rulebook.
- **Embed present, entry gone** — an image with no recorded argument for
  existing. `three image entries describe rules that moved on` (#141) is the
  precedent: entries drift from the rules they describe, and only a reader
  caught it.

Stating it as one rule rather than three checks means there is one thing to
verify and one thing to argue with.

## Decision 5 — Deleting an unlisted embed is the correct default

This is the case the maintainer raised: someone places an image by hand,
believing it belongs, without writing the entry. `--write` deletes it.

That is right, and the reason is not the script. `assets/IMAGES.md:5` makes
entries selective by design — *"A rule only appears here if the rule is a
spatial or geometric fact"* — and `.claude/rules/assets.md` makes that file the
only place the specification is written. An embed with no entry is an image whose
argument was never made. The remedy is two table cells, and those two cells are precisely
what a reviewer needs.

The deletion is safe because of where it happens: `--write` runs on a proposal
branch, so every deletion appears in a pull-request diff and is read by a person
before it merges. `--check` in CI reports it earlier still.

**What makes it not hostile is the message.** `--check` prints the row to paste
and, when the rule is in the rejected list, points at the reclassification ritual
`assets/IMAGES.md:32` requires — struck through, marked, with what changed. The
door stays shut with the key beside it.

## Decision 6 — No `--prune`

Considered: make `--write` refuse to delete an unlisted embed unless a second
flag says so.

Rejected. The deletion is already gated by human review of a pull-request diff
(Decision 5). A second lock on the same door gets trusted *instead of* the
review, rather than as well as it. It is also a second policy surface over one
property, which is the mistake `Non-Goals` records for `check_image_files` — and
a flag used once a year is used wrongly.

## Decision 7 — Placement is the end of the section's own prose

Not the end of its span. `scripts/ruleset_ast.py` gives a section a `line_end`
that includes its sub-headings, which is right for citation scanning and wrong
here: `# Terrain` in `docs/17-infantry.md` spans `INF-006` through `INF-009`, so
its span ends after four rules. The image belongs under the Terrain prose,
before `## INF-006`.

The rule that covers both cases: **the image goes after the section's last line
before its first child heading, or at the end of its body when it has none.**
For a leaf rule such as `CORE-001` those are the same line.

The script imports `ruleset_ast` for this rather than matching headings itself,
for the reason `build_index.py`'s own docstring gives about hand-rolled
structure: *"a second, silently disagreeing answer to the question
`ruleset_ast.py` already answers once."*

## Decision 8 — Several images per section, ordered by the table

`check_image_index` already permits it: it rejects a repeated *path*, never a
repeated Rule cell. Two rows naming `CORE-001` with different slugs pass today.

So `images` in the index is a list, the embeds are written in the order the
table lists them, one blank line apart, and the script never reorders. The table
is the source; ordering it is an editorial act and belongs to whoever edits it.

## Decision 9 — Identity is the path; the alt text is derived from the slug

The script recognises its own embeds by the image path, so an embed already
present is left in place rather than duplicated.

The alt text is normalised on every run, derived from the filename's slug:
`core-001-unit-base-volume.png` gives `CORE-001 — unit base volume`. The obvious
alternative, the rule's title, was rejected by Decision 8: two images on one rule
would carry identical alt text, which is the case where alt text matters most.

Normalising rather than preserving means a hand-edited alt is overwritten. That
is the same trade as everywhere else here — the generated text has one definition
— and it is visible in the diff.

## Decision 10 — A step on the existing job, not a new required check

`system/ci-gates.md` records both halves of this: a required check that never
fires blocks the merge forever, and a new check does nothing until branch
protection is changed, which is an admin action outside this pull request.

Adding `--check` as a step of the existing `Docs ruleset linter` job inherits a
gate that is already required and already runs on every pull request with no
`paths:` filter. The job name does not change, so protection stays valid.

## Decision 11 — The file is renamed, not the entry

`assets/images/core-001-unit-base.png` was drawn; `assets/IMAGES.md` has named
`core-001-unit-base-volume.png` since `Add assets/IMAGES.md and TODO.md` (#45). One of the two moves.

The entry stays. Its slug describes what the panels show — a volume — and
`assets/IMAGES.md:42` requires the slug to describe *"the content shown, not the
rule's title"*. `CORE-001` is titled *Unit Base*, so `unit-base` is the title and
`unit-base-volume` is the content. The index had it right.

## Decision 12 — One parser of `assets/IMAGES.md`, in a module of its own

`lint_ruleset.py` had the only parser because it was the only reader. This
change makes three, and the alternative to moving it is `insert_images.py`
importing the linter, or writing a second parser.

Importing the linter is wrong on direction: a placement script does not depend
on a checker. A second parser is worse, and this repository has already written
down why twice — `scripts/repo.py` on the rule-ID pattern, `scripts/tasks_format.py`
on the anchor format, both saying that the second copy drifts and the drift is
silent. A checker and a placer disagreeing about which rows are entries would
place an image the checker never validated.

So `scripts/images_index.py` owns the parse and the shape of an entry — which
kind it is, what prefix its filename must carry, what alt text it produces —
and the three readers own what they do with it. `lint_ruleset.py` keeps its
checks unchanged; only where its rows come from moves. The three parser cases in
`tests/test_lint_ruleset.py` move to `tests/test_images_index.py` with it.

## Decision 13 — The script writes a document only to place or remove an image

Found by `proposal-auditor` on the first draft, and it was a blocker. The
rewrite was built by rebuilding each section and re-joining the file, and two
habits rode along with it: a trailing newline was added where the file had none,
and blank runs were collapsed wherever they appeared. Every document with an
entry goes through that path, drawn or not. `--write` would have edited five
documents — `05-construction-components.md`, `09-transport.md`, `10-weapons.md`
and `17-infantry.md` besides the intended one — none of them named in this
proposal.

That is the thing `system/workflow.md` forbids outright: a `docs/*.md` change no
proposal describes. It would also have made `tasks.md` false, and the applier
would have hit its own stop condition and stopped, correctly.

Two rules now:

- **Whitespace is the document's, not the script's.** Removing an embed takes
  the blank line that introduced it, because the script wrote that line. Nothing
  else is touched, and the file's trailing-newline state is preserved — seven
  documents in `docs/` end without one.
- **A rewrite nothing reported is itself a finding** (`silent_rewrite`). This is
  the general form, and it is what makes `--check` a real guard: green means
  `--write` is a no-op, whatever a future edit to this script does. Without it,
  `preflight.py` and CI were both green on a tree where `--write` changed four
  unrelated documents — a gate quiet about the very thing it exists to watch.

The second rule is why this is a decision and not a bug fix. The first version
was wrong; a checker that could not see it being wrong was the actual defect.

## Decision 14 — The entry narrows to the image, and says what that costs

`proposal-auditor` compared the drawn file against `CORE-001`'s entry and found
one panel where three were asked for: no model inside the volume, no `2 × 3 UB`
footprint. That finding was right about the image.

**Part of it was wrong.** It reported no dimension or label anywhere. The two
loose pieces beside the stack are the width and the depth, and the alternating
layers are the height — measured by counting elements rather than by drawn
annotation, which is this repository's idiom and not an omission.
`system/design-process.md` reaches for the model before the notation, and
`CODE_OF_DESIGN.md` puts it plainly: the model supplies the values.

The maintainer's judgement, and this decision: the image is representative of a
volume, and a model inside would not make it clearer. So the entry narrows.

**The direction is the risk, and it is why this is written down.** Rewriting an
entry to match whatever was drawn is how an index stops being a specification.
`assets/IMAGES.md:136` records the shape of that failure for `WPN-003` — *"An
image drawn from the entry would have contradicted the rule, which is worse than
a stale argument: the What column is an instruction."* Narrowing is legitimate
here on one condition, and the new *Why* column is written to meet it: **it
still argues for the image that exists, on its own terms**, rather than
inheriting an argument made for panels nobody drew. Thirteen plate layers is a
quantity a reader cannot convert at a glance — the same ground on which this
file already accepts an image for `Terrain (INF-006 – INF-008)`.

What it costs is recorded in `assets/IMAGES.md` itself, in a section of its own,
because that file's whole discipline is that a superseded judgement stays
visible: the base-inside-the-volume fact and the footprint arithmetic are
carried by prose alone from here.

Three rejections lean on this image and were checked against the narrowed
version: `TRN-003`, `TRN-020` and `DEP-003`/`DEP-004` each rest on the
dimensioned volume or on the horizontal `4 × 3` figure, and the render carries
both. Nothing cascades.

## Decision 15 — The change is named for its outcome

`add-image-to-core-rule` — the branch already carries that name, and
`openspec/config.yaml` requires the change directory to match it.

The name understates the machinery, deliberately. The machinery exists so that
this outcome, and the nineteen after it, cost one command each. What ships is an
image in a rule.
