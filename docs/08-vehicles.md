# StudCraft Vehicle System

**Version:** 0.2.0 Draft

---

# Purpose

This document defines how vehicles are built and operated in StudCraft.

Vehicles have no predefined statistics. Their capabilities emerge from their physical construction.

Vehicle size, locomotion, crew, weapons and interior space determine how a vehicle behaves.

---

# Design Philosophy

Vehicles are physical machines.

Their capabilities should be readable from their construction rather than from abstract statistics.

---

# VEH-001 — Vehicle Footprint

A powered vehicle occupies two or more Unit Bases (UB) (`02-core-rules.md`, CORE-001).

| Vehicle         |    Footprint |
| --------------- | -----------: |
| Bike            |     1 × 2 UB |
| Buggy           |     2 × 2 UB |
| Jeep            |     2 × 3 UB |
| Tank            |     2 × 5 UB |
| Heavy Transport |     3 × 8 UB |
| Super Heavy     | Player Built |

There is no maximum footprint size. A vehicle's footprint determines its maximum height (VEH-028), while the Deployment Volume provides an additional ceiling (`06-deployment.md`, DEP-001).

---

# VEH-002 — Vehicle Facing

Every vehicle must have an obvious front.

The front is the end the model is built to lead with. Facing follows `02-core-rules.md` (CORE-002) and determines movement and turning (`07-movement.md`, MOVE-001; VEH-008 through VEH-011).

---

# VEH-003 — Measuring Vehicle Length

Vehicle length is measured along its longest axis.

Movement distance is calculated from this length. Decorative elements are ignored.

---

# VEH-004 — Standard Movement

A vehicle moves **three times its own length** for **1 Action Point** (`02-core-rules.md`, CORE-006).

Measure from the vehicle's front along its facing (`07-movement.md`, MOVE-003). The same point is used when moving in reverse (VEH-006).

| Vehicle         |   Length | Movement |
| --------------- | -------: | -------: |
| Bike            |  6 studs | 18 studs |
| Buggy           |  8 studs | 24 studs |
| Jeep            |  9 studs | 27 studs |
| Tank            | 15 studs | 45 studs |
| Heavy Transport | 24 studs | 72 studs |

A Wounded Pilot reduces this to twice the vehicle's length (VEH-031).

---

# VEH-005 — Forward Movement

Vehicles normally move forward in their current facing.

---

# VEH-006 — Reverse Movement

Vehicles may move backwards while retaining their current facing.

Reverse movement uses the same distance as forward movement unless restricted by a scenario.

---

# VEH-007 — No Diagonal Movement

Vehicles do not move diagonally (`07-movement.md`, MOVE-007).

They combine forward or reverse movement with turns.

---

# VEH-008 — Wheel Vehicles

Wheel vehicles may perform either of the following for **1 Action Point**:

* 90° left turn
* 90° right turn

They pivot around their rear axle.

---

# VEH-009 — Tracked Vehicles

Tracked vehicles pivot around their centre.

For **1 Action Point**, they may rotate:

* 90°
* 180°
* 270°

---

# VEH-010 — Walkers

Walkers pivot around their centre.

For **1 Action Point**, they may rotate 90° in either direction.

---

# VEH-011 — Hover Vehicles

Hover vehicles move forward and backward using standard movement (VEH-004).

They may turn 90° left or right for **1 Action Point**, pivoting around their centre.

Future rules may introduce lateral movement.

---

# VEH-012 — Locomotion Type

Every vehicle must clearly represent one locomotion system.

Examples:

* Wheels
* Tracks
* Walker legs
* Hover system

Vehicles cannot combine locomotion systems unless explicitly designed to do so.

---

# VEH-013 — Pilot

Every powered vehicle requires a Pilot: a minifigure physically occupying a visible operating position (`VEH-015`).

A decorative empty seat is not a Pilot.

The Pilot occupies one Unit Base (`09-transport.md`, TRN-014), so the vehicle requires space for the Pilot in addition to its machinery. This establishes the two-Unit-Base minimum in VEH-001.

The Pilot resolves Impacts as a normal component (`16-damage-system.md`, DMG-005).

A vehicle without a Pilot, or with a Dead Pilot, cannot move unless another crew member takes over.

---

# VEH-014 — Weapon Systems

Each visible vehicle weapon is an independent weapon system and follows the universal Weapon System rules (`10-weapons.md`, WPN-008; `11-combat.md`, CBT-006).

---

# VEH-015 — Crew

Vehicles may carry one or more crew members.

Crew must physically fit inside the vehicle. Each crew member occupies one Unit Base (`09-transport.md`, TRN-014, TRN-019).

Exposed crew can be targeted. Fully enclosed crew is protected by the construction.

---

# VEH-016 — Passengers

Passenger capacity is determined by interior volume (`09-transport.md`).

A passenger may embark only when the transport has enough free Unit Bases for that passenger (`09-transport.md`, TRN-005).

No transport capacity statistic exists.

---

# VEH-017 — Components

Vehicles are collections of components.

Examples:

* Pilot
* Wheels
* Tracks
* Weapons
* Doors
* Windows
* Turrets

Components resolve Impacts independently (`16-damage-system.md`).

---

# VEH-018 — Damage

Vehicles have no Hit Points.

Impacts affect individual components.

Examples:

* Broken window
* Disabled weapon
* Destroyed wheel
* Lost Pilot
* Destroyed door

---

# VEH-019 — Immobilized Vehicles

A vehicle that cannot move remains on the battlefield and may continue operating its functional systems unless another rule states otherwise.

This includes vehicles immobilized by Pilot loss, locomotion damage or being stranded (`VEH-025`).

---

# VEH-020 — Construction Priority

Vehicle performance should emerge from construction.

> **Can this be represented by the LEGO model?**

If so, construction takes priority over abstraction.

---

# VEH-021 — Terrain Threshold

Every vehicle has a **Terrain Threshold**, determined by its locomotion (`VEH-022` through `VEH-024`).

It is measured in plate layers (`16-damage-system.md`, DMG-003).

* An obstacle taller than the threshold blocks movement.
* A rise greater than the threshold requires a slope or ramp (`VEH-027`).
* A drop deeper than the threshold strands the vehicle (`VEH-025`).
* Obstacles and drops equal to the threshold are crossed normally.

Stairs are never a legal vehicle ascent.

A vehicle leaving a height entirely is falling and uses VEH-026 instead.

---

# VEH-022 — Wheeled and Tracked Thresholds

For wheeled and tracked vehicles, the Terrain Threshold is the height of the wheel or road wheel's axle above the ground.

This is half the wheel's diameter. Where a tracked vehicle has no visible axle, use half the height of the track run.

---

# VEH-023 — Walker Thresholds

For walkers, the Terrain Threshold is the height of the knee joint above the ground (`05-construction-components.md`, CMP-006).

Where no distinct knee exists, use half the leg's standing height.

---

# VEH-024 — Hover Thresholds

For hover vehicles, the Terrain Threshold is the height of the hover assembly (`05-construction-components.md`, CMP-005), measured from the ground to where the assembly meets the hull.

A hull resting directly on the ground has a threshold of 0.

Hover vehicles cannot be stranded by drops and may pass over depressions.

They cannot cross a gap wider than their own footprint: a surface must remain beneath the vehicle.

If the hover assembly is destroyed, the hull settles and its Terrain Threshold becomes 0.

---

# VEH-025 — Stranded Vehicles

A vehicle that enters a drop deeper than its Terrain Threshold becomes **stranded** and is Immobilized (`VEH-019`).

Its position in the depression represents the state; no marker is used (`02-core-rules.md`, CORE-016).

Freeing a stranded vehicle is not currently defined.

Hover vehicles cannot be stranded (`VEH-024`).

---

# VEH-026 — Vehicle Falling

A vehicle that leaves a height without using a slope or ramp falls.

Measure the fall from the surface left to the surface reached, in plate layers (`07-movement.md`, MOVE-015).

A fall no deeper than the Terrain Threshold causes no damage.

Beyond the threshold, roll one D6 for every complete brick (3 plate layers) of additional fall. Each roll is a Damage Roll (`16-damage-system.md`, DMG-015):

* 4–6: no effect
* 1–3: one component advances one state

Each failed roll is assigned to a component physically touching the ground when the vehicle lands. The controlling player chooses the component.

Failures beyond the number of eligible components are lost.

Crew and passengers are never harmed by a vehicle's fall.

Hover vehicles take no falling damage.

Infantry may disembark from a vehicle at the bottom of a drop (`09-transport.md`, TRN-006), but the drop's walls remain ordinary terrain (`17-infantry.md`, INF-008, INF-010).

---

# VEH-027 — Vehicle Ascent

A vehicle may cross a rise no greater than its Terrain Threshold (`VEH-021`) directly.

A greater rise requires a slope or ramp covering the entire rise and resting on both surfaces. The angle is not measured (`07-movement.md`, MOVE-012; `05-construction-components.md`, CMP-021).

If no suitable slope or ramp exists, the rise is impassable.

Stairs are never a legal vehicle ascent.

A vehicle descending a full slope or ramp is driving, not falling. Any other descent is a fall (`VEH-026`).

A walker may cross a rise or stairs directly when its Terrain Threshold permits it.

---

# VEH-029 — Where Height Is Counted From

Vehicle height is measured from the surface the vehicle rests on when standing on its own locomotion to its highest point.

Locomotion counts.

A vehicle carried inside another vehicle is measured as it would stand on its own, against its own limits (`09-transport.md`, TRN-001, TRN-003).

Terrain does not change a vehicle's legal height. A vehicle on a hill, in a depression or on a ramp is not remeasured.

Height is measured vertically, never along a leaning element.

Terrain capability is still read from the relevant locomotion component (`VEH-022` through `VEH-024).

---

# VEH-030 — What Counts Toward Height

Vehicle height is measured to the highest point of its **Gameplay Geometry** (`15-geometry-layers.md`, GEO-001).

Visual Geometry does not affect the height limit.

| Element                                           | Layer    | Counts |
| ------------------------------------------------- | -------- | ------ |
| Bare mast, flag, ornament, non-functional antenna | Visual   | No     |
| Mast carrying an observation post                 | Gameplay | Yes    |
| Turret mounting a weapon                          | Gameplay | Yes    |
| Superstructure holding a crew station             | Gameplay | Yes    |
| Transport space                                   | Gameplay | Yes    |
| Decorative armour                                 | Visual   | No     |

Movable Gameplay Geometry is measured in its highest position during play.

Models carried outside a vehicle are not embarked and count toward vehicle height. They also occupy their own Deployment Volume space (`06-deployment.md`, DEP-006).

Adding Visual Geometry does not change vehicle height or legality (`15-geometry-layers.md`, GEO-007).

---

# VEH-031 — Wounded Pilot

A vehicle with a Wounded Pilot (`VEH-013`) moves **twice its own length** per movement action instead of three times (`VEH-004`).

Facing, measurement and Action Point cost are unchanged.

| Vehicle         |   Normal | Wounded Pilot |
| --------------- | -------: | ------------: |
| Bike            | 18 studs |      12 studs |
| Buggy           | 24 studs |      16 studs |
| Jeep            | 27 studs |      18 studs |
| Tank            | 45 studs |      30 studs |
| Heavy Transport | 72 studs |      48 studs |

Only the Pilot's Wounded state affects movement. A Wounded locomotion component does not change movement distance.

A destroyed locomotion component is governed by VEH-019.

---

# Summary

Vehicle behaviour emerges from:

* Size
* Locomotion
* Terrain capability
* Crew
* Components
* Interior volume

Vehicles have no predefined profiles or statistics.

Terrain capability comes from the locomotion's construction.

Height is determined by the vehicle's footprint and the Deployment Volume ceiling.

A Wounded Pilot reduces movement from three lengths to two.

---

> **Every Brick Matters.**
