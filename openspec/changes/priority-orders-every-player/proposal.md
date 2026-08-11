# Priority orders every player

## Why

`FLOW-003` determines Priority like this:

> At the beginning of every Turn, **both players** roll **1D6**.

Two words carry the whole defect. The ruleset never states how many players a game has, and the one rule that would answer the question has quietly answered it already: two.

It is not confined to that sentence. Every place the sequence of play is written down assumes a second player and no third:

- `FLOW-003` — "both players roll", "on a tie, both players roll again", "both players then alternate", and Priority is ceded to "**the other player**".
- `FLOW-002`, step 3 — "if a player has no unactivated units remaining, **the other player** continues activating their own remaining units consecutively".
- `FLOW-009` — "a Turn ends when every unit from **both players** has completed one activation".
- The Turn Sequence diagram — "Cede Priority (**opponent** activates first)".
- `docs/14-glossary.md`, *Priority* — "cedable to **the opponent**".

**The gameplay failure is narrower than the wording.** One die roll produces one winner, and with two players a winner is already a complete order: the loser goes second. With three it is not. The ruleset would know who activates first and nothing whatever about who activates after them — and `FLOW-002` would then hand the leftover units to "the other player", of which there are two.

**Nothing else in StudCraft is two-player.** A unit receives 3 Action Points (`CORE-006`) without asking who owns the model opposite. `CORE-009` grants a shot at whatever can be seen and names no owner. `DEP-001` agrees a Deployment Volume and `DEP-002` spends it per army, however many armies there are. `CORE-005` leaves terrain and structure placement to the scenario, and `FLOW-013` already requires the scenario to say how victory is judged for whatever players exist. The Component Damage System resolves an Impact against a component, not against a side.

The sequence of play is the only thing standing between StudCraft and a game of three.

## What Changes

- **`FLOW-001`** states the player count for the first time: **two or more**, with no upper limit. The limit is not written because the players already settle it when they agree the battlefield and the Deployment Volume (steps 3 and 4; `06-deployment.md`, DEP-001), with the models in front of them. The rule asserts no relation between those two that the ruleset has not written down — see `design.md`, Decision 8, which records why not, and what a later change would have to write.

- **`FLOW-003`** is rewritten around one mechanism. Every player rolls 1D6 simultaneously, and the results — highest to lowest — set the **Activation Order** for the Turn. The player who takes **first place in that order** holds Priority — first place, not the highest roll, because after a tie re-roll those are not the same thing. A tie is re-rolled by the tied players only, ordering their places among themselves; a player who did not tie keeps the place their first roll gave them. A player with no units left on the battlefield does not roll and takes no place in the order at all. The Priority player still makes one choice: activate now, or cede and take the **last** place, moving everyone else up one. Only that player makes it, once, and a player who reaches first place because someone else ceded does not inherit the choice.

- **`FLOW-002`**, steps 2 and 3. Step 2 activates one unit each in Activation Order instead of "alternating". Step 3 replaces the two-player leftover clause with the general one: a player with no unactivated units left is **skipped**, and the order carries on without them. `FLOW-002` is then the only rule that states the skip — `FLOW-003` cites it rather than repeating it.

- **`FLOW-009`** — "every unit from every player", not "from both players".

- **The Turn Sequence diagram** and the **Summary**, both of which restate the above and both of which currently restate the two-player version of it.

- **`docs/14-glossary.md`** — the *Priority* entry says "activate first or second", "cedable to the opponent" and "held by the player who rolled highest"; all three are corrected. A new ***Activation Order*** entry is added at the end of the file, because `FLOW-003` now defines a term a reader cannot infer from context and this glossary is in append order.

- **`docs/06-deployment.md`**, two sentences of narrative — the Design Philosophy's "a ceiling **both players** agreed to" and the Design Notes' "the volume **both players** agreed to". Neither is a rule and neither changes meaning, but a document declaring two players contradicts a `FLOW-001` that declares two or more, and this change is what makes the contradiction exist.

## What Does Not Change

- **A two-player game plays identically, clause for clause, but for the one case named at the end of this bullet.** `design.md` tabulates six clauses, old against new. Five reduce exactly:

  - The higher roll takes first place, and with it Priority — which is what "the player with the highest result gains **Priority**" produced, because at two players a tie is re-rolled until broken and the highest roll and first place are always the same player.
  - A tie is re-rolled by the players who rolled the same result, who are both of them, which is what "both players roll again until the tie is broken" produced.
  - Ceding moves the Priority player to the last of two places, which is "letting the other player activate first".
  - Cycling the order is alternation.
  - A player skipped for having nothing left to activate leaves one player cycling alone, which is "the other player continues activating their own remaining units consecutively".

  The sixth is the roll itself, and it carries the exception. *A player with no units left on the battlefield does not roll* is a new clause, and at two players it changes one case — one the old text handled incoherently. A player with nothing on the table could roll highest and hold a Priority whose only usable branch was to cede. `FLOW-013` leaves the end of a game to the scenario, so nothing in the ruleset says that situation cannot arise. It is closed here rather than preserved, because preserving it would mean writing the incoherence down on purpose, and it is the one behavioural difference this change makes to a two-player game.

- **The alternating unit activation system keeps its name.** `FLOW-002`'s procedure stops saying "alternate", but the system named in the Purpose and the Summary does not get renamed — see `design.md`, Decision 9.

- **`CORE-009`, `CBT-010` and the glossary's *Turn*.** All three cite `FLOW-002`, and all three were read against the new text: "one unit at a time", "during its own activation" and "every unit on the battlefield is activated once" are true of any number of players. None is edited.

- **`MOVE-017`'s friendly and enemy units.** With no alliance rule, every unit that is not yours is an enemy unit, which is what the rule already says. Teams are the scenario's business (`FLOW-013`), and a scenario that declares them declares what "friendly" means in it.

- **`FLOW-013`.** The scenario already has to state how the game ends and how victory is judged, for whatever players exist. It gains no clause about three-player victory, and it needs none.

- **No spec delta.** `docs/03-game-flow.md` predates this repository's OpenSpec workflow and has never been formalised as a capability — `openspec/specs/` holds no game-flow spec to write a `MODIFIED` block against, and `scenario-defines-victory` changed this same document with no `specs/` directory at all. The edits are tracked as ordinary doc-edit tasks, per `system/proposal-review.md` (*Delta vs. Direct Edit*).

- **`CHANGELOG.md` and every `**Version:**` header.** Release-cut-only. No `**Bump:**` line is written: minor is the default, and this is one — no legal army becomes illegal, no cost or measurement moves, and the only two-player behaviour that changes is the incoherent case named above.

## Out of Scope

- **Teams, alliances and shared victory.** A scenario may already declare them (`FLOW-013`); this change neither adds a rule for them nor forbids one. It makes the ruleset able to seat three players, which is what has to be true first.
- **Where each player deploys.** `06-deployment.md` charges a Deployment Volume per player and never places anyone on the table — placement is the scenario's (`CORE-005`). Nothing there assumes two, so nothing there is fixed beyond the two narrative sentences named above.
- **Turn-order variants.** Rolling once for the whole game, seating order, initiative that carries between Turns: all rejected in `design.md`, Decision 2, so the same suggestions are not re-proposed.
