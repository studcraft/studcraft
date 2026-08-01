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

Every vehicle and infantry model occupies space; a scenario-placed structure's Deployment Area occupation is not yet defined (`02-core-rules.md`, CORE-005).

That occupied space becomes the cost of including the model.

Larger models provide greater capabilities but consume more deployment capacity.

---

# DEP-001 — Deployment Area

Before the game begins, players agree on a Deployment Area.

A Deployment Area is measured in **Unit Bases (UB)** — see `02-core-rules.md` (CORE-001) for the Unit Base definition (4 × 3 studs).

Deployment Areas may have any dimensions agreed upon by the players.

Examples:

- 5 × 1 UB
- 5 × 5 UB
- 10 × 10 UB
- Scenario-defined areas

---

# DEP-002 — Army Capacity

A player's army may occupy any combination of models that physically fits inside the agreed Deployment Area.

No additional points system exists.

Examples:

A 5 × 5 UB Deployment Area could contain:

- 25 infantry.

or

- 1 large tank.

or

- 2 medium vehicles.

or

- 1 transport carrying infantry.

Any legal combination is allowed provided it physically fits.

---

# DEP-003 — Vehicle Footprint

A vehicle occupies every Unit Base covered by its footprint.

Example:

Vehicle dimensions:

2 × 5 UB

Deployment cost:

10 Unit Bases.

This area is unavailable for any other model.

---

# DEP-004 — Infantry

Each infantry model occupies 1 Unit Base (`02-core-rules.md`, CORE-003). Deployed individually, this UB counts against the Deployment Area; already embarked inside a transport, it counts only against the transport's own interior UB (DEP-006) — not as additional Deployment Area.

---

# DEP-005 — Transport Capacity

Transport capacity is not purchased.

It is determined entirely by the physical cargo compartment.

If a minifigure physically fits inside the vehicle, it may be transported.

If it does not fit, it cannot.

The LEGO model is the source of truth.

---

# DEP-006 — Embarked Units

Embarked units are considered part of the transport during deployment.

Their occupied space is the transport interior, not additional Deployment Area.

This represents one of the main strategic advantages of transport vehicles.

Example:

A transport occupies:

2 × 5 UB

It physically carries:

8 infantry.

Deployment Cost:

Only the transport footprint.

The infantry do not consume additional Deployment Area while embarked.

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

As long as the Deployment Area is respected, all armies are legal.

---

# DEP-009 — Scenario Scaling

StudCraft naturally supports multiple game sizes.

Suggested examples:

## Patrol

Deployment Area:

5 × 1 UB

Fast introductory games.

---

## Skirmish

Deployment Area:

5 × 5 UB

Small tactical engagements.

---

## Battle

Deployment Area:

10 × 10 UB

Combined-arms battles.

---

## Massive Battle

Any agreed Deployment Area.

No upper limit exists.

---

# Design Notes

StudCraft intentionally replaces army points with physical space.

Players pay for larger units by sacrificing deployment capacity.

Large vehicles gain transport capacity, survivability and firepower naturally.

Small forces gain flexibility and numbers.

Balance emerges from construction rather than army lists.

---

# Summary

Deployment follows four principles:

1. Army size is measured in Unit Bases.
2. Vehicles consume space according to their footprint.
3. Transport capacity depends on physical interior volume.
4. Embarked units do not consume additional Deployment Area.

Embarking, disembarking and access point rules are defined in `09-transport.md`.

---

> **Every Brick Matters.**