# StudCraft Transport System

**Version:** 0.2.0 Draft

---

# Purpose

This document defines how units embark, travel and disembark from transport vehicles.

StudCraft does not use abstract transport statistics.

Instead, transport capacity is the **Unit Base (UB)** volume available inside the vehicle.

This creates a unified system where deployment, movement and transport all use the same unit of measurement.

---

# Design Philosophy

Transport vehicles are mobile spaces.

Every transported object occupies physical space measured in Unit Bases.

The interior layout of a vehicle is therefore a meaningful design decision.

---

# TRN-001 — Unit Base Occupancy

Every transported object occupies Unit Base volume — one or more whole Unit Bases, or a share of one where the object is cargo shorter than a Unit Base (TRN-013). See `02-core-rules.md` (CORE-001) for the Unit Base definition.

This represents the minimum operational space required by the object.

Examples:

- Infantry: 1 UB
- Supply crate: up to 1 UB (TRN-013)
- Motorcycle: 2 UB
- Light Walker: 2 UB
- Heavy Walker: Defined by its footprint

---

# TRN-002 — Infantry Occupancy

Every infantry model always occupies exactly **1 Unit Base** (`02-core-rules.md`, CORE-003).

This includes:

- The minifigure
- Its weapons
- Equipment
- Backpack
- Shield
- Accessories

Whether standing or seated, the infantry model continues to occupy exactly one Unit Base.

Changing posture never changes transport capacity.

A Unit Base is a volume, and cargo may divide one (TRN-013) — see `02-core-rules.md` (CORE-001). A minifigure never does: no Unit Base is shared with one, even when a seated model physically leaves room above it. The space was paid for on embarking (TRN-005).

---

# TRN-003 — Cargo Capacity

A transport vehicle's capacity is the Unit Base volume available inside its cargo compartment — see `02-core-rules.md` (CORE-001).

Count the Unit Bases its floor holds, then check its clearance (TRN-019): a position with less than one Unit Base of clear height above it is a partial Unit Base, not a whole one.

A load is measured against that volume:

- Infantry counts one whole Unit Base apiece, and never shares (TRN-002).
- Cargo counts its own height, and several objects may share one Unit Base (TRN-013).

Example:

Cargo bay:

2 × 4 UB, one Unit Base of clear height

Capacity:

8 UB

Possible loads:

- 8 infantry
- 4 infantry + 1 light walker (2 UB) + 2 UB of cargo
- 6 infantry + six ammo crates of 4 plate layers each — three crates share one Unit Base, so six take two
- Any legal combination occupying no more than 8 UB

---

# TRN-004 — Interior Layout

The cargo compartment should clearly represent its available Unit Bases.

Interior design is part of the game.

Examples:

- Seats
- Benches
- Cargo racks
- Empty floor
- Equipment lockers

These elements occupy space and influence transport capacity.

---

# TRN-005 — Embarking

Embarking costs **1 Action Point per Unit Base** the embarking unit occupies — an infantry model (1 UB) costs 1 AP; a motorcycle (2 UB) costs 2 AP, matching Disembarking (TRN-006).

The AP is spent from the embarking unit's own pool, during its own activation (`03-game-flow.md`, FLOW-004) — the same 3 AP it can also spend moving, attacking, or otherwise acting that same activation (`FLOW-007`). It does not receive a separate activation later just because it ended up inside a transport.

Requirements:

- The unit must be adjacent to a functional access point.
- The access point must be open.
- A free Unit Base must exist inside the transport — free as a volume, so the compartment's clearance must admit it (TRN-019).

The model is then physically placed inside one available Unit Base.

---

# TRN-006 — Disembarking

Disembarking costs:

**1 Action Point per Unit Base**

An infantry model (1 UB) therefore costs:

**1 AP**

The AP is spent from the disembarking unit's own pool, during its own activation — a unit that begins its activation already embarked spends AP to disembark, then may spend any AP remaining from the same 3 AP allotment to move, attack, or otherwise act.

The unit must be placed adjacent to a functional access point.

If there is insufficient space outside the vehicle, the unit cannot disembark.

---

# TRN-007 — Access Points

Only functional access points may be used.

An access point's opening must physically pass the models that use it; one that does not is decorative (`05-construction-components.md`, CMP-018).

Examples:

- Doors
- Rear ramps
- Side hatches
- Roof hatches

Decorative access points have no gameplay effect.

---

# TRN-008 — Opening and Closing

Opening or closing any access point costs **1 Action Point** (`02-core-rules.md`, CORE-007).

Examples:

- Door
- Ramp
- Cargo hatch

The component must physically move.

---

# TRN-009 — Open Transport

A transport is considered open when transported units are physically visible.

Examples:

- Jeep
- Truck
- Hover platform
- Open boat
- Flatbed vehicle

Visible passengers:

- May be targeted.
- May attack.
- Require normal line of sight (`02-core-rules.md`, CORE-008/CORE-009; `11-combat.md`, CBT-002).

---

# TRN-010 — Closed Transport

A transport is considered closed when passengers are completely enclosed.

Passengers inside:

- Cannot be targeted directly.
- Cannot attack unless firing through an opening.

Protection comes from the vehicle's construction: passengers are internal components the hull protects, exactly like any other Internal Components relationship (`16-damage-system.md`, DMG-007) — an Impact that penetrates the hull with remaining strength continues toward them (DMG-017) like it would toward any protected component. No additional armour value is required; the hull's own Resistance is what stands between the Impact and the passengers.

---

# TRN-011 — Firing Ports

A transport may include:

- Windows
- Gun ports
- Roof hatches
- Observation slits

Only passengers with physical line of sight through these openings may attack.

The opening determines the firing arc.

A firing port passes a line of sight, not a model, so the access-opening requirement does not apply to it (`05-construction-components.md`, CMP-018). A roof hatch serving as both a firing port and an access point must satisfy that requirement in its access-point role only.

---

# TRN-012 — Transparent Elements

Transparent LEGO elements represent windows or viewports (`04-construction-standard.md`, SCS-009).

Passengers and attackers may interact through them if line of sight exists (`02-core-rules.md`, CORE-008).

---

# TRN-013 — Cargo

Cargo occupies Unit Bases, and unlike infantry it may share one.

A Unit Base divides into **slices**. A slice measures 4 × 3 studs by the height of the object standing in it, and the slices sharing one Unit Base may total no more than the Unit Base's height — see `02-core-rules.md` (CORE-001).

- An object **narrower** than 4 × 3 studs still takes a whole slice: the horizontal footprint is already spent, so sharing is only ever vertical.
- An object **wider or longer** than one Unit Base takes a slice of its own height in every Unit Base its footprint covers.

| Cargo | Footprint | Height |
|---|---|---|
| Ammo crate | 1 UB | 4 plate layers |
| Fuel drum pallet | 1 UB | 8 plate layers |
| Drone | 1 UB | 12 plate layers |
| Motorbike | 2 UB | 12 plate layers |
| Walker | 2 UB or more | 12 plate layers |

Footprints and heights are read from the model like every other measured value; the figures above are examples, not assignments.

Three ammo crates of 4 plate layers therefore share one Unit Base. A crate and a minifigure never share one: the minifigure occupies a whole Unit Base standing or seated (TRN-002), leaving no slice for the crate.

Cargo and passengers compete equally for transport space.

---

# TRN-014 — Crew Compartments

Crew members occupy their own Unit Bases.

Driver positions are separate from passenger compartments.

Crew space does not count as cargo capacity.

---

# TRN-015 — Emergency Exit

If one access point becomes unusable,

passengers may use any remaining functional access point.

If none remain,

the passengers are trapped.

---

# TRN-016 — Destroyed Access Points

Destroyed access points permanently alter the vehicle.

Examples:

- Blown-off door
- Jammed hatch
- Destroyed ramp

The LEGO model should represent these changes whenever possible.

---

# TRN-017 — Interior Design Matters

The internal layout of a transport affects gameplay.

Examples:

- Wide corridors improve deployment.
- Multiple exits improve flexibility.
- Benches reduce available cargo space.
- Large ramps simplify disembarkation.

Well-designed interiors provide tactical advantages.

---

# TRN-018 — Mobile Terrain

Transport vehicles are also terrain features.

Players interact with:

- Doors
- Windows
- Roofs
- Walls
- Hatches
- Ramps

Every structural element may become tactically relevant.

---

# TRN-019 — Interior Clearance

What must fit inside a vehicle is the Unit Base itself rather than the loose model (`02-core-rules.md`, CORE-001; `04-construction-standard.md`, SCS-005). A position offering less than one Unit Base of clear height is therefore a partial Unit Base (TRN-003), and holds no whole one.

Clearance is measured from the surface the model rests on — the floor, the deck or the bench, and for infantry the surface under its base rather than the top of it — upward to whatever is above it. That surface is the model's floor, not an obstruction: a bench 3 plate layers high needs one Unit Base of clear height *above the bench*. Seating raises the roof a compartment needs rather than shrinking its occupant — which is what TRN-017 already means by "benches reduce available cargo space".

Everything else physically in the way does count: a roof, a beam, a rack, a pipe. An element that reduces a compartment's usable volume is modifying Gameplay Geometry, not decorating it — see `15-geometry-layers.md` (GEO-002) — whatever it looks like.

- **Infantry and crew need one Unit Base of clear height.** An infantry model occupies exactly one Unit Base whether standing or seated (TRN-002), and a crew member occupies one like any other passenger (TRN-014). A compartment shorter than that carries neither.
- **Cargo needs only its own height.** Cargo divides a Unit Base (TRN-013), so a compartment 9 plate layers high carries cargo up to 9 plate layers — a partial Unit Base per position, in TRN-003's sense.

A low closed transport is therefore not an illegal model. It is a freight hull rather than a troop hull.

A position with no roof over it has nothing above to measure against, so no clearance applies there. Where an enclosure is incomplete enough that its occupants stay visible, the transport is open by TRN-009's own test, and its passengers are targetable, able to attack, and without the hull protection TRN-010 gives them. The builder pays in survivability rather than in a legality ruling.

**What this costs an existing model.** A closed compartment built under one Unit Base of clear height stops carrying infantry, and that includes a closed cockpit: a Pilot with no Unit Base is no Pilot, and a vehicle without a Pilot cannot move — see `08-vehicles.md` (VEH-013). Raising the roof by a plate or two, or opening it, is the whole repair.

---

# TRN-020 — Interior Levels

A vehicle may stack interior levels.

Each level needs one Unit Base of clear height above its own floor (`02-core-rules.md`, CORE-001), and each floor above the lowest costs what it measures — one plate at its thinnest.

| Levels | Height needed above the lowest interior floor |
|---|---|
| 1 | one Unit Base |
| 2 | two Unit Bases + 1 plate |
| 3 | three Unit Bases + 2 plates |

The lowest level rests on the vehicle's own hull and pays nothing for it — which is why an interior exactly two Unit Bases tall does not hold two levels. It is one plate short.

Each level is a cargo compartment like any other: its capacity is read from TRN-003 and its clearance from TRN-019.

How many levels a vehicle has room for is bounded by its own height rather than by this rule, and that height answers to two limits — its footprint and the agreed ceiling (`08-vehicles.md`, VEH-028).

---

# Summary

Transport in StudCraft follows these principles:

1. Everything occupies Unit Bases.
2. Infantry always occupies exactly 1 UB, and never shares it.
3. Transport capacity is the Unit Base volume available inside, and cargo may share a Unit Base.
4. A closed compartment shorter than one Unit Base of clear height carries cargo but no infantry, crew included.
5. Embarking costs 1 AP per occupied Unit Base.
6. Disembarking costs 1 AP per occupied Unit Base.
7. Open transports expose passengers.
8. Closed transports protect passengers.
9. Interior design is part of gameplay.

---

> **Every Brick Matters.**