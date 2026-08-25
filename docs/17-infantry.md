# StudCraft Infantry Rules

---

# Purpose

This document defines what an infantry model is and what it can do.

Infantry is a unit domain, as Vehicles is. The mechanics every unit shares are `07-movement.md`; the rules below are the infantry implementation of them.

---

# Design Philosophy

Infantry has no movement statistic.

Its movement is derived from its Unit Base:

* The 3-stud depth defines forward and backward steps.
* The 4-stud width defines sideways steps.

This makes movement measurable directly from the model. A spare Unit Base can be used instead of a ruler.

The count differs by axis because the axes do: 4 UB forward and 3 UB sideways are both 12 studs.

The infantry base is Gameplay Geometry (`15-geometry-layers.md`, GEO-001). Visual Geometry does not modify movement measurements (`15-geometry-layers.md`, GEO-003).

---

# INF-001 — Infantry Unit

An infantry model is a minifigure occupying one Unit Base (`02-core-rules.md`, CORE-003).

Every infantry model is built on one base of `4 × 3` studs, one plate thick — the horizontal reading of the Unit Base (`02-core-rules.md`, CORE-001). Its 4-stud edge is the front, which is the facing every unit has (`02-core-rules.md`, CORE-002).

That orientation is what every direction below is measured relative to — the general rule is `07-movement.md` (MOVE-001).

A minifigure has two hands, and may only use equipment it can physically carry in them. Which equipment needs one hand and which needs two is stated where that equipment is defined — weapons by `10-weapons.md` (WPN-010), shields by `05-construction-components.md` (CMP-014).

---

# INF-002 — Forward Movement

Standard infantry movement:

**Up to 4 UB forward, in whole UB steps.**

A unit may move 1, 2, 3 or 4 UB, or stay put.

Forward movement reads the Unit Base's 3-stud depth (`02-core-rules.md`, CORE-001), so 4 UB is 12 studs.

Each movement action costs **1 Action Point** (`02-core-rules.md`, CORE-006) and moves the unit in a single direction. Changing direction requires a separate movement action (`07-movement.md`, MOVE-007).

Distance is measured from the face of the base that leads in the direction of travel — the front face moving forward, the rear face moving backward (INF-004), the corresponding side face moving sideways (INF-003). This is the general measurement rule (`07-movement.md`, MOVE-003) read against an infantry base.

Each movement action is measured independently: spending two Action Points on movement allows two separate moves of up to 4 UB each, not one move of 8 UB.

A Wounded model's limit is lower — see INF-012.

---

# INF-003 — Side Movement

Infantry may move sideways, left or right.

**Up to 3 UB sideways, in whole UB steps.**

A unit may move 1, 2 or 3 UB sideways, or stay put.

Side movement reads the Unit Base's 4-stud width (`02-core-rules.md`, CORE-001), so 3 UB is 12 studs.

Side movement is a movement action and costs **1 Action Point**, the same as forward movement (INF-002).

Infantry reaches an off-axis position by combining a forward or backward move with a side move, each its own movement action (`07-movement.md`, MOVE-007).

A Wounded model's limit is lower — see INF-012.

---

# INF-004 — Backward Movement

Infantry may move backwards.

**Up to 4 UB backward, in whole UB steps.**

Backward movement reads the same 3-stud axis and the same limit as forward movement, and costs **1 Action Point** (INF-002).

The unit keeps its facing. No rotation is required.

A Wounded model's limit is lower — see INF-012.

---

# INF-005 — Rotation

Infantry may rotate to any facing.

Rotation does not require measuring.

Rotating costs:

**1 Action Point**

The new facing becomes immediately active.

---

# Terrain

Terrain physically affects infantry movement. What a slope and a stepped surface are built from is `07-movement.md` (MOVE-012, MOVE-013), and what physically supports a unit at all is MOVE-014; what infantry can do with them is below.

## INF-006 — One Brick Obstacles

Height: **up to 3 plate layers**.

Obstacle height is measured in plate layers, the same unit `16-damage-system.md` (DMG-003) uses: a plate counts as 1 and a standard brick as 3.

Infantry may cross freely. No additional movement cost.

---

## INF-007 — Two Brick Obstacles

Height: **4 to 6 plate layers**.

Infantry may climb. Climbing costs **1 additional Action Point** for each such obstacle the move crosses, on top of the movement action itself — so a move over one such obstacle costs **2 AP**.

The climb is part of that movement action and does not increase the movement limit: the full move still counts against the limit its own direction sets — **4 UB** forward or backward (INF-002, INF-004), **3 UB** sideways (INF-003) — or the Wounded model's shorter limit (INF-012).

---

## INF-008 — Three Brick Obstacles

Height: **7 or more plate layers**.

Cannot be climbed directly.

A legal access point is required.

Examples:

- Slopes
- Stairs
- Ramps

Without one of these, the obstacle is impassable.

---

## INF-009 — Slopes and Stairs

Infantry may move normally over connected slopes (`07-movement.md`, MOVE-012) at no additional Action Point cost.

A stepped surface (`07-movement.md`, MOVE-013) is climbed one step at a time. Each step is treated as an obstacle:

- 3 plate layers or fewer: no additional AP (INF-006).
- 4 to 6 plate layers: +1 AP (INF-007).
- 7 or more plate layers: cannot be climbed (INF-008), which stops the climb at that step.

Distance traveled up a slope or a stepped surface counts against the normal movement limit (INF-002).

---

# INF-011 — Falling Damage

Falling and placement are resolved according to `07-movement.md` (MOVE-015).

For infantry, falling damage is based on height fallen, measured in plate layers (`INF-006`).

The first brick (3 plate layers) causes no damage. For every complete brick beyond the first, roll 1D6 as a Damage Roll (`16-damage-system.md`, DMG-014).

Each Damage Roll is resolved independently:

| D6 Result | Result                                                  |
| --------- | ------------------------------------------------------- |
| 1–3       | Damage — advance the faller's Component State one step. |
| 4–6       | No Damage — no effect.                                  |

Falling damage does not use an Impact, so no Geometry Check is made and Resistance does not apply.

Vehicle falling is resolved separately under `08-vehicles.md` (VEH-026).


## Examples

* Fall of 1 brick (3 plate layers) → 0 Damage Rolls.
* Fall of 2 bricks → 1 Damage Roll.
* Fall of 3 bricks → 2 Damage Rolls.
* Fall of 5 bricks → 4 Damage Rolls.
* Fall of 10 bricks → 9 Damage Rolls.

---

# INF-012 — Wounded Movement

A Wounded infantry model (`16-damage-system.md`, DMG-002) moves **at most 2 UB** in whichever direction it travels.

Each direction reads its own axis of the Unit Base (`02-core-rules.md`, CORE-001), so 2 UB is **6 studs forward or backward** (INF-002, INF-004) and **8 studs sideways** (INF-003) — distances those rules already allow, with the longer ones removed.

Nothing else about the move changes. It still costs **1 Action Point**, it still travels in a single direction (`07-movement.md`, MOVE-007), and rotation (INF-005), slopes and stairs (INF-009) and falling (`07-movement.md`, MOVE-015; INF-011) are untouched. Climbing a two-brick obstacle still costs the 1 additional Action Point INF-007 charges — what changes there is the length of the move the climb belongs to, not the climb.

The limit is counted in whole Unit Bases rather than taken as half the normal distance, because half of a 3 UB side move is not a whole Unit Base.

---

# Summary

Infantry in StudCraft follows seven simple principles:

1. An infantry model is a minifigure with two hands, on a base of `4 × 3` studs, one plate thick, whose 4-stud edge is its front.
2. Forward and backward movement is up to 4 UB, read across the Unit Base's 3-stud depth — 12 studs.
3. Side movement is up to 3 UB, read across its 4-stud width — 12 studs.
4. Each movement action costs 1 Action Point, and so does a rotation.
5. Obstacles up to 3 plate layers are crossed freely, 4 to 6 cost 1 additional Action Point each, and 7 or more need a slope, a stair or a ramp — and a stair's own steps are obstacles read the same way.
6. A fall rolls one D6 per complete brick beyond the first, each die a Damage Roll.
7. A Wounded model moves at most 2 UB in any direction — 6 studs forward or backward, 8 sideways.

---

> **Every Brick Matters.**
