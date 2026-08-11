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

Read horizontally, this is the size of the physical base an infantry model is built on — required by `04-construction-standard.md`, SCS-002. The 4-stud edge is the front (CORE-002).

Height is counted in plate layers because that is the ruleset's vertical unit — a plate counts as 1 and a standard brick as 3 (`16-damage-system.md`, DMG-003; `08-vehicles.md`, VEH-021). Thirteen plate layers is therefore 4 bricks and a plate. Height is measured from the underside of the base an infantry model stands on: that base is part of the volume, not the floor beneath it.

The height is read from the model rather than chosen. Infantry occupies exactly one Unit Base whether standing or seated (`09-transport.md`, TRN-002), so a Unit Base must contain a standing minifigure on the base it is built on (`04-construction-standard.md`, SCS-002): 4 bricks from its feet to the top of its head, and one plate beneath them. Thirteen plate layers is that model, base included, and a Unit Base is the minimum operational space an object needs (`09-transport.md`, TRN-001), so it takes that and no more. **The stud on top of the minifigure's head is not counted here.** The counts in the paragraph above are stacking heights: a stud sits inside the piece above it rather than adding to the stack, and this measurement is taken the same way. Nor do headgear, weapons or equipment change the figure — infantry occupies exactly one Unit Base whatever it carries (`09-transport.md`, TRN-002).

**What must fit is the Unit Base.** Wherever a rule asks whether something physically fits — a passenger, a crew member, cargo, a model passing an opening — the volume that must fit is the Unit Base: one for a minifigure, its own volume in Unit Bases for a vehicle (`04-construction-standard.md`, SCS-005). Never the loose model. A minifigure that would slip into a smaller gap than its Unit Base does not fit there.

**Projections.** A rule never reads more of the volume than it needs:

| Reading | Used by |
|---|---|
| Horizontal projection — `4 × 3` studs | Distances, movement, deployment floors, footprints |
| The volume itself — `4 × 3` studs by 13 plate layers | Transport capacity, interior space, and the Deployment Volume a model must fit inside |
| Vertical projection — 4 studs by 13 plate layers | Passing through an opening |

The vertical projection is taken across the front, because the 4-stud edge is the front (CORE-002) and it is what enters an opening first.

A projection supplies a measured value and nothing else — the boundary `15-geometry-layers.md` draws (GEO-003).

It never replaces a physical check. Line of Sight (CORE-008) and Cover (CORE-010) are resolved against the plastic actually on the table, never against a Unit Base's silhouette (`15-geometry-layers.md`, GEO-004).

All distances, Deployment Volumes and vehicle footprints are expressed using this unit. When a footprint is written as `W × D` UB (e.g. "Jeep: 2 × 3 UB"), the first number is a count of 4-stud widths and the second a count of 3-stud depths — a `2 × 3 UB` footprint measures `8 × 9` studs, not `6 × 12`. A footprint is a horizontal reading, and says nothing about how tall a model actually is — though for a vehicle it does bound how tall the model may be (`08-vehicles.md`, VEH-028).

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

Infantry are represented by LEGO minifigures.

Infantry occupy one Unit Base.

---

## CORE-004 — Vehicles

A powered vehicle occupies two or more Unit Bases.

One of those is taken by its Pilot, who occupies a Unit Base like any other crew member (`09-transport.md`, TRN-014) and is required for the vehicle to move at all (`08-vehicles.md`, VEH-013). A single-Unit-Base vehicle would be entirely filled by its own driver, with no vehicle left around them.

Its footprint is defined by the LEGO model itself.

Vehicle movement and transport capacity are described in the Vehicle Rules.

---

## CORE-005 — Structures

Buildings, fortifications and scenery are permanent battlefield elements.

Structures follow the Construction Standard. Structure-specific damage (collapse, breaching walls) and Deployment Volume occupation for scenario-placed structures are not yet defined — a structure's individual components (doors, windows, walls) already resolve Impacts through the standard Component Damage System (`16-damage-system.md`) like any other component; only structure-wide consequences (e.g. a building collapsing) remain future work.

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

**No Action Point cost scales with size.** Not with the size of the unit paying it — its footprint, its height, or the Unit Bases it occupies: an infantry model and a motorcycle pay the same to embark (`09-transport.md`, TRN-005). Not with the size of an interactive element it operates (CORE-007): a hatch and a cargo ramp cost the same to open. The allotment above is fixed, so a price that grew with the model would put a large enough model beyond acting at all — forbidden by arithmetic rather than by a rule, which is not how this ruleset forbids anything. A measurement may still decide **which** rule applies: an obstacle of 3 plate layers is crossed freely and one of 4 is climbed (`07-movement.md`, MOVE-009, MOVE-010). And where more than one Action Point is spent, the reason is stated in the rule that spends it and is never size — `11-combat.md`, CBT-001 charges per weapon system attacking, `08-vehicles.md`, VEH-008 per 90° turn, and MOVE-010 charges the climb itself: the second Action Point buys crossing the obstacle, not the obstacle's height.

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

Infantry uses the universal Component State machine (`16-damage-system.md`, DMG-005) exactly like any other component — CORE-011/012/013 describe the infantry-specific physical representation of each state, and what Wounded costs an infantry model, not a separate state system.

## CORE-011 — Operational

The minifigure stands upright.

The unit functions normally.

---

## CORE-012 — Wounded

The minifigure is placed in a seated position, representing an injured soldier.

The seated position is the game marker. No additional token is required.

A Wounded minifigure's movement is reduced — `07-movement.md` (MOVE-021) states by how much. Its own movement is the only thing reduced: it rotates and falls exactly as if Operational, and a climb still costs the additional Action Point MOVE-010 charges, on top of a move that is now shorter. The weapons it carries are components in their own right and are degraded only when they are themselves Wounded (`11-combat.md`, CBT-015) — but an unarmed attack is the one attack whose weapon system is the minifigure itself (`12-melee.md`, MEL-008), so a Wounded minifigure punches worse, and CBT-015 says by how much. The seated pose is the marker for all of it — a seated model moves less, and the next successful Impact advances it to Dead (`16-damage-system.md`, DMG-005), the same as any other component.

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