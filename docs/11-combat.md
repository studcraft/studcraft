# StudCraft Combat Resolution

**Version:** 0.2.0 Draft

---

# Purpose

This document defines how attacks are resolved in StudCraft.

Combat separates **Impact generation** from **Impact resolution**:

* The attacker generates Impacts.
* The defender determines their consequences.

Weapons do not assign Damage Values. The targeted component determines what happens when an Impact is resolved.

---

# Design Philosophy

StudCraft keeps combat modular by separating two responsibilities:

**Weapons determine offensive capability.**

They determine how an attack is delivered, how many Attack Dice it generates, and the Impact Strength of those Impacts.

**Targets determine consequences.**

The Component Damage System determines how each Impact interacts with the targeted component.

This allows the same weapon rules to interact with infantry, vehicles, buildings and terrain without separate damage systems.

---

# CBT-001 — Attack Sequence

Every attack costs **1 Action Point per weapon system attacking** (`02-core-rules.md`, CORE-006), regardless of how many Attack Dice that weapon system generates.

Ranged attacks follow:

1. Declare the weapon system.
2. Declare the target.
3. Verify Line of Sight.
4. Verify Weapon Range.
5. Generate Attack Dice.
6. Resolve the Attack Roll.
7. Count successful Impacts.
8. Defender resolves the Impacts.
9. Apply physical model changes.

For melee attacks, Line of Sight and Weapon Range are replaced by **Physical Contact** (`12-melee.md`, MEL-001, MEL-014). All later steps are identical.

---

# CBT-002 — Line of Sight

Ranged attacks use the universal Physical Visibility rule (`02-core-rules.md`, CORE-008, CORE-009).

A target may be selected if any legal target area is physically visible from the attacker's point of view.

---

# CBT-003 — Weapon Range

A ranged target must be within the weapon's maximum range:

`Range = Weapon Length × 6`

See `10-weapons.md`, WPN-005.

Melee attacks do not use Weapon Range.

---

# CBT-004 — Attack Dice

Each weapon system generates Attack Dice according to its weapon rules.

For ranged weapons, each **Functional Muzzle** generates **1 Attack Die (D6)** (`10-weapons.md`, WPN-006).

For melee attacks, each independently wielded melee weapon generates **1 Attack Die** (`12-melee.md`, MEL-003).

Example:

```text
4 Functional Muzzles → 4 Attack Dice
```

---

# CBT-005 — Attack Roll

Each Attack Die is rolled independently.

The result determines whether that die generates an Impact:

| D6 Result | Result    |
| --------- | --------- |
| 4–6       | 1 Impact  |
| 1–3       | No Impact |

Example:

```text
Roll:    2  4  5  6
Result:     3 Impacts
```

Each Attack Die can generate a maximum of **1 Impact**.

---

# CBT-006 — Independent Weapon Systems

Each weapon system (`10-weapons.md`, WPN-008) attacks independently and resolves its own Attack Sequence.

Each weapon system therefore costs **1 Action Point** when it attacks, regardless of the number of Attack Dice it generates.

---

# CBT-007 — Multiple Targets

Unless restricted by a scenario, independent weapon systems may attack different targets.

A single weapon system normally assigns all of its Attack Dice to one target.

Its dice may be split between multiple targets only when its mount can physically rotate to re-aim independently of the platform carrying it, such as a turntable, ball joint, swivel mount or a minifigure's shoulder — the rotation point is the shoulder, not the hand.

Each target must be one the mount reaches by rotating alone, without turning the platform. A minifigure's arm therefore covers the targets in front of it and no others.

Fixed mounts cannot split their Attack Dice between targets.

When Attack Dice are split:

* All targets must be declared before any die is rolled.
* The mount must reach each target by rotating alone.
* Line of Sight is checked separately for each target.
* Weapon Range is checked separately for each target.
* A die assigned to a target that fails any of these checks has no valid target and is not rolled.
* The attack still costs the single Action Point for that weapon system.

---

# CBT-008 — Defender Resolution

After successful Impacts are counted, the Component Damage System resolves them.

That system determines:

1. Which component is targeted.
2. Whether the Impact penetrates its geometry.
3. Whether the component changes state.
4. Whether the Impact continues to another component.

See `16-damage-system.md`, DMG-011 through DMG-016.

Combat generates the Impacts; the Damage System determines their consequences.

---

# CBT-009 — Physical State Changes

Combat results are represented physically on the LEGO model.

When a component is destroyed, it is physically removed according to the Universal Destruction rule (`16-damage-system.md`, DMG-005).

---

# CBT-011 — No Damage Values

Combat does not assign Damage Values.

Weapons provide offensive properties such as:

* Attack Dice.
* Impact Strength.
* Ranged delivery through Range and Line of Sight.
* Melee delivery through Physical Contact.

Impact Strength (`10-weapons.md`, WPN-021) is derived from the physical size of the muzzle or striking end. It is used by the Damage System's Geometry Check (`16-damage-system.md`, DMG-013).

The target's construction determines Resistance and all resulting consequences.

---

# CBT-012 — Cover

Cover does not modify weapon performance or Impact resolution.

It only determines whether a component can be selected as a target (`02-core-rules.md`, CORE-010; `16-damage-system.md`, DMG-011).

A hidden component is untargetable.

---

# CBT-013 — Armour

Armour is not a separate statistic.

It is the colloquial description of a component's construction-derived **Resistance** (`16-damage-system.md`, DMG-003, DMG-004).

Resistance belongs to the defending component, not the weapon.

All components use the same Damage System. There is no separate Armour mechanic.

---

# CBT-014 — Future Combat Extensions

The following are **not currently part of StudCraft**:

* Suppression
* Blast Weapons
* Fire
* Smoke
* Explosions
* Overwatch
* Reaction Fire

Future combat rules must preserve the Impact-based combat system.

---

# CBT-015 — Attacking While Wounded

A Wounded weapon (`16-damage-system.md`, DMG-002) still attacks, but each Attack Die is less reliable.

For every Attack Die it generates:

1. Roll **2D6**.
2. Keep the lower result.
3. Resolve that result using CBT-005.

Therefore:

| Kept Result | Result    |
| ----------- | --------- |
| 4–6         | 1 Impact  |
| 1–3         | No Impact |

The two dice count as **one Attack Die**. The second die can never generate an additional Impact.

The number of Attack Dice does not change:

* Each Functional Muzzle still generates one ranged Attack Die.
* Each independently wielded melee weapon still generates one melee Attack Die.

The rule applies to the component making the attack:

* A Wounded soldier with an Operational weapon attacks normally.
* An Operational soldier with a Wounded weapon uses this rule.
* An unarmed attack (`12-melee.md`, MEL-008) uses the attacker's own state.

Wounded states do not stack. If both the attacker and its weapon are Wounded, apply this rule only once to each Attack Die.

Everything else remains unchanged, including:

* Range.
* Impact Strength.
* Action Point cost.
* Target allocation.

---

# Combat Flow

```text
Weapon System
     │
     ▼
Delivery Method
(Ranged: Line of Sight + Range
 Melee: Physical Contact)
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
Component Damage System
(Target Component
 → Geometry Check
 → Damage Roll
 → Component State Change
 → Penetration)
     │
     ▼
Physical Model Changes
```

Ranged and melee attacks differ only in their **Delivery Method**.

From **Generate Attack Dice** onward, both use the same combat resolution.

---

# Summary

Combat separates **Impact generation** from **Impact resolution**.

The attacker determines:

* How the attack is delivered.
* How many Attack Dice are generated.
* The Impact Strength of each Impact.

The Attack Roll determines whether each Attack Die produces an Impact:

* **4–6:** Impact.
* **1–3:** No Impact.

The defender determines what each Impact does through the Component Damage System.

A Wounded weapon, or a Wounded minifigure making an unarmed attack, generates the same number of Attack Dice but resolves each die using two D6 and keeps the lower result.

This keeps combat modular, construction-driven and consistent across infantry, vehicles, buildings and terrain.

---

> **Every Brick Matters.**
