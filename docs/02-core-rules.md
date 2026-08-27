# StudCraft Core Rules

**Version:** 0.2.0 Draft

---

# Purpose

This document defines the universal game rules used by every StudCraft scenario.

These rules apply to all units unless another rule explicitly states otherwise.

---

# Design Philosophy

StudCraft is built around a small set of **universal foundations** shared by every game system.

These foundations provide the common language for how the game measures space, handles actions, determines direction and visibility, and represents game state.

## Universal Foundations

* **Unit Bases (UB)** — the universal spatial measurement.
* **Action Points (AP)** — the universal action economy.
* **Facing** — the common reference for direction and orientation.
* **Physical Visibility** — line of sight is determined by the models and battlefield.
* **Physical Representation** — game state should be represented physically whenever possible.

Systems such as **Movement, Combat, Damage, Weapons, Infantry, and Vehicles** build upon these foundations rather than creating parallel rules.

> **The model supplies the values. The ruleset supplies the procedures.**


---

# The Battlefield

StudCraft is played using LEGO terrain and models.

Everything placed on the table is considered part of the battlefield.

Examples:

* Buildings
* Vehicles
* Walls
* Bridges
* Doors
* Ramps
* Terrain

Only physical LEGO elements may affect gameplay.

---

# CORE-001 — Unit Base (UB)

StudCraft uses a single universal spatial measurement.

One **Unit Base (UB)** is a volume measuring:

**4 studs wide × 3 studs deep × 13 plate layers tall**

Read horizontally, it is `4 × 3` studs.

Height is counted in plate layers, the ruleset's vertical unit: a plate counts as 1 and a standard brick as 3 (`16-damage-system.md`, DMG-003; `08-vehicles.md`, VEH-021). It is measured from the underside of the base a model stands on, which is part of the volume rather than the floor beneath it.

A footprint written `W × D UB` counts 4-stud widths by 3-stud depths, so a `2 × 3 UB` footprint measures `8 × 9` studs.

A distance written `N UB` counts N Unit Bases along the single axis its rule names: 4 UB of depth is 12 studs, 3 UB of width is 12 studs (`17-infantry.md`, INF-002, INF-003).

Each rule states which dimensions of the Unit Base it reads. A measured value never replaces a physical check (`15-geometry-layers.md`, GEO-003, GEO-004).

![CORE-001 — unit base volume](../assets/images/core-001-unit-base-volume.png)

---

# CORE-002 — Facing

Every unit has a facing, and every model must have an obvious front.

Which part of a model is its front is defined by its domain rule — infantry (`17-infantry.md`, INF-001), vehicles (`08-vehicles.md`, VEH-002).

---

# Unit Types

## CORE-003 — Infantry

Infantry are represented by LEGO minifigures.

Infantry occupy one Unit Base.

What an infantry model can do, and how it must be built, is defined by `17-infantry.md`.

---

## CORE-004 — Vehicles

A vehicle is a powered model, and its footprint is defined by the LEGO model itself.

What a vehicle can do, and how it must be built, is defined by `08-vehicles.md`.

---

## CORE-005 — Structures

Buildings, fortifications and scenery are permanent battlefield elements.

A structure's doors, windows and other functional parts follow `05-construction-components.md`. Its walls, slopes, stairs and platforms are terrain governed by `07-movement.md`.

How a unit crosses or occupies these constructions is defined by its domain rules:

* Infantry: `17-infantry.md`
* Vehicles: `08-vehicles.md`

---

# CORE-006 — Action Points

Every unit activates using Action Points (AP).

Action Points represent everything a unit can do during its activation. The rule governing an action defines its AP cost.

Every unit receives exactly **3 Action Points** per activation, regardless of its type or construction. No unit gains additional AP through its profile.

---

# CORE-007 — Physical Interaction

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

Visual Geometry is physically present and therefore affects visibility (`15-geometry-layers.md`, GEO-004).

A transparent element does not block sight. It stops an Impact only through its own Resistance, like any other component (`16-damage-system.md`, DMG-007).

---

## CORE-009 — If You Can See It

> **If you can see it, you can shoot it.**

---

# CORE-010 — Physical Cover

Cover is physical, not templated.

A component that is completely hidden by terrain, another model or Visual Geometry cannot be selected as a target (`15-geometry-layers.md`, GEO-004; `16-damage-system.md`, DMG-011).

A partially visible component has no separate cover level. It is simply visible or it is not.

There is no partial or heavy cover bonus and no abstract cover template.

---

# CORE-014 — Visible Equipment

Equipment must be physically represented.

A unit cannot use equipment that is not present on the model.

---

# CORE-016 — Battlefield Representation

Whenever possible, changes in game state should be represented by modifying the model itself.

StudCraft prefers physical representation over markers.

---

# Universal Rule

When rules from different levels conflict, the higher level takes precedence:

1. Foundations
2. Core Rules
3. Scenario Rules

This hierarchy ranks these three levels only. System documents such as Movement, Vehicles and Damage define the rules for their own subjects.

The physical model is the source of every physical fact read by the rules.

---

> **Every Brick Matters.**
