# StudCraft Design Code

> **Every Brick Matters.**

---

# Purpose

This document defines the core design philosophy of StudCraft.

It is **not** a rulebook.

Instead, it serves as the project's constitution.

Every new mechanic, rule, component or expansion should be evaluated against these principles.

If a proposal violates the Design Code, it should be redesigned before being added to the game.

---

## "The Model Is The Rules" and the written rules

The rules live in `docs/`. There are over two hundred of them, and they are numbered, precise and binding. That is not in tension with this document's central claim, but the relationship is worth stating plainly, because it is the first thing a new reader asks.

**The model supplies the values. The ruleset supplies the procedures.**

A weapon's range is not written anywhere — you measure the weapon. But *that* range is `Weapon Length × 6`, and that a target must be inside it, and how the resulting Attack Dice are rolled, are all written down, because none of them can be read off a brick.

So "The Model Is The Rules" does not mean there are no written rules. It means there is **no profile to consult before looking at the model** — no stat card, no unit entry, no hidden number that the model merely illustrates. Every quantity the rules consume is measured from the construction in front of you.

This document states no rules of its own. Where a principle below mentions a specific value, it cites the rule in `docs/` that owns it, and that rule is the authority.

---

# The StudCraft Philosophy

StudCraft is not a traditional tabletop wargame.

It is a **construction-driven game**, where LEGO models are both the miniatures and the rules.

Players do not build models to match a profile.

Instead, they build models that *become* their profile.

Every mechanic in StudCraft should reinforce this philosophy.

---

# Principle 1 — The Model Is The Rules

The physical model is the primary source of gameplay information.

Whenever possible, a player should understand how a model behaves simply by looking at it.

Examples:

- Weapon length determines range.
- Weapon muzzles determine attack dice.
- Vehicle size determines movement.
- Cargo space determines transport capacity.
- Visible components determine targetable areas.

If a mechanic requires consulting a profile before looking at the model, reconsider the design.

---

# Principle 2 — Every Brick Matters

Every LEGO element should have a meaningful purpose.

A brick may represent:

- Structure
- Armour
- Pilot
- Weapon
- Door
- Window
- Wheel
- Track
- Cargo space
- Interior layout

Decoration is encouraged, but functional construction is the heart of StudCraft.

---

# Principle 3 — Construction Over Abstraction

Whenever a rule can be represented by construction, construction takes priority.

Ask this question before introducing a new rule:

> **Can this be represented by the LEGO model?**

If the answer is yes, prefer the physical solution.

Examples:

Instead of a transport statistic, build a larger cargo compartment.

Instead of a weapon profile, build a longer barrel.

Instead of a movement value, use the vehicle's physical dimensions.

---

# Principle 4 — Components Over Statistics

Models are collections of components.

Examples:

- Pilots
- Weapons
- Wheels
- Tracks
- Doors
- Windows
- Turrets

Components may be individually targeted, damaged and replaced.

Vehicles are machines, not health bars.

Buildings are structures, not hit point pools.

---

# Principle 5 — Impacts Over Damage

Weapons never inflict damage directly.

Weapons generate **Impacts**.

The target resolves those Impacts according to its components' construction.

This separation creates a flexible and modular combat system.

---

# Principle 6 — Physical State Over Tokens

Whenever possible, the LEGO model itself should represent its current condition.

Examples:

- A wounded soldier sits down.
- A destroyed window is removed.
- A broken door remains open.
- A disabled weapon is detached.
- A destroyed wheel is removed.

Avoid markers, counters and tokens unless absolutely necessary.

---

# Principle 7 — One Universal Measurement

StudCraft uses a single measurement system.

The **Unit Base (UB)** is the fundamental unit of the game.

One Unit Base measures:

**4 × 3 studs**

— defined by `docs/02-core-rules.md` (CORE-001), which is the authority on its dimensions and orientation.

Everything should be expressed using Unit Bases whenever practical.

Examples:

- Deployment
- Vehicle footprints
- Transport capacity
- Cargo
- Interior layouts

A common language makes the game easier to learn and expand.

---

# Principle 8 — One Universal Economy

StudCraft uses a single resource for actions.

Every unit receives:

**3 Action Points (AP)**

— defined by `docs/02-core-rules.md` (CORE-006), which is the authority on the amount and on what may be spent.

Construction determines what a unit *can* do.

Action Points determine *when* it can do it.

Avoid introducing additional resource systems unless they provide significant value.

---

# Principle 9 — Physical Visibility

Visibility is determined by the model, not by abstract templates.

The core rule is simple:

> **If you can see it, you can shoot it.**

Visibility is symmetric: what can see you can target you. Whether that produces a shot outside a unit's own activation is a rule, not a principle — `docs/02-core-rules.md` (CORE-009) decides it.

Construction determines cover, exposure and firing opportunities.

---

# Principle 10 — Modular Rules

Each document in the repository should have one clear responsibility.

Examples:

- Weapons generate Impacts.
- Combat resolves attacks.
- The Component Damage System resolves Impacts.
- Vehicles define movement.
- Transport defines capacity.

Rules should interact through well-defined interfaces, not by duplicating mechanics.

---

# Principle 11 — Simplicity Before Complexity

Whenever two solutions achieve the same goal, choose the simpler one.

Complexity should emerge from:

- Player decisions.
- Model construction.
- Battlefield interaction.

Not from lengthy rule exceptions.

---

# Principle 12 — Consistency

A rule should behave the same way regardless of context.

If a mechanic works for infantry, consider whether it should also work for:

- Vehicles
- Buildings
- Terrain
- Future expansions

Consistency reduces the number of special cases players must remember.

---

# Principle 13 — Build Freedom

Players are free to build their own creations.

StudCraft does not define fixed units.

Instead, it defines a common construction language.

Creativity is encouraged, provided that models follow the construction standards described in the rules.

---

# Principle 14 — Easy to Learn, Deep to Master

The core rules should be understandable after a single game.

Depth should emerge from:

- Construction choices.
- Tactical positioning.
- Component interaction.
- Battlefield design.

Not from memorising complex statistics.

---

# Principle 15 — Future Compatibility

New mechanics should extend the existing systems instead of replacing them.

Whenever possible:

- Reuse existing Action Points.
- Reuse Unit Bases.
- Reuse the Impact system.
- Reuse the Component Damage System.

Avoid introducing parallel systems that duplicate existing mechanics.

---

# Design Checklist

Before adding a new rule, ask:

- Can it be represented by the LEGO model?
- Does it require hidden statistics?
- Does it reuse an existing system?
- Does it introduce unnecessary exceptions?
- Does it make construction more meaningful?
- Does it remain intuitive?
- Does it reinforce "Every Brick Matters"?

If the answer to any of these questions is "No", reconsider the design.

---

# Final Statement

StudCraft is a game about building.

The models are not illustrations of the rules.

They **are** the rules.

Every decision made while building should have the potential to influence the game.

Every brick should matter.

---

> **The Model Is The Rules.**

> **Every Brick Matters.**