# StudCraft Movement Rules

**Version:** 0.2.0 Draft

---

# Purpose

This document defines the movement mechanics every unit shares.

Movement in StudCraft is entirely based on the physical LEGO model.

Distances are measured using LEGO studs.

No diagonal movement exists.

How far a particular unit moves, and what terrain it can cross, is stated by its own domain — `17-infantry.md` for infantry, `08-vehicles.md` for vehicles.

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

Movement is always performed relative to the current facing of the unit (`02-core-rules.md`, CORE-002).

Which directions a unit may move in is its own domain's rule: infantry moves forward, backward, left and right (`17-infantry.md`, INF-002 through INF-004), while a vehicle moves forward and in reverse and changes direction by turning (`08-vehicles.md`, VEH-005, VEH-006, VEH-008 through VEH-011).

---

# MOVE-003 — Measuring Movement

Movement is measured along the direction of travel, and the whole distance is measured from one point on the model, not from wherever the model happens to be widest.

Where that point is, is its own domain's rule — infantry measures from the face of its base that leads in the direction of travel (`17-infantry.md`, INF-002), a vehicle from its front along its facing (`08-vehicles.md`, VEH-004).

When movement ends, the unit occupies its new position completely.

---

# MOVE-007 — No Diagonal Movement

StudCraft does not use diagonal movement.

A unit reaches an off-axis position by combining the movement and turns allowed by its own domain — infantry combines forward or backward movement with sideways movement (`17-infantry.md`, INF-003), while vehicles combine forward movement with turns (`08-vehicles.md`, VEH-007). Each movement leg is a separate movement action and costs 1 Action Point.

> **No diagonal movement.**

---

# Terrain Movement

Terrain physically affects movement.

## MOVE-012 — Slopes

A slope is built from LEGO slope elements, and is a valid climbing surface.

Whether a given unit may ascend one is its own domain's question — infantry (`17-infantry.md`, INF-009), vehicles (`08-vehicles.md`, VEH-027).

---

## MOVE-013 — Stairs

A stepped surface is terrain built from discrete steps, whatever the steps are built from, and each step has a measurable height.

Whether a given unit may climb one is its own domain's question — infantry (`17-infantry.md`, INF-009), vehicles never (`08-vehicles.md`, VEH-027).

---

## MOVE-014 — Vertical Access

Any stable LEGO surface may support a unit, and physical construction determines accessibility.

Which constructions grant a given unit access is its own domain's question — infantry (`17-infantry.md`, INF-008, INF-010), vehicles (`08-vehicles.md`, VEH-021, VEH-027).

---

# MOVE-015 — Falling

A unit that leaves a higher position without support falls. A unit may do this deliberately — stepping off a ledge is a legal way to descend, at the risk its own domain's rule describes — infantry (`17-infantry.md`, INF-011), vehicles (`08-vehicles.md`, VEH-026).

The unit is placed directly below the point it left, at the first surface that physically supports it. Falling immediately ends the movement action; any unspent movement from that action is lost.

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

A lowered ramp immediately becomes usable terrain (MOVE-014). Whether it grants a given unit access is its own domain's question — infantry (`17-infantry.md`, INF-008), vehicles (`08-vehicles.md`, VEH-027). Where the ramp leads to an opening, that opening must physically pass the model as well (`05-construction-components.md`, CMP-018).

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
2. A distance is measured along the direction of travel, from one point on the model.
3. Each movement action costs 1 Action Point and moves in one direction.
4. A unit that leaves a height without support falls, and lands on the first surface that supports it.
5. Physical construction always defines legal movement, and models may not overlap.
6. How far a unit moves, and what terrain it can cross, is its own domain's rule — `17-infantry.md`, `08-vehicles.md`.

---

> **Every Brick Matters.**