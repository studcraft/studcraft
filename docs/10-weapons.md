# StudCraft Weapon System

**Version:** 0.1.0 Draft

---

# Purpose

This document defines how weapons are built, measured and used during a game of StudCraft.

Weapons in StudCraft do not have traditional statistics.

Instead, every weapon derives its capabilities directly from its physical LEGO construction.

The weapon model is its profile.

---

# Design Philosophy

StudCraft weapons follow one simple principle:

> If two players can look at the same weapon, they should reach the same conclusion about how it behaves.

Weapon performance must emerge from:

- Physical size
- Construction
- Mounting position
- Visible components

No hidden weapon profiles exist.

---

# WPN-001 — Functional Weapon

A weapon is any LEGO construction capable of making an attack.

Every ranged weapon must include:

- A weapon body.
- At least one functional muzzle.
- A physical mounting point.

Melee weapons replace the functional muzzle with a functional striking end, as defined in `12-melee.md`.

Weapons that do not satisfy these conditions are decorative.

---

# WPN-002 — Functional Muzzle

A functional muzzle is represented by one of the following LEGO elements:

- Round Plate 1×1
- Round Brick 1×1

Each visible functional muzzle represents one firing barrel.

Melee weapons use a functional striking end instead of a muzzle. See `12-melee.md` (MEL-003).

---

# WPN-003 — Weapon Length

Weapon length is measured from:

Rear of the weapon body

to

The foremost functional muzzle.

Decorative elements are ignored.

---

# WPN-004 — Maximum Weapon Length

A weapon may never be longer than the longest dimension of the platform carrying it.

Examples:

Infantry (1 UB, 4 × 3 studs)

Maximum weapon length:

4 studs.

Bike

Maximum weapon length:

Vehicle length.

Tank

Maximum weapon length:

Vehicle length.

---

# WPN-005 — Weapon Range

Weapon range is determined by construction.

Range equals:

**Weapon Length × 2**

Examples

| Weapon Length | Maximum Range |
|---------------|--------------:|
| 2 studs | 4 studs |
| 4 studs | 8 studs |
| 6 studs | 12 studs |
| 8 studs | 16 studs |
| 12 studs | 24 studs |

No additional range values exist.

---

# WPN-006 — Rate of Fire

Each functional muzzle grants:

**1 Attack Die (D6)**

Examples

| Functional Muzzles | Attack Dice |
|-------------------:|------------:|
| 1 | 1 |
| 2 | 2 |
| 3 | 3 |
| 4 | 4 |
| 6 | 6 |

Rate of fire is entirely determined by construction.

---

# WPN-007 — Muzzle Separation

StudCraft requires each functional muzzle to be separated from the next by at least one stud of weapon body.

Example

```
[M][O][M][O]
```

Where:

- M = Weapon Body
- O = Functional Muzzle

This is a StudCraft construction convention.

It naturally limits the maximum rate of fire.

---

# WPN-008 — Weapon Systems

Each independently mounted weapon is considered its own weapon system.

Examples

A tank with:

- Main Cannon
- Coaxial Machine Gun
- Roof Machine Gun

contains:

Three independent weapon systems.

Each weapon may choose its own target unless restricted by future scenario rules.

---

# WPN-009 — Weapon Mounts

Weapons must be physically attached to the model.

Valid mounts include:

- Hands
- Turrets
- Hull Mounts
- Pintle Mounts
- Side Mounts

Floating weapons are not permitted.

---

# WPN-010 — Infantry Weapons

Infantry weapons must be carried by the minifigure.

Equipment follows the physical model.

Examples:

One-handed:

- Knife
- Sword
- Pistol
- Shield

Two-handed:

- Rifle
- Machine Gun
- Rocket Launcher

The model determines what the unit can use.

---

# WPN-011 — Vehicle Weapons

Vehicle weapons must be permanently mounted.

Examples:

- Hull Cannon
- Turret Cannon
- Side Weapon
- Roof Weapon

Weapon position determines firing arc.

---

# WPN-012 — Line of Fire

A weapon may only attack targets that are physically visible from its muzzle.

Buildings, terrain and vehicles block line of fire.

Transparent elements follow the Material Rules.

---

# WPN-013 — Attack Procedure

To resolve a ranged attack:

1. Check line of sight.
2. Check weapon range.
3. Count functional muzzles.
4. Roll one D6 per muzzle.
5. Resolve hits using the Combat Rules.

---

# WPN-014 — Multiple Weapons

A unit carrying multiple weapons may use them according to its available Action Points.

Future scenarios may limit the number of weapons fired during a single activation.

---

# WPN-015 — Decorative Weapons

Decorative barrels, antennas, hoses and mechanical details have no gameplay effect.

Only functional muzzles count.

---

# WPN-016 — Weapon Damage

Weapons do not possess intrinsic damage values.

Weapons generate attack dice.

The final effect depends on:

- Target
- Armour
- Materials
- Cover
- Combat Rules

This keeps weapon construction simple while allowing future expansion.

---

# WPN-017 — Future Weapon Types

Future supplements may introduce:

- Flamethrowers
- Explosive Weapons
- Beam Weapons
- Energy Weapons
- Indirect Fire
- Smoke Launchers

These must continue to follow the StudCraft Weapon Construction Standard.

---

# Summary

Weapons in StudCraft are defined by three physical properties:

## Length

Determines maximum range.

---

## Functional Muzzles

Determine the number of attack dice.

---

## Mounting Position

Determines firing arc.

---

No hidden statistics are required.

A player should understand every weapon simply by looking at the LEGO model.

---

> **Every Brick Matters.**