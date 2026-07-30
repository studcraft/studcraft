# StudCraft Core Rules

**Version:** 0.1.0 Draft

---

# Purpose

This document defines the universal game rules used by every StudCraft scenario.

These rules apply to all units unless another rule explicitly states otherwise.

---

# The Battlefield

StudCraft is played using LEGO terrain and models.

Everything placed on the table is considered part of the battlefield.

Examples:

- Buildings
- Vehicles
- Walls
- Bridges
- Doors
- Ramps
- Terrain

Only physical LEGO elements may affect gameplay.

---

# Unit Base

## CORE-001 — Unit Base (UB)

StudCraft uses a single measuring unit.

One **Unit Base (UB)** is a LEGO Plate measuring:

**4 × 3 studs**

This is the standard base for infantry. The 4-stud edge is the front (CORE-002).

All distances, deployment areas and vehicle footprints are expressed using this unit. When a footprint is written as `W × D` UB (e.g. "Jeep: 2 × 3 UB"), the first number is a count of 4-stud widths and the second a count of 3-stud depths — a `2 × 3 UB` footprint measures `8 × 9` studs, not `6 × 12`.

---

# Unit Orientation

## CORE-002 — Facing

Every unit has a facing.

For infantry:

The 4-stud side of the base is the front.

For vehicles:

The front is determined by the vehicle construction.

Facing determines:

- Forward movement
- Rear movement
- Left side
- Right side
- Front firing arcs
- Rear firing arcs
- Shield direction

---

# Unit Types

## CORE-003 — Infantry

Infantry are represented by LEGO minifigures mounted on a standard Unit Base.

Infantry occupy one Unit Base.

---

## CORE-004 — Vehicles

Vehicles occupy one or more Unit Bases.

Their footprint is defined by the LEGO model itself.

Vehicle movement and transport capacity are described in the Vehicle Rules.

---

## CORE-005 — Structures

Buildings, fortifications and scenery are permanent battlefield elements.

Structures follow the Construction Standard. Structure-specific damage (collapse, breaching walls) and Deployment Area occupation for scenario-placed structures are not yet defined — a structure's individual components (doors, windows, walls) already resolve Impacts through the standard Component Damage System (`16-damage-system.md`) like any other component; only structure-wide consequences (e.g. a building collapsing) remain future work.

---

# Activation

## CORE-006 — Action Points

Every unit activates using Action Points (AP).

Action Points represent everything a unit can do during its activation.

Examples include:

- Move
- Fire
- Open a door
- Close a door
- Embark
- Disembark
- Stand up (see `16-damage-system.md`, DMG-019, Repairs)
- Reload (future rule)
- Operate mechanisms

Every unit receives exactly **3 Action Points** per activation, regardless of its type or construction. No unit gains additional AP through its profile.

---

# Interactive Elements

## CORE-007 — Physical Interaction

Any LEGO element that can physically move may become interactive.

Examples:

- Doors

- Gates

- Drawbridges

- Ramps

- Hatches

- Elevators

Opening or closing an interactive element costs:

**1 Action Point**

unless another rule specifies otherwise.

---

# Line of Sight

## CORE-008 — Physical Visibility

StudCraft uses true line of sight.

A target is visible if any part of it can be physically seen from the attacker's point of view.

No visibility templates are used.

This includes Visual Geometry (decoration, greebling, and similar) — see `15-geometry-layers.md` (GEO-004).

---

## CORE-009 — If You Can See It

Fundamental combat rule:

> If you can see it, you can shoot it.

This is symmetric: if it can see you, you can be its target during its own activation (`03-game-flow.md`, FLOW-002). It does not grant a shot outside of a unit's own activation — StudCraft has no reaction fire (`11-combat.md`, CBT-014 lists it as a possible future extension, not a current rule).

---

# Cover

## CORE-010 — Physical Cover

Cover is physical, not templated: a component that is completely hidden — by terrain, another model, or Visual Geometry (`15-geometry-layers.md`, GEO-004) — cannot be selected as a target (`16-damage-system.md`, DMG-012).

A partially visible component has no separate cover level; it is simply visible or it isn't. There is no partial or heavy cover bonus, and no abstract cover template.

---

# Infantry States

Infantry uses the universal Component State machine (`16-damage-system.md`, DMG-005) exactly like any other component — CORE-011/012/013 describe the infantry-specific physical representation of each state, not a separate state system.

## CORE-011 — Operational

The minifigure stands upright.

The unit functions normally.

---

## CORE-012 — Wounded

The minifigure is placed in a seated position, representing an injured soldier.

The seated position is the game marker. No additional token is required.

A Wounded unit has no penalty of any kind — it moves, attacks, rotates, and climbs exactly as if Operational (`16-damage-system.md`, DMG-005: Wounded "continues to function normally"). The seated pose is purely a visual marker. The only consequence of Wounded is that the next successful Impact advances the minifigure to Dead (`11-combat.md`, CBT-008), the same as any other component.

---

## CORE-013 — Dead

The minifigure is physically removed from the battlefield — the same removal every component undergoes on reaching Dead (`16-damage-system.md`, DMG-006). No casualty marker is used; removal is the marker.

Dead units no longer participate in the game and no longer block movement, Line of Sight, or provide Cover.

---

# Equipment

## CORE-014 — Visible Equipment

Equipment must be physically represented.

A unit cannot use equipment that is not present on the model.

Examples:

Weapons

Shields

Backpacks

Tools

Medical packs

Special devices

---

## CORE-015 — Hands

A minifigure may only use equipment it can physically carry.

As a general guideline:

One hand carries one one-handed item.

Examples:

- Pistol
- Sword
- Knife
- Shield

Two-handed equipment occupies both hands.

Examples:

- Rifle
- Heavy Machine Gun
- Rocket Launcher

The physical model determines what the unit carries.

---

# Physical State

## CORE-016 — Battlefield Representation

Whenever possible, changes in game state should be represented by modifying the model itself.

Examples:

A wounded soldier sits.

A dead soldier is removed.

A destroyed weapon is removed.

A broken window loses its transparent brick.

An opened door is physically opened.

StudCraft always prefers physical representation over markers.

---

# Universal Rule

Whenever a conflict exists between:

- written rules
- physical construction

the following priority applies:

1. Foundations
2. Core Rules
3. Construction Standards
4. Scenario Rules

---

# Design Notes

These rules intentionally avoid introducing statistics.

The goal of StudCraft is for players to understand the battlefield simply by observing the LEGO models.

The physical model is always the primary source of truth.

---

> **Every Brick Matters.**