# StudCraft

> **The Model Is The Rules.**
>
> **Every Brick Matters.**

StudCraft is a construction-driven tabletop wargame built with LEGO® bricks.

Unlike traditional miniature games, StudCraft does not rely on predefined unit profiles, hidden statistics or fixed army lists.

Instead, the physical LEGO model defines how a unit behaves.

If you can build it, you can play it.

---

# Vision

StudCraft combines building and tabletop gaming into a single experience.

Every meaningful gameplay element should be represented by the model itself.

Examples include:

- Weapon length determines range.
- Weapon muzzles determine attack dice.
- Vehicle size determines movement.
- Interior space determines transport capacity.
- Physical components determine what can be targeted.

The goal is simple:

> **The model should explain the rules.**

---

# Design Principles

StudCraft is built around a small set of universal principles.

- The Model Is The Rules
- Every Brick Matters
- Construction Over Abstraction
- Components Over Statistics
- Impacts Over Damage
- Physical State Over Tokens
- One Universal Measurement (Unit Base)
- One Universal Action Economy (Action Points)

These principles are fully described in:

`CODE_OF_DESIGN.md`

---

# Repository Structure

```
/
├── README.md
├── CODE_OF_DESIGN.md
├── CONTRIBUTING.md
├── CHANGELOG.md
├── LICENSE
├── AGENTS.md
│
└── docs/
    ├── 01-foundations.md
    ├── 02-core-rules.md
    ├── 03-game-flow.md
    ├── 04-construction-standard.md
    ├── 05-construction-components.md
    ├── 06-deployment.md
    ├── 07-movement.md
    ├── 08-vehicles.md
    ├── 09-transport.md
    ├── 10-weapons.md
    ├── 11-combat.md
    ├── 12-melee.md
    ├── 14-glossary.md
    ├── 15-geometry-layers.md
    └── 16-damage-system.md
```

`13-*.md` is a deliberate gap, not a missing file — `docs/13-materials.md` was removed (its content folded into `16-damage-system.md`), and per this repo's rule-ID-stability convention, document numbers are not reused or renumbered after removal.

---

# Rulebook

The recommended reading order is:

## Part I — Foundations

1. `01-foundations.md`
2. `02-core-rules.md`
3. `03-game-flow.md`
4. `15-geometry-layers.md`

These documents explain the game's philosophy and core systems, including how to read what part of a model matters (Gameplay Geometry) versus what's purely visual.

---

## Part II — Construction

5. `04-construction-standard.md`
6. `05-construction-components.md`

Learn how legal models are built.

---

## Part III — Deployment & Movement

7. `06-deployment.md`
8. `07-movement.md`
9. `08-vehicles.md`
10. `09-transport.md`

Learn how armies are deployed and how units move across the battlefield.

---

## Part IV — Combat

11. `10-weapons.md`
12. `11-combat.md`
13. `12-melee.md`
14. `16-damage-system.md`

Learn how attacks are generated and resolved, and how components take and resist damage.

---

## Reference

15. `14-glossary.md`

Quick lookup for core terms.

---

# Core Concepts

StudCraft is intentionally built around a small number of universal systems.

## Unit Base (UB)

The universal measurement of the game.

One Unit Base is a volume:

**4 studs wide × 3 studs deep × 12 plate layers tall**

— defined by `docs/02-core-rules.md` (CORE-001), which is the authority on its dimensions, its orientation and which projection a rule reads.

Everything is measured using Unit Bases.

---

## Action Points (AP)

Every activated unit receives:

**3 Action Points**

Movement, combat and interactions all consume AP.

---

## Components

Models are collections of functional components.

Examples:

- Pilot
- Wheel
- Weapon
- Door
- Window
- Track

Destroying components changes gameplay.

---

## Impacts

Weapons do not inflict damage.

Weapons generate **Impacts**.

Targets resolve those Impacts according to their construction (`16-damage-system.md`).

---

# Current Status

Current development stage:

**Version 0.1**

Implemented systems:

- Core Rules
- Construction
- Deployment
- Movement
- Vehicles
- Transport
- Weapons
- Combat
- Melee
- Game Flow
- Geometry Layers
- Damage System

The project is ready for its first full playtests.

---

# Contributing

Contributions are welcome.

Before submitting changes, please read:

- `CODE_OF_DESIGN.md`
- `CONTRIBUTING.md`
- `AGENTS.md`

StudCraft values consistency over complexity.

Whenever possible:

> Build the solution instead of writing a new rule.

---

# AI Collaboration

StudCraft is designed to be developed collaboratively by humans and AI agents.

AI contributors should follow the instructions described in:

`AGENTS.md`

Design discussions and future proposals may be tracked separately using OpenSpec.

---

# Disclaimer

StudCraft is an independent fan-made project.

It is **not affiliated with, endorsed by or sponsored by the LEGO Group**.

LEGO® is a trademark of the LEGO Group.

---

# License

This project is released under the MIT License.

See `LICENSE` for details.

---

> **The Model Is The Rules.**

> **Every Brick Matters.**