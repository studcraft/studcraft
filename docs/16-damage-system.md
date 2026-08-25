# StudCraft Damage System

**Version:** 0.2.0 Draft

---

# Purpose

This document defines how structural damage is resolved in StudCraft.

StudCraft does not use:

* Hit Points
* Armour Values
* Saving Throws
* Damage Tables
* Hidden Unit Profiles

Instead, every battlefield object is a collection of physical LEGO components.

The model defines what a component can withstand. Dice determine whether an otherwise possible effect actually occurs.

> **The Model Is The Rules.**

---

# Design Philosophy

StudCraft separates combat into two responsibilities.

**Combat generates Impacts.**

Weapons determine how attacks are delivered, how many Attack Dice they generate, and whether those dice produce Impacts. These rules are defined in `11-combat.md`.

**The Damage System resolves Impacts.**

Once an Impact exists, the target's physical construction determines whether it can affect a component. Dice then determine whether that physically possible effect actually damages it.

This creates two independent questions:

**Geometry:** Can the Impact affect the component?

**Dice:** Does the effect actually damage it?

Components do not have health values. They change state when an Impact successfully damages them.

---

# Component Damage

## DMG-001 — Component Targeting

Combat never resolves damage against an entire unit.

Every Impact is assigned to one visible component.

Examples include:

* Minifig
* Shield
* Door
* Window
* Cannon
* Turret
* Wheel
* Armour Plate
* Pilot
* Cockpit

A vehicle is therefore a collection of independent components.

This keeps damage construction-driven: the physical component receiving the Impact determines the relevant Resistance and state.

---

## DMG-002 — Component States

Every component uses the same three-state progression:

**Operational → Wounded → Dead**

**Operational** — the component functions normally.

**Wounded** — the component has suffered structural damage but remains functional.

A Wounded component suffers only the degradation associated with the capability it provides:

* Wounded infantry moves less effectively (`17-infantry.md`, INF-012).
* A vehicle with a Wounded Pilot moves less effectively (`08-vehicles.md`, VEH-031).
* A Wounded weapon resolves each Attack Die using the Wounded attack rule (`11-combat.md`, CBT-015).

These are the only Wounded-state degradations defined by the core rules.

All other properties remain unchanged, including:

* Resistance
* Impact Strength
* The Damage Roll rolled against it
* Footprint
* Unit Base occupancy
* Transport capacity
* Action Point costs

A second successful damaging Impact changes the component from Wounded to Dead.

**Dead** — the component is immediately removed from the model.

An infantry model represents its state physically:

* Operational: upright
* Wounded: seated
* Dead: removed

No damage token is required.

The three-state model replaces abstract health values with visible physical states.

---

## DMG-003 — Geometry Defines Resistance

Resistance is never assigned as a statistic.

It is measured directly from the LEGO construction.

Resistance is the **smallest section of material an Impact must cross in its direction of travel**, measured in plate layers.

The conversion is:

* 1 plate = 1 Resistance
* 1 brick = 3 Resistance
* Other LEGO elements are measured by their physical thickness in the direction of travel.

Only material actually crossed by the Impact contributes.

Empty internal space contributes nothing.

If an enclosed structure contains multiple walls, each wall is a separate component with its own Resistance. Their thicknesses are not combined.

The outer component protects components behind it (`DMG-006`).

Impact Strength (`10-weapons.md`, WPN-021) uses the same unit.

Resistance therefore emerges from construction rather than from a hidden defensive statistic.

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

These examples illustrate the construction-based principle: changing the physical model changes the rule outcome.

---

## DMG-005 — Universal Destruction

When a component reaches Dead, it is removed from the model.

Examples:

* Destroy a wheel → remove the wheel.
* Destroy a cannon → remove the cannon.
* Destroy a shield → remove the shield.
* Destroy a door → remove the door.
* Destroy a minifig → remove the minifig.

There are no special destruction rules.

The same physical state change applies to every component.

---

## DMG-006 — Internal Components

Components may protect other components.

Example:

**Armour → Pilot**

The Pilot cannot be affected while the Armour blocks the Impact.

If the Armour is penetrated, the Impact may continue toward the Pilot according to DMG-016.

This creates layered protection through physical construction rather than requiring separate armour mechanics.

---

## DMG-007 — No Material-Specific Mechanics

All components use the same damage rules regardless of what they represent.

Glass, metal, wood, infantry and LEGO assemblies are all resolved using:

* Resistance
* Geometry Check
* Damage Roll
* Component State

Material does not provide special modifiers.

A component's behavior depends only on its physical construction and the capability it provides.

This keeps the system universal and prevents hidden material statistics.

---

# Damage Resolution

## DMG-008 — Impact Resolution

The Damage System begins when a successful Impact has been generated by Combat.

Each Impact is resolved independently through:

**Select Target Component → Geometry Check → Damage Roll → State Change → Penetration → Model Change**

Combat determines whether an Impact exists. The Damage System determines what that Impact does.

The same damage procedure therefore applies regardless of whether the Impact came from a ranged weapon or a melee attack.

---

## DMG-011 — Select Target Component

Every successful Impact is assigned to one visible component.

Hidden components cannot be selected directly.

Examples:

* Shield
* Wheel
* Cannon
* Door
* Minifig
* Armour Plate

Impacts are never assigned to an entire vehicle.

Target selection is component-based so that damage always interacts with the physical LEGO structure rather than with an abstract unit health value.

---

## DMG-012 — Composite Vehicle Targeting

Each component of a vehicle behaves independently.

When an attack generates multiple Impacts, each Impact may be assigned to a different visible component of the same target unit.

Example:

A Jeep contains:

* Chassis
* Driver
* Cannon
* Four Wheels
* Windows
* Doors

Six incoming Impacts could be assigned as:

* 2 → Window
* 1 → Wheel
* 2 → Turret
* 1 → Door

Each component resolves its assigned Impacts independently.

Destroying one component does not automatically damage another.

This allows complex models to behave as collections of physical components without requiring vehicle-specific damage tables.

---

## DMG-013 — Geometry Check

Compare the Impact Strength with the target component's Resistance.

| Relationship          | Result                                                       |
| --------------------- | ------------------------------------------------------------ |
| Strength < Resistance | The Impact ends immediately. No Damage Roll is made.         |
| Strength ≥ Resistance | The Impact can affect the component and proceeds to DMG-014. |

If the Impact cannot physically overcome the component's Resistance, no further damage resolution occurs.

Geometry therefore determines whether an effect is physically possible before probability is introduced.

---

## DMG-014 — Damage Roll

For every Impact that passes the Geometry Check, the defender rolls one D6.

| D6 Result | Result                                           |
| --------- | ------------------------------------------------ |
| 1–3       | Damage — advance the component's state one step. |
| 4–6       | No Damage — the component remains unchanged.     |

A successful Damage Roll changes the component:

**Operational → Wounded**

or:

**Wounded → Dead**

The Damage Roll represents uncertainty after the Impact has already proved physically capable of affecting the component.

It does not represent armour.

The distinction is fundamental:

**Geometry determines possibility. Dice determine outcome.**

---

## DMG-015 — Multiple Impacts

Each Impact is resolved independently.

Impacts never combine their Strength.

Each successful Impact creates another opportunity to change the target component's state.

Example:

A two-muzzle shotgun generates two successful Impacts against an Operational minifig.

If both Damage Rolls result in **1–3**:

**Operational → Wounded → Dead**

The minifig is destroyed by two separate Impacts, not by combining their Strength.

This preserves the principle that each weapon muzzle produces an independent effect.

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

Penetration therefore follows the physical path of the Impact and does not depend on whether the previous component was actually damaged.

---

## DMG-018 — Recovery

A damaged component is not repaired. What is broken stays broken.

A Wounded minifigure is the one thing that recovers: it may spend **1 Action Point** to return to Operational — infantry on foot, and a Pilot or crew member inside a vehicle alike.

**Wounded → Operational**

A Dead component cannot return. It has already been removed from the model (`DMG-002`).

---

# Combat Examples

## Example 1 — Pistol vs Minifig

Minifig:

**Resistance = 3**

Pistol:

**Strength = 3**

Attack Roll: 4–6 → **1 Impact**

Geometry:

**3 ≥ 3**

Damage Roll: 1–3 → **Damage**

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

Both Attack Rolls: 4–6 → **2 Impacts**

Both Geometry Checks succeed.

Both Damage Rolls: 1–3 → **Damage**

Result:

**Operational → Wounded → Dead**

One shotgun attack can therefore destroy the minifig because it generated two independent Impacts.

---

## Example 3 — Heavy Cannon vs Shield

Shield:

**Resistance = 3**

Heavy Cannon:

**Strength = 6**

Attack Roll: 4–6 → **1 Impact**

Geometry:

**6 ≥ 3**

Damage Roll: 1–3 → **Damage**

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

Attack Roll: 4–6 → **1 Impact**

Geometry:

**3 ≥ 2**

Damage Roll: 1–3 → **Damage**

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

Attack Roll: 4–6 → **1 Impact**

Geometry:

**3 < 6**

The Impact ends immediately.

No Damage Roll occurs.

A larger muzzle is required to affect the wall.

A 2×2 muzzle produces:

**Strength = 6**

and therefore passes the Geometry Check.

---

# Summary

The Damage System defines:

* Components
* Resistance
* Component States
* Wounded behavior
* Destruction
* Internal Protection
* Geometry Checks
* Damage Rolls
* Penetration
* Multiple Impacts
* Recovery

Weapon attack generation and Attack Rolls are defined by `11-combat.md`.

The Damage System does not use:

* Hit Points
* Armour Values
* Damage Statistics
* Lookup Tables
* Hidden Unit Profiles
* Material-specific modifiers

Every damage interaction emerges from two sources:

1. The physical LEGO construction.
2. The uncertainty introduced by the dice.

> **The Model Is The Rules.**
