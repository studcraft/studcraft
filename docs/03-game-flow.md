# StudCraft Game Flow

**Version:** 0.1.0 Draft

---

# Purpose

This document defines the sequence of play in StudCraft.

It explains how a game begins, how turns are played, how units are activated and how a game ends.

StudCraft uses an **alternating unit activation system**, where players activate one unit at a time until every unit has acted.

---

# Design Philosophy

StudCraft does not use separate Movement, Shooting or Assault phases.

Instead, each unit completes its entire activation before the next unit is activated.

This creates a dynamic, cinematic and easy-to-follow flow of play.

---

# FLOW-001 — Starting a Game

Before the first Turn:

1. Select a scenario.
2. Agree on the battlefield size.
3. Select the deployment size (measured in Unit Bases).
4. Build each player's force.
5. Deploy all units.
6. Determine Priority.
7. Begin Turn 1.

---

# FLOW-002 — Turn Structure

Each game is divided into Turns.

At the beginning of every Turn:

1. Determine Priority.
2. Players alternate activating one unit at a time.
3. Continue until every unit has been activated once.
4. Resolve End of Turn effects.
5. Begin a new Turn.

---

# FLOW-003 — Priority

At the beginning of every Turn, both players roll **1D6**.

The player with the highest result gains **Priority**.

On a tie, both players roll again until the tie is broken.

The player with Priority chooses one of the following:

- Activate one of their own units now, keeping the activation.
- Cede Priority, letting the other player activate first instead.

This is a single choice made once, at the start of the Turn. Whichever player activates first, both players then strictly alternate activating one unit at a time (per FLOW-002) for the remainder of the Turn.

Priority is determined again at the beginning of every Turn.

---

# FLOW-004 — Unit Activation

When a unit is activated, it immediately receives:

**3 Action Points (AP)**

(see `02-core-rules.md`, CORE-006, for the canonical definition)

The player may spend these AP in any legal order.

When all AP have been spent, or the player decides to stop, the activation ends.

A unit may only be activated once per Turn.

---

# FLOW-005 — Universal Action Points

The 3 AP defined in CORE-006 apply identically to every unit type in StudCraft, with no exceptions:

- Infantry
- Vehicles
- Walkers
- Hovercraft
- Future unit types

No unit gains additional AP through its profile.

Differences between units emerge from their physical construction, not from hidden statistics.

---

# FLOW-006 — Common Actions

Action Points may be spent on actions such as:

- Move
- Rotate
- Attack
- Open a door
- Close a door
- Open a ramp
- Close a ramp
- Embark
- Disembark
- Interact with terrain
- Operate scenario objectives

Each action's AP cost is defined in its corresponding rule document.

---

# FLOW-007 — Combining Actions

Actions may be combined freely during an activation.

Examples:

**Example A**

- Move
- Move
- Attack

---

**Example B**

- Open Door
- Move
- Enter Building

---

**Example C**

- Rotate
- Move
- Attack

---

**Example D**

- Open Ramp
- Disembark Infantry
- Close Ramp

Players may combine actions in any order, provided they have enough AP remaining.

---

# FLOW-008 — Activated Units

After completing its activation, a unit becomes **Activated**.

Activated units:

- May defend themselves.
- May be attacked.
- Continue to occupy the battlefield normally.

They may not activate again until the next Turn.

---

# FLOW-009 — End of Turn

A Turn ends when every unit from both players has completed one activation.

Then:

1. Resolve temporary effects.
2. Resolve scenario effects.
3. Begin a new Turn by determining Priority again.

---

# FLOW-010 — End of Game

The active scenario determines when the game ends.

Examples include:

- Survive a fixed number of Turns.
- Capture objectives.
- Eliminate a specific target.
- Escort a convoy.
- Evacuate the battlefield.

---

# FLOW-011 — Action Economy

Action Points are the universal resource in StudCraft.

Every meaningful action consumes AP.

Examples include:

- Moving
- Attacking
- Opening doors
- Closing doors
- Operating ramps
- Embarking
- Disembarking
- Interacting with objectives

Players must decide how to spend their limited AP each activation.

---

# FLOW-012 — No Hidden Statistics

StudCraft does not use hidden activation values.

Every unit follows the same activation sequence:

- Gain AP (CORE-006).
- Spend AP.
- End activation.

Construction determines what a unit can do.

The activation system remains identical for all units.

---

# Turn Sequence

```text
Start Turn

↓

Determine Priority

↓

Priority player chooses:
• Activate own unit now (continue)
or
• Cede Priority (opponent activates first)

↓

Alternate Unit Activations

↓

Each Activated Unit receives 3 AP

↓

Spend AP

↓

Next Unit

↓

All Units Activated

↓

Resolve End of Turn Effects

↓

Begin Next Turn
```

---

# Summary

Every Turn follows the same structure:

1. Determine Priority.
2. The Priority player chooses who activates first.
3. Players alternate activating one unit at a time.
4. Each activated unit receives **3 AP**.
5. Spend AP in any legal combination.
6. Continue until every unit has activated.
7. Resolve End of Turn effects.
8. Start a new Turn.

StudCraft replaces traditional game phases with **alternating unit activations**, keeping every player involved throughout the game.

---

> **Every Brick Matters.**