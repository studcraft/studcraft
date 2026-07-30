# StudCraft Melee Combat

**Version:** 0.1.0 Draft

---

# Purpose

This document defines hand-to-hand combat in StudCraft.

Melee combat follows the same Impact-based philosophy as ranged combat.

Weapons do not inflict damage.

Weapons generate Impacts.

The defender resolves those Impacts using the Component Damage System (`16-damage-system.md`).

---

# Design Philosophy

Melee is not a different combat system — it is a different method of delivering an Impact. Once physical contact is established, melee follows exactly the same combat flow as every other attack in the game.

```
Weapon
    │
    ▼
Physical Contact
    │
    ▼
Generate Impact
    │
    ▼
Standard Combat Resolution
```

Ranged and melee combat differ only in how an Impact is generated, never in how it is resolved. No melee-specific damage rules exist.

---

# MEL-001 — Physical Contact

A melee attack may only be declared if the attacking weapon's functional striking end (MEL-013) is in physical contact with the target component.

If the weapon cannot physically reach the target, the attack is not legal. No measuring tools are required — physical contact is checked directly on the model.

---

# MEL-002 — Component Targeting

A melee attack may target any visible, physically reachable component, exactly like a ranged attack (`16-damage-system.md`, DMG-012).

Examples:

- Minifig
- Shield
- Vehicle crew
- Wheel
- Track
- Door
- Window
- Weapon
- Interactive scenery
- Any other valid physical component

The target must be reachable by the attacking weapon's functional striking end (MEL-001, MEL-013).

---

# MEL-003 — One Weapon, One Impact

Every independently wielded melee weapon generates exactly **1 Attack Die (D6)**, regardless of how many functional striking ends (MEL-013) it has built. A weapon never generates additional Attack Dice because it has multiple striking surfaces — only independently wielded weapons count.

If a weapon has more than one functional striking end, the attacker declares which one delivers the Impact for that attack; that striking end's size determines the Impact's Strength (`10-weapons.md`, WPN-021).

Examples:

```
Knife           → 1 Attack Die
Sword           → 1 Attack Die
Sword + Dagger  → 2 Attack Dice (two independently wielded weapons)
Two Swords      → 2 Attack Dice (two independently wielded weapons)
Double-ended staff (one weapon, two striking ends) → 1 Attack Die — the attacker declares which end strikes
```

---

# MEL-004 — Simultaneous Resolution

Melee follows the universal Simultaneous Resolution rule (`11-combat.md`, CBT-010): both combatants declare their attacks, both sets of Impacts are fully resolved before removing models, and a combatant eliminated during resolution still has its own already-declared attack resolved.

---

# MEL-005 — Standard Combat Resolution

Once a melee weapon generates its Attack Die (MEL-003), every step that follows is identical to a ranged Impact (`16-damage-system.md`, DMG-011 through DMG-017): Attack Roll, Select Target Component, Geometry Check, Damage Roll, Component State Change, and Penetration where applicable. No melee-specific resolution rules exist.

---

# MEL-006 — Multiple Combatants

Several units may engage the same target.

Each attacking unit resolves its own melee attack independently.

Impacts are then assigned and resolved normally.

---

# MEL-007 — Weapons

Only visible, physically built melee weapons with a functional striking end (MEL-013) may be used — the same decorative-elements principle as ranged weapons (`10-weapons.md`, WPN-015).

Examples:

- Knife
- Sword
- Axe
- Spear
- Hammer
- Club

Decorative hilts, guards, and non-functional blades have no gameplay effect.

---

# MEL-008 — Unarmed Combat

If no dedicated melee weapon exists, a unit may attack using its bare hands.

An unarmed attack generates **1 Attack Die** with **Impact Strength 1**, representing punches, kicks, or physical force.

---

# MEL-009 — Shields

Shields are defensive components. They never generate Attack Dice. Their interaction with combat is completely defined by the Component Damage System (`16-damage-system.md`); no melee-specific shield rules exist.

---

# MEL-010 — Merged into Component Targeting

Vehicle component targeting adds no rule beyond MEL-002 (Component Targeting) — a vehicle component is targeted exactly like any other component: visible and physically reachable. This ID is retained, rather than deleted, per this repo's rule-ID-stability convention; see MEL-002 for the actual rule.

---

# MEL-011 — Physical Representation

Combat results should be represented on the LEGO model whenever possible, per the universal physical-representation principle (`02-core-rules.md`, CORE-016; `16-damage-system.md`, DMG-006).

Examples:

- Wounded minifigure sits.
- Dead minifigure lies down or is removed.
- Destroyed components (weapons, shields, doors) are removed.

No additional markers are required.

---

# MEL-012 — Interaction with Combat Rules

Unless explicitly stated otherwise, melee combat follows all rules defined in:

- 11-combat.md
- 10-weapons.md
- 16-damage-system.md

This document only defines how melee weapons generate Attack Dice. Everything after that belongs to the standard combat system.

---

# MEL-013 — Functional Striking End

A functional striking end is the physical point of contact through which a melee weapon delivers an Impact. It replaces the concept of a firing muzzle for melee weapons (`10-weapons.md`, WPN-001, WPN-002).

A functional striking end is built as an N×N footprint slot, sized 1×1 through 4×4 — the same size categories as a muzzle. Unlike a muzzle (WPN-002), a striking end is **not** required to be built from round pieces: bladed, pointed, and other melee-appropriate shapes are all valid.

A striking end's size determines the Impact Strength it generates, exactly like a muzzle (`10-weapons.md`, WPN-021) — both represent the physical contact surface through which a weapon transfers energy into the target; a muzzle and a functional striking end are the same concept, expressed through two different delivery methods.

---

# MEL-014 — Weapon Reach

Weapon reach in melee is determined entirely by the physical geometry of the LEGO model — specifically, its Weapon Length (`10-weapons.md`, WPN-003).

No written reach value or additional range statistic is required — reach is checked directly against the model (MEL-001).

---

# Summary

Melee combat is a special case of the standard combat system, not an independent one. Ranged and melee differ only in how an Impact is generated:

- Physical contact, not Line of Sight and Range, gates the attack (MEL-001, MEL-014).
- Each independently wielded weapon generates exactly one Attack Die, regardless of striking-end count (MEL-003); a striking end's size still determines Impact Strength (MEL-013, WPN-021).
- Both combatants resolve simultaneously (MEL-004, CBT-010).

Every Impact — ranged or melee — then resolves through the exact same sequence: Attack Roll, Select Target Component, Geometry Check, Damage Roll, Component State Change, Penetration (MEL-005). No separate damage system exists.

---

> **Every Brick Matters.**