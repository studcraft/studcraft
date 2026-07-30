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

Every motorized vehicle must include a visible Pilot position, occupied by a crew minifigure (`08-vehicles.md`, VEH-015).

Requirements:

- The Pilot must be a distinct, visible minifigure in an operating position.
- A decorative "empty seat" does not count as a Pilot.

Current gameplay:

- Required for all motorized vehicles.
- Losing the Pilot disables vehicle movement (`08-vehicles.md`, VEH-013).

---

# CMP-003 — Wheels

Wheels define wheeled locomotion.

Requirements:

- Must physically touch the ground.
- Must rotate freely.
- Decorative wheels are ignored.

Movement is resolved using the Vehicle Movement Rules.

---

# CMP-004 — Tracks

Tracks define tracked locomotion.

Requirements:

- Must be physically represented.
- Both sides should contain tracks.
- Decorative track details have no effect.

Tracked vehicles pivot around the centre of the model.

---

# CMP-005 — Hover System

Hover vehicles replace wheels or tracks with hover emitters.

Hover components must be visually distinguishable.

Hover vehicles:

- Ignore wheel requirements.
- Pivot around the centre.
- Follow Hover Movement Rules.

---

# CMP-006 — Walkers

Walkers use articulated legs instead of wheels or tracks.

Requirements:

- Legs must visibly support the vehicle.
- Decorative legs have no gameplay effect.

Walkers pivot around the centre of the model.

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
- Follow the Material Rules for transparent elements.

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

A Shield is defensive equipment carried by infantry.

Requirements:

- Must be physically attached to the model.
- Must remain visible.
- Must occupy one hand.

Shield effects are defined in future Equipment Rules.

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