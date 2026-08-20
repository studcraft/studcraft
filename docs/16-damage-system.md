# StudCraft Damage System

**Version:** 0.2.0 Draft

---

# Purpose

This document defines the structural model used to resolve damage in StudCraft, and the dice-based sequence that resolves an Impact against it.

Its purpose is identical to the Weapon System:

> **Every rule must be inferred by observing the LEGO model itself.**

Players should never need hidden statistics or external reference tables to determine how resistant a construction is.

This specification intentionally eliminates traditional concepts such as:

- Hit Points
- Armour Values
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

## DMG-001 — Component Targeting

Combat never targets an entire unit. Instead, every impact is assigned to one visible component.

Examples include:

- Minifig
- Shield
- Door
- Window
- Cannon
- Turret
- Wheel
- Armour Plate
- Pilot
- Cockpit

A vehicle is not a single object. It is a collection of independent components.

---

## DMG-002 — Components Have No Hit Points

Components only possess structural integrity, represented through a universal state machine (full definition in DMG-005):

```
Operational → Wounded → Dead
```

Every component in the game follows exactly the same three states. There are no exceptions: a wheel, a shield, a cannon and a minifig all use the same state progression.

---

## DMG-003 — Geometry Defines Resistance

Resistance is never assigned as a statistic. It is read directly from the model.

Resistance is the **smallest structural section that an impact must cross in its direction of travel**, measured in plate layers (the finest LEGO unit of height). This conversion applies to every component without exception: a plate counts as 1, a brick counts as 3, and any other LEGO element counts as the plate-equivalent of its own thickness in the direction of travel. No component type is exempt, and none is measured differently — a moulded piece (a minifig torso, a wheel, an accessory shield) is read the same way as a built assembly (a wall, a shield, a hull).

Only material the Impact actually crosses contributes. Empty internal space contributes nothing — a component is assumed hollow unless it is physically built solid. Where an Impact would cross more than one wall of an enclosed structure, those walls are separate components (DMG-001), each with its own Resistance, and the outer one protects what lies behind it (DMG-007) — resolved one after another by Penetration (DMG-017). Their thicknesses are never added together into a single Resistance.

Impact Strength (`10-weapons.md`, WPN-021) is expressed in the same unit.

The Geometry Check (DMG-014) therefore compares two counts of plate layers rather than two different units.

The important concept is not the external volume. It is the amount of structure the projectile must physically penetrate.

---

## DMG-004 — Reading Component Resistance

Resistance belongs to the construction itself. Changing the way a component is built naturally changes its resistance.

### Example 1 — Minifig

A minifig torso, measured like any other component: roughly one brick of material in the direction of travel. Therefore `Resistance = 3`.

### Example 2 — Mounted Cannon

A cannon housing built with a 2-plate-thick front wall. The projectile enters through the front. The smallest structural section crossed is `2 plate layers`. Therefore `Resistance = 2`.

### Example 3 — Shield built with Bricks

A shield built from standard bricks (1 brick = 3 plates tall). The projectile crosses `3 plate layers`. Therefore `Resistance = 3`.

### Example 4 — Shield built with Plates

A shield constructed from four stacked plates. Viewed from the front, the projectile must cross `4 plate layers`. Therefore `Resistance = 4`.

A brick-built shield (Resistance 3) and a four-plate shield (Resistance 4) can occupy similar external bulk, yet resolve to different resistance values because the count of physical layers — not the external silhouette — is what matters. StudCraft rewards engineering, not appearance.

### Example 5 — Bunker

A bunker wall built two bricks thick. The projectile crosses `6 plate layers` (2 bricks × 3 plates). Therefore `Resistance = 6`.

### Example 6 — Moulded Windscreen

A windscreen — a single moulded LEGO element, not a built assembly — measured the same way as any other component: `1 plate` thick in the direction of travel. Therefore `Resistance = 1`. No component type is exempt from this measurement — a thin moulded piece resolves low (this example), a thick one resolves high (Example 1, the minifig), by the same conversion.

### Example 7 — Vehicle Hull

A vehicle hull with 1-brick front armour, an empty interior, and 1-brick rear armour. An Impact striking the front crosses `3 plate layers` of structure. Therefore `Resistance = 3`.

The empty interior contributes nothing, and the rear wall is a separate component (DMG-001) — not part of this one's Resistance. If the Impact penetrates the front wall, DMG-017 determines whether it continues toward whatever is inside.

---

## DMG-005 — Component State Progression

Every component progresses through exactly three states.

```
Operational → Wounded → Dead
```

**Operational** — the component functions normally.

**Wounded** — the component has suffered structural damage. It still functions, and where the capability it provides is one of the three the ruleset degrades, it functions worse. Exactly three degradations exist, each owned by the document that owns the capability: a Wounded infantry model's movement (`17-infantry.md`, INF-012), the movement of a vehicle whose Pilot is Wounded (`08-vehicles.md`, VEH-031), and how each Attack Die is read when the component providing the attack is Wounded (`11-combat.md`, CBT-015). That list is closed, so most components — a door, a window, a wheel, a shield, a hull — lose nothing at all by being Wounded, and are simply one Impact from Dead. Nothing else about a Wounded component changes: its Resistance (DMG-003), the Impact Strength of a weapon (`10-weapons.md`, WPN-021), the Damage Roll rolled against it (DMG-015), its Unit Base occupancy, its footprint, its transport capacity and every Action Point cost are all read exactly as they are for an Operational component. A second successful damaging impact will kill it, and a repair (DMG-019) returns it to Operational.

**Dead** — the component immediately ceases to exist. It is physically removed from the model. No dead component remains on the battlefield. This is the same physical-representation principle as `02-core-rules.md` (CORE-016) — see DMG-006.

An infantry model is placed in the pose of its state: upright while Operational, seated once Wounded. The pose is the marker; no token is used.

---

## DMG-006 — Universal Destruction

Destroyed always means exactly the same thing: the component is removed.

Examples: destroy a wheel → remove the wheel. Destroy a cannon → remove the cannon. Destroy a shield → remove the shield. Destroy a door → remove the door. Destroy a minifig → remove the minifig.

There are no special destruction rules. This is the canonical statement of "prefer physical representation" for damage — `11-combat.md` (CBT-009) points here instead of restating it.

---

## DMG-007 — Internal Components

Components may protect other components.

Example:

```
Armour → Pilot
```

The Pilot cannot be affected while the Armour blocks the incoming impact. Only after penetrating or destroying the Armour may the impact continue toward the Pilot (mechanically resolved by DMG-017, Penetration).

This naturally creates layered protection without requiring additional rules.

---

## DMG-008 — No Material-Specific Mechanics

Every component follows exactly the same mechanical rules regardless of what it represents — glass, metal, wood, infantry, or anything else. Resistance (DMG-003/004), the Geometry Check (DMG-014), the Damage Roll (DMG-015), and the Component State machine (DMG-005) apply identically to every component; where DMG-005's Wounded state costs a component something, the cost is set by the capability that component provides — moving, or attacking — and never by the material it represents. StudCraft does not define material-specific hit thresholds, Resistance modifiers, or damage tables of any kind.

A typical minifig (Resistance 3, per DMG-004 Example 1) takes exactly two failed Damage Rolls to go from Operational to Dead — the same as a wheel, a shield, or a cannon built with the same Resistance. Nothing about *what* a component represents changes how it resolves an Impact — only its Resistance does.

Physical/cosmetic representation of a component reaching Dead (how a broken window should look versus a destroyed wheel) is left entirely to the player and the table, per `02-core-rules.md` (CORE-016) — this document does not prescribe it. Future supplements may add cosmetic guidance for specific constructions without changing any mechanic defined here.

---

# Damage Resolution

This section defines the dice-based sequence that resolves an Impact against a component, once Part 1's structural rules have established the components and their resistance.

Combat in StudCraft is divided into two independent responsibilities:

- **Geometry** determines what is physically possible.
- **Dice** determine what actually happens.

The LEGO model defines capability. The dice introduce uncertainty.

## DMG-009 — Combat Resolution Overview

Every combat action follows the same sequence, whether ranged or melee (`12-melee.md`).

```
Weapon → Delivery Method → Generate Attack Dice → Attack Roll →
Successful Impacts → Select Target Component → Geometry Check →
Damage Roll → Component State Change → Penetration →
Physical Model Changes
```

Every impact is resolved independently.

---

## DMG-010 — Generate Impacts

Each weapon muzzle generates exactly one impact. The weapon specification already defines (per `10-weapons.md`):

- Number of impacts (Attack Dice, WPN-006 — one per muzzle)
- Impact Strength (WPN-021 — determined by muzzle size)

Example — Shotgun (`○ ○`, two muzzles) generates Impact A and Impact B.

---

## DMG-011 — Attack Roll

The attacker rolls one die for every generated impact. A result of 4, 5, or 6 succeeds and creates one valid impact (per `11-combat.md` CBT-005's existing threshold). A result of 1, 2, or 3 fails; the impact simply disappears.

Where the component providing the attack is Wounded — the weapon, or the attacker itself in an unarmed attack (`12-melee.md`, MEL-008) — the roll for each impact is two dice read as one (`11-combat.md`, CBT-015). The number of impacts rolled for does not change.

Example — two-barrel shotgun: one die succeeds, one fails. Only one impact continues.

---

## DMG-012 — Select Target Component

Every successful impact is assigned to one visible component. Hidden components cannot be selected as a target.

Examples: Shield, Wheel, Cannon, Door, Minifig, Armour Plate.

Impacts are never assigned to an entire vehicle — only to components.

---

## DMG-013 — Composite Vehicle Targeting

Every component of a composite vehicle behaves independently (per DMG-001). When a single attack generates multiple valid impacts, each impact may be assigned to a different visible component of the same target — impacts are never required to concentrate on one component.

Example — Jeep: Chassis, Driver, Cannon, Front Left Wheel, Front Right Wheel, Rear Left Wheel, Rear Right Wheel.

A player may intentionally target the cannon, the driver, or one wheel. Each resolves independently: destroying the cannon does not damage the vehicle; destroying a wheel does not damage the driver.

Example — Multiple Impacts, One Target: 6 impacts against the Jeep may be assigned as 2 → Window, 1 → Wheel, 2 → Turret, 1 → Door; each component resolves only the impacts assigned to it.

---

## DMG-014 — Geometry Check

The impact strength is compared against the resistance of the target component.

If `Strength < Resistance`: the impact immediately ends. No dice are rolled by the defender. The impact simply lacks enough energy to affect the component.

If `Strength ≥ Resistance`: the impact is capable of damaging the component. Combat continues to DMG-015.

---

## DMG-015 — Damage Roll

The defender rolls one D6 for that impact. A result of 4, 5, or 6 succeeds: nothing happens, the component remains unchanged. A result of 1, 2, or 3 fails: the component advances exactly one state (`Operational → Wounded` or `Wounded → Dead`).

This die does not represent armour — the Geometry Check already proved the impact could cause damage. It represents the uncertainty of combat: a fortunate deflection, an imperfect impact, a glancing hit, mechanical failure, luck.

---

## DMG-016 — Multiple Impacts

Each impact is completely independent. Impacts never combine their strength. Instead, each successful impact creates another opportunity to change the target's state.

Example — a shotgun (`○ ○`) against a minifig at Operational: both attack rolls succeed, both geometry checks succeed, the defender performs two Damage Rolls. If both fail, the minifig goes `Operational → Wounded → Dead`. The minifig dies from a single shotgun blast — not because the shotgun dealt more damage, but because it generated multiple impacts.

---

## DMG-017 — Penetration

An impact may continue through multiple components. "Successfully affects" here means the impact passed the Geometry Check (`Strength ≥ Resistance`, DMG-014) — penetration is a consequence of geometry, not of the Damage Roll's outcome. Whenever an impact passes the Geometry Check against a component, its remaining strength is calculated:

```
Remaining Strength = Current Strength − Component Resistance
```

If remaining strength is greater than zero, the impact continues in the same direction, toward the next component (per DMG-007, Internal Components) — regardless of whether the Damage Roll against the current component succeeds or fails.

### Example

Heavy Cannon (`Strength 6`) vs. Shield (`Resistance 3`): after affecting the shield, `Remaining Strength = 3`. The impact continues. A minifig behind the shield (`Resistance 3`) is still a valid target — `3 ≥ 3`, the impact is capable of damaging it. The minifig now performs its own Damage Roll. Each component always resolves independently.

---

## DMG-018 — Weapon Distribution

Each muzzle creates one independent impact.

By default, all impacts from the same weapon system are assigned to the same target (per `11-combat.md` CBT-007). This document adds one exception: impacts may be assigned to **different target units** only if the weapon mount can physically rotate to re-aim independently of the platform carrying it.

Examples of free rotation (exception applies): minifig torso, turntable, ball joint, swivel mount. This deliberately puts all infantry-carried weapon systems under the exception — a person's own body can turn between shots the way a vehicle's fixed hull mount cannot; this is intentional, not an oversight.

Examples that require Action Points instead (CBT-007 applies, no split): fixed mount, entire vehicle movement, repositioning the weapon carrier.

This is independent of DMG-013 (splitting a single target's incoming impacts across *its own* components) — that always applies regardless of mount type.

Weapon articulation is read directly from the LEGO model.

---

## DMG-019 — Repairs

A unit may spend **1 Action Point**, once per activation, to repair its own Wounded component, restoring it to Operational (`Wounded → Operational`). For an infantry model that repair is standing up — `DMG-005` is where the two poses are defined.

Repairing a *different* unit's Wounded component additionally requires visible repair equipment (`02-core-rules.md`, CORE-014 — a tool, medical pack, or similar) on the repairing unit, and physical adjacency to the target.

Dead components cannot be repaired — they have already been removed from the model. Future construction rules will define rebuilding.

---

# Combat Examples

## Example 1 — Pistol vs Minifig

Minifig `Resistance 3`. Pistol `Strength 3`. Attack Roll: Success. Geometry: `3 ≥ 3`. Damage Roll: Failure. Result: `Operational → Wounded`. Second successful impact: `Wounded → Dead`.

## Example 2 — Shotgun vs Minifig

Shotgun (2 muzzles, `Strength 3` each). Minifig `Resistance 3`. Attack Rolls: Success, Success. Both geometry checks succeed (`3 ≥ 3` each). Damage Rolls: Failure, Failure. Result: `Operational → Wounded → Dead`. One shotgun blast eliminates the Minifig.

## Example 3 — Heavy Cannon vs Shield

Shield `Resistance 3`. Heavy Cannon `Strength 6`. Attack succeeds. Geometry succeeds (`6 ≥ 3`). Damage Roll: Failure. Shield becomes `Wounded`. Remaining Strength `3` continues toward the protected Minifig, which now resolves the impact independently (DMG-017).

## Example 4 — Jeep Cannon

Mounted Cannon (2 plates thick, `Resistance 2`). Enemy Cannon `Strength 3`. Attack succeeds. Geometry succeeds (`3 ≥ 2`). Damage Roll fails. Mounted Cannon becomes `Wounded`. A second successful impact kills it. Remaining Strength `1` continues toward the Jeep's hull (one brick, `Resistance 3`), but `1 < 3` — the impact stops there. The Jeep remains operational but without its weapon.

## Example 5 — Rifle vs Bunker Wall

Bunker wall (two bricks thick, `Resistance 6`). Rifle `Strength 3` (one 1×1 muzzle). Attack Roll: Success. Geometry: `3 < 6`. The Impact ends immediately — no Damage Roll is made and the wall is unaffected (DMG-014).

Cracking it requires a larger muzzle, not more dice: a 2×2 muzzle generates `Strength 6`, which passes at `6 ≥ 6`.

---

# Combat Philosophy

StudCraft intentionally separates engineering from probability.

The LEGO model answers: **Can this happen?**

The dice answer: **Did it happen?**

Geometry determines capability. Dice determine uncertainty. Neither replaces the other.

---

# Summary

This document establishes the structural foundations of the damage system and the sequence that resolves it.

It defines: Components, Resistance, Structural States and what being Wounded costs (DMG-005), Destruction, Internal Protection, and the absence of any material-specific mechanic (DMG-008); and the combat resolution sequence — Generate Impacts, Attack Roll, Select Target Component, Composite Vehicle Targeting, Geometry Check, Damage Roll, Multiple Impacts, Penetration, Weapon Distribution, and Repairs.

The system never requires: Hit Points, Armour Values, Damage Statistics, Lookup Tables, Hidden Unit Profiles.

Every combat interaction emerges from two sources only: the physical LEGO construction, and the uncertainty introduced by the dice.

---

> **The Model Is The Rules.**
