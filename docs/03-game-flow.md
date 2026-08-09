# StudCraft Game Flow

**Version:** 0.2.0 Draft

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

1. Select a scenario (FLOW-013).
2. Agree the objectives and how victory is judged.
3. Agree on the battlefield size.
4. Agree the Deployment Volume — `W × D × H` in Unit Bases (`06-deployment.md`, DEP-001).
5. Build each player's force.
6. Deploy all units.
7. Determine Priority.
8. Begin Turn 1.

Step 2 comes before step 5 deliberately: what a force is trying to achieve shapes what it should bring. If the scenario already states its objectives, this step is confirming them; if the players are inventing a scenario, this is where they do it.

---

# FLOW-002 — Turn Structure

Each game is divided into Turns.

At the beginning of every Turn:

1. Determine Priority.
2. Players alternate activating one unit at a time.
3. Continue until every unit has been activated once. If a player has no unactivated units remaining, the other player continues activating their own remaining units consecutively, with no alternation, until they too have all been activated.
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

This is a single choice made once, at the start of the Turn. Whichever player activates first, both players then alternate activating one unit at a time (per FLOW-002) for the remainder of the Turn, until one player has no unactivated units left — at which point the other continues activating consecutively (FLOW-002).

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

- May be attacked, and resolve incoming Impacts as the defender (`11-combat.md`, CBT-008) — this is not a reaction or an out-of-turn attack, just the standard defender-side resolution any target performs.
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

The active scenario determines when the game ends and who has won (FLOW-013).

Examples of ending conditions include:

- Survive a fixed number of Turns.
- Capture objectives.
- Eliminate a specific target.
- Escort a convoy.
- Evacuate the battlefield.

Each of these is an ending condition, not a victory condition. A scenario states both: the game ends when the convoy reaches the far edge *or* Turn 6 passes, and the escorting player wins if it arrived. The ruleset supplies neither — it requires the scenario to supply both.

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

# FLOW-013 — Scenario

Every game is played under a scenario. The scenario is what makes one game different from another: the ruleset defines how models behave, and the scenario defines what the players are trying to do with them.

A scenario **must** state:

- **How the game ends** — a Turn limit, a condition being met, or both (FLOW-010).
- **How victory is judged** — what each player must achieve, and how a winner is determined when the game ends. A scenario may declare that a game can be drawn.

A scenario **may** also state:

- The battlefield size (FLOW-001) and the Deployment Volume (`06-deployment.md`, DEP-001).
- Where terrain and structures are placed (`02-core-rules.md`, CORE-005).
- Restrictions on otherwise-legal actions, such as limiting the weapons a unit may fire in one activation (`10-weapons.md`, WPN-014), restricting reverse movement (`08-vehicles.md`, VEH-006), or restricting how a weapon system's Attack Dice may be split (`11-combat.md`, CBT-007).
- Additional movement options such as sprinting (`07-movement.md`, MOVE-004).

Scenario rules sit fourth in the rule priority order (`02-core-rules.md`, Universal Rule): they may restrict or extend the ruleset for one game, and never contradict Foundations, Core Rules or Construction Standards.

This ruleset defines no objectives of its own. It states what a scenario must declare, not what it may declare — the same way DEP-001 requires a Deployment Volume to be agreed without dictating its size. A scenario that wants objective markers, capture rules or victory points describes them itself.

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