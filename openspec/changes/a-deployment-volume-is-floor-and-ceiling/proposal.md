# A Deployment Volume's floor is counted, not packed

## Why

`deployment-is-a-volume` (#81) left one question standing and wrote it down so it would be proposed rather than rediscovered:

> **Is the floor packed or budgeted?**
>
> - **Packing**: the floor is a shape, and a `1 × 2 UB` vehicle needs two Unit Bases of depth to sit in. `DEP-001`'s `W × D` framing implies this.
> - **Budget**: the floor is a count, and a `1 × 2 UB` vehicle costs 2 of the 25 a `5 × 5 UB` game holds. `DEP-003`'s "This area is unavailable for any other model" implies this.

Both readings are in the ruleset today, in rules that sit forty lines apart.

**They disagree about real armies.** `DEP-009`'s Patrol preset is `5 × 1 × 2 UB`. Under packing that floor is a rectangle one Unit Base deep, so **no vehicle deeper than one Unit Base can be fielded in a Patrol game** — a Bike is `1 × 2 UB` (`08-vehicles.md`, VEH-001) and does not fit. Under a budget it is five Unit Bases to spend: a Bike costs two and leaves three.

That is #81's own qualifier, and it is the accurate one: `VEH-028` allows two Unit Bases side by side as well as front to back, so a `2 × 1 UB` vehicle is one deep and fits either way.

Nothing in `docs/` decides which. A reader who assumes the wrong one builds an illegal army.

**The maintainer's decision: the floor is a budget.** Five Unit Bases means five Unit Bases, whatever shape they were agreed in.

The narrow purpose:

> **A Deployment Volume's floor is a number of Unit Bases. Each model spends the Unit Bases of its footprint, and an army is legal when the total does not exceed the floor and every model fits under the ceiling.**

## What Changes

Two ruleset documents and one capability. **No rule ID is retired or renumbered.**

- **`DEP-001`** — states that `W × D` is how the floor is *agreed*, and that the floor it agrees is their product: a count of Unit Bases. `5 × 1` and `1 × 5` are the same five. The ceiling `H` is unchanged and remains a bound rather than a price.
- **`DEP-002`** — stops saying an army must "fit inside" the Deployment Volume, which is the packing reading, and states the arithmetic instead: each model spends the Unit Bases of its footprint, and the total may not exceed the floor.
- **`DEP-002`'s examples** — replaced. The current four say a `5 × 5 × 4 UB` volume "could contain 25 infantry **or** 1 large tank **or** 2 medium vehicles", which under a budget is wrong twice over: it implies one tank exhausts twenty-five Unit Bases, and it never shows the addition a reader has to do. The replacement is arithmetic that checks out, using footprints the ruleset already names.
- **`docs/14-glossary.md`, the *Deployment Volume* entry** — "The battlefield space a player's army must fit inside" is the packing reading in the one place a reader looks the term up.
- **`openspec/specs/unit-base`, the *Unit Base Projections* requirement** — reads "the volume itself for transport capacity, interior space, and the Deployment Volume a model must fit inside". **That capability carries both readings too**, since its own scenario already says a vehicle's cost "is read from the horizontal projection … and its height is charged nothing". One `MODIFIED` delta, and no scenario changes.

## What Does Not Change

- **The ceiling.** `H` is agreed in whole Unit Bases, is compared against each model's own height, and is charged nothing. #81 settled that and this proposal does not reopen it.
- **`DEP-003`'s arithmetic.** It already states a cost as a number, and its paragraph bounding a vehicle's height twice is exactly right. **Its closing sentence does change**: "This area is unavailable for any other model" is the last exclusion-of-space language in the chapter, and #81 recorded that settling this question is "a mechanical change to `DEP-002` **and `DEP-003`**". That is task 1.4 — `design.md`, Decision 7.
- **`DEP-009`'s presets.** `5 × 1 × 2 UB` is five Unit Bases and a two-Unit-Base ceiling. The numbers do not move; this change is what makes them mean something definite.
- **`DEP-004`, `DEP-005`, `DEP-006`, `DEP-007`, `DEP-008`.** Untouched — see Out of Scope.
- **Every "must fit" elsewhere in the ruleset.** `TRN-019`, `VEH-015`, `WPN-020` and `DEP-004` all ask whether something physically fits *inside a vehicle or a footprint*. That is a physical check on the model and is a different question; grepped and confirmed.
- **`CHANGELOG.md` and every version header.** Release-cut-only.

## Checked elsewhere

- `python3 scripts/rule.py refs DEP-001 DEP-002 DEP-003` — `DEP-002` is cited by nothing; `DEP-001` by `FLOW-001`, `FLOW-013`, `DEP-003`, `VEH-001`, `VEH-028` and the glossary, every one of them for *that a volume is agreed* rather than for how its floor is read. `DEP-003`'s citers read it for footprint cost, which this change leaves alone.
- `grep -rn "fits inside\|fit inside\|must fit" docs/` — **eight hits.** Three are this change's subject; four are physical-fit checks inside a vehicle or a weapon footprint (`TRN-019`, `VEH-015`, `WPN-020`, **`DEP-005`** — not `DEP-004`, which ends four lines above it); and the eighth is the document Summary's "must fit under the agreed ceiling as well", which is a ceiling statement and correct as it stands.
- **`docs/01-foundations.md` was opened.** `system/proposal-review.md` names it as the document a rule-shaped sweep misses. Its line 85 — "Deployment Volumes are measured in UB, as a volume — a floor and a ceiling" — is clean under this reading and needs no task.
- **`openspec/specs/` grepped for the term**, which is how the `unit-base` requirement was found. `weapon-construction` also names Deployment Volume; its use is about a weapon's footprint and needs nothing.

## Out of Scope

- **`DEP-007`, `DEP-008` and `DEP-009`'s duplication.** `DEP-008` restates `DEP-002`'s permission and cites nothing; `DEP-009` is a table of suggestions; `DEP-007` is a boundary that decides nothing. All three are real and all three read differently under the two answers this proposal chooses between — **which is why they wait for it rather than ship with it.** Cleaning them first would have baked in a reading nobody had stated.
- **Renaming "Deployment Volume".** The name was chosen deliberately by #81 and is cited from five rules and the glossary. A floor counted in Unit Bases and a ceiling in Unit Bases is still a volume; what needed saying was how the floor is read, not what to call it.
- **How a rotated footprint sits on the grid.** #81 listed this as part of the same open question. Under a budget it stops being a question: a footprint costs the Unit Bases it covers whichever way round it is placed. Recorded here because the answer is "no rule needed", which is worth stating once.
