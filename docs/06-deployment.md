# StudCraft Deployment Rules

**Version:** 0.2.0 Draft

---

# Purpose

This document defines how armies are built and deployed in StudCraft.

Unlike traditional tabletop games, StudCraft does not use points values.

Instead, armies are limited by the physical space they occupy.

The battlefield determines the size of the game.

---

# Design Philosophy

StudCraft measures army size using physical volume instead of abstract points.

Every vehicle and infantry model occupies space; a scenario-placed structure's Deployment Volume occupation is not yet defined (`02-core-rules.md`, CORE-005).

The floor that space covers becomes the cost of including the model. Its height is not charged: how tall a model may be is a ceiling both players agreed to (DEP-001), not a price one of them pays.

Wider models provide greater capabilities but consume more deployment capacity.

---

# DEP-001 — Deployment Volume

Before the game begins, players agree on a Deployment Volume.

A Deployment Volume is measured in **Unit Bases (UB)** — see `02-core-rules.md` (CORE-001) for the Unit Base definition — and is written `W × D × H`: a floor `W × D`, and the height `H` every model in a player's army must fit under.

Where only two numbers are agreed, the ceiling is one Unit Base. That is also the lowest a Deployment Volume can be: infantry occupies exactly one Unit Base (`02-core-rules.md`, CORE-003), so a shorter one admits no army at all.

A one-Unit-Base ceiling is an infantry game, and deliberately so. A powered vehicle carries a Pilot occupying a Unit Base of its own (`02-core-rules.md`, CORE-003; `08-vehicles.md`, VEH-013), and that Unit Base rests on a floor which rests on the vehicle's locomotion — all of it height, before any hull exists. A closed cockpit needs the clearance above it as well (`09-transport.md`, TRN-019). Players who want vehicles agree a taller volume.

Deployment Volumes may have any dimensions agreed upon by the players, subject only to the one Unit Base of height an army needs to exist in.

`H` is agreed in whole Unit Bases. A model's own height is measured as its rule measures it — a vehicle's in plate layers (`08-vehicles.md`, VEH-030) — so a hull 22 plate layers tall fits a ceiling of two Unit Bases with room to spare.

Examples:

- 4 × 4 UB — two numbers, so one Unit Base tall: infantry only
- 5 × 5 × 4 UB
- 10 × 10 × 6 UB
- Scenario-defined volumes

A low ceiling is a scenario choice rather than an oversight. Tunnels, hangars, cargo holds and fights inside a hull are agreed here, by choosing a smaller `H`, and need no rule of their own.

---

# DEP-002 — Army Capacity

A player's army may occupy any combination of models that fits inside the agreed Deployment Volume — on its floor and under its ceiling. An infantry model's height is its Unit Base, weapons and equipment included (`02-core-rules.md`, CORE-001; `09-transport.md`, TRN-002). A vehicle's is what `08-vehicles.md`, VEH-028 measures: from the surface it rests on to the top of its Gameplay Geometry.

No additional points system exists.

Examples:

A 5 × 5 × 4 UB Deployment Volume could contain:

- 25 infantry.

or

- 1 large tank.

or

- 2 medium vehicles.

or

- 1 transport carrying infantry.

Any legal combination is allowed provided it fits, read that way.

---

# DEP-003 — Vehicle Footprint

A vehicle occupies every Unit Base covered by its footprint.

Example:

Vehicle dimensions:

2 × 5 UB

Deployment cost:

10 Unit Bases.

This area is unavailable for any other model.

The footprint is what this rule charges, and it bounds nothing else. How tall a vehicle may build is settled by the ceiling of the agreed Deployment Volume (DEP-001; `08-vehicles.md`, VEH-028), not by the space it covers.

---

# DEP-004 — Infantry

Each infantry model occupies 1 Unit Base (`02-core-rules.md`, CORE-003). Deployed individually, this UB counts against the Deployment Volume; already embarked inside a transport, it counts only against the transport's own interior UB (DEP-006) — not as additional Deployment Volume.

---

# DEP-005 — Transport Capacity

Transport capacity is not purchased.

It is determined entirely by the physical cargo compartment.

If a Unit Base fits inside the vehicle, a minifigure may be transported in it (`02-core-rules.md`, CORE-001; `09-transport.md`, TRN-019).

If it does not fit, it cannot.

The LEGO model is the source of truth.

---

# DEP-006 — Embarked Units

Embarked units are considered part of the transport during deployment.

Their occupied space is the transport interior, not additional Deployment Volume.

This represents one of the main strategic advantages of transport vehicles.

Example:

A transport occupies:

2 × 5 UB

It physically carries:

8 infantry.

Deployment Cost:

Only the transport footprint.

The infantry do not consume additional Deployment Volume while embarked.

The waiver is for **embarked** units. A model carried on the outside — on a roof, a bonnet, a hull top or the outside of a turret — is not embarked, so it is deployed individually and costs Deployment Volume of its own: one Unit Base for an infantry model (DEP-004), its own footprint for a vehicle (DEP-003). Embarking means occupying a constructed interior space measured in Unit Bases (`09-transport.md`, TRN-001), and an externally carried model counts toward the carrier's height as well (`08-vehicles.md`, VEH-030).

---

# DEP-007 — Embarking, Disembarking and Transport State

Embarking, disembarking, access points, and open/closed transport rules are defined in `09-transport.md`.

Deployment only determines how much battlefield space a transport (and its embarked units) consumes before the game begins. See DEP-005 and DEP-006.

---

# DEP-008 — Mixed Forces

Players are free to mix infantry, vehicles and transports.

Examples:

Force A

- 20 infantry.

Force B

- 2 tanks.
- 8 infantry.

Force C

- 1 super-heavy transport.
- 2 walkers inside.
- 4 infantry.

As long as the Deployment Volume is respected, all armies are legal.

---

# DEP-009 — Scenario Scaling

StudCraft naturally supports multiple game sizes.

Suggested examples:

## Patrol

Deployment Volume:

5 × 1 × 2 UB

Fast introductory games.

---

## Skirmish

Deployment Volume:

5 × 5 × 4 UB

Small tactical engagements.

---

## Battle

Deployment Volume:

10 × 10 × 6 UB

Combined-arms battles.

---

## Massive Battle

Any agreed Deployment Volume.

No upper limit exists.

---

# Design Notes

StudCraft intentionally replaces army points with physical space.

Players pay for wider units by sacrificing floor space, and for taller ones by having to agree a Deployment Volume that admits them.

Large vehicles gain transport capacity, survivability and firepower naturally.

Small forces gain flexibility and numbers.

Balance emerges from construction rather than army lists.

---

# Summary

Deployment follows four principles:

1. Army size is measured in Unit Bases.
2. Vehicles consume floor space according to their footprint, and must fit under the agreed ceiling.
3. Transport capacity depends on physical interior volume.
4. Embarked units do not consume additional Deployment Volume.

Embarking, disembarking and access point rules are defined in `09-transport.md`.

---

> **Every Brick Matters.**