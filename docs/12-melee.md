# StudCraft Melee Combat

**Version:** 0.2.0 Draft

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
Generate Attack Dice
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

A melee attack may target any visible, physically reachable component, exactly like a ranged attack (`16-damage-system.md`, DMG-011).

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

Each independently wielded weapon is its own weapon system (`10-weapons.md`, WPN-008) and costs its own **1 Action Point** to attack with (`11-combat.md`, CBT-001) — wielding two weapons and attacking with both is two attacks, not one attack producing two dice.

If the weapon is Wounded, that die is rolled as `11-combat.md` (CBT-015) directs.

Examples:

```
Knife                 → 1 weapon system → 1 Attack Die  → 1 AP
Sword                 → 1 weapon system → 1 Attack Die  → 1 AP
Sword + Dagger        → 2 weapon systems → 2 Attack Dice → 2 AP (attacking with both)
Two Swords            → 2 weapon systems → 2 Attack Dice → 2 AP (attacking with both)
Double-ended staff    → 1 weapon system → 1 Attack Die  → 1 AP — the attacker declares which end strikes
```

---

# MEL-005 — Standard Combat Resolution

Once a melee weapon generates its Attack Die (MEL-003), Combat Resolution (`11-combat.md`) and the Component Damage System determine every remaining step, exactly as for a ranged Impact.

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

If no dedicated melee weapon exists, a unit may attack using its bare hands — its own weapon system for AP-cost purposes (`11-combat.md`, CBT-001: 1 AP).

An unarmed attack generates **1 Attack Die**, counting as a size-1 striking end (`10-weapons.md`, WPN-021) for Impact Strength purposes, representing punches, kicks, or physical force.

Because the attacker is the weapon system here, it is the attacker's own Component State that is read: a Wounded minifigure rolls that die as `11-combat.md` (CBT-015) directs.

---

# MEL-009 — Shields

Shields are defensive components. They never generate Attack Dice. Their interaction with combat is completely defined by the Component Damage System (`16-damage-system.md`); no melee-specific shield rules exist.

---

# MEL-011 — Physical Representation

Combat results should be represented on the LEGO model whenever possible, per the universal physical-representation principle (`02-core-rules.md`, CORE-016; `16-damage-system.md`, DMG-002, DMG-005).

Examples:

- Wounded minifigure sits.
- Dead minifigure is removed.
- Destroyed components (weapons, shields, doors) are removed.

No additional markers are required.

---

# MEL-012 — Interaction with Combat Rules

Unless explicitly stated otherwise, melee combat follows all rules defined in:

- 11-combat.md
- 10-weapons.md
- 16-damage-system.md

This document defines only how a melee attack generates an Impact — physical contact (MEL-001), reach (MEL-014), striking ends (MEL-013), and Attack Dice (MEL-003). All subsequent resolution belongs to Combat Resolution and the Component Damage System.

---

# MEL-013 — Functional Striking End

A functional striking end is the physical contact surface through which a melee weapon delivers an Impact. It replaces the concept of a firing muzzle for melee weapons (`10-weapons.md`, WPN-001, WPN-002).

A functional striking end is built as an N×N footprint slot — the same sizing as a muzzle (WPN-002), including no fixed maximum: it scales with the weapon's construction. Unlike a muzzle, a striking end is **not** required to be built from round pieces: bladed, pointed, and other melee-appropriate shapes are all valid.

A striking end's size determines the Impact Strength it generates, exactly like a muzzle (`10-weapons.md`, WPN-021) — both represent the physical contact surface through which a weapon transfers energy into the target; a muzzle and a functional striking end are the same concept, expressed through two different delivery methods.

---

# MEL-014 — Weapon Reach

"Reach" is not a value consulted separately from the Physical Contact check (MEL-001) — it is a description of *why* that check comes out the way it does. A weapon's Weapon Length (`10-weapons.md`, WPN-003) is what physically lets it touch a target at a given distance; building a longer weapon is how a player makes their model reach farther. There is no reach number to look up, and none is needed — the model already decides the outcome the moment MEL-001's contact check is made.

---

# Summary

Melee combat is a special case of the standard combat system, not an independent one. Ranged and melee differ only in how an Impact is generated:

- Physical contact, not Line of Sight and Range, gates the attack (MEL-001, MEL-014).
- Each independently wielded weapon generates exactly one Attack Die, regardless of striking-end count (MEL-003); a striking end's size still determines Impact Strength (MEL-013, WPN-021).
- A Wounded weapon still generates that die and reads it worse — as does a Wounded minifigure attacking unarmed, the one attack whose weapon system is the attacker (MEL-008; `11-combat.md`, CBT-015).

Every Impact — ranged or melee — then resolves through the exact same sequence: Attack Roll (`11-combat.md`, CBT-005), then Select Target Component, Geometry Check, Damage Roll, Component State Change and Penetration (`16-damage-system.md`, DMG-008). No separate damage system exists.

---

> **Every Brick Matters.**