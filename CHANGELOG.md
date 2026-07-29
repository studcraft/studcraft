# Changelog

All notable changes to StudCraft are documented in this file.

The project follows Semantic Versioning.

Version format:

MAJOR.MINOR.PATCH

Example:

0.1.0

This file is written only by the `Release cut` workflow — no PR should
edit it by hand, ever. Nothing needs to be declared to get a release:
any `docs/*.md` change since the last release tag defaults to a minor
bump automatically. See `system/workflow.md` for why, and for the
optional escape hatches if a change is actually breaking.

---

# [Unreleased]

## Weapon Construction System

Reworked `docs/10-weapons.md` so every offensive property is derived from
geometry instead of fixed parts:

- Functional muzzles are now square (1×1 through 4×4) instead of a fixed
  round 1×1 piece (WPN-002). Muzzle size determines a new Impact
  Strength value (WPN-021).
- Weapon Length is now the longest dimension of the functional Weapon
  Body, excluding decorative elements (WPN-003) — replaces the previous
  "rear of body to foremost muzzle" measurement.
- **BREAKING**: Removed the mandatory 1-stud muzzle separation rule.
  Muzzles may now be placed directly adjacent, as long as they don't
  overlap (WPN-007, WPN-020).
- Added the Weapon Front Footprint and Muzzle Placement rules governing
  how a weapon's front face is partitioned into muzzles (WPN-019,
  WPN-020).
- Added the Weapon Proportion constraint, `Length ≥ 2 × Width` (WPN-018).
- Generalized the single-weapon maximum length rule into a Weapon
  Capacity constraint, `Σ(Weapon Length) ≤ Platform Length` (WPN-004).
- Added glossary entries for Weapon Body, Weapon Front, Weapon Front
  Footprint, Muzzle Size, Impact Strength, Weapon Capacity, and Platform
  Length.

**Bump:** major

---

# [0.1.0] - Initial Core Rule Set

## Added

### Core Philosophy

- Introduced "The Model Is The Rules".
- Introduced "Every Brick Matters".
- Established the Unit Base (UB) as the universal measurement.
- Established Action Points (AP) as the universal action economy.

---

### Core Rules

Added the initial game framework.

Documents:

- 01-foundations.md
- 02-core-rules.md
- 03-game-flow.md
- 14-glossary.md

---

### Construction

Defined:

- Vehicle construction
- Functional components
- Unit Bases
- Physical validation principles

---

### Deployment

Introduced physical-space-based army building.

Added:

- Deployment Area
- Army Capacity
- Vehicle Footprint cost
- Mixed Forces
- Scenario Scaling

---

### Movement

Added movement rules for:

- Infantry
- Wheeled vehicles
- Tracked vehicles
- Walkers
- Hover vehicles

Vehicle movement is based on:

- Physical model length
- Locomotion type

Diagonal movement removed.

---

### Combat

Introduced the Impact System.

Weapons no longer have:

- Damage
- Strength
- Armour Penetration

Weapons now define only:

- Range
- Attack Dice
- Firing Position

---

### Weapons

Weapon rules are now entirely construction-driven.

Added:

- Weapon Length
- Functional Muzzles
- Range calculation
- Attack Dice generation

---

### Materials

Introduced Material Responses.

Added support for:

- Glass
- Infantry
- Metal
- Stone
- Wood
- Organic materials

---

### Vehicles

Vehicles are now treated as collections of components.

Removed the concept of vehicle Hit Points.

Added:

- Engine
- Wheels
- Tracks
- Turrets
- Doors
- Windows

---

### Transport

Introduced Unit Base transport capacity.

Transport capacity is now determined by interior Unit Bases instead of abstract statistics.

Added:

- Open transports
- Closed transports
- Access points
- Embarkation
- Disembarkation

---

### Melee

Added hand-to-hand combat.

Introduced:

- Simultaneous combat
- Contact requirement
- Shared Impact System

---

### Game Flow

Introduced alternating unit activation.

Added:

- Priority
- 3 Action Points per activation
- Universal activation system

---

### Documentation

Created:

README.md

CODE_OF_DESIGN.md

CONTRIBUTING.md

CHANGELOG.md

AGENTS.md

---

# Future Versions

Future releases will continue following Semantic Versioning.

Example:

0.2.0

Added:

Equipment

Terrain

Visibility

Building Rules

Scenario System

0.3.0

Advanced Vehicles

Campaign Rules

Reaction System

Model Validation

1.0.0

First Stable Release

Complete Core Rulebook

Public Playtest Complete

---

> Every Brick Matters.