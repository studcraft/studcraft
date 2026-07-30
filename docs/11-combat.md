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

Every attack follows the same procedure, and costs **1 Action Point** per weapon system attacking (`02-core-rules.md`, CORE-006) — the same cost regardless of how many Attack Dice that weapon system rolls.

1. Declare the weapon system.
2. Declare the target.
3. Verify Line of Sight.
4. Verify Weapon Range.
5. Roll Attack Dice.
6. Count successful Impacts.
7. Defender resolves Impacts.
8. Update the LEGO model.

For melee attacks, steps 3–4 (Line of Sight, Weapon Range) are replaced by a single Physical Contact check (`12-melee.md` MEL-001, MEL-014); every other step applies identically.

---

# CBT-002 — Line of Sight

Combat uses the universal Physical Visibility rule (`02-core-rules.md`, CORE-008, CORE-009): a target must be physically visible from the attacker's point of view. If any legal target area is visible, the attack is allowed.

---

# CBT-003 — Weapon Range

A target must be inside the weapon's maximum range: `Range = Weapon Length × 2` — see `10-weapons.md` (WPN-005) for the full definition.

---

# CBT-004 — Attack Dice

Every functional muzzle generates **1 Attack Die (D6)** — see `10-weapons.md` (WPN-006) for the full definition. Each die is resolved per CBT-005.

Example

Weapon: 4 Functional Muzzles → Attack Roll: 4D6

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

Each weapon system, as defined in `10-weapons.md` (WPN-008), attacks independently — resolving its own Attack Sequence (CBT-001). See CBT-007 for target-selection rules across multiple weapon systems.

---

# CBT-007 — Multiple Targets

Unless restricted by a scenario,

independent weapon systems may attack different targets.

Individual attack dice from the same weapon system cannot be split between multiple targets, unless the weapon mount can physically rotate to re-aim independently of the platform carrying it (e.g. a turntable, ball joint, or swivel mount). See `16-damage-system.md` (DMG-018, Weapon Distribution) for the full rule. Fixed mounts follow the no-split rule above with no exception.

---

# CBT-008 — Defender Resolution

After counting successful Impacts, responsibility passes to the Component Damage System (`16-damage-system.md`), which determines how each Impact affects the targeted component (see the Combat Flow diagram below for the full step sequence).

---

# CBT-009 — Physical State Changes

Combat results are always represented physically. This is the same rule as `16-damage-system.md` (DMG-006) — a destroyed component is physically removed; see DMG-006, Universal Destruction, for the canonical statement and examples.

---

# CBT-010 — Simultaneous Resolution

This rule governs resolution order, not entitlement to attack: it does not by itself grant any unit a second attack or a free counter-attack. StudCraft's default activation (`03-game-flow.md`, FLOW-002) is strictly one unit at a time — two attacks only resolve together when something else already declares them so (e.g. a future scenario rule for mutual engagement).

When two attacks are declared to resolve together, both are fully resolved before removing models, and being eliminated during resolution does not cancel an attack already declared.

Example

Two infantry models with mutually declared attacks against each other.

Both may become casualties.

---

# CBT-011 — No Damage Values

Combat never assigns damage values. Weapons generate offensive capability — Range, Attack Dice, and Impact Strength, fully defined by `10-weapons.md`'s own Summary — while the target determines every consequence (`16-damage-system.md`).

Impact Strength (`10-weapons.md` WPN-021) is a geometrically-derived property — determined by muzzle or striking-end size, not a hidden statistic — and is consumed by `16-damage-system.md`'s Geometry Check (DMG-014). This updates the original version of this rule, which predated Impact Strength and Muzzle Size (WPN-021) and stated that weapons possess no "Strength" at all.

---

# CBT-012 — Cover

Cover never changes weapon performance.

Cover affects only how the target resolves incoming impacts — the exact rules are defined in `02-core-rules.md` (CORE-010).

---

# CBT-013 — Armour

Armour is not a separate statistic — it is the colloquial name for a component's construction-derived Resistance (`16-damage-system.md`, DMG-003, DMG-004). Armour is never a weapon property; it belongs to the defending model, expressed entirely through how the component is built.

Armour determines how impacts are resolved via the Geometry Check and Damage Roll (DMG-014, DMG-015) — the same mechanism every component uses, with no separate Armour mechanic layered on top.

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
Delivery Method (Line of Sight + Range, or Physical Contact — `12-melee.md` MEL-001/MEL-014)
    │
    ▼
Generate Attack Dice
    │
    ▼
Attack Roll
    │
    ▼
Successful Impacts
    │
    ▼
Component Damage System (Select Target Component → Geometry Check → Damage Roll → Component State Change → Penetration — `16-damage-system.md` DMG-012 through DMG-017)
    │
    ▼
Physical Model Changes
```

Combat determines whether an Impact exists (Delivery Method, Attack Dice, Attack Roll, Successful Impacts); the Component Damage System determines what it does. Ranged and melee attacks differ only in Delivery Method — everything from Generate Attack Dice onward is identical for both.

---

# Summary

Weapons never determine damage.

Weapons only determine:

- How an attack is delivered (ranged or melee).
- How many Attack Dice it generates.
- The Strength of each Impact.

The target determines everything else.

This keeps StudCraft modular and entirely construction-driven.

---

> **Every Brick Matters.**