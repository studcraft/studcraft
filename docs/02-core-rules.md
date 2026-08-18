# StudCraft Core Rules

**Version:** 0.2.0 Draft

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

One **Unit Base (UB)** is a volume measuring:

**4 studs wide × 3 studs deep × 13 plate layers tall**

Read horizontally it is `4 × 3` studs.

Height is counted in plate layers, the ruleset's vertical unit: a plate counts as 1 and a standard brick as 3 (`16-damage-system.md`, DMG-003; `08-vehicles.md`, VEH-021). It is measured from the underside of the base a model stands on, which is part of the volume rather than the floor beneath it.

All distances, Deployment Volumes and footprints are expressed using this unit. A footprint written `W × D` UB counts 4-stud widths by 3-stud depths, so a `2 × 3 UB` footprint measures `8 × 9` studs, not `6 × 12`.

Each rule states which dimensions of the Unit Base it reads, and a measured value never replaces a physical check (`15-geometry-layers.md`, GEO-003, GEO-004).

---

# Unit Orientation

## CORE-002 — Facing

Every unit has a facing, and every model must have an obvious front.

Which part of a model is its front is its own domain's rule — infantry (`17-infantry.md`, INF-001), vehicles (`08-vehicles.md`, VEH-002).

---

# Unit Types

## CORE-003 — Infantry

Infantry are represented by LEGO minifigures.

Infantry occupy one Unit Base.

What an infantry model can do, and how it must be built, is an infantry rule — `17-infantry.md`.

---

## CORE-004 — Vehicles

A vehicle is a powered model, and its footprint is defined by the LEGO model itself.

What a vehicle can do, and how it must be built, is a vehicle rule — `08-vehicles.md`.

---

## CORE-005 — Structures

Buildings, fortifications and scenery are permanent battlefield elements.

A structure's doors, windows and other functional parts follow `05-construction-components.md`, like any other model's; its walls, slopes, stairs and platforms are terrain — `07-movement.md` (MOVE-012 through MOVE-014) states what those constructions are — and how a unit crosses or stands on them is its own domain's rule: `17-infantry.md` (INF-006 through INF-010) for infantry, `08-vehicles.md` (VEH-021 through VEH-024, VEH-027) for vehicles. Structure-specific damage (collapse, breaching walls) and Deployment Volume occupation for scenario-placed structures are not yet defined — a structure's individual components (doors, windows, walls) already resolve Impacts through the standard Component Damage System (`16-damage-system.md`) like any other component; only structure-wide consequences (e.g. a building collapsing) remain future work.

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

**No Action Point cost scales with size** — not with the size of the unit paying it, and not with the size of an interactive element it operates (CORE-007). An action's cost is set by the rule that governs that action, and where more than one Action Point is spent that rule states why; the reason is never size. A measurement may still decide **which** rule applies, and which measurement is read is the unit's own domain's rule — an obstacle's height for infantry (`17-infantry.md`, INF-006 through INF-008), a Terrain Threshold for a vehicle (`08-vehicles.md`, VEH-021).

---

# Interactive Elements

## CORE-007 — Physical Interaction

Any LEGO element that can physically move may become interactive.

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

A transparent element does not block sight. It stops an Impact only by its own Resistance, like any other component (`16-damage-system.md`, DMG-008).

---

## CORE-009 — If You Can See It

Fundamental combat rule:

> If you can see it, you can shoot it.

---

# Cover

## CORE-010 — Physical Cover

Cover is physical, not templated: a component that is completely hidden — by terrain, another model, or Visual Geometry (`15-geometry-layers.md`, GEO-004) — cannot be selected as a target (`16-damage-system.md`, DMG-012).

A partially visible component has no separate cover level; it is simply visible or it isn't. There is no partial or heavy cover bonus, and no abstract cover template.

---

# Equipment

## CORE-014 — Visible Equipment

Equipment must be physically represented.

A unit cannot use equipment that is not present on the model.

---

# Physical State

## CORE-016 — Battlefield Representation

Whenever possible, changes in game state should be represented by modifying the model itself.

StudCraft always prefers physical representation over markers.

---

# Universal Rule

When rules from different levels conflict, the higher level takes precedence:

1. Foundations
2. Core Rules
3. Scenario Rules

The order ranks these three levels only. A system document — Movement, Vehicles, Damage and the rest — is not a level in it; it states the rules for its own subject.

The physical model is the source of every physical fact these rules read; this order settles which rule reads it and what it means.

---

> **Every Brick Matters.**