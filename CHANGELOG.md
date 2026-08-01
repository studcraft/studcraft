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

---

# [0.2.0] - 2026-08-01

- Add GitHub Pages site via Actions (docs/ stays untouched) (#1)
- Fix Gemfile.lock: bump pinned Bundler to 2.5.6 (#2)
- Apply just-the-docs default layout to all pages (#3)
- Split AGENTS.md into system/ docs and enforce mandatory git workflow (#4)
- Add OpenSpec tooling: opsx commands, skills, and prompt files (#5)
- Decouple version bumps from PR merges + automate release-cut (#6)
- Add structural linter for docs/*.md ruleset (#8)
- Add repository-strategy.md: block force-push and history rewrites (#9)
- Move bump declaration from CHANGELOG.md to commit messages (#10)
- Decouple archiving from a proposal's applying PR (#12)
- Weapon construction system: geometry-driven Range/Attack Dice/Impact Strength (#7)
- Geometry layers: formalize Gameplay Geometry vs Visual Geometry (#11)
- Enforce archive/apply separation with a CI gate (#13)
- Component damage system: geometry-driven damage resolution (#14)
- Remove paths filter from docs-ruleset-linter trigger (#16)
- Archive component-damage-system change (#15)
- Batch archiving instead of one PR per merged proposal (#17)
- Consolidate this session's lessons into system/ docs (#18)
- Consolidate Unit Base and Action Point restatements to CORE-001/CORE-006 (#19)
- Ruleset consistency fixes: 11 findings from manual review (#20)
- Remove docs/13-materials.md; fold its two real mechanics into damage-system.md (#21)
- Simplify melee combat: delegate resolution to the standard combat system (#22)
- Apply melee review cleanup: 5 of 6 actionable comments (#23)
- Unify Combat Flow diagram for ranged and melee delivery methods (#24)
- Apply combat review cleanup: verify against current state, fix real gaps (#25)
- Split Combat Flow diagram by actual ownership, simplify CBT-008, fix Summary (#26)
- General consistency verification: unify diagrams, fix VEH-014 duplication (#27)
- Full audit repairs: 34 of 35 findings from delete-me-audit.md (#28)
- Audit round 2: fix all 24 findings from delete-me-audit-resut.md (#29)
- Align Impact Strength and Resistance units; remove minifig exception (#30)
- Apply editorial-reviews-cleanup: 10 of 15 items across three reviews (#31)
- Add editorial-reviews-followup proposal (not applied) (#32)
- Add movement-audit-repairs proposal (not applied) (#33)
- Add vehicle-terrain-thresholds proposal (not applied) (#34)
- Archive 16 changes and reconcile the living specs (#35)
- Archive gameplay-visual-geometry; refresh its delta first (#36)

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