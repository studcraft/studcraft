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

A functional muzzle is a round construction area on the Weapon Front — a round plate or round tile — sized:

- 1×1
- 2×2
- 3×3
- 4×4

Square or rectangular pieces (e.g. 1×1 square plate, 1×2, 2×1, 1×3, 2×4) are not valid — only round pieces represent a muzzle. The area a muzzle occupies on the Weapon Front Footprint is still measured as an N×N grid slot (per WPN-019/WPN-020), the same way a round LEGO plate or tile occupies a square footprint of studs even though the visible piece is round.

Each functional muzzle represents one firing barrel. Muzzle size determines Impact Strength (WPN-021).

Melee weapons use a functional striking end instead of a muzzle. See `12-melee.md` (MEL-003).

---

# WPN-003 — Weapon Length

Weapon Length is the longest dimension of the functional Weapon Body.

Decorative elements are ignored.

---

# WPN-004 — Weapon Capacity

The sum of the Weapon Length of every weapon mounted on a platform may never exceed the platform's longest dimension (its Platform Length).

```
Σ(Weapon Length) ≤ Platform Length
```

Platform Length is the largest dimension of the Unit Base or vehicle carrying the weapons.

Examples

Infantry (1 UB, 4 × 3 studs — Platform Length 4)

Valid:

- One weapon, length 4.
- Two weapons, length 2 each.
- One weapon length 3 plus one weapon length 1.

Invalid:

- Two weapons, length 4 each.

Jeep (2 × 3 UB, 8 × 9 studs — Platform Length 9)

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

regardless of muzzle size. Muzzle size affects Impact Strength (WPN-021), not the number of dice.

Each die is rolled and resolved as an Attack Roll (`11-combat.md`, CBT-005): a result of 4, 5, or 6 confirms the shot left the muzzle and generates one valid Impact; a result of 1, 2, or 3 means that die produced nothing.

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

# WPN-007 — Muzzle Adjacency

Functional muzzles may be placed directly adjacent to one another, sharing an edge with no gap of weapon body between them.

Example

```
██··
```

Where each `█` cell is a separate functional muzzle occupying adjacent footprint cells.

The only placement restriction is that muzzles may not overlap (WPN-020). No minimum separation between muzzles is required.

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

Targeting rules for independent weapon systems are defined in `11-combat.md` (CBT-006, CBT-007).

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

A weapon's Line of Fire follows the universal Line of Sight rule (`11-combat.md`, CBT-002), applied from the weapon's muzzle: buildings, terrain and vehicles block it, and transparent elements follow the Material Rules.

---

# WPN-013 — Attack Procedure

Resolving a ranged attack follows the universal Attack Sequence defined in `11-combat.md` (CBT-001): declare weapon, declare target, verify Line of Sight, verify Range, roll Attack Dice, count Impacts, defender resolves Impacts, update the model.

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

# WPN-018 — Weapon Proportion

Weapon Length must be at least twice the Weapon Width.

```
Length ≥ 2 × Width
```

Weapon Width is the smallest dimension of the Weapon Body.

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

This prevents unrealistic weapon proportions.

---

# WPN-019 — Weapon Front Footprint

Every weapon has exactly one Weapon Front — the only face from which the weapon may fire.

Muzzles may not be placed on the rear, side, top, or bottom faces of the weapon.

The Weapon Front is represented by a square construction area, the Weapon Front Footprint:

```
Weapon Width × Weapon Width
```

Examples

Weapon Width = 1

```
■
```

Weapon Width = 2

```
■■
■■
```

Weapon Width = 4

```
■■■■
■■■■
■■■■
■■■■
```

The footprint defines the only available space for muzzle construction.

---

# WPN-020 — Muzzle Placement

Every muzzle occupies one square footprint slot inside the Weapon Front Footprint, built as a round piece (WPN-002).

Rules:

- Muzzles must be round (WPN-002).
- Muzzles may not overlap.
- Every muzzle must fit entirely inside the Weapon Front Footprint.
- Unused footprint space is allowed. Muzzles are not required to cover every square.
- Muzzles may be directly adjacent to one another (WPN-007).

The designer may partition the Weapon Front Footprint in any valid way.

Example

Weapon Body: 8 × 4. Weapon Width: 4. Weapon Front Footprint:

```
■■■■
■■■■
■■■■
■■■■
```

Valid configurations:

Twin Barrel

```
●●··
····
····
····
```

2 Attack Dice, Muzzle Size 1.

Quad Barrel

```
●●··
●●··
····
····
```

4 Attack Dice, Muzzle Size 1.

Heavy Cannon

```
██··
██··
····
····
```

1 Attack Die, Muzzle Size 2.

Hybrid

```
██··
██··
●●··
····
```

3 Attack Dice. Muzzle Sizes: 2, 1, 1.

Every valid partition produces a different weapon. No weapon profile is required.

---

# WPN-021 — Impact Strength

Impact Strength equals the size of the muzzle that generated the attack.

| Muzzle | Impact Strength |
|--------|-----------------:|
| 1×1 | 1 |
| 2×2 | 2 |
| 3×3 | 3 |
| 4×4 | 4 |

A weapon with muzzles of different sizes produces Attack Dice with different Impact Strengths — each die's Impact Strength depends only on the muzzle that rolled it.

---

# Weapon Archetypes

StudCraft defines no weapon classes. Weapons emerge naturally from construction. These are illustrative examples only, not additional rules:

- One small muzzle → Rifle
- Several small muzzles → Machine Gun
- One large muzzle → Cannon
- Many small muzzles → Rocket Launcher
- Several medium muzzles → Naval Battery

Every archetype follows exactly the same construction rules (WPN-002 through WPN-021).

---

# Summary

Weapons in StudCraft are defined by three physical properties:

## Length

Determines Range (WPN-005) and Weapon Capacity consumption (WPN-004).

---

## Muzzle Count

Determines the number of Attack Dice (WPN-006).

---

## Muzzle Size

Determines Impact Strength (WPN-021). Muzzles are always round (WPN-002).

---

No hidden statistics are required.

A player should understand every weapon simply by looking at the LEGO model.

---

> **Every Brick Matters.**
