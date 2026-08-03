## Why

### Nothing in the ruleset says how a game is won

A search of all fifteen documents for *win*, *winner*, *victory* and *defeat* returns one hit, and it is about a muzzle defeating a thickness of brick.

`FLOW-010` states when a game **ends** — survive a fixed number of Turns, capture objectives, eliminate a target. It never states who has **won** when it does. Two players can play a complete game by these rules and have no sanctioned way to say which of them succeeded.

### And "scenario" is never defined, while eight rules depend on it

`FLOW-001` opens with "Select a scenario." Nothing anywhere says what a scenario is or what one must contain, yet it carries more weight than any other undefined term in the ruleset:

| Rule | What it delegates to the scenario |
|---|---|
| `FLOW-010` | when the game ends |
| `CORE-005` | placement of structures |
| `CORE` Universal Rule | fourth in the rule-priority order |
| `DEP-001` | scenario-defined Deployment Areas |
| `MOVE-004` | sprinting and special movement |
| `VEH-006` | restrictions on reverse movement |
| `WPN-014` | limiting weapons fired per activation |
| `CBT-007` | restricting how Attack Dice split between targets |

Eight rules point at an artefact the ruleset never describes. That is the dangling-reference pattern this repo has repaired repeatedly, at its largest scale.

The two gaps are one gap. Objectives cannot be defined at the start of a game if nothing consumes them, and the thing that should consume them — the scenario — has no definition to put them in.

## What Changes

Three edits, in the order the dependency runs.

- **`FLOW-013` — Scenario** (new). States what a scenario must specify, and what it may. Gives the eight deferrals above something to cite.
- **`FLOW-010`** — extends from "when the game ends" to when it ends **and who has won**, both supplied by the scenario.
- **`FLOW-001`** — a new step, after selecting the scenario and before building forces: agree the objectives and how victory is judged.

Also a glossary entry for **Scenario**, since it is now a defined term.

### Where the new step goes, and why there

`FLOW-001`'s sequence is: select a scenario, agree battlefield size, agree deployment size, build forces, deploy, determine Priority, begin.

The objectives step goes **second**, immediately after selecting the scenario and before the two sizing steps. What a force is trying to achieve shapes what it should bring, and by step 4 a player is already committing to a build. Agreeing objectives after that would be agreeing them too late to matter.

## Impact

**No existing mechanic changes.** No distance, cost, threshold or roll is touched. Nothing that is legal becomes illegal.

**One new rule ID**, `FLOW-013`. No existing ID is renumbered.

**The ruleset still prescribes no objectives.** `FLOW-013` says a scenario must state its victory conditions; it does not say what they may be, and it invents no marker, capture or scoring mechanic. That restraint is deliberate and matches how this ruleset treats every other player-agreed quantity — `DEP-001` requires a Deployment Area to be agreed without dictating its size, and `FLOW-001` already requires a battlefield size the same way.

It is also Principle 13 applied one level up: the game defines no fixed units, and should define no fixed missions either. What it can define is what a mission has to declare.

**Victory is a scenario property, not a rules property.** A reader looking for "how do I win StudCraft" will now find the answer — *the scenario says, and here is what it must say* — rather than finding nothing at all.

### Deliberately not included

- **Any objective mechanic.** No objective markers, no capture rules, no victory points. A scenario that wants them describes them; the ruleset does not presume the shape.
- **A scenario library.** Worth having, and it does not belong in `docs/`. A scenario is a configuration built on the rules, not a rule: giving one a `FLOW-` style ID would subject it to the ruleset's versioning and priority order, which is wrong. It belongs in its own directory, marked as examples rather than canon, and it is the lowest-risk contribution anyone can make to this repo because it touches no rule.

  Not recorded in `TODO.md` either: that file is scoped to gaps the documents declare in their own text, each entry quoting the rule that declares it. "The repository ships no scenarios" is a repository gap, not a declared one. This paragraph is the record, and the archive preserves it.
- **Draw conditions, concessions, timed games.** All scenario-level concerns.

Not applied — proposal only.
