# StudCraft Combat Resolution

**Version:** 0.1.0 Draft

---

# Purpose

This document defines how attacks are resolved in StudCraft.

Weapons do not inflict damage directly.

Weapons generate **Impacts**.

The target determines the consequences of those impacts.

This separation allows the same weapon to interact naturally with infantry, vehicles, buildings and terrain.

---

# Design Philosophy

StudCraft separates combat into two independent systems.

**The attacker produces impacts.**

**The defender resolves them.**

This keeps weapon rules simple while allowing targets to behave differently.

---

# CBT-001 — Attack Sequence

Every attack follows the same procedure.

1. Declare the weapon system.
2. Declare the target.
3. Verify Line of Sight.
4. Verify Weapon Range.
5. Roll Attack Dice.
6. Count successful Impacts.
7. Defender resolves Impacts.
8. Update the LEGO model.

---

# CBT-002 — Line of Sight

A target must be physically visible.

Visibility is determined from the attacking weapon.

If any legal target area is visible, the attack is allowed.

Fundamental Rule:

> If you can see it, you can shoot it.

---

# CBT-003 — Weapon Range

A target must be inside the weapon's maximum range.

Weapon Range is defined in:

10-weapons.md

Range = Weapon Length × 2

---

# CBT-004 — Attack Dice

Every functional muzzle generates:

**1 Attack Die (D6)**

Example

Weapon:

4 Functional Muzzles

Attack Roll:

4D6

---

# CBT-005 — Successful Impacts

Each die showing:

**4, 5 or 6**

generates one Impact.

Each die showing:

1, 2 or 3

misses.

Example

Roll:

2 4 5 6

Result:

3 Impacts

---

# CBT-006 — Independent Weapon Systems

Each weapon system attacks independently.

Example

Tank

Main Cannon

Roof Machine Gun

Coaxial Machine Gun

Each weapon resolves its own attack sequence.

---

# CBT-007 — Multiple Targets

Unless restricted by a scenario,

independent weapon systems may attack different targets.

Individual attack dice from the same weapon system cannot be split between multiple targets.

---

# CBT-008 — Defender Resolution

After counting Impacts,

the defender becomes responsible for resolving them.

The defender uses the appropriate rules.

Examples

Infantry

13-materials.md

Vehicles

08-vehicles.md

Structures

13-materials.md

---

# CBT-009 — Physical State Changes

Whenever possible,

combat results should modify the LEGO model itself.

Examples

Minifigure sits.

Weapon removed.

Door opened.

Window removed.

Wheel detached.

Physical representation always takes priority over tokens.

---

# CBT-010 — Simultaneous Resolution

If two attacks occur simultaneously,

both attacks are fully resolved before removing models.

Example

Two infantry models fighting in melee.

Both may become casualties.

---

# CBT-011 — No Damage Values

Weapons never possess:

- Damage
- Strength
- Armour Penetration

Weapons only define:

- Range
- Number of Attack Dice
- Firing Position

Everything else belongs to the target.

---

# CBT-012 — Cover

Cover never changes weapon performance.

Cover affects only how the target resolves incoming impacts.

The exact rules are defined in:

13-materials.md

---

# CBT-013 — Armour

Armour is never a weapon property.

Armour belongs to the defending model.

Armour determines how impacts are resolved.

---

# CBT-014 — Future Combat Extensions

Future versions may include:

- Suppression
- Blast Weapons
- Fire
- Smoke
- Explosions
- Overwatch
- Reaction Fire

These additions must preserve the Impact-based combat system.

---

# Combat Flow

```
Weapon
    │
    ▼
Generate Attack Dice
    │
    ▼
Generate Impacts
    │
    ▼
Target Resolves Impacts
    │
    ▼
Physical Model Changes
```

---

# Summary

Weapons never determine damage.

Weapons only determine:

- How far they shoot.
- How many dice they roll.
- Where they can fire.

The target determines everything else.

This keeps StudCraft modular and entirely construction-driven.

---

> **Every Brick Matters.**