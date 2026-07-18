# StudCraft Material Response System

**Version:** 0.1.0 Draft

---

# Purpose

This document defines how battlefield objects respond to Impacts.

Weapons never determine damage.

Weapons only generate Impacts.

Every target resolves those impacts according to its own material properties.

This makes materials one of the core mechanics of StudCraft.

---

# Design Philosophy

StudCraft does not classify targets by "Hit Points".

Instead, every object on the battlefield is built from LEGO.

Those LEGO elements represent different materials.

Each material responds differently when struck.

---

# MAT-001 — Material Ownership

Every visible component belongs to one material type.

Examples:

- Infantry
- Glass
- Wood
- Stone
- Metal
- Organic

A component can only belong to one primary material.

Armour is not a material. It is a modifier that changes how a component resolves Impacts, defined in MAT-011.

---

# MAT-002 — Physical Components

Impacts are resolved against visible physical components.

Examples:

- Door
- Window
- Wall
- Wheel
- Turret
- Hull
- Soldier

Players target components, not abstract health pools.

---

# MAT-003 — Glass

Transparent LEGO elements represent glass.

Examples:

- Windows
- Cockpits
- Observation ports

Response:

The first unresolved Impact breaks the glass.

Remove the transparent LEGO element.

The opening remains.

---

# MAT-004 — Infantry

Standing minifigure

↓

First unresolved Impact

↓

Seated minifigure (Wounded)

---

Seated minifigure

↓

Second unresolved Impact

↓

Minifigure removed or laid down (Dead)

No wound counters are required.

The model itself represents its condition.

---

# MAT-005 — Doors

Doors are interactive components.

An unresolved Impact may:

- Jam the door.
- Destroy the door.
- Leave it open.

The exact effect may be chosen by the scenario or future rules.

Destroyed doors should be physically removed whenever possible.

---

# MAT-006 — Windows

Destroyed windows permanently remain open.

Visibility immediately changes.

Future attacks use the new opening.

---

# MAT-007 — Wheels

Vehicles with wheels may lose individual wheels.

Future vehicle rules determine movement penalties.

The damaged wheel should be marked or removed if practical.

---

# MAT-008 — Tracks

Tracked vehicles may suffer track damage.

Future vehicle rules determine movement penalties.

---

# MAT-009 — Weapon Systems

Weapon systems are independent components.

An unresolved Impact may disable a weapon.

Disabled weapons may no longer fire.

The weapon should be physically marked or removed whenever practical.

---

# MAT-010 — Engines

Vehicles may contain a visible engine compartment.

Engine damage is resolved using Vehicle Rules.

A damaged engine may reduce movement or immobilize the vehicle.

---

# MAT-011 — Armour

Armour does not prevent attacks.

Armour determines how Impacts are resolved.

Future armour rules may provide:

- Defence Dice
- Impact cancellation
- Component protection

Armour belongs to the target.

Never to the weapon.

---

# MAT-012 — Stone

Stone represents structural protection.

Examples:

- Fortress walls
- Bunkers
- Towers

Stone usually ignores small-arms Impacts.

Heavy weapons may affect stone structures in future versions.

---

# MAT-013 — Metal

Metal represents structural vehicle components.

Examples:

- Hull
- Turrets
- Bulkheads

Metal normally requires heavier weapons or repeated Impacts.

Future rules will define specific behaviour.

---

# MAT-014 — Wood

Wood is easier to damage than stone or metal.

Examples:

- Crates
- Wooden doors
- Barricades

Wood may break after one or more unresolved Impacts.

---

# MAT-015 — Organic Materials

Examples:

- Trees
- Bushes
- Alien vegetation

Organic materials may:

- Block movement.
- Provide cover.
- Be destroyed.

Future rules will define environmental effects.

---

# MAT-016 — Cover

Cover is determined physically.

The more of a target is hidden,

the greater its protection.

No abstract cover templates exist.

Future rules will assign Defence Dice according to visible exposure.

---

# MAT-017 — Physical Damage

Whenever possible,

damage is represented physically.

Examples:

Remove a window.

Detach a weapon.

Open a broken door.

Remove a wheel.

Lay a casualty down.

Physical representation always has priority.

---

# MAT-018 — Target Components

Players may only target components they can physically see.

Examples:

Visible wheel

Visible turret

Visible door

Visible gun

Visible window

Visible soldier

Hidden components cannot be selected.

---

# MAT-019 — Independent Resolution

Each component resolves its own Impacts.

Example:

Vehicle receives:

6 Impacts.

Attacker assigns:

2 → Window

1 → Wheel

2 → Turret

1 → Door

Each component resolves only the Impacts assigned to it.

This creates tactical precision without additional complexity.

---

# MAT-020 — Future Materials

Future supplements may introduce:

- Concrete
- Ceramic armour
- Force fields
- Energy shields
- Ice
- Lava
- Water
- Toxic terrain

Each new material should define only its own response to Impacts.

No changes to weapon rules are required.

---

# Material Flow

```
Weapon

↓

Impact

↓

Component

↓

Material

↓

Physical Consequence
```

---

# Summary

Materials define what happens after an Impact.

Weapons never define damage.

Targets define consequences.

Every component behaves according to its own material.

The battlefield itself records the result.

---

> **Every Brick Matters.**