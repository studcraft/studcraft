# Design — the Unit Base as a volume

## Context

`CORE-001` is cited ten times across seven documents in `docs/`, plus its own
heading in `02-core-rules.md`. Every citation is accounted for below: each one
either changes, is reworded opportunistically, or is verified unaffected with the
reason recorded so the question is not reopened. `README.md` and
`CODE_OF_DESIGN.md` restate the definition without citing it, and are corrected
here for that reason.

---

## Decision 1 — what must fit is the Unit Base, never the loose model

This is the spine of the change, and every other decision hangs off it.

The ruleset says in four places that physical fit decides:

- `SCS-005` — "If something physically fits: It fits", applied to passengers, cargo, vehicles, buildings and terrain.
- `VEH-015` — "Crew must physically fit inside the vehicle."
- `VEH-016` — "If a passenger physically fits, it may embark."
- `DEP-005` — "If a minifigure physically fits inside the vehicle, it may be transported."

None of them says *what* the thing that fits is. Read as loose plastic, a seated
minifigure slips into 9 plate layers and the rules give two answers for one
model. Read as the Unit Base, there is one answer everywhere:

> **A minifigure is one Unit Base. A vehicle is its own volume in Unit Bases.
> That volume is what has to fit.**

This is not new reasoning in this repository. `CMP-018` reached exactly the same
conclusion for an opening's *width*: an earlier draft measured 16 mm of
minifigure torso, and the correction recorded in
`openspec/changes/access-openings-must-pass-the-model/tasks.md` was that
"everything in StudCraft is expressed in Unit Bases, and an aperture is not the
exception". Decision 1 finishes that sentence for the other two axes.

Consequences, all of them stated in the rules rather than left to be discovered:

- The four rules above each gain one sentence naming the Unit Base as the thing
  that fits. None of them loses its wording, and none becomes an exception.
- It applies to **crew as well as passengers**. A crew member occupies a Unit
  Base like anyone else (`TRN-014`, `CMP-013`), so a closed cockpit under 12
  plate layers has no room for its Pilot — and a vehicle without a Pilot cannot
  move (`VEH-013`). `TRN-019` says so where a player will read it, and
  `proposal.md` records it as the change's real migration cost. A crew exemption
  was rejected: see below.

---

## The height is read, not chosen

`TRN-002` fixes the floor: a minifigure occupies exactly one Unit Base "whether
standing or seated", so a Unit Base must contain a standing minifigure — about
4 bricks from its feet to the top of its head, a figure `CMP-018` already states.

Height is then counted in the ruleset's own vertical unit: plate layers, a plate
counting 1 and a standard brick 3 (`DMG-003`, and `VEH-021` for terrain). Four
bricks is twelve of them, and it is the smallest whole-brick height that contains
the figure. Nothing in the ruleset asks a Unit Base to be taller, and a Unit Base
is the minimum operational space an object needs (`TRN-001`), so it takes exactly
that.

**Stated honestly: 12 is derived up to rounding, not forced.** An earlier draft
of this design claimed `TRN-001` supplied a hard ceiling. It does not — `TRN-001`
bounds how many Unit Bases an *object* occupies, not how tall the unit is. What
it does supply is the reason to take the smallest height that works rather than a
comfortable one. The datum matters for the same reason: `CMP-018`'s "about 4
bricks" is measured with the figure standing on its base, and the 12 layers are
measured from the **top face** of that plate — the plate is the model's floor,
not part of its space (decision 3).

---

## Decision 2 — the organising principle: projections

A Unit Base is a volume. No rule reads the whole volume unless it needs it; each
reads whichever **projection** it needs.

| Reading | Used for |
|---|---|
| Horizontal projection, `4 × 3` studs | Movement, deployment, footprints |
| The volume itself | Carrying capacity, interior space |
| Vertical projection, `4 studs × 12 plate layers` | Passing an opening |

**Which vertical projection.** The volume presents two vertical faces — `4 × 12`
from the front and `3 × 12` from the side. The front governs, because `CORE-002`
already makes the 4-stud edge the front, and `CMP-018` independently arrived at
that same figure for an opening's width.

**Where the principle stops.** Projections feed *measured values* (`GEO-003`).
They never replace a physical check: Line of Sight and Cover (`CORE-008`,
`CORE-010`) resolve against the real plastic on the table, exactly as `GEO-004`
requires, and never against a Unit Base silhouette. **The boundary is written
alongside the principle, in the same rule.** Stated without it, someone proposes
tracing sight lines against projected volumes, which dismantles the premise of
the game.

Naming the principle once in `CORE-001` is what makes this change cheap. Without
it, six rules each need their own guard clause — and this repository has spent
several changes deleting exactly that kind of restatement.

---

## Decision 3 — interior clearance

A Unit Base is a 12-plate-layer volume and it is what must fit (decision 1), so a
closed bay 9 layers high holds no whole Unit Base.

- **Infantry and crew need all 12 layers.** A minifigure is one Unit Base
  standing or seated (`TRN-002`); posture never changes it, and the space was
  paid for at embarking (`TRN-005`).
- **Cargo needs only its own height**, because cargo divides a Unit Base
  (decision 5). The same 9-layer bay carries cargo up to 9 layers.

A low closed transport is therefore not broken, it is **specialised**: a freight
hull rather than a troop hull.

**Seating raises the floor, it does not shrink the occupant.** Clearance is
measured from the surface a model stands or sits on, because that surface is the
model's floor. A bench 3 layers high needs 12 clear layers *above the bench*.
`TRN-017` already says "Benches reduce available cargo space"; this is the same
statement with a number. Without the sentence, a bench would be an obstruction
that makes its own occupant not fit — which is what an earlier draft of `TRN-019`
accidentally said.

**Interior fittings are Gameplay Geometry, so no `GEO-003` boundary is crossed.**
A pipe hanging inside a bay reduces the compartment's usable volume, and
`GEO-002`'s own test is that Visual Geometry is "every decorative element that
**does not modify** Gameplay Geometry". Transport volume is Gameplay Geometry by
name (`GEO-001`). Something that reduces it is Gameplay Geometry however
decorative it looks — exactly as `GEO-002` already rules for a plate sitting in a
structural cross-section. Nothing in `GEO-003` has to change.

**Where the roof isn't.** A position with no roof over it has nothing above to
measure against, so no clearance applies. That is deliberately keyed on the roof
rather than on `TRN-009`, which defines *open* by visibility, not by absence of a
roof — a roofed vehicle with large windows (`TRN-012`) is open under `TRN-009`
and still has a roof to measure. Where an enclosure is incomplete enough that its
occupants stay visible, `TRN-009`'s own test applies and the passengers are
targetable, able to attack, and without `TRN-010`'s hull protection. The builder
pays in survivability rather than in a legality ruling.

---

## Decision 4 — where the 12 plate layers are measured from

From the **top face of the plate**. The plate is the minifigure's floor, not part
of its space, so one Unit Base of height is 12 plate layers exactly — and
therefore 4 whole bricks.

**Not a piece.** The Unit Base is the base volume everything is measured in.
Whether a plate happens to sit underneath is irrelevant to the definition, and
for infantry that plate is not counted. `CORE-001` keeps calling the 4 × 3 plate
the standard base for infantry — that sentence is about how infantry is mounted,
not about what the unit of measurement is. This dissolves the "is the plate part
of the Unit Base?" question rather than answering it.

The vehicle still has to build its interior floors, and they are not free
(`TRN-020`):

```
N interior levels = 12N + (N − 1) plate layers above the lowest interior floor
```

| Levels | Plate layers | Bricks |
|---:|---:|---|
| 1 | 12 | 4 |
| 2 | 25 | 8 + 1 plate |
| 3 | 38 | 12 + 2 plates |

The `(N − 1)` is the intermediate floors at their thinnest — one plate each; a
floor built thicker costs what it actually measures. The first level rests on the
vehicle's own hull and pays nothing, which is why a vehicle exactly 8 bricks tall
does **not** hold two levels: it is one plate short.

---

## Decision 5 — `CMP-018`: measure the clear opening against the vertical projection

Two different decorations are involved, and separating them dissolves the problem.

- **On the model passing through.** What passes is the model's Unit Base
  (decision 1), and everything a model carries is already inside it — `TRN-002`
  says so item by item. Anything protruding beyond the volume is repositioned;
  it is not the doorway's problem.
- **On the vehicle.** An element hanging in the doorway reduces the **clear**
  opening. The check measures the actual gap, never the nominal frame, so
  decoration narrowing an opening counts exactly as `GEO-004` requires.

`CMP-018` keeps its opening sentence — an access point's opening must physically
pass the models that use it — and gains the sentence that says which object is
being passed. That is what stops the rule from giving two verdicts on one
doorway: without it, a plumed helmet and a 12-layer opening are undecidable.

This does not cross the `GEO-003` / `GEO-004` boundary. The required clearance is
read from the Unit Base; whether a given opening provides it is still settled
against the plastic as built, decoration included. `GEO-004` already treated the
width half this way; the height half now matches it.

Consequence: passing the model through stops being *necessary*. Nothing forbids
it — it is simply no longer the only way to answer the question.

---

## Decision 6 — cargo divides a Unit Base; a minifigure never does

Objects shorter than 12 plate layers do not each cost a whole Unit Base. They
share one, provided their combined height stays inside it.

A Unit Base divides into **slices**. Each object occupies a slice measuring
4 × 3 studs by its own height, and the heights must sum to no more than 12 plate
layers.

| Contents | Plate layers | Fits |
|---|---:|---|
| Three ammunition boxes, 4 layers each | 12 | yes, exactly |
| Two boxes plus one 4-layer object | 12 | yes |
| One box plus a minifigure | 4 + 12 = 16 | no |

Slices rather than free three-dimensional packing, and the worked example shows
why: a box measuring 4 × 3 studs has already consumed the horizontal footprint,
so sharing can only be vertical. An object narrower than 4 × 3 still takes a
whole slice of its own height — it pays for width it does not use, exactly as
small cargo already does today. An object whose footprint covers **more** than
one Unit Base takes a slice of its own height in each Unit Base it covers, which
is why `TRN-013`'s table separates footprint from height instead of quoting one
number per object.

**Minifigures are indivisible, and `TRN-002` already says so**: infantry occupies
exactly one Unit Base "whether standing or seated", and "changing posture never
changes transport capacity". No Unit Base is ever shared with a minifigure, even
when a seated one physically leaves room. The carve-out needs no new wording,
only a pointer from `TRN-013`.

---

## Verified unaffected — recorded so the question is not reopened

| Rule | Why it is safe |
|---|---|
| `MOVE-002`, `MOVE-005`, `MOVE-006` | Step sizes read the Unit Base's width (4) and depth (3). Neither moves. "Laying spare Unit Bases end to end" still works — a player lays the plates that define the footprint. A note that movement uses two of three axes would be a restatement of `CORE-001`, not a clarification. |
| `CORE-008`, `CORE-010` | Line of Sight and Cover resolve against real plastic, never against a projection. Not merely unaffected — a boundary this change states, in `CORE-001`. |
| `CORE-004`, `VEH-001`, `VEH-013` | All read "occupies two or more Unit Bases". The verb looks ambiguous once a Unit Base has three dimensions; it is not, because deployment reads the horizontal projection. Settled by stating the principle in `CORE-001`, not rule by rule. `VEH-013`'s derivation of the two-Unit-Base minimum reads better as a volume argument than as an area one, and this change cites it from `TRN-019` rather than editing it. |
| `DEP-003` | Already says "every Unit Base **covered by its footprint**" — explicitly planar in its own words. |
| `DEP-001`, `DEP-009`, `FLOW-001` | Deployment sizes are written as 2D pairs (`5 × 5 UB`). Any residual ambiguity lives in `CORE-001` and is fixed there once. |
| `SCS-001`, `SCS-002`, `SCS-003`, `SCS-014` | `SCS-014`'s "transport capacity is determined exclusively by the interior volume" was already the volumetric reading and becomes literally true without an edit. The other three are construction requirements that read footprints. None of the four cites `CORE-001`; none needs to. |
| `CMP-013` | Crew compartments occupy Unit Bases and are not cargo capacity. True as an area, true as a volume; the clearance consequence for crew is stated once, in `TRN-019`. |
| `GEO-001`, `GEO-002`, `GEO-003` | `GEO-001` already lists "Transport volume" as Gameplay Geometry, which is what `CORE-001` now defines. `GEO-002`'s test is what makes interior fittings Gameplay Geometry (decision 3). `GEO-003`'s list is untouched, for the same reason. |
| The `(4 × 3 studs)` parentheticals in `04-construction-standard.md`, `06-deployment.md`, `07-movement.md`, `08-vehicles.md` | Each cites `CORE-001` and quotes the horizontal figures in a horizontal context (footprint, deployment area, step size). Qualifying four pointers would be four restatements of the projection principle. `01-foundations.md` is the exception and does change, because it presents the definition rather than pointing at a use of it. |

---

## Rejected

- **Exempting crew from clearance.** It would keep every existing low-cockpit
  vehicle mobile, and it costs an explicit exception against Principle 12: a
  Unit Base would mean one thing in the cargo bay and another in the cockpit.
  Decision 1 says the Unit Base is what fits, everywhere. The cost is recorded
  in `TRN-019` and in `proposal.md` instead of being hidden.
- **Letting a seated minifigure occupy less than a Unit Base.** `TRN-002` already
  refuses it — "changing posture never changes transport capacity" — and the
  space is paid for at embarking (`TRN-005`). Posture is a physical-state
  representation (Principle 6), not an accounting device.
- **Editing `GEO-001`'s pointer to `WPN-004`.** `GEO-001` says "Platform" means
  what it means in `WPN-004`: a Unit Base or a vehicle. That stays true, and
  `WPN-004` now says "horizontal" in its own text. Adding it to `GEO-001` too
  would make three documents state the same qualification — the duplication this
  repository has been removing.
- **A separate rule ID for the projection principle.** Every reading of it starts
  at `CORE-001`. A rule whose entire content is "here is how to read `CORE-001`"
  belongs inside `CORE-001`.
- **A `geometry-layers` spec delta.** `GEO-004`'s access-opening bullet is
  reworded, but the living requirement — *Visual Geometry Still Applies to
  Physical Checks* — and its scenarios stay true: the check is still made against
  the physical model with decoration counting. Writing a delta anyway would
  collide with the unarchived `access-openings-must-pass-the-model` delta on the
  same requirement, which is the exact failure `system/workflow.md` ("When
  several changes modified the same requirement") documents.
- **A `transport` capability.** `docs/09-transport.md` predates this repo's
  OpenSpec workflow and has never been formalised;
  `system/proposal-review.md` ("Delta vs. Direct Edit") says not to invent a
  delta against a capability that does not exist. `TRN-*` edits are tracked as
  ordinary doc-edit tasks. The one exception is deliberate and is argued below.
- **Filing interior clearance under the `unit-base` capability.** An earlier draft
  did. Clearance is a property of a *compartment*, not of the unit of
  measurement, so it is a `09-transport.md` doc edit with no delta. Cargo
  divisibility stays under `unit-base`, because what a Unit Base can be divided
  into is a statement about the unit itself, and the living capability already
  carries "Infantry occupies one Unit Base" — the same kind of statement.
- **Declaring low closed transports invalid.** Decision 3 charges them in cargo
  type and survivability instead. A legality ruling would add an exception where
  the existing open/closed distinction already produces the right answer.
- **Capping the number of interior levels.** `TRN-020` makes them countable, not
  limited. **Nothing in the shipped ruleset bounds a vehicle's height at all** —
  I checked `docs/` for one and there is none, and vehicle height as a ratio of
  the Unit Base is out of scope for this change. An earlier draft of this design
  compared `13N − 1` against a 72-plate-layer ceiling derived from a 12-stud
  footprint; that ceiling does not exist in any rule, and the comparison was
  deleted rather than shipped. The honest statement is that a tower of decks
  pays its footprint once and nothing stops it today, which is an argument for
  the out-of-scope Deployment-Area change, not for a cap here
  (`system/proposal-review.md`, "Do Not Cap What the Model Already Bounds").

---

## Design Checklist (`CODE_OF_DESIGN.md`), run against the finished text

- **Can it be represented by the LEGO model?** The height is read off a
  minifigure and counted in plate layers. Clearance is measured inside the hull.
- **Does it require hidden statistics?** No number is assigned anywhere; every
  figure is read from plastic.
- **Does it reuse an existing system?** Plate layers already carry `DMG-003`'s
  Resistance and `VEH-021`'s Terrain Threshold (Principle 15). No new unit.
- **Does it introduce unnecessary exceptions?** One carve-out — minifigures never
  share a Unit Base — and it is `TRN-002` restated as a pointer. The crew
  exemption that would have been a second one was rejected above.
- **Does it make construction more meaningful?** Interior height becomes a design
  decision: a builder chooses between a troop hull and a freight hull, pays a
  plate per interior floor, and pays for seating in headroom.
- **Does it remain intuitive?** "Does a Unit Base fit in that space" replaces
  "is height a rule at all".
- **Does it reinforce "Every Brick Matters"?** A plate of interior floor now costs
  something. So does the roof height a builder chooses.

Principle 7 (One Universal Measurement) is the one this change most directly
serves: height was the last dimension not expressed in Unit Bases. `README.md`
and `CODE_OF_DESIGN.md` restate the old two-dimensional definition without citing
`CORE-001`, so both are corrected here — Principle 7 in particular would
otherwise contradict the rule it defers to.
