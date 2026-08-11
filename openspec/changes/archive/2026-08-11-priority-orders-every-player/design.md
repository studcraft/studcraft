# Design — Priority orders every player

## The defect, stated once

`FLOW-003` asks two players for one die roll and gets back a complete answer, because with two
players the winner of a comparison and the order of the whole field are the same object. That
coincidence is what the rule is built on, and it holds for exactly one player count.

Add a third player and the roll answers a strictly smaller question. It names who activates
first. It says nothing about who activates second, and `FLOW-002` — which has to know — asks
"the other player" for it and finds two.

So this change is not "add a multiplayer mode". It is the removal of a coincidence the rule
mistook for a mechanism.

---

## Decision 1 — One simultaneous roll, not a bracket of pairwise rolls

The obvious generalisation of "both players roll and compare" is to keep comparing in pairs:
player 1 against player 2, the winner against player 3, and so on. It was considered and
rejected on four counts.

- **A bracket needs an order before it can produce one.** Who is "player 1"? Any answer is a
  seating rule, and a seating rule is the thing the roll exists to avoid.
- **Pairwise comparison is not transitive.** A rolls 5 against B's 3; B rolls 6 against C's 4;
  C rolls 6 against A's 2. The same three dice produce a different winner depending on which
  pair is compared first, so the bracket, not the dice, decides the Turn.
- **It produces a winner, not an order.** The ruleset needs every place filled, so a bracket
  needs a losers' bracket behind it — roughly `2N` comparisons where the field needs `N`
  results.
- **It multiplies the tie case.** Every comparison can tie and re-roll. One roll has one tie
  case; a bracket has one per match.

A single simultaneous roll sorted from highest to lowest has none of these properties. It fills
every place in one action, needs no prior ordering, and cannot disagree with itself.

**The tie clause has to be scoped for that last property to hold.** "The tied players roll again"
is unambiguous while there is one tie, and ambiguous the moment there are two: with 6, 6, 3, 3
every player has tied, and a reading that puts all four into one re-roll lets a 3 finish ahead of
a 6. So the re-roll is scoped to **each set of players who rolled the same result**, ordering
their places among themselves and no others. The two 6s settle places 1 and 2 between them, the
two 3s settle places 3 and 4, and no lower result can overtake a higher one however the reader
groups them. This case exists only from four players upward, which is why the rest of this design
works its examples at three.

## Decision 2 — The roll sets the whole order, and it is re-rolled every Turn

Two alternatives were considered and both are rejected.

**Roll once, keep the order for the game** (or take it from seating). It is fewer dice, and it
makes the first roll of the game decide every Turn of it. `FLOW-003` already rejects that shape
by re-determining Priority every Turn, and the reason survives at any player count: a player who
loses the roll should lose one Turn, not the game's sequence.

**Roll only for first place, and let the rest follow some other rule.** There is no other rule
available that is not either a seating order or a second roll, so this is Decision 1 with extra
steps.

Determining the whole order from the one roll costs nothing beyond what is already being rolled,
and it is the only reading under which `FLOW-002` has an answer for its own step 3.

## Decision 3 — Priority is first place in the Activation Order, not the highest roll

The current rule says "the player with the highest result gains **Priority**", and at two
players that phrase is exact: a tie is re-rolled until broken, so the deciding roll *is* the
highest roll.

At three it stops being exact. Rolls of 6, 6 and 3 leave two players who rolled highest, and the
re-roll that separates them is a roll of its own — smaller than the 3 as often as not. "The
player who rolled highest" then names nobody, or names the wrong player.

So Priority is attached to the order the rule has just finished constructing: **the player who
takes first place in the Activation Order holds Priority.** The rule already builds a total order
and there is no reason to grant its one right by any other means. The glossary entry is corrected
the same way, because it carried the same phrase.

**That needed one more word than the first draft gave it, and the audit of the applied text found
out why.** "The player who takes first place" is a description that stays true as the Turn moves:
a cede moves the ceding player to last and everyone else up one, so a different player takes first
place, and the rule then says four lines below that this player does not inherit the choice. Read
literally, the rule granted Priority to someone it immediately withheld the choice from. So the
rule and the glossary both bind possession to the moment: **first place when the order is
determined**. Priority is settled once, when the roll and its re-rolls are finished, and moving
through the order afterwards does not re-grant it.

## Decision 4 — Ceding moves the player to last place, not down one place

With two players the two readings are the same object, so the existing rule does not decide
between them, and a decision had to be made rather than derived.

**Last place is what ceding has always meant.** The reason to cede is information: let other
players commit their units before you commit yours. Last place is the maximum of exactly that,
so the rule and its purpose point the same way. Dropping one place would make the concession
shrink as the field grows — with three players a cede would cost almost nothing, and the choice
would stop being a choice.

It is also one sentence that behaves identically at every player count, which "drop one place"
is not (Principle 12).

The bullet names **the player who was second**, not the player who rolled second-highest, for
Decision 3's reason: after a re-roll the two need not be the same player. Everything in the rule
after the order is built refers to places, never to results — including the Turn Sequence diagram,
which uses the same five words rather than a looser gloss of its own.

## Decision 5 — Only the Priority player cedes, and only once

`FLOW-003` already says the choice is "a single choice made once, at the start of the Turn". At
two players that sentence has nothing to disambiguate. At three it does: if ceding passes first
place to another player, does that player now get to cede too?

If it did, a Turn could open with every player ceding in sequence and the order arriving back
where it started, having consumed a rule and decided nothing. So the new text says it outright —
a player who reaches first place because someone else ceded does not inherit the choice. That is
not a new restriction; it is the existing one, made unambiguous at the player count that can
test it.

## Decision 6 — A player with no units left does not roll

`FLOW-013` leaves the end of the game entirely to the scenario, so nothing in the ruleset says a
game stops when a player runs out of units — and at three players it plainly should not.

If a player with nothing on the table rolls, they can roll highest, and then hold a right they
cannot exercise — "activate one of their own units now" is impossible, while "cede Priority" is
still available and still reorders everyone else. A player with nothing on the table would get a
live decision over the sequence of play for the rest of the game.

The fix is upstream of Priority rather than inside it: **a player with no units left on the
battlefield does not roll and takes no place in the Activation Order.** They cannot hold Priority
because they are not in the order that grants it, and no clause about eliminated players is
needed anywhere else. This deliberately does not define elimination, or say when a game ends —
`FLOW-013` owns that, and the clause is worded to need no help from it.

**This is the one place the change alters a two-player game.** The defect above is not new and
is not three-player-only: under the current text a two-player game whose scenario has not ended
can have the emptied player roll, win Priority and cede. It is closed here rather than preserved,
because preserving it would mean writing the incoherence down on purpose. `proposal.md` names it
as the single exception to its identity claim.

The clause also creates a state no earlier text could reach: an Activation Order with one player
in it. Nothing breaks. That player holds Priority, activates, and cycles alone; the cede branch is
still offered and moving to the last of one place changes nothing, so it is a null choice rather
than an illegal one. Recorded here so it is not mistaken for an oversight.

## Decision 7 — `FLOW-002` owns the skip, and states it once

`FLOW-002` step 3 currently ends the Turn's alternation with a special case: when one player runs
out of units, "the other player continues activating their own remaining units consecutively,
with no alternation".

The general rule is shorter and has no special case in it: **a player with no unactivated units
left is skipped, and the order carries on without them.** With two players it produces exactly
the sentence it replaces — skip one of two and the other cycles alone, which is "consecutively,
with no alternation". With five players it produces the four remaining ones continuing in order,
which the old sentence could not express at all.

So the change removes a clause rather than adding one (Principle 11), and the removal is the
point: the old text was a special case only because it was written for the only case. Nothing in
the replacement restates the consecutive case either — it is what cycling an order of one *is*,
and writing it down again would put the special case back under a new name.

`FLOW-003` does not repeat the skip. An earlier draft stated it in both rules, which is the
"same rule asserted twice, independently" class from `system/proposal-review.md`. `FLOW-002`
owns the Turn's structure, so it owns the skip; `FLOW-003` points at `FLOW-002` for the
activation procedure the skip is part of, and says nothing about the skip itself.

The document's Summary does mention it, and that is not a second assertion — a Summary restates
the rules above it by definition (`system/proposal-review.md`, *The Summary Is Part of the Rule*).
What matters is that exactly one **rule** carries it, so there is exactly one place to edit if it
ever changes.

## Decision 8 — The player count is stated, and not capped

`FLOW-001` gains "two or more players". It does not gain a maximum, and the omission is
deliberate.

`system/proposal-review.md` (*Do Not Cap What the Model Already Bounds*) is the standing
argument. The ruleset already bounds every link of the chain except the last, and the last is
agreed at the table rather than computed:

```
each player's army   ≤ the Deployment Volume agreed in step 4 (DEP-001, DEP-002)
the Deployment Volume ≤ the battlefield agreed in step 3 (FLOW-001; WPN-005 states this link)
how many such volumes a battlefield holds — agreed by the players, like the two above it
```

Note that it is the **second** link that does the work, not the first. `DEP-001` charges a
Deployment Volume **per player** and `DEP-002` spends it per army, so N armies do not fit inside
one volume and no inequality of the form "players × army ≤ volume" is available. What bounds the
player count is how many volumes the agreed battlefield holds — a question the players answer
when they agree the battlefield, with the models in front of them, which is what Principle 1
asks for. Placement is not the ruleset's at all (`CORE-005`).

**The second link is not written down either, and `FLOW-001` therefore does not lean on it.**
`DEP-001` says a Deployment Volume "may have any dimensions agreed upon by the players" and
`DEP-009` says "No upper limit exists"; nothing relates either to the battlefield. `WPN-005`
already asserts the relation and cites `FLOW-001` for it — "the Deployment Volume [is bounded] by
the battlefield the players agree on before it" — and `FLOW-001` has never said so. An earlier
draft of this change's `FLOW-001` paragraph made the same assertion, which would have left the
same unwritten relation asserted in two rules and defined in none. Task 6.4 rewrote it to rest on
the agreement itself, which `DEP-001` does establish. Writing the link down properly, and
re-aiming `WPN-005` at wherever it lands, is a change of its own and is named under *What this
change deliberately leaves open* below.

A number written into `FLOW-001` would answer that question again, in advance, for tables it has
never seen.

The lower bound is stated, because it is not derivable: one player is not a game, and nothing
else in the ruleset says so.

## Decision 9 — The alternating unit activation system keeps its name

`03-game-flow.md`'s Purpose and Summary both name the system: an **alternating unit activation
system**. With three players the activation is a rotation rather than an alternation, and
renaming it was considered.

It is not renamed. "Alternating activation" is the established name for this family of turn
structures in tabletop games regardless of player count, and the two sentences that carry it are
describing what StudCraft is rather than instructing anyone what to do. The instructions are in
`FLOW-002` and `FLOW-003`, and those are the sentences that stop saying "alternate" and start
naming the Activation Order.

Recorded here so the rename is not proposed again as an inconsistency: it was seen, and the name
was kept. `tasks.md` task 5.10 checks that both lines survive the change.

## Decision 10 — No spec delta

`docs/03-game-flow.md` predates this repository's OpenSpec workflow. `openspec/specs/` holds
`action-economy`, `component-damage`, `damage-resolution`, `geometry-layers`, `unit-base`,
`weapon-capacity` and `weapon-construction` — no game-flow capability, so there is nothing for a
`MODIFIED` block to target, and inventing one is what `system/proposal-review.md` (*Delta vs.
Direct Edit*) forbids.

The precedent is exact: `2026-08-07-scenario-defines-victory` changed this same document and
shipped with no `specs/` directory at all.

`action-economy` is not the right home either. It owns the supply of Action Points and what may
be charged for them; who acts in what order is not an economy question, and adding a turn-order
requirement to it would put two mechanisms in one capability for no reason but that a capability
already existed.

One consequence has to be written into `tasks.md` rather than left to be discovered: `openspec
validate` **fails** on a delta-free change (`Change must have at least one delta`). That is why
the verification section runs `scripts/preflight.py` instead, which validates a change only when
it ships deltas — the same workaround the script already documents.

## Decision 11 — Minor, and no `**Bump:**` line

`system/documentation-standards.md` (Versioning) makes minor the default and reserves the marker
for a major. This is a minor: no legal army becomes illegal, no cost or measurement moves, and a
two-player game reads the new text and plays as before in every branch but one (Decision 6, and
the table below). What it adds is a player count the ruleset did not have.

---

## The two-player reduction, clause by clause

The claim in `proposal.md` — that a two-player game is unchanged but for one case — is checkable,
and this is the check. Each row states the old clause, the new one, and what the new one evaluates to when there
are two players.

| Old `FLOW-003` / `FLOW-002` | New text | At two players |
|---|---|---|
| "both players roll **1D6**" | every player rolls 1D6, simultaneously; a player with no units left does not roll | two players roll 1D6 — **except** where one of them has nothing left on the table and the scenario has not ended the game, the one case this change alters (Decision 6) |
| "the player with the highest result gains **Priority**" | the results set the Activation Order, highest to lowest; the player in first place holds Priority | higher roll takes first place and holds Priority; lower roll takes second, the only remaining place |
| "on a tie, both players roll again until the tie is broken" | each set of players who rolled the same result rolls again, ordering their places among themselves and no others; a tie inside a re-roll is broken the same way | there is one set and it is both of them, re-rolling until broken |
| "cede Priority, letting **the other player** activate first instead" | cede Priority, moving to the last place; everyone else moves up one, so the player who was second activates first | last of two places is second, so the other player activates first |
| "both players then alternate activating one unit at a time" | players activate one unit each in Activation Order, cycling through it | a two-place cycle is an alternation |
| "if a player has no unactivated units remaining, **the other player** continues activating their own remaining units consecutively" | a player with no unactivated units left is skipped, and the order carries on without them | skip one of two and the other cycles alone — consecutively, with no alternation |

Six clauses. Five are identities. The first row carries the one exception, and it is the only
branch of the new text whose two-player behaviour differs from the old text's — which is why
`proposal.md` claims identity with one named exception rather than compatibility.

---

## What this change deliberately leaves open

- **Teams, alliances and shared victory.** `FLOW-013` already lets a scenario declare how victory
  is judged, and a scenario that wants two players against one describes it. This change does not
  add an alliance rule to the ruleset, and does not decide whether one belongs there. What it
  settles is that the sequence of play no longer stands in the way.
- **What "friendly" means once teams exist.** `MOVE-017` lets friendly units move around each
  other and has enemy units block movement. Without alliances, "friendly" is "yours" and the rule
  is complete. A future alliance rule has to say whether an ally's units block, and that rule owns
  the question — not this one.
- **When a player is out of the game.** Decision 6 keeps a player with no units off the table out
  of the Activation Order without defining elimination, because `FLOW-013` leaves the end of a
  game to the scenario. Whether the ruleset should define it at all is a separate question, and
  the clause is worded so that answering it either way changes nothing here.
- **Whether ceding should exist at all at high player counts.** With eight players, ceding costs
  seven activations of information given away for one gained. That is a balance judgement about a
  rule this change inherits rather than introduces, and no number in the ruleset is available to
  settle it. The rule is the same at every count (Decision 4), which is the property worth keeping
  if it is ever revisited.
- **Turn-order effects a scenario might want.** A scenario may already restrict otherwise-legal
  actions (`FLOW-013`). Whether it may also fix, seed or freeze the Activation Order is not stated
  here, in either direction.
- **Whether the Deployment Volume is bounded by the battlefield.** `WPN-005` says it is and cites
  `FLOW-001`; `FLOW-001` does not say it, `DEP-001` lets the players agree any dimensions, and
  `DEP-009` says no upper limit exists. The relation is real at the table and unwritten in the
  ruleset. This change declined to write it — a rule about deployment does not belong in a
  proposal about turn order, and `WPN-005`'s citation needs re-aiming in the same pass. Task 6.4
  removed this change's own dependence on it.
- **Reading the Activation Order off the table.** The dice are rolled simultaneously and openly
  and then, in the current rules, forgotten — the order becomes something the players remember,
  which is easy at two and is state at five. Leaving each die where it fell, and moving your own
  to the end of the line when you cede, would make the order physical. Principle 1 and Principle 6
  both point that way and no rule currently says either. It is left open rather than adopted
  because it is a new rule about components on the table, not a repair to this one, and nothing
  here is undecided without it.
