# StudCraft Game Flow

**Version:** 0.2.0 Draft

---

# Purpose

This document defines the sequence of play in StudCraft.

It explains how a game begins, how Turns and unit activations are resolved, and how a game ends.

StudCraft uses an **alternating unit activation system**: players activate one unit at a time until every unit has activated once.

---

# Design Philosophy

StudCraft does not use separate Movement, Shooting or Assault phases.

Instead, a unit completes its entire activation before another unit is activated.

This keeps the game flow simple and ensures that movement, combat and other actions can be combined naturally within the same activation.

The result is a continuous sequence of meaningful unit decisions rather than disconnected phases.

---

# FLOW-001 — Starting a Game

StudCraft is played by **two or more players**, each fielding their own force.

Before the first Turn:

1. Select a scenario (`FLOW-013`).
2. Agree the objectives and how victory is judged.
3. Agree on the battlefield size.
4. Agree the Deployment Volume — `W × D × H` in Unit Bases (`06-deployment.md`, DEP-001).
5. Build each player's force.
6. Deploy all units.
7. Determine Priority.
8. Begin Turn 1.

The battlefield and Deployment Volume are agreed before forces are built so that the physical space and mission can influence force construction.

If the scenario already defines the objectives, step 2 confirms them. If the players are creating the scenario, this is where they establish them.

---

# FLOW-002 — Turn Structure

Each game is divided into Turns.

At the beginning of every Turn:

1. Determine Priority (`FLOW-003`).
2. Activate units one at a time in the Activation Order.
3. Skip players who have no unactivated units remaining.
4. Continue until every unit has been activated once.
5. Resolve End of Turn effects (`FLOW-009`).
6. Begin a new Turn.

Every unit therefore receives exactly one activation per Turn.

This alternating structure keeps all players involved throughout the Turn rather than giving one player a complete sequence of actions before the opponent can respond.

---

# FLOW-003 — Priority

At the beginning of every Turn, every player with units still on the battlefield rolls **1D6**, simultaneously.

The results determine the **Activation Order**, from highest result to lowest. The player placed first holds **Priority**.

Ties are resolved by rerolling only the tied players. The reroll determines their order among themselves; all other positions remain unchanged. A tie in a reroll is resolved the same way.

The player with Priority makes one choice:

* **Activate** one of their own units immediately, keeping their position in the Activation Order.
* **Cede Priority**, moving to the last position in the Activation Order while every other player moves up one position.

This choice is made only once, at the beginning of the Turn.

A player who reaches first position because another player ceded Priority does not gain another Priority choice.

Priority determines who acts first; it does not change the number of activations a player receives.

Priority and Activation Order are determined again at the beginning of every Turn.

---

# FLOW-004 — Unit Activation

When a unit is activated, it receives its Action Points (`02-core-rules.md`, CORE-006).

The player may spend those Action Points in any legal order.

The activation ends when:

* the unit has spent all available Action Points; or
* the player chooses to stop.

A unit may be activated only once per Turn.

The activation is the fundamental decision unit of StudCraft: all actions performed by a unit belong to the same continuous activation.

---

# FLOW-007 — Combining Actions

Actions may be combined freely during an activation.

Players may perform any legal sequence of actions provided they have enough Action Points.

Examples:

**Example A**

* Move
* Move
* Attack

**Example B**

* Open Door
* Move
* Close Door

**Example C**

* Rotate
* Move
* Attack

**Example D**

* Open Ramp
* Disembark
* Close Ramp

StudCraft therefore does not require players to finish one type of action before beginning another.

---

# FLOW-008 — Activated Units

After completing its activation, a unit becomes **Activated**.

An Activated unit:

* May still be attacked and resolves incoming Impacts normally as the defender (`11-combat.md`, CBT-008).
* Continues to occupy the battlefield normally.
* Cannot activate again until the next Turn.

Being Activated does not create a defensive action or reaction. It only records that the unit has already completed its activation for the current Turn.

---

# FLOW-009 — End of Turn

A Turn ends when every unit has completed one activation.

Then:

1. Resolve temporary effects.
2. Resolve scenario effects.
3. Begin the next Turn by determining Priority.

End of Turn effects occur after all unit activations and before the next Turn begins.

---

# FLOW-010 — End of Game

The active scenario determines when the game ends and how victory is judged (`FLOW-013`).

A scenario may end the game through conditions such as:

* A fixed Turn limit.
* Capturing an objective.
* Eliminating a specific target.
* Escorting a convoy.
* Evacuating the battlefield.

**The end condition determines when the game stops.**

**The victory condition determines who wins when it stops.**

These are separate rules and a scenario must define both.

For example, a scenario may state that the game ends when a convoy reaches the far edge or Turn 6 ends, and that the escorting player wins if the convoy arrived.

---

# FLOW-012 — No Hidden Statistics

StudCraft does not use hidden activation statistics.

Every unit receives the same Action Point allotment defined by `02-core-rules.md` (CORE-006) and follows the same activation sequence (`FLOW-004`).

A unit's physical construction determines what it can do.

The game therefore does not require hidden Initiative, Speed or Activation values to determine when or how often a unit acts.

---

# FLOW-013 — Scenario

Every game is played under a scenario.

The ruleset defines how models behave. The scenario defines what the players are trying to accomplish and when the game ends.

A scenario **must** state:

* **How the game ends** — a Turn limit, a condition being met, or both (`FLOW-010`).
* **How victory is judged** — what each player must achieve and how a winner is determined when the game ends.
* Whether the game can end in a draw.

A scenario **may** also state:

* The battlefield size and Deployment Volume (`FLOW-001`, `06-deployment.md`, DEP-001).
* Where terrain and structures are placed (`02-core-rules.md`, CORE-005).
* Restrictions on otherwise-legal actions, such as limiting weapons fired in one activation (`10-weapons.md`, WPN-014), restricting reverse movement (`08-vehicles.md`, VEH-006), or restricting how a weapon system's Attack Dice are split (`11-combat.md`, CBT-007).
* Additional movement options such as sprinting (`17-infantry.md`, INF-002).
* Scenario-specific objectives, capture rules, victory points or other mission mechanics.

Scenario rules are third in the rule priority order (`02-core-rules.md`, Universal Rule). They may restrict or extend the ruleset for that game but may not contradict Foundations or Core Rules.

The core rules define model behavior and the general flow of play; the scenario defines the specific purpose and conditions of the game.

---

# Summary

The flow of a StudCraft game is:

1. Select the **Scenario**.
2. Make the required **Agreements**.
3. Build the forces.
4. Deploy the units.
5. Repeat Turns:
   1. Determine **Priority**.
   2. Follow the **Activation Order**.
   3. Activate each unit once.
   4. Resolve End of Turn effects.
6. End the game when the scenario's end condition is met.
7. Determine the winner using the scenario's victory condition.

StudCraft replaces traditional Movement, Shooting and Assault phases with **alternating unit activations**.

Each unit completes its entire activation before the next unit acts, allowing movement, combat and other actions to be combined freely while keeping the sequence of play clear.

---

> **Every Brick Matters.**
