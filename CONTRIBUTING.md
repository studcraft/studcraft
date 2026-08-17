# Contributing to StudCraft

First of all, thank you for your interest in contributing to StudCraft.

StudCraft is an open design project whose goal is to create a tabletop wargame where **the LEGO model is the rules**.

Every contribution, whether it is a rule, a scenario, a vehicle, or a documentation improvement, helps the project grow.

Before contributing, please read:

- `README.md`
- `CODE_OF_DESIGN.md`

These documents define the philosophy that every contribution must follow.

---

# Design First

StudCraft is not a collection of isolated rules.

It is a coherent design system.

When proposing a change, always ask:

> **Does this reinforce "The Model Is The Rules"?**

If the answer is no, reconsider the proposal.

---

# Guiding Principles

Every contribution should respect these principles:

- The model is the rules.
- Every Brick Matters.
- Construction over abstraction.
- Components over statistics.
- Impacts over damage.
- Physical state over tokens.
- Simplicity before complexity.
- Modular design.

These principles are described in detail in `CODE_OF_DESIGN.md`.

---

# What Can Be Contributed?

Contributions are welcome in many areas.

Examples include:

## Rules

- New mechanics
- Rule clarifications
- Balancing improvements
- Optional rules

---

## Construction Standards

- New functional components
- Building standards
- Validation rules

---

## Scenarios

- Missions
- Campaigns
- Objective systems

---

## Terrain

- Buildings
- Roads
- Bridges
- Obstacles
- Environmental effects

---

## Vehicles

- Construction examples
- Interior layouts
- Component ideas

---

## Documentation

- Corrections
- Better explanations
- Diagrams
- Examples
- Translations

---

# Before Creating a New Rule

Ask yourself:

- Can this already be represented using existing rules?
- Can this be solved by construction instead?
- Is this introducing unnecessary complexity?
- Is this reusable?
- Is it intuitive?

The simplest solution is usually the best one.

Check [`TODO.md`](TODO.md) too: if the ruleset already declares your gap, the entry quotes the rule that declares it, and closing it means editing that rule rather than adding one beside it.

---

# Rule Design Checklist

A proposed rule should:

- Have a single responsibility.
- Reuse existing systems whenever possible.
- Avoid creating exceptions.
- Be easy to explain.
- Be easy to remember.
- Be physically represented whenever possible.

---

# Writing Style

Documentation should be:

- Clear
- Concise
- Modular
- Consistent

Avoid ambiguous language.

Whenever possible:

Use:

> "A vehicle moves 1.5 times its own length."

Instead of:

> "Vehicles generally move a considerable distance."

Rules should be precise.

---

# Repository Structure

Please keep new documents organized.

```
docs/

01-foundations.md

02-core-rules.md

03-game-flow.md

05-construction-components.md

06-deployment.md

07-movement.md

08-vehicles.md

09-transport.md

10-weapons.md

11-combat.md

12-melee.md

14-glossary.md

15-geometry-layers.md

16-damage-system.md
```

Large systems should receive their own document.

Avoid mixing unrelated mechanics.

---

# Naming Conventions

Rule identifiers should follow this format:

```
MOV-001

WPN-001

CBT-001

TRN-001
```

Each document owns its own namespace.

---

# Versioning

StudCraft follows semantic versioning.

```
Major.Minor.Patch
```

Examples:

```
0.1.0

0.2.0

1.0.0
```

Major

Breaking changes.

Minor

New features.

Patch

Corrections and clarifications.

---

# Pull Requests

A good contribution explains:

- What changed.
- Why it changed.
- Which documents are affected.
- Which Design Principles are reinforced.

Whenever possible, include gameplay examples.

---

# AI Contributions

StudCraft is designed to be developed with both human and AI collaborators.

AI-generated contributions are welcome.

However, every proposal should:

- Follow the Design Code.
- Be internally consistent.
- Avoid inventing unnecessary mechanics.
- Reuse existing systems.

Human review is always recommended.

---

# The Golden Question

Before proposing any new mechanic, ask:

> **Can this be represented by the LEGO model?**

If the answer is yes,

build it.

If the answer is no,

consider whether the rule is truly necessary.

---

# Final Goal

StudCraft is not trying to become the largest tabletop ruleset.

It aims to become one of the most intuitive.

Every new contribution should make the game:

- Easier to understand.
- More enjoyable to build.
- More enjoyable to play.
- More faithful to its philosophy.

---

> **The Model Is The Rules.**

> **Every Brick Matters.**