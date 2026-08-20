# Design — A Deployment Volume's floor is counted, not packed

## Decision 1 — Budget, not packing

This is the maintainer's decision, made on the case that separates the two readings. Both were live in the ruleset and neither had been stated.

**What each reading says about a `5 × 1 × 2 UB` Patrol game:**

| | Packing | Budget |
|---|---|---|
| The floor is | a rectangle five Unit Bases wide and one deep | five Unit Bases to spend |
| Infantry (`1 × 1`) | five fit | five, at one each |
| A Bike (`1 × 2 UB`) | **cannot be fielded** — two deep, the floor is one | costs two, three left over |
| A `2 × 1 UB` vehicle | fits — one deep. `VEH-028` allows either arrangement | costs two, the same |
| A rotated `4 × 6`-stud footprint | needs a rule for how it lands on the grid | costs the Unit Bases it covers, whichever way round |

**The second row is why the headline must be stated carefully.** An earlier draft of this design said no vehicle at all could be fielded in a Patrol game. `VEH-028` allows two Unit Bases side by side as readily as front to back, so a `2 × 1 UB` vehicle is one Unit Base deep and fits a `5 × 1` floor under either reading. #81's own wording — "no vehicle **deeper than one Unit Base**" — was the accurate one and is restored.

**The maintainer's reading, in their words:** five Unit Bases means five Unit Bases; a `1 × 2` motorcycle spends two and three remain for anything else, provided nothing stands taller than the agreed ceiling.

**The ruleset already leaned this way in the rule that does the arithmetic.** `DEP-003` states a vehicle's cost as a number — *"Vehicle dimensions: 2 × 5 UB. Deployment cost: 10 Unit Bases"* — and calls the result an area that "is unavailable for any other model". That is spending, not placing. What implied packing was `DEP-001`'s `W × D` notation and `DEP-002`'s "fits inside", neither of which is doing arithmetic.

**Why this is the better answer and not merely the chosen one:**

- A Deployment Volume is agreed **before the game** and limits what army you may bring. It is not a region of the table that models stand in during play — `FLOW-001` agrees it as a setup step and nothing places models inside it afterwards. A limit on composition is a budget.
- `DEP-002` is titled **Army Capacity**. Capacity is a quantity.
- Packing needs a rule this ruleset does not have and would not want: how a footprint whose studs do not divide evenly into `4 × 3` lands on a grid. `CODE_OF_DESIGN.md` Principle 11 — a subsystem where a count would do.
- Packing makes small games arbitrarily hostile. A `5 × 1 UB` floor admits no vehicle at all, and nothing in `DEP-009` warns a reader choosing Patrol that they have chosen an infantry-only game by accident.

**What packing had going for it**, recorded because it is not nothing: `DEP-001` writes two numbers and calls their product a floor, which is shape language; and Principle 1, The Model Is The Rules, is happiest when a limit is something you can see on the table. The answer to the second is that this limit is agreed in conversation before anything is on the table.

## Decision 2 — `W × D` stays, and now says what it produces

The obvious follow-on is to write the floor as one number and stop implying a rectangle. Rejected.

Two numbers carry information a single count does not: they tell players the *scale* of the game they are agreeing to, and `5 × 5` reads differently from `25 × 1` even where both are twenty-five Unit Bases. `DEP-001`'s examples use that — `4 × 4 UB`, `5 × 5 × 4 UB`, `10 × 10 × 6 UB` — and they communicate.

So the notation stays and the rule says what the notation yields: **the floor is their product, a count of Unit Bases.** `5 × 1` and `1 × 5` agree the same five, and a rule that says so closes the question the notation opens.

## Decision 3 — `DEP-002`'s examples are replaced, not trimmed

They read:

> A 5 × 5 × 4 UB Deployment Volume could contain: 25 infantry. **or** 1 large tank. **or** 2 medium vehicles. **or** 1 transport carrying infantry.

Under a budget every line after the first is wrong or unfalsifiable. Twenty-five Unit Bases do not buy *one* large tank — `DEP-003`'s own example vehicle is `2 × 5 UB`, so twenty-five buys two of those and five infantry besides. "2 medium vehicles" names no footprint and cannot be checked. And the "or" framing implies each line exhausts the volume, which is the packing reading arriving through the back door.

**Fourteen lines that teach the wrong model are worse than none.** The replacement is one worked sum, using footprints the ruleset already states, that a reader can verify against `DEP-003` and `DEP-004`.

This also settles the fat that `06-deployment.md` carries here — but the reason to replace them is that they are wrong, not that they are long.

## Decision 4 — One `MODIFIED` delta against `unit-base`

`openspec/specs/unit-base`'s **Unit Base Projections** requirement says the volume itself is read for "transport capacity, interior space, and the Deployment Volume a model must fit inside".

**That capability carried both readings, exactly as `docs/` did.** Its own scenario says a vehicle's Deployment cost "is read from the horizontal projection of the Unit Bases it covers, and its height is charged nothing" — a budget — while the requirement text has a model fitting inside a volume.

The delta changes the requirement's wording and **no scenario**. `scripts/check_delta_coverage.py` fails a `MODIFIED` block that drops a scenario the living spec has, so all four are reproduced unchanged.

Rejected: leaving the spec alone on the grounds that `docs/` is the source of truth. `openspec/specs/` is what the archive reads and what a future change deltas against; a requirement that contradicts the ruleset is a defect wherever it lives, and this one would have gone on quietly disagreeing.

## Decision 5 — `DEP-007`, `DEP-008` and `DEP-009` wait

All three are known findings. `DEP-008` closes with *"As long as the Deployment Volume is respected, all armies are legal"*, which is `DEP-002`'s own permission restated, and it cites nothing and is cited by nothing. `DEP-009` is four suggested volumes under a heading that decides nothing. `DEP-007` is a responsibility boundary.

**They wait because every one of them reads differently under the two answers above.** `DEP-009`'s Patrol preset is the case the readings disagree about. Deleting `DEP-008` for repeating `DEP-002` would have meant repeating whichever version of `DEP-002` the cleanup happened to assume — and the cleanup was drafted before anyone had noticed the question was open.

That sequencing error was nearly made. It is recorded here so the next document is approached the same way: **settle what a document means before removing what it says twice.**

## Decision 7 — `DEP-003` changes one sentence, because #81 said it would

The first draft of this proposal declared `DEP-003` untouched and called it "exactly right". **#81's record says otherwise**, in the same paragraph that recorded the question:

> Settling it is a mechanical change to `DEP-002` **and `DEP-003`**, not a rewording, so it needs its own proposal.

Most of `DEP-003` needed nothing — it states a cost as a number, which is the budget reading, and its double height bound is correct. But its closing sentence is *"This area is unavailable for any other model."*

**Under a budget there is no area and nothing is made unavailable.** Unit Bases are spent. That sentence was the last exclusion-of-space language in the chapter, and it was sitting in the rule this change nominates as the one that was always right — a residue of the exact ambiguity being removed, in the worst possible place for it.

It becomes *"Those Unit Bases are spent, and cannot be spent again."*

Rejected: leaving it, on the reading that "unavailable" already means spent. It does, to someone who has already decided the answer. To a reader arriving at `DEP-003` to find out, it describes a region.

## Decision 8 — `DEP-002` does not re-list what a model spends

`DEP-002` now says each model spends the Unit Bases of its footprint. It would read more helpfully with the two cases spelled out — one for infantry, its footprint for a vehicle.

Rejected, because `DEP-006` already carries that exact list for externally carried models: *"one Unit Base for an infantry model (DEP-004), its own footprint for a vehicle (DEP-003)"*. Adding it to `DEP-002` would make this change create the second copy, which is the failure class it is an instance of.

`DEP-003` and `DEP-004` state the two cases and `DEP-002` cites the floor it measures them against. That is the pointer, not the copy.

## Open — does a crew member add to the total?

**Recorded rather than answered, the way #81 recorded the question this change settles.**

The audit of the applied text was cut short by a session limit. It had confirmed every figure in the worked example against `VEH-001` and `VEH-028`, and was raising what it called "the crew question the new arithmetic exposes" when it stopped. What follows is what that reviewer's lead turns up on being followed — not the finding they were about to write, which nobody has.

With the floor stated as a budget, a reader adds numbers. The question they reach is whether a vehicle's Pilot and crew cost Unit Bases of their own.

**The answer is no, and it is derivable in one hop.** `VEH-013` says the Pilot "occupies a Unit Base of its own… This is why the minimum footprint is two Unit Bases (VEH-001) rather than one: at one, the Pilot is the whole vehicle." The Pilot is inside the footprint the vehicle already charges. `VEH-015` puts crew in the same place. And `DEP-006` states the principle outright for embarked units: "Their occupied space is the transport interior, not additional Deployment Volume."

**No rule states it in one place, and none contradicts another.** That makes it a clarity question rather than a defect, which is why it is not fixed here: this change already edits five places across two documents and carries a delta, and a sixth edit answering a question no rule gets wrong is scope this proposal did not set out with.

Where it would go, when someone takes it: `DEP-002` now states the arithmetic, so it is the rule that should say what does *not* enter into it.

## Decision 6 — the name stays

"Deployment Volume" was chosen deliberately by #81, over "Deployment Area", and is cited from `FLOW-001`, `FLOW-013`, `DEP-003`, `VEH-001`, `VEH-028` and the glossary.

A floor counted in Unit Bases, under a ceiling measured in Unit Bases, is still a volume — the models occupy it in three dimensions even where the *limit* on them is a count and a bound. What needed saying was how the floor is read. Renaming a term cited six times to fix a sentence is the wrong size of change.
