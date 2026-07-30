# StudCraft Vehicle System

**Version:** 0.1.0 Draft

---

# Purpose

This document defines how vehicles are built and operated in StudCraft.

Vehicles do not use predefined statistics.

Their capabilities emerge directly from their physical construction.

Vehicle size, locomotion, engines and weapon systems determine how a vehicle behaves.

---

# Design Philosophy

Vehicles are physical machines.

Players should understand how a vehicle moves simply by looking at it.

StudCraft avoids abstract movement values whenever possible.

Instead, movement is determined by:

- Vehicle footprint
- Locomotion type
- Engine
- Available space

---

# VEH-001 — Vehicle Footprint

A vehicle occupies one or more Unit Bases (UB) — see `02-core-rules.md` (CORE-001) for the Unit Base definition (4 × 3 studs).

Examples

Motorbike

1 × 2 UB

Jeep

2 × 3 UB

Tank

2 × 5 UB

Heavy Transport

3 × 8 UB

No maximum vehicle size exists.

---

# VEH-002 — Vehicle Facing

Every vehicle must have an obvious front.

Facing determines:

- Forward movement
- Rear
- Left
- Right
- Weapon arcs
- Turning

---

# VEH-003 — Measuring Vehicle Length

Vehicle length is measured along its longest axis.

Movement distance is always calculated from this length.

Decorative elements are ignored.

---

# VEH-004 — Standard Movement

A vehicle moves:

**One and a half (1.5×) times its own length**

Measure from the vehicle's front.

After moving, the rear of the vehicle will approximately occupy the previous position of the front, plus half its own length.

Examples

Vehicle length:

8 studs

Movement:

12 studs

Vehicle length:

12 studs

Movement:

18 studs

Vehicle length:

20 studs

Movement:

30 studs

This rule scales naturally for all vehicle sizes.

---

# VEH-005 — Forward Movement

Vehicles normally move forward.

Movement follows the vehicle's current facing.

Diagonal movement does not exist.

---

# VEH-006 — Reverse Movement

Vehicles may move backwards.

They keep their current facing.

Reverse movement uses the same movement distance unless restricted by future scenarios.

---

# VEH-007 — No Diagonal Movement

StudCraft does not use diagonal movement.

Vehicles combine forward movement with turns.

---

# VEH-008 — Wheel Vehicles

Vehicles using wheels represent conventional steering systems.

Wheel vehicles may perform:

- 90° Left Turn
- 90° Right Turn

The pivot point is the **rear axle** of the vehicle.

This simulates real steering geometry.

---

# VEH-009 — Tracked Vehicles

Tracked vehicles pivot around the center of the model.

They may rotate:

- 90°
- 180°
- 270°

This represents differential steering.

---

# VEH-010 — Walkers

Walkers pivot around the center of the model.

They may rotate freely in 90° increments.

Walkers ignore wheel steering restrictions.

---

# VEH-011 — Hover Vehicles

Hover vehicles behave similarly to wheeled vehicles.

They may:

- Move forward and backward.
- Turn 90° left or right.

They pivot around the center of the model instead of the rear.

Future rules may introduce lateral movement for advanced hover systems.

---

# VEH-012 — Locomotion Type

Every vehicle must clearly represent one locomotion system.

Examples

- Wheels
- Tracks
- Walker Legs
- Hover System

A vehicle cannot combine locomotion systems unless explicitly designed to do so.

---

# VEH-013 — Engine

Every powered vehicle must include an engine.

The engine is represented by a **4×2 brick** integrated into the model.

The engine is a mandatory functional component.

If destroyed, the vehicle may become immobilized.

Future versions may define engine colors to represent different power classes.

---

# VEH-014 — Weapon Systems

Each visible weapon is treated as an independent weapon system.

Vehicle weapons follow the Weapon Rules.

Each weapon resolves attacks independently.

---

# VEH-015 — Crew

Vehicles may carry one or more crew members.

Crew must physically fit inside the vehicle.

Crew visibility depends on the construction.

An exposed driver may be targeted.

A fully enclosed crew compartment protects the crew.

---

# VEH-016 — Passengers

Passenger capacity depends entirely on the interior volume.

If a passenger physically fits, it may embark.

If it does not fit, it cannot.

No transport statistic exists.

---

# VEH-017 — Components

Vehicles are collections of components.

Examples

- Engine
- Wheels
- Tracks
- Weapons
- Doors
- Windows
- Turrets

Components resolve Impacts independently.

See:

materials.md

---

# VEH-018 — Damage

Vehicles do not have Hit Points.

Instead, individual components suffer the effects of Impacts.

Examples

Broken window

Disabled weapon

Destroyed wheel

Damaged engine

Destroyed door

This allows vehicles to degrade naturally over time.

---

# VEH-019 — Immobilized Vehicles

A vehicle that cannot move due to engine or locomotion damage remains on the battlefield.

It may continue operating any remaining functional systems unless otherwise specified.

---

# VEH-020 — Construction Priority

Vehicle performance should emerge from construction.

Whenever a new rule is proposed, ask:

"Can this be represented by the LEGO model?"

If the answer is yes,

the construction should take priority over abstraction.

---

# Summary

Vehicle behaviour is defined by five physical characteristics.

- Size
- Locomotion
- Engine
- Components
- Interior volume

No predefined vehicle profiles are required.

A player should understand how a vehicle behaves simply by examining its construction.

---

> **Every Brick Matters.**