# StudCraft Transport System

**Version:** 0.2.0 Draft

---

# Purpose

This document defines how units embark, travel and disembark from transport vehicles.

Transport capacity is measured entirely in **Unit Bases (UB)**.

---

# Design Philosophy

Transport vehicles are physical spaces.

Their capacity and layout are determined by their construction.

---

# TRN-001 — Unit Base Occupancy

Every transported object occupies one or more Unit Bases, except cargo, which may occupy a fraction of one (`TRN-013`).

See `02-core-rules.md` (CORE-001) for the Unit Base definition.

Examples:

- Infantry: 1 UB
- Motorcycle: 2 UB
- Walker: its footprint
- Cargo: its physical volume

---

# TRN-002 — Infantry Occupancy

Every infantry model occupies exactly **1 Unit Base**, including its weapons and equipment (`02-core-rules.md`, CORE-003).

Infantry never shares a Unit Base, regardless of posture.

---

# TRN-003 — Cargo Capacity

A transport's capacity is the Unit Base volume available inside its cargo compartment.

Count the Unit Bases available on the compartment floor and apply its clear height (`TRN-019`).

- Infantry occupies 1 UB and never shares it (`TRN-002`).
- Cargo may share a UB vertically (`TRN-013`).
- A load is legal when its occupied volume does not exceed the available capacity.

Example:

A cargo bay measuring `2 × 4 UB` with one Unit Base of clear height provides **8 UB** of capacity.

---

# TRN-004 — Interior Layout

The interior layout of a transport determines its available space.

Seats, benches, racks, lockers and other functional elements occupy physical space and may reduce capacity.

---

# TRN-005 — Embarking

Embarking costs **1 Action Point**.

The unit must:

- Be adjacent to a functional access point.
- Use an open access point.
- Fit inside the transport (`TRN-001`, `TRN-019`).

Place the unit inside the available transport space.

---

# TRN-006 — Disembarking

Disembarking costs **1 Action Point**.

The unit must be placed adjacent to a functional access point with enough space to stand there.

If no legal position is available, it cannot disembark.

---

# TRN-007 — Access Points

Only functional access points may be used.

An access point must physically pass the models that use it (`05-construction-components.md`, CMP-018).

Examples:

- Doors
- Rear ramps
- Side hatches
- Roof hatches

---

# TRN-008 — Opening and Closing

Opening or closing an access point costs **1 Action Point** (`02-core-rules.md`, CORE-007).

The component must physically move.

---

# TRN-009 — Open Transport

A transport is open when its passengers are physically visible.

Visible passengers:

- May be targeted.
- May attack.
- Follow normal line of sight rules (`02-core-rules.md`, CORE-008, CORE-009).

Examples:

- Jeep
- Truck
- Hover platform
- Open boat
- Flatbed vehicle

---

# TRN-010 — Closed Transport

A transport is closed when its passengers are completely enclosed.

Passengers inside:

- Cannot be targeted directly.
- Cannot attack unless they have physical line of sight through an opening.

The vehicle's construction protects its passengers according to the Component Damage System (`16-damage-system.md`).

---

# TRN-011 — Firing Ports

A transport may provide firing ports through:

- Windows
- Gun ports
- Roof hatches
- Observation slits

A passenger may attack through an opening only if it has physical line of sight to the target.

The opening determines the available firing arc.

A firing port does not need to pass a model (`05-construction-components.md`, CMP-018).

A component serving as both a firing port and an access point must satisfy CMP-018 in its access-point role.

---

# TRN-012 — Transparent Elements

Transparent LEGO elements may represent windows or viewports (`05-construction-components.md`, CMP-022).

They do not block line of sight when transparent (`02-core-rules.md`, CORE-008).

---

# TRN-013 — Cargo

Cargo occupies physical volume and may share a Unit Base vertically.

A Unit Base may be divided into slices according to cargo height. The total height of cargo sharing one Unit Base cannot exceed its 13 plate layers (`02-core-rules.md`, CORE-001).

Cargo narrower than `4 × 3` studs still occupies a full horizontal slice. Sharing is therefore vertical only.

Cargo covering multiple Unit Bases occupies the corresponding slice in each one.

Examples:

- A 4-plate crate occupies 4/13 UB.
- Three 4-plate crates fit in one UB.
- A 13-plate cargo object occupies one full UB.
- Infantry never shares a UB (`TRN-002`).

Cargo and passengers use the same available transport volume.

---

# TRN-014 — Crew Compartments

Crew members occupy their own Unit Bases.

A crew position is separate from passenger capacity.

A driver position therefore requires its own space in addition to cargo or passenger space.

---

# TRN-015 — Emergency Exit

If an access point becomes unusable, passengers may use any remaining functional access point.

If none remain, they cannot disembark.

---

# TRN-016 — Destroyed Access Points

A destroyed access point permanently changes the vehicle's available access.

Examples:

- Blown-off door
- Jammed hatch
- Destroyed ramp

The model should represent the change whenever possible.

---

# TRN-017 — Interior Design Matters

Interior construction affects transport capacity and operation.

Examples:

- Benches reduce available space.
- Wide corridors provide easier access.
- Multiple exits provide alternative access points.
- Large ramps provide access to larger models.

---

# TRN-018 — Mobile Terrain

Transport vehicles are battlefield terrain.

Their:

- Doors
- Windows
- Roofs
- Walls
- Hatches
- Ramps

may interact with units and movement according to the rules governing those elements.

---

# TRN-019 — Interior Clearance

A model fits inside a transport only if the Unit Base volume it occupies can physically fit within the available space (`02-core-rules.md`, CORE-001).

Measure clear height from the surface the model rests on to the obstruction above it.

- Infantry and crew require **1 UB** of clear height.
- Cargo requires only its own height (`TRN-013`).
- Benches, roofs, racks, beams and other elements reduce available space.
- An open position has no upper clearance requirement.

A compartment shorter than 1 UB of clear height cannot carry infantry or crew.

---

# TRN-020 — Interior Levels

A vehicle may have multiple interior levels.

Each level requires **1 Unit Base of clear height** above its own floor (`02-core-rules.md`, CORE-001).

Each floor above the lowest adds its own physical thickness.

| Levels | Minimum height above lowest floor |
|---|---:|
| 1 | 1 UB |
| 2 | 2 UB + 1 plate |
| 3 | 3 UB + 2 plates |

Each level has its own cargo capacity and clearance (`TRN-003`, `TRN-019`).

The number of levels a vehicle can contain is limited by its construction and maximum height (`08-vehicles.md`, VEH-028).

---

# Summary

Transport in StudCraft follows these principles:

1. Transport capacity is measured in Unit Bases.
2. Infantry occupies exactly 1 UB and never shares it.
3. Cargo may share a Unit Base vertically.
4. A model must physically fit inside its transport.
5. Embarking costs 1 AP.
6. Disembarking costs 1 AP.
7. Open transports expose passengers.
8. Closed transports protect passengers according to their construction.
9. Interior construction determines available capacity and access.

---

> **Every Brick Matters.**