# StudCraft Vehicle System

**Version:** 0.1.0 Draft

---

# Purpose

This document defines how vehicles are built and operated in StudCraft.

Vehicles do not use predefined statistics.

Their capabilities emerge directly from their physical construction.

Vehicle size, locomotion, crew and weapon systems determine how a vehicle behaves.

---

# Design Philosophy

Vehicles are physical machines.

Players should understand how a vehicle moves simply by looking at it.

StudCraft avoids abstract movement values whenever possible.

Instead, movement is determined by:

- Vehicle footprint
- Locomotion type
- Pilot
- Available space

---

# VEH-001 — Vehicle Footprint

A vehicle occupies one or more Unit Bases (UB) — see `02-core-rules.md` (CORE-001) for the Unit Base definition (4 × 3 studs).

Examples

| Vehicle | Footprint |
|----------|----------:|
| Bike | 1 × 2 UB |
| Buggy | 2 × 2 UB |
| Jeep | 2 × 3 UB |
| Tank | 2 × 5 UB |
| Heavy Transport | 3 × 8 UB |
| Super Heavy | Player Built |

No maximum vehicle size exists.

---

# VEH-002 — Vehicle Facing

Every vehicle must have an obvious front — the universal Facing rule (`02-core-rules.md`, CORE-002) applies to vehicles exactly like any other unit.

Facing additionally determines turning behavior, covered by the locomotion-specific rules (VEH-008 through VEH-011).

---

# VEH-003 — Measuring Vehicle Length

Vehicle length is measured along its longest axis.

Movement distance is always calculated from this length.

Decorative elements are ignored.

---

# VEH-004 — Standard Movement

A vehicle moves:

**One and a half (1.5×) times its own length**

Costing **1 Action Point** (`02-core-rules.md`, CORE-006), the same as any other Move action.

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

Wheel vehicles may perform, each costing **1 Action Point** (matching MOVE-008's infantry rotation cost):

- 90° Left Turn
- 90° Right Turn

The pivot point is the **rear axle** of the vehicle.

This simulates real steering geometry.

---

# VEH-009 — Tracked Vehicles

Tracked vehicles pivot around the center of the model.

They may rotate, each costing **1 Action Point**:

- 90°
- 180°
- 270°

This represents differential steering.

---

# VEH-010 — Walkers

Walkers pivot around the center of the model.

They may rotate freely in 90° increments, each costing **1 Action Point**.

Walkers ignore wheel steering restrictions.

---

# VEH-011 — Hover Vehicles

Hover vehicles behave similarly to wheeled vehicles: they move forward and backward at the standard cost (VEH-004), and may turn 90° left or right, each costing **1 Action Point**.

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

# VEH-013 — Pilot

Every powered vehicle — wheeled, tracked, walker, or hover (VEH-012) — requires a Pilot to move, a crew member (VEH-015) occupying a visible operating position.

The Pilot resolves Impacts like any other component (`16-damage-system.md`, DMG-005: Operational / Wounded / Dead).

If the vehicle has no Pilot — none embarked, or the Pilot is Dead — the vehicle cannot move, unless another crew member takes over (future rules).

---

# VEH-014 — Weapon Systems

Vehicle-mounted weapons follow the universal Weapon System rule (`10-weapons.md`, WPN-008; `11-combat.md`, CBT-006) — each visible weapon is its own independent weapon system, resolving attacks independently.

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

- Pilot
- Wheels
- Tracks
- Weapons
- Doors
- Windows
- Turrets

Components resolve Impacts independently (`16-damage-system.md`).

---

# VEH-018 — Damage

Vehicles do not have Hit Points.

Instead, individual components suffer the effects of Impacts.

Examples

Broken window

Disabled weapon

Destroyed wheel

Pilot lost

Destroyed door

This allows vehicles to degrade naturally over time.

---

# VEH-019 — Immobilized Vehicles

A vehicle that cannot move — through Pilot loss, locomotion damage, or being stranded in a drop (VEH-025) — remains on the battlefield.

It may continue operating any remaining functional systems unless otherwise specified.

---

# VEH-020 — Construction Priority

Vehicle performance should emerge from construction.

Whenever a new rule is proposed, ask:

"Can this be represented by the LEGO model?"

If the answer is yes,

the construction should take priority over abstraction.

---

# VEH-021 — Terrain Threshold

Every vehicle has a single **Terrain Threshold**, read from its locomotion system (VEH-012) rather than assigned as a statistic. It is measured in plate layers, the same unit obstacles and Resistance use (`16-damage-system.md`, DMG-003): a plate counts as 1 and a standard brick as 3.

The threshold governs three things:

- An obstacle **taller** than the threshold blocks movement. The vehicle cannot cross it and must go around, or ascend by a slope or ramp (VEH-027). Do not use MOVE-011's access-point list here: it is the infantry rule and includes stairs, which are never a legal vehicle ascent.
- A drop **deeper** than the threshold strands the vehicle (VEH-025).

- A rise **greater** than the threshold requires a slope or ramp to ascend (VEH-027).

An obstacle or drop equal to the threshold is crossed normally. Each locomotion type reads its own threshold: VEH-022 for wheels and tracks, VEH-023 for walkers, VEH-024 for hover.

A drop is not a fall. This rule covers driving into a depression, ditch or trench; a vehicle that leaves a height entirely is falling, and VEH-026 covers that. Both measure against this same threshold.

---

# VEH-022 — Wheeled and Tracked Thresholds

For a wheeled or tracked vehicle, the Terrain Threshold is **axle height**: the height of the wheel or road wheel's axle above the ground.

On a LEGO model this is the wheel's radius, so the threshold is half the wheel's own diameter — a wheel cannot climb a step taller than its own centre. Where a tracked build shows no visible axle, use half the height of the track run instead.

Wheeled and tracked vehicles are stranded by drops deeper than this threshold (VEH-025).

---

# VEH-023 — Walker Thresholds

For a walker, the Terrain Threshold is **knee height**: the height of the leg's knee joint above the ground, as built (`05-construction-components.md`, CMP-006).

A walker steps over obstacles below its knee and steps down into depressions below its knee without difficulty. Where a leg has no distinct knee joint, use half the leg's standing height.

Walkers are stranded by drops deeper than this threshold (VEH-025).

---

# VEH-024 — Hover Thresholds

For a hover vehicle, the Terrain Threshold is the height of the **hover assembly** — the emitters, pylons or skirt that hold the hull clear of the ground (`05-construction-components.md`, CMP-005) — measured in plate layers from the ground to where that assembly meets the hull.

This is the hover equivalent of a wheel's axle. In every locomotion type you measure the part that carries the vehicle, never the body it carries: the wheel to its axle (VEH-022), the leg to its knee (VEH-023), the hover assembly to its full height.

Measuring the assembly rather than the visible gap matters for enclosed builds. A skirt that reaches the ground leaves no gap to see, but its own height is still the threshold.

A hover model built with its hull flat on the ground has no assembly to measure and a Terrain Threshold of 0 — every obstacle blocks it. Nothing forbids that build; it simply cannot cross anything, which is the model telling you it is not finished. `CMP-005` already requires hover components to be visually distinguishable, and this is why: the assembly is the vehicle's terrain capability, so it has to be visible to be measured.

A taller assembly clears more terrain at the cost of a taller silhouette, which is easier to see and therefore to shoot (`02-core-rules.md`, CORE-008) — the same trade a walker makes with long legs.

Hover thresholds are usually the lowest of any locomotion type: a hover vehicle is stopped by walls a wheeled vehicle drives over. In exchange it is **never stranded by a drop** (VEH-025) — it passes over depressions instead of entering them, and their depth is irrelevant.

That immunity has one limit: a hover vehicle cannot cross a gap wider than its own footprint (VEH-001). There must be a surface beneath it to hover above.

Hover emitters are components like any other. If the assembly is destroyed the hull settles, the Terrain Threshold becomes 0, and the vehicle can still move across flat ground but is blocked by everything else.

---

# VEH-025 — Stranded Vehicles

A vehicle that enters a drop deeper than its Terrain Threshold (VEH-021) becomes **stranded** and is Immobilized, resolved exactly as VEH-019 already defines: it remains on the battlefield and may continue operating any remaining functional systems.

Stranded introduces no new state and no marker — the vehicle's position in the depression is the physical representation (`02-core-rules.md`, CORE-016).

Freeing a stranded vehicle is not yet defined, in the same way VEH-013 leaves crew replacement to future rules.

Hover vehicles cannot be stranded (VEH-024).

---

# VEH-026 — Vehicle Falling

A vehicle that leaves a height and comes down under gravity — rather than descending a slope or ramp (VEH-027) — falls. Measure the fall in plate layers, from the surface it left to the surface it lands on.

A fall no deeper than the vehicle's Terrain Threshold (VEH-021) causes no damage. The vehicle has dropped a kerb, not fallen.

Beyond that, roll one D6 for every complete brick (3 plate layers) fallen **past the threshold**. Each die is an independent Damage Roll (`16-damage-system.md`, DMG-015), resolved exactly as infantry falling is (`07-movement.md`, MOVE-016): a result of 4, 5 or 6 means nothing happens, and a result of 1, 2 or 3 advances one component by one state.

Every failed die is applied to a component that physically touches the ground when the vehicle lands — a wheel, a track, or a foot. The controlling player chooses which. Failures beyond the number of such components are lost: a vehicle whose locomotion is already destroyed is Immobilized (VEH-019) and cannot be immobilized twice.

**Crew and passengers are never harmed by a vehicle's fall.** This is a deliberate simplification rather than an oversight — the case is rare, and the consequence below is the real cost.

Hover vehicles take no falling damage. They descend under power rather than falling, consistent with their immunity to being stranded (VEH-024).

A vehicle at the bottom of a drop may be a trap. Infantry inside it disembark normally (`09-transport.md`, TRN-006), but then face the drop's walls as ordinary terrain: 7 or more plate layers requires a slope, stair or ramp (`07-movement.md`, MOVE-011, MOVE-014). Driving into a ravine can strand a squad as effectively as it strands the vehicle.

---

# VEH-027 — Vehicle Ascent

A vehicle crosses any rise no greater than its Terrain Threshold (VEH-021) by driving over it, whatever it is built from.

To reach a height **greater** than its Terrain Threshold, a vehicle needs a slope or a ramp that physically covers the entire rise, resting on both the lower and the upper surface. The angle does not matter and is never measured: LEGO slope elements (`04-construction-standard.md`, SCS-011) and a lowered ramp (SCS-008) bound it by their own construction.

If no slope or ramp covers the full rise, the height is impassable to that vehicle. It must go around.

**Stairs are never a legal ascent for a vehicle**, however shallow each step is. Infantry climb stairs (`07-movement.md`, MOVE-013); vehicles do not. What matters is the total rise, not the individual steps — a staircase is one obstacle, not a series of small ones.

A vehicle that descends a slope or ramp covering the full drop is driving, not falling, and takes no falling damage (VEH-026). A vehicle that leaves a height by any other route is falling.

This needs no separate walker rule. A walker whose knee clears the whole rise simply crosses it under VEH-021 — a tall enough walker steps over a flight of stairs the same way it steps over a wall.

---

# Summary

Vehicle behaviour is defined by six physical characteristics.

- Size
- Locomotion
- Terrain capability
- Crew
- Components
- Interior volume

No predefined vehicle profiles are required.

Terrain capability is read from the locomotion like everything else: a wheel's axle, a walker's knee, a hover assembly's height (VEH-021 through VEH-024).

A player should understand how a vehicle behaves simply by examining its construction.

---

> **Every Brick Matters.**