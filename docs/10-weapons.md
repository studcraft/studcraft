# StudCraft Weapon System

**Version:** 0.2.0 Draft

---

# Purpose

This document defines how weapons are built, measured and used during a game of StudCraft.

Weapons do not use predefined statistics. Their capabilities emerge from their physical construction.

The weapon model is its profile.

---

# Design Philosophy

StudCraft weapons follow one principle:

> If two players can look at the same weapon, they should reach the same conclusion about how it behaves.

Weapon performance emerges from:

- Physical size
- Construction
- Mounting position
- Visible components

No hidden weapon profiles exist.

---

# WPN-001 — Functional Weapon

A weapon is any LEGO construction capable of making an attack.

Every ranged weapon must include:

- A weapon body carrying the muzzle or striking end.
- At least one functional muzzle (WPN-002).
- A physical mounting point.

Melee weapons replace the muzzle with a functional striking end, as defined in `12-melee.md` (MEL-013).

Weapons that do not satisfy these conditions are decorative.

---

# WPN-002 — Functional Muzzle

A functional muzzle is a round construction area on the Weapon Front. Common sizes include:

- 1×1
- 2×2
- 3×3
- 4×4

This list is illustrative, not a limit. A muzzle may be any size that physically fits its Weapon Front Footprint (WPN-019).

Square or rectangular pieces do not represent functional muzzles. The muzzle must be visibly round, whether made from a single piece or several pieces.

Each functional muzzle represents one firing barrel.

Muzzle size determines Impact Strength (WPN-021).

Melee weapons use a functional striking end in place of a muzzle, as defined in `12-melee.md` (MEL-013).

---

# WPN-003 — Weapon Dimensions

Weapon Length is the longest dimension of the functional Weapon Body, measured along its firing axis. Weapon Width is the side of the Weapon Body's front face, which is built square.

Mounting hardware and decorative elements are ignored.

---

# WPN-004 — Weapon Capacity

The sum of the Weapon Length of every weapon mounted on a platform may not exceed the platform's longest horizontal dimension.

**Σ(Weapon Length) ≤ Platform Length**

Platform Length is the largest horizontal dimension of the Unit Base or vehicle carrying the weapons.

Examples:

**Infantry — 1 UB, 4 × 3 studs**

Valid:

- One weapon, length 4.
- Two weapons, length 2 each.
- One weapon length 3 plus one weapon length 1.

Invalid:

- Two weapons, length 4 each.

**Jeep — 2 × 3 UB, 8 × 9 studs**

Valid:

- One weapon, length 9.
- Two weapons, length 4 each.
- Three weapons, length 3 each.
- One weapon length 5 plus two weapons length 2.

Invalid:

- Two weapons, length 9 each.
- Three weapons, length 4 each.

---

# WPN-005 — Weapon Range

Weapon Range equals **Weapon Length × 6**.

| Weapon Length | Maximum Range |
|---|---:|
| 2 studs | 12 studs |
| 4 studs | 24 studs |
| 6 studs | 36 studs |
| 8 studs | 48 studs |
| 12 studs | 72 studs |

Line of Sight remains a physical check (`02-core-rules.md`, CORE-008), so maximum range is only relevant where that distance is unobstructed.

---

# WPN-006 — Rate of Fire

Each functional muzzle grants **1 Attack Die (D6)**.

Muzzle size affects Impact Strength (WPN-021), not the number of dice.

Each die is resolved as an Attack Roll (`11-combat.md`, CBT-005):

- 4–6: the shot generates one Impact.
- 1–3: the die produces nothing.

| Functional Muzzles | Attack Dice |
|---:|---:|
| 1 | 1 |
| 2 | 2 |
| 3 | 3 |
| 4 | 4 |
| 6 | 6 |

A Wounded weapon still grants one die per muzzle; the dice are resolved differently as defined in `11-combat.md` (CBT-015).

---

# WPN-007 — Muzzle Adjacency

Functional muzzles may be placed directly adjacent to one another.

No minimum separation is required.

Muzzles may not overlap (WPN-020).

---

# WPN-008 — Weapon Systems

Each independently mounted weapon is a separate weapon system.

For example, a tank with a main cannon, coaxial machine gun and roof machine gun has three weapon systems.

Targeting rules are defined in `11-combat.md` (CBT-006, CBT-007).

---

# WPN-009 — Weapon Mounts

Weapons must be physically attached to the model.

Valid mounts include:

- Hands
- Turrets
- Hull mounts
- Pintle mounts
- Side mounts

Floating weapons are not permitted.

---

# WPN-010 — Infantry Weapons

Infantry weapons must be carried by the minifigure in its two hands (`17-infantry.md`, INF-001).

One-handed weapons occupy one hand.

Two-handed weapons occupy both.

The model determines what the unit can use.

---

# WPN-011 — Vehicle Weapons

Vehicle weapons must be permanently mounted.

Examples include:

- Hull cannons
- Turret cannons
- Side weapons
- Roof weapons

Weapon position determines its firing arc.

---

# WPN-012 — Line of Fire

A weapon's Line of Fire follows the universal Line of Sight rule (`11-combat.md`, CBT-002).

It is determined from the attacker's point of view (`02-core-rules.md`, CORE-008), not from the muzzle itself.

Buildings, terrain and vehicles block Line of Sight. Transparent elements do not.

---

# WPN-014 — Multiple Weapons

A unit carrying multiple weapons may use them according to its available Action Points.

---

# WPN-015 — Decorative Weapons

Decorative barrels, antennas, hoses and mechanical details have no gameplay effect.

Only functional weapons and their functional muzzles count.

---

# WPN-016 — Weapon Damage

Weapons do not have a damage value.

Each successful Attack Die generates an Impact whose Strength is determined by the muzzle or striking end that produced it (WPN-021).

The effect of the Impact depends on the target's Resistance and the Geometry Check (`16-damage-system.md`, DMG-003, DMG-013), followed by the Damage Roll (DMG-014).

Cover only determines whether the target can be selected (`02-core-rules.md`, CORE-010).

---

# WPN-018 — Weapon Proportion

Weapon Length must be at least twice its Weapon Width.

**Length ≥ 2 × Width**

Valid examples:

- 1×2
- 1×4
- 2×4
- 2×6
- 3×6
- 4×8

Invalid examples:

- 2×2
- 4×4
- 6×6

---

# WPN-019 — Weapon Front Footprint

Every weapon has exactly one Weapon Front: the only face from which it may fire.

The Weapon Front is a square construction area whose dimensions equal the Weapon Width.

Muzzles may only be placed within this footprint.

---

# WPN-020 — Muzzle Placement

Every muzzle occupies a square footprint slot inside the Weapon Front Footprint (WPN-019).

Rules:

- Muzzles must be round (WPN-002).
- Muzzles may not overlap.
- Every muzzle must fit entirely inside the Weapon Front Footprint.
- Unused footprint space is allowed.
- Muzzles may be adjacent to one another (WPN-007).

The designer may arrange the muzzles in any valid configuration.

Example:

A Weapon Body 8 × 4 has a Weapon Width of 4 and therefore a 4 × 4 Weapon Front Footprint.

Possible configurations include:

**Twin Barrel**

- 2 muzzles
- 2 Attack Dice
- Impact Strength 3 each

**Quad Barrel**

- 4 muzzles
- 4 Attack Dice
- Impact Strength 3 each

**Heavy Cannon**

- 1 muzzle
- 1 Attack Die
- Impact Strength 6

**Hybrid**

- 1 muzzle of size 2
- 2 muzzles of size 1
- 3 Attack Dice
- Impact Strengths 6, 3 and 3

No weapon profile is required. The physical configuration determines the result.

---

# WPN-021 — Impact Strength

Impact Strength equals the muzzle size multiplied by 3.

For melee weapons, use the size of the functional striking end (`12-melee.md`, MEL-013).

| Muzzle Size | Impact Strength |
|---|---:|
| 1×1 | 3 |
| 2×2 | 6 |
| 3×3 | 9 |
| 4×4 | 12 |
| N×N | 3N |

A muzzle N studs wide produces an Impact Strength of 3N.

A weapon with multiple muzzles of different sizes produces Attack Dice with different Impact Strengths. Each die uses the size of the muzzle that generated it.

There is no fixed maximum Impact Strength. Larger muzzles require larger Weapon Front Footprints, Weapon Bodies and platforms.

---

# Weapon Archetypes

StudCraft defines no weapon classes. These are construction examples only:

- One small muzzle → Rifle
- Several small muzzles → Machine Gun
- One large muzzle → Cannon
- Many small muzzles → Rocket Launcher
- Several medium muzzles → Naval Battery

All follow the same construction rules.

---

# Summary

Weapons are defined by three physical properties:

## Length

Determines Range (WPN-005) and Weapon Capacity (WPN-004).

## Muzzle Count

Determines the number of Attack Dice (WPN-006).

## Muzzle Size

Determines Impact Strength (WPN-021).

Weapons define only how an Impact is generated. Combat and the Component Damage System determine its consequences (`11-combat.md`, `16-damage-system.md`).

No hidden statistics are required.

A player should understand every weapon simply by looking at the LEGO model.

---

> **Every Brick Matters.**