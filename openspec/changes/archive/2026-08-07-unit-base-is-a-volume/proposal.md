# Make the Unit Base a volume

## Why

`CORE-001` defines a Unit Base as an area — "a LEGO Plate measuring 4 × 3 studs".
Several shipped rules already read it as a volume and cannot work otherwise:

- `TRN-005` requires "a free Unit Base ... **inside** the transport". A plate has no inside.
- `TRN-002` puts a minifigure *and* its weapons, equipment, backpack, shield and accessories inside one Unit Base.
- `TRN-003` counts Unit Bases "available inside its cargo compartment".
- `CMP-013` separates crew compartments from Cargo Bays, both measured in Unit Bases.
- The glossary's `Cargo Bay` entry calls it "the **interior space** of a transport vehicle, measured in Unit Bases".
- `GEO-001` lists "**Transport volume**" among the measurable properties of Gameplay Geometry.
- `SCS-014` — "Transport capacity is determined exclusively by the interior volume."

The ruleset is already volumetric in practice. It was documented in 2D, volume
language entered only where 2D could not stretch — all of it in transport — and
it was never defined. This change writes down what the ruleset is already doing:

```
UB = 4 studs (width) × 3 studs (depth) × 12 plate layers (height)
```

It also settles a question four shipped rules leave open. `SCS-005`, `VEH-015`,
`VEH-016` and `DEP-005` all say physical fit decides, and none of them says what
the thing that fits *is*. **It is the Unit Base**: one for a minifigure, its own
volume in Unit Bases for a vehicle. Read as loose plastic instead, a seated
minifigure slips into a space no Unit Base fits, and the rules answer the same
question twice.

## What Changes

- **`CORE-001`** becomes a volume, states where its height comes from, and names
  the projection principle every other rule reads through — plus the boundary
  that stops projections from replacing a physical check.
- **`SCS-005`, `VEH-015`, `VEH-016`, `DEP-005`** each gain one sentence naming the
  Unit Base as the thing that must fit. No wording is removed and no exception is
  created.
- **`CMP-018`** stops saying height "has no Unit Base": an opening's height is
  measured against the vertical projection, against the *clear* opening, and what
  passes through it is the model's Unit Base.
- **`GEO-004`**'s access-opening bullet moves with `CMP-018`, and the geometry
  Summary's list of physical checks catches up with it.
- **`WPN-004`** and the `Platform Length` glossary entry read the **horizontal**
  projection, so infantry's Platform Length stays 4 studs.
- **`TRN-003`** counts volume rather than objects; **`TRN-013`** lets cargo — and
  only cargo — divide a Unit Base into slices.
- **Two new rules**: `TRN-019` (Interior Clearance) and `TRN-020` (Interior Levels).
- **`01-foundations.md`, `README.md` and `CODE_OF_DESIGN.md`'s Principle 7** track
  the definition instead of restating a two-dimensional one. The glossary's `UB`,
  `Platform Length` and `Cargo Bay` entries follow, and `Interior Clearance`,
  `Slice` and `Projection` are added.
- `TRN-001`, `TRN-002`, `TRN-005` and `09-transport.md`'s Purpose are reworded
  opportunistically: each becomes literally true instead of loosely true.

## Impact

- Affected documents: `docs/01-foundations.md`, `docs/02-core-rules.md`,
  `docs/04-construction-standard.md`, `docs/05-construction-components.md`,
  `docs/06-deployment.md`, `docs/08-vehicles.md`, `docs/09-transport.md`,
  `docs/10-weapons.md`, `docs/14-glossary.md`, `docs/15-geometry-layers.md`,
  plus `README.md` and `CODE_OF_DESIGN.md`.
- Affected capabilities: `unit-base` (MODIFIED + ADDED), `weapon-capacity` (MODIFIED).
- Rule IDs added: `TRN-019`, `TRN-020`. None renumbered, none removed.
- **What this costs an already-built model**, in full — both consequences are
  written into `TRN-019` rather than left to be discovered mid-game:
  - A **closed** compartment with less than 12 plate layers of clearance stops
    carrying infantry. It keeps carrying cargo, so it becomes a freight hull.
  - The same applies to a **closed cockpit**. A Pilot with no Unit Base is no
    Pilot, and `VEH-013` says a vehicle without one cannot move. This is the
    larger of the two costs, and it is the price of not writing a crew exemption
    (`design.md`, Rejected).
  - Neither costs anything to repair: raise the roof by a plate or two, or open it.
- Archive order is not free: `access-openings-must-pass-the-model` holds an
  unarchived `geometry-layers` delta describing `CMP-018` in the wording this
  change replaces. It must be archived first, or reconciled. Task 10.1.

## Out of Scope

- **Charging Deployment Area by volume instead of area.** `DEP-003` charges the
  Unit Bases a vehicle *covers*; charging what it *encloses* would close the
  multi-deck exploit, and it rewrites `DEP-001`, `DEP-002`, `DEP-003` and
  `DEP-009` and redefines what a game size means. Separate change.
- **The multi-deck exploit itself.** `TRN-020` makes interior levels countable,
  not limited, and nothing in the shipped ruleset bounds a vehicle's height. See
  `design.md` (Rejected) for why a cap is the wrong repair.
- **Vehicle height as a ratio of the Unit Base.** Not tracked in `docs/` or
  `TODO.md`; this change supplies the Unit Base height such a rule would read.
