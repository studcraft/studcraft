# Design — CORE stops describing units

## Decision 1 — What stays in CORE, and the test that decides it

The test is not "is this universal?" — a great deal about infantry is universal to infantry. It is:

> **Does every unit type read this rule, or does it read a different answer per unit type?**

A rule giving one answer stays. A rule giving a per-domain answer belongs to the domains, and CORE keeps at most a pointer.

| Rule | Answer | Verdict |
|---|---|---|
| `CORE-001` volume, conversion, footprint | one | stays |
| `CORE-001` "the base every infantry model is built on" | infantry only | moves |
| `CORE-002` every model has an obvious front | one | stays |
| `CORE-002` how that front is decided | per domain | moves |
| `CORE-006` 3 AP, no cost scales with size | one | stays |
| `CORE-014` equipment must be on the model | one | stays |
| `CORE-015` hands | minifigures only | retired |

`CORE-003` and `CORE-004` already pass the test. This change applies it to the rules around them.

## Decision 2 — `CORE-001` keeps everything but one sentence

Sixteen rules cite `CORE-001`. Reading each against the text that survives: `CMP-018`, `VEH-028`, `TRN-019` and `WPN-004` read dimensions; `DEP-001`, `DEP-002`, `VEH-001`, `TRN-001`, `TRN-002`, `TRN-003`, `TRN-013`, `TRN-020` read the volume or the footprint convention; `INF-002`, `INF-003` and `INF-012` read the 3-stud depth and 4-stud width as step sizes.

**Exactly one citer reads it for the sentence being removed:** `INF-001`, which says an infantry model is "built on the base required by `02-core-rules.md` (CORE-001)". Decision 3 moves it.

**Rejected: removing the `4 × 3` horizontal reading with it.** It is the physical anchor of the volume — footprints, deployment floors and transport capacity all consume it — and the review that prompted this change says so outright. What is infantry-specific is not the measurement; it is the claim that a minifigure must be built on one.

## Decision 3 — `INF-001` states its base rather than fetching it

Today the chain is circular. `INF-001` asks `CORE-001` what base an infantry model is built on, and `CORE-001` answers with an infantry fact. It asks `CORE-002` which edge is the front, and `CORE-002` answers "for infantry: the 4-stud side".

After this change `INF-001` states both, and cites CORE for the universal parts it consumes: the Unit Base's dimensions (`CORE-001`) and that a model has a facing at all (`CORE-002`).

**No value changes.** The base is still `4 × 3` studs and one plate. The front is still the 4-stud edge. What changes is which document a reader finds it in — and a reader of the infantry document now finds it there rather than two hops away.

## Decision 4 — `CORE-002`'s list of what facing determines goes

The rule listed six things: forward movement, rear movement, left side, right side, front firing arcs, rear firing arcs.

The first four are `MOVE-001`, which this repository rewrote a fortnight ago to say that **which directions a unit may move in is its own domain's rule** — infantry has four, a vehicle has two and turns between them. Leaving CORE's list in place restates the thing `MOVE-001` was corrected for saying.

**A list of what a rule is consumed for is a snapshot a command can print** (`system/documentation-standards.md`, How a Rule Is Written), and this one is already wrong for vehicles.

**The last two items are firing arcs, and they leave the ruleset.** A first draft pointed them at `11-combat.md`. That was wrong: `grep -rn "arc" docs/` finds the word only in `WPN-011` — "Weapon position determines firing arc", about mounted vehicle weapons — and in `09-transport.md`. **No rule ever defined a unit's front or rear arc**, what it spanned, or what it decided; `CORE-002`'s bullet list and the glossary sentence restating it were the whole of it, and neither said anything a player could apply.

Dropping them is therefore not a move, and this change does not pretend otherwise. Inventing an arc rule would be a gameplay addition; leaving a pointer at a document that does not answer would be a dangling reference wearing a citation. If arcs are wanted, they are Combat's to define, in their own change.

**No shorter version of the list survives either.** An earlier draft kept a two-item one — movement directions and arcs — which is the same defect at a third of the length. `MOVE-001` already cites `CORE-002` from the movement side, and that is the interface.

## Decision 5 — `CORE-015` is retired, and the shield goes to Components

`CORE-015` says a minifigure may only use equipment it can physically carry, gives the one-hand / two-hand guideline, and notes a shield is one-handed.

Its subject is minifigure hands. Infantry is a domain now, and weapons have been one since `10-weapons.md` was written — where `WPN-010` already reproduces the guideline and cites `CORE-015` as though the answer lived in CORE.

What is universal is `CORE-014`: equipment must be physically represented, and a unit cannot use what is not on the model. That stays, and it is the whole of what CORE needs to say about equipment.

**`CORE-014` does not absorb the first sentence, and an earlier draft claimed it did.** "A minifigure may only use equipment it can physically carry" is a carry-capacity constraint; `CORE-014` is a presence constraint. A repair tool a minifigure has no hand for is present and uncarriable, and only one of the two rules refuses it. The sentence goes to `INF-001` with the hand count, where its subject already lives.

**The hand count is stated once, in `INF-001`.** A first draft had `CMP-014` and `WPN-010` each assert "two hands" on their own authority, which is two owners for one fact — and by Decision 1's own test, hands are minifigure-only and the minifigure is Infantry's. Components and Weapons cite it for what they each need: one hand for a shield, one or two for a weapon.

**The shield goes to `CMP-014`, not to `WPN-010`.** A shield is not a weapon — it is cover, and cover is a component. `CMP-014` is already the shield rule, already states that a shield is defensive equipment attached to an infantry model, and already cites `CORE-015` for the hand. It absorbs the fact instead of pointing at a retired rule.

**Rejected: keeping `CORE-015` as a one-line pointer.** A rule whose whole body is a forwarding address is not a rule; it is a redirect that has to be maintained. The two citers are re-aimed and the number is retired.

## Decision 6 — No `openspec/specs/` delta

`system/proposal-review.md` ("Delta vs. Direct Edit"): a `MODIFIED` delta can only target a capability that already exists. `unit-base`, `action-economy` and `component-damage` are the capabilities in play, and no requirement or scenario in any of them stops being true — the Unit Base is unchanged, the Action Point economy is untouched, and no damage behaviour is involved.

Nothing here changes behaviour at all. This change moves sentences between documents.

**Note for whoever archives it:** a delta-free change archives by moving its directory, and until `archive-a-delta-free-change` merges, the `OpenSpec archive must be separate from apply` gate refuses that on its own. Batch it with a change that carries a delta, or archive it after that fix lands.

## Decision 7 — `CORE-009` keeps the principle and nothing else

The rule is one blockquote and one sentence. The sentence disclaims reaction fire and cites `CBT-014`.

`core-states-only-what-it-owns` compressed that sentence from a paragraph and deliberately kept its disclaiming form, arguing that an absolute prohibition would outrank the scenario extensions `CBT-010` and `FLOW-013` contemplate. **That reasoning was about the wording of a sentence that stayed.** Removing the sentence removes the prohibition and the disclaimer together, which raises neither problem: nothing in CORE then says anything about when a shot may be taken, and `FLOW-002` already states that activation is one unit at a time.

**The consequence is that `CBT-014` ends up cited by nothing**, and that is the right shape. It is Combat's list of what Combat has not built. A reader asking "is there reaction fire?" is asking a combat question, and `11-combat.md` answers it. Nothing needs to point at a list of absences from another document.

**Rejected: keeping the `CBT-014` citation alone**, as a bare "see also". It would keep a sentence in CORE whose only purpose is to stop `CBT-014` looking uncited, which is optimising for a script's shortlist rather than for a reader.

## Decision 8 — `CORE-006` stops banning a pricing scheme no rule uses

**Decided by the maintainer, against the recommendation this document first recorded.** The evidence for keeping the paragraph was put twice and did not persuade; what follows is the reasoning that won and what it costs, so that neither is rediscovered from scratch.

**The argument for removal:** a prohibition needs something to prohibit. Every action in the ruleset carries a flat cost written into the rule that charges it — 1 Action Point to move, to rotate, to attack per weapon system, to open any interactive element, to repair, to embark, to disembark. Nowhere is a cost multiplied by a footprint, a height or a Unit Base count. Stating that costs do not scale with size is an exception to a scheme the ruleset never establishes, and `system/documentation-standards.md` asks a rule to state what is, not what is not.

**The argument that lost, recorded because it is not weak.** The requirement was added by `2026-08-10-no-action-point-cost-scales-with-size`, and not prophylactically: `TRN-005` and `TRN-006` did price by Unit Base, and against a fixed 3 Action Point budget a four-Unit-Base unit could never embark and, once inside, never leave. That change rewrote both rules flat and added the principle. So the ruleset reads clean today **because** of the paragraph, and the case for keeping it is that the failure it prevents is a silent one — a model priced out rather than forbidden, discovered at the table.

**What decided it:** the two rules that once violated the principle now state their flat cost themselves. `TRN-005` says "an infantry model of one Unit Base and a motorcycle of two pay the same" in its own words; `TRN-006` says the cost is the same whatever the unit occupies. The correction survives in the rules that were corrected. What `CORE-006` added on top was a general ban and two citations pointing at it — and a general ban is exactly the shape that reads as an exception to something.

**What it costs, stated rather than minimised:**

- **A capability delta.** `openspec/specs/action-economy` carries `Requirement: Action Cost Does Not Scale With Size` with four scenarios. This change ships a `REMOVED` block for it, and it is the only part of the change that touches a capability at all.
- **The four scenarios still describe what happens.** An infantry model and a four-Unit-Base unit both spend 1 Action Point to embark — because `TRN-005` says 1 Action Point and says nothing about Unit Bases. The delta removes a requirement, not a behaviour.
- **What guards it now:** `CORE-006` fixes the allotment at 3 with no way to earn more, and every rule that charges writes its own price. A cost that grew with the model would have to be written into one of those rules, where it sits against the fixed budget in plain sight. That is a weaker guarantee than a stated ban, and it is the trade being made.

**The third sentence goes with the first two.** "A measurement may still decide **which** rule applies…" — added a day earlier, and correct — exists only to stop the ban being read too widely. With no ban, it qualifies nothing.

**Rejected: shortening the paragraph to one line** rather than deleting it. It was offered and declined. It would have kept the requirement, avoided the delta and removed the two worked examples that made the paragraph heavy — but it keeps the shape the objection is about, which is CORE stating a prohibition instead of the charging rules stating their prices.
