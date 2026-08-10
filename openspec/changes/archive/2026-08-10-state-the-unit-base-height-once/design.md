# Design — State the Unit Base's height once

## Context

`unit-base-is-a-volume` (#73) turned the Unit Base from a 4 × 3 plate into a volume,
`4 × 3 × 12`. It gave the height an owner (`CORE-001`) but left every pre-existing
restatement of it standing, because the restatements were true and the change was
already large. `infantry-occupies-a-unit-base` (#79) then removed the wording that
confused the volume with a physical plate, again without touching the figures.

This change finishes that sequence on the vertical axis: the height is stated where
the unit is defined or introduced, and referred to everywhere it is used.

---

## Decision 1 — what replaces a figure, and the vocabulary is closed

Three phrasings, each for a different reading of the volume. `CORE-001`'s projections
table already names them; this change uses its vocabulary rather than inventing any.

| Where | Replacement | Why this one |
|---|---|---|
| Clearance inside a compartment (`TRN-003`, `TRN-019`, `TRN-020`, the transport Summary, `VEH-028`, the glossary's *Interior Clearance*) | **one Unit Base of clear height** | These read **the volume itself** — `CORE-001`'s row for "transport capacity and interior space" |
| The slice budget (`TRN-013`, the glossary's *Slice*) | **the Unit Base's height** | A budget is a scalar, not a face |
| An opening (`CMP-018`) | **the Unit Base's vertical projection** | `CORE-001`'s own name for the reading an opening takes, which `CMP-018` already used |

**Exactly these three forms, everywhere.** An earlier draft produced five surface
forms for the first row alone — "one Unit Base of clear height", "a full Unit Base of
clear height", "the full Unit Base of clear height", "one Unit Base of clearance" and
a bare "one Unit Base" — which is the drift this change exists to remove, reintroduced
by the change itself. `tasks.md` uses the exact string in every replacement, and
verifications 9.6, 9.7 and 10.7 count every occurrence of it, and of each banned
variant, rather than a sample.

**Never a bare "one Unit Base" for a clearance.** A clearance is a height; a Unit Base
is a volume. "A compartment shorter than one Unit Base" compares a height to a volume
and reads as sloppy in the two places a reader is most likely to meet it first — the
document Summary and the glossary. Both keep "of clear height".

**Not "the vertical projection" for clearance either.** `CORE-001` defines the
vertical projection as `4 studs by 12 plate layers` — a face, taken across the front,
for deciding what passes through a doorway. Using the doorway's word for a compartment
height would be a second meaning for a term that currently has exactly one.

**`UB` is not a unit of height.** `TRN-020`'s replacement table writes its cells as
"one Unit Base of clear height" and "two Unit Bases + 1 plate", not `1 UB` and
`2 UB + 1 plate`. In the same document `UB` already means a capacity (`8 UB`) and a
footprint (`2 × 4 UB`); a third meaning inside a Height column, where `2 UB + 1 plate`
reads as a volume added to a plate, is exactly the collision the paragraph above
avoids.

---

## Decision 2 — `TRN-020` loses its formula

`12N + (N − 1) plate layers` is arithmetic on a number that lives in another
document. What a builder needs is stated directly instead: one Unit Base of clear
height per level, plus what each floor above the lowest actually measures — one plate
at its thinnest.

The table stays, because three worked cases are a convenience the rule earns, and
loses two of its three columns. `Plate layers` was the formula evaluated; `Bricks` was
that column divided by three. Both are `CORE-001` arithmetic, and `CORE-001` already
says "Twelve plate layers is therefore exactly 4 bricks" — a builder who wants the
brick count has one multiplication and one owner to get it from, instead of a second
table that must be kept true.

**The worked example is generalised, and that is a correction as well as a
rewording.** `TRN-020` currently says "a vehicle exactly 8 bricks tall does not hold
two levels. It is one plate short." Eight bricks is 24 plate layers and two levels
need 25, so the arithmetic is right — but the rule measures "above the lowest interior
floor" and the example measures a whole vehicle, hull included. *An interior exactly
two Unit Bases tall* measures what the rule measures, and stays correct at any height:
two levels always need two Unit Bases plus the one plate of the floor between them.
Checked at both heights — 24 against 25 today, 26 against 27 after the height changes.

---

## Decision 3 — the fractions go; vertical overflow is left open, deliberately

`TRN-013`'s `Space` column held `⅓ UB` for a 4-plate crate, `⅔ UB` for an 8-plate
pallet, `1 UB` for a 12-plate drone. Every value is the `Height` column divided by
12. Nothing in the ruleset says so, and no player measures a third of a Unit Base.

The column is removed. `Footprint` and `Height` stay **untouched, plate counts
included**: a crate's height is read from the crate, and it is the input the slice
rule consumes. An earlier draft also rewrote the drone, motorbike and walker heights
from `12 plate layers` to "one Unit Base", which would have replaced three measured
values with a reference — Principle 1 in reverse, in the one column of the one table
whose whole job is to be read off the model.

`TRN-019`'s "three quarters of a Unit Base per position" goes the same way, and
becomes *a partial Unit Base*, which is `TRN-003`'s existing term for exactly this.

**What happens when cargo exceeds one Unit Base of height is not settled here.** An
earlier draft added one sentence to `TRN-013` — "Cargo whose slices exceed it takes a
second Unit Base" — and it does not survive contact with `TRN-003`. Capacity is
counted from floor positions: "Count the Unit Bases its floor holds, then check its
clearance". A position with more clearance than one Unit Base is still one position,
and `TRN-020` requires a real floor before a second one exists. So there is no second
Unit Base for a 16-plate-layer crate to take, and the sentence would have charged a
capacity the compartment has no way to supply.

The question is real and the ruleset does not answer it: a compartment with two Unit
Bases of clearance and no intermediate floor holds one Unit Base of capacity per floor
position, and a crate taller than a Unit Base fits physically while fitting nothing
the rules count. Answering it means deciding whether clearance above one Unit Base
yields capacity without a floor — which is a mechanical change to `TRN-003` and
`TRN-020`, not a rewording, and this change makes none. Recorded here so it is
proposed rather than rediscovered.

---

## Decision 4 — where a figure legitimately stays

The line: **the figure appears where the unit is introduced or defined, and nowhere
where it is used.**

- **`CORE-001`.** It is the definition. All three occurrences stay, including both
  projection rows.
- **`14-glossary.md`, *Unit Base*.** A glossary entry that says "see `CORE-001`" and
  nothing else is not a glossary entry. The repository's own entries restate values
  where the value *is* the definition (*Weapon Range*: "equal to Weapon Length × 6").
  The two entries that lose the figure — *Interior Clearance* and *Slice* — are not
  defining the Unit Base; they were quoting it.
- **`01-foundations.md`, `README.md`, `CODE_OF_DESIGN.md` (Principle 7).** All three
  state the dimension line and immediately name `CORE-001` as the authority. An
  earlier draft removed the figure from `01-foundations.md` alone, on the grounds that
  its pointer conceded the line above it was a copy. That was wrong twice over. The
  same argument applies verbatim to `README.md` and `CODE_OF_DESIGN.md`, which carry
  the same line and the same deferral, so the draft would have left one repository
  solving the same problem two ways. And within `01-foundations.md` itself, the very
  next section states `**3 Action Points (AP)**` and then defers to `CORE-006` — the
  overview's shape is "headline value, then the authority", and the Unit Base would
  have become the one entry with no value.

An introduction that names its authority in the next breath is not the drift this
change is about. A rule that quotes a figure it does not own is.

---

## Decision 5 — `CMP-018` and `CORE-001` stop citing each other

`CORE-001` derives the height from a minifigure "about 4 bricks from its feet to the
top of its head (`05-construction-components.md`, CMP-018)". `CMP-018` states "A
minifigure on its base stands about 4 bricks tall, which is where those 12 plate
layers come from", citing `CORE-001`. Two statements of one fact, each pointing at
the other as its source, and they do not agree: one measures the minifigure, the other
the minifigure on its base, and those differ by exactly the plate the follow-up change
is about.

`CORE-001` owns the derivation. Its outbound citation to `CMP-018` is removed and its
sentence is otherwise untouched; `CMP-018` keeps only what is its own job — that an
opening must be at least as clear as what passes through it — and points at
`CORE-001`.

This is what makes the follow-up change small: after it, exactly one sentence in the
ruleset says where the Unit Base's height comes from.

---

## Decision 6 — `assets/IMAGES.md` is in scope, in two places

`assets/IMAGES.md` specifies images the ruleset needs. Two of its entries quote text
this change rewrites:

- The **`TRN-020` rejection** turns on "the stacking is arithmetic … N levels need
  `12N + (N − 1)` plate layers". The formula is deleted from the ruleset by this
  change, so the rejection would cite text that no longer exists — a dangling
  reference of exactly the class `system/proposal-review.md` lists first. The
  rejection itself is unaffected and stays: stacking is still arithmetic, and
  `VEH-028` still works the answer out in its own text.
- The **`TRN-019` image brief** instructs an illustrator to draw "a bare floor with 12
  clear layers to the roof" and "the 12 layers it needs" above a bench. Task 5.9
  rewrites the bench sentence in `TRN-019` itself, so the brief would be drawing a
  rule the ruleset no longer states. `assets/IMAGES.md`'s own standard for that column
  is that it must be enough for someone who has not read the rule to produce a correct
  drawing — a brief that contradicts the rule fails it.

The `CORE-001` image entry is **not** touched. It dimensions the volume and marks the
plate as floor outside it: that is the figure and the measurement plane, and both
belong to the change that moves them.

**No CI gate restricts `assets/`.** `branch-naming.yml` checks the shape of the branch
name and, when `docs/*.md` changed, that the name matches the single OpenSpec change
directory touched; it constrains no other path. `docs-require-proposal.yml` requires
the proposal, which exists. The one standing requirement is
`.claude/rules/assets.md`'s — re-run `scripts/lint_ruleset.py` after touching
`assets/`, which verification 9.6 does.

---

## Why no spec delta

`openspec/specs/unit-base/spec.md` states the same requirements this change edits the
prose of — the height, the projections, the slice budget — and none of them changes.
A `MODIFIED` block that reworded the spec to match the docs' new phrasing would assert
a requirement change that did not happen, and `scripts/check_delta_coverage.py`
measures deltas against the living spec, not against `docs/`.

The next change does need deltas: three requirements in
`openspec/specs/unit-base/spec.md` carry the figure, and a fourth in
`openspec/specs/weapon-capacity/spec.md` does ("the Unit Base's 12 plate layers of
height are not considered") — four deltas across two capabilities, and
`system/proposal-review.md`'s note on archiving order applies to the pair. Written
here so the omission reads as a decision rather than an oversight.

---

## Rejected

**Doing this together with the change from 12 to 13.** One PR, one proposal, half the
ceremony. Rejected: every sentence this change rewrites is a sentence that change
would rewrite, so a combined change edits each one once but audits a mechanical
dimension change and a repository-wide rewording as a single diff. Separated, the
second change is small enough to read in one sitting — which is where
`system/proposal-review.md` says the findings actually are. The order is also not
reversible: doing the number first means touching fifteen figures that this change
then deletes.

**Converting movement, ranges and Resistance to Unit Bases.** `MOVE-004`'s 12 studs
would become "3 base widths or 4 base depths" depending on the axis, `WPN-005`'s
Range × 6 would lose its arithmetic entirely, and `DMG-003`'s Resistance measures
material thickness, which is not a volume anyone occupies. The Unit Base expresses
the space a thing takes; studs express distance and plate layers express material.
Both readings already exist in `CORE-001`'s projections table, and collapsing them
would make the ruleset less physical, not more.

**Removing the `Height` column from `TRN-013`'s cargo table along with `Space`.** It
looked like the same kind of derived value. It is not: a crate's height is read from
the crate, and it is the input the slice rule consumes. Only the column that divided
it by 12 goes. See Decision 3 for the related draft that rewrote three of its cells
and was dropped for the same reason.

**Keeping `⅓ UB` but writing it as `4/13` after the next change.** Considered and
rejected in advance, because it will be the obvious repair when someone notices the
fractions are gone. A thirteenth of a Unit Base is not a quantity any rule needs, any
player measures, or any model shows. The sum-against-a-budget rule replaces all of
them.

**Giving "partial Unit Base" a glossary entry.** It now appears in `TRN-003` and
`TRN-019`, and `TRN-019`'s use cites `TRN-003`, which defines it in place. Two sites
with a citation between them is below this repository's bar for a term; a third
unaccompanied use would clear it.

---

## Decision 7 — what the audit of the applied text changed

The applied text was audited before the pull request was opened, and five of its
findings were defects in this proposal's own replacement wording rather than in the
transcription. `tasks.md` section 10 carries the repairs; the reasoning is here.

- **`TRN-019`'s new opening pre-empted its second paragraph.** Task 5.8 replaced the
  deleted figure with a statement of where clearance is measured from — the very thing
  the next paragraph owns, and in narrower words: "the surface a model stands on"
  against "stands **or sits** on". Removing a tautology by introducing a duplication is
  not a repair. The premise the sentence needs ("what must fit is the Unit Base") is
  already in the clause before it.
- **`TRN-020` stated the floor cost three times in four sentences.** Two of the three
  existed to introduce and explain the formula. With the formula gone they restate the
  sentence between them, so the introduction loses its clause.
- **A table header called a floor plate "clear height".** `| Levels | Clear height
  needed above the lowest interior floor |` — but its values include the intermediate
  floors, which are solid. Read literally it demanded a plate more than the rule does,
  and it gave a second meaning to a term the glossary defines. Decision 1 refuses that
  for "vertical projection" and then did it to "clear height" one decision later.
- **A banned variant survived in the glossary and was recorded as correct.** Task 7.3
  confirmed *Cargo Bay*'s "less than one Unit Base of clearance" as already-sanctioned
  phrasing. It is one of the five forms Decision 1 names and bans, six entries from
  *Interior Clearance*, which states the same threshold properly.
- **The `TRN-019` image brief lost its number.** It requires "every clear height
  dimensioned in plate layers" and then, after task 8.2, named no plate count. The
  brief now says where the figure lives.

The blocker the audit opened with is a git one, not a text one: the applying agent's
scope was the paths `tasks.md` names, so `proposal.md` and `design.md` stayed
untracked, and `Docs require OpenSpec proposal` tests the checkout. They are committed
in a second commit rather than amended into the first — `system/repository-strategy.md`
allows only forward.

---

## Handover — three things the follow-up change must not rediscover

1. **`VEH-028`'s two derivations and the glossary's *Maximum Height*.** "4 plate
   layers for every stud" is `12 ÷ 3`; "one Unit Base of height for every two studs"
   and "half a Unit Base" both read 6 as half of 12. At 13 none of the three divides,
   and `VEH-028`'s "half as much again" no longer lands on 6. This needs a decision
   about the multiplier, not a rewording — which is why it was deferred, and why
   deferring it leaves one rule visibly stating figures in two styles.
2. **`TRN-013`'s drone, motorbike and walker rows.** All three are 12 plate layers
   because they were chosen to equal a Unit Base's height, and the `Space` column that
   said so is gone. At 13 they quietly stop illustrating "cargo as tall as a Unit
   Base". They are measured values and correct as they stand; the follow-up should
   decide whether the example is still the example it wants.
3. **Four spec deltas, two capabilities** — three requirements in
   `openspec/specs/unit-base/spec.md` and one in
   `openspec/specs/weapon-capacity/spec.md`.
