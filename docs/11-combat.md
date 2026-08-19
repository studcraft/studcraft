# StudCraft Combat Resolution

**Version:** 0.2.0 Draft

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

A target must be inside the weapon's maximum range: `Range = Weapon Length × 6` — see `10-weapons.md` (WPN-005) for the full definition, and for why that figure has no written maximum.

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

A Wounded weapon reads each of these dice differently — see CBT-015.

---

# CBT-006 — Independent Weapon Systems

Each weapon system, as defined in `10-weapons.md` (WPN-008), attacks independently — resolving its own Attack Sequence (CBT-001). See CBT-007 for target-selection rules across multiple weapon systems.

---

# CBT-007 — Multiple Targets

Unless restricted by a scenario,

independent weapon systems may attack different targets.

Individual attack dice from the same weapon system cannot be split between multiple targets, unless the weapon mount can physically rotate to re-aim independently of the platform carrying it (e.g. a turntable, ball joint, or swivel mount). See `16-damage-system.md` (DMG-018, Weapon Distribution) for the full rule. Fixed mounts follow the no-split rule above with no exception.

When a weapon system's dice are split across multiple targets, all targets are declared before any die is rolled, and Line of Sight (CBT-002) and Weapon Range (CBT-003) are each verified individually against every declared target — a die assigned to a target that fails either check simply has no target and is not rolled. The whole attack still costs the single, per-weapon-system Action Point defined in CBT-001, regardless of how many targets its dice are split across.

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

Hypothetical example (no current rule produces this — illustrates the mechanism for whatever future rule might)

Two infantry models with mutually declared attacks against each other.

Both may become casualties.

---

# CBT-011 — No Damage Values

Combat never assigns damage values. Weapons generate offensive capability — Range, Attack Dice, and Impact Strength, fully defined by `10-weapons.md`'s own Summary — while the target determines every consequence (`16-damage-system.md`).

Impact Strength (`10-weapons.md` WPN-021) is a geometrically-derived property — determined by muzzle or striking-end size, not a hidden statistic — and is consumed by `16-damage-system.md`'s Geometry Check (DMG-014). This updates the original version of this rule, which predated Impact Strength and Muzzle Size (WPN-021) and stated that weapons possess no "Strength" at all.

---

# CBT-012 — Cover

Cover never changes weapon performance, and never changes how an Impact resolves once an attack is declared. It only gates whether a component can be selected as a target in the first place (`02-core-rules.md`, CORE-010; `16-damage-system.md`, DMG-012) — hidden means untargetable, nothing more.

---

# CBT-013 — Armour

Armour is not a separate statistic — it is the colloquial name for a component's construction-derived Resistance (`16-damage-system.md`, DMG-003, DMG-004). Armour is never a weapon property; it belongs to the defending model, expressed entirely through how the component is built.

Armour determines how impacts are resolved via the Geometry Check and Damage Roll (DMG-014, DMG-015) — the same mechanism every component uses, with no separate Armour mechanic layered on top.

---

# CBT-014 — Future Combat Extensions

None of the following exists in StudCraft today, and no rule grants it.

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

# CBT-015 — Attacking While Wounded

A Wounded weapon (`16-damage-system.md`, DMG-005) still fires, less reliably.

For **each** Attack Die it generates (CBT-004; `10-weapons.md`, WPN-006; `12-melee.md`, MEL-003), roll **two dice instead of one, and read only the lower of the two**. That pair resolves as a single die against CBT-005's unchanged threshold: a 4, 5 or 6 generates one Impact, anything lower generates none. A hit therefore needs both dice at 4 or better — one chance in four, where an Operational weapon has one in two.

**The second die is never an Impact.** The number of Attack Dice is still the number of functional muzzles (`10-weapons.md`, WPN-006) or independently wielded melee weapons (`12-melee.md`, MEL-003), and each muzzle still generates exactly one impact (`16-damage-system.md`, DMG-010). A Wounded weapon rolls more dice and produces no more Impacts than it did before. `16-damage-system.md` (DMG-011) states the same thing from the damage side.

This rule reads the state of the component that provides the attack. Usually that is the weapon, which is a component in its own right (`16-damage-system.md`, DMG-001; `02-core-rules.md`, CORE-014): a Wounded soldier carrying an Operational rifle attacks exactly as if unhurt, and an unhurt soldier carrying a Wounded rifle rolls the pair of dice above.

An unarmed attack (`12-melee.md`, MEL-008) is the one case where the attacker *is* the weapon system, so there the rule reads the attacker: a Wounded minifigure punches with the pair of dice above.

Degradations never stack. A Wounded minifigure firing a Wounded rifle rolls one pair per Attack Die, not two — this rule reads one component per attack, and for that attack the component is the rifle.

Everything else the weapon has is unchanged: its Range (CBT-003), the Impact Strength of every die it rolls (`10-weapons.md`, WPN-021), the 1 Action Point the attack costs (CBT-001), and whether its dice may be split across targets (CBT-007).

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

A Wounded weapon — or a Wounded minifigure attacking unarmed — generates the same number of Attack Dice and reads each of them worse (CBT-015).

This keeps StudCraft modular and entirely construction-driven.

---

> **Every Brick Matters.**