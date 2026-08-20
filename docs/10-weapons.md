# StudCraft Weapon System

**Version:** 0.2.0 Draft

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

- A weapon body — the structure carrying the muzzle or striking end: barrel, mechanism, support. Decoration does not count.
- At least one visible functional muzzle (WPN-002).
- A physical mounting point.

Melee weapons replace the functional muzzle with a functional striking end, visible in the same way, as defined in `12-melee.md` (MEL-013).

Weapons that do not satisfy these conditions are decorative.

---

# WPN-002 — Functional Muzzle

A functional muzzle is a round construction area on the Weapon Front — a round plate or round tile. Common sizes:

- 1×1
- 2×2
- 3×3
- 4×4

This list is illustrative, not a ceiling — a muzzle may be any size the Weapon Front Footprint (WPN-019) can physically hold. Larger muzzles (5×5 and beyond) are valid on a large enough Weapon Front, at the cost of a longer Weapon Body (WPN-018) and a bigger platform to carry it (WPN-004).

Round LEGO plates and tiles are not manufactured in every size — 1×1, 2×2, 4×4, 6×6, and 8×8 are common; 3×3, 5×5, and other odd sizes are not standard single pieces. A muzzle at one of these sizes is still valid: build the footprint slot from the closest available round element, or assemble it from more than one round piece, as long as the result reads clearly as a round muzzle occupying that N×N slot.

Square or rectangular pieces (e.g. 1×1 square plate, 1×2, 2×1, 1×3, 2×4) are not valid — only round pieces represent a muzzle. The area a muzzle occupies on the Weapon Front Footprint is still measured as an N×N grid slot (per WPN-019/WPN-020), the same way a round LEGO plate or tile occupies a square footprint of studs even though the visible piece is round.

Each functional muzzle represents one firing barrel. Muzzle size determines Impact Strength (WPN-021).

A functional muzzle is the physical contact surface through which a ranged weapon transfers energy into an Impact. Melee weapons use a functional striking end in its place, which plays exactly the same role — see `12-melee.md` (MEL-013).

---

# WPN-003 — Weapon Length

Weapon Length is the longest dimension of the functional Weapon Body, measured along the weapon's firing axis — the axis running perpendicular to the Weapon Front (WPN-019), which is the face the length axis points through.

Measure the Weapon Body only. Mounting hardware (WPN-009) and decorative elements are not part of it and are ignored.

---

# WPN-004 — Weapon Capacity

The sum of the Weapon Length of every weapon mounted on a platform may never exceed the platform's longest dimension (its Platform Length).

```
Σ(Weapon Length) ≤ Platform Length
```

Platform Length is the largest **horizontal** dimension of the Unit Base or vehicle carrying the weapons. A Unit Base is a volume — see `02-core-rules.md` (CORE-001) — and this reads only its `4 × 3` stud footprint, so infantry's Platform Length stays 4 studs and the Unit Base's height never enters the calculation.

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

**Weapon Length × 6**

Examples

| Weapon Length | Maximum Range |
|---------------|--------------:|
| 2 studs | 12 studs |
| 4 studs | 24 studs |
| 6 studs | 36 studs |
| 8 studs | 48 studs |
| 12 studs | 72 studs |

No additional range values exist.

There is no maximum Range, for the same reason there is no maximum Impact Strength (WPN-021): the limit is what the attacker's platform can carry. That limit is real, it is simply not written as a number. Weapon Length is bounded by Platform Length (WPN-004), platform size by the agreed Deployment Volume (`08-vehicles.md`, VEH-001; `06-deployment.md`, DEP-003), and the Deployment Volume by the battlefield the players agree on before it (`03-game-flow.md`, FLOW-001). Range therefore scales with the size of the game on its own.

Maximum Range is rarely the practical limit in any case. Line of Sight is a physical check (`02-core-rules.md`, CORE-008), so a weapon reaching 72 studs only matters where 72 studs of clear sight exist. On a battlefield with terrain, that is uncommon.

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

A Wounded weapon still grants one die per muzzle; what changes is how each of those dice is read (`11-combat.md`, CBT-015).

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

Infantry weapons must be carried by the minifigure in the two hands `17-infantry.md` (INF-001) gives it: one-handed weapons (knife, sword, pistol) occupy one of them, two-handed weapons (rifle, machine gun, rocket launcher) occupy both.

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

A weapon's Line of Fire follows the universal Line of Sight rule (`11-combat.md`, CBT-002) — determined from the attacker's point of view (`02-core-rules.md`, CORE-008), not the muzzle specifically: buildings, terrain and vehicles block it, and transparent elements do not.

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

Weapons do not possess a damage value. Weapons generate Attack Dice, each carrying an Impact Strength derived from the muzzle or striking end that rolled it (WPN-021) — a geometric property of the weapon, not a hidden statistic.

The final effect of a successful Impact depends entirely on the target: its Resistance/Armour and the Geometry Check (`16-damage-system.md`, DMG-003, DMG-014), and the Damage Roll (DMG-015). Cover only determines whether the target can be selected at all (`02-core-rules.md`, CORE-010) — it has no effect once an attack is declared.

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

Reloading is future work of its own: no weapon in the current construction rules runs out of ammunition, so nothing reloads today.

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

2 Attack Dice, Muzzle Size 1, Impact Strength 3 each.

Quad Barrel

```
●●··
●●··
····
····
```

4 Attack Dice, Muzzle Size 1, Impact Strength 3 each.

Heavy Cannon

```
██··
██··
····
····
```

1 Attack Die, Muzzle Size 2, Impact Strength 6.

Hybrid

```
██··
██··
●●··
····
```

3 Attack Dice. Muzzle Sizes: 2, 1, 1. Impact Strengths: 6, 3, 3.

Every valid partition produces a different weapon. No weapon profile is required.

---

# WPN-021 — Impact Strength

Impact Strength equals the size of the muzzle — or, for melee weapons, the functional striking end (`12-melee.md`, MEL-013) — that generated the attack, multiplied by 3.

One stud of muzzle width represents one brick of penetrating power, and a brick is 3 plate layers (`16-damage-system.md`, DMG-003) — so Impact Strength and Resistance are both counts of plate layers, and the Geometry Check (DMG-014) compares like with like instead of two different units.

| Size | Impact Strength |
|--------|-----------------:|
| 1×1 | 3 |
| 2×2 | 6 |
| 3×3 | 9 |
| 4×4 | 12 |
| N×N | 3N |

As a shortcut: a muzzle N studs wide defeats a component N bricks thick. This stops dividing evenly once a component is built from plates rather than whole bricks (a 4-plate shield is Resistance 4, not a whole number of bricks) — the shortcut aids reasoning, but the table above is the operative value.

There is no maximum size. A large enough Weapon Front Footprint (WPN-019) supports arbitrarily large muzzles or striking ends, with Impact Strength scaling accordingly. Threatening a highly Resistant component (`16-damage-system.md`, DMG-003) requires a correspondingly large Weapon Front, which in turn requires a longer Weapon Body (WPN-018) and a larger platform to carry it (WPN-004) — bigger guns need bigger platforms. No component is unconditionally invulnerable; it is only safe from whatever can't be mounted on the attacker's current platform. An infantry model, carrying the largest muzzle its platform permits (2×2, per WPN-004/WPN-018/WPN-019/WPN-020), generates Impact Strength 6 — enough to affect a component built from one or two standard bricks (Resistance 3 or 6).

A weapon with multiple muzzles or striking ends of different sizes produces Attack Dice with different Impact Strengths — each die's Impact Strength depends only on the muzzle or striking end that rolled it.

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

Weapons define only how an Impact is generated. Every consequence of that Impact is determined by Combat Resolution (`11-combat.md`) and the Component Damage System (`16-damage-system.md`).

No hidden statistics are required.

A player should understand every weapon simply by looking at the LEGO model.

---

> **Every Brick Matters.**
