# StudCraft Damage System

**Version:** 0.1.0 Draft

---

# Purpose

This document defines the structural model used to resolve damage in StudCraft, and the dice-based sequence that resolves an Impact against it.

Its purpose is identical to the Weapon System:

> **Every rule must be inferred by observing the LEGO model itself.**

Players should never need hidden statistics or external reference tables to determine how resistant a construction is.

This specification intentionally eliminates traditional concepts such as:

- Hit Points
- Armor Values
- Saving Throws
- Damage Tables
- Hidden Unit Profiles

Instead, every object on the battlefield is represented as a collection of physical LEGO components whose behavior is completely determined by their construction.

Rule identifiers in this document use the prefix `DMG-`, per `system/documentation-standards.md`.

---

# Design Philosophy

StudCraft separates combat into two completely different concepts.

Weapons do **not** deal damage. Weapons generate **impacts**.

Components do **not** have health. Components simply change state when an impact successfully affects them.

Combat itself is further divided into two independent responsibilities: Geometry determines what is physically possible. Dice determine what actually happens.

Everything required to resolve combat must already exist in the physical model.

---

# Component Damage

This section defines the structural model: components, geometry-derived Resistance, and the universal state machine every component uses.

---

# DMG-001 — Component Targeting

Combat never targets an entire unit. Instead, every impact is assigned to one visible component.

Examples include:

- Minifig
- Shield
- Door
- Window
- Cannon
- Turret
- Wheel
- Armor Plate
- Pilot
- Cockpit

A vehicle is not a single object. It is a collection of independent components.

---

# DMG-002 — Components Have No Hit Points

Components only possess structural integrity, represented through a universal state machine (full definition in DMG-005):

```
OK → TOUCHED → DESTROYED
```

Every component in the game follows exactly the same three states. There are no exceptions: a wheel, a shield, a cannon and a minifig all use the same state progression.

---

# DMG-003 — Geometry Defines Resistance

Resistance is never assigned as a statistic. It is read directly from the model.

The resistance of a component is the **smallest structural section that an impact must cross in its direction of travel**.

In practice, this usually corresponds to the smallest dimension of the component measured in LEGO bricks.

The important concept is not the external volume. It is the amount of structure the projectile must physically penetrate.

---

# DMG-004 — Reading Component Resistance

Resistance belongs to the construction itself. Changing the way a component is built naturally changes its resistance.

## Example 1 — Minifig

Approximate dimensions: `4 × 4 × 1`. A frontal impact crosses `1 brick`. Therefore `Resistance = 1`.

## Example 2 — Mounted Cannon

Component dimensions: `4 × 2 × 2`. The projectile enters through the front. The smallest structural section crossed is `2 bricks`. Therefore `Resistance = 2`.

## Example 3 — Shield built with Bricks

Dimensions: `4 × 3 × 1`. Constructed using standard bricks. The projectile crosses `1 brick`. Therefore `Resistance = 1`.

## Example 4 — Shield built with Plates

A shield constructed from four stacked plates. Viewed from the front, the projectile must cross `4 plate layers`. Therefore `Resistance = 4`.

Although both shields occupy similar external dimensions, their internal construction produces different resistance values. StudCraft rewards engineering, not appearance.

---

# DMG-005 — Component State Progression

Every component progresses through exactly three states.

```
OK → TOUCHED → DESTROYED
```

**OK** — the component functions normally.

**TOUCHED** — the component has suffered structural damage. It continues to function normally. A second successful damaging impact will destroy it.

**DESTROYED** — the component immediately ceases to exist. It is physically removed from the model. No destroyed component remains on the battlefield. This is the same physical-representation principle as `02-core-rules.md` (CORE-016) and `13-materials.md` (MAT-017) — see DMG-006.

---

# DMG-006 — Universal Destruction

Destroyed always means exactly the same thing: the component is removed.

Examples: destroy a wheel → remove the wheel. Destroy a cannon → remove the cannon. Destroy a shield → remove the shield. Destroy a door → remove the door. Destroy a minifig → remove the minifig.

There are no special destruction rules. This is the canonical statement of "prefer physical representation" for damage — `11-combat.md` (CBT-009) and `13-materials.md` (MAT-017) both point here instead of restating it.

---

# DMG-007 — Internal Components

Components may protect other components.

Example:

```
Armor → Pilot
```

The Pilot cannot be affected while the Armor blocks the incoming impact. Only after penetrating or destroying the Armor may the impact continue toward the Pilot (mechanically resolved by DMG-017, Penetration).

This naturally creates layered protection without requiring additional rules.

---

# DMG-008 — Relationship to Materials

`13-materials.md` (MAT-001 through MAT-020) already defines a component/material system. This document does not discard it — it completes it:

- **Material** (MAT-001) still determines a component's substance and its physical/cosmetic response on reaching DESTROYED — MAT-003 (glass removal), MAT-005/MAT-006 (doors and windows), MAT-007/MAT-008 (wheels and tracks), MAT-009 (weapon systems), MAT-010 (pilot), MAT-012–MAT-015 (stone, metal, wood, organic) all continue to describe *what happens physically* when a component is destroyed, and are unaffected by this document.
- **This document replaces the fixed, material-specific hit-count assumptions** in MAT-003 and MAT-004 with the universal, geometry-derived mechanism: Resistance (DMG-003/004), the Geometry Check (DMG-014), the Damage Roll (DMG-015), and the Component State machine (DMG-005). A typical minifig (Resistance 1, per DMG-004 Example 1) still takes two failed Damage Rolls to go from OK to DESTROYED — the same two-impact result MAT-004 already described — but now derived from construction instead of asserted as a fixed rule for that material.
- **MAT-011 (Armour)** said future rules may provide "Defence Dice, Impact cancellation, Component protection." This document fulfills that: the Geometry Check is the impact-cancellation mechanism (an impact below Resistance ends immediately, DMG-014), and the Damage Roll (DMG-015) is the Defence Dice mechanism.
- **MAT-016 (Cover)** is explicitly **not** addressed by this document. Cover remains deferred to a future proposal, unchanged.
- **MAT-019 (Independent Resolution)** — splitting a single target's incoming impacts across its own components (e.g. 2 → Window, 1 → Wheel) — is unaffected and remains the mechanism for DMG-012 (Select Target Component).

---

# Damage Resolution

This section defines the dice-based sequence that resolves an Impact against a component, once Part 1's structural rules have established the components and their resistance.

Combat in StudCraft is divided into two independent responsibilities:

- **Geometry** determines what is physically possible.
- **Dice** determine what actually happens.

The LEGO model defines capability. The dice introduce uncertainty.

---

# DMG-009 — Combat Resolution Overview

Every combat action follows the same sequence.

```
Weapon → Generate Impacts → Attack Roll → Select Component →
Geometry Check → Damage Roll → Component State Change →
Remaining Strength continues if applicable
```

Every impact is resolved independently.

---

# DMG-010 — Generate Impacts

Each weapon muzzle generates exactly one impact. The weapon specification already defines (per `10-weapons.md`):

- Number of impacts (Attack Dice, WPN-006 — one per muzzle)
- Impact Strength (WPN-021 — determined by muzzle size)

Example — Shotgun (`○ ○`, two muzzles) generates Impact A and Impact B.

---

# DMG-011 — Attack Roll

The attacker rolls one die for every generated impact. A result of 4, 5, or 6 succeeds and creates one valid impact (per `11-combat.md` CBT-005's existing threshold). A result of 1, 2, or 3 fails; the impact simply disappears.

Example — two-barrel shotgun: one die succeeds, one fails. Only one impact continues.

---

# DMG-012 — Select Target Component

Every successful impact is assigned to a visible component (per `13-materials.md` MAT-018/MAT-019).

Examples: Shield, Wheel, Cannon, Door, Minifig, Armor Plate.

Impacts are never assigned to an entire vehicle — only to components.

---

# DMG-013 — Composite Vehicle Targeting

Every component of a composite vehicle behaves independently (per DMG-001).

Example — Jeep: Chassis, Driver, Cannon, Front Left Wheel, Front Right Wheel, Rear Left Wheel, Rear Right Wheel.

A player may intentionally target the cannon, the driver, or one wheel. Each resolves independently: destroying the cannon does not damage the vehicle; destroying a wheel does not damage the driver.

---

# DMG-014 — Geometry Check

The impact strength is compared against the resistance of the target component.

If `Strength < Resistance`: the impact immediately ends. No dice are rolled by the defender. The impact simply lacks enough energy to affect the component.

If `Strength ≥ Resistance`: the impact is capable of damaging the component. Combat continues to DMG-015.

---

# DMG-015 — Damage Roll

The defender rolls one D6 for that impact. A result of 4, 5, or 6 succeeds: nothing happens, the component remains unchanged. A result of 1, 2, or 3 fails: the component advances exactly one state (`OK → TOUCHED` or `TOUCHED → DESTROYED`).

This die does not represent armor — the Geometry Check already proved the impact could cause damage. It represents the uncertainty of combat: a fortunate deflection, an imperfect impact, a glancing hit, mechanical failure, luck.

---

# DMG-016 — Multiple Impacts

Each impact is completely independent. Impacts never combine their strength. Instead, each successful impact creates another opportunity to change the target's state.

Example — a shotgun (`○ ○`) against a minifig at OK: both attack rolls succeed, both geometry checks succeed, the defender performs two Damage Rolls. If both fail, the minifig goes `OK → TOUCHED → DESTROYED`. The minifig dies from a single shotgun blast — not because the shotgun dealt more damage, but because it generated multiple impacts.

---

# DMG-017 — Penetration

An impact may continue through multiple components. Whenever an impact successfully affects a component, its remaining strength is calculated:

```
Remaining Strength = Current Strength − Component Resistance
```

If remaining strength is greater than zero, the impact continues in the same direction, toward the next component (per DMG-007, Internal Components).

## Example

Heavy Cannon (`Strength 4`) vs. Shield (`Resistance 3`): after affecting the shield, `Remaining Strength = 1`. The impact continues. A minifig behind the shield (`Resistance 1`) is still a valid target — the impact is capable of damaging it. The minifig now performs its own Damage Roll. Each component always resolves independently.

---

# DMG-018 — Weapon Distribution

Each muzzle creates one independent impact.

By default, all impacts from the same weapon system are assigned to the same target (per `11-combat.md` CBT-007). This document adds one exception: impacts may be assigned to **different target units** only if the weapon mount can physically rotate to re-aim independently of the platform carrying it.

Examples of free rotation (exception applies): minifig torso, turntable, ball joint, swivel mount.

Examples that require Action Points instead (CBT-007 applies, no split): fixed mount, entire vehicle movement, repositioning the weapon carrier.

This is independent of DMG-012 (splitting a single target's incoming impacts across *its own* components, per MAT-019) — that always applies regardless of mount type.

Weapon articulation is read directly from the LEGO model.

---

# DMG-019 — Repairs

Repairing consumes Action Points. Each repair restores exactly one state (`TOUCHED → OK`).

Destroyed components cannot be repaired — they have already been removed from the model. Future construction rules will define rebuilding.

---

# Combat Examples

## Example 1 — Pistol vs Minifig

Minifig `Resistance 1`. Pistol `Strength 1`. Attack Roll: Success. Geometry: `1 ≥ 1`. Damage Roll: Failure. Result: `OK → TOUCHED`. Second successful impact: `TOUCHED → DESTROYED`.

## Example 2 — Shotgun vs Minifig

Shotgun (2 muzzles). Attack Rolls: Success, Success. Both geometry checks succeed. Damage Rolls: Failure, Failure. Result: `OK → TOUCHED → DESTROYED`. One shotgun blast eliminates the Minifig.

## Example 3 — Heavy Cannon vs Shield

Shield `Resistance 3`. Heavy Cannon `Strength 4`. Attack succeeds. Geometry succeeds. Damage Roll: Failure. Shield becomes `TOUCHED`. Remaining Strength `1` continues toward the protected Minifig, which now resolves the impact independently (DMG-017).

## Example 4 — Jeep Cannon

Mounted Cannon (`4 × 2 × 2`, `Resistance 2`). Enemy Cannon `Strength 2`. Attack succeeds. Geometry succeeds. Damage Roll fails. Mounted Cannon becomes `TOUCHED`. A second successful impact destroys it. The Jeep remains operational but without its weapon.

---

# Combat Philosophy

StudCraft intentionally separates engineering from probability.

The LEGO model answers: **Can this happen?**

The dice answer: **Did it happen?**

Geometry determines capability. Dice determine uncertainty. Neither replaces the other.

---

# Summary

This document establishes the structural foundations of the damage system and the sequence that resolves it.

It defines: Components, Resistance, Structural States, Destruction, Internal Protection, and how this system relates to Materials (DMG-008); and the combat resolution sequence — Generate Impacts, Attack Roll, Select Target Component, Composite Vehicle Targeting, Geometry Check, Damage Roll, Multiple Impacts, Penetration, Weapon Distribution, and Repairs.

The system never requires: Hit Points, Armor Values, Damage Statistics, Lookup Tables, Hidden Unit Profiles.

Every combat interaction emerges from two sources only: the physical LEGO construction, and the uncertainty introduced by the dice.

---

> **The Model Is The Rules.**
