# Design — Infantry occupies a Unit Base rather than being mounted on one

## Decision 1 — The Unit Base is a measurement; the infantry base is a component

Two things with one name, and the ruleset needs both:

- The **Unit Base** is a volume and the game's single measuring unit (`CORE-001`).
  Nothing physical is required for it to exist. A vehicle's footprint is counted in
  Unit Bases and contains none of them as parts.
- The **infantry base** is a physical element every infantry model must be built on
  (`SCS-002`). Its size is one Unit Base read horizontally.

One name for both is right, and renaming either would be worse: the base is sized by
the unit, and two rules read values off it. What was wrong is that `CORE-001` and
`CORE-003` used words describing the component while naming the measurement.

The Rule Hierarchy (`system/design-process.md`) is why the component stays. Physical
construction is level 1, and the infantry base is the ruleset's cleanest instance of
it: facing and the origin of every movement measurement are read off a plate instead
of tracked. Replacing it with "a geometric reference unit" moves two rules from
level 1 to level 4.

## Decision 2 — `SCS-002` states the requirement; two rules cite it

The requirement is a construction requirement, and `04-construction-standard.md` is
where construction requirements live. `SCS-002` is already titled *Infantry Base*.

Two rules mention that a base exists and each cites `SCS-002` rather than stating the
requirement itself. **The mention does not vanish, and this change does not claim it
does**: `CORE-001` needs it to say what the volume is to an infantry model, and
`MOVE-002` to name its own reference frame. What each stops doing is stating the
requirement as a rule and naming the front edge, which `CORE-002` owns.

`CORE-003` mentions it **not at all**. `CORE-001` is two rules above it in the same
document and already carries the mention and the citation; a second copy seven lines
later would be this change committing the defect it is removing.

What each keeps as its own:

- `CORE-001` — the dimensions, the projection table, and the base's horizontal size.
- `CORE-003` — occupancy, in the sentence it already has. Other rules cite `CORE-003`
  for exactly that (`DEP-004`).
- `MOVE-002` — "the base's orientation defines movement and line of advance." That
  sentence is movement's own and appears nowhere else. Its content does not change;
  only its opening pronoun does, because task 3.2 stops naming the front edge and
  "This orientation" would then point at an orientation `MOVE-002` no longer states.

`SCS-004` is not part of this. It says "Every model must have an obvious front, per
the universal Facing rule (`02-core-rules.md`, CORE-002)" — it names no edge and
reads nothing off a base, so citing it for facing would aim at a rule that points
away from itself. `CORE-002` is cited directly, in the same words in both places.

## Decision 3 — Narrowing #73's pointer exemption to one pointer

#73's `design.md` set the test — a pointer changes "because it presents the
definition rather than pointing at a use of it" — and exempted four `(4 × 3 studs)`
pointers on the ground that each "quotes the horizontal figures in a horizontal
context".

That ground holds for the two this change leaves alone. `DEP-001` reads a deployment
area and `VEH-001` a footprint; both are uses, and `CORE-001`'s projection table
already names them as users of the horizontal reading. Restating *which* projection
each reads would put that table's content in two more documents, which is what #73
declined and what this change also declines.

`MOVE-002`'s figures also sat in a horizontal context, so the exemption held for them
too — **and they go anyway, for Decision 2's reason rather than this one.** `MOVE-002`
is one of the three voices of the mounting requirement, and stating the base's size
there is the third copy of it. Nothing replaces the figures: `MOVE-002` cites
`SCS-002` and states no size at all.

`SCS-001` is the one it misses. Its subject is the unit itself — pre-change, "The
fundamental **building** unit of StudCraft is the Unit Base" — so there is no
horizontal use for the exemption to attach to, and the sentence promises "its
definition" before giving figures that are no longer it. #73 shipped the correct form into `09-transport.md`
in the same change ("the Unit Base definition: a volume of 4 × 3 studs by 12 plate
layers") and a fuller deferral into `01-foundations.md`. `SCS-001` borrows that
deferral clause almost word for word, without `01-foundations.md`'s dimension line —
which that document keeps because it introduces the unit, and `SCS-001` does not.

**Quoting nothing rather than quoting the volume** is deliberate. `SCS-001`'s next
sentence is "This corresponds to the footprint of a LEGO minifigure", and a volume
does not correspond to a footprint. Writing the volume into `SCS-001` would make its
own next line false; deferring, and naming the horizontal projection in that next
line, leaves both true and copies no dimensions into a second document.

## Decision 4 — `SCS-001` calls it a measuring unit, not a building unit

Raised in review on PR #79, and it is the same defect as the rest of this change in
its smallest form. `CORE-001` says "StudCraft uses a single **measuring** unit";
`SCS-001` said "the fundamental **building** unit". Two names for one term, and the
divergent one sat in the document whose subject is building, where "building unit"
reads as a part you build with — the reading this change exists to remove.

`consolidate-core-measurements` chose that word deliberately, to "keep the
construction-standard-specific framing (this is *the* fundamental building unit for
construction purposes)". The framing was sound while a Unit Base was a 4 × 3 plate:
something you build with. #73 made it a volume, so the word no longer describes the
thing, and the reason it was chosen for is the reason it now has to go.

**Rejected alternatives**, both defensible:

- **`spatial unit`**, the reviewer's second suggestion. It appears nowhere in `docs/`
  and would be a third name for one term.
- **Principle 7's unmodified "the fundamental unit of the game"** (`CODE_OF_DESIGN.md`).
  It carries no part-reading at all and would have matched the constitution's own
  sentence. `measuring` wins only because `SCS-001`'s next clause points at
  `CORE-001`, so the noun and the pointer agree; had `SCS-001` not carried that
  pointer, the unmodified form would have been the better choice.

Nothing else in `SCS-001` moves. Its third sentence, "Every measurement in the game is
derived from this unit", is pre-existing and stays: it says measurements are expressed
in this unit rather than a parallel one, which naming the unit does not imply. It is
not a claim that no other unit exists — `CORE-001` calls the plate layer "the
ruleset's vertical unit" two rules away.

## Decision 5 — Completing #73's Decision 4 rather than reversing it

#73's Decision 4 is titled **"Not a piece."** and says: "`CORE-001` keeps calling the
4 × 3 plate the standard base for infantry — that sentence is about how infantry is
mounted, not about what the unit of measurement is."

The intent is right and this change keeps it. What #73 left is a pronoun: the
sentence reads "**This** is the standard base for infantry", and after #73 "this" is
the volume defined two lines above, not a 4 × 3 plate. So the sentence now says a
volume is a base — the conflation #73's Decision 4 set out to dissolve, in the definition
rule itself.

The repair says what the volume is to an infantry model — **read horizontally**, the
size of its base — and hands the component to `SCS-002`. The qualifier is not
optional: the base is 4 × 3 studs and the volume is 4 × 3 × 12, so a sentence
equating them without it would reintroduce the conflation in the definition rule
itself. That is #73's Decision 4's own position stated in text that survives the unit being
a volume. Nothing about "not a piece" is reversed; the plate stays uncounted and
outside the volume (`CORE-001`'s floor-plate sentence is untouched).

**One consequence #73 did not foresee, and this change owns.** #73 waived `MOVE-004`
on the ground that "laying spare Unit Bases end to end" still works because "a player
lays the plates that define the footprint" — a reading available only while
`CORE-001` identified the plate with the base. Removing that identification falsifies
it: a volume cannot be laid end to end. Rather than leave a sentence this change
breaks, `MOVE-004` says *infantry bases* — one word, no new fact, and the only rule
outside the three under repair that needed to move with them.

## Why no spec delta

`openspec/specs/unit-base/spec.md` needs no change, and writing one would be worse
than writing none:

- Its requirement text asserts the dimensions, the fit rule and the projections.
  None of the three changes here.
- Its scenario `Infantry occupies one Unit Base` already reads "**WHEN** an infantry
  model is placed on its standard base / **THEN** it occupies exactly one Unit
  Base". That is the split this change writes into `docs/`: a standard base exists,
  and what it does is occupy one Unit Base. The spec was already right; three rules
  in `docs/` were not.
- A `MODIFIED` block would reproduce all four of that requirement's scenarios to
  satisfy `scripts/check_delta_coverage.py`, adding a copy of text that is not
  changing, and it would collide with any later change that does touch the
  requirement — the failure `system/workflow.md` documents under "When several
  changes modified the same requirement".

`vehicle-height-from-footprint` (#75) and `scenario-defines-victory` shipped `docs/`
changes with no spec delta on the same reasoning.

## Rejected

- **Decoupling the Unit Base from any physical base**, as the external review of
  `02-core-rules.md` recommends (`REVIEW-001`, `REVIEW-002`, `REVIEW-004`). Two
  grounds, in order of strength:
  1. **The review contradicts itself.** `REVIEW-008` promises the change does not
     alter "physical construction requirements", while `REVIEW-002` asks the document
     to state "that a model does not need to be physically constructed on a 4×3
     baseplate in order to occupy 1 UB" — which voids `SCS-002`, a physical
     construction requirement. One of the two has to go.
  2. **It moves `CORE-002` off the model.** Facing is read off the base's 4-stud
     edge. With no base, facing becomes a declaration rather than a measurement,
     which is the direction Principle 1 and the Rule Hierarchy's level 1 forbid.
     `MOVE-003` measures "from the edge of the base", which the horizontal
     projection could also supply, so it is a weaker case and is not relied on here.

  The parts of the review that are **correct** need no text, because the ruleset
  already says them: a vehicle needs no physical 4 × 3 plates (`CORE-004`,
  `SCS-003`), a vehicle's height is not capped at 12 plate layers (`VEH-028`), and
  the dimensions and the three projections stay as they are (`CORE-001`).
- **Citing `CMP-018` as evidence for the rejection.** It reads the *measurement* —
  "Infantry is invariably 1 Unit Base, 4 studs" — and survives the review's
  recommendation untouched. Using it would have overstated the case.
- **Removing `MOVE-002` outright.** Its own sentence is not a restatement, and rule
  identifiers stay stable (`system/documentation-standards.md`). A rule reduced to a
  pointer is still a rule; a deleted `MOVE-002` is a gap for no gain.
- **Renaming `SCS-002` or `MOVE-002`.** Both are titled *Infantry Base*, which is
  still what each is about. Headings are the anchors citations and readers use.
- **Saying "baseplate" anywhere.** The review's word, and it names a specific class
  of part. `SCS-002` requires a base measuring 4 × 3 studs; a plate assembly
  satisfies it. Naming the part would add the constraint the review was worried
  about.
- **Qualifying `DEP-001`'s and `VEH-001`'s pointers.** Decision 3. #73 was right
  about both, and `VEH-001` additionally shares its wording with `CORE-004` and
  `VEH-013` — #73 grouped the three deliberately, and editing one would make them
  diverge.
- **Fixing `CORE-001`'s infantry-specific height datum in passing.** Real, and it
  changes the living spec's requirement text (`proposal.md`, Out of Scope).

## Verified unaffected

- `CORE-002`, `CORE-004`: untouched. `CORE-004` already says a vehicle's footprint
  "is defined by the LEGO model itself". `CORE-002`'s bare "the base" gains an
  antecedent it did not have: task 1.1 mentions the base two rules above it, where
  before nothing in `02-core-rules.md` established one until `CORE-003`, two rules
  below.
- `SCS-004`: untouched. It already defers to `CORE-002`, which is what lets `SCS-002`
  stop naming the edge — and it means `04-construction-standard.md` now states the
  front edge nowhere, deferring twice, three rules apart. Deliberate: Core Rules sit
  above Construction Standards, and a pointer beats a copy.
- `MOVE-003`, `MOVE-005`, `MOVE-006`: untouched. No step size is stated by the new
  `MOVE-002` text, and `MOVE-003` keeps measuring from the base's edges. `MOVE-004`
  changes one word, for the reason in Decision 5.
- `SCS-003`: untouched, its "size ceiling (none)" clause included — loose after #75
  and recorded in `proposal.md`, Out of Scope, rather than repaired here.
- `DEP-001`, `VEH-001`, `CMP-018`, `DEP-004`, `TRN-002`, `TRN-014`: untouched, each
  for a reason recorded above or in `proposal.md`.
- `docs/14-glossary.md`: untouched. Its `UB` entry is already the volume, and this
  change introduces no term.
- `docs/01-foundations.md`: untouched. #73 already corrected it by this same test.
