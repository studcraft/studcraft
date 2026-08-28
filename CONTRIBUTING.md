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

**There are fifteen, and [`CODE_OF_DESIGN.md`](CODE_OF_DESIGN.md) defines them — `Principle 1` through `Principle 15`. Read them there.**

Every contribution should reinforce all fifteen. A proposal that conflicts with any of them gets redesigned rather than argued for.

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

**The questions are the Design Checklist closing [`CODE_OF_DESIGN.md`](CODE_OF_DESIGN.md). There are seven. Ask them there.** Any "no" means reconsidering the design.

[`system/design-process.md`](system/design-process.md) adds what the checklist does not: when several solutions would work, which to reach for first — construction before an existing rule, an existing rule before a new one, a new subsystem last.

Check [`TODO.md`](TODO.md) too: if the ruleset already declares your gap, the entry quotes the rule that declares it, and closing it means editing that rule rather than adding one beside it.

---

# Writing Style

**How a rule is written is [`system/documentation-standards.md`](system/documentation-standards.md)** — one imperative sentence, the reason in one clause, no over-explanation. It also owns the skeleton every ruleset document carries, and `python3 scripts/lint_ruleset.py` checks that skeleton.

Rules are precise. Write "a vehicle moves 1.5 times its own length", never "vehicles generally move a considerable distance".

---

# Repository Structure

The tree is in [`README.md`](README.md), and
[`system/documentation-standards.md`](system/documentation-standards.md) owns
what may be added to it — including the checklist for adding a new numbered
document, which touches more files than the document itself.

Large systems get their own document. Avoid mixing unrelated mechanics.

---

# Naming Conventions

**Owned by
[`system/documentation-standards.md`](system/documentation-standards.md).** In
short: a rule identifier is `ABC-001`, each document owns its prefix, and **an
identifier is never renumbered and never reused** — a deleted rule's number is
retired rather than handed on, and `scripts/check_id_stability.py` compares
every push against the base to prove it.

Do not guess a prefix. `python3 scripts/rule.py doc <file>` prints the one a
document actually uses.

---

# Versioning

**Nobody edits a version by hand — not `CHANGELOG.md`, and not a `**Version:**`
header in a ruleset document.** The `Release cut` workflow reads the latest tag
and the `docs/` changes since it, computes the bump, and writes both. A pull
request that edits `CHANGELOG.md` alongside `docs/` is refused by a CI gate,
which is what stops two proposal branches colliding on it.

Nothing has to be declared: a `docs/` change defaults to a **minor** release.
[`system/workflow.md`](system/workflow.md) has the mechanism and the one
override.

---

# Pull Requests

**Every change goes on a branch. Nothing is committed to `main` directly.** A
change to `docs/*.md` — the ruleset itself — additionally needs an OpenSpec
proposal, on its own branch named for it. Everything else (`README.md`,
`AGENTS.md`, `system/*.md`) needs a branch and no proposal.
[`system/workflow.md`](system/workflow.md) is the whole of it, and
[`system/repository-strategy.md`](system/repository-strategy.md) carries the
branch-naming table the CI gates read.

Before pushing:

```bash
python3 scripts/preflight.py
```

It runs every gate that can be answered without a push, so a red check is not
the first thing your pull request tells you.

A good contribution explains what changed, why it changed, which documents are
affected, and which Design Principles it reinforces. Include gameplay examples
wherever they help.

---

# AI Contributions

StudCraft is designed to be developed with both human and AI collaborators, and AI-generated contributions are welcome.

**[`AGENTS.md`](AGENTS.md) governs them, and it is binding rather than advisory.** It names which `system/` document owns each part of the work, and which of the four repository agents in `.claude/agents/` is raised at which step. An agent that applies a proposal itself, or issues its own git commands, has skipped the control the split exists to be.

A human reads the result before it is pushed. That step belongs to no agent.

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