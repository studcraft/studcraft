# StudCraft Damage System

**Version:** 0.2.0 Draft

---

# Purpose

This document defines how structural damage is resolved in StudCraft.

StudCraft does not use:

- Hit Points
- Armour Values
- Saving Throws
- Damage Tables
- Hidden Unit Profiles

Instead, every battlefield object is a collection of physical LEGO components.

The model defines what a component can withstand. Dice determine whether an otherwise possible effect actually occurs.

> **The Model Is The Rules.**

---

# Design Philosophy

StudCraft separates damage into two questions:

**Geometry:** Can the Impact affect the component?

**Dice:** Does the effect actually damage it?

Weapons generate Impacts. Components do not have health values. Components simply change state when an Impact successfully damages them.

---

# Component Damage

## DMG-001 — Component Targeting

Combat never targets an entire unit.

Every Impact is assigned to one visible component.

Examples include:

- Minifig
- Shield
- Door
- Window
- Cannon
- Turret
- Wheel
- Armour Plate
- Pilot
- Cockpit

A vehicle is therefore a collection of independent components.

---

## DMG-002 — Component States

Every component uses the same three-state progression:

Operational → Wounded → Dead

**Operational** — the component functions normally.

**Wounded** — the component has suffered structural damage but remains functional.

A Wounded component suffers only the degradation associated with the capability it provides:

- Wounded infantry moves less effectively (`17-infantry.md`, INF-012).
- A vehicle with a Wounded Pilot moves less effectively (`08-vehicles.md`, VEH-031).
- A Wounded weapon resolves each Attack Die using the Wounded attack rule (`11-combat.md`, CBT-015).

These are the only Wounded-state degradations defined by the core rules.

All other properties remain unchanged, including:

- Resistance
- Impact Strength
- Footprint
- Unit Base occupancy
- Transport capacity
- Action Point costs

A second successful damaging Impact changes the component from Wounded to Dead.

**Dead** — the component is immediately removed from the model.

An infantry model represents its state physically:

- Operational: upright
- Wounded: seated
- Dead: removed

No damage token is required.

---

## DMG-003 — Geometry Defines Resistance

Resistance is never assigned as a statistic.

It is measured directly from the LEGO construction.

Resistance is the **smallest structural section that an Impact must cross in its direction of travel**, measured in plate layers.

The conversion is:

- 1 plate = 1 Resistance
- 1 brick = 3 Resistance
- Other LEGO elements are measured by their physical thickness in the direction of travel.

Only material actually crossed by the Impact contributes.

Empty internal space contributes nothing.

If an enclosed structure contains multiple walls, each wall is a separate component with its own Resistance. Their thicknesses are not combined.

The outer component protects components behind it (`DMG-007`).

Impact Strength (`10-weapons.md`, WPN-021) uses the same unit.

---

## DMG-004 — Reading Resistance

Changing the physical construction of a component changes its Resistance.

Examples:

### Minifig

A typical minifig torso is approximately one brick thick.

**Resistance = 3**

### Cannon Housing

A cannon housing with a 2-plate-thick front wall:

**Resistance = 2**

### Brick Shield

A shield one brick thick:

**Resistance = 3**

### Plate Shield

A shield made from four stacked plates:

**Resistance = 4**

### Bunker Wall

A wall two bricks thick:

**Resistance = 6**

### Moulded Component

A moulded component is measured in exactly the same way as a built component.

A windscreen 1 plate thick has:

**Resistance = 1**

A thicker moulded component simply has a higher Resistance.

---

## DMG-005 — Universal Destruction

When a component reaches Dead, it is removed from the model.

Examples:

- Destroy a wheel → remove the wheel.
- Destroy a cannon → remove the cannon.
- Destroy a shield → remove the shield.
- Destroy a door → remove the door.
- Destroy a minifig → remove the minifig.

There are no special destruction rules.

---

## DMG-006 — Internal Components

Components may protect other components.

Example:

Armour → Pilot

The Pilot cannot be affected while the Armour blocks the Impact.

If the Armour is penetrated, the Impact may continue toward the Pilot according to DMG-017.

This creates layered protection without requiring additional armour rules.

---

## DMG-007 — No Material-Specific Mechanics

All components use the same damage rules regardless of what they represent.

Glass, metal, wood, infantry and LEGO assemblies are all resolved using:

- Resistance
- Geometry Check
- Damage Roll
- Component State

Material does not provide special modifiers.

A component's behavior depends only on its physical construction and the capability it provides.

---

# Damage Resolution

## DMG-008 — Combat Resolution

Every Impact follows this sequence:

Weapon → Delivery Method → Generate Attack Dice → Attack Roll → Successful Impact → Select Target Component → Geometry Check → Damage Roll → State Change → Penetration → Model Change

Every Impact is resolved independently.

---

## DMG-009 — Generate Impacts

Each functional weapon muzzle generates one Attack Die and therefore one potential Impact (`10-weapons.md`, WPN-006).

The weapon determines:

- Number of Attack Dice
- Impact Strength of each die

For example, a two-muzzle shotgun generates two Attack Dice.

---

## DMG-010 — Attack Roll

Roll one D6 for each Attack Die.

- **4–6:** the die generates one valid Impact.
- **1–3:** the die generates no Impact.

When the component providing the attack is Wounded, use the Wounded attack rule (`11-combat.md`, CBT-015).

The number of Attack Dice does not change.

---

## DMG-011 — Select Target Component

Every successful Impact is assigned to one visible component.

Hidden components cannot be selected directly.

Examples:

- Shield
- Wheel
- Cannon
- Door
- Minifig
- Armour Plate

Impacts are never assigned to an entire vehicle.

---

## DMG-012 — Composite Vehicle Targeting

Each component of a vehicle behaves independently.

When an attack generates multiple Impacts, each Impact may be assigned to a different visible component of the same target.

Example:

A Jeep contains:

- Chassis
- Driver
- Cannon
- Four Wheels
- Windows
- Doors

Six incoming Impacts could be assigned as:

- 2 → Window
- 1 → Wheel
- 2 → Turret
- 1 → Door

Each component resolves its assigned Impacts independently.

Destroying one component does not automatically damage another.

---

## DMG-013 — Geometry Check

Compare the Impact Strength with the target component's Resistance.

If:

**Strength < Resistance**

the Impact ends immediately.

No Damage Roll is made.

If:

**Strength ≥ Resistance**

the Impact can damage the component and proceeds to DMG-014.

---

## DMG-014 — Damage Roll

For every Impact that passes the Geometry Check, the defender rolls one D6.

- **1–3:** the Impact damages the component. The component advances one state.
- **4–6:** the Impact does not damage the component. The component remains unchanged.

Therefore:

**Operational → Wounded**

or:

**Wounded → Dead**

The Damage Roll represents uncertainty after the Impact has already proved physically capable of affecting the component.

It does not represent armour.

---

## DMG-015 — Multiple Impacts

Each Impact is resolved independently.

Impacts never combine their Strength.

Each successful Impact creates another opportunity to change the target component's state.

Example:

A two-muzzle shotgun generates two successful Impacts against an Operational minifig.

If both Damage Rolls fail:

Operational → Wounded → Dead

The minifig is destroyed by two separate Impacts, not by combining their Strength.

---

## DMG-016 — Penetration

An Impact may continue through multiple components.

When an Impact passes the Geometry Check, subtract the Resistance of the component it crossed:

**Remaining Strength = Current Strength − Component Resistance**

If Remaining Strength is greater than zero, the Impact continues in the same direction toward the next component.

Penetration does not depend on the Damage Roll.

The Impact continues whether the current component becomes Wounded or remains unchanged.

### Example

Heavy Cannon:

**Strength = 6**

Shield:

**Resistance = 3**

After passing through the shield:

**Remaining Strength = 6 − 3 = 3**

A minifig behind the shield with Resistance 3 can therefore be affected:

**3 ≥ 3**

The minifig then performs its own Geometry Check and Damage Roll.

---

## DMG-017 — Weapon Distribution

Each muzzle generates one independent Impact.

By default, all Impacts from the same weapon system must be assigned to the same target unit (`11-combat.md`, CBT-007).

They may be divided between different target units only when the weapon mount can physically rotate and re-aim independently.

Examples where splitting is allowed:

- Minifig torso
- Turntable
- Ball joint
- Swivel mount

Examples where splitting is not allowed:

- Fixed hull mount
- Repositioning the vehicle
- Moving the weapon carrier

Infantry-carried weapons qualify because the minifig itself can turn between attacks.

This rule concerns splitting Impacts between **target units**.

DMG-012 separately allows incoming Impacts to be distributed between different components of the same target unit.

Weapon articulation is determined directly from the LEGO model.

---

## DMG-018 — Repairs

A unit may spend **1 Action Point**, once per activation, to repair one of its own Wounded components.

The component returns:

Wounded → Operational

For infantry, this is represented by standing the minifigure back up.

Repairing another unit requires:

- A visible repair tool or equipment
- Physical adjacency to the target

Dead components cannot be repaired because they have already been removed from the model.

---

# Combat Examples

## Example 1 — Pistol vs Minifig

Minifig:

**Resistance = 3**

Pistol:

**Strength = 3**

Attack Roll: 4-6.

Geometry:

**3 ≥ 3**

Damage Roll: 1–3.

Result:

**Operational → Wounded**

A second successful damaging Impact changes the minifig to Dead.

---

## Example 2 — Shotgun vs Minifig

Shotgun:

**2 muzzles**

Each muzzle:

**Strength = 3**

Minifig:

**Resistance = 3**

Both Attack Rolls: 4-6.

Both Geometry Checks succeed.

Both Damage Rolls: 1–3..

Result:

**Operational → Wounded → Dead**

One shotgun attack can therefore destroy the minifig because it generated two independent Impacts.

---

## Example 3 — Heavy Cannon vs Shield

Shield:

**Resistance = 3**

Heavy Cannon:

**Strength = 6**

Attack Roll: 4-6.

Geometry:

**6 ≥ 3**

Damage Roll: 1–3.

Shield becomes Wounded.

Remaining Strength:

**6 − 3 = 3**

The Impact continues toward the protected minifig.

---

## Example 4 — Jeep Cannon

Mounted Cannon:

**Resistance = 2**

Enemy Cannon:

**Strength = 3**

Attack Roll: 4-6.

Geometry:

**3 ≥ 2**

Damage Roll: 1–3.

The cannon becomes Wounded.

A second successful damaging Impact destroys it.

Remaining Strength:

**3 − 2 = 1**

The Impact continues toward the Jeep hull.

Hull:

**Resistance = 3**

Since:

**1 < 3**

the Impact stops.

---

## Example 5 — Rifle vs Bunker Wall

Bunker wall:

**Resistance = 6**

Rifle:

**Strength = 3**

Attack Roll: 4-6.

Geometry:

**3 < 6**

The Impact ends immediately.

No Damage Roll occurs.

A larger muzzle is required to affect the wall.

A 2×2 muzzle produces:

**Strength = 6**

and therefore passes the Geometry Check.

---

# Combat Philosophy

StudCraft separates engineering from probability.

The LEGO model answers:

**Can this happen?**

The dice answer:

**Did it happen?**

Geometry determines physical capability.

Dice determine uncertainty.

Neither replaces the other.

---

# Summary

The Damage System defines:

- Components
- Resistance
- Component States
- Wounded behavior
- Destruction
- Internal Protection
- Geometry Checks
- Damage Rolls
- Penetration
- Multiple Impacts
- Weapon Distribution
- Repairs

The system does not use:

- Hit Points
- Armour Values
- Damage Statistics
- Lookup Tables
- Hidden Unit Profiles
- Material-specific modifiers

Every combat interaction emerges from two sources:

1. The physical LEGO construction.
2. The uncertainty introduced by the dice.

> **The Model Is The Rules.**