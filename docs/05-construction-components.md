# StudCraft Construction Components

**Version:** 0.1.0 Draft

---

# Purpose

This document defines the functional construction components used in StudCraft.

Components are physical LEGO elements that provide gameplay functionality.

A component only has a game effect if it complies with the construction rules defined in this document.

---

# Design Philosophy

StudCraft uses construction instead of hidden statistics.

Players should be able to identify the purpose of every important component simply by looking at the model.

Components define capabilities.

They do not define abstract statistics.

---

# CMP-001 — Functional Components

A functional component is a physical part of a model that affects gameplay.

Examples include:

- Pilot
- Wheels
- Tracks
- Hover systems
- Weapons
- Doors
- Windows
- Ramps
- Turrets
- Cargo Bays

Decorative elements have no gameplay effect.

---

# CMP-002 — Pilot

Every powered vehicle must include a visible Pilot position, occupied by a crew minifigure (`08-vehicles.md`, VEH-015).

Requirements:

- The Pilot must be a distinct, visible minifigure in an operating position.
- A decorative "empty seat" does not count as a Pilot.

Current gameplay:

- Required for all powered vehicles.
- Losing the Pilot disables vehicle movement (`08-vehicles.md`, VEH-013).

---

# CMP-003 — Wheels

Wheels define wheeled locomotion.

Requirements:

- Must physically touch the ground.
- Must rotate freely.
- Decorative wheels are ignored.

Movement is resolved using the Vehicle Movement Rules. Terrain behaviour follows `08-vehicles.md` (VEH-022) — a wheel's axle height is its Terrain Threshold.

---

# CMP-004 — Tracks

Tracks define tracked locomotion.

Requirements:

- Must be physically represented.
- Both sides should contain tracks.
- Decorative track details have no effect.

Pivot behavior follows `08-vehicles.md` (VEH-009), and terrain behaviour (VEH-022).

---

# CMP-005 — Hover System

Hover vehicles replace wheels or tracks with hover emitters.

Hover components must be visually distinguishable.

Hover vehicles ignore wheel requirements. Pivot and movement behavior follows `08-vehicles.md` (VEH-011), and terrain behaviour (VEH-024) — the height of the hover assembly is the vehicle's Terrain Threshold, which is why these components must be visible.

---

# CMP-006 — Walkers

Walkers use articulated legs instead of wheels or tracks.

Requirements:

- Legs must visibly support the vehicle.
- Decorative legs have no gameplay effect.

Pivot behavior follows `08-vehicles.md` (VEH-010), and terrain behaviour (VEH-023) — a walker's knee height is its Terrain Threshold.

---

# CMP-007 — Weapons

Weapons are defined separately in:

`10-weapons.md`

Construction determines:

- Weapon length
- Range
- Attack Dice
- Firing direction

Only physically represented weapons may attack.

---

# CMP-008 — Turrets

A turret is any rotating weapon mount.

Requirements:

- Must physically rotate.
- Rotation should be visible.
- Weapons mounted on the turret rotate with it.

Turrets follow the normal rotation rules.

---

# CMP-009 — Doors

Doors are interactive components.

Requirements:

- Must physically open and close.
- Decorative doors have no gameplay effect.

Doors are used for:

- Embarking
- Disembarking
- Entering buildings
- Line of Sight

Opening or closing a door costs **1 Action Point** (see `02-core-rules.md`, CORE-007).

---

# CMP-010 — Ramps

Ramps function like doors.

Requirements:

- Must physically move.
- Decorative ramps have no effect.

Ramps may serve as vehicle access points.

Lowering or raising a ramp costs **1 Action Point** (see `02-core-rules.md`, CORE-007).

---

# CMP-011 — Windows

Transparent LEGO elements represent windows, per the Construction Standard (`04-construction-standard.md`, SCS-009).

Windows:

- Allow visibility.
- May provide firing positions.
- Resolve Impacts like any other component (`16-damage-system.md`).

---

# CMP-012 — Cargo Bays

Cargo Bays transport Unit Bases.

Capacity is determined entirely by the available internal space.

Cargo Bays never have an abstract transport value.

---

# CMP-013 — Crew Compartments

Driver positions are separate from Cargo Bays.

Crew compartments:

- Occupy Unit Bases.
- Are not counted as cargo capacity.
- Must be physically represented.

---

# CMP-014 — Shields

A Shield is defensive equipment carried by infantry — a physical component that may be targeted or may interpose to protect a component behind it, exactly like any other component (`16-damage-system.md`, DMG-007, DMG-012).

Requirements:

- Must be physically attached to the model.
- Must remain visible.
- Must occupy one hand.

A shield provides no bonus beyond being a component in the way — its own Resistance (DMG-003) determines what it takes to get through it.

---

# CMP-015 — Accessories

Accessories are decorative unless another rule specifically defines them.

Examples:

- Antennas
- Lights
- Exhausts
- Mirrors
- Decorative panels

These components have no gameplay effect by default.

---

# CMP-016 — Functional Integrity

Removing a functional component immediately changes the model's capabilities.

Examples:

Pilot lost

→ Vehicle cannot move.

Remove Weapon

→ Weapon cannot attack.

Destroy Door

→ Door can no longer function normally.

Gameplay always reflects the current physical model.

---

# CMP-017 — Component Visibility

Functional components should be easy to identify.

Players should not need to ask whether a component exists.

Good construction communicates functionality clearly.

---

# Summary

StudCraft components provide gameplay through physical construction.

Components define what a model can do.

If a component is removed, damaged or destroyed, the model immediately behaves differently.

StudCraft therefore treats every important brick as a meaningful part of the game.

---

> **Every Brick Matters.**