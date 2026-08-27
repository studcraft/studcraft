# Infantry states its distances in Unit Bases

## Why

**The living spec already requires this and no document does it.**
`openspec/specs/unit-base/spec.md` says *"Every distance, Deployment Volume, and
vehicle or infantry footprint SHALL be expressed using this unit"*, and assigns
*"the horizontal projection (4 × 3 studs) for distances, movement, deployment
floors and footprints"*. Footprints, capacities and Deployment Volumes comply.
**Distances do not** — `17-infantry.md` states movement in studs,
`08-vehicles.md` states it in studs, and `10-weapons.md` states range in studs.

Infantry is where the gap costs most, because its stud figures were never a
second unit of measure. They were the Unit Base's own axes spelled out: 12 studs
forward is four base-depths, 12 studs sideways is three base-widths. Every rule
that read those numbers restated the arithmetic beside it, and `INF-012` derived
a Wounded limit by counting steps precisely because a fraction of 12 studs is not
always legal.

**This change converts infantry and no one else.** It is the first document to
state a distance in `UB`; `08-vehicles.md` and `10-weapons.md` are still owed and
Out of Scope says so.

**No distance changes.** Every limit is the same number of studs after this
change as before it.

**This proposal was written after the edits were made.** That is not the workflow
(`system/workflow.md`, Git Workflow); `design.md`, Decision 1 records why the
sequence was inverted and what it cost. Part of what it cost is visible in
`tasks.md` Part B, which repairs eleven defects a pre-application audit would
have caught first.

**The change outgrew its name.** The directory and branch are `fix-infantry`,
and Part C retires a rule in `11-combat.md` and edits `02-core-rules.md`,
`08-vehicles.md`, `TODO.md` and `CODE_OF_DESIGN.md`. The name cannot change —
`openspec/config.yaml` requires one dedicated branch per proposal and the gate
compares the two exactly. `design.md`, Decision 8 accepts it and says where a
reader looking for the `CBT-014` retirement will find it.

## What Changes

### `CORE-001`: what a distance written in `UB` means

**`UB` already meant a volume, and this change gives it a second reading.** Every
bare `N UB` in the ruleset counts volumes — "Infantry occupies 1 UB", "provides
**8 UB** of capacity" — and the one written form `CORE-001` gave for counting
them was two-dimensional: *"A footprint written `W × D UB` counts 4-stud widths
by 3-stud depths."*

`CORE-001` now also states that **a distance written `N UB` counts N Unit Bases
along the single axis its rule names**. The glossary's `UB` entry matches it, and
`01-foundations.md`'s list of what UB measures gains the use it now has. Without
this, a reader arriving from `09-transport.md` reads "up to 4 UB forward" as four
volumes.

### `17-infantry.md`: distances stated in Unit Bases

| Rule | Was | Is now | Studs |
|---|---|---|---|
| `INF-002` Forward | up to 12 studs, in multiples of 3 | **up to 4 UB, in whole UB steps** | 12 |
| `INF-003` Side | up to 12 studs, in multiples of 4 | **up to 3 UB, in whole UB steps** | 12 |
| `INF-004` Backward | up to 12 studs, in multiples of 3 | **up to 4 UB, in whole UB steps** | 12 |
| `INF-012` Wounded | at most two steps — 6 or 8 studs | **at most 2 UB** | 6 / 8 |

**Each rule states which axis it reads**, because `CORE-001` requires it: *"Each
rule states which dimensions of the Unit Base it reads."* Forward and backward
read the 3-stud depth, sideways reads the 4-stud width. Without that clause `4 UB`
forward and `3 UB` sideways read as different distances when they are the same
twelve studs — `design.md`, Decision 2.

The Design Philosophy section already stated both axes and is unchanged.

### Prose compressed across the document

Justification and worked-out reasoning are removed from `INF-002`, `INF-003`,
`INF-004`, `INF-007` and `INF-009` — the same standard `general-review` (#130)
applied to the other fourteen documents
(`system/documentation-standards.md`, "How a Rule Is Written"). The worked
example under `INF-003`, the sprinting note under `INF-002` and `INF-009`'s
paragraph reconciling its own step count with `INF-007` all go.

### `INF-007`: climbing is charged per obstacle

**The first of two rule changes in this proposal.** `INF-007` said a climb costs
"1 additional Action Point … for a total cost of **2 AP**", stated absolutely.
`INF-009` says a stepped surface is climbed one step at a time and charges each
step, which a two-step staircase makes 3 AP. The sentence that had reconciled
them was prose, and the compression removed it.

`INF-007` now charges **1 additional Action Point for each such obstacle the move
crosses**. The ordinary case — one obstacle — still costs 2 AP in total. This is
also what the general rule already said: `MOVE-013` reads *"Each step is an
obstacle in its own right, read individually."* `design.md`, Decision 3.

### Nothing in `docs/` names a mechanic that does not exist

**The second rule change, and it removes one rule.** `INF-002`'s sprinting note
was one of five places where the ruleset described what it does not contain.
Deleting one and leaving four states the standard for infantry alone, and #130
already retired `WPN-017 — Future Weapon Types` for exactly this reason — *"a
list of things that do not exist"*.

| Where | What goes |
|---|---|
| `03-game-flow.md`, `FLOW-013` | the bullet naming sprinting, and the `WPN-014` clause beside it — `WPN-014`'s "Future scenarios may limit the number of weapons fired" was deleted by #130, so that citation dangles the same way. The scenario power stays: the rule's closing sentence already carries it |
| `11-combat.md` | **`CBT-014 — Future Combat Extensions` is retired.** Seven mechanics StudCraft does not have, and a constraint on rules nobody has written |
| `08-vehicles.md`, `VEH-011` | "Future rules may introduce lateral movement." |
| `02-core-rules.md`, `CORE-005` | "Structure-wide effects such as building collapse or breaching are not currently defined." |
| `CODE_OF_DESIGN.md`, Principle 9 | the clause deferring reaction fire to `CBT-014` |
| `TODO.md` | the three entries that quoted the deleted sentences |

`CBT-014`'s number is retired, never reissued, and no stub is left
(`system/documentation-standards.md`, Naming Conventions). `CBT-015` keeps its
number, and `CBT-010` was already retired before this change — `11-combat.md`
carries two gaps afterwards, not one.

**No rule in `docs/` cited `CBT-014`, and two files outside it did.**
`scripts/rule.py refs` reports "cited by nothing" and cannot see them: it reads
an index built from `docs/`, and `scripts/lint_ruleset.py` reads `docs/` and
`assets/IMAGES.md` only. `system/proposal-review.md` names this failure class
first — *"grep the whole repository before deleting a rule"* — and `tasks.md`
task 9.4 is that grep. `design.md`, Decision 6.

### `INF-010` is retired

*Vertical Access* restated `INF-008`: both said a face of 7 or more plate layers
needs a slope, a stair or a ramp. The archived change that created the document
recorded the overlap and left the fold for later
(`2026-08-18-infantry-is-a-first-class-domain`, Decision 14). This change deletes
`INF-010`; the number is retired and no stub is left.

Two citations naming it are amended to name `INF-008` alone —
`07-movement.md` (`MOVE-014`) and `08-vehicles.md` (`VEH-026`).

**`INF-008` is not widened to carry `INF-010`'s closing sentence.** It still
heads its three access points "Examples:", so whether that list is exhaustive is
open exactly as it was before this change. `design.md`, Decision 4 records the
choice; Out of Scope names what is still owed.

### Repairs found by auditing the applied text

Eleven, all in `tasks.md` Part B, none of them changing what a rule means:

- **The applied text spelled the unit `BU` — BLOCKER.** The ruleset's
  abbreviation is `UB`, defined by `CORE-001` and used by six other documents.
  Nothing in the ruleset is called a `BU`.
- **`UB` as a distance was undefined — BLOCKER.** `CORE-001`, the glossary and
  `01-foundations.md` carry the reading; see above.
- **The Summary contradicted the rules above it — BLOCKER.** Items 2, 3 and 7
  still read "up to 12 studs, in multiples of 3", and item 5 stated the climb
  cost the way `INF-007` did before this change.
- **`INF-002` did not own its measurement point.** It pointed at `MOVE-003`,
  which points back at `INF-002`. `MOVE-003` does answer before it delegates, so
  no reader was stranded — but the domain rule stated nothing about its own
  domain. `INF-002` takes the answer and `MOVE-003` keeps the handoff alone,
  which is the form `MOVE-012`, `MOVE-013` and `MOVE-014` already use.
- **`INF-009` lost a rule with the prose.** "7 or more not climbable at all
  (INF-008), **which stops the climb at that step**" became "cannot be climbed",
  leaving a player mid-staircase with no stated outcome.
- **`INF-009` restated `INF-007`.** "Each step is charged separately" is what
  the new `INF-007` says; it goes.
- **`INF-004` lost its Action Point cost.** The compression left it inheriting
  `INF-002`'s "movement limit and step size", which is not its cost.
- **`INF-012` was still written in studs**, in a document that no longer is.
- **`INF-007` named one limit for a rule that applies in every direction —
  BLOCKER.** Found by auditing the applied text, so it is `tasks.md` Part D
  rather than Part B. `main` read "12 studs", correct on both axes because
  4 × 3 and 3 × 4 are the same distance; `4 UB` is correct forward and wrong
  sideways, where `INF-003` allows 3. `INF-007` now defers to the limit the
  move's own direction sets, and the Design Philosophy says the count differs by
  axis.
- **`INF-009`'s "Distance traveled up either"** lost the two antecedents the
  deleted paragraphs had given it.
- **The three obstacle rules glossed inconsistently.** `INF-007` lost its brick
  gloss and `INF-006` and `INF-008` kept theirs; the two survivors go, because
  `INF-006` states the plate-to-brick conversion outright one line later.
- **The glossary's *Step* entry** cited `INF-012` for a term `INF-012` no longer
  uses and explained a fraction argument it no longer makes. Retargeted at
  `INF-002`, `INF-003` and `INF-004`, which all say "in whole UB steps".

### Outside `docs/`

`system/repository-strategy.md` (Branch Naming) allows a ruleset branch to carry
a non-`docs/` file when `design.md` names which and why. Decision 6 names both.

- **`TODO.md` loses two entries and gains one.** Two quoted sentences this
  change deletes. The `CBT-014` entry is **replaced**: retiring that rule opens
  the question of whether `CORE-009`'s *"If you can see it, you can shoot it"*
  grants a shot outside the attacker's activation, and the new entry quotes
  `CORE-009`, which survives. The `VEH-006` entry stays. `TODO.md quotes the
  ruleset verbatim` is a required check, so this travels in the same commit.
- **`CODE_OF_DESIGN.md` loses one clause.** Principle 9 deferred *"whether that
  produces a shot outside a unit's own activation"* to `CBT-014`. Deleting the
  rule without this leaves the charter citing a retired ID and a principle
  deferring to nothing.

**Three archived changes put the reaction-fire question in `CBT-014` on
purpose.** This change does not overturn them and does not restate their answer
as a new rule — it moves the question to `TODO.md`, where an open question
belongs. `design.md`, Decision 6.

**The standard this change sets is a `docs/` standard.** `system/workflow.md`
already draws that line: `docs/*.md` is the ruleset, everything else is the
repository. `TODO.md` and `CODE_OF_DESIGN.md` are edited here because this
change breaks something they say, not because the standard reaches them.

## What Does Not Change

- **Every distance.** 12 studs forward, 12 sideways, 12 backward, 6 and 8 for a
  Wounded model. The unit is different; the tape measure is not.
- **The obstacle thresholds.** 3 plate layers or fewer, 4 to 6, 7 or more.
  `INF-008` still requires a legal access point and still lists slopes, stairs
  and ramps.
- **`INF-001`, `INF-005`, `INF-011`.** Untouched.
- **Action Points.** Still 3 per activation (`02-core-rules.md`, CORE-006), still
  1 per movement action and 1 per rotation.
- **`CHANGELOG.md` and every `**Version:**` header.** Release-cut only
  (`system/documentation-standards.md`, Versioning).

## Out of Scope

- **Vehicle and weapon distances.** `08-vehicles.md` states movement in studs
  and `10-weapons.md` states range in studs, and both still owe the unit-base
  spec the same conversion infantry makes here. **Until they make it, a player
  comparing an infantry move to a weapon's range converts**, and the factor
  differs by axis — ×3 forward, ×4 sideways. Every changed rule carries its stud
  figure for that reason. `design.md`, Decision 7 records the cost as accepted
  rather than unnoticed.
- **Whether `INF-008`'s three access points are examples or a closed set.** The
  question predates this change, and settling it is a rule decision rather than a
  unit change. Still owed, as it was after #119.
- **Rules for the mechanics `CBT-014` listed.** Retiring the list is not a
  decision about suppression, fire or overwatch; it is a decision to stop naming
  them in a document that defines none of them.
- **A `sprinting` rule.** `FLOW-013` still permits a scenario to extend the
  ruleset; the ruleset still does not define sprinting.
- **What counts as one obstacle, and when an infantry descent is a fall.**
  `INF-007` charging per obstacle makes the count load-bearing, and only
  `MOVE-013` supplies one — for the steps of a stepped surface, which `INF-009`
  already handles. Outside that, whether a wall crossed up-and-over is one
  obstacle or two is undecided, and `VEH-027` states for vehicles what no rule
  states for infantry: which descents are movement and which are a fall
  (`07-movement.md`, MOVE-015). Raised by the audit of the applied text and left
  standing — deciding it is a terrain rule, not a unit conversion.
- **Three notations for `N UB`, of which `CORE-001` now defines two.** The count
  of Unit Base volumes — `09-transport.md`'s "8 UB of capacity" — is still
  disambiguated by its own prose rather than by `CORE-001`. `design.md`,
  Decision 2.
- **`WPN-014` is now cited by nothing.** Removing `FLOW-013`'s mis-aimed clause
  was right, and it was that rule's only citation. Whether `WPN-014` is
  standalone or disconnected is its own reading.
