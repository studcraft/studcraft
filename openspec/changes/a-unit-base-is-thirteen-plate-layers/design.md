# Design — A Unit Base is thirteen plate layers

## Context

`unit-base-is-a-volume` (#73) made the Unit Base a volume and chose 12 plate layers
for its height, reasoning that a minifigure is "about 4 bricks" and that 12 is the
smallest whole-brick height containing it. `design.md` for that change recorded a
Decision 4 — the plate an infantry model stands on is its floor, not part of its
space — which "dissolves the 'is the plate part of the Unit Base?' question rather
than answering it".

The question came back, because the plate travels with the model. This change answers
it: the base is inside.

`state-the-unit-base-height-once` (#80) and `deployment-is-a-volume` (#81) were both
written to make this change small. #80 left the figure in five places instead of
twenty-four; #81 deleted the two derivations that computed with it and would not
divide at 13.

---

## Decision 1 — the measurement, and why it is exact

A minifigure measures **4 bricks** from the soles of its feet to the top of its head,
and the base `SCS-002` requires is **one plate**. 4 bricks is 12 plate layers, so the
model as it stands on the table is **13**.

This is not an approximation dressed up as one. It was verified against an
orthographic render of a minifigure on its base beside a stack of four bricks and one
plate: the two are flush, and their studs align. Measured off the image at 27 pixels
per plate layer — the base plate spans exactly that — the minifigure is 324 pixels
(12.0 plate layers) and the whole model 351 (13.0).

**Reproduce it at the table rather than trusting that.** The render is not in the
repository, and an auditor cannot recompute a measurement from a file that is not
there. Stand a minifigure on a 4 × 3 plate; build a stack of four bricks on another
plate beside it; the tops are level. That check takes a minute and settles the whole
change — which is the standard the old wording failed, since "about 4 bricks" cannot
be checked at all.

**The head stud is not counted, and `CORE-001` owns that as its own decision.** A
stud is not height: it occupies the tube of the piece above it, which is why a brick
stacks at 3 plate layers and a plate at 1 with their studs already inside those
counts. Without the rule a minifigure measures 13½ and no whole figure is correct.

An earlier draft justified it "for the same reason a brick's stud is not counted in
its 3 plate layers" and cited the paragraph above, which cites `DMG-003`. That was
wrong: `DMG-003` measures material across an impact's direction of travel and never
meets a stud, so it cannot be the authority. The sentence now claims no precedent and
names no rule — it states the convention and the reason, in the rule that needs it.
Whether the same convention should be written once for every height in the ruleset —
`VEH-030`'s vehicles, `MOVE-011`'s obstacles — is a real question and a separate
proposal; nothing in `docs/` currently answers it either way.

**Why the old derivation was wrong twice.** "About 4 bricks" is loose about a
measurement that is exact, and "the smallest whole-brick height that does" reasons
from a preference for whole bricks rather than from the model — then reaches a figure
that excludes a mandatory part of the model to stay whole. Principle 1 asks for the
opposite: read the plastic, and let the number be what it is. 13 is not a whole
number of bricks, and that is not an objection.

---

## Decision 2 — the measuring plane moves to the underside of the base

`CORE-001` measured from the **top face** of the base plate. It now measures from the
**underside**: the base is part of the Unit Base.

That is the change of substance behind the figure, and it is what makes the volume
true wherever it is used:

- On the battlefield the base rests on the ground. Nothing observable changes.
- Inside a transport the base rests on the deck, so a passenger needs 13 clear plate
  layers above that deck — which is what "one Unit Base of clear height" (`TRN-019`)
  now means, with no sentence rewritten.
- Through a doorway the base passes with the model, so the clear opening must admit
  13 — which is what `CMP-018`'s vertical projection now reads, again with no sentence
  rewritten.

Under the old plane each of those needed 12 **plus** the plate nobody had counted.
The rules said 12 and the table needed 13. This is that gap closed.

**Cargo has no base and loses nothing.** A crate's slice is its own height and the
budget is the Unit Base's height (`TRN-013`), which is now 13. Three 4-plate crates
still share one Unit Base — 12 of 13 — and a fourth still does not fit.

---

## Decision 3 — `TRN-013`'s three cargo heights stay where they are

The drone, motorbike and walker rows read `12 plate layers`. #80 deliberately left
them alone, on the grounds that a height read from a model is not a restatement of
`CORE-001` even when the two agree — and recorded in its Handover that the follow-up
should decide whether the examples were still the examples it wanted.

**They stay at 12**, and the reasoning in #80 is why.

The tempting move is to bump them, because all three were originally chosen to be
exactly one Unit Base tall. But #80 kept them literal on the explicit grounds that "a
height read from a model is not a restatement of `CORE-001` even when the two agree",
and rejected replacing them with "one Unit Base" for the same reason. Moving them by
hand now would concede that they *are* the unit restated — and would commit every
future height change to hunting three table cells that no grep for the unit will find.

Nothing in the table claims they fill a Unit Base: #80 deleted the `Space` column that
said so. A drone 12 plate layers tall is a legal example of cargo, and the slice rule
above the table does the rest. If the table ever needs an example of cargo exactly one
Unit Base tall, the honest way to write it is "one Unit Base", not a figure kept in
lockstep by hand.

---

## Decision 4 — where the figure legitimately stays, unchanged from #80

The line #80 drew holds: **the figure appears where the unit is introduced or
defined, and nowhere where it is used.** That is `CORE-001` and its two projection
rows, the glossary's *Unit Base* entry, and the three overview surfaces —
`01-foundations.md`, `README.md`, `CODE_OF_DESIGN.md` — each of which states the
dimension line and names `CORE-001` as the authority in the next breath.

This change edits exactly those, plus the `CORE-001` image brief, `SCS-002` (Decision
6) and three sentences that name the surface a clearance is measured from. The only
`12 plate layers` left standing in `docs/` afterwards is `TRN-013`'s three cargo
heights, which Decision 3 keeps deliberately — that is the whole return on #80.

---

## Decision 5 — the image brief gains the panel that is the derivation

`assets/IMAGES.md`'s `CORE-001` entry currently briefs five panels and says the volume
is "dimensioned 4 studs wide × 3 studs deep × 12 plate layers tall, with a standing
minifigure inside it and the plate it stands on marked as floor, outside the volume".
Two thirds of that sentence is what this change reverses.

It also gains a sixth panel: the minifigure on its base, flush with a stack of four
bricks and a plate. That panel is not decoration — it is the derivation, and it is the
one part of this change prose genuinely cannot carry. `assets/IMAGES.md`'s own test
for the column is whether text alone is enough; for "these two stacks are the same
height", it is not.

**The photograph is not committed.** `assets/images/` holds a `.gitkeep` and nothing
else; every entry in the index is a brief for an image not yet drawn. Adding one real
render for one panel of a six-panel brief would leave the entry half-satisfied and the
convention half-applied. The brief describes what to draw; drawing it is its own task.

---

## Rejected

**Keeping 12 and declaring the base plate part of the floor everywhere.** This is the
status quo, and it is coherent right up to the moment a model is carried. A transport
deck is a floor, the passenger's base sits on it, and the rules would still say 12
while the plastic needs 13. Declaring the plate "not part of the space" does not make
it stop occupying space.

**14 plate layers, counting the head stud.** The stud is real plastic and it does
stick up. Rejected because the ruleset already decided this question for every other
element: a brick is 3 plate layers, its stud is not counted, and the stud occupies the
tube of whatever sits above it. A minifigure under a 13-plate-layer ceiling has its
head stud in exactly that position. Counting it here would make the Unit Base the only
element in StudCraft measured stud-inclusive.

**Rounding to 15 — five bricks — to keep whole bricks.** The old derivation's
instinct, extended. Rejected: it invents two plate layers of air that no model
occupies, in the volume that defines "the minimum operational space an object needs"
(`TRN-001`). A unit that rounds up is a unit that lies about the model.

**Adjusting `VEH-028`'s proportion to compensate.** It needs no adjustment — #81
restated it as one Unit Base per two studs, which scales with the unit. Worth stating
because the previous version of that rule (6 plate layers per stud) would have needed
exactly this kind of repair, and the reason #81 rewrote it was to avoid having to make
one here.

---

## The spec deltas

Four requirements across two capabilities carry the figure:

| Capability | Requirement | What moves |
|---|---|---|
| `unit-base` | Unit Base Measurement | 12 → 13, the brick equivalence, the measuring plane, and the stale "deployment area" #81 handed on |
| `unit-base` | Unit Base Projections | the vertical projection's 12 → 13 |
| `unit-base` | Cargo Divides a Unit Base | the slice budget's 12 → 13, and its *Three short crates share one Unit Base* scenario, which says three 4-plate crates "occupy **exactly** one Unit Base together" — at 13 they occupy one with a plate spare, the same correction #80 already made in `docs/09-transport.md` |
| `weapon-capacity` | Platform Length Definition | its scenario *Infantry Platform Length ignores the Unit Base's height* says "the Unit Base's 12 plate layers of height are not considered" |

Every scenario keeps its name — `system/workflow.md` treats a scenario heading as an
identifier — and bodies are corrected in place.

**These deltas must be written against the living `openspec/specs/`, and the living
spec is two changes behind.** `state-the-unit-base-height-once` wrote none, but
`deployment-is-a-volume` wrote a `MODIFIED` block on *Unit Base Projections* that has
not been archived. Two unarchived changes modifying one requirement is the case
`system/workflow.md` describes under "When several changes modified the same
requirement", and its rule is that the last change carries the authoritative delta
while the superseded one moves to `specs-superseded/`.

The cheaper and correct order is to run `Archive cut` first, so the living spec
absorbs #81's delta and this change's deltas are written against a current spec. That
is also what "Archive close to the merge, not in batches of seventeen" asks for, and
there are three unarchived changes waiting. This proposal's spec deltas are therefore
written **after** the archive lands; the `docs/` tasks do not depend on it.


---

## Decision 6 — `SCS-002` has to pin the base, because the derivation now leans on it

`SCS-002` requires "one physical base measuring 4 × 3 studs" and says nothing about
how thick it is. That was harmless while #73's Decision 4 kept the base outside the
volume: its thickness could not affect a height measured from its top face.

It is not harmless now. `CORE-001`'s 13 is 4 bricks of minifigure **plus one plate of
base**, so a builder who uses a brick-thick base has a legal infantry model 15 plate
layers tall that does not fit its own Unit Base — and `CORE-001` would be citing
`SCS-002` for a fact `SCS-002` does not state.

`SCS-002` now says the base is one plate thick. That is what every infantry base in
the ruleset's examples already is, so no legal model becomes illegal; what changes is
that the derivation has something to stand on.

The alternative was to have `CORE-001` count one plate of base regardless of what the
builder used. Rejected: it would make the Unit Base a figure that ignores the model in
front of it, in the one rule this change exists to make read the model.

---

## Decision 7 — half a Unit Base is now half a plate layer, and `VEH-028` says so

`VEH-028`'s footprint bound is one Unit Base of height per two studs of the narrowest
side, so an odd narrowest side gives a limit of *n* and a half Unit Bases. At 12 plate
layers that was a whole number — 1.5 UB was 18, six bricks exactly. At 13 it is 19½.

The rule stays deterministic, because #81 wrote it to compare rather than round: a
vehicle's height is measured in plate layers and checked against the limit, so 19
passes and 20 fails. But `DMG-003` calls the plate layer the finest unit of height in
the game, and a threshold sitting between two of them should be visible where a
builder meets it. `VEH-028` gains one clause saying the limit is met by any whole
plate count below it.

This is the class `system/proposal-review.md` records as multipliers falsified by
numbers added later, caught before merging rather than after. The multiplier itself is
sound — it is unit-relative, which is exactly why #81 rewrote it in Unit Bases.

---

## Versioning — this change carries `**Bump:** major`

A compartment or doorway built to exactly 12 plate layers of clear height stops
carrying infantry. That is a breaking change to models already on the table, and
`system/documentation-standards.md` provides the marker for it: a commit message line
`**Bump:** major`, which `scripts/release_cut.py` reads. It is not a version edit and
does not touch `CHANGELOG.md` or any header.

The precedent is split — `component-damage-system` and `weapon-construction-system`
both carried the marker as an explicit task, and #73, which was equally breaking on
the same subject, did not. Carrying it is the reading that matches SemVer and the
document that describes the mechanism.
