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

StudCraft measures army size using physical space instead of abstract points.

Every vehicle and infantry model occupies physical space. The floor area occupied by a model determines how much Deployment Volume floor space is required to deploy it.

Vehicle height is not determined by its footprint.

The Deployment Volume defines both the available floor area and the maximum deployment height. A model may be deployed if its physical geometry fits within the agreed Deployment Volume.

Wider models consume more floor space. Taller models require sufficient vertical clearance.

Balance emerges from the physical space available rather than from points or army lists.

---

# DEP-001 — Deployment Volume

Before the game begins, players agree on a **Deployment Volume**.

A Deployment Volume is measured in **Unit Bases (UB)** (`02-core-rules.md`, CORE-001) and written `W × D × H`.

* `W × D` is the available floor area, counted in Unit Bases.
* `H` is the maximum deployment height in Unit Bases.

If only two dimensions are given, the Deployment Volume is **1 UB high**.

A `5 × 1` floor and a `1 × 5` floor both contain five Unit Bases.

Deployment Volumes may have any dimensions agreed upon by the players or defined by the scenario.

> **If it fits, it deploys.**

---

# DEP-002 — Army Capacity

A player's army is any combination of models that can be physically placed within the agreed Deployment Volume.

Every model must fit within the Deployment Volume's floor and beneath its ceiling. Models cannot overlap. A model occupies whole Unit Bases: a footprint covering part of one covers all of it.

The player chooses which models to deploy. No points or other army-capacity system is used.

The physical placement of the models is the final check. A combination is legal if all models can be placed within the Deployment Volume at the same time.

---

# DEP-003 — Vehicle Footprint

A vehicle occupies every Unit Base covered by its footprint.

The footprint determines the vehicle's horizontal Deployment Volume occupation.

Example:

Vehicle dimensions:

`2 × 5 UB`

Deployment occupation:

`10 Unit Bases`

Those Unit Bases are occupied and cannot be occupied by another model.

Vehicle height is checked separately against the Deployment Volume ceiling.

---

# DEP-004 — Infantry

Each infantry model occupies 1 Unit Base (`02-core-rules.md`, CORE-003).

When deployed individually, this UB counts against the Deployment Volume floor.

When embarked inside a transport, the infantry model occupies the transport's interior space and does not consume additional Deployment Volume floor space (`DEP-006`).

---

# DEP-005 — Transport Capacity

Transport capacity is not purchased.

It is determined entirely by the physical cargo compartment.

If a Unit Base fits inside the vehicle, a minifigure may be transported in it (`09-transport.md`, TRN-019).

If it does not fit, it cannot.

> **The LEGO model is the source of truth.**

---

# DEP-006 — Embarked Units

Embarked units are considered part of the transport during deployment.

Their occupied space is the transport interior, not additional Deployment Volume floor space.

This represents one of the main strategic advantages of transport vehicles.

Example:

A transport occupies:

`2 × 5 UB`

It physically carries:

8 infantry.

Deployment occupation:

Only the transport footprint.

The infantry do not consume additional Deployment Volume floor space while embarked.

The waiver applies only to embarked units. A model carried on the outside — on a roof, bonnet, hull top or outside of a turret — is not embarked.

An externally carried infantry model is therefore deployed individually and occupies 1 Unit Base of Deployment Volume floor space (`DEP-004`).

An externally carried vehicle is deployed according to its own footprint (`DEP-003`).

Externally carried models also form part of the physical model for deployment-height purposes and must fit beneath the Deployment Volume ceiling (`08-vehicles.md`, VEH-030).

---

# DEP-007 — Embarking, Disembarking and Transport State

Embarking, disembarking, access points, and open/closed transport rules are defined in `09-transport.md`.

Deployment only determines how much battlefield space a transport and its embarked units consume before the game begins.

See `DEP-005` and `DEP-006`.

---

# DEP-008 — Mixed Forces

Players may freely combine infantry, vehicles and transports within their Deployment Volume.

For example, a `5 × 4 × 2 UB` Deployment Volume may contain:

* **20 infantry**, filling the floor.
* **2 tanks and 8 infantry**, if their footprints can be placed within the floor and all models fit beneath the ceiling.
* **1 super-heavy transport carrying 2 walkers and 4 infantry**, provided the transport and its contents satisfy the applicable transport rules and the complete deployed model fits within the Deployment Volume.

These are examples only.

Any combination is legal if all models can be physically placed within the Deployment Volume at the same time.

---

# DEP-009 — Scenario Scaling

StudCraft naturally supports multiple game sizes.

Examples:

## Patrol

Deployment Volume:

`5 × 1 × 2 UB`

Fast introductory games.

---

## Skirmish

Deployment Volume:

`5 × 5 × 4 UB`

Small tactical engagements.

---

## Battle

Deployment Volume:

`10 × 10 × 6 UB`

Combined-arms battles.

---

## Massive Battle

Any agreed Deployment Volume.

No upper limit exists.

---

# Design Notes

StudCraft intentionally replaces army points with physical space.

Wider models consume more floor space, while taller models require sufficient vertical clearance within the agreed Deployment Volume.

Large vehicles gain transport capacity, survivability and firepower naturally through their physical construction.

Small forces gain flexibility and numbers.

Balance emerges from construction and physical deployment space rather than from points values.

---

# Summary

Deployment follows four principles:

1. Army size is measured using Unit Bases.
2. Vehicles consume floor space according to their footprint.
3. A model's height is checked against the Deployment Volume ceiling.
4. Transport capacity depends on physical interior space, and embarked units do not consume additional Deployment Volume floor space.

Embarking, disembarking and access point rules are defined in `09-transport.md`.

---

> **Every Brick Matters.**
