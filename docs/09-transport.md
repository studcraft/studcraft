# StudCraft Transport System

**Version:** 0.1.0 Draft

---

# Purpose

This document defines how units embark, travel and disembark from transport vehicles.

StudCraft does not use abstract transport statistics.

Instead, transport capacity is determined by the number of **Unit Bases (UB)** available inside the vehicle.

This creates a unified system where deployment, movement and transport all use the same unit of measurement.

---

# Design Philosophy

Transport vehicles are mobile spaces.

Every transported object occupies physical space measured in Unit Bases.

The interior layout of a vehicle is therefore a meaningful design decision.

---

# TRN-001 — Unit Base Occupancy

Every transported object occupies one or more Unit Bases (UB).

One Unit Base measures:

**4 × 3 studs**

This represents the minimum operational space required by the object.

Examples:

- Infantry: 1 UB
- Supply crate: 1 UB
- Motorcycle: 1 UB
- Light Walker: 2 UB
- Heavy Walker: Defined by its footprint

---

# TRN-002 — Infantry Occupancy

Every infantry model always occupies:

**1 Unit Base**

This includes:

- The minifigure
- Its weapons
- Equipment
- Backpack
- Shield
- Accessories

Whether standing or seated, the infantry model continues to occupy exactly one Unit Base.

Changing posture never changes transport capacity.

---

# TRN-003 — Cargo Capacity

A transport vehicle's capacity equals the number of complete Unit Bases available inside its cargo compartment.

Example:

Cargo bay:

2 × 4 UB

Capacity:

8 UB

Possible loads:

- 8 infantry
- 6 infantry + 2 cargo crates
- 4 infantry + 1 light walker (2 UB)
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

Embarking costs:

**1 Action Point**

Requirements:

- The unit must be adjacent to a functional access point.
- The access point must be open.
- A free Unit Base must exist inside the transport.

The model is then physically placed inside one available Unit Base.

---

# TRN-006 — Disembarking

Disembarking costs:

**1 Action Point per Unit Base**

An infantry model (1 UB) therefore costs:

**1 AP**

The unit must be placed adjacent to a functional access point.

If there is insufficient space outside the vehicle, the unit cannot disembark.

---

# TRN-007 — Access Points

Only functional access points may be used.

Examples:

- Doors
- Rear ramps
- Side hatches
- Roof hatches

Decorative access points have no gameplay effect.

---

# TRN-008 — Opening and Closing

Opening or closing any access point costs:

**1 Action Point**

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
- Require normal line of sight.

Fundamental Rule:

> If you can see it, you can shoot it.

---

# TRN-010 — Closed Transport

A transport is considered closed when passengers are completely enclosed.

Passengers inside:

- Cannot be targeted directly.
- Cannot attack unless firing through an opening.

Protection comes from the vehicle's construction.

No additional armour value is required.

---

# TRN-011 — Firing Ports

A transport may include:

- Windows
- Gun ports
- Roof hatches
- Observation slits

Only passengers with physical line of sight through these openings may attack.

The opening determines the firing arc.

---

# TRN-012 — Transparent Elements

Transparent LEGO elements represent windows or viewports.

Visibility through transparent elements follows the Material Rules.

Passengers and attackers may interact through them if line of sight exists.

---

# TRN-013 — Cargo

Cargo occupies Unit Bases exactly like infantry.

Examples:

Ammo crate

1 UB

Fuel drum pallet

1 UB

Drone

1 UB

Motorbike

1 UB

Walker

Multiple UB

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

# Summary

Transport in StudCraft follows these principles:

1. Everything occupies Unit Bases.
2. Infantry always occupies exactly 1 UB.
3. Transport capacity equals the number of available Unit Bases.
4. Embarking costs 1 AP.
5. Disembarking costs 1 AP per occupied Unit Base.
6. Open transports expose passengers.
7. Closed transports protect passengers.
8. Interior design is part of gameplay.

---

> **Every Brick Matters.**