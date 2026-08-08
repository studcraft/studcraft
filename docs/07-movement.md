# StudCraft Movement Rules

**Version:** 0.2.0 Draft

---

# Purpose

This document defines how units move across the battlefield.

Movement in StudCraft is entirely based on the physical LEGO model.

Distances are measured using LEGO studs.

No diagonal movement exists.

---

# Design Philosophy

Movement should be:

- Easy to measure.
- Easy to understand.
- Based on the model itself.
- Free from templates and measuring sticks.

Movement always follows the geometry of LEGO studs.

---

# MOVE-001 — Unit Orientation

Every unit has four possible movement directions:

- Forward
- Backward
- Left
- Right

Movement is always performed relative to the current facing of the unit.

Diagonal movement is never allowed.

---

# MOVE-002 — Infantry Base

Every infantry model is built on the base required by `04-construction-standard.md`, SCS-002.

Which edge of that base is its front is settled by the universal Facing rule (`02-core-rules.md`, CORE-002).

The base's orientation defines movement and line of advance.

---

# MOVE-003 — Measuring Movement

Movement is measured along the direction of travel, from the edge of the base that leads in that direction: the front edge moving forward, the rear edge moving backward, and the corresponding side edge moving left or right.

When movement ends, the unit occupies its new position completely.

---

# MOVE-004 — Infantry Movement

Standard infantry movement:

**Up to 12 studs forward, in multiples of 3 studs**

12 is the maximum, not a fixed distance — a unit may move 3, 6, 9 or 12 studs, or stay put.

The step size is the Unit Base's depth (`02-core-rules.md`, CORE-001): moving forward crosses the 3-stud axis, so forward movement counts whole base-depths, exactly as side movement counts whole base-widths of 4 (MOVE-005). Both numbers come from the base itself, so a player can measure either by laying spare infantry bases end to end.

One movement action costs **1 Action Point** (`02-core-rules.md`, CORE-006) and moves the unit in a single direction. Changing direction requires a second movement action (MOVE-007).

Each movement action is measured independently: a unit spending two Action Points on movement makes two separate moves of up to 12 studs each, not one move of 24.

Future scenarios may allow sprinting or other special movement.

---

# MOVE-005 — Side Movement

Infantry may move sideways, left or right.

**Up to 12 studs, in multiples of 4 studs**

The step size is the Unit Base's width (`02-core-rules.md`, CORE-001) — moving sideways crosses the 4-stud axis. Legal distances are therefore 4, 8 and 12 studs. Partial side movement is not allowed.

Side movement is a movement action and costs **1 Action Point**, the same as moving forward (MOVE-004).

---

# MOVE-006 — Backward Movement

Infantry may move backwards.

**Up to 12 studs, in multiples of 3 studs** — the same limit and step size as forward movement (MOVE-004), because backward movement crosses the same 3-stud axis of the base.

The unit keeps its facing. No rotation is required.

Backward movement is a movement action and costs **1 Action Point**.

---

# MOVE-007 — No Diagonal Movement

StudCraft does not use diagonal movement.

Players combine forward and lateral movement instead. Each leg is its own movement action, costing 1 Action Point each.

Example — instead of moving diagonally:

- Forward 6 studs (1 AP)
- Left 4 studs (1 AP)

This maintains compatibility with the LEGO grid, and means a unit with 3 AP can make at most three movement legs in an activation.

---

# MOVE-008 — Rotation

Infantry may rotate to any facing.

Rotation does not require measuring.

Rotating costs:

**1 Action Point**

The new facing becomes immediately active.

---

# Terrain Movement

Terrain physically affects movement.

---

# MOVE-009 — One Brick Obstacles

Height: **up to 3 plate layers** (one brick or less).

Obstacle height is measured in plate layers, the same unit `16-damage-system.md` (DMG-003) uses: a plate counts as 1 and a standard brick as 3.

Infantry may cross freely. No additional movement cost.

---

# MOVE-010 — Two Brick Obstacles

Height: **4 to 6 plate layers** (more than one brick, up to two).

Infantry may climb. Climbing costs **1 additional Action Point** on top of the movement action that crosses the obstacle, so a move over such an obstacle costs 2 AP in total.

The climb is part of that movement action and does not increase the distance the unit may travel: the 12-stud limit (MOVE-004) still applies to the move as a whole.

---

# MOVE-011 — Three Brick Obstacles

Height: **7 or more plate layers** (taller than two bricks).

Cannot be climbed directly.

A legal access point is required.

Examples:

- Slopes
- Plate stairs
- Ramps

Without one of these, the obstacle is impassable.

---

# MOVE-012 — Slopes

Slopes are valid climbing surfaces.

Units may move normally over connected slopes, at no additional Action Point cost — a slope is ordinary terrain, not an obstacle to climb. Distance travelled up a slope counts against the normal movement limit (MOVE-004).

---

# MOVE-013 — Stairs

Plate-built stairs are valid movement paths.

Units may climb them normally, at no additional Action Point cost, and the distance climbed counts against the normal movement limit (MOVE-004) — the same as slopes (MOVE-012).

---

# MOVE-014 — Vertical Access

If no slope, stair or ramp exists, the wall cannot be climbed. These are the three legal access points listed in MOVE-011, and no other construction grants access.

Physical construction determines accessibility.

---

# Falling

---

# MOVE-015 — Falling

A unit that leaves a higher position without support falls. A unit may do this deliberately — stepping off a ledge is a legal way to descend, at the risk described in MOVE-016.

The unit is placed directly below the point it left, at the first surface that physically supports it. Falling immediately ends the movement action; any unspent movement from that action is lost.

---

# MOVE-016 — Falling Damage

Falling damage depends on the height fallen, measured in plate layers — the same unit obstacles use (MOVE-009).

Roll **one D6 for every complete brick (3 plate layers) fallen beyond the first**. A remainder of one or two plate layers adds no die.

The first brick is free, which is why a fall of 3 plate layers or less needs no roll at all: MOVE-009 already treats that height as trivial to cross, and stepping down it is no more dangerous than stepping over it.

Each die is treated as a Damage Roll (`16-damage-system.md`, DMG-015): a result of 4, 5, or 6 means no damage. A result of 1, 2, or 3 advances the faller's Component State one step (`Operational → Wounded`, or `Wounded → Dead`).

The dice are independent and are never pooled, resolved exactly as multiple Impacts are (DMG-016). Two failed dice therefore take an Operational unit to Dead — the higher the fall, the more dice, and the more likely both a wound and a death.

This is a declared exception to the normal sequence: falling has no Impact Strength and no attacker, so there is no Geometry Check (DMG-014) to pass first. The Damage Rolls apply directly, and Resistance plays no part in falling damage.

No height is certainly fatal. A unit that survives a very tall fall has simply passed every Damage Roll, which `16-damage-system.md` (DMG-015) already describes as a fortunate landing rather than an oversight. This is intentional: in StudCraft, geometry can rule an outcome out — the first brick of a fall, like an Impact below a component's Resistance (DMG-014) — but geometry never rules an outcome in. A minifig can survive two cannon Impacts for the same reason it can survive a fall from a tower.

This rule covers infantry only. Vehicle falling is defined separately in `08-vehicles.md` (VEH-026), which scales from each vehicle's own Terrain Threshold rather than from a fixed first brick.

Example:

- Fall of 1 brick (3 plate layers) → no dice, no damage.
- Fall of 2 bricks → Roll 1D6. A failure wounds; a fall this short cannot kill an Operational unit.
- Fall of 3 bricks → Roll 2D6, resolved independently. Two failures kill.
- Fall of 5 bricks → Roll 4D6, resolved independently.
- Fall of 10 bricks → Roll 9D6. Survival is very unlikely.

---

# Vehicle Movement

Vehicle movement depends on:

- Physical dimensions.
- Locomotion type.

Vehicle-specific rules are described in `08-vehicles.md`, including terrain. The Terrain Threshold rules (VEH-021 through VEH-024) give each locomotion type its own limit, read from the model; VEH-025 covers being stranded, VEH-026 falling, and VEH-027 ascent.

Vehicles and infantry differ most at stairs: infantry climb them (MOVE-013), vehicles never do (VEH-027).

---

# MOVE-017 — Collision

Units may not finish movement occupying the same physical space. Models may not overlap.

Friendly units may move around each other if enough space physically exists. Enemy units block movement unless another rule allows otherwise.

---

# MOVE-018 — Doors

Closed doors block movement. Once opened, the doorway becomes a valid movement path for any model the opening physically passes (`05-construction-components.md`, CMP-018).

Opening or closing a door is an interactive element action (`02-core-rules.md`, CORE-007).

---

# MOVE-019 — Ramps

A lowered ramp immediately becomes usable terrain and is a legal access point (MOVE-011, MOVE-014). Where the ramp leads to an opening, that opening must physically pass the model as well (`05-construction-components.md`, CMP-018).

Lowering or raising a ramp is an interactive element action (`02-core-rules.md`, CORE-007).

---

# MOVE-020 — Interactive Terrain

Any movable LEGO element may become part of a movement path.

Examples:

- Drawbridges
- Elevators
- Gates
- Hinged platforms

Operating one is an interactive element action (`02-core-rules.md`, CORE-007).

---

# Physical Priority

If a movement question can be answered by observing the LEGO model,

the model always takes precedence over interpretation.

---

# Summary

Movement in StudCraft is based on six simple principles:

1. No diagonal movement.
2. Infantry move up to 12 studs forward or backward, in multiples of 3.
3. Side movement is up to 12 studs, in multiples of 4.
4. Each movement action costs 1 Action Point and moves in one direction.
5. Walls require physical access — a slope, a stair or a ramp.
6. Physical construction always defines legal movement.

---

> **Every Brick Matters.**