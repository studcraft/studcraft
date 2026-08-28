# Design — An image reaches the clear-opening rule

## Decision 1 — The embed is placed by the script, not typed

`scripts/insert_images.py --write` — landed on `main` via #144, archived at
`openspec/changes/archive/2026-08-27-add-image-to-core-rule/` — writes the
embed. Placing it is mechanical: which rule, which file, which line, and the
answer is already in `assets/IMAGES.md`. Typing it by hand is the transcription
defect the script was built to remove, and `.claude/rules/assets.md` routes a
by-hand placement back to the index first.

`--write` runs on this branch because it edits `docs/`. The script is handed
nothing about which change it serves — it reads the index and acts on whatever
it finds — so the only thing it can check is that the branch names *some*
unarchived change (the archived `add-image-to-core-rule` `design.md`,
Decision 3). This branch is named for this change's directory, which satisfies
that and is what `openspec/config.yaml` requires anyway.

## Decision 2 — The entry is left unchanged, and that is the maintainer's call

`assets/IMAGES.md`'s four-step flow puts a maintainer reading between the drawn
file and the proposal (step 2), and step 3 states plainly: where the image and
the entry disagree, "the maintainer decides which of the two changes".

They disagree. `CMP-018`'s *What it must show* column instructs the illustrator
to dimension the frame's nominal aperture, to draw the clear-opening measurement
around the hinged element and label it, and to dimension it against the model.
The drawn image carries none of those as a drawn annotation. It shows a doorway
with a hinged door hanging part-way across it, twice, a minifig on its base at
each, and pass versus no-pass marked by the signage above.

**The maintainer's decision: the image is representative, and the entry is not
changed.** The reasoning is the ruleset's own. A minifig on its `4 × 3` base
(`INF-001`) at the height it stands is one Unit Base (`CORE-001`: `4 × 3 × 13`
plate layers). That Unit Base either passes the clear opening the hinged element
leaves, or it does not — which is exactly `CMP-018`'s check, "at least as wide
as the model's front edge and as tall as the model stands", read off the model
rather than off a dimension line. Measuring by the state of the build is this
repository's idiom (the archived `add-image-to-core-rule` `design.md`,
Decision 14; `system/design-process.md` reaches for the model before the
notation).

**This proposal makes no claim that the entry's text now describes the drawn
image** — it does not, and rewriting it to match is a separate editorial act the
maintainer chose not to take here. The *What it must show* column was an
instruction to whoever drew the image (`assets/IMAGES.md:18`); the image is
drawn and accepted, and the entry stays as the record of what was asked for.

## Decision 3 — The non-`docs/` file this branch carries

`assets/images/cmp-018-clear-opening.png` — the drawn image itself. It is the
only non-`docs/` path this branch adds besides its own change directory.
`system/repository-strategy.md` ("Branch Naming") requires a ruleset branch to
name such a file and say why: this one cannot be placed without being present,
and the whole change is placing it. It carries the name
`assets/IMAGES.md` has listed for the `CMP-018` entry since the entry was
written, so no rename is needed (unlike `CORE-001`'s file, which arrived
misnamed — the archived `add-image-to-core-rule` `design.md`, Decision 11).

## Decision 4 — The change is named for its outcome

`add-image-to-clear-opening-rule`, parallel to `add-image-to-core-rule`.
`openspec/config.yaml` requires one dedicated branch per proposal, and a name
matching the change directory is the only mechanical check of that.

There is no machinery this time — #144 built it. What ships is an image in a
rule.
