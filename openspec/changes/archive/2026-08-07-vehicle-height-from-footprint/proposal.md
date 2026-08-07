# Limit vehicle height from the footprint

## Why

A vehicle's footprint is charged as Deployment Area (`DEP-003`), and nothing
limits how high it may build on top of it. A player buys two Unit Bases of
Deployment Area and stacks functional construction — weapons, observation
posts, crew stations, transport space — vertically above them without paying
anything further.

Three shipped rules make that concrete rather than theoretical:

- `TRN-020` (Interior Levels) makes stacked decks legal and countable, and
  bounds nothing: `12N + (N − 1)` plate layers buys N levels, at any footprint.
- `DEP-006` waives Deployment Area for embarked units, so every Unit Base of
  every deck above the first carries its load free.
- `VEH-001` says "No maximum vehicle size exists", which is true of the
  footprint and was never meant to be a statement about height.

The ruleset already reads a vehicle's horizontal dimensions off the model
everywhere. Its vertical dimension is the one measurement nothing reads.

## What Changes

One relationship, read off the Unit Base rather than chosen:

> **For every stud across the narrowest side of its footprint, a vehicle may
> rise 6 plate layers** — two bricks, or one Unit Base of height for every two
> studs.

- **Three new rules in `docs/08-vehicles.md`**, following `VEH-027`:
  - `VEH-028` — Maximum Height: the ratio, the worked table, the non-rectangular
    reading, and what an illegal build means.
  - `VEH-029` — Base Plane: the datum height is counted from, and why ground
    clearance is not height.
  - `VEH-030` — What Counts Toward Height: Gameplay Geometry only, height as
    plastic measured in plate layers and never converted from studs, movable
    elements at their highest, and models carried on the outside.
- **`VEH-001`** gains a cross-reference. Its "No maximum vehicle size exists"
  stays true as written and is not corrected.
- **`CORE-001`**'s closing sentence — "A footprint is a horizontal reading, and
  says nothing about a model's height" — gains a qualifying clause. It shipped
  three days ago to stop readers inferring a height from a footprint, and after
  `VEH-028` a vehicle's footprint fixes its maximum.
- **`DEP-003`** gains a cross-reference: the Unit Bases it charges are the ones
  `VEH-028` measures.
- **`DEP-006`** gains one sentence saying its waiver is for embarked units, so a
  model carried on the outside is deployed individually. That is what `DEP-006`
  already means; it is stated because the roof is exactly where a player expects
  the waiver to apply, and because the deployment half of that ruling belongs in
  the deployment document rather than in a rule about height.
- **`08-vehicles.md`'s Summary** gains one line. Its list of six physical
  characteristics is unchanged — the list is what the rules read from a vehicle
  during play, and Maximum Height is checked once before deployment and never
  consulted again (`design.md`, decision 7).
- **The glossary** gains `Maximum Height` and `Base Plane`.

## Impact

- Affected documents: `docs/08-vehicles.md`, `docs/02-core-rules.md`,
  `docs/06-deployment.md`, `docs/09-transport.md`, `docs/14-glossary.md`.
  `TRN-020` gains a one-line cross-reference for the same reason `DEP-003` does:
  it is the rule this change bounds, and a reader computing `12N + (N − 1)` for
  eight levels should not have to be in the vehicle document to learn that a
  footprint caps it.
- Affected capabilities: none. `08-vehicles.md` and `06-deployment.md` predate
  this repository's OpenSpec workflow and have never been formalised as
  capabilities, so there is nothing to write a delta against — the wording
  changes are tracked as ordinary doc-edit tasks (`system/proposal-review.md`,
  "Delta vs. Direct Edit"). `vehicle-terrain-thresholds` and
  `vehicle-minimum-footprint` both shipped the same way. The `CORE-001` sentence
  being qualified is not in `openspec/specs/unit-base/spec.md`, so that edit
  needs no delta either.
- Rule IDs added: `VEH-028`, `VEH-029`, `VEH-030`. None renumbered, none removed.
- **Version: minor, declared by saying nothing.** `docs/*.md` changes default to
  a minor bump (`system/documentation-standards.md`, Versioning) and no
  `**Bump:** major` marker is added. This change can require an existing model to
  be rebuilt, but so did `unit-base-is-a-volume`, which made every closed
  compartment under 12 plate layers stop carrying infantry and shipped as a
  minor. Recorded here so the question is not reopened at release-cut time.

### What this costs an already-built model

Two things, stated rather than left to be discovered:

- **A tower built upward is no longer legal.** A one-Unit-Base-wide mast carrying
  an observation post, or a stack of decks on a bike-sized hull, must be lowered
  or widened. That is the point of the change.

  **A tower built downward still is.** Height is counted from the Base Plane, so
  a narrow hull standing on 60 plate layers of leg reaches the same altitude and
  this rule says nothing about it. That is not an oversight — it is `VEH-023`'s
  walker, and decision 3 in `design.md` explains why charging it here would make
  every long-legged walker illegal. It is paid for in silhouette (`CORE-008`) and
  in legs that are destructible components (`VEH-017`, `VEH-018`), not in this
  limit. `VEH-029` says so rather than leaving a reader to notice it, and
  `design.md` records it as open question 6.
- **An element that elevates is now measured in a pose it was never measured
  in** (`VEH-030`). A long barrel, a folding crane arm or a dish that tilts up is
  measured at its highest, so a build that was legal lying flat can fail. At
  every footprint in `VEH-001`'s table the full weapon allowance still fits
  raised to vertical, with margin — the arithmetic is in `design.md` ("Numbers
  checked against numbers"). It bites only on a vehicle more than 2.4 times
  longer than it is wide.

Nothing else. The tightest footprint the ruleset permits is 2 Unit Bases side by
side (8 × 3 studs), which allows 18 plate layers, and a Pilot needs 12 of them
plus a roof (`TRN-019`).

### What it does not do

So nobody credits it with more: it does not limit transport capacity and it does
not close the multi-deck advantage. It **bounds** it — a 4-stud-wide vehicle now
has room for one interior level, a 12-stud-wide one for five — while `TRN-003`
and `SCS-014` still leave an upper deck's Unit Bases free under `DEP-006`. That
hole is separate and is not attempted here.

## Out of Scope

- **Structures.** A scenario-placed structure's Deployment Area occupation is
  explicitly future work (`CORE-005`); this does not open it. One consequence is
  worth naming: the mast this rule stops can be rebuilt without locomotion
  (`VEH-012`) and deployed as a structure, where nothing charges it at all. The
  tower is displaced, not eliminated, and closing that needs `CORE-005` finished.
- **Infantry.** Infantry occupies exactly one Unit Base whatever its posture
  (`CORE-003`, `TRN-002`) and is a minifigure rather than a construction.
- **What a model carried on the outside of a vehicle actually does.** `VEH-030`
  settles that it counts toward height and `DEP-006` that it costs Deployment
  Area. Whether it moves with the carrier, may act, or how it gets off is
  undefined today and stays undefined — defining it is a transport change, not a
  height one (`design.md`, open question 4).
- **Closing the multi-deck advantage.** Whoever closes it starts from `TRN-003`
  ("the Unit Base volume available inside its cargo compartment") and `SCS-014`
  ("interior volume"), and should know that `TRN-014` exempts crew space from
  cargo capacity — so any limit phrased around cargo compartments is answered by
  calling the upper deck a crew station.
- **A second constraint at the wide end.** Six plate layers per stud is generous
  once a footprint is large; whether a height-against-length check is also wanted
  is a separate question (`design.md`, open questions).
