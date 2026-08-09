# StudCraft Vehicle System

**Version:** 0.2.0 Draft

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

A powered vehicle occupies two or more Unit Bases (UB) — see `02-core-rules.md` (CORE-001) for the Unit Base definition (4 × 3 studs), and VEH-013 for why one is not enough.

Examples

| Vehicle | Footprint |
|----------|----------:|
| Bike | 1 × 2 UB |
| Buggy | 2 × 2 UB |
| Jeep | 2 × 3 UB |
| Tank | 2 × 5 UB |
| Heavy Transport | 3 × 8 UB |
| Super Heavy | Player Built |

No maximum vehicle size exists. The footprint does bound how high the vehicle may build on it — one Unit Base for every two studs of its narrowest side (VEH-028) — and the agreed Deployment Volume bounds it again (`06-deployment.md`, DEP-001), but no dimension of the footprint itself is capped.

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

**Three (3×) times its own length**

Costing **1 Action Point** (`02-core-rules.md`, CORE-006), the same as any other Move action.

Measure from the vehicle's front, along its facing.

Every vehicle therefore covers three of its own lengths per action, whatever its size. A small vehicle is not slow — it is small. Because the multiplier is a whole number, every resulting distance is a whole number of studs; there is no half stud to measure.

Examples

Footprints below are VEH-001's; only the two right-hand columns belong to this rule.

| Vehicle | Longest dimension | Movement |
|---|---:|---:|
| Bike | 6 studs | 18 studs |
| Buggy | 8 studs | 24 studs |
| Jeep | 9 studs | 27 studs |
| Tank | 15 studs | 45 studs |
| Heavy Transport | 24 studs | 72 studs |

Large vehicles rarely realise these figures. A 24-stud transport moving 72 studs needs a clear lane of nearly a hundred studs, and terrain seldom offers one — the limit in play is the battlefield, not the rule.

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

Because the Pilot occupies a Unit Base of its own (`09-transport.md`, TRN-014), a powered vehicle needs room for its Pilot in addition to its machinery. This is why the minimum footprint is two Unit Bases (`02-core-rules.md`, CORE-004; VEH-001) rather than one: at one, the Pilot is the whole vehicle. The floor is not a chosen number — it is whatever this rule and TRN-014 together imply.

The Pilot resolves Impacts like any other component (`16-damage-system.md`, DMG-005: Operational / Wounded / Dead).

If the vehicle has no Pilot — none embarked, or the Pilot is Dead — the vehicle cannot move, unless another crew member takes over (future rules).

---

# VEH-014 — Weapon Systems

Vehicle-mounted weapons follow the universal Weapon System rule (`10-weapons.md`, WPN-008; `11-combat.md`, CBT-006) — each visible weapon is its own independent weapon system, resolving attacks independently.

---

# VEH-015 — Crew

Vehicles may carry one or more crew members.

Crew must physically fit inside the vehicle. A crew member occupies a Unit Base like any other passenger (`09-transport.md`, TRN-014), so what must fit is that Unit Base (`02-core-rules.md`, CORE-001).

Crew visibility depends on the construction.

An exposed driver may be targeted.

A fully enclosed crew compartment protects the crew.

---

# VEH-016 — Passengers

Passenger capacity depends entirely on the interior volume.

If a passenger's Unit Base physically fits, it may embark (`02-core-rules.md`, CORE-001).

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

A taller assembly clears more terrain at the cost of a taller silhouette, which is easier to see and therefore to shoot (`02-core-rules.md`, CORE-008), and of the height it takes against both of VEH-028's bounds — the footprint's proportion as much as the agreed ceiling. That is the same trade a walker makes with long legs.

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

# VEH-028 — Maximum Height

A vehicle's height is bounded twice, and it is legal only under both bounds:

- **By its own footprint.** For every two studs across the narrowest side of its footprint, a vehicle may rise one Unit Base.
- **By the agreed ceiling.** No model may exceed the height agreed for the Deployment Volume (`06-deployment.md`, DEP-001).

The two answer different questions and neither replaces the other. The footprint bound is a proportion the model carries wherever it is played: a vehicle may be as tall as its own base justifies. The ceiling is the size of the game, agreed once and the same for every model on the table. A wide vehicle in a low-roofed scenario is stopped by the ceiling; a narrow one in a large game is stopped by its footprint.

The footprint is the Unit Bases the vehicle covers — the ones `06-deployment.md` (DEP-003) charges. Written `A × B` UB it measures `4A × 3B` studs (`02-core-rules.md`, CORE-001), so its narrowest side is the smaller of those two numbers. Where an outline is not rectangular, read `A × B` as the smallest rectangle of Unit Bases enclosing it. That rectangle serves this measurement only and changes no vehicle's Deployment Volume cost, which DEP-003 still charges per Unit Base actually covered.

The proportion is read off the Unit Base rather than chosen. One Unit Base is the volume one person occupies, on a narrowest side of 3 studs; a vehicle is allowed half as much again, which is half a Unit Base of height for every stud and therefore one for every two. Stating it in Unit Bases rather than in plate layers keeps it true of the unit itself — `02-core-rules.md` (CORE-001) owns the conversion, and nothing here repeats it.

| Vehicle | Footprint | Studs | Narrowest side | Maximum Height |
|---|---|---|---:|---:|
| Bike | 1 × 2 UB | 4 × 6 | 4 | 2 UB |
| Buggy | 2 × 2 UB | 8 × 6 | 6 | 3 UB |
| Jeep | 2 × 3 UB | 8 × 9 | 8 | 4 UB |
| Tank | 2 × 5 UB | 8 × 15 | 8 | 4 UB |
| Heavy Transport | 3 × 8 UB | 12 × 24 | 12 | 6 UB |

Tank and Jeep share a limit because they share a narrowest side. Stretching a vehicle along its long axis buys it nothing: a long thin vehicle is still a thin vehicle.

The same two Unit Bases give different limits depending on how they are arranged — side by side (2 × 1 UB, 8 × 3 studs) they allow one and a half Unit Bases, front to back (1 × 2 UB, 4 × 6 studs) two. That is not an exploit to close. The arrangement is built into the model, chosen once at the bench and paid for in the shape of the vehicle. Turning the finished model on the table changes nothing, because the narrowest side is a property of the rectangle and not of which way it points.

An odd narrowest side gives a limit of a whole number of Unit Bases and a half. Nothing is rounded: a vehicle's own height is measured in plate layers (VEH-030) and compared against the limit.

Height is counted once, from the surface the vehicle rests on (VEH-029) to the top of its Gameplay Geometry (VEH-030) — **locomotion included** — and that one figure is checked against both bounds. A walker's legs, a wheel's diameter and a hover assembly are height exactly as a hull is: they are what holds the rest of the model up there, and a base that cannot justify a tall hull cannot justify tall legs either.

A vehicle exceeding either bound is not a legal vehicle. It cannot be deployed until it is rebuilt — lower, or on a wider footprint — or, where the ceiling is what stops it, until the players agree a taller volume. There is no penalty, no marker and no in-game state: this is a construction check made once before the game, exactly like the two-Unit-Base minimum (`02-core-rules.md`, CORE-004; VEH-013). Legality is settled before deployment and never revisited, so a vehicle whose construction is altered in play (VEH-018) is not measured again.

This introduces no height statistic, vehicle class or size category. VEH-001's "No maximum vehicle size exists" stays true as written: a footprint may be any size, and the height allowed grows with it.

How many interior levels a vehicle carries follows from whichever bound is lower, at the cost `09-transport.md` (TRN-020) sets.

---

# VEH-029 — Where Height Is Counted From

Height (VEH-028) is counted from **the surface the vehicle rests on when it stands on its own locomotion**. A vehicle that begins the game inside another (`09-transport.md`, TRN-001, TRN-003) is measured the same way and against its own two bounds: its own height is what is checked, never its height plus the carrier's, and a vehicle stowed lying down or in a cradle is measured as it would stand.

**Locomotion counts.** Everything between that surface and the top of the vehicle's Gameplay Geometry is the vehicle's height: a walker two Unit Bases tall on legs another Unit Base long stands three Unit Bases high, and which part of it reaches that far changes nothing — not for the room it takes under the ceiling, and not for the proportion its footprint has to justify (VEH-028).

Terrain capability is still read from those same parts — a wheel by its axle (VEH-022), a leg by its knee (VEH-023), a hover assembly by its full height (VEH-024) — and tall locomotion still costs silhouette (`02-core-rules.md`, CORE-008). What it no longer buys is reach no limit can see. This rule used to say a vehicle "can gain reach by standing on tall locomotion instead of by building upward, and this limit never sees it"; reach gained on long legs and reach gained by building upward are the same reach on the table, so both are now measured, and both are checked against both of VEH-028's bounds. A walker that wants long legs wants a wider footprint to justify them.

This is a check made at the bench, not on the table. A vehicle on a hill, in a depression or part-way up a ramp is not measured again: legality was settled before deployment (VEH-028), so terrain elevation never enters it.

Height is counted straight up, never along a leaning element. A mast raked backwards is measured by how high it reaches, not by how long it is.

---

# VEH-030 — What Counts Toward Height

A vehicle's height (VEH-028) is counted to the highest point of its **Gameplay Geometry** (`15-geometry-layers.md`, GEO-001). Visual Geometry above that point is unrestricted and never makes a vehicle illegal.

Height is plastic, measured from the surface the vehicle rests on (VEH-029) in plate layers. Nothing is converted into anything else: a weapon's Length is measured in studs along its own firing axis (`10-weapons.md`, WPN-003), and a weapon standing upright is measured by how high its plastic actually reaches.

This rule adds no classification of its own, and writes no list of functional and decorative parts — a second list would drift from `15-geometry-layers.md` (GEO-002)'s. Which layer an element belongs to is GEO-001 and GEO-002's question, settled by the test those rules already apply: Gameplay Geometry is the minimum physical information required to play the game, and Visual Geometry is what remains when an element's purpose is purely aesthetic. The table below is that test applied to height, not a new one.

| Element | Layer | Counts |
|---|---|---|
| Bare mast, flag, ornament, non-functional antenna | Visual | No |
| Mast carrying an observation post | Gameplay | Yes |
| Turret mounting a weapon (`10-weapons.md`, WPN-009) | Gameplay | Yes |
| Superstructure holding a crew station (`09-transport.md`, TRN-014) | Gameplay | Yes |
| Transport space (`09-transport.md`, TRN-003) | Gameplay | Yes |
| Decorative armour bolted onto a structural wall | Visual | No |

An element holding a crew position is Gameplay Geometry because a crew member occupies a Unit Base of its own (TRN-014). A mast holding nothing carries no Unit Base and feeds no measured value — GEO-002 lists antennas among its own examples of Visual Geometry for exactly that reason. A mast is therefore measured to the height of whatever it carries, and everything below that point is included automatically; only plastic continuing *above* the last functional element is free.

This is not an exception to `15-geometry-layers.md` (GEO-004). GEO-007 settles it: a model does not become invalid, and its measured values do not change, solely as a result of adding Visual Geometry — and a height limit that counted decoration would invalidate a legal vehicle the moment a flag went on it. Access openings ask a different question, whether a model physically passes through (`05-construction-components.md`, CMP-018), and decoration obstructs passage, so it counts there. Both of VEH-028's bounds ask how much functional construction a model raises into the volume, and a flag raises none.

Decoration is never free in play, only in legality. A tall decorative mast is real plastic: visible, blocking sight lines and shootable (`02-core-rules.md`, CORE-008; GEO-004). The player who builds one pays in silhouette rather than in a rules violation.

**A movable element is measured in the highest position it can physically be placed in during play**, not the position it happens to occupy when checked. A turret that rotates, a barrel that elevates and a ramp that lifts are Gameplay Geometry wherever they are placed; measured as found, the check would be answered by lowering the barrel first and raising it again afterwards.

**A model carried on the outside counts too.** Transported models occupy a physically constructed interior space measured in Unit Bases (`09-transport.md`, TRN-001, TRN-003); a model on a roof, bonnet, hull top or the outside of a turret is not in such a space and is not embarked. Nothing forbids placing it there. It counts toward this height, measured in the highest position it can be placed in, because it can see, be seen and be shot at (`02-core-rules.md`, CORE-008, CORE-009) — and it costs Deployment Volume of its own, which `06-deployment.md` (DEP-006) owns. The outside of a vehicle is never a cheaper way to carry a model than the inside.

Externally carried models are counted at the one check VEH-028 describes, so a model that mounts, dismounts or is removed in play never causes the vehicle to be measured again.

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

Height is read from both the footprint and the agreed Deployment Volume: one Unit Base for every two studs of the narrowest side, and never above the ceiling the players agreed, counted from the surface the vehicle rests on and measured to the top of its Gameplay Geometry (VEH-028 through VEH-030).

A player should understand how a vehicle behaves simply by examining its construction.

---

> **Every Brick Matters.**