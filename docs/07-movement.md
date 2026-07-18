# StudCraft Movement Rules

**Version:** 0.1.0 Draft

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

All infantry are mounted on a standard Unit Base (UB):

4 × 3 studs

The 4-stud edge is always considered the front.

This orientation defines movement and line of advance.

---

# MOVE-003 — Measuring Movement

Movement is measured from the front edge of the unit.

When movement ends, the unit occupies its new position completely.

Models may not overlap.

---

# MOVE-004 — Infantry Movement

Standard infantry movement:

**12 studs forward**

This equals three Unit Base lengths.

This value represents a normal movement action.

Future scenarios may allow sprinting or other special movement.

---

# MOVE-005 — Side Movement

Infantry may move sideways.

Side movement is measured in multiples of **4 studs**.

This keeps movement aligned with the Unit Base.

Examples:

- 4 studs
- 8 studs
- 12 studs

Partial side movement is not allowed.

---

# MOVE-006 — Backward Movement

Infantry may move backwards using the same movement allowance.

The unit keeps its facing.

No rotation is required.

---

# MOVE-007 — No Diagonal Movement

StudCraft does not use diagonal movement.

Players combine forward and lateral movement instead.

Example:

Instead of moving diagonally:

- Forward 8 studs
- Left 4 studs

This maintains compatibility with the LEGO grid.

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

Height:

1 Brick

Infantry may cross freely.

No additional movement cost.

---

# MOVE-010 — Two Brick Obstacles

Height:

2 Bricks

Infantry may climb.

Climbing costs:

**1 additional Action Point**

on top of the normal movement cost.

---

# MOVE-011 — Three Brick Obstacles

Height:

3 Bricks or more

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

Units may move normally over connected slopes.

---

# MOVE-013 — Stairs

Plate-built stairs are valid movement paths.

Units may climb them normally.

---

# MOVE-014 — Vertical Access

If no slope or stair exists:

The wall cannot be climbed.

Physical construction determines accessibility.

---

# Falling

---

# MOVE-015 — Falling

A unit that leaves a higher position without support falls.

Falling immediately ends movement.

---

# MOVE-016 — Falling Damage

Falling damage depends on the height fallen.

For each brick of height fallen:

Roll one D6.

Keep only the **lowest result**.

The greater the fall, the greater the chance of suffering damage.

Combat rules determine the effects of the result.

Example:

- Fall of 1 brick → Roll 1D6.
- Fall of 2 bricks → Roll 2D6, keep the lowest.
- Fall of 5 bricks → Roll 5D6, keep the lowest.

---

# Vehicle Movement

Vehicle movement depends on:

- Physical dimensions.
- Locomotion type.

Vehicle-specific rules are described in `08-vehicles.md`.

---

# Collision

Units may not finish movement occupying the same physical space.

Friendly units may move around each other if enough space exists.

Enemy units block movement unless another rule allows otherwise.

---

# Doors

Closed doors block movement.

Opening a door costs:

**1 Action Point**

Once opened, the doorway becomes a valid movement path.

---

# Ramps

Lowering or raising a ramp costs:

**1 Action Point**

A lowered ramp immediately becomes usable terrain.

---

# Interactive Terrain

Any movable LEGO element may become part of movement.

Examples:

- Drawbridges
- Elevators
- Gates
- Hinged platforms

Interaction normally costs:

**1 Action Point**

---

# Physical Priority

If a movement question can be answered by observing the LEGO model,

the model always takes precedence over interpretation.

---

# Summary

Movement in StudCraft is based on five simple principles:

1. No diagonal movement.
2. Infantry move 12 studs.
3. Side movement uses multiples of 4 studs.
4. Walls require physical access (slopes or stairs).
5. Physical construction always defines legal movement.

---

> **Every Brick Matters.**