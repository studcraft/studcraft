# StudCraft Foundations

**Version:** 0.1.0 Draft

---

# Purpose

This document introduces the fundamental concepts of StudCraft.

It defines the language used throughout the rulebook and explains the design philosophy behind the game.

Every player should read this document before reading the detailed rules.

---

# What is StudCraft?

StudCraft is a construction-driven tabletop wargame.

Instead of predefined unit profiles, the physical LEGO model defines how a unit behaves.

Every meaningful gameplay characteristic should be visible in the model itself.

The goal is to create a game where building and playing are part of the same experience.

---

# The Core Philosophy

StudCraft is built around one central principle:

> **The Model Is The Rules.**

Players should be able to understand how a model behaves simply by looking at its construction.

Examples include:

- Weapon length defines range.
- Weapon muzzles define attack dice.
- Vehicle size defines movement.
- Cargo space defines transport capacity.
- Visible openings define lines of fire.

Whenever possible, construction replaces abstraction.

---

# Every Brick Matters

Every LEGO element should contribute to gameplay.

A brick may represent:

- Structure
- Armour
- Pilot
- Weapon
- Door
- Window
- Cargo space
- Wheel
- Track
- Interior layout

Decoration is encouraged, but functional construction is the heart of StudCraft.

---

# Unit Base (UB)

The Unit Base (UB) is the universal measurement used throughout the game.

One Unit Base measures:

**4 × 3 studs**

(see `02-core-rules.md`, CORE-001, for the canonical definition)

Everything in StudCraft is ultimately measured using Unit Bases.

Examples:

- Infantry occupies 1 UB.
- Deployment areas are measured in UB.
- Vehicle footprints are measured in UB.
- Transport capacity is measured in UB.
- Cargo occupies UB.

Using a single measurement system keeps the rules simple and consistent.

---

# Action Points (AP)

Every unit activates using the same action economy.

Each activated unit receives:

**3 Action Points (AP)**

(see `02-core-rules.md`, CORE-006, for the canonical definition)

Action Points are spent to perform actions such as:

- Move
- Rotate
- Attack
- Open doors
- Close doors
- Embark
- Disembark

The same resource is shared across every unit type.

---

# Components

StudCraft treats models as collections of physical components.

Examples include:

- Pilot
- Weapons
- Wheels
- Tracks
- Doors
- Windows
- Turrets

Components are meaningful game elements.

They may be targeted, damaged and interact with other rules.

---

# Impacts

Weapons do not directly cause damage.

Instead, successful attacks generate **Impacts**.

The target resolves those Impacts according to its construction (`16-damage-system.md`).

This separates the attack from its physical effect, keeping weapon rules simple while allowing targets to resolve consequences independently.

---

# Physical Representation

Whenever possible, the LEGO model itself represents the current game state.

Examples:

- A wounded minifigure sits down.
- A dead minifigure is removed.
- A destroyed door is removed.
- A broken window is detached.
- A disabled weapon is taken off the model.

StudCraft minimizes the use of tokens and external markers.

---

# Universal Systems

StudCraft is intentionally built around a small number of universal systems.

These systems are reused throughout the rulebook:

- Unit Bases (UB)
- Action Points (AP)
- Components
- Impacts

Whenever a new rule is introduced, it should build upon these systems instead of creating new ones.

---

# Modularity

Each rule document has a single responsibility.

Examples:

- Movement defines how units move.
- Weapons define how attacks are generated.
- Combat resolves attacks.
- The Component Damage System determines the effects of impacts.
- Transport defines passenger capacity.

This modular structure keeps the game easy to expand and maintain.

---

# Learning StudCraft

See `README.md`'s Rulebook section for the recommended reading order — it
introduces each system only after its prerequisites have been explained,
and is the single place that list is maintained.

---

# Summary

StudCraft is built on a simple idea:

The LEGO model is not an illustration of the rules.

It **is** the rules.

By using a small number of universal systems and expressing gameplay through physical construction, StudCraft creates a game where building and playing become one continuous experience.

---

> **The Model Is The Rules.**

> **Every Brick Matters.**