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

**Up to 12 studs forward, in multiples of 3 studs**

12 is the maximum, not a fixed distance — a unit may move 3, 6, 9 or 12 studs, or stay put.

The step size is the Unit Base's depth (`02-core-rules.md`, CORE-001): moving forward crosses the 3-stud axis, so forward movement counts whole base-depths, exactly as side movement counts whole base-widths of 4 (INF-003). Both numbers come from the base itself, so a player can measure either by laying spare infantry bases end to end.

The distance is measured from the face of the base that leads in the direction of travel — the front face moving forward, the rear face moving backward (INF-004), the corresponding side face moving sideways (INF-003). This is the general measurement rule (`07-movement.md`, MOVE-003) read against an infantry base.

One movement action costs **1 Action Point** (`02-core-rules.md`, CORE-006) and moves the unit in a single direction. Changing direction requires a second movement action (`07-movement.md`, MOVE-007).

Each movement action is measured independently: a unit spending two Action Points on movement makes two separate moves of up to 12 studs each, not one move of 24.

A Wounded model's limit is lower — see INF-012.

Future scenarios may allow sprinting or other special movement.

---

# INF-003 — Side Movement

Infantry may move sideways, left or right.

**Up to 12 studs, in multiples of 4 studs**

The step size is the Unit Base's width (`02-core-rules.md`, CORE-001) — moving sideways crosses the 4-stud axis. Legal distances are therefore 4, 8 and 12 studs. Partial side movement is not allowed.

Side movement is a movement action and costs **1 Action Point**, the same as moving forward (INF-002).

Infantry reaches an off-axis position by combining a forward or backward move with a side move, each its own movement action (`07-movement.md`, MOVE-007).

Example — instead of moving diagonally:

- Forward 6 studs (1 AP)
- Left 4 studs (1 AP)

A Wounded model's limit is lower — see INF-012.

---

# INF-004 — Backward Movement

Infantry may move backwards.

**Up to 12 studs, in multiples of 3 studs** — the same limit and step size as forward movement (INF-002), because backward movement crosses the same 3-stud axis of the base.

The unit keeps its facing. No rotation is required.

Backward movement is a movement action and costs **1 Action Point**.

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

Height: **up to 3 plate layers** (one brick or less).

Obstacle height is measured in plate layers, the same unit `16-damage-system.md` (DMG-003) uses: a plate counts as 1 and a standard brick as 3.

Infantry may cross freely. No additional movement cost.

---

## INF-007 — Two Brick Obstacles

Height: **4 to 6 plate layers** (more than one brick, up to two).

Infantry may climb. Climbing costs **1 additional Action Point** on top of the movement action that crosses the obstacle, so a move over such an obstacle costs 2 AP in total.

The climb is part of that movement action and does not increase the distance the unit may travel: the limit on that move still applies as a whole — 12 studs (INF-002), or a Wounded model's shorter limit (INF-012).

---

## INF-008 — Three Brick Obstacles

Height: **7 or more plate layers** (taller than two bricks).

Cannot be climbed directly.

A legal access point is required.

Examples:

- Slopes
- Stairs
- Ramps

Without one of these, the obstacle is impassable.

---

## INF-009 — Slopes and Stairs

Infantry may move normally over connected slopes (`07-movement.md`, MOVE-012) at no additional Action Point cost: a slope is ordinary terrain, not an obstacle to climb.

A stepped surface (`07-movement.md`, MOVE-013) is climbed one step at a time, and each step is an obstacle read exactly like any other — 3 plate layers or fewer crossed freely (INF-006), 4 to 6 for 1 additional Action Point (INF-007), 7 or more not climbable at all (INF-008), which stops the climb at that step. Stairs built from steps of a plate or two therefore cost nothing.

**Each such step is charged.** A move crossing two steps of 4 to 6 plate layers spends the movement action's Action Point and 2 more, because it climbed two obstacles and not one — INF-007's "2 AP in total" counts one climb, which is the ordinary case rather than the only one. A staircase steep enough to charge for twice is one a unit may not finish in a single activation, which the 3 Action Points of `02-core-rules.md` (CORE-006) bound on their own.

Distance traveled up either counts against the normal movement limit (INF-002).

A vehicle reads the same staircase as one obstacle of its total rise rather than a series of small ones (`08-vehicles.md`, VEH-027): infantry takes the steps and a vehicle cannot.

---

## INF-010 — Vertical Access

A vertical face taller than INF-008's threshold cannot be climbed unless a slope, stair or ramp physically reaches it. Those are the three legal access points INF-008 lists, and no other construction grants access.

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

A Wounded infantry model (`16-damage-system.md`, DMG-002) moves **at most two steps** in whichever direction it travels.

The step is the one that direction already uses (`02-core-rules.md`, CORE-001): the Unit Base's 3-stud depth forward and backward (INF-002, INF-004), and its 4-stud width sideways (INF-003). So a Wounded model may move **up to 6 studs forward or backward** and **up to 8 studs sideways** — distances those rules already allow, with the longer ones removed.

Nothing else about the move changes. It still costs **1 Action Point**, it still travels in a single direction (`07-movement.md`, MOVE-007), and rotation (INF-005), slopes and stairs (INF-009) and falling (`07-movement.md`, MOVE-015; INF-011) are untouched. Climbing a two-brick obstacle still costs the 1 additional Action Point INF-007 charges — what changes there is the length of the move the climb belongs to, not the climb.

The limit is counted in steps rather than taken as half the normal distance because half of a side move is 6 studs, which INF-003 does not allow. A fraction of a legal distance is not always a legal distance; a count of steps always is.

---

# Summary

Infantry in StudCraft follows seven simple principles:

1. An infantry model is a minifigure with two hands, on a base of `4 × 3` studs, one plate thick, whose 4-stud edge is its front.
2. Forward and backward movement is up to 12 studs, in multiples of 3.
3. Side movement is up to 12 studs, in multiples of 4.
4. Each movement action costs 1 Action Point, and so does a rotation.
5. Obstacles up to 3 plate layers are crossed freely, 4 to 6 cost 1 additional Action Point, and 7 or more need a slope, a stair or a ramp — and a stair's own steps are obstacles read the same way.
6. A fall rolls one D6 per complete brick beyond the first, each die a Damage Roll.
7. A Wounded model moves at most two steps in any direction — 6 studs forward or backward, 8 sideways.

---

> **Every Brick Matters.**
