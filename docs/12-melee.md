# StudCraft Melee Combat

**Version:** 0.1.0 Draft

---

# Purpose

This document defines hand-to-hand combat in StudCraft.

Melee combat follows the same Impact-based philosophy as ranged combat.

Weapons do not inflict damage.

Weapons generate Impacts.

The defender resolves those Impacts according to the Material Rules.

---

# Design Philosophy

Melee combat should be:

- Fast
- Simultaneous
- Physical
- Easy to resolve

No additional combat statistics are introduced.

The existing combat system is reused whenever possible.

---

# MEL-001 — Melee Range

A melee attack may only be declared if the attacking weapon is in physical contact with the target.

If the weapon cannot physically reach the target, the attack is not legal.

---

# MEL-002 — Eligible Targets

A melee attack may target:

- Infantry
- Vehicle crew (if exposed)
- Vehicle components
- Doors
- Windows
- Interactive scenery
- Any other valid physical component

The target must be reachable by the attacking weapon.

---

# MEL-003 — Attack Dice

Melee weapons generate Attack Dice exactly as defined in `10-weapons.md`.

Each functional muzzle or striking end generates:

**1 Attack Die (D6)**

For melee weapons, the striking end replaces the concept of a firing muzzle.

Examples:

- Knife → 1 die
- Sword → 1 die
- Double-ended staff → 2 dice (if built with two striking ends)

---

# MEL-004 — Simultaneous Combat

Both combatants resolve their attacks simultaneously.

Procedure:

1. Both players declare their attacks.
2. Both roll Attack Dice.
3. Count successful Impacts.
4. Both defenders resolve Impacts.
5. Apply all physical changes.

Even if one combatant is eliminated, its attack is still resolved.

---

# MEL-005 — Successful Impacts

Each result of:

**4, 5 or 6**

generates one Impact.

Results of:

1, 2 or 3

have no effect.

This follows the standard Combat Rules.

---

# MEL-006 — Multiple Combatants

Several units may engage the same target.

Each attacking unit resolves its own melee attack independently.

Impacts are then assigned and resolved normally.

---

# MEL-007 — Weapons

Only visible melee weapons may be used.

Examples:

- Knife
- Sword
- Axe
- Spear
- Hammer
- Club

Decorative elements have no gameplay effect.

---

# MEL-008 — Improvised Weapons

If no dedicated melee weapon exists, a unit may attack using its bare hands.

An unarmed attack generates:

**1 Attack Die**

This represents punches, kicks or physical force.

---

# MEL-009 — Shields

Shields are defensive equipment.

They do not generate Attack Dice.

Future Equipment Rules will define how shields help resolve incoming Impacts.

---

# MEL-010 — Component Attacks

Melee attacks may target exposed vehicle components.

Examples:

- Door
- Wheel
- Track
- Weapon
- Pilot

The target component resolves Impacts using the Material Rules.

---

# MEL-011 — Physical Representation

Combat results should be represented on the LEGO model whenever possible.

Examples:

- Wounded minifigure sits.
- Dead minifigure lies down.
- Broken door opens or is removed.
- Destroyed weapon is detached.

No additional markers are required.

---

# MEL-012 — Interaction with Combat Rules

Unless explicitly stated otherwise, melee combat follows all rules defined in:

- 11-combat.md
- 10-weapons.md
- 13-materials.md

This document only defines the differences specific to hand-to-hand combat.

---

# Summary

Melee combat follows the same philosophy as ranged combat.

The only differences are:

- Physical contact is required.
- Both sides resolve attacks simultaneously.
- Melee weapons replace ranged weapons.
- The defender always resolves Impacts.

No separate damage system exists.

---

> **Every Brick Matters.**