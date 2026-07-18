# AGENTS.md

> Instructions for AI agents contributing to StudCraft.

---

# Purpose

This document defines how AI agents should interact with the StudCraft repository.

StudCraft is a specification-driven project.

Agents are expected to preserve the project's philosophy, maintain consistency and extend the rules without introducing unnecessary complexity.

Before making any contribution, every agent should read:

1. `README.md`
2. `CODE_OF_DESIGN.md`
3. `CONTRIBUTING.md`

These documents define the project's identity.

---

# Project Philosophy

StudCraft is founded on one central idea:

> **The Model Is The Rules.**

Gameplay should emerge from the physical LEGO model whenever possible.

Avoid replacing physical representation with abstract mechanics.

---

# Core Principles

Every contribution should reinforce the following principles:

- The Model Is The Rules
- Every Brick Matters
- Construction Over Abstraction
- Components Over Statistics
- Impacts Over Damage
- Physical State Over Tokens
- Modular Design
- Simplicity Before Complexity

If a proposal conflicts with these principles, redesign it.

---

# Agent Responsibilities

Agents should:

- Preserve consistency across documents.
- Prefer extending existing systems over creating new ones.
- Keep rules modular.
- Reduce unnecessary complexity.
- Explain the reasoning behind significant proposals.
- Maintain clear technical writing.

Agents should avoid introducing mechanics that duplicate existing functionality.

---

# Design Process

Before proposing a new mechanic, ask:

1. Can this be represented physically by the LEGO model?
2. Can an existing system already solve this?
3. Does this introduce hidden statistics?
4. Does this make construction more meaningful?
5. Does this remain intuitive for players?

If the answer to any question is negative, reconsider the proposal.

---

# Rule Hierarchy

When multiple solutions exist, prioritize them in this order:

1. Physical construction
2. Existing rules
3. New modular rule
4. New subsystem

New subsystems should be introduced only when absolutely necessary.

---

# Preferred Design Patterns

Agents should favor:

- Universal systems
- Reusable mechanics
- Component-based design
- Physical representation
- Consistent terminology
- Minimal exceptions

Avoid special-case rules whenever possible.

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
    ├── 13-materials.md
    └── 14-glossary.md
```

Agents should preserve this modular organization.

---

# Documentation Guidelines

Each document should have one clear responsibility.

Avoid mixing unrelated systems.

Rules should:

- Be deterministic.
- Be concise.
- Be easy to reference.
- Reuse existing terminology.

Every document should include:

- Purpose
- Design Philosophy
- Rule Definitions
- Summary

---

# Naming Conventions

Rule identifiers should remain stable.

Examples:

```
MOV-001
WPN-001
CBT-001
TRN-001
FLOW-001
```

Each document owns its own namespace.

---

# Versioning

StudCraft follows Semantic Versioning.

```
MAJOR.MINOR.PATCH
```

Examples:

- 0.1.0
- 0.2.0
- 1.0.0

Agents should update the changelog whenever behaviour changes.

---

# OpenSpec Workflow

StudCraft uses OpenSpec for design discussions and architectural decisions.

Rules should not be added directly without first considering whether they belong in an OpenSpec proposal.

OpenSpec stores:

- Design proposals
- Design decisions
- Historical rationale
- Future ideas

The `/docs` directory stores only the current accepted rules.

---

# Communication Style

Agents should:

- Explain why a proposal improves the design.
- Prefer evolution over replacement.
- Avoid unnecessary rewrites.
- Preserve backwards compatibility whenever practical.

Large architectural changes should be proposed before implementation.

---

# Decision Filter

Before suggesting any rule, ask:

- Does this reinforce construction?
- Does this simplify the game?
- Does this remove hidden information?
- Does this reuse existing mechanics?
- Does this fit the Design Code?

If not, redesign it.

---

# Long-Term Vision

StudCraft should remain:

- Modular
- Construction-driven
- Physically intuitive
- Easy to learn
- Deep to master
- Friendly to both human and AI contributors

The project should grow by expanding existing systems rather than replacing them.

---

# Final Principle

Whenever an agent is uncertain about a design decision, return to the project's central philosophy:

> **The Model Is The Rules.**

If the LEGO model can express the rule, let the model do the work.

---

> **Every Brick Matters.**