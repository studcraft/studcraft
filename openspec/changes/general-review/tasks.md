# Tasks — The ruleset states its rules and stops

## How to read this file

**Part A is already applied.** It was applied by hand, on this branch, before
this proposal existed (`design.md`, Decision 1). Its boxes are checked because
the work is in the tree, not because a task was followed. Each entry names what
to verify, so a reviewer can check the claim rather than take it.

**Part B is applied**, by `scripts/apply_tasks.py` rather than by hand — 46
anchor pairs across 17 files, in two runs. It is written as anchor pairs for
that reason: every anchor was checked with exact-substring matching and occurred
**exactly once in the file its task names**. One box is unticked, task 12.1, and
that is deliberate.

If an anchor returns anything other than 1, **stop and report it** rather than
guessing which occurrence was meant. Never edit a document to make a
verification command pass — report the mismatch instead.

### How to read the replacement blocks

The triple-backtick fence marks where the text starts and stops. **The fence is
not part of the text** — do not write the backticks into the document.

### Order matters

Edits apply in the order below, each against the result of the ones above it.
Several sections edit the same file.

### What Part B must not do

**No task here restores prose Part A removed.** Part B repairs what the
compression broke — a citation aimed at the wrong rule, a clause asserting a
retired rule, a heading at the wrong level — and where a repair had a
restore-it and a delete-it form, the delete-it form was chosen (sections 4
and 8).

**One task adds words, and it is three of them**: task 6.1 puts `Damage Roll`
back into `DMG-002`'s list, because leaving it out states a rule the ruleset
does not mean.

If a replacement block would remove a rule, change a number, or add a mechanic,
it is wrong — stop and report it.

**Sections 23, 27, 28, 29 and 31 are the exceptions, and all five are rule
changes rather than repairs.** They sit in Part C for that reason, the maintainer
decided all five, and `design.md` (Decisions 13 through 17) records the
reasoning. Nothing else in this file changes what a rule means.

---

# Part A — Applied

## A1. Prose compressed across all fifteen documents

- [x] Every `docs/*.md` rule that carried justification, worked-out reasoning or
      defensive qualification now states the rule and stops
      (`system/documentation-standards.md`, "How a Rule Is Written").
- [x] List markers unified, tables given headers, and `> **…**` used for the
      lines a rule benefits from a player being able to quote.
- [x] Verify no mechanic moved with the words: `python3 scripts/preflight.py`.

## A2. Twelve rule IDs retired

- [x] `CBT-010`, `MEL-004` — simultaneous resolution, a case no rule produces
      (`design.md`, Decision 6).
- [x] `MEL-010` — the ID-stability stub (`design.md`, Decision 10).
- [x] `GEO-006`, `GEO-007` — folded into `GEO-005`.
- [x] `WPN-013` — restated `CBT-001`. `WPN-017` — a list of weapon types that do
      not exist.
- [x] `VEH-028` — the footprint-derived height bound (`design.md`, Decision 4).
- [x] `DMG-009`, `DMG-010`, `DMG-011`, `DMG-018` — restatements of `DMG-008`,
      `WPN-006`, `CBT-005` and `CBT-007`.
- [x] Verify: `python3 scripts/check_id_stability.py main` reports no `moved`
      and no `reused`. Retirement is not reported by design — the twelve are
      listed in `proposal.md` instead.

## A3. `16-damage-system.md` renumbered

- [x] Eleven rules take the number below the one they had, closing the gaps the
      four deletions left. The full mapping is in `proposal.md`.
- [x] `design.md`, Decision 3 records that this breaks
      `system/documentation-standards.md` (Naming Conventions) and why it was
      chosen anyway.
- [x] Verify: `python3 scripts/rule.py doc 16-damage-system.md` lists
      `DMG-001` … `DMG-008`, `DMG-011` … `DMG-016`, `DMG-018`, with `DMG-009`,
      `DMG-010` and `DMG-017` the only gaps.

## A4. `08-vehicles.md` — height has one bound

- [x] `VEH-028` removed. `VEH-029` (where height is counted from) and `VEH-030`
      (what counts toward it) are unchanged and now feed the agreed ceiling
      alone (`06-deployment.md`, DEP-001).

## A5. `06-deployment.md` — `DEP-002` reads the floor as a placement

- [x] `DEP-002` states that an army is legal when every model can be physically
      placed inside the Deployment Volume at the same time, without overlapping.
- [x] `DEP-003`, `DEP-004`, `DEP-006` follow that reading: a footprint
      *occupies* Unit Bases rather than *spending* them.

`DEP-001` still carries one clause of the reading this replaced. That is task
1.1, not an A-item.

## A6. `03-game-flow.md` — the ASCII Turn Sequence is gone

- [x] The fenced diagram restated `FLOW-002` and `FLOW-003`; the document's
      Summary now carries the sequence as a numbered list.

## A7. Outside `docs/`

- [x] `assets/IMAGES.md` — the `VEH-028` row is removed with its rule, and the
      penetration row is rekeyed `DMG-017` → `DMG-016`.
- [x] `TODO.md` — its quoted-ruleset section matches the compressed text.
      Verify: `python3 scripts/check_todo_quotes.py`.
- [x] `cspell.json` — `rulebook` and `wargame` added.
- [x] `tests/test_ruleset_ast.py`, `tests/test_build_index.py` — repinned from
      named rules onto behaviour plus a whole-corpus invariant
      (`design.md`, Decision 8). Verify: `.venv/bin/pytest -q`.

---

# Part B — Owed

Every item came from a read-only audit of the applied text (`ruleset-auditor`,
`system/proposal-review.md`, "Review the Applied Text, Not Only the Diff").
Sections 1 and 2 are blockers.

## 1. `docs/06-deployment.md` — one clause contradicts `DEP-002` — BLOCKER

**The two rules do not disagree about their jobs.** `DEP-001` agrees the volume;
`DEP-002` says every model must be inside its floor and under its ceiling. That
division is right and stays.

**One clause disagrees**: "The floor is counted rather than treated as a shape"
denies that shape matters, and `DEP-002` makes physical placement the final
check, which is a question of shape. `DEP-009`'s Patrol floor is `5 × 1` — five
Unit Bases. A Buggy is `2 × 2 UB` (`08-vehicles.md`, VEH-001), four of them.
Counted, `4 ≤ 5` and it deploys. Placed, two Unit Bases of depth do not go into
a floor one deep.

**The second sentence of that line stays.** "A `5 × 1` floor and a `1 × 5` floor
both contain five Unit Bases" is true under both readings — congruent
rectangles, and turning the table is not a rule question.

- [x] 1.1 In `docs/06-deployment.md`, replace this anchor — the whole line:

```
The floor is counted rather than treated as a shape. A `5 × 1` floor and a `1 × 5` floor both contain five Unit Bases.
```

with:

```
A `5 × 1` floor and a `1 × 5` floor both contain five Unit Bases.
```

- [x] 1.2 In `docs/14-glossary.md`, replace this anchor — the *Deployment
      Volume* entry's body, which states the budget reading in the one place a
      reader looks the term up:

```
The limit on a player's army, agreed before the game and measured in Unit Bases: a floor of `W × D` Unit Bases to spend, and a ceiling `H` every model must stand under. See `06-deployment.md` (DEP-001).
```

with:

```
The limit on a player's army, agreed before the game and measured in Unit Bases: a floor of `W × D` Unit Bases every model must be placed within, and a ceiling `H` every model must stand under. See `06-deployment.md` (DEP-001).
```

- [x] 1.3 Read `DEP-001` through `DEP-004` and `DEP-008` end to end afterwards,
      not only the changed lines (`system/proposal-review.md`).

## 2. Citations that name the wrong rule — BLOCKER

Twenty-two lines, twenty-eight IDs, all consequences of the renumbering
(`design.md`, Decision 3). **The linter cannot see any of them**: it checks that
a cited ID exists, and every one of these does.

Two invert a rule rather than mislabelling it — tasks 2.2 and 2.10 both send a
reader asking *"can I target this?"* to Composite Vehicle Targeting, which says
an attack **may** assign Impacts to any visible component.

- [x] 2.1 In `docs/02-core-rules.md`, replace this anchor:

```
A transparent element does not block sight. It stops an Impact only through its own Resistance, like any other component (`16-damage-system.md`, DMG-008).
```

with:

```
A transparent element does not block sight. It stops an Impact only through its own Resistance, like any other component (`16-damage-system.md`, DMG-007).
```

- [x] 2.2 In `docs/02-core-rules.md`, replace this anchor:

```
A component that is completely hidden by terrain, another model or Visual Geometry cannot be selected as a target (`15-geometry-layers.md`, GEO-004; `16-damage-system.md`, DMG-012).
```

with:

```
A component that is completely hidden by terrain, another model or Visual Geometry cannot be selected as a target (`15-geometry-layers.md`, GEO-004; `16-damage-system.md`, DMG-011).
```

- [x] 2.3 In `docs/05-construction-components.md`, replace this anchor:

```
A shield protects only what it physically stands between: one interposed between the attacker and a component protects it (`16-damage-system.md`, DMG-007), one facing away blocks nothing. Orientation matters for that reason, not for any separate defensive bonus.
```

with:

```
A shield protects only what it physically stands between: one interposed between the attacker and a component protects it (`16-damage-system.md`, DMG-006), one facing away blocks nothing. Orientation matters for that reason, not for any separate defensive bonus.
```

- [x] 2.4 In `docs/08-vehicles.md`, replace this anchor:

```
The Pilot resolves Impacts as a normal component (`16-damage-system.md`, DMG-005).
```

with:

```
The Pilot resolves Impacts as a normal component (`16-damage-system.md`, DMG-002).
```

- [x] 2.5 In `docs/08-vehicles.md`, replace this anchor:

```
Beyond the threshold, roll one D6 for every complete brick (3 plate layers) of additional fall. Each roll is a Damage Roll (`16-damage-system.md`, DMG-015):
```

with:

```
Beyond the threshold, roll one D6 for every complete brick (3 plate layers) of additional fall. Each roll is a Damage Roll (`16-damage-system.md`, DMG-014):
```

- [x] 2.6 In `docs/10-weapons.md`, replace this anchor — two IDs on one line:

```
The effect of the Impact depends on the target's Resistance and the Geometry Check (`16-damage-system.md`, DMG-003, DMG-014), followed by the Damage Roll (DMG-015).
```

with:

```
The effect of the Impact depends on the target's Resistance and the Geometry Check (`16-damage-system.md`, DMG-003, DMG-013), followed by the Damage Roll (DMG-014).
```

- [x] 2.7 In `docs/11-combat.md`, replace this anchor — `DMG-017` does not
      exist:

```
See `16-damage-system.md`, DMG-012 through DMG-017.
```

with:

```
See `16-damage-system.md`, DMG-011 through DMG-016.
```

- [x] 2.8 In `docs/11-combat.md`, replace this anchor:

```
When a component is destroyed, it is physically removed according to the Universal Destruction rule (`16-damage-system.md`, DMG-006).
```

with:

```
When a component is destroyed, it is physically removed according to the Universal Destruction rule (`16-damage-system.md`, DMG-005).
```

- [x] 2.9 In `docs/11-combat.md`, replace this anchor:

```
Impact Strength (`10-weapons.md`, WPN-021) is derived from the physical size of the muzzle or striking end. It is used by the Damage System's Geometry Check (`16-damage-system.md`, DMG-014).
```

with:

```
Impact Strength (`10-weapons.md`, WPN-021) is derived from the physical size of the muzzle or striking end. It is used by the Damage System's Geometry Check (`16-damage-system.md`, DMG-013).
```

- [x] 2.10 In `docs/11-combat.md`, replace this anchor:

```
It only determines whether a component can be selected as a target (`02-core-rules.md`, CORE-010; `16-damage-system.md`, DMG-012).
```

with:

```
It only determines whether a component can be selected as a target (`02-core-rules.md`, CORE-010; `16-damage-system.md`, DMG-011).
```

- [x] 2.11 In `docs/11-combat.md`, replace this anchor:

```
A Wounded weapon (`16-damage-system.md`, DMG-005) still attacks, but each Attack Die is less reliable.
```

with:

```
A Wounded weapon (`16-damage-system.md`, DMG-002) still attacks, but each Attack Die is less reliable.
```

- [x] 2.12 In `docs/12-melee.md`, replace this anchor:

```
A melee attack may target any visible, physically reachable component, exactly like a ranged attack (`16-damage-system.md`, DMG-012).
```

with:

```
A melee attack may target any visible, physically reachable component, exactly like a ranged attack (`16-damage-system.md`, DMG-011).
```

- [x] 2.13 In `docs/12-melee.md`, replace this anchor — two IDs on one line:

```
Combat results should be represented on the LEGO model whenever possible, per the universal physical-representation principle (`02-core-rules.md`, CORE-016; `16-damage-system.md`, DMG-005, DMG-006).
```

with:

```
Combat results should be represented on the LEGO model whenever possible, per the universal physical-representation principle (`02-core-rules.md`, CORE-016; `16-damage-system.md`, DMG-002, DMG-005).
```

- [x] 2.14 In `docs/12-melee.md`, replace this anchor — the sentence describes
      the whole sequence, not penetration, and the Attack Roll now belongs to
      `11-combat.md`:

```
Every Impact — ranged or melee — then resolves through the exact same sequence: Attack Roll, Select Target Component, Geometry Check, Damage Roll, Component State Change, Penetration (`16-damage-system.md`, DMG-016). No separate damage system exists.
```

with:

```
Every Impact — ranged or melee — then resolves through the exact same sequence: Attack Roll (`11-combat.md`, CBT-005), then Select Target Component, Geometry Check, Damage Roll, Component State Change and Penetration (`16-damage-system.md`, DMG-008). No separate damage system exists.
```

- [x] 2.15 In `docs/14-glossary.md`, replace this anchor:

```
Passengers cannot be targeted directly; they are internal components the hull protects, reachable only if an Impact penetrates the hull with remaining strength (`09-transport.md`, TRN-010; `16-damage-system.md`, DMG-007, DMG-016).
```

with:

```
Passengers cannot be targeted directly; they are internal components the hull protects, reachable only if an Impact penetrates the hull with remaining strength (`09-transport.md`, TRN-010; `16-damage-system.md`, DMG-006, DMG-016).
```

- [x] 2.16 In `docs/14-glossary.md`, replace this anchor:

```
The three-state progression every component uses: `Operational`, `Wounded`, `Dead`. Universal — no component type has an exception. See `16-damage-system.md` (DMG-005).
```

with:

```
The three-state progression every component uses: `Operational`, `Wounded`, `Dead`. Universal — no component type has an exception. See `16-damage-system.md` (DMG-002).
```

- [x] 2.17 In `docs/14-glossary.md`, replace this anchor:

```
The step in damage resolution that compares an Impact's Strength against a component's Resistance; below Resistance, the Impact ends immediately with no further roll. See `16-damage-system.md` (DMG-014).
```

with:

```
The step in damage resolution that compares an Impact's Strength against a component's Resistance; below Resistance, the Impact ends immediately with no further roll. See `16-damage-system.md` (DMG-013).
```

- [x] 2.18 In `docs/14-glossary.md`, replace this anchor:

```
The die roll that follows a passed Geometry Check; on a 1, 2, or 3 the component's state advances by one step. See `16-damage-system.md` (DMG-015).
```

with:

```
The die roll that follows a passed Geometry Check; on a 1, 2, or 3 the component's state advances by one step. See `16-damage-system.md` (DMG-014).
```

- [x] 2.19 In `docs/14-glossary.md`, replace this anchor — the closing sentence
      of the *Wounded* entry:

```
A Wounded infantry model is placed seated, which is how the state is shown on the model. See `16-damage-system.md`, DMG-005.
```

with:

```
A Wounded infantry model is placed seated, which is how the state is shown on the model. See `16-damage-system.md`, DMG-002.
```

- [x] 2.20 In `docs/14-glossary.md`, replace this anchor — the closing sentence
      of the *Step* entry:

```
Not to be confused with a stair's step (INF-009) or with a Component State advancing one step (`16-damage-system.md`, DMG-005).
```

with:

```
Not to be confused with a stair's step (INF-009) or with a Component State advancing one step (`16-damage-system.md`, DMG-002).
```

- [x] 2.21 In `docs/17-infantry.md`, replace this anchor:

```
The first brick (3 plate layers) causes no damage. For every complete brick beyond the first, roll 1D6 as a Damage Roll (`16-damage-system.md`, DMG-015).
```

with:

```
The first brick (3 plate layers) causes no damage. For every complete brick beyond the first, roll 1D6 as a Damage Roll (`16-damage-system.md`, DMG-014).
```

- [x] 2.22 In `docs/17-infantry.md`, replace this anchor:

```
A Wounded infantry model (`16-damage-system.md`, DMG-005) moves **at most two steps** in whichever direction it travels.
```

with:

```
A Wounded infantry model (`16-damage-system.md`, DMG-002) moves **at most two steps** in whichever direction it travels.
```

- [x] 2.23 Verify: `python3 scripts/rule.py orphans` no longer reports
      `DMG-011 Select Target Component` or `DMG-013 Geometry Check`, and
      `python3 scripts/rule.py show DMG-002` reports inbound citations. All
      three have none today, because every citation meant for them names a
      neighbour.

## 3. `docs/08-vehicles.md` — `VEH-028` is retired and still asserted

`docs/06-deployment.md` states "Vehicle height is not determined by its
footprint". Until these land, one of the two documents is simply false.

- [x] 3.1 In `docs/08-vehicles.md`, replace this anchor:

```
There is no maximum footprint size. A vehicle's footprint determines its maximum height (VEH-028), while the Deployment Volume provides an additional ceiling (`06-deployment.md`, DEP-001).
```

with:

```
There is no maximum footprint size. A vehicle's height is bounded by the agreed Deployment Volume ceiling (`06-deployment.md`, DEP-001).
```

- [x] 3.2 In `docs/08-vehicles.md`, replace this anchor — "its own limits" meant
      `VEH-028`'s two bounds:

```
A vehicle carried inside another vehicle is measured as it would stand on its own, against its own limits (`09-transport.md`, TRN-001, TRN-003).
```

with:

```
A vehicle carried inside another vehicle is measured as it would stand on its own, against the agreed Deployment Volume ceiling (`06-deployment.md`, DEP-001; `09-transport.md`, TRN-001, TRN-003).
```

- [x] 3.3 In `docs/08-vehicles.md`, replace this anchor — the Summary line:

```
Height is determined by the vehicle's footprint and the Deployment Volume ceiling.
```

with:

```
Height is bounded by the agreed Deployment Volume ceiling.
```

- [x] 3.4 Verify no `VEH-028` remains in the ruleset:
      `grep -rn "VEH-028" docs/ assets/`.

## 4. `docs/12-melee.md` — a Summary asserting a retired rule

`MEL-004` and `CBT-010` are both retired, so no rule states this. **Delete the
bullet; do not restate the rule** (`design.md`, Decision 6) — a player asking
"does my target strike back?" is answered by `FLOW-002` and `CBT-001`, and
nothing grants a reaction for a rule to deny.

- [x] 4.1 In `docs/12-melee.md`, replace this anchor — two Summary bullets:

```
- A Wounded weapon still generates that die and reads it worse — as does a Wounded minifigure attacking unarmed, the one attack whose weapon system is the attacker (MEL-008; `11-combat.md`, CBT-015).
- A melee attack is one unit's own action — it never grants the target a free counter-attack (MEL-004).
```

with:

```
- A Wounded weapon still generates that die and reads it worse — as does a Wounded minifigure attacking unarmed, the one attack whose weapon system is the attacker (MEL-008; `11-combat.md`, CBT-015).
```

- [x] 4.2 Verify nothing else asserts it: `grep -rn "counter-attack" docs/`.

## 5. `docs/11-combat.md` — a pointer to a rule that no longer exists

`DMG-018` is Repairs, and `CBT-007` states the split rule in full immediately
above, so the pointer is wrong and redundant at once.

- [x] 5.1 In `docs/11-combat.md`, replace this anchor — the last bullet and the
      line below it:

```
* The attack still costs the single Action Point for that weapon system.

See `16-damage-system.md`, DMG-018, Weapon Distribution.
```

with:

```
* The attack still costs the single Action Point for that weapon system.
```

## 6. `docs/16-damage-system.md` — `DMG-002` omits the Damage Roll

`specs/component-damage/spec.md` keeps "Resistance, Impact Strength, **the
Damage Roll**, Unit Base occupancy, footprint, transport capacity and Action
Point costs" unchanged for a `Wounded` component. The list omits the Damage
Roll, which reads as an opening the spec does not have.

- [x] 6.1 In `docs/16-damage-system.md`, replace this anchor — the head of the
      unchanged-properties list:

```
* Resistance
* Impact Strength
* Footprint
```

with:

```
* Resistance
* Impact Strength
* The Damage Roll rolled against it
* Footprint
```

## 7. `assets/IMAGES.md` — one pass

- [x] 7.1 In `assets/IMAGES.md`, replace this anchor — the composite-targeting
      row is keyed to a number that is now the Geometry Check:

```
| DMG-013 | `assets/images/dmg-013-composite-targeting.png` |
```

with:

```
| DMG-012 | `assets/images/dmg-012-composite-targeting.png` |
```

- [x] 7.2 In `assets/IMAGES.md`, replace this anchor:

```
- **DMG-007 (Internal Components)** — Introduces the "Armour → Pilot" concept that DMG-017's image already resolves mechanically; a separate diagram would repeat it.
- **DMG-018 (Weapon Distribution)** — Whether a mount rotates is a binary construction check made directly on the model, not something prose obscures.
```

with:

```
- **DMG-006 (Internal Components)** — Introduces the "Armour → Pilot" concept that DMG-016's image already resolves mechanically; a separate diagram would repeat it.
- **CBT-007 (Multiple Targets)** — Whether a mount rotates is a binary construction check made directly on the model, not something prose obscures.
```

- [x] 7.3 In `assets/IMAGES.md`, replace this anchor:

```
Closed Transport's "impact continues toward internal passengers" is the same mechanism as DMG-017's image, not a new one.
```

with:

```
Closed Transport's "impact continues toward internal passengers" is the same mechanism as DMG-016's image, not a new one.
```

- [x] 7.4 In `assets/IMAGES.md`, replace this anchor — both rejection reasons
      rest on an image row this change deleted with its rule:

```
- **TRN-020 (Interior Levels)** — The stacking is arithmetic on a height the CORE-001 image already dimensions: one Unit Base of clear height per level, plus a plate for each floor above the lowest. How many levels fit is then a comparison against whichever of VEH-028's two bounds is lower, both of which the VEH-028 image draws, so nothing is left for a picture to settle.
```

with:

```
- **TRN-020 (Interior Levels)** — The stacking is arithmetic on a height the CORE-001 image already dimensions: one Unit Base of clear height per level, plus a plate for each floor above the lowest. How many levels fit is then a comparison against the agreed Deployment Volume ceiling, which is a number the players chose rather than a geometry a picture can settle.
```

- [x] 7.5 In `assets/IMAGES.md`, replace this anchor:

```
What DEP-003 charges is that floor; the two height bounds it feeds one of are drawn in VEH-028's image, not in a second one here.
```

with:

```
What DEP-003 occupies is that floor; height is checked separately against the agreed ceiling and needs no image of its own.
```

- [x] 7.6 In `assets/IMAGES.md`, replace this anchor — the "fourth notation"
      paragraphs record a defect that no longer exists. No `○` remains anywhere
      in `docs/`, and `DMG-010` is retired:

```
There is a fourth notation outside this document. `16-damage-system.md` writes a two-muzzle shotgun as `` `○ ○` `` in DMG-010 and DMG-016 — a hollow circle where WPN-020 uses a filled `●` for the same thing.

**That one is not an image job.** It appears inline, mid-sentence, twice, and an inline image would read worse than the text does. The fix is to write "a shotgun with two muzzles" in words and drop the glyph, which removes the fourth notation without adding anything. Recorded here because it surfaced from the same scan, and because someone tidying the weapon grids will otherwise leave it behind as the last inconsistent one. It needs its own change: `docs/16-damage-system.md` is the ruleset, so it needs a proposal.
```

with:

```
The remaining notations are the three above. A fourth — a hollow `○` for a muzzle, where WPN-020 uses a filled `●` — is gone from the ruleset along with the rules that carried it.
```

- [x] 7.7 In `assets/IMAGES.md`, replace this anchor — the count is one high
      since `VEH-028`'s row went (`system/proposal-review.md`, "Verify the
      Number"):

```
**23 images** specified, across 8 of the 15 ruleset documents
```

with:

```
**22 images** specified, across 8 of the 15 ruleset documents
```

- [x] 7.8 In `assets/IMAGES.md`, replace this anchor — the cross-reference
      points at the bullet task 7.2 rekeyed, and `DMG-018` is now Repairs:

```
This list already declines DMG-018 as "a binary construction check made directly on the model"
```

with:

```
This list already declines CBT-007 as "a binary construction check made directly on the model"
```

- [x] 7.9 Verify: `grep -c "^| .*assets/images/" assets/IMAGES.md` reports `22`,
      and `grep -rn "DMG-017\|DMG-018\|VEH-028" assets/IMAGES.md` returns
      nothing.

## 8. `MEL-010` was the one sanctioned stub — five files still say so

`MEL-010` stays deleted (`design.md`, Decision 10). **Five** files outside
`docs/` name it as a worked example of a number kept because its rule merged
into another, and all five are now false. `CBT-011` and `WPN-021` are the
better example anyway: they keep a number *and a live rule*.

This section said "three" and listed three when it was first written. Tasks 8.4
and 8.5 are the two it missed, found by task 8.6's grep on the first run — the
grep is the reason the section is now right, and it stays.

- [x] 8.1 In `system/documentation-standards.md`, replace this anchor:

```
A rule may be deleted. Its number is retired, never reissued, and no stub is
left in its place — the diff records that the rule was there. `MEL-010` is the
one stub, a number kept because its rule merged into another. Where the rule
stays and only its design was superseded, the note goes inside that rule:
`CBT-011` and `WPN-021` (`system/proposal-review.md`).
```

with:

```
A rule may be deleted. Its number is retired, never reissued, and no stub is
left in its place — the diff records that the rule was there. Where the rule
stays and only its design was superseded, the note goes inside that rule:
`CBT-011` and `WPN-021` (`system/proposal-review.md`).
```

- [x] 8.2 In `system/workflow.md`, replace this anchor:

```
same convention `MEL-010` and `CBT-011` follow in the ruleset.
```

with:

```
same convention `CBT-011` and `WPN-021` follow in the ruleset.
```

- [x] 8.3 In `scripts/check_delta_coverage.py`, replace this anchor — the
      docstring:

```
keep the name and correct the body — the same stable-identifier convention
MEL-010 and CBT-011 follow in the ruleset itself.
```

with:

```
keep the name and correct the body — the same stable-identifier convention
CBT-011 and WPN-021 follow in the ruleset itself.
```

- [x] 8.4 In `system/proposal-review.md`, replace this anchor:

```
recur for a reader of the ruleset, in the rule itself. `MEL-010`, `CBT-011` and
`WPN-021` keep the superseded thing visible and say why, rather than leaving a
clean surface that invites the same suggestion again.
```

with:

```
recur for a reader of the ruleset, in the rule itself. `CBT-011` and `WPN-021`
keep the superseded thing visible and say why, rather than leaving a clean
surface that invites the same suggestion again.
```

- [x] 8.5 In `.claude/agents/ruleset-auditor.md`, replace this anchor:

```
IDs are permanent — never renumbered, never reused. A superseded rule keeps its number and carries a note saying so (`MEL-010`, `CBT-011`, `WPN-021`). The `13-*.md` gap is deliberate for the same reason. Report any renumbering, any reuse, any gap that is not.
```

with:

```
IDs are permanent — never renumbered, never reused. A superseded rule keeps its number and carries a note saying so (`CBT-011`, `WPN-021`). The `13-*.md` gap is deliberate for the same reason. Report any renumbering, any reuse, any gap that is not.
```

- [x] 8.6 Verify: `grep -rn "MEL-010" README.md CODE_OF_DESIGN.md
      CONTRIBUTING.md TODO.md system/ scripts/ docs/ .claude/` returns nothing.
      `openspec/changes/archive/` is history and is left alone
      (`system/proposal-review.md`).

## 9. `docs/14-glossary.md` — *Component* cites rules that do not carry its claims

Neither `DMG-001` nor `DMG-002` mentions Hit Points, and neither defines
Resistance — `DMG-003` does.

- [x] 9.1 In `docs/14-glossary.md`, replace this anchor:

```
A single visible physical part of a model that combat targets independently (Pilot, Door, Wheel, Weapon, Track, and similar). Components have no Hit Points — only a Component State and a Resistance, both read from the model. See `16-damage-system.md` (DMG-001, DMG-002).
```

with:

```
A single visible physical part of a model that combat targets independently (Pilot, Door, Wheel, Weapon, Track, and similar). Components have no Hit Points — only a Component State and a Resistance, both read from the model. See `16-damage-system.md` (DMG-001, DMG-002, DMG-003).
```

## 10. `docs/17-infantry.md` — `Design Philosophy` is at `##`

The pass demoted it, so it nests inside `# Purpose` rather than standing as one
of the four required skeleton sections (`system/documentation-standards.md`,
"Documentation Guidelines"). The linter matches the heading text and does not
see the level.

- [x] 10.1 In `docs/17-infantry.md`, replace this anchor:

```
## Design Philosophy

Infantry has no movement statistic.
```

with:

```
# Design Philosophy

Infantry has no movement statistic.
```

## 11. `scripts/build_index.py` — a comment whose example no longer exists

The comment names `11-combat.md`'s Combat Flow as a fence containing rule IDs.
That fence no longer names any, and **no fence in `docs/` does** — verified by
walking every fenced block in the AST. The behaviour the comment defends is
unchanged and still deliberate; only its example is dead.

- [x] 11.1 In `scripts/build_index.py`, replace this anchor:

```
        # `body` includes fenced content, deliberately: a rule named inside a
        # fenced diagram *is* referenced by that document — 11-combat.md's
        # Combat Flow names DMG-012 through DMG-017 in a fence, and that is
        # the map of the procedure, not an example of syntax. This is now
```

with:

```
        # `body` includes fenced content, deliberately: a rule named inside a
        # fenced diagram *is* referenced by that document — a flow diagram
        # naming the rules it sequences is the map of the procedure, not an
        # example of syntax. No fence in docs/ names one today; the inclusion
        # is what keeps the next one counted. This is now
```

## 13. `scripts/` must not name a live rule

**A script's behaviour never depends on a rule — verified by reading every
match of `[A-Z]{2,6}-[0-9]{3}` in `scripts/`.** Every one is in a comment, a
docstring or a `--help` line. The only rule-shaped thing in the code is the ID
*pattern* (`repo.RULE_ID_RE`), which is generic, and no checker, index or parser
branches on an ID.

**The illustrations are the exposure.** A comment naming `DMG-019` or `WPN-016`
is a dependency on a rule that can be retired, renumbered or reworded, and three
of them had already rotted before this section was written — one of them,
`build_index.py`'s, was repaired in section 11 without the class behind it being
named.

The rule this section installs: **a script may illustrate freely, and never with
an ID that exists.** Invented prefixes (`AAA-`, `BBB-`) cannot rot, and neither
can a placeholder. An invented *number* under a real prefix — `VEH-099`,
`WPN-999` — is equally safe and is left as it stands.

Out of scope, and worth deciding separately: comments naming a document
filename. `04-construction-standard.md` and `13-materials.md` were both removed,
so those can rot too, but a docstring describing the corpus reads worse without
them.

**`apply_tasks.py --check` reports this task as `skip`, and that is correct.**
Its anchor is a *prefix* of its own replacement — the new paragraph is appended
after it — so the anchor is still in the file after the edit lands, and the
script cannot tell an applied task from an unapplied one. It says so and refuses
to guess. The tick is right; the edit is in the file. An anchor that survives
its own replacement is the thing to avoid next time: extend it to include the
line *after* the insertion point.

- [x] 13.1 In `system/documentation-standards.md`, replace this anchor —
      installing the constraint where rule-ID stability already lives, so this
      does not have to be rediscovered from rotted comments a third time:

```
Image filenames are a separate namespace owned by `assets/IMAGES.md`.
`scripts/lint_ruleset.py` checks them against that convention and against the
rule IDs in `docs/`.
```

with:

```
Image filenames are a separate namespace owned by `assets/IMAGES.md`.
`scripts/lint_ruleset.py` checks them against that convention and against the
rule IDs in `docs/`.

**A script never names a rule that exists**, in code, comment, docstring or
`--help` text. No script's behaviour depends on one — the only rule-shaped
thing in `scripts/` is `repo.RULE_ID_RE` — and an illustration that names a
live ID is a dependency on a rule that can be retired or renumbered. Illustrate
with an invented prefix (`AAA-001`, `BBB-002`), a placeholder, or an invented
number under a real prefix (`VEH-099`): none of the three can rot. `tests/`
follows the same convention, and for the same reason.
```

- [x] 13.2 In `scripts/lint_ruleset.py`, replace this anchor — the docstring's
      four examples, one of which describes text no longer in `06-deployment.md`:

```
- Duplicate rule IDs within a document (e.g. two `# WPN-002` headers).
- Rule IDs that aren't strictly increasing within their document.
- Cross-document rule references that point at an ID which doesn't exist
  in the target document, in both of the forms this repo writes:
  the parenthesised "`10-weapons.md` (WPN-002)" and the comma form
  "`08-vehicles.md`, VEH-013", including comma-separated runs of IDs.
  A parenthesised ID carrying the citing document's own prefix is
  checked against that document instead of against the filename that
  happens to precede it — each document owns its namespace, so
  "`09-transport.md`, TRN-001), ... its own Unit Base (DEP-004)" in
  06-deployment.md is a reference to DEP-004 and not a broken one into
  09-transport.md.
```

with:

```
- Duplicate rule IDs within a document (e.g. two `# AAA-002` headers).
- Rule IDs that aren't strictly increasing within their document.
- Cross-document rule references that point at an ID which doesn't exist
  in the target document, in both of the forms this repo writes:
  the parenthesised "`nn-other.md` (AAA-002)" and the comma form
  "`nn-other.md`, AAA-013", including comma-separated runs of IDs.
  A parenthesised ID carrying the citing document's own prefix is
  checked against that document instead of against the filename that
  happens to precede it — each document owns its namespace, so
  "`nn-other.md`, AAA-001), ... its own Unit Base (BBB-004)" in the
  document owning `BBB-` is a reference to BBB-004 and not a broken one
  into `nn-other.md`.
```

- [x] 13.3 In `scripts/lint_ruleset.py`, replace this anchor — three live IDs
      in one comment, and `DMG-019` no longer exists at all:

```
# The comma form — "`08-vehicles.md`, VEH-013" — is what this repo writes most,
# and until this existed nothing checked it: roughly two thirds of the citations
# in docs/ were never verified by any script. A citation may name several IDs in
# a run ("`02-core-rules.md`, CORE-008, CORE-009"), so capture the whole run and
# split it afterwards. The run stops at the first thing that isn't an ID, which
# is what keeps "`16-damage-system.md`, DMG-019, Repairs)" from swallowing the
# word Repairs.
```

with:

```
# The comma form — "`nn-other.md`, AAA-013" — is what this repo writes most,
# and until this existed nothing checked it: roughly two thirds of the citations
# in docs/ were never verified by any script. A citation may name several IDs in
# a run ("`nn-other.md`, AAA-008, AAA-009"), so capture the whole run and
# split it afterwards. The run stops at the first thing that isn't an ID, which
# is what keeps "`nn-other.md`, AAA-019, Repairs)" from swallowing the
# word Repairs.
```

- [x] 13.4 In `scripts/lint_ruleset.py`, replace this anchor:

```
        # "Terrain Movement (MOVE-009 – MOVE-011)" — is the unnumbered case and
```

with:

```
        # "Terrain Movement (AAA-009 – AAA-011)" — is the unnumbered case and
```

- [x] 13.5 In `scripts/lint_ruleset.py`, replace this anchor:

```
            # filename and the ID, which is what lets "see `10-weapons.md`
            # (WPN-002)" and a continuation form, where a second bare ID follows
```

with:

```
            # filename and the ID, which is what lets "see `nn-other.md`
            # (AAA-002)" and a continuation form, where a second bare ID follows
```

- [x] 13.6 In `scripts/ruleset_ast.py`, replace this anchor — the module
      docstring's example of the bug this module fixed:

```
heading pattern of its own, `scripts/rule.py show DEP-009` included.
```

with:

```
heading pattern of its own — any rule carrying scenario sub-headings was
printed without them.
```

- [x] 13.7 In `scripts/ruleset_ast.py`, replace this anchor:

```
# The em dash is required here: a heading like "## DMG-005 States" (no em
```

with:

```
# The em dash is required here: a heading like "## AAA-005 States" (no em
```

- [x] 13.8 In `scripts/ruleset_ast.py`, replace this anchor — the field
      comments:

```
    rule_id: str | None  # "MOVE-012" when this heading is a rule header
    rule_prefix: str | None  # "MOVE"
    rule_number: int | None  # 12
    rule_title: str | None  # "Slopes"
```

with:

```
    rule_id: str | None  # "AAA-012" when this heading is a rule header
    rule_prefix: str | None  # "AAA"
    rule_number: int | None  # 12
    rule_title: str | None  # the text after the em dash
```

- [x] 13.9 In `scripts/build_index.py`, replace this anchor — the example is
      true today, which is exactly what makes it a dependency:

```
    `06-deployment.md`'s DEP-009 is exactly that case: four `##` scenarios
    that must not appear as chapters or as rules.
```

with:

```
    A rule presenting several worked scenarios as `##` sub-headings is exactly
    that case: they must not appear as chapters or as rules.
```

- [x] 13.10 In `scripts/check_delta_coverage.py`, replace this anchor:

```
keep the name and correct the body — the same stable-identifier convention
CBT-011 and WPN-021 follow in the ruleset itself.
```

with:

```
keep the name and correct the body — the same stable-identifier convention the
ruleset itself follows, where a rule whose design was superseded keeps its
number and carries a note saying so.
```

- [x] 13.11 In `scripts/check_todo_quotes.py`, replace this anchor — the
      example quotes a sentence this change deleted from the ruleset:

```
    `future` / `not yet defined` finds passages that declare no gap at all
    (`WPN-016`'s "allowing future expansion" is a closing remark that
    declares nothing). Telling those apart means
    reading the sentence, which belongs to `ruleset-auditor`, not to a regex.
```

with:

```
    `future` / `not yet defined` finds passages that declare no gap at all —
    a closing remark that future supplements may extend something declares
    nothing a reader can act on. Telling those apart means reading the
    sentence, which belongs to `ruleset-auditor`, not to a regex.
```

- [x] 13.12 In `scripts/rule.py`, replace this anchor — the `--help` examples:

```
  rule.py show VEH-013        the rule itself, as it reads in docs/
  rule.py refs VEH-013        every rule that cites it — the inverse graph
  rule.py neighbors VEH-013   what sits either side of it in its document
  rule.py touched <change>    every rule an OpenSpec change names
  rule.py orphans             rules nothing cites and no glossary entry defines
  rule.py glossary            glossary entries that point at no rule
  rule.py doc 08-vehicles.md  a document's chapters and rules, first sentence too
```

with:

```
  rule.py show <ID>           the rule itself, as it reads in docs/
  rule.py refs <ID>           every rule that cites it — the inverse graph
  rule.py neighbors <ID>      what sits either side of it in its document
  rule.py touched <change>    every rule an OpenSpec change names
  rule.py orphans             rules nothing cites and no glossary entry defines
  rule.py glossary            glossary entries that point at no rule
  rule.py doc <document.md>   a document's chapters and rules, first sentence too
```

- [x] 13.13 In `scripts/rule.py`, replace this anchor:

```
  rule.py show CORE-002 CORE-006 FLOW-002 FLOW-003 FLOW-004
```

with:

```
  rule.py show <ID> <ID> <ID> <ID> <ID>
```

- [x] 13.14 In `scripts/tasks_format.py`, replace this anchor:

```
    - [ ] 2.1 In `CMP-001`, replace this anchor — the whole rule body:
```

with:

```
    - [ ] 2.1 In `AAA-001`, replace this anchor — the whole rule body:
```

- [x] 13.15 In `scripts/verify_tasks.py`, replace this anchor:

```
    as often on the second as on the first — "before: **2** (TRN-005's sentence
```

with:

```
    as often on the second as on the first — "before: **2** (AAA-005's sentence
```

- [x] 13.16 Verify no live rule ID is left in `scripts/`. Every remaining match
      must be an invented prefix (`AAA-`, `BBB-`) or an invented number under a
      real one (`VEH-099`):
      `grep -rn "[A-Z]\{2,6\}-[0-9]\{3\}" scripts/`

- [x] 13.17 Verify the suite still passes and the linter still catches what
      these comments describe: `.venv/bin/pytest -q` and
      `python3 scripts/preflight.py`. **No test asserts on a docstring**, so a
      green suite here is evidence the edits were comment-only.

- [x] 13.18 In `.claude/rules/tooling.md`, replace this anchor — the constraint
      13.1 installs is in `system/documentation-standards.md`, but nothing loads
      it at the moment it applies. `.claude/rules/tooling.md` has
      `paths: scripts/*.py`, so it is what an agent editing a script reads. It
      routes to the owner; it does not restate the rule
      (`system/documentation-standards.md`, "What `system/` Is For"):

```
- `system/documentation-standards.md` — Repository Structure, and how a rule is
  written. A new script states its own job in its docstring; the structure
  table names directories, not files.
```

with:

```
- `system/documentation-standards.md` — Repository Structure, how a rule is
  written, and Naming Conventions: **a script never names a rule that exists**,
  in code, comment, docstring or `--help`. A new script states its own job in
  its docstring; the structure table names directories, not files.
```

- [x] 13.19 Verify the routing reaches it: `.claude/rules/tooling.md` names
      `system/documentation-standards.md`, and that document states the
      constraint. Re-run `python3 scripts/preflight.py`.

## 14. Two defects this change is responsible for

Both found after section 13 landed. Neither needs a proposal of its own: this
branch *is* the general-fix branch, and splitting a one-line correction out of
the change that caused it buys nothing.

### 14.1 is a false sentence this change wrote

Task 13.1 closed the new constraint with "`tests/` follows the same convention,
and for the same reason". **It does not.** `tests/` names `VEH-001` in five
files, plus `CORE-010`, `TRN-005`, `WPN-021`, `VEH-013` and `INF-001`; only
`test_rule.py` uses `AAA-`/`BBB-`.

**The claim was wrong, and the reasoning under it was wrong too.** The suite
survived a pass that retired twelve rules — but not because its fixtures avoid
live IDs. It survived because **a fixture defines its own document**: a
`# VEH-001` inside a test's own markdown string does not read the real rule, it
invents one wearing that name. There is no dependency to remove.

**Rejected: renaming the fixtures to `AAA-`/`BBB-`.** Fifty edits that remove no
dependency, in files where the ID is already local by construction. The two
tests that genuinely *did* depend on `docs/` were repaired in Part A
(`design.md`, Decision 8), and that was the real exposure.

- [x] 14.1 In `system/documentation-standards.md`, replace this anchor:

```
number under a real prefix (`VEH-099`): none of the three can rot. `tests/`
follows the same convention, and for the same reason.
```

with:

```
number under a real prefix (`VEH-099`): none of the three can rot.

`tests/` is not held to this. A test fixture defines its own document, so an ID
inside one is local by construction and names nothing in `docs/`. What a test
must not do is reach into `docs/` for a *real* rule — that is the dependency,
and it is what `tests/test_ruleset_ast.py` and `tests/test_build_index.py` were
repaired for.
```

### 14.2 is older than this branch, in a file this change already edits

`docs/08-vehicles.md` has an unclosed code span: `` `VEH-022` through
`VEH-024). `` — the closing backtick before the parenthesis is missing, so the
rendered text runs the span into the rest of the line. It predates this branch
and no task in sections 1–13 names the line.

**Taken here anyway**, because this change edits `08-vehicles.md` five times and
leaving a known broken span in a file being repaired is a worse diff than the
one extra character. Recorded rather than slipped in: a reader comparing the
task list against the diff should find every edit accounted for.

- [x] 14.2 In `docs/08-vehicles.md`, replace this anchor:

```
Terrain capability is still read from the relevant locomotion component (`VEH-022` through `VEH-024).
```

with:

```
Terrain capability is still read from the relevant locomotion component (`VEH-022` through `VEH-024`).
```

- [x] 14.3 Verify: `python3 scripts/preflight.py` and `.venv/bin/pytest -q`
      both green, and `grep -n "VEH-024" docs/08-vehicles.md` shows the span
      closed.

## 15. The gate that would have caught section 13, and one dead exemption

Two script changes, each with its test in the same commit
(`.claude/rules/tooling.md`).

### What is *not* here, and why

**`scripts/check_id_stability.py` should report a `retitled` ID** — one present
in both revisions whose rule *title* changed. That is renumbering in place, it
is purely mechanical, and it would have flagged all eleven `DMG-*` shifts on the
first run instead of the twenty-eight broken citations they produced. It is the
highest-value check missing from this repository.

**It cannot land in this pull request.** `preflight.py` runs
`check_id_stability.py` against `origin/main`, and this branch *is* eleven
retitled IDs. The check's first act would be to fail the change that adds it,
and the only ways out are worse than waiting: an exemption for this branch is
"a policy change wearing a configuration disguise" (`.claude/rules/tooling.md`),
and reverting the renumbering reopens a decision the maintainer already took
(`design.md`, Decision 3).

**After this merges, `main` carries the new numbering and no retitles remain**,
so the check lands green in the next pull request. Recorded here so it is
scheduled rather than rediscovered.

**`build_index.py`'s `GLOSSARY = "14-glossary.md"` stays.** Something has to
name the glossary, and a constant that names it once is the right shape. It is
the same class as a rotted comment only in that a document can be removed —
`04-` and `13-` were — but unlike a comment, this one fails loudly.

### 15.1 — `SECTION_DEBT` is half dead, and the exemption hid it

`scripts/lint_ruleset.py` exempts `02-core-rules.md` from two required sections.
**Part A of this change gave that document a `# Design Philosophy` section**, so
half the exemption now covers a section that exists — and nobody noticed,
because an exemption's job is to stop the check from asking.

`# Summary` is still absent, so the entry shrinks rather than goes.

- [x] 15.1 In `scripts/lint_ruleset.py`, replace this anchor:

```
# 02-core-rules.md predates the standard and has neither a Design Philosophy nor
# a Summary section. Adding them changes the ruleset, which needs an OpenSpec
# proposal, so it is recorded here rather than fixed in passing. The point of
# the exemption is that it is a closed list: a *new* document cannot join it
# without someone editing this line.
SECTION_DEBT = {"02-core-rules.md": ("Design Philosophy", "Summary")}
```

with:

```
# 02-core-rules.md predates the standard and had neither a Design Philosophy nor
# a Summary section. It has a Design Philosophy now, so only the Summary is still
# owed. Adding one changes the ruleset, which needs an OpenSpec proposal, so it is
# recorded here rather than fixed in passing. The point of the exemption is that
# it is a closed list: a *new* document cannot join it without someone editing
# this line, and an entry that stops being true is meant to shrink like this one
# rather than sit unread.
SECTION_DEBT = {"02-core-rules.md": ("Summary",)}
```

### 15.2 — the constraint from section 13 becomes a gate

`system/documentation-standards.md` now says a script never names a rule that
exists. Nothing enforces it, and `.claude/rules/tooling.md` is explicit about
what that is worth: "Context can be read and ignored; a hook cannot." The
linter already holds the set of live IDs, so this is one function.

- [x] 15.2 In `scripts/lint_ruleset.py`, replace this anchor — the docstring's
      last check, gaining one below it:

```
- The image filenames in assets/IMAGES.md: that each follows the naming
  convention that file defines, that it names a document which exists,
  and that the rule it illustrates exists in that document.
```

with:

```
- The image filenames in assets/IMAGES.md: that each follows the naming
  convention that file defines, that it names a document which exists,
  and that the rule it illustrates exists in that document.
- Rule IDs named anywhere in scripts/: none may be a rule that exists in
  docs/, per system/documentation-standards.md (Naming Conventions).
```

- [x] 15.3 In `scripts/lint_ruleset.py`, replace this anchor — the new check
      goes above `main`:

```
def main() -> int:
```

with:

```
def check_scripts_name_no_live_rule(ids_by_file: dict[str, set[str]]) -> list[str]:
    """No file in scripts/ may name a rule that exists in docs/.

    `system/documentation-standards.md` (Naming Conventions) states the rule and
    the reason: no script's behaviour depends on a rule, so every ID in scripts/
    is an illustration, and an illustration naming a live ID is a dependency on
    a rule that can be retired or renumbered. Three had rotted before anything
    checked — one named a rule that no longer existed at all.

    `tests/` is deliberately not covered. A fixture defines its own document, so
    an ID inside one is local by construction and names nothing in docs/.
    """
    live = {rule_id for ids in ids_by_file.values() for rule_id in ids}

    errors: list[str] = []
    for path in sorted(SCRIPTS_DIR.glob("*.py")):
        for number, line in enumerate(path.read_text().splitlines(), start=1):
            for rule_id in dict.fromkeys(RULE_ID_RE.findall(line)):
                if rule_id in live:
                    errors.append(
                        f"scripts/{path.name}:{number}: names {rule_id}, which is a "
                        f"rule in docs/. Illustrate with an invented prefix "
                        f"(AAA-001, BBB-002) or a placeholder — "
                        f"system/documentation-standards.md (Naming Conventions)."
                    )
    return errors


def main() -> int:
```

- [x] 15.4 In `scripts/lint_ruleset.py`, replace this anchor — the constant sits
      beside the other path constant:

```
IMAGES_INDEX = REPO_ROOT / "assets" / "IMAGES.md"
```

with:

```
IMAGES_INDEX = REPO_ROOT / "assets" / "IMAGES.md"
SCRIPTS_DIR = REPO_ROOT / "scripts"
```

- [x] 15.5 In `scripts/lint_ruleset.py`, replace this anchor — wiring it in:

```
    errors.extend(check_image_index(ids_by_file))
```

with:

```
    errors.extend(check_image_index(ids_by_file))
    errors.extend(check_scripts_name_no_live_rule(ids_by_file))
```

- [x] 15.6 In `tests/test_lint_ruleset.py`, replace this anchor — the new test
      class goes at the end of the file's skeleton coverage, before whatever
      follows `structure_errors`:

```
class TestTheDocumentSkeleton:
```

with:

```
class TestScriptsNameNoLiveRule:
    """The check that keeps a script's illustrations from becoming references.

    Both cases are built in `tmp_path`: a script that names a live rule, and one
    that names an invented ID. `tests/` is not covered by the check, which is
    why this file may go on saying `VEH-001` in its own fixtures.
    """

    def _errors(self, tmp_path, monkeypatch, source: str) -> list[str]:
        (tmp_path / "example.py").write_text(source)
        monkeypatch.setattr(lint_ruleset, "SCRIPTS_DIR", tmp_path)
        return lint_ruleset.check_scripts_name_no_live_rule(
            {"08-vehicles.md": {"VEH-001", "VEH-002"}}
        )

    def test_a_script_naming_a_live_rule_is_reported(self, tmp_path, monkeypatch):
        errors = self._errors(tmp_path, monkeypatch, "# see VEH-001 for the shape\n")
        assert len(errors) == 1
        assert "VEH-001" in errors[0]
        assert "example.py:1" in errors[0]

    def test_an_invented_id_is_accepted(self, tmp_path, monkeypatch):
        assert self._errors(tmp_path, monkeypatch, "# see AAA-001 for the shape\n") == []

    def test_an_invented_number_under_a_real_prefix_is_accepted(
        self, tmp_path, monkeypatch
    ):
        assert self._errors(tmp_path, monkeypatch, "# a bare (VEH-099) is fine\n") == []

    def test_every_offending_line_is_reported_not_only_the_first(
        self, tmp_path, monkeypatch
    ):
        errors = self._errors(tmp_path, monkeypatch, "# VEH-001\n# nothing\n# VEH-002\n")
        assert len(errors) == 2
        assert "example.py:1" in errors[0]
        assert "example.py:3" in errors[1]


class TestTheDocumentSkeleton:
```

### 15.9 — the test that encoded the old exemption

**Found by task 15.7 failing, which is what it is for.** Task 15.1 shrank
`SECTION_DEBT` to `("Summary",)` and nothing in section 15 updated
`tests/test_lint_ruleset.py`, where a test strips *both* headings and asserts no
error. That test now fails, correctly: `# Design Philosophy` is required of
`02-core-rules.md` again, because the document has one.

**The replacement does more than un-break it.** The old test only proved the
exemption was honoured; it could not have told anyone the exemption had outlived
half its reason, which is exactly how this went unnoticed for several commits.
The new pair pins both directions — what is still exempt, and what stopped being
exempt.

- [x] 15.9 In `tests/test_lint_ruleset.py`, replace this anchor:

```
    def test_the_recorded_exemption_is_not_reported_again(self):
        assert "02-core-rules.md" in lint_ruleset.SECTION_DEBT
        text = COMPLETE.replace("# Design Philosophy", "# Notes").replace("# Summary", "# Notes")
        assert structure_errors("02-core-rules.md", text) == []
```

with:

```
    def test_the_recorded_exemption_is_not_reported_again(self):
        # What 02-core-rules.md is still owed: a Summary, and nothing else.
        assert lint_ruleset.SECTION_DEBT["02-core-rules.md"] == ("Summary",)
        text = COMPLETE.replace("# Summary", "# Notes")
        assert structure_errors("02-core-rules.md", text) == []

    def test_a_section_the_exemption_no_longer_covers_is_reported(self):
        # The other half of the same exemption, retired once the document
        # gained the section. An exemption records debt and never notices when
        # the debt is paid, so the check has to be the thing that notices.
        text = COMPLETE.replace("# Design Philosophy", "# Notes")
        errors = structure_errors("02-core-rules.md", text)
        assert any("Design Philosophy" in error for error in errors)
```

- [x] 15.7 Verify: `.venv/bin/pytest -q` and `python3 scripts/preflight.py` both
      green. The linter must still report nothing against `docs/` — section 13
      already cleared `scripts/`, so this gate lands on a repository that
      already satisfies it. **A gate that goes red the moment it is added has
      not been verified; it has been discovered.**

- [x] 15.8 Verify the gate bites: temporarily add a line naming a live rule to a
      file in `scripts/`, run `python3 scripts/lint_ruleset.py`, confirm it
      fails naming that file and ID, then revert the line. **Do not leave it.**
      A check nobody has seen fail is a check nobody has tested.

## 16. Deployment is a physical act, and footprints are whole

The maintainer stated the model this chapter has been circling since #129, in
their own words: **it is a PHYSICAL act — you put in as many elements as fit.**
A `5 × 1 × 1 UB` volume takes five infantry, or one `1 × 2 UB` Bike and three
infantry, or two Bikes and one infantry: whatever fits physically without models
overlapping. And if a model measures `1 × 2.5`, that is really `1 × 3` — there
are no partial footprints, only complete ones.

*(Written as prose rather than a blockquote on purpose:
`check_task_anchors.py` reads three or more consecutive `>` lines as a
replacement block written in the wrong convention, and fails the file. It is
right to — one file, one convention — and a quotation is not an exception worth
teaching it.)*

Three things follow, and only one of them was in `docs/`.

**Placement is real, not a calculation.** `DEP-002` says an army "can be
physically placed" and that "physical placement is the final check", but never
says a player does it — with the models, before the game. `DEP-007` pulls the
other way, calling deployment a measure of "how much battlefield space" is
consumed. A general reader cannot tell whether to build the box or do sums.

**Whole footprints are a new rule.** Nothing in `docs/` says a footprint rounds
up. `DEP-003`'s "every Unit Base covered by its footprint" implies it, and
`VEH-001`'s table hides the question by giving whole numbers. **The opposite
rule exists nearby and must survive**: inside a transport, cargo divides a Unit
Base into slices (`09-transport.md`, TRN-013). This rule is about the
deployment floor, not the interior.

**`DEP-006` still charges floor for a model that is not on the floor** — the
last piece of the budget reading in the chapter.

### 16.1–16.2 — `DEP-001` describes a box and nothing else

- [x] 16.1 In `docs/06-deployment.md`, replace this anchor — under placement,
      `W × D` is a rectangle measured in Unit Bases, not a count of them:

```
* `W × D` is the available floor area, counted in Unit Bases.
```

with:

```
* `W × D` is the available floor area, measured in Unit Bases.
```

- [x] 16.2 In `docs/06-deployment.md`, replace this anchor — the sentence is
      true and now serves nothing. It survived from the reading `DEP-002`
      replaced, where it argued that shape did not matter; under placement it
      only invites a reader to think in totals:

```
If only two dimensions are given, the Deployment Volume is **1 UB high**.

A `5 × 1` floor and a `1 × 5` floor both contain five Unit Bases.

Deployment Volumes may have any dimensions agreed upon by the players or defined by the scenario.
```

with:

```
If only two dimensions are given, the Deployment Volume is **1 UB high**.

Deployment Volumes may have any dimensions agreed upon by the players or defined by the scenario.
```

### 16.3 — `DEP-002` says what a player does

- [x] 16.3 In `docs/06-deployment.md`, replace this anchor — the whole rule
      body:

```
A player's army is any combination of models that can be physically placed within the agreed Deployment Volume.

Every model must fit within the Deployment Volume's floor and beneath its ceiling. Models cannot overlap.

The player chooses which models to deploy. No points or other army-capacity system is used.

The physical placement of the models is the final check. A combination is legal if all models can be placed within the Deployment Volume at the same time.
```

with:

```
**Put the models in the Deployment Volume. Whatever fits is a legal army.**

This is a physical act, done with the models before the game begins, not a calculation made about them.

Every model stands within the floor and beneath the ceiling, and no two models overlap.

A model occupies whole Unit Bases. A footprint covering part of a Unit Base covers all of it: a model measuring `1 × 2.5 UB` occupies `1 × 3 UB`. There are no partial footprints on the deployment floor — cargo inside a transport is the one place a Unit Base divides (`09-transport.md`, TRN-013).

Nothing requires the volume to be filled. The player chooses what to bring, and no points or other army-capacity system exists.

Example — a `5 × 1 × 1 UB` Deployment Volume:

* **5 infantry**, one Unit Base each (DEP-004).
* **1 Bike and 3 infantry** — a Bike is `1 × 2 UB` (`08-vehicles.md`, VEH-001), laid across the width so it is one Unit Base deep and two wide.
* **2 Bikes and 1 infantry.**

Each is legal for the same reason: the models physically fit, all at once, without overlapping.
```

### 16.4 — a model on a roof is not on the floor

- [x] 16.4 In `docs/06-deployment.md`, replace this anchor:

```
An externally carried infantry model is therefore deployed individually and occupies 1 Unit Base of Deployment Volume floor space (`DEP-004`).

An externally carried vehicle is deployed according to its own footprint (`DEP-003`).

Externally carried models also form part of the physical model for deployment-height purposes and must fit beneath the Deployment Volume ceiling (`08-vehicles.md`, VEH-030).
```

with:

```
The waiver applies only to embarked units. A model carried on the outside — on a roof, bonnet, hull top or outside of a turret — is not embarked.

An externally carried model occupies no floor of its own. It stands on the carrier, and the carrier's footprint is already on the floor — charging it a Unit Base it does not stand on is arithmetic, and this chapter does arithmetic nowhere else.

What it must do is fit: it is part of the carrier's physical height and must stand beneath the ceiling (`08-vehicles.md`, VEH-030).
```

### 16.5 — the Summary follows the rules

- [x] 16.5 In `docs/06-deployment.md`, replace this anchor — "Army size is
      measured using Unit Bases" is the calculation reading, in the restatement
      a reader reaches last (`system/proposal-review.md`, "The Summary Is Part
      of the Rule"):

```
1. Army size is measured using Unit Bases.
2. Vehicles consume floor space according to their footprint.
3. A model's height is checked against the Deployment Volume ceiling.
4. Transport capacity depends on physical interior space, and embarked units do not consume additional Deployment Volume floor space.
```

with:

```
1. An army is whatever physically fits inside the agreed Deployment Volume, placed without overlapping.
2. A vehicle occupies the whole Unit Bases its footprint covers.
3. Every model stands beneath the agreed ceiling.
4. Transport capacity depends on physical interior space, and embarked units occupy the interior rather than the floor.
```

- [x] 16.6 Read `06-deployment.md` end to end afterwards, `DEP-003` and
      `DEP-008` included — both were written against the reading these tasks
      complete, and a rule that now restates or contradicts `DEP-002` is what
      this pass is for. Report rather than fix.

- [x] 16.7 Verify: `python3 scripts/preflight.py` green, and
      `grep -rn "floor space\|to spend\|consume" docs/06-deployment.md`
      returns nothing that charges a model for space it does not stand on.

## 17. What section 16 left standing

Found by task 16.6's reading, which is what that task is for. All four are the
same defect: prose written against the calculation reading, left behind when the
rules above it stopped calculating.

- [x] 17.1 In `docs/06-deployment.md`, replace this anchor — the Design
      Philosophy still describes floor space as something a model *requires*
      rather than stands in, and takes five paragraphs to say what the volume
      is:

```
StudCraft measures army size using physical space instead of abstract points.

Every vehicle and infantry model occupies physical space. The floor area occupied by a model determines how much Deployment Volume floor space is required to deploy it.

Vehicle height is not determined by its footprint.

The Deployment Volume defines both the available floor area and the maximum deployment height. A model may be deployed if its physical geometry fits within the agreed Deployment Volume.

Wider models consume more floor space. Taller models require sufficient vertical clearance.

Balance emerges from the physical space available rather than from points or army lists.
```

with:

```
StudCraft measures army size with physical space instead of points.

The Deployment Volume is a box the players agree on before the game: a floor `W × D` and a ceiling `H`, both in Unit Bases. **An army is whatever physically fits inside it.**

A wider model takes more of the floor and leaves less for everything else. A taller one needs the clearance to stand. Nothing about a vehicle's height follows from its footprint.

Balance comes from what a player can fit, not from a list.
```

- [x] 17.2 In `docs/06-deployment.md`, replace this anchor — `DEP-007`'s middle
      sentence is the "space consumed" framing, and it restates `DEP-006`:

```
Deployment only determines how much battlefield space a transport and its embarked units consume before the game begins.

See `DEP-005` and `DEP-006`.
```

with:

```
What deployment settles is where a transport and its embarked units stand before the game begins — `DEP-005` and `DEP-006`.
```

- [x] 17.3 In `docs/06-deployment.md`, replace this anchor — `DEP-008` closes
      with a near-verbatim copy of the sentence task 16.3 removed from
      `DEP-002`. A rule that restates another is the thing this whole change
      removes; it now points instead:

```
These are examples only.

Any combination is legal if all models can be physically placed within the Deployment Volume at the same time.
```

with:

```
These are examples only. What makes any of them legal is `DEP-002`: the models fit, all at once, without overlapping.
```

- [x] 17.4 In `docs/06-deployment.md`, replace this anchor — Design Notes and
      Design Philosophy say the same two things in different words, at opposite
      ends of the document. What is left here is only what the Philosophy does
      not already carry:

```
StudCraft intentionally replaces army points with physical space.

Wider models consume more floor space, while taller models require sufficient vertical clearance within the agreed Deployment Volume.

Large vehicles gain transport capacity, survivability and firepower naturally through their physical construction.

Small forces gain flexibility and numbers.

Balance emerges from construction and physical deployment space rather than from points values.
```

with:

```
A large vehicle earns its transport capacity, survivability and firepower from its own construction, and pays for them in the floor it stands on. A small force gains flexibility and numbers instead.

That trade is the whole of army selection here. The Design Philosophy above states it once.
```

- [x] 17.5 Verify: `python3 scripts/preflight.py` green, and
      `grep -rn "consume\|to spend\|required to deploy" docs/06-deployment.md`
      returns only the negated forms inside `DEP-004` and `DEP-006` — the ones
      saying an embarked model consumes **no** floor.

- [x] 17.6 Read `06-deployment.md` end to end one more time. This is the third
      reading of this chapter in this change, and the first two each found
      something the one before missed. Report; do not fix.

## 18. What the third reading found

Two hits, and **one of them is text task 17.4 wrote.** A reading pass catches
what a grep cannot, which is the whole argument for doing three of them: neither
of these matches `consume`, `to spend` or `floor space`, so both verification
commands in sections 16 and 17 passed over them.

- [x] 18.1 In `docs/06-deployment.md`, replace this anchor — "counts against"
      is a ledger, in the rule for the most common model in the game. `DEP-002`
      was rewritten to say deployment is a physical act and not a calculation;
      this is the calculation, one rule below it:

```
When deployed individually, this UB counts against the Deployment Volume floor.

When embarked inside a transport, the infantry model occupies the transport's interior space and does not consume additional Deployment Volume floor space (`DEP-006`).
```

with:

```
Deployed on its own, it stands on the Deployment Volume's floor.

Embarked in a transport, it stands in the transport's interior instead, and takes no floor of its own (`DEP-006`).
```

- [x] 18.2 In `docs/06-deployment.md`, replace this anchor — "pays for them in
      the floor" is a price, written into Design Notes by task 17.4 while that
      same task was removing prices from the chapter. The trade it describes is
      real; the metaphor is the one `DEP-002` no longer supports:

```
A large vehicle earns its transport capacity, survivability and firepower from its own construction, and pays for them in the floor it stands on. A small force gains flexibility and numbers instead.
```

with:

```
A large vehicle earns its transport capacity, survivability and firepower from its own construction, and stands on more of the floor for it, leaving less room beside it. A small force fits more models in the same box.
```

- [x] 18.3 Verify: `python3 scripts/preflight.py` green, and
      `grep -rn "counts against\|pays for\|consume\|to spend" docs/06-deployment.md`
      returns **one** line — `DEP-006`'s "The infantry do not consume additional
      Deployment Volume floor space while embarked", which is the negated form.

      This task first said "the two negated lines in `DEP-004` and `DEP-006`",
      copied from 17.5 without noticing that **task 18.1 removes the word from
      `DEP-004` in the same section**. The applier refused to tick it against
      the wrong expectation, which is the correct call: a verification is only
      worth running if being wrong is allowed to show.

- [x] 18.4 Read `06-deployment.md` end to end a fourth time. **Read for the
      framing rather than the words**: the three greps so far each missed a hit
      the next reading found, because a ledger can be written without using any
      of the words a grep knows. Report; do not fix. If this reading finds
      nothing, say so — that is the result that ends the loop.

## 19. Carried means inside, and task 16.4 got it backwards

The maintainer's statement, which settles a rule this change had moved the wrong
way: **a unit is carried only in the transport space its carrier actually has,
that space is itself bounded by the agreed Deployment Volume, and models may not
be put on the outside in disorder.**

**Task 16.4 is the error.** It removed `DEP-006`'s charge on an externally
carried model, on the argument that a model standing on a roof does not stand on
the floor and charging it a Unit Base of floor was the chapter's last piece of
arithmetic. The arithmetic objection was right. **The conclusion was wrong**: it
made perching models on hulls free, which is exactly the disorder the rule
existed to prevent.

The resolution is neither the charge nor the waiver. **There is no third place.**
A model is inside its carrier's transport space (`09-transport.md`, TRN-001,
TRN-003) — embarked, and taking no floor of its own — or it stands on the
Deployment Volume floor like any other model. Nothing is perched, so nothing has
to be priced.

**It also fixes a contradiction 16.4 introduced.** `08-vehicles.md`'s `VEH-030`
still reads "Models carried outside a vehicle ... also occupy their own
Deployment Volume space (`06-deployment.md`, DEP-006)" — against a `DEP-006`
that, since 16.4, says they occupy none. Two documents, opposite answers, and
neither the linter nor any grep in sections 16 to 18 could see it.

- [x] 19.1 In `docs/06-deployment.md`, replace this anchor — the paragraphs task
      16.4 wrote, plus the sentence above them. **"The waiver applies only to
      embarked units" is the fourth reading's finding**: a waiver names an
      exemption from an obligation presumed to exist, which is the same ledger
      shape as "counts against" and "pays for", in a word no grep in sections 16
      to 18 would ever have looked for. It goes with the rest:

```
The waiver applies only to embarked units. A model carried on the outside — on a roof, bonnet, hull top or outside of a turret — is not embarked.

An externally carried model occupies no floor of its own. It stands on the carrier, and the carrier's footprint is already on the floor — charging it a Unit Base it does not stand on is arithmetic, and this chapter does arithmetic nowhere else.

What it must do is fit: it is part of the carrier's physical height and must stand beneath the ceiling (`08-vehicles.md`, VEH-030).
```

with:

```
A unit is carried only inside the transport space its carrier physically has (`09-transport.md`, TRN-001, TRN-003). A model that is not inside it is not being carried: it is deployed on its own and stands on the floor, like any other model.

There is no third place. Models are not perched on hulls, roofs or turrets to avoid taking floor, and anything built onto the outside of a vehicle is part of that vehicle's height (`08-vehicles.md`, VEH-030).
```

- [x] 19.2 In `docs/06-deployment.md`, replace this anchor — `DEP-005` states
      what bounds a transport's capacity and stops one bound short. The
      compartment is inside a vehicle, and the vehicle has to fit the box:

```
If a Unit Base fits inside the vehicle, a minifigure may be transported in it (`09-transport.md`, TRN-019).

If it does not fit, it cannot.
```

with:

```
If a Unit Base fits inside the vehicle, a minifigure may be transported in it (`09-transport.md`, TRN-019).

If it does not fit, it cannot.

The compartment is bounded twice over: by what the vehicle is physically built to hold, and by the vehicle itself having to stand inside the agreed Deployment Volume (DEP-001).
```

- [x] 19.3 In `docs/08-vehicles.md`, replace this anchor — `VEH-030` answers
      the question `DEP-006` now answers differently:

```
Models carried outside a vehicle are not embarked and count toward vehicle height. They also occupy their own Deployment Volume space (`06-deployment.md`, DEP-006).
```

with:

```
Anything built onto the outside of a vehicle counts toward its height. A model is carried only inside the vehicle's transport space; one that is not inside it deploys on its own (`06-deployment.md`, DEP-006).
```

- [x] 19.4 Verify: `python3 scripts/preflight.py` green, and
      `grep -rn "externally carried\|carried outside\|not embarked" docs/`
      returns nothing that says a model outside a transport takes, or avoids
      taking, floor of its own.

- [x] 19.5 Read `DEP-005`, `DEP-006` and `VEH-030` together, in that order, as
      a reader following the citations does. The three now answer one question
      between them and each was written at a different time. Report; do not fix.

## 20. Reverting what this change added to a chapter that was already clear

**The maintainer's call, and it is right.** Tasks 16.4, 19.1, 19.2 and 19.3
added text to `DEP-005`, `DEP-006` and `VEH-030` to state a rule that
`09-transport.md` already owns: `TRN-005` says "Place the unit **inside** the
available transport space", `TRN-001` says every transported object occupies
Unit Bases of that space, and `VEH-016` says a passenger may embark only when
there are free ones. Carried means inside. It was written once, in the right
document, before this change touched anything.

**What those four tasks actually did was restate it in two more places** — the
defect this whole change exists to remove, committed by the change itself. The
text as `Part A` left it needed nothing.

All three rules go back to their Part A wording.

**This makes `apply_tasks.py --check` report `skip` on tasks 16.4, 19.2 and
19.3 from here on.** Their anchors are back in the files, because that is what a
revert does, and the script cannot tell a restored anchor from an unapplied
task. It says so and defers — "either a later task restored the text, or the
tick is wrong, a reader decides". A later task restored the text. The ticks are
right, and this paragraph is the reader's decision, recorded once.

**One objection, stated once and not acted on.** `DEP-006`'s restored line reads
"occupies 1 Unit Base of Deployment Volume floor space", which is the same
vocabulary shape as the "counts against" that section 18 removed from `DEP-004`.
The *substance* is right under the maintainer's rule — a model that never
embarked deploys on its own — and the maintainer reads it as clear. **Not a
weighty objection**, so it stays as written; recorded here so the next reader
knows it was seen and left, rather than missed.

- [x] 20.1 In `docs/06-deployment.md`, replace this anchor — everything tasks
      16.4 and 19.1 wrote:

```
A unit is carried only inside the transport space its carrier physically has (`09-transport.md`, TRN-001, TRN-003). A model that is not inside it is not being carried: it is deployed on its own and stands on the floor, like any other model.

There is no third place. Models are not perched on hulls, roofs or turrets to avoid taking floor, and anything built onto the outside of a vehicle is part of that vehicle's height (`08-vehicles.md`, VEH-030).
```

with:

```
The waiver applies only to embarked units. A model carried on the outside — on a roof, bonnet, hull top or outside of a turret — is not embarked.

An externally carried infantry model is therefore deployed individually and occupies 1 Unit Base of Deployment Volume floor space (`DEP-004`).

An externally carried vehicle is deployed according to its own footprint (`DEP-003`).

Externally carried models also form part of the physical model for deployment-height purposes and must fit beneath the Deployment Volume ceiling (`08-vehicles.md`, VEH-030).
```

- [x] 20.2 In `docs/06-deployment.md`, replace this anchor — task 19.2's
      sentence. `DEP-002` already says every model must fit inside the agreed
      volume, and a transport is a model:

```
If it does not fit, it cannot.

The compartment is bounded twice over: by what the vehicle is physically built to hold, and by the vehicle itself having to stand inside the agreed Deployment Volume (DEP-001).
```

with:

```
If it does not fit, it cannot.
```

- [x] 20.3 In `docs/08-vehicles.md`, replace this anchor — task 19.3's
      sentence, back to what `VEH-030` said before this change:

```
Anything built onto the outside of a vehicle counts toward its height. A model is carried only inside the vehicle's transport space; one that is not inside it deploys on its own (`06-deployment.md`, DEP-006).
```

with:

```
Models carried outside a vehicle are not embarked and count toward vehicle height. They also occupy their own Deployment Volume space (`06-deployment.md`, DEP-006).
```

- [x] 20.4 Verify the revert is exact: `git diff HEAD -- docs/06-deployment.md`
      shows no change to `DEP-005`, and `DEP-006` differs from `HEAD` in nothing
      but what sections 1 and 16 changed elsewhere in the rule.
      `git diff HEAD -- docs/08-vehicles.md` shows no change to `VEH-030`.

- [x] 20.5 Verify: `python3 scripts/preflight.py` green.

## 21. `DEP-002` goes back to Part A, plus one clause

**The maintainer's call, and there is no weighty objection to it.** Task 16.3
replaced a four-paragraph rule with a longer one, in a change whose purpose is
to shorten. Audited piece by piece, only one addition earns its place:

| What 16.3 added | Verdict |
|---|---|
| "This is a physical act… not a calculation made about them." | **Redundant.** Part A already says "The physical placement of the models is the final check." |
| The `5 × 1 × 1 UB` worked example, three bullets | **Redundant.** `DEP-008` already carries a worked example with three combinations. Two of the same thing in one chapter. |
| "Nothing requires the volume to be filled." | **Redundant.** Part A's "The player chooses which models to deploy" covers it. |
| The `TRN-013` carve-out about cargo dividing a Unit Base | **Redundant here.** It pre-empts a question `DEP-002` never raises, in a rule that does not mention interiors. |
| **Whole footprints** — a `1 × 2.5 UB` model occupies `1 × 3 UB` | **Kept.** Stated nowhere in `docs/` — not in Part A, not in `DEP-003`. Without it a model can claim half a Unit Base and argue over the other half. |

The one that survives fits as a clause on Part A's own sentence, not as a
paragraph with an example.

- [x] 21.1 In `docs/06-deployment.md`, replace this anchor — the whole rule
      body as task 16.3 left it:

```
**Put the models in the Deployment Volume. Whatever fits is a legal army.**

This is a physical act, done with the models before the game begins, not a calculation made about them.

Every model stands within the floor and beneath the ceiling, and no two models overlap.

A model occupies whole Unit Bases. A footprint covering part of a Unit Base covers all of it: a model measuring `1 × 2.5 UB` occupies `1 × 3 UB`. There are no partial footprints on the deployment floor — cargo inside a transport is the one place a Unit Base divides (`09-transport.md`, TRN-013).

Nothing requires the volume to be filled. The player chooses what to bring, and no points or other army-capacity system exists.

Example — a `5 × 1 × 1 UB` Deployment Volume:

* **5 infantry**, one Unit Base each (DEP-004).
* **1 Bike and 3 infantry** — a Bike is `1 × 2 UB` (`08-vehicles.md`, VEH-001), laid across the width so it is one Unit Base deep and two wide.
* **2 Bikes and 1 infantry.**

Each is legal for the same reason: the models physically fit, all at once, without overlapping.
```

with:

```
A player's army is any combination of models that can be physically placed within the agreed Deployment Volume.

Every model must fit within the Deployment Volume's floor and beneath its ceiling. Models cannot overlap. A model occupies whole Unit Bases: a footprint covering part of one covers all of it.

The player chooses which models to deploy. No points or other army-capacity system is used.

The physical placement of the models is the final check. A combination is legal if all models can be placed within the Deployment Volume at the same time.
```

- [x] 21.2 Verify the rule is Part A's text plus one clause, and nothing else:
      `git diff HEAD -- docs/06-deployment.md` shows exactly one changed line
      inside `DEP-002` — the one gaining "A model occupies whole Unit Bases: a
      footprint covering part of one covers all of it." Every other line of the
      rule must be absent from the diff.

- [x] 21.3 Verify: `python3 scripts/preflight.py` green.

## 22. Reverting the prose this change had no business rewriting

**The maintainer's scope, stated plainly: what was already written was fine.
The job was to find contradictions and broken references.** Sections 16, 17 and
18 went past that and rewrote prose that had neither problem — in a chapter
whose Part A wording the maintainer had already settled.

Every rewrite below is reverted to Part A. What survives in `06-deployment.md`
is exactly two edits, and both earn it:

- **Task 1.1** — deleting `DEP-001`'s "The floor is counted rather than treated
  as a shape", which contradicted `DEP-002`. A contradiction.
- **Task 21.1** — one clause on `DEP-002`: "A model occupies whole Unit Bases: a
  footprint covering part of one covers all of it." A rule stated nowhere in
  `docs/`, and stated by the maintainer.

- [x] 22.1 In `docs/06-deployment.md`, restore the Design Philosophy. Replace
      this anchor:

```
StudCraft measures army size with physical space instead of points.

The Deployment Volume is a box the players agree on before the game: a floor `W × D` and a ceiling `H`, both in Unit Bases. **An army is whatever physically fits inside it.**

A wider model takes more of the floor and leaves less for everything else. A taller one needs the clearance to stand. Nothing about a vehicle's height follows from its footprint.

Balance comes from what a player can fit, not from a list.
```

with:

```
StudCraft measures army size using physical space instead of abstract points.

Every vehicle and infantry model occupies physical space. The floor area occupied by a model determines how much Deployment Volume floor space is required to deploy it.

Vehicle height is not determined by its footprint.

The Deployment Volume defines both the available floor area and the maximum deployment height. A model may be deployed if its physical geometry fits within the agreed Deployment Volume.

Wider models consume more floor space. Taller models require sufficient vertical clearance.

Balance emerges from the physical space available rather than from points or army lists.
```

- [x] 22.2 In `docs/06-deployment.md`, restore `DEP-001`'s wording. Task 1.1's
      deletion stays; tasks 16.1 and 16.2 are undone. Replace this anchor:

```
* `W × D` is the available floor area, measured in Unit Bases.
* `H` is the maximum deployment height in Unit Bases.

If only two dimensions are given, the Deployment Volume is **1 UB high**.

Deployment Volumes may have any dimensions agreed upon by the players or defined by the scenario.
```

with:

```
* `W × D` is the available floor area, counted in Unit Bases.
* `H` is the maximum deployment height in Unit Bases.

If only two dimensions are given, the Deployment Volume is **1 UB high**.

A `5 × 1` floor and a `1 × 5` floor both contain five Unit Bases.

Deployment Volumes may have any dimensions agreed upon by the players or defined by the scenario.
```

- [x] 22.3 In `docs/06-deployment.md`, restore `DEP-004`. Replace this anchor:

```
Deployed on its own, it stands on the Deployment Volume's floor.

Embarked in a transport, it stands in the transport's interior instead, and takes no floor of its own (`DEP-006`).
```

with:

```
When deployed individually, this UB counts against the Deployment Volume floor.

When embarked inside a transport, the infantry model occupies the transport's interior space and does not consume additional Deployment Volume floor space (`DEP-006`).
```

- [x] 22.4 In `docs/06-deployment.md`, restore `DEP-007`. Replace this anchor:

```
What deployment settles is where a transport and its embarked units stand before the game begins — `DEP-005` and `DEP-006`.
```

with:

```
Deployment only determines how much battlefield space a transport and its embarked units consume before the game begins.

See `DEP-005` and `DEP-006`.
```

- [x] 22.5 In `docs/06-deployment.md`, restore `DEP-008`'s close. Replace this
      anchor:

```
These are examples only. What makes any of them legal is `DEP-002`: the models fit, all at once, without overlapping.
```

with:

```
These are examples only.

Any combination is legal if all models can be physically placed within the Deployment Volume at the same time.
```

- [x] 22.6 In `docs/06-deployment.md`, restore the Design Notes. Replace this
      anchor:

```
A large vehicle earns its transport capacity, survivability and firepower from its own construction, and stands on more of the floor for it, leaving less room beside it. A small force fits more models in the same box.

That trade is the whole of army selection here. The Design Philosophy above states it once.
```

with:

```
StudCraft intentionally replaces army points with physical space.

Wider models consume more floor space, while taller models require sufficient vertical clearance within the agreed Deployment Volume.

Large vehicles gain transport capacity, survivability and firepower naturally through their physical construction.

Small forces gain flexibility and numbers.

Balance emerges from construction and physical deployment space rather than from points values.
```

- [x] 22.7 In `docs/06-deployment.md`, restore the Summary. Replace this anchor:

```
1. An army is whatever physically fits inside the agreed Deployment Volume, placed without overlapping.
2. A vehicle occupies the whole Unit Bases its footprint covers.
3. Every model stands beneath the agreed ceiling.
4. Transport capacity depends on physical interior space, and embarked units occupy the interior rather than the floor.
```

with:

```
1. Army size is measured using Unit Bases.
2. Vehicles consume floor space according to their footprint.
3. A model's height is checked against the Deployment Volume ceiling.
4. Transport capacity depends on physical interior space, and embarked units do not consume additional Deployment Volume floor space.
```

- [x] 22.8 Verify the chapter is Part A plus two edits and nothing else:
      `git diff HEAD -- docs/06-deployment.md` shows **two** changed regions —
      `DEP-001` losing one sentence, and `DEP-002` gaining one clause. Anything
      else in the diff means a revert missed. Report it rather than ticking.

- [x] 22.9 Verify: `python3 scripts/preflight.py` green.

---

# Part C — Found by a later reading

**Nothing in Part C is applied.** Sections 24, 25, 26, 30, 32, 33, 34 and 35 are
repairs of the kind Part B carries. Sections 23, 27, 28, 29 and 31 are rule
changes, and the only five in this file.

Section 32, and part of section 35, repair defects **pre-existing on `main`** —
the tracks example, and three retired rule IDs still cited from `system/`. Every
other repair here fixes something this change introduced.

## 23. A staircase is a chain of obstacles, and every domain reads it the same way

**This section changes what a rule means. It is not a repair, and it is the
maintainer's decision** (`design.md`, Decision 13).

`VEH-027` said "Stairs are never a legal vehicle ascent" and, four lines later,
that a walker may cross stairs its Terrain Threshold permits. The absolute is
what goes: a stepped surface is a chain of obstacles, each read on its own
against the moving unit's own threshold, for infantry and vehicles alike.

The shared half moves to `MOVE-013`, which already owns what a stepped surface
is. Each domain document then states only what its own domain charges, and
`17-infantry.md` stops describing vehicles at all.

Five edits. Four are deletions.

- [x] 23.1 In `docs/07-movement.md`, `MOVE-013`, replace this anchor:

```
A stepped surface is terrain built from discrete steps, whatever the steps are built from, and each step has a measurable height.

Whether a given unit may climb one is its own domain's question — infantry (`17-infantry.md`, INF-009), vehicles never (`08-vehicles.md`, VEH-027).
```

with:

```
A stepped surface is terrain built from discrete steps, whatever the steps are built from, and each step has a measurable height. Each step is an obstacle in its own right, read individually.

Whether a given unit may climb one is its own domain's question — infantry (`17-infantry.md`, INF-009), vehicles (`08-vehicles.md`, VEH-027).
```

  Two changes: the shared rule gains its sentence, and `never` goes. `MOVE-013`
  now reads exactly like `MOVE-012` and `MOVE-014` beside it — the asymmetry was
  the only thing that set it apart.

- [x] 23.2 In `docs/08-vehicles.md`, `VEH-021`, replace this anchor:

```
* Obstacles and drops equal to the threshold are crossed normally.

Stairs are never a legal vehicle ascent.

A vehicle leaving a height entirely is falling and uses VEH-026 instead.
```

with:

```
* Obstacles and drops equal to the threshold are crossed normally.

A vehicle leaving a height entirely is falling and uses VEH-026 instead.
```

  A deletion. The bullets above it already resolve a stepped surface, obstacle by
  obstacle, and the rule already cites `VEH-027` for the rest.

  **The anchor spans three paragraphs on purpose:** the deleted sentence occurs
  twice in this file, and this is the occurrence in `VEH-021`. Task 23.3 handles
  the other.

- [x] 23.3 In `docs/08-vehicles.md`, `VEH-027`, replace this anchor:

```
Stairs are never a legal vehicle ascent.

A vehicle descending a full slope or ramp is driving, not falling. Any other descent is a fall (`VEH-026`).

A walker may cross a rise or stairs directly when its Terrain Threshold permits it.
```

with:

```
A stepped surface is a chain of such rises, each read on its own (`07-movement.md`, MOVE-013).

A vehicle descending a full slope or ramp is driving, not falling. Any other descent is a fall (`VEH-026`).
```

  "Such rises" is the rule's own first sentence — a rise no greater than the
  Terrain Threshold is crossed directly, a greater one needs a slope or ramp, and
  a step is read by both. Nothing new is charged.

  **The walker sentence goes and nothing replaces it.** A walker's knee is its
  Terrain Threshold (`VEH-023`) exactly as a wheel's axle is (`VEH-022`); once
  every vehicle reads a step against its own threshold, a walker rule states the
  general case twice.

- [x] 23.4 In `docs/17-infantry.md`, `INF-009`, replace this anchor:

```
Distance traveled up either counts against the normal movement limit (INF-002).

A vehicle reads the same staircase as one obstacle of its total rise rather than a series of small ones (`08-vehicles.md`, VEH-027): infantry takes the steps and a vehicle cannot.
```

with:

```
Distance traveled up either counts against the normal movement limit (INF-002).
```

  A deletion, and it closes the audit's finding 2 as well: the sentence cited
  `VEH-027` for a claim `VEH-027` no longer carried. There is no asymmetry left
  to explain, and an infantry rule has no business describing vehicles.

  `:157` and `:159` stay untouched. They state what infantry pays in Action
  Points per step, which is infantry's own.

- [x] 23.5 In `system/proposal-review.md`, replace this anchor:

```
`VEH-021` pointing a vehicle at an infantry rule that permits stairs, which
`VEH-027` forbids; `MOVE-016` stating "each die is a Damage Roll" twice;
`DMG-004`'s closing paragraph displaced three times by later examples; a new
`VEH-004` table reintroducing `VEH-001`'s footprints as a parenthetical.
```

with:

```
`DMG-004`'s closing paragraph displaced three times by later examples; a new
`VEH-004` table reintroducing `VEH-001`'s footprints as a parenthetical.
```

  This document's canonical example of "a rule that contradicts one three
  documents away" was this exact pair, and tasks 23.1 through 23.4 remove the
  contradiction it names. `system/*.md` needs a branch but no proposal
  (`system/workflow.md`, Git Workflow); it travels here because it goes stale in
  the same commit.

  **`MOVE-016` goes with it, and that is a second repair in one edit.**
  `MOVE-016` was retired before this change and `python3 scripts/rule.py show
  MOVE-016` reports no such rule, so the example named a rule a reader cannot
  reach. The two survivors — `DMG-004` and the `VEH-004`/`VEH-001` pair — are
  live and make the same point.

### Verification

- [x] 23.6 `grep -c -F "Stairs are never a legal vehicle ascent." docs/08-vehicles.md`
      returns **0**. It was 2.

- [x] 23.7 `grep -rn "stair" docs/08-vehicles.md` returns nothing. The document
      no longer names stairs at all — `MOVE-013` owns the construction and
      `VEH-027` reads it.

- [x] 23.8 `grep -rni "vehicle" docs/17-infantry.md` — every remaining hit is
      about transport or about a vehicle's fall, not about terrain. Report any
      hit that answers a vehicle's terrain question.

- [x] 23.9 `python3 scripts/rule.py refs MOVE-013 VEH-027 INF-009` — every citer
      names a rule that exists, and no citer claims vehicles cannot climb stairs.

- [x] 23.10 `python3 scripts/preflight.py` — every check green.

- [x] 23.11 Read `MOVE-012`, `MOVE-013`, `MOVE-014`, `VEH-021`, `VEH-027` and
      `INF-009` in full, plus both Summaries. `system/proposal-review.md` is
      explicit that this is where the findings are, and this section is a rule
      change rather than a transcription.

---

## 24. `DEP-008`'s worked example cannot be satisfied

**This change invented the number.** On `main`, `DEP-008` listed three forces
and named no Deployment Volume at all — there was no floor to check them
against, and nothing to get wrong. The compression rewrote the three forces as
bullets under a `5 × 4 × 2 UB` volume, and the arithmetic does not hold:

- The floor is `5 × 4` = **20 Unit Bases**, which the first bullet states
  ("20 infantry, filling the floor").
- A Tank is `2 × 5 UB` = 10 UB (`08-vehicles.md`, VEH-001). **Two Tanks are the
  entire floor** — 5 along the 5-axis, 2 along the 4-axis, twice over. The
  second bullet's eight infantry have nowhere to stand.
- **No single floor satisfies both bullets.** The first requires exactly 20, the
  second requires at least 28. Raising the number fixes one by breaking the
  other.

The third bullet is a milder defect of the same kind: a Super Heavy is
`Player Built` (`VEH-001`), so "1 super-heavy transport carrying 2 walkers and
4 infantry" is not impossible — it is unfalsifiable, which is not what a worked
example is for.

The delete-it form is available, so it is taken (`How to read this file`). The
volume goes, and with it the three conditional clauses: each restates `DEP-002`,
and the rule's own closing line already says it once.

- [x] 24.1 In `docs/06-deployment.md`, `DEP-008`, replace this anchor:

```
For example, a `5 × 4 × 2 UB` Deployment Volume may contain:

* **20 infantry**, filling the floor.
* **2 tanks and 8 infantry**, if their footprints can be placed within the floor and all models fit beneath the ceiling.
* **1 super-heavy transport carrying 2 walkers and 4 infantry**, provided the transport and its contents satisfy the applicable transport rules and the complete deployed model fits within the Deployment Volume.
```

with:

```
For example:

* 20 infantry.
* 2 tanks and 8 infantry.
* 1 super-heavy transport carrying 2 walkers and 4 infantry.
```

  The three forces are `main`'s, in the bullet form Part A gave them. What goes
  is the invented volume and the claims measured against it.

### Verification

- [x] 24.2 `grep -c -F "Deployment Volume may contain:" docs/06-deployment.md`
      returns **0**. It was 1.

- [x] 24.3 `grep -c -F "5 × 4 × 2" docs/06-deployment.md` returns **0**. The
      volume this change invented appears in no other rule.

      **Not a bare `5 × 4`**: `DEP-009`'s Skirmish volume is `5 × 5 × 4 UB` and
      contains that substring, so the loose grep would report a hit that task
      24.1 is not supposed to remove.

- [x] 24.4 Read `DEP-008` in full. It states that forces may be mixed, gives
      three unmeasured illustrations, and refers the legality test to placement
      — which is `DEP-002`'s, not its own.

      **Task 22.8's hunk count is superseded, and no cumulative count replaces
      it.** Part A and Part B are committed on this branch, so `git diff HEAD`
      shows Part C's edits alone — two hunks here, this task's and task 26.1's.
      Counting regions against a moving baseline was the wrong check to write.

      What is checkable instead: this change makes **exactly four** edits to
      `docs/06-deployment.md` — task 1.1 deleting `DEP-001`'s counting clause,
      task 21.1 adding one clause to `DEP-002`, this task, and task 26.1. Read
      the chapter and confirm there is no fifth.

      The applier reported the mismatch rather than editing the ruleset to make
      the number come out, which is what the instruction at the top of this file
      asks for.

- [x] 24.5 `python3 scripts/preflight.py` — every check green.

---

## 25. `Weapon Width` is read by three rules and defined by none

`main` defined it, in `WPN-018`: *"Weapon Width is the smallest dimension of the
Weapon Body."* The compression deleted the sentence and no rule supplies another,
while three still read the term:

- `WPN-018` — `Length ≥ 2 × Width`
- `WPN-019` — the Weapon Front is a square whose dimensions equal the Weapon Width
- `WPN-020` — "A Weapon Body 8 × 4 has a Weapon Width of 4"

`14-glossary.md:127` sends a reader to `WPN-018` for it. **Not cosmetic:** the
Weapon Front Footprint is Width × Width, and every muzzle count and Impact
Strength derives from it (`WPN-021`).

**This task adds words, and it is the second in this file to do so** — the other
is 6.1, for the same reason. A term three rules read and none defines has no
delete-it form.

### Why `WPN-003` and not `WPN-018`, where it was

`python3 scripts/rule.py refs WPN-018` reports **cited by nothing**. Restoring the
definition there puts it in a dead end: neither `WPN-019` nor `WPN-020` has
anything to do with the proportion constraint, and neither cites the rule that
would hold their definition.

`WPN-003` is the rule that says which dimension of the Weapon Body is which, and
it is cited — by `MEL-014` and by the glossary's *Weapon Body*. `WPN-018` states
a constraint; carrying a definition as well makes it state two things where the
standard asks for one (`system/documentation-standards.md`, How a Rule Is
Written).

**The rule is retitled and keeps its number.** That is the one thing no script
reports (`design.md`, Decision 12), so it is written down here: `WPN-003` widens
from Length to both dimensions. It is not a different rule wearing the same
number — both existing citations still aim true. `MEL-014:180` cites it for
Weapon Length, which it still defines, and the glossary's *Weapon Body* already
claims both dimensions for it.

- [x] 25.1 In `docs/10-weapons.md`, replace this anchor — **the rule heading is
      part of it**:

```
# WPN-003 — Weapon Length

Weapon Length is the longest dimension of the functional Weapon Body, measured along its firing axis.
```

with:

```
# WPN-003 — Weapon Dimensions

Weapon Length is the longest dimension of the functional Weapon Body, measured along its firing axis. Weapon Width is the Weapon Body's smallest dimension.
```

  **"the Weapon Body's" rather than "its".** The nearest antecedent for "its"
  would be *Weapon Length*, then *its firing axis*; the Weapon Body is two
  clauses back. `main`'s deleted sentence was explicit for the same reason —
  "Weapon Width is the smallest dimension of the Weapon Body" — and a definition
  three rules read cannot rest on a pronoun.

  `WPN-018`, `WPN-019`, `WPN-020` and `docs/14-glossary.md` are **not touched**.
  Every sentence that reads the term keeps its wording, and the two citations of
  `WPN-003` keep theirs.

### Verification

- [x] 25.2 `grep -c -F "Weapon Width is the Weapon Body's smallest dimension" docs/10-weapons.md`
      returns **1**.

- [x] 25.3 `grep -c -F "# WPN-003 — Weapon Length" docs/10-weapons.md` returns
      **0**.

- [x] 25.4 `python3 scripts/rule.py refs WPN-003` — still `MEL-014` and the
      glossary's *Weapon Body*, and the rule now prints under its new title. A
      third citer means something was edited that this task does not name.

- [x] 25.5 `python3 scripts/build_index.py` — the index carries rule titles, so
      it is regenerated rather than left for the `Ruleset index is current`
      check to fail on.

- [x] 25.6 `python3 scripts/preflight.py` — every check green.

- [x] 25.7 Read `WPN-003`, `WPN-018`, `WPN-019` and `WPN-020` in full, in that
      order. The question is whether a reader meeting "Weapon Width" in `WPN-019`
      now has somewhere to have learnt it.

      **Not fixed here, and not a defect:** `docs/14-glossary.md` has no *Weapon
      Width* entry of its own. It did not have one before this change either, and
      adding one is a separate decision.

---

## 26. `DEP-001` keeps one sentence of the counting model, and it illustrates nothing

**The contradiction the audit reported is already gone.** `main` stated the
counting model outright:

> **The floor is `W × D` Unit Bases, counted**: a `5 × 1` floor and a `1 × 5`
> floor are the same five, **and neither is a shape a model has to fit within**.

Task 1.1 deleted the clause that decided it — "neither is a shape a model has to
fit within". What survives is its illustration, restored with the rest of the
chapter by task 22.2:

> A `5 × 1` floor and a `1 × 5` floor both contain five Unit Bases.

On its own that sentence makes no claim about what fits, so it does not
contradict `DEP-002`. It is also trivially true: `5 × 1` and `1 × 5` are the same
rectangle. It existed to illustrate a claim that is no longer in the document,
and now illustrates nothing.

**This is a deletion the maintainer asked for, not a repair.** Task 22.2
restored the line deliberately. It goes because the clause it served went.

- [x] 26.1 In `docs/06-deployment.md`, `DEP-001`, replace this anchor:

```
If only two dimensions are given, the Deployment Volume is **1 UB high**.

A `5 × 1` floor and a `1 × 5` floor both contain five Unit Bases.

Deployment Volumes may have any dimensions agreed upon by the players or defined by the scenario.
```

with:

```
If only two dimensions are given, the Deployment Volume is **1 UB high**.

Deployment Volumes may have any dimensions agreed upon by the players or defined by the scenario.
```

  **`W × D is the available floor area, counted in Unit Bases` is not touched.**
  There, "counted in Unit Bases" is the unit the floor is measured in, and task
  22.2 chose that word over "measured" on purpose.

### Verification

- [x] 26.2 `grep -c -F "floor both contain five Unit Bases" docs/06-deployment.md`
      returns **0**. It was 1.

- [x] 26.3 Read `DEP-001` and `DEP-002` in sequence. `DEP-001` agrees a box;
      `DEP-002` says what fills it, and that physical placement is the final
      check. Nothing between them counts, spends or budgets (`design.md`,
      Decision 5).

      **This is the fourth and last edit this change makes to
      `docs/06-deployment.md`** — see task 24.4 for the list. No hunk count is
      stated here: Part A and Part B are committed, so a diff against HEAD shows
      Part C alone and the running total tasks 22.8 and 24.4 tried to keep was
      never checkable from it.

- [x] 26.4 `python3 scripts/preflight.py` — every check green.

---

## 27. Three gaps the ruleset signposted, closed by ruling on them

**This section changes what a rule means, and the maintainer decided all three
rulings in it** (`design.md`, Decision 14). It is the second of the five rule
changes in this file; sections 28, 29 and 31 are the others.

The compression deleted two markers that told a reader a rule was not finished:

- `VEH-013` said "unless another crew member takes over **(future rules)**". The
  parenthesis went, turning an acknowledged gap into an exception a player will
  reach for — with no cost, no timing and no requirement stated anywhere.
- `VEH-031` said *"What `VEH-019` calls 'locomotion damage' is named there and
  defined by no rule; this rule does not define it either."* That went too, while
  `VEH-019` kept "locomotion damage" in its list of causes and `VEH-031` kept
  "A destroyed locomotion component is governed by `VEH-019`" — a pointer into
  the gap.

**Neither is restored as a marker. Both are defined.** The maintainer's rulings:

> Any team member may take control for 1 Action Point. Without a Pilot the
> vehicle does not move — someone has to take the controls.

> If the locomotion dies — wheels, tracks, legs, hover emitters — the vehicle loses one step, like infantry. Not cumulative, so it creates no confusion.
> And if the locomotion means is destroyed, the vehicle is Immobilized.

**The two rulings meet at the component/system line, and that is the reading
these tasks are written against**: one destroyed locomotion *component* costs a
step; the locomotion *system* entirely destroyed immobilizes the vehicle
(`VEH-012` — every vehicle represents one locomotion system). Without that line
the two rulings answer the same question twice.

**A third marker goes with them**, `VEH-025`'s "Freeing a stranded vehicle is not
currently defined":

> If it is in a hole it CANNOT be recovered. Full stop. If it is abandoned, what we said before.

That separates two cases the old text let a reader run together — a vehicle
nobody is driving, which task 27.1 answers, and a vehicle physically stuck, which
task 27.8 answers. After this section `docs/08-vehicles.md` carries no
"not yet defined" marker at all, and `TODO.md` loses the two entries that quoted
these sentences (task 27.9).

- [x] 27.1 In `docs/08-vehicles.md`, `VEH-013`, replace this anchor:

```
A vehicle without a Pilot, or with a Dead Pilot, cannot move unless another crew member takes over.
```

with:

```
A vehicle without a Pilot cannot move.

Any other minifigure aboard — crew (`VEH-015`) or passenger (`VEH-016`) — may take over for **1 Action Point**, physically moving into the operating position. That minifigure is the Pilot from then on.
```

  **"or with a Dead Pilot" goes, and it is not a loss.** A Dead component is
  removed from the model (`16-damage-system.md`, DMG-002), so a vehicle with a
  Dead Pilot is a vehicle without one. The clause named a state that cannot
  persist.

  The Action Point cost is written in the form `VEH-008` through `VEH-011`
  already use. The handover is a physical act because `VEH-013`'s own first
  sentence already requires a Pilot to occupy a visible operating position — no
  new mechanism is introduced to enforce it.

  **Passengers are included on purpose.** `VEH-015` is Crew and `VEH-016` is
  Passengers; restricting the handover to `VEH-015` would strand a full
  transport whose Pilot is gone.

- [x] 27.2 In `docs/08-vehicles.md`, `VEH-019`, replace this anchor:

```
This includes vehicles immobilized by Pilot loss, locomotion damage or being stranded (`VEH-025`).
```

with:

```
This includes vehicles immobilized by Pilot loss (`VEH-013`), destroyed locomotion (`VEH-031`) or being stranded (`VEH-025`).
```

  Each of the three causes now names the rule that defines it. "Locomotion
  damage" was the vague one — a Wounded wheel and a destroyed locomotion system
  are not the same thing, and `VEH-031` is where the difference is stated.

- [x] 27.3 In `docs/08-vehicles.md`, `VEH-031`, replace this anchor — **the rule
      heading is part of it**:

```
# VEH-031 — Wounded Pilot

A vehicle with a Wounded Pilot (`VEH-013`) moves **twice its own length** per movement action instead of three times (`VEH-004`).
```

with:

```
# VEH-031 — Reduced Movement

A vehicle moves **twice its own length** per movement action instead of three times (`VEH-004`) when its Pilot is Wounded (`VEH-013`) or a locomotion component is Dead (`16-damage-system.md`, DMG-002).
```

  The rule covers two causes now, so the title naming one is wrong. **It keeps
  its number and is retitled** — the thing no script reports (`design.md`,
  Decision 12), written down here for that reason.

- [x] 27.4 In `docs/08-vehicles.md`, `VEH-031`, replace this anchor — one table
      header row:

```
| Vehicle         |   Normal | Wounded Pilot |
```

with:

```
| Vehicle         |   Normal |       Reduced |
```

  **No number in the table changes**, and the column keeps its width, so the
  five data rows and the alignment row below stay aligned untouched.

- [x] 27.5 In `docs/08-vehicles.md`, `VEH-031`, replace this anchor:

```
Only the Pilot's Wounded state affects movement. A Wounded locomotion component does not change movement distance.

A destroyed locomotion component is governed by VEH-019.
```

with:

```
The reduction is not cumulative. A vehicle moves twice its own length whether one cause applies or both, and however many locomotion components are Dead.

A Wounded locomotion component does not change movement distance.

A vehicle whose locomotion is entirely destroyed cannot move and is Immobilized (`VEH-019`).
```

  "Only the Pilot's Wounded state affects movement" is deleted because task 27.3
  makes it false.

  The last line is what stops a vehicle with no wheels left from rolling at two
  lengths a turn. It is a separate binary case rather than more arithmetic, which
  is what "not cumulative" asks for.

- [x] 27.6 In `docs/08-vehicles.md`, `VEH-004`, replace this anchor — one line
      below the movement table:

```
A Wounded Pilot reduces this to twice the vehicle's length (VEH-031).
```

with:

```
A Wounded Pilot or a Dead locomotion component reduces this to twice the vehicle's length (VEH-031).
```

- [x] 27.7 In `docs/08-vehicles.md`, the Summary, replace this anchor:

```
A Wounded Pilot reduces movement from three lengths to two.
```

with:

```
A Wounded Pilot or a Dead locomotion component reduces movement from three lengths to two.
```

  These two state `VEH-031`'s effect away from `VEH-031`. Task 27.3 gives the
  rule a second cause, and a summary that names one of two is the defect this
  whole change exists to remove.

- [x] 27.8 In `docs/08-vehicles.md`, `VEH-025`, replace this anchor:

```
Freeing a stranded vehicle is not currently defined.
```

with:

```
A stranded vehicle cannot be freed.
```

  **The third marker, and it closes rather than survives.** The maintainer's
  ruling: *"If it is in a hole it CANNOT be recovered. Full stop. If it is
  abandoned, what we said before."*

  A stranded vehicle sits in a depression deeper than its Terrain Threshold, and
  nothing in the ruleset lifts a model out of one. "Not currently defined"
  invited a house rule for a case the model already answers — the vehicle is in
  the hole, and it stays there.

  **This is not the Pilot handover.** Task 27.1 covers a vehicle whose Pilot is
  gone; this covers one that is physically stuck. The two were reachable from the
  same sentence before, which is why they are separated here.

- [x] 27.9 In `TODO.md`, replace this anchor — two whole entries:

```
### A crew member taking over from a dead Pilot

`VEH-013` (`docs/08-vehicles.md`):

> A vehicle without a Pilot, or with a Dead Pilot, cannot move unless another crew member takes over.

What would have to be decided: which crew positions are eligible to take over, whether taking over costs AP, and whether it requires a dedicated action or happens automatically.

### Freeing a stranded vehicle

`VEH-025` (`docs/08-vehicles.md`):

> Freeing a stranded vehicle is not currently defined.

What would have to be decided: whether a stranded vehicle can be freed at all, by whom, and what action or cost would be required.

### Reverse movement restrictions
```

with:

```
### Reverse movement restrictions
```

  **This is not optional tidying.** `TODO.md` quotes the ruleset verbatim and
  `scripts/check_todo_quotes.py` verifies every quote against the document it
  cites — a required check. Tasks 27.1 and 27.8 delete both quoted sentences, so
  leaving these entries fails the gate.

  Each entry asks a question this section answers. "Which crew positions are
  eligible, whether taking over costs AP" — any minifigure aboard, 1 Action
  Point. "Whether a stranded vehicle can be freed at all" — it cannot. A closed
  gap leaves `TODO.md` rather than staying with an answer attached
  (`TODO.md`'s own second paragraph).

  `VEH-011`'s lateral-movement entry and the other three stay: nothing here
  touches them.

### Verification

- [x] 27.10 `grep -c -F "future rules" docs/08-vehicles.md` — `VEH-011`'s
      "Future rules may introduce lateral movement" is capitalised, so this
      returns **0**. A **1** means an unrelated marker was introduced.

- [x] 27.11 `grep -c -F "Wounded Pilot" docs/08-vehicles.md` returns **2**. It
      was 5. The two survivors are `VEH-004`'s line and the Summary's, both
      rewritten by tasks 27.6 and 27.7 to name the second cause as well; the three
      that go are `VEH-031`'s heading, table header and body sentence.

- [x] 27.12 `grep -c -F "not currently defined" docs/08-vehicles.md` returns
      **0**. It was 1, and task 27.8 is the only task that touches it.

- [x] 27.13 `python3 scripts/check_todo_quotes.py` — every surviving quote still
      appears verbatim in the document it cites. This is the check task 27.9
      exists for.

- [x] 27.14 `python3 scripts/rule.py refs VEH-031 VEH-019 VEH-013` — `VEH-031`
      gains `VEH-019` as a citer and `VEH-013` keeps its own. No citer names a
      rule that does not exist.

- [x] 27.15 `python3 scripts/build_index.py` — `VEH-031`'s title changed and the
      index carries titles.

- [x] 27.16 `python3 scripts/preflight.py` — every check green.

- [x] 27.17 Read `VEH-004`, `VEH-013`, `VEH-015`, `VEH-016`, `VEH-019`, `VEH-025`
      and `VEH-031` in full, plus the document's Summary. Three questions a reader
      must be able to answer afterwards: what a vehicle whose Pilot is gone does,
      what a vehicle with one destroyed wheel does that a vehicle with no
      locomotion at all does not, and what happens to a vehicle in a hole.

      **`16-damage-system.md:86-92` and the glossary's *Wounded* entry are
      deliberately untouched.** Both enumerate **Wounded**-state degradations,
      and both say a Wounded wheel loses nothing — which task 27.5 keeps true. A
      Dead locomotion component is not a Wounded degradation, so neither list
      gains an entry.

      **No "not yet defined" marker survives in this document**, and that is the
      result rather than an accident: all three were closed by a ruling.

---

## 28. Nothing is repaired, and infantry stands back up

**A rule change, and the third in this file** (`design.md`, Decision 15).

The audit found `DMG-018` ambiguous: it charges 1 Action Point once per
activation to repair one of a unit's own Wounded components, then lists what
"repairing another unit requires" without saying whether that cost still applies.
`main` had the word that decided it — *"Repairing a **different** unit's Wounded
component **additionally** requires..."* — and the compression deleted it.

The maintainer's ruling removes the question instead of answering it:

> I would remove the ability to repair anything. If it is broken, it broke, full stop. It cannot be repaired.
> The exception is infantry, which for 1 AP reverts the state machine.

So repair goes, and one reversal survives: a Wounded infantry model stands back
up. `DMG-002` already maps the states to poses — upright, seated, removed — so
standing up *is* the state change, shown on the model rather than tracked beside
it.

**Blast radius is two edits in one file.** `python3 scripts/rule.py refs DMG-018`
reports **cited by nothing**, `docs/14-glossary.md` has no *Repair* entry, and no
other document uses the word.

- [x] 28.1 In `docs/16-damage-system.md`, replace this anchor — **the rule
      heading is part of it**:

```
## DMG-018 — Repairs

A unit may spend **1 Action Point**, once per activation, to repair one of its own Wounded components.

The component returns:

**Wounded → Operational**

For infantry, this is represented by standing the minifigure back up.

Repairing another unit requires:

* A visible repair tool or equipment.
* Physical adjacency to the target.

Dead components cannot be repaired because they have already been removed from the model.

Repairs reverse a Wounded state but do not recreate destroyed physical components.
```

with:

```
## DMG-018 — Recovery

A damaged component is not repaired. What is broken stays broken.

Any Wounded minifigure may spend **1 Action Point** to return to Operational — infantry on foot, and a Pilot or crew member inside a vehicle alike.

**Wounded → Operational**

A Dead component cannot return. It has already been removed from the model (`DMG-002`).
```

  The rule keeps its number and is retitled — the thing no script reports
  (`design.md`, Decision 12).

  **No "exception" framing, and the Pilot is named.** Calling it an exception
  described the rule's history rather than the rule; a reader meeting `DMG-018`
  fresh needs to know who recovers, not what used to be possible. The maintainer's
  own reading was that a Pilot's case was not obvious by inference, so the rule
  says it.

  **No citation of `CORE-003`, deliberately.** That rule says infantry *are*
  minifigures; it does not say every minifigure is infantry, which is the
  direction the claim needs. Citing it would be the defect section 2 of this
  change repaired twenty-eight times — an ID that exists and does not carry the
  claim attached to it. The rule states the case outright instead.

  **"Return to Operational" rather than "stand back up".** `DMG-002` already maps
  the states to poses — upright, seated, removed — so naming the state names the
  pose, and copying the mapping here would give it two owners. It also reads
  correctly for a Pilot, seated in the cockpit either way.

  **"Once per activation" goes because it now guards nothing.** The old rule let
  a unit pick among its own components; the new one has a single subject, and a
  model that is standing cannot stand again.

  The repair tool and the adjacency requirement go with the capability they
  qualified. `CORE-014` is untouched — it is the general rule that equipment must
  be on the model, and it was never about repairs.

- [x] 28.2 In `docs/16-damage-system.md`, the Summary, replace this anchor — one
      bullet:

```
* Repairs
```

with:

```
* Recovery
```

### Verification

- [x] 28.3 `grep -c -i repair docs/16-damage-system.md` returns **1**. It was 7.

      **The survivor is task 28.1's own replacement text** — "A damaged component
      is **not repaired**." A **0** means 28.1 did not apply. A **2 or more** means
      a mention outside the two anchors was missed.

- [x] 28.4 `grep -rn -i repair docs/` — every hit is the one in
      `16-damage-system.md`. No other document mentioned repair before this
      section and none may after.

- [x] 28.5 `python3 scripts/rule.py orphans` — `DMG-018` was already on the list
      and stays there. It is standalone rather than disconnected: the resolution
      sequence reaches it, exactly as `V.2` records for `DMG-012` and `DMG-015`.

- [x] 28.6 `python3 scripts/build_index.py` — `DMG-018`'s title changed and the
      index carries titles.

- [x] 28.7 `python3 scripts/preflight.py` — every check green.

- [x] 28.8 Read `DMG-002` and `DMG-018` together. `DMG-002` states the three
      states and the poses that show them; `DMG-018` states the only transition
      that runs backwards.

      **A Pilot recovers, and the rule says so out loud.** `CORE-003` makes every
      minifigure an infantry model, so it followed already — but it followed by
      inference, and the rule now names the case. A recovered Pilot also lifts
      `VEH-031`'s reduced movement.

      **Pre-existing and not fixed here:** `DMG-002` shows infantry states by
      pose — upright, seated, removed — and a Pilot is seated in its operating
      position whether Operational or Wounded, so the pose distinguishes nothing
      for a crewed vehicle. That is true on `main` and this section does not make
      it worse. Report it; do not solve it in this change.

---

## 29. A minifigure's shoulder is a rotating mount, and rotation has reach

**A rule change, and the fourth in this file** (`design.md`, Decision 16).

`CBT-007` permits a weapon system to split its Attack Dice between targets "only
when its mount can physically rotate to re-aim independently of the platform
carrying it, such as a turntable, ball joint or swivel mount", and forbids it to
fixed mounts. `WPN-009` lists **Hands** as a valid mount, and a minifigure's arm
turns at the shoulder.

**The rule therefore reads both ways for every infantry model in the game.** A
minifigure carrying a four-muzzle weapon either engages four targets or one, for
the same single Action Point (`CBT-006`), and nothing in the text decides which.

The retired `DMG-018` had decided it — *"Examples of free rotation (exception
applies): minifig torso, turntable, ball joint, swivel mount. This deliberately
puts all infantry-carried weapon systems under the exception ... this is
intentional, not an oversight."* Consolidating into `CBT-007` was right; dropping
the decision was not (`system/proposal-review.md`, "Record What You Decided Not
to Do").

The maintainer's ruling restores the answer and narrows it:

> Go to the human. Without turning the body, the arm can aim at several targets as long as those targets are in front of the minifigure. The rule applies to the minifigure too, because the rotation point is not the HAND, it is the SHOULDER.

**That is stricter than the retired text, which named the minifig *torso*.**
Turning the torso is turning the body, which this ruling excludes. The arm alone
is what re-aims.

- [x] 29.1 In `docs/11-combat.md`, `CBT-007`, replace this anchor:

```
Its dice may be split between multiple targets only when its mount can physically rotate to re-aim independently of the platform carrying it, such as a turntable, ball joint or swivel mount.

Fixed mounts cannot split their Attack Dice between targets.
```

with:

```
Its dice may be split between multiple targets only when its mount can physically rotate to re-aim independently of the platform carrying it, such as a turntable, ball joint, swivel mount or a minifigure's shoulder — the rotation point is the shoulder, not the hand.

Each target must be one the mount reaches by rotating alone, without turning the platform. A minifigure's arm therefore covers the targets in front of it and no others.

Fixed mounts cannot split their Attack Dice between targets.
```

  Two things, and the second is general rather than infantry-specific:

  **The shoulder is named**, which is what closes `WPN-009`'s *Hands* case. The
  weapon is held in the hand; the mount that rotates is the shoulder.

  **Rotation has reach.** A turret turning 360° is limited by nothing; a swivel
  mount with short travel is limited by its travel; an arm is limited to the
  front. The minifigure sentence is the worked instance of that rule, not an
  exception beside it.

  **No arc in degrees, deliberately.** The ruleset has no angular measure —
  `WPN-011` says only "Weapon position determines its firing arc" and `CBT-002`
  resolves visibility physically, from the attacker's point of view. The check is
  made on the model: point the arm at the target, and if it reaches without
  turning the body, the target is legal.

- [x] 29.2 In `docs/11-combat.md`, `CBT-007`, replace this anchor — the procedure
      list for a split attack:

```
* All targets must be declared before any die is rolled.
* Line of Sight is checked separately for each target.
* Weapon Range is checked separately for each target.
* A die assigned to a target that fails either check has no valid target and is not rolled.
```

with:

```
* All targets must be declared before any die is rolled.
* The mount must reach each target by rotating alone.
* Line of Sight is checked separately for each target.
* Weapon Range is checked separately for each target.
* A die assigned to a target that fails any of these checks has no valid target and is not rolled.
```

  **Task 29.1 adds a third per-target condition and this list is the operative
  procedure.** Left as it was, the list enumerates two conditions and "either
  check" fixes the count at two, so a player following the procedure never
  applies the reach limit the section exists to add.

  Nothing else in the list changes, and no new mechanic appears — the bullet
  restates 29.1's sentence where the procedure is carried out.

### Verification

- [x] 29.3 `grep -c -F "the rotation point is the shoulder, not the hand"
      docs/11-combat.md` returns **1**.

- [x] 29.4 `grep -c -F "fails either check" docs/11-combat.md` returns **0**.
      Task 29.2 is the only task that touches that phrase.

- [x] 29.5 `grep -rn "minifig torso, turntable" docs/` returns nothing. The
      retired wording is not restored anywhere — this section states the shoulder
      instead, and the two are not the same joint.

      **Not a bare `minifig torso`**: `DMG-004`'s Resistance example says "A
      typical minifig torso is approximately one brick thick", which is unrelated
      to weapon mounts and stays.

- [x] 29.6 `python3 scripts/preflight.py` — every check green.

- [x] 29.7 Read `CBT-006`, `CBT-007` and `WPN-009` in that order, plus `WPN-011`.
      The question a reader must be able to answer: whether a minifigure with a
      four-muzzle weapon may engage two enemies standing in front of it, and
      whether it may engage one standing behind.

      **`WPN-011`'s "Weapon position determines its firing arc" is deliberately
      untouched.** It states the same idea for a mounted weapon and states it
      physically; task 29.1 gives the general rule its own sentence in the rule
      that needs it, without turning either into a number.

---

## 30. `assets/IMAGES.md` argues from text that no longer exists

**A repair, not a rule change.** `assets/IMAGES.md` is referential — it specifies
images a later process should draw and nothing in `docs/` depends on it — so the
standard is that every claim it makes about a rule is currently true. Several are
not.

Two facts, checked rather than assumed:

- `grep -rn "█ ■ ● ○ · ▪ ▫ ░ ▒ □" docs/` returns **nothing**.
- `grep -c '```' docs/10-weapons.md` returns **0**.

The compression removed every character grid from the ruleset. Three whole
sections of this file exist to discuss those grids, two image entries were
promoted into the list *because* of them, and five "Why text alone is not enough"
columns quote sentences their rules no longer carry.

The maintainer's instruction: **leave only what is needed, delete what does not
exist.**

- [x] 30.1 In `assets/IMAGES.md`, delete three sections. Replace this anchor:

```
## Images supplement the text; they do not replace it

When an image lands, **leave the ASCII block in the rule.** The column above is headed *"Why text alone is not enough"*, not *"what the text should be replaced by"*.

`docs/` is read in a terminal, through `grep`, and by screen readers. A rule whose only diagram is a `.png` becomes unreadable in all three the moment images do not load. Two representations of one spatial fact in different media is not the duplication this repo works to remove — that is two *rules* stating the same mechanic, which can drift apart into a contradiction. A picture and its text alternative cannot contradict each other; at worst one is less clear.

## Why the weapon grids are worth illustrating at all

The three grid rules use overlapping symbols with different meanings, and no rule carries a legend:

| Symbol | WPN-007 | WPN-019 | WPN-020 |
|---|---|---|---|
| `█` | a functional muzzle | — | a size-2 muzzle |
| `■` | — | a footprint slot | the unpartitioned footprint |
| `●` | — | — | a size-1 muzzle |
| `·` | unused footprint | — | unused footprint |

A reader meeting `██··` in WPN-007 has to reconstruct that legend from rules further down the document, where the same characters mean something narrower. One consistent visual language across the three images removes that problem entirely — which is a better reason for these images than any individual diagram being hard to picture.

The remaining notations are the three above. A fourth — a hollow `○` for a muzzle, where WPN-020 uses a filled `●` — is gone from the ruleset along with the rules that carried it.

## Coverage of the character grids

A full scan of `docs/` for block and shape glyphs (`█ ■ ● ○ · ▪ ▫ ░ ▒ □`) finds nine fenced grid blocks. All nine are in `10-weapons.md`, and all belong to the three rules listed in that section above — one in WPN-007, three in WPN-019, five in WPN-020. No other document represents LEGO geometry as characters, and there is no ASCII minifigure anywhere in the ruleset.

The remaining fenced blocks stay as they are. Formulas are equations and an image would be worse than the text. Directed graphs belong in Mermaid, which stays diffable, rather than in a raster image.

---

## docs/02-core-rules.md
```

with:

```
## docs/02-core-rules.md
```

  All three describe character grids. The first instructs a future editor to
  "leave the ASCII block in the rule"; there is none to leave. The second is a
  legend for symbols no document uses. The third counts nine fenced blocks where
  there are zero.

  **Nothing is re-derived to replace them.** The argument they made was about a
  representation the ruleset no longer uses.

- [x] 30.2 In `assets/IMAGES.md`, `CORE-001`'s row, replace this anchor:

```
| CORE-001 | `assets/images/core-001-unit-base-volume.png` | Three panels. First, the Unit Base as a volume, dimensioned 4 studs wide × 3 studs deep × 13 plate layers tall, with a model inside it and the base it stands on drawn within the volume rather than below it. Second, the same volume seen from above, dimensioned `4 × 3` studs. Last, a "2 × 3 UB" footprint measuring 8 × 9 studs, beside a 6 × 12 rectangle marked wrong. | Two geometric facts here are carried by prose alone: that the unit encloses space rather than covering it, and that the base a model stands on is inside the volume rather than the floor under it — the rule says the height is measured from that base's underside, which a reader has to picture to apply. The rule text itself flags the 8×9-vs-6×12 confusion as one readers get wrong. |
```

with:

```
| CORE-001 | `assets/images/core-001-unit-base-volume.png` | Three panels. First, the Unit Base as a volume, dimensioned 4 studs wide × 3 studs deep × 13 plate layers tall, with a model inside it and the base it stands on drawn within the volume rather than below it. Second, the same volume seen from above, dimensioned `4 × 3` studs. Last, a `2 × 3 UB` footprint measuring 8 × 9 studs, with the multiplication marked on both axes. | Two geometric facts here are carried by prose alone: that the unit encloses space rather than covering it, and that the base a model stands on is inside the volume rather than the floor under it — the rule says the height is measured from that base's underside, which a reader has to picture to apply. |
```

  The `6 × 12` rectangle and the sentence claiming the rule flags that confusion
  both go: `CORE-001` states `8 × 9` and never mentions `6 × 12`. What survives is
  the multiplication itself, which is still the fact worth drawing.

- [x] 30.3 In `assets/IMAGES.md`, `CMP-018`'s row, replace this anchor:

```
| CMP-018 | `assets/images/cmp-018-clear-opening.png` | A doorway in a vehicle wall, twice. Both times the frame's nominal aperture is dimensioned in studs and plate layers, a hinged element hangs part-way across it, and the measurement that counts is drawn around that element rather than around the frame — labelled as the clear opening. In the first, an opening 4 studs wide and 13 plate layers clear — one Unit Base — passes the model; in the second the same frame fails it, with only the hanging element differing between the two. | The frame is what a reader measures and the wrong thing to measure, and no wording of "clear rather than nominal" makes two identical frames visibly different sizes — a drawing of one doorway with two measurements does. It is also the only one of GEO-004's three physical checks that needs an image of its own: Cover is declined separately at CORE-010, and Line of Sight is whatever can physically be seen from where the shooter stands, which no drawing of one build settles. |
```

with:

```
| CMP-018 | `assets/images/cmp-018-clear-opening.png` | A doorway in a vehicle wall, twice. Both times the frame's nominal aperture is dimensioned, a hinged element hangs part-way across it, and the measurement that counts is drawn around that element rather than around the frame — labelled as the clear opening, and dimensioned against the model beside it: at least as wide as that model's front edge and as tall as it stands. In the first the model passes; in the second the same frame fails, with only the hanging element differing between the two. | The frame is what a reader measures and the wrong thing to measure, and no wording of "clear rather than nominal" makes two identical frames visibly different sizes — a drawing of one doorway with two measurements does. It is one of GEO-004's physical checks that needs an image of its own: Cover is declined separately at CORE-010, and Line of Sight is whatever can physically be seen from where the shooter stands, which no drawing of one build settles. |
```

  `CMP-018` no longer measures a Unit Base. It measures the model that uses the
  opening — "at least as wide as the model's front edge and as tall as the model
  stands" — so the image is dimensioned against the model, not against a fixed
  4 × 13.

  **"the only one of `GEO-004`'s three physical checks" also goes.** Section 31
  moves Resistance into `GEO-004`, so the list is no longer three and
  access-opening clearance is no longer the only entry with an image — `DMG-003`
  has one.

- [x] 30.4 In `assets/IMAGES.md`, `VEH-024`'s row, replace this anchor:

```
| VEH-024 | `assets/images/veh-024-hover-assembly-height.png` | A hover vehicle's emitter/pylon/skirt assembly with its full height marked from the ground to the hull, including an enclosed skirt that reaches the ground and leaves no visible gap. | The rule explicitly warns that "measuring the assembly rather than the visible gap matters for enclosed builds" — the intuitive reading (measure the gap) is wrong, and only a picture can pre-empt that mistake. |
```

with:

```
| VEH-024 | `assets/images/veh-024-hover-assembly-height.png` | A hover vehicle's emitter/pylon/skirt assembly with its full height marked from the ground to where it meets the hull, including an enclosed skirt that reaches the ground and leaves no visible gap. | The threshold is the assembly's height, and the intuitive reading is the gap under the hull. On an enclosed skirt the two differ by the whole assembly and the gap is zero, so the wrong reading produces a legal-looking answer rather than an obviously absent one. |
```

  The quoted warning is not in `VEH-024`. The argument is rewritten from what the
  rule now says — ground to where the assembly meets the hull — rather than from
  a sentence that was deleted.

- [x] 30.5 In `assets/IMAGES.md`, `WPN-003`'s row, replace this anchor:

```
| WPN-003 | `assets/images/wpn-003-length-axis-front-face.png` | A weapon body with its firing axis drawn perpendicular through the Weapon Front, and the Weapon Front Footprint (WPN-019) outlined on that face, distinguished from the other five faces of the body. | Weapon Length is defined via an axis "perpendicular to the Weapon Front," and the Weapon Front is itself "the only face from which the weapon may fire" — two spatial definitions that depend on each other and are easy to reverse without a 3D view. |
```

with:

```
| WPN-003 | `assets/images/wpn-003-length-axis-front-face.png` | A weapon body with its firing axis drawn along the body, Weapon Length measured along that axis and Weapon Width marked as the body's smallest dimension, and the Weapon Front (WPN-019) outlined on the face the axis exits, distinguished from the other five faces. | Length and Width are two dimensions of one body read against different axes, and the Weapon Front is the only face the weapon fires from — three spatial facts that depend on each other and are easy to reverse without a 3D view. |
```

  Two reasons. The quoted "perpendicular to the Weapon Front" is not `WPN-003`'s
  wording. And task 25.1 gives the rule Weapon Width, which every muzzle count
  derives from — the image that illustrates the rule should show both dimensions
  it defines.

- [x] 30.6 In `assets/IMAGES.md`, delete the `WPN-007` and `WPN-019` rows.
      Replace this anchor:

```
| WPN-007 | `assets/images/wpn-007-muzzle-adjacency.png` | A Weapon Front Footprint holding two muzzles that share an edge, marked valid, beside the same footprint with two muzzles overlapping, marked invalid. Unused footprint cells visibly distinct from occupied ones. | The rule's `██··` block is the whole explanation and carries no legend, so a reader must infer that `█` is a muzzle and `·` is unused footprint from a later rule that uses the same characters for something narrower. The image also has to show that adjacency is allowed and only overlap is not — a distinction four characters cannot carry. |
| WPN-019 | `assets/images/wpn-019-front-footprint-sizes.png` | The Weapon Front Footprint at Widths 1, 2 and 4 — a square of side Weapon Width — shown against the weapon body so the relationship between body width and available muzzle space is visible. | The rule shows three character squares with no indication of scale or of how they sit on the weapon. The footprint is the space every muzzle competes for, so getting its size wrong invalidates every weapon built from it. |
| WPN-020 | `assets/images/wpn-020-muzzle-placement.png` | Five panels: the unpartitioned Weapon Front Footprint the rule starts from, then that same footprint partitioned as twin barrel, quad barrel, heavy cannon and hybrid, each labelled with the Attack Dice and Impact Strengths it produces. | The rule's own ASCII diagrams compress a genuinely spatial muzzle layout into a flat character grid. A real image showing the same footprint yielding several distinct, valid weapons makes "no fixed weapon profile" concrete. |
```

with:

```
| WPN-020 | `assets/images/wpn-020-muzzle-placement.png` | Five panels: the unpartitioned Weapon Front Footprint the rule starts from, then that same footprint partitioned as twin barrel, quad barrel, heavy cannon and hybrid, each labelled with the Attack Dice and Impact Strengths it produces. | The rule lists its configurations as text and the layout they describe is spatial. One footprint shown yielding four distinct, valid weapons is what makes "no fixed weapon profile" concrete. |
```

  **Both deleted rows were promoted into this list because of the grids**, in
  their own words: `WPN-019` "has three character grids of its own", and a reader
  of `WPN-007` "still meets a bare `██··` and no legend". Neither rule carries a
  grid now, so neither promotion stands. Task 30.9 returns them to the rejected
  list with that reason rather than dropping them silently.

  `WPN-020` stays — a muzzle layout is spatial whatever notation the rule uses —
  and its column stops citing ASCII diagrams that are gone.

- [x] 30.7 In `assets/IMAGES.md`, `DMG-003`'s row, replace this anchor:

```
| DMG-003 | `assets/images/dmg-003-resistance-cross-section.png` | A shield built from bricks (Resistance 3) and a similarly-sized shield built from four stacked plates (Resistance 4), both with the Impact's direction of travel marked, showing Resistance as the layer count crossed, not the external silhouette. | The rule's own text notes that two builds of "similar external bulk" resolve to different Resistance values — the whole point is that the model's outside doesn't tell you the answer. Only a cross-section view can show that. |
```

with:

```
| DMG-003 | `assets/images/dmg-003-resistance-cross-section.png` | A shield built from bricks (Resistance 3) and a similarly-sized shield built from four stacked plates (Resistance 4), both with the Impact's direction of travel marked, showing Resistance as the layer count crossed, not the external silhouette. | Resistance is the thickness an Impact crosses in its direction of travel, so two shields of the same external size resolve differently depending on what they are built from. The outside of the model does not carry the answer, and only a cross-section shows it. |
```

  The quoted "similar external bulk" is not in `DMG-003`. The argument survives —
  it is exactly what the rule's conversion table and "only material actually
  crossed" mean — and is written from those instead.

- [x] 30.8 In `assets/IMAGES.md`, the totals, replace this anchor:

```
**22 images** specified, across 8 of the 15 ruleset documents
```

with:

```
**20 images** specified, across 8 of the 15 ruleset documents
```

  Task 30.6 removes two. The document count is unchanged: `10-weapons.md` keeps
  `WPN-003` and `WPN-020`.

- [x] 30.9 In `assets/IMAGES.md`, the rejected list, replace this anchor:

```
- ~~**WPN-007 (Muzzle Adjacency)**~~ — **Reclassified; now specified above.** Originally folded into the WPN-020 image on the grounds that adjacency is visible in those worked examples. That was correct under the original criterion, which asked whether the *concept* needed illustrating. It was reclassified when the criterion widened: a folded image inside WPN-020 does nothing for a reader of WPN-007, who still meets a bare `██··` and no legend.
- ~~**WPN-019 (Weapon Front Footprint)**~~ — **Reclassified; now specified above.** Originally covered by WPN-003's image, which outlines the footprint on the weapon front. Same reasoning as WPN-007: WPN-019 has three character grids of its own, and an illustration living in another rule does not replace them.
```

with:

```
- **WPN-007 (Muzzle Adjacency)** — Adjacency and overlap are visible in WPN-020's worked examples, and whether two muzzles overlap is a check made on the built weapon. It was specified for a while, on the grounds that a reader met a bare `██··` block with no legend; the block is gone and the grounds with it.
- **WPN-019 (Weapon Front Footprint)** — Covered by WPN-003's image, which outlines the footprint on the weapon front. It was specified for a while, because the rule carried three character grids of its own; those are gone and the grounds with them.
```

  The file's own **Reclassifying** convention asks that a judgement reversed be
  visible rather than silent, which is why these keep their entries and say what
  changed. The strikethrough goes because the entries are no longer reclassified
  *out* of this list — they are back in it.

- [x] 30.10 In `assets/IMAGES.md`, the "Rewritten because the rule changed under
      them" section, replace this anchor:

```
- **`CMP-018`** specified "the Unit Base's vertical projection" fitting a clear opening. Same removal; the rule now states 4 studs wide and 13 plate layers clear, and the entry says so.
```

with:

```
- **`CMP-018`** specified "the Unit Base's vertical projection" fitting a clear opening. Same removal; the rule now measures the model that uses the opening, and the entry says so.
```

  `CMP-018` stopped stating a fixed `4 × 13` clearance. This bullet described the
  entry as matching a rule text that no longer exists — the same defect the
  section it sits in was written to record.

- [x] 30.11 In `assets/IMAGES.md`, the rejected list, replace this anchor:

```
- **WPN-002 (Functional Muzzle), WPN-018 (Weapon Proportion)** — Neither displays a character grid. WPN-002 is a definition, and WPN-018 states a proportion as an inequality with valid/invalid dimension lists that read perfectly well as text. An image would add nothing to either.
```

with:

```
- **WPN-002 (Functional Muzzle), WPN-018 (Weapon Proportion)** — WPN-002 is a definition, and WPN-018 states a proportion as an inequality with valid/invalid dimension lists that read perfectly well as text. An image would add nothing to either.
```

  **A third live claim about character grids**, and the last one. No rule in
  `docs/` displays a grid, so "Neither displays a character grid" is a criterion
  this section abolishes — it reads as a live test a future candidate could
  fail. The two reasons that follow it are sound and stay.

- [x] 30.12 In `assets/IMAGES.md`, the rejected list, replace this anchor:

```
Of the three physical checks GEO-004 lists, Cover is declined at CORE-010 above and Line of Sight is settled from the shooter's own viewpoint rather than from any diagram; only access-opening clearance needs an image of its own, and it has one under `docs/05-construction-components.md` (CMP-018).
```

with:

```
Of the physical checks GEO-004 lists, Cover is declined at CORE-010 above and Line of Sight is settled from the shooter's own viewpoint rather than from any diagram; access-opening clearance needs an image of its own, and it has one under `docs/05-construction-components.md` (CMP-018).
```

  Same repair as in task 30.3, in the second place the claim is made. Section 31
  moves Resistance into `GEO-004`, so the list is not three and access-opening
  clearance is not the only entry with an image — `DMG-003` has one.

### Verification

- [x] 30.13 `grep -c "ASCII\|character grid\|glyph" assets/IMAGES.md` returns
      **1** — the rejected-list bullet for `WPN-019`, which names "character
      grids" as the reason the entry was specified and the reason it no longer
      is.

      **Read that hit rather than trusting the count.** It must read as a record
      of a reversed judgement, not as a live claim about `docs/`. The `WPN-007`
      bullet matches none of the three terms; it names `██··` instead, for the
      same historical reason.

- [x] 30.14 `grep -c -F "| WPN-0" assets/IMAGES.md` returns **2** — `WPN-003` and
      `WPN-020`.

      **It was 5, not 4.** Four image rows, plus the symbol-legend table header
      `| Symbol | WPN-007 | WPN-019 | WPN-020 |` that task 30.1 deletes with its
      whole section.

- [x] 30.15 `grep -c -F "three physical checks" assets/IMAGES.md` returns **0**.
      Tasks 30.3 and 30.12 are the only tasks that touch that phrase.

- [x] 30.16 `python3 scripts/lint_ruleset.py` — every filename still follows the
      convention, names a document that exists, and illustrates a rule that exists
      in it. This is the check that covers `assets/IMAGES.md`
      (`.claude/rules/assets.md`).

- [x] 30.17 `python3 scripts/preflight.py` — every check green.

- [x] 30.18 Read `assets/IMAGES.md` end to end against `docs/`. Every "Why text
      alone is not enough" column must be an argument about the rule as it now
      reads, and every quotation in one must still appear in the rule it names.

      **This file has no mechanical guard for that** — `lint_ruleset.py` checks
      filenames and rule existence, not whether a column describes the rule
      truthfully. Its own "Rewritten because the rule changed under them" section
      says so, and this section is the second time it has had to be run.

---

## 31. Resistance is a physical check, not a measured value

**A rule change, and the fifth in this file** (`design.md`, Decision 17). It is
the widest one here: three documents, and it moves a term between two of
`15-geometry-layers.md`'s categories rather than editing a sentence.

The audit reported `GEO-002` and `DMG-003` contradicting each other over
decorative armour. The contradiction is milder than reported — `DMG-003` says
"smallest **structural** section", and that word already excludes decoration — but
**nothing tells a reader whether a plate added outside a wall is structural**, and
`GEO-002`'s replacement sentence restates the question instead of answering it:

> A decorative element becomes Gameplay Geometry if it physically forms part of the structure or functional geometry measured by another rule.

`main` had answered it — decorative armour *bolted on top of* a wall does not add
Resistance — and the compression deleted that sentence. The maintainer's ruling
goes the other way:

> If it has "something" in front of the brick it adds to the path. A brick with a plate outside it — that is part of the hull, not decoration. Decoration is a tile with a print on it, a sticker. If you put a plate there it is already part of the hull.

### Why this is a move rather than a patch

`15-geometry-layers.md` sorts everything into two boxes. `GEO-003` holds the
**measured values**, which ignore Visual Geometry. `GEO-004` holds the **physical
checks**, which use the model exactly as it exists on the table, Visual Geometry
included.

Under the ruling, Resistance is read from the plastic in the Impact's path. That
is `GEO-004`'s definition word for word, and Resistance is currently in
`GEO-003`'s list — so the fix is to move it. Patching `GEO-002` would leave the
category that discards decoration before the direction of travel is even
considered.

**Decorative armour is not promoted to Gameplay Geometry.** It stays Visual: it
still does not change weapon Range or Attack Dice (`GEO-005`), and still does not
count toward vehicle height (`VEH-030` lists it as Visual). What changes is only
that Visual Geometry stops being discarded when something has to cross it.

**The same build yields different Resistance from different directions**, and
that is correct rather than a defect — `DMG-003` already says "in its direction
of travel". A wall plated on one face resists more from that face than from the
bare one.

- [x] 31.1 In `docs/15-geometry-layers.md`, `GEO-001`, replace this anchor:

```
* Movement geometry
* Component structural thickness

Derived values such as Range, Attack Dice, Impact Strength, Resistance and Capacity are calculated from Gameplay Geometry by their respective rules.
```

with:

```
* Movement geometry

Derived values such as Range, Attack Dice, Impact Strength and Capacity are calculated from Gameplay Geometry by their respective rules.
```

  Both mentions leave for the same reason: thickness in an Impact's path is read
  from the model as built, so it is neither an example of Gameplay Geometry nor a
  value derived from it.

- [x] 31.2 In `docs/15-geometry-layers.md`, `GEO-002`, replace this anchor:

```
A decorative element becomes Gameplay Geometry if it physically forms part of the structure or functional geometry measured by another rule.
```

with:

```
Material an Impact must cross is never ignored: a plate or panel outside a wall is part of what the Impact crosses and adds to its Resistance (`16-damage-system.md`, DMG-003; `GEO-004`). What is decorative is the printing on a piece, not the piece.
```

  The circular sentence goes. The replacement answers the question a reader
  arrives with — a plate is plastic in the way, printing is not — and points at
  the two rules that now own the answer.

  **The example list above it is not touched.** Cosmetic armour and decorative
  plates remain Visual Geometry, because they still change no measured value.

- [x] 31.3 In `docs/15-geometry-layers.md`, `GEO-003`, replace this anchor:

```
* Range
* Attack Dice
* Impact Strength
* Resistance
* Weapon Capacity
```

with:

```
* Range
* Attack Dice
* Impact Strength
* Weapon Capacity
```

- [x] 31.4 In `docs/15-geometry-layers.md`, `GEO-004`, replace this anchor:

```
* Line of Sight
* Target visibility
* Cover
* Access openings
```

with:

```
* Line of Sight
* Target visibility
* Cover
* Access openings
* Resistance
```

  Tasks 31.3 and 31.4 are the move, and they are written as two edits so a
  reviewer sees the term leave one list and arrive in the other.

- [x] 31.5 In `docs/16-damage-system.md`, `DMG-003`, replace this anchor:

```
Resistance is the **smallest structural section that an Impact must cross in its direction of travel**, measured in plate layers.
```

with:

```
Resistance is the **smallest section of material an Impact must cross in its direction of travel**, measured in plate layers.
```

  "Structural" was the word carrying the old answer, and it is the word that made
  a reader ask whether a bolted-on plate qualified. Material in the path is
  material in the path.

- [x] 31.6 In `docs/14-glossary.md`, the *Resistance* entry, replace this anchor:

```
The smallest structural cross-section an Impact must cross, measured in plate layers and read directly from the model, not assigned as a statistic — no component type is exempt, moulded pieces included. See `16-damage-system.md` (DMG-003, DMG-004).
```

with:

```
The smallest cross-section of material an Impact must cross in its direction of travel, measured in plate layers and read directly from the model, not assigned as a statistic — no component type is exempt, moulded pieces included. See `16-damage-system.md` (DMG-003, DMG-004).
```

  The glossary must not outlive the rule it cites. "In its direction of travel" is
  added because the entry never carried it and the direction is now what decides
  the number.

- [x] 31.7 In `docs/15-geometry-layers.md`, `GEO-004`, replace this anchor — the
      rule's own closing summary:

```
Therefore, Visual Geometry can physically block sight or access even though it does not modify a measured value.
```

with:

```
Therefore, Visual Geometry can physically block sight or access, and material an Impact crosses counts toward Resistance, even though none of it modifies a measured value.
```

  **This is the rule's only summarising sentence and it named three of four
  checks.** After task 31.4 the list includes Resistance, and the sentence
  omitted the one case the section exists to add — while still saying Visual
  Geometry "does not modify a measured value" beside a bullet for a value counted
  in plate layers. Both halves are now stated together.

- [x] 31.8 In `docs/15-geometry-layers.md`, the Design Philosophy, replace this
      anchor:

```
Visual Geometry is still physically present on the table. It may therefore affect direct physical checks such as Line of Sight, Cover and access, even though it does not modify measured values.
```

with:

```
Visual Geometry is still physically present on the table. It may therefore affect direct physical checks such as Line of Sight, Cover, access and the Resistance an Impact crosses, even though it does not modify measured values.
```

  `system/proposal-review.md` ("The Summary Is Part of the Rule") requires a
  change touching a rule to check the document's own framing in the same pass. A
  reader who reads the Design Philosophy and stops gets the pre-change answer
  otherwise.

- [x] 31.9 In `docs/14-glossary.md`, the *Visual Geometry* entry, replace this
      anchor:

```
Every decorative element of a model that does not modify Gameplay Geometry. Never affects measured rule values; still counts for physical checks like Line of Sight and Cover. See `15-geometry-layers.md` (GEO-002, GEO-004).
```

with:

```
Every decorative element of a model that does not modify Gameplay Geometry. Never affects measured rule values; still counts for physical checks like Line of Sight and Cover, and for the Resistance of material an Impact crosses. See `15-geometry-layers.md` (GEO-002, GEO-004).
```

  The entry cites `GEO-004` directly, so it must list what `GEO-004` lists. Task
  31.6 corrected the *Resistance* entry; this is the entry on the other side of
  the same move.

### Verification

- [x] 31.10 `grep -rn "structural" docs/` returns exactly two hits, both in
      `16-damage-system.md` and neither about Resistance: the document's Purpose
      line and `DMG-002`'s "suffered structural damage but remains functional".
      A third hit means an edit was missed.

- [x] 31.11 `grep -c -F "* Resistance" docs/15-geometry-layers.md` returns **1**,
      and reading it shows it under `GEO-004` rather than `GEO-003`. A **2** means
      task 31.3 did not apply.

- [x] 31.12 `grep -rn "Line of Sight, Cover and access" docs/` returns nothing.
      Task 31.8 is the only task that touches that phrase, and it is the
      pre-change list.

- [x] 31.13 `python3 scripts/rule.py refs GEO-002 GEO-003 GEO-004 DMG-003` — no
      citer claims Resistance ignores Visual Geometry. Report any that does rather
      than editing it here.

- [x] 31.14 `python3 scripts/preflight.py` — every check green.

- [x] 31.15 Read `GEO-001` through `GEO-005` in order, then `DMG-003`, then the
      glossary's *Resistance* and *Visual Geometry* entries. The question a reader
      must be able to answer: a brick wall with a plate added to one outer face —
      what does an Impact crossing that face meet, and what does one crossing the
      bare face meet.

      **`GEO-005` and `VEH-030` are deliberately untouched.** Two models with the
      same Gameplay Geometry still have the same Range, Attack Dice and Impact
      Strength, and decorative armour still counts toward no height limit. This
      section widens what an Impact crosses and nothing else.

      **Consequence taken knowingly:** plating a hull with cheap plates is real
      armour now. That is the model deciding, and it is also an optimisation the
      ruleset did not previously offer.

      **Reported and not acted on**, because it asks for a design decision this
      section does not carry: `15-geometry-layers.md`'s boxed line *"Build freely
      without changing the measured rules of the model"* and `GEO-005`'s Minimum
      Representation paragraph both still read as unconditional. They remain true
      of every measured value — Resistance is no longer one — but a reader could
      take them as promising that decoration never matters. Whether to qualify
      them is the maintainer's call, not this change's.

---

## 32. The Vehicle example calls tracks decorative

**A repair, and the defect is pre-existing on `main`** — this change did not
introduce it, and no task in Part A or B touched the line.

`docs/15-geometry-layers.md`'s Vehicle example lists **tracks** as Visual
Geometry. Four rules disagree:

- `CMP-004` — tracks must be physically represented, on both sides
- `VEH-012` — they are one of the four locomotion systems
- `VEH-022` — the Terrain Threshold is read from "half the height of the track run"
- `VEH-029` — "Locomotion counts" toward vehicle height

`CMP-004` carries the distinction the example lost, in one word: *"**Decorative
track details** have no effect."* The detail is decorative; the track is not.

A reader meeting this example before `08-vehicles.md` concludes the tracks can
come off with no consequence, and loses the Terrain Threshold and the locomotion
half of the height with them.

- [x] 32.1 In `docs/15-geometry-layers.md`, the Vehicle example, replace this
      anchor:

```
**Gameplay Geometry:** Platform dimensions, weapon locations, movement geometry and transport capacity.
**Visual Geometry:** tracks, fenders, lights, exhausts and decorative armour.
```

with:

```
**Gameplay Geometry:** Platform dimensions, locomotion, weapon locations, movement geometry and transport capacity.
**Visual Geometry:** track details, fenders, lights, exhausts and decorative armour.
```

  Two words. `tracks` becomes `track details`, matching `CMP-004`'s wording, and
  `locomotion` joins the Gameplay line so the contrast is stated rather than
  inferred from a document away.

  **`decorative armour` stays on the Visual line**, and section 31 does not change
  that: it still alters no measured value. Whether an Impact crossing it adds
  Resistance is now `GEO-004`'s question, not this list's.

### Verification

- [x] 32.2 `grep -c -F "**Visual Geometry:** tracks" docs/15-geometry-layers.md`
      returns **0**.

- [x] 32.3 Read all three Examples — Weapon, Vehicle, Building — against
      `GEO-001` and `GEO-002`. Each closes with "measured values remain unchanged
      by its visual detail", which must still be true of every item on its Visual
      line.

      **The Weapon and Building examples are untouched and were checked**: tubes,
      slopes, supports, roof style, colours, facade details and decorative doors
      change no measured value. Only the Vehicle line named a functional system.

- [x] 32.4 `python3 scripts/preflight.py` — every check green.

---

## 33. `01-foundations.md` closes with one motto where it must close with two

**A repair.** `system/documentation-standards.md` states the requirement and
explains, in the same paragraph, why nothing reports the breach:

> `01-foundations.md` carries both, **closing with the first**. The linter checks
> the last non-empty line.

`lint_ruleset.py` reads the last non-empty line, which is still
`> **Every Brick Matters.**`. The block above it is missing and the check is
green.

**The audit overstated this one.** It reported that the document "no longer
states" the project's central philosophy. It does — `01-foundations.md:33`, under
`# The Core Philosophy`, is exactly that statement. What is missing is the
closing pair `main` carried, and only that.

- [x] 33.1 In `docs/01-foundations.md`, replace this anchor — the document's last
      two lines:

```
---

> **Every Brick Matters.**
```

with:

```
---

> **The Model Is The Rules.**

> **Every Brick Matters.**
```

  **This task adds words, and it is the third in this file to do so** — the others
  are 6.1 and 25.1, and all three for the same reason: the omission states
  something the ruleset does not mean.

  **No delete-it form exists.** Removing the surviving motto fails the linter and
  the standard. The only other route is amending
  `system/documentation-standards.md` to drop "carries both" — a change to the
  norm rather than to the text that broke it, and `01-foundations.md` is the one
  document deliberately carrying two.

### Verification

- [x] 33.2 `grep -c -F "The Model Is The Rules" docs/01-foundations.md` returns
      **2** — `:33` in `# The Core Philosophy`, and the new closing line. It was 1.

- [x] 33.3 `python3 scripts/lint_ruleset.py` — passes, exactly as it did before
      this task. **That is the point rather than the reassurance**: the check
      reads one line and could not see this, which is why
      `system/documentation-standards.md` says so in the same breath as the rule.

- [x] 33.4 Read the last five lines of every document in `docs/`. **Twelve** close
      with `> **Every Brick Matters.**` alone; `15-geometry-layers.md` and
      `16-damage-system.md` close with `> **The Model Is The Rules.**`; and
      `01-foundations.md` closes with both, the second of them last. 12 + 2 + 1 =
      **15**, which is every document.

      **Reported, not fixed: the count is wrong.** All 15 documents were read.
      Twelve close with `> **Every Brick Matters.**` alone
      (`02-core-rules.md`, `03-game-flow.md`, `05-construction-components.md`,
      `06-deployment.md`, `07-movement.md`, `08-vehicles.md`,
      `09-transport.md`, `10-weapons.md`, `11-combat.md`, `12-melee.md`,
      `14-glossary.md`, `17-infantry.md`), not fourteen. `15-geometry-layers.md`
      and `16-damage-system.md` do close with `> **The Model Is The Rules.**`,
      and `01-foundations.md` does close with both, the second of them last —
      those two parts of the claim check out. 12 + 2 + 1 = 15, which is every
      document in `docs/`; "fourteen" would make 17.

- [x] 33.5 `python3 scripts/preflight.py` — every check green.

---

## 34. Three glossary entries contradict the rules they cite

**A repair, and three deletions.** Each entry names a rule and then states
something that rule does not say. A glossary that outlives its rule is worse than
no glossary: it reads as authority and cannot be reached by any check.

Each task removes the false claim and keeps the definition. **No entry is
removed** — all three terms exist and need defining — and no deleted clause is
restored to the rule it came from.

- [x] 34.1 In `docs/14-glossary.md`, the *Muzzle* entry, replace this anchor:

```
A round functional construction area (typically 1×1 through 4×4, with no fixed maximum — see `10-weapons.md` WPN-002) on the Weapon Front Footprint, built from a round plate or round tile, representing one firing barrel.
```

with:

```
A round functional construction area (typically 1×1 through 4×4, with no fixed maximum — see `10-weapons.md` WPN-002) on the Weapon Front Footprint, representing one firing barrel.
```

  **The glossary forbade a build the rule permits.** `WPN-002` reads "visibly
  round, **whether made from a single piece or several pieces**"; the entry
  required a round plate or round tile, which rules out a muzzle built from
  several. The clause goes rather than being rewritten — "a round functional
  construction area" already carries the requirement, and `WPN-002` owns the
  detail.

- [x] 34.2 In `docs/14-glossary.md`, the *Access Opening* entry, replace this
      anchor:

```
The gap a model passes through when it uses a door, hatch or ramp. An access point whose opening does not physically pass a given model is decorative for that model and has no gameplay effect. See `05-construction-components.md` (CMP-018).
```

with:

```
The gap a model passes through when it uses a door, hatch or ramp. See `05-construction-components.md` (CMP-018).
```

  **`CMP-018` no longer says this, and no other rule does.** The concept —
  an opening that fails a model is decorative *for that model* — survived only
  here, which made the glossary the sole source of a rule. `CMP-018` states the
  check itself: an access opening must physically pass every model that uses it.

- [x] 34.3 In `docs/14-glossary.md`, the *Weapon Range* entry, replace this
      anchor:

```
The maximum distance a ranged weapon may attack, equal to Weapon Length × 6. Bounded in practice by Line of Sight and by what the attacker's platform can carry, rather than by a written maximum. See `10-weapons.md` (WPN-005).
```

with:

```
The maximum distance a ranged weapon may attack, equal to Weapon Length × 6. Bounded in practice by Line of Sight rather than by a written maximum. See `10-weapons.md` (WPN-005).
```

  **Half the claim survives and half does not.** `WPN-005` kept the Line of Sight
  bound — "maximum range is only relevant where that distance is unobstructed" —
  and lost the platform chain entirely: `WPN-004` limiting total mounted Weapon
  Length, read against `VEH-001` and `DEP-003`, read against the Deployment
  Volume. The entry keeps the half its rule still carries.

### Verification

- [x] 34.4 `grep -c -F "round plate or round tile" docs/14-glossary.md` returns
      **0**.

- [x] 34.5 `grep -c -F "is decorative for that model" docs/14-glossary.md` returns
      **0**, and `grep -rn "decorative for that model" docs/` returns nothing at
      all — the concept is gone from the ruleset rather than moved.

- [x] 34.6 `grep -c -F "platform can carry" docs/14-glossary.md` returns **0**.

- [x] 34.7 Read all 47 glossary entries against the rules they cite. **This is the
      only check there is**: `lint_ruleset.py` verifies that a cited rule exists,
      not that it says what the entry claims, which is how all three of these
      passed every gate.

      Report anything else found rather than fixing it here — the audit checked
      the other 44 and found them agreeing with their rules, so a fourth would be
      a new finding.

      All 47 entries read against the rules they cite. No new contradiction
      found — everything checked out, including the entries touched elsewhere
      in this change (Weapon Body/Front/Front Footprint against `WPN-003`/
      `WPN-019`; Resistance and Visual Geometry against `GEO-002`/`GEO-004`/
      `DMG-003`; Geometry Check/Damage Roll/Penetration against `DMG-013`/
      `DMG-014`/`DMG-016`; Deployment Volume against `DEP-001`).

- [x] 34.8 `python3 scripts/preflight.py` — every check green.

---

## 35. Nothing outside `docs/` names a rule that exists

**A repair, and every task here is a deletion or a substitution. No rule in
`docs/` is touched.**

The audit reported that `CBT-011` lost its supersession note while
`system/proposal-review.md` and `.claude/agents/ruleset-auditor.md` still name it
as the exemplar. Reading the files found more than that, and found the report
partly wrong:

- **`WPN-021` never carried such a note**, not even on `main`. Checked against
  `git show main:docs/10-weapons.md`. The claim naming both rules was already
  half false before this change and is now false entirely.
- **Four files make it**, not two: `system/documentation-standards.md`,
  `system/proposal-review.md`, `system/workflow.md` and
  `.claude/agents/ruleset-auditor.md`.
- **More dead references, none of them in the audit.**
  `system/proposal-review.md` quotes `WPN-021` verbatim — *"No component is
  unconditionally invulnerable..."* — and the compression deleted that sentence.
  The same file names `WPN-017` (retired by this change), `MOVE-016` and
  `MOVE-004` (retired earlier), inside the list of common failures that includes
  "a retired rule ID still cited from outside `docs/`". Task 23.5 removes
  `MOVE-016`; tasks 35.14 and 35.15 remove the other two.

**Nothing is restored to `CBT-011`.** The maintainer's ruling:

> Delete what is surplus. No need to add noise where it does not belong.
> Auditors should not use rules as examples. They should have a BASE form that is not from the real rule set.

The convention itself is owned by `system/documentation-standards.md`, Naming
Conventions, and that sentence stands on its own without naming a rule. The ID
examples are the copy, and the copy is what rotted — the same lesson as
Decision 11, which stopped `scripts/` naming live rules, applied to `system/` and
`.claude/`.

### The BASE form

Agent definitions use `ABC-001` for a rule ID and `` `NN-document.md`` for a
ruleset document. Neither resolves, so neither can go stale. `grep -rn "ABC-0"`
across the repository returns nothing today.

**Operational exemptions are not examples and stay.** An auditor is told that
`02-core-rules.md` lacks Design Philosophy and Summary by recorded exemption,
which two documents close with `> **The Model Is The Rules.**`, and that
`docs/14-glossary.md` is in append order. Replacing those with placeholders would
make the agent report false findings on every run. They name real documents
because the agent must recognise those documents.

- [x] 35.1 In `system/documentation-standards.md`, replace this anchor:

```
A rule may be deleted. Its number is retired, never reissued, and no stub is
left in its place — the diff records that the rule was there. Where the rule
stays and only its design was superseded, the note goes inside that rule:
`CBT-011` and `WPN-021` (`system/proposal-review.md`).
```

with:

```
A rule may be deleted. Its number is retired, never reissued, and no stub is
left in its place — the diff records that the rule was there. Where the rule
stays and only its design was superseded, the note goes inside that rule.
```

  The policy is complete without the examples. This document owns it; the other
  two now point here rather than restating it with IDs.

- [x] 35.2 In `system/proposal-review.md`, "Record What You Decided Not to Do",
      replace this anchor:

```
A rejection and its reasoning belong in `design.md`, and if the question will
recur for a reader of the ruleset, in the rule itself. `CBT-011` and `WPN-021`
keep the superseded thing visible and say why, rather than leaving a clean
surface that invites the same suggestion again.
```

with:

```
A rejection and its reasoning belong in `design.md`, and if the question will
recur for a reader of the ruleset, in the rule itself: keep the superseded thing
visible and say why, rather than leaving a clean surface that invites the same
suggestion again.
```

  The instruction survives word for word. Only the two IDs that no longer
  demonstrate it go.

- [x] 35.3 In `system/proposal-review.md`, "Do Not Cap What the Model Already
      Bounds", replace this anchor:

```
The instinct to add a maximum is usually wrong here. `WPN-021` wrote the
argument: *"No component is unconditionally invulnerable; it is only safe from
whatever can't be mounted on the attacker's current platform."*
```

with:

```
The instinct to add a maximum is usually wrong here. Nothing is unconditionally
invulnerable; a component is only safe from whatever cannot be mounted on the
attacker's current platform.
```

  **This is the reference the audit missed.** The quoted sentence was deleted
  from `WPN-021` by the compression, so the file quotes a rule that no longer
  says it. The argument is true and stays; the attribution goes.

- [x] 35.4 In `.claude/agents/ruleset-auditor.md`, section 4, replace this
      anchor:

```
IDs are permanent — never renumbered, never reused. A superseded rule keeps its number and carries a note saying so (`CBT-011`, `WPN-021`). The `13-*.md` gap is deliberate for the same reason. Report any renumbering, any reuse, any gap that is not.
```

with:

```
IDs are permanent — never renumbered, never reused. A superseded rule keeps its number and carries a note saying so. A gap in the document numbering is deliberate where a document was removed and its number retired — `system/documentation-standards.md` records which. Report any renumbering, any reuse, any gap that is not.
```

  Both dependencies go: the two rule IDs, and the hard-coded `13-*.md`. The agent
  is given the shape and the document that records the instances, so a future
  retirement does not make this line wrong.

- [x] 35.5 In `.claude/agents/ruleset-auditor.md`, section 2, replace this
      anchor:

```
- **Cross-document citation existence**, in both the parenthesised `` `10-weapons.md` (WPN-021) `` and comma `` `08-vehicles.md`, VEH-013 `` forms. **Existence is no longer your job. Aim still is — see section 3.**
```

with:

```
- **Cross-document citation existence**, in both the parenthesised `` `NN-document.md` (ABC-001) `` and comma `` `NN-document.md`, ABC-001 `` forms. **Existence is no longer your job. Aim still is — see section 3.**
```

- [x] 35.6 In `.claude/agents/ruleset-auditor.md`, section 3, replace this
      anchor:

```
The convention is `` `08-vehicles.md`, VEH-013 `` across documents and a bare `VEH-013` within one. The linter verifies existence; do not re-check it.
```

with:

```
The convention is `` `NN-document.md`, ABC-001 `` across documents and a bare `ABC-001` within one. The linter verifies existence; do not re-check it.
```

  Tasks 35.5 and 35.6 teach a citation *format*. A format is illustrated as well
  by a placeholder as by a live rule, and a placeholder cannot be retired.

- [x] 35.7 In `.claude/agents/ruleset-auditor.md`, section 7, replace this
      anchor:

```
Rules are deterministic, concise, easy to reference, and reuse existing terminology. A rule leaving an outcome genuinely undecided is a finding — unless it explicitly defers to the scenario (`FLOW-013`), which is a defined mechanism.
```

with:

```
Rules are deterministic, concise, easy to reference, and reuse existing terminology. A rule leaving an outcome genuinely undecided is a finding — unless it explicitly defers to the scenario, which is a defined mechanism.
```

- [x] 35.8 In `.claude/agents/ruleset-auditor.md`, replace this anchor:

```
`rule.py doc` on `08-vehicles.md` costs about a sixth of reading it, and a single `rule.py show` about a twenty-fifth.
```

with:

```
`rule.py doc` on a ruleset document costs about a sixth of reading it, and a single `rule.py show` about a twenty-fifth.
```

- [x] 35.9 In `.claude/agents/proposal-auditor.md`, replace this anchor:

```
`rule.py doc` on `08-vehicles.md` costs about a sixth of reading it, and a single `rule.py show` about a twenty-fifth.
```

with:

```
`rule.py doc` on a ruleset document costs about a sixth of reading it, and a single `rule.py show` about a twenty-fifth.
```

  Tasks 35.8 and 35.9 edit the same sentence in two files. Each anchor occurs
  once in the file its task names.

- [x] 35.10 In `.claude/agents/ruleset-auditor.md`, replace this anchor:

```
To read several rules, pass several arguments: `python3 scripts/rule.py show CORE-002 FLOW-003 WPN-019`.
```

with:

```
To read several rules, pass several arguments: `python3 scripts/rule.py show <ID> <ID> <ID>`.
```

- [x] 35.11 In `.claude/agents/proposal-auditor.md`, replace this anchor:

```
To read several rules, pass several arguments: `python3 scripts/rule.py show CORE-002 FLOW-003 WPN-019`.
```

with:

```
To read several rules, pass several arguments: `python3 scripts/rule.py show <ID> <ID> <ID>`.
```

- [x] 35.12 In `.claude/agents/proposal-applier.md`, replace this anchor:

```
To check several rules, pass several arguments: `python3 scripts/rule.py show CORE-002 FLOW-003 WPN-019`.
```

with:

```
To check several rules, pass several arguments: `python3 scripts/rule.py show <ID> <ID> <ID>`.
```

  `<ID>` rather than `ABC-001` here, because this is a command an agent may copy.
  A placeholder that looks like an argument is safer than a fake one that looks
  like a real one and fails.

- [x] 35.13 In `system/workflow.md`, "Scenario names are identifiers", replace
      this anchor:

```
scenario's content becomes wrong, **keep the name and correct the body** — the
same convention `CBT-011` and `WPN-021` follow in the ruleset.
```

with:

```
scenario's content becomes wrong, **keep the name and correct the body** — the
same convention a superseded rule follows in the ruleset.
```

  **The fourth file making the claim.** This section's preamble named three;
  `system/workflow.md` is the one it missed, and verification 35.14 would have
  failed on it.

- [x] 35.14 In `system/proposal-review.md`, the common-failure list, replace this
      anchor:

```
- **A changed rule's own ID never grepped, only the ones it retired** — #126
  emptied `CORE-006` and wrote into `WPN-017`, and `TODO.md` quoted both;
```

with:

```
- **A changed rule's own ID never grepped, only the ones it retired** — #126
  emptied one rule and wrote into another, and `TODO.md` quoted both;
```

  **`WPN-017` is retired by this change**, so the sentence names a rule a reader
  cannot reach — and it does so inside the list of common failures that includes
  "a retired rule ID still cited from outside `docs/`". `CORE-006` still exists,
  but the pair is de-identified together: the failure is about the shape, and
  naming either invites the next retirement to break it again.

- [x] 35.15 In `system/proposal-review.md`, "Multipliers Set Early Get Falsified
      by Numbers Added Later", replace this anchor:

```
`VEH-004`'s `1.5×` and `WPN-005`'s `× 2` were both reasonable when written and
both wrong once `MOVE-004`, `WPN-004` and `CORE-001` existed to check them
```

with:

```
`VEH-004`'s `1.5×` and `WPN-005`'s `× 2` were both reasonable when written and
both wrong once `INF-002`, `WPN-004` and `CORE-001` existed to check them
```

  `MOVE-004` was retired before this change. `INF-002` is the rule that now
  carries the 12-stud infantry move the sentence argues against, so the example
  is retargeted rather than dropped — `VEH-004`, `WPN-005`, `WPN-004` and
  `CORE-001` all still exist and the argument is unchanged.

### Verification

- [x] 35.16 `grep -rnE "\b(CORE|MOVE|VEH|WPN|CBT|MEL|DMG|GEO|CMP|TRN|DEP|FLOW|INF|SCS)-[0-9]{3}\b" .claude/agents/`
      returns nothing. **No agent definition names a rule that exists.**

- [x] 35.17 `grep -rn "CBT-011" system/ .claude/` returns nothing. Same for
      `grep -rn "WPN-021" system/ .claude/`. Four files carried the claim, not
      three: tasks 35.1, 35.2, 35.4 and 35.13.

- [x] 35.18 `python3 scripts/rule.py show WPN-017 MOVE-016 MOVE-004` reports no
      such rule for all three, **and** `grep -rn "WPN-017" system/`,
      `grep -rn "MOVE-016" system/` and `grep -rn "MOVE-004" system/` each return
      nothing. Tasks 23.5, 35.14 and 35.15 are the only tasks that remove them.

      `openspec/changes/archive/` is history and is not searched
      (`system/proposal-review.md` says so itself).

- [x] 35.19 `grep -rnE "[0-9]{2}-[a-z-]+\.md" .claude/agents/` returns **three**
      hits, all in `ruleset-auditor.md`. Between them they name five documents,
      and each names one because the agent must recognise that document rather
      than because it illustrates a point:

      - `02-core-rules.md` missing Design Philosophy and Summary — a recorded
        linter exemption, not a finding.
      - `15-geometry-layers.md` and `16-damage-system.md` closing with
        `> **The Model Is The Rules.**`, and `01-foundations.md` with both.
      - `docs/14-glossary.md` being in append order.

      **Replacing these with placeholders would make the agent report false
      findings on every run.** If a fourth hit appears, it is an example and
      should go.

      **The count and location are right — three hits, all in
      `ruleset-auditor.md` (lines 28, 56, 72). One of the three descriptions is
      itself now stale**, and this task's own text repeats the error: task 15.1
      shrank `scripts/lint_ruleset.py`'s `SECTION_DEBT` to
      `{"02-core-rules.md": ("Summary",)}` — `02-core-rules.md` gained a Design
      Philosophy section in Part A and only its Summary is still exempt.
      `.claude/agents/ruleset-auditor.md:28` still reads "`02-core-rules.md`
      missing Design Philosophy and Summary is a known exemption recorded in
      the script" — an auditor reading that line today is told to withhold a
      finding the script no longer withholds. No task in this file touches that
      line. Reported rather than fixed here.

- [x] 35.20 `grep -rn "delete-me-audit-findings" .` returns nothing. The working
      file this review ran from is not part of the pull request.

      **Expect exactly one hit: this task's own line**, which has to quote the
      filename in order to state the check. Any second hit is a real reference
      and must be removed. `docs/`, `system/`, `.claude/`, `scripts/` and
      `TODO.md` all come back clean.

- [x] 35.21 `python3 scripts/preflight.py` — every check green.

- [x] 35.22 Read `.claude/agents/ruleset-auditor.md` and
      `.claude/agents/proposal-auditor.md` end to end. Every remaining statement
      must be true of the repository rather than of one snapshot of the ruleset.

      **Left alone deliberately:** `system/proposal-review.md` states the weapon
      Range chain naming `WPN-004`, `VEH-001`, `DEP-003` and `FLOW-001`. Those
      four rules exist and the chain they form is still true, so it is a worked
      example rather than a dead reference. It is the next thing in this file
      that will rot, and it is recorded here so the next reader meets it knowing
      that.

      **Reported and not acted on:** nothing enforces the BASE form. Task 35.16
      is a one-off grep, and `system/documentation-standards.md` states the
      sibling constraint for `scripts/` only — "a script never names a rule that
      exists". Extending that sentence to agent definitions, and widening
      `lint_ruleset.py` to check `.claude/agents/`, is a policy change and a new
      gate. It belongs in its own proposal, not in a repair section.

### Found while applying

Task 35.19 sent a reader to `ruleset-auditor.md:28` to confirm the document names
it keeps are operational. Reading it found the line itself stale.

- [x] 35.23 In `.claude/agents/ruleset-auditor.md`, section 2, replace this
      anchor:

```
- The document skeleton and the closing motto. `02-core-rules.md` missing Design Philosophy and Summary is a known exemption recorded in the script, not something to report again.
```

with:

```
- The document skeleton and the closing motto. `02-core-rules.md` missing a Summary is a known exemption recorded in the script, not something to report again.
```

  **`02-core-rules.md` has a Design Philosophy**, at its own heading, and
  `scripts/lint_ruleset.py`'s `SECTION_DEBT` exempts `("Summary",)` and nothing
  else — task 15.1 of this change shrank it when Part A gave the document that
  section. The line told the auditor to withhold a finding the script no longer
  withholds.

  This is the same defect class as the rest of section 35 — a statement about the
  repository that stopped being true — found one line above one of its own
  verifications. The document is still named, and still for an operational
  reason, so task 35.19's count of three stands.

- [x] 35.24 `grep -c -F "missing Design Philosophy and Summary" .claude/agents/ruleset-auditor.md`
      returns **0**, and `grep -n "SECTION_DEBT" scripts/lint_ruleset.py` shows
      `SECTION_DEBT = {"02-core-rules.md": ("Summary",)}`. The agent's claim and
      the script now agree. Both run and confirmed.

---

## 36. What the audit of the applied text found

`ruleset-auditor` read the result after Part C landed. **Five of its findings are
contradictions and are repaired here.** The rest need a maintainer's decision and
are recorded at the end of this section rather than guessed at.

Nothing here changes a rule the maintainer decided. Each task removes a
disagreement between two rules, or scopes an absolute a neighbouring sentence
already breaks.

- [x] 36.1 In `docs/08-vehicles.md`, `VEH-024`, replace this anchor:

```
If the hover assembly is destroyed, the hull settles and its Terrain Threshold becomes 0.
```

with:

```
If the hover assembly is destroyed, the hull settles and the vehicle is Immobilized (`VEH-031`).
```

  **Two rules decided the same event differently.** A hover assembly is
  locomotion (`VEH-012`; `CMP-005`), so task 27.5's "a vehicle whose locomotion is
  entirely destroyed cannot move and is Immobilized" covers it — while this
  sentence gave the same vehicle a working Terrain Threshold of 0, and a
  threshold is only ever read to answer a movement question (`VEH-021`).

  Before section 27 there was no conflict: a destroyed hover assembly was
  governed by nothing, and settling to 0 was the whole ruling. Section 27 gave
  the case an owner and left this sentence behind.

  The hull still settles — that is the model. What it no longer claims is a
  threshold for a vehicle that cannot move.

- [x] 36.2 In `docs/15-geometry-layers.md`, `GEO-002`, replace this anchor:

```
Material an Impact must cross is never ignored: a plate or panel outside a wall is part of what the Impact crosses and adds to its Resistance (`16-damage-system.md`, DMG-003; `GEO-004`). What is decorative is the printing on a piece, not the piece.
```

with:

```
Material an Impact must cross is never ignored, however decorative it looks. What is decorative is the printing on a piece, not the piece. How that material resolves is measured where Resistance is measured (`16-damage-system.md`, DMG-003; `GEO-004`).
```

  **`GEO-002` was stating a combination rule that `16-damage-system.md` owns and
  states differently.** "Adds to its Resistance" says two thicknesses become one
  number; `DMG-003` says "each wall is a separate component with its own
  Resistance. Their thicknesses are not combined", `DMG-001` lists **Armour
  Plate** as a component in its own right, and `DMG-016` crosses two thicknesses
  by subtracting and continuing.

  The maintainer's ruling survives intact — material in the Impact's path is never
  discarded for looking decorative, which is the whole of Decision 17. What goes
  is `GEO-002` answering *how* it resolves, which is not its question.

  **The mechanism is still undecided and is recorded below.** This task removes
  the disagreement; it does not settle which reading is right.

- [x] 36.3 In `docs/15-geometry-layers.md`, `GEO-003`, replace this anchor:

```
Only Gameplay Geometry is used when calculating measured rule values.
```

with:

```
Only Gameplay Geometry is used when calculating measured rule values. Resistance is not one of them — it is read from the model as built (`GEO-004`).
```

  Task 31.3 took Resistance out of `GEO-003`'s list, but the list is prefaced
  "Examples include" and the rule's operative sentence is unqualified. Removing an
  item from a list of examples does not remove it from a general claim, and
  `CORE-001` sends a reader to `GEO-003` and `GEO-004` as a pair — so whoever
  reaches `GEO-003` first still gets the pre-change answer.

- [x] 36.4 In `docs/14-glossary.md`, the *Component State* entry, replace this
      anchor:

```
The three-state progression every component uses: `Operational`, `Wounded`, `Dead`. Universal — no component type has an exception. See `16-damage-system.md` (DMG-002).
```

with:

```
The three-state progression every component uses: `Operational`, `Wounded`, `Dead`. No component type is exempt from the states; only a Wounded minifigure can run them backwards (`16-damage-system.md`, DMG-018). See `16-damage-system.md` (DMG-002).
```

  After section 28 exactly one component type has an exception, and this entry
  says none does. It is the defect class section 34 was written to remove — an
  entry naming a rule and then stating something the ruleset no longer supports —
  arriving in the same change that removed three others.

- [x] 36.5 In `docs/16-damage-system.md`, `DMG-018`, replace this anchor:

```
A damaged component is not repaired. What is broken stays broken.

Any Wounded minifigure may spend **1 Action Point** to return to Operational — infantry on foot, and a Pilot or crew member inside a vehicle alike.
```

with:

```
A damaged component is not repaired. What is broken stays broken.

A Wounded minifigure is the one thing that recovers: it may spend **1 Action Point** to return to Operational — infantry on foot, and a Pilot or crew member inside a vehicle alike.
```

  **A minifigure is a component** — `DMG-001` lists Minifig and Pilot, and
  `VEH-013` says the Pilot resolves Impacts as a normal component. So the rule
  stated a universal and broke it one line later, and a reader had to guess that
  "repaired" and "return to Operational" are different acts.

  Six words of scope. **Not the "exception" framing task 28.1 deleted** — that
  described the rule's history; this states which sentence governs which
  component.

### Verification

- [x] 36.6 `grep -c -F "Terrain Threshold becomes 0" docs/08-vehicles.md` returns
      **0**. `VEH-024`'s other threshold-0 sentence — "A hull resting directly on
      the ground has a threshold of 0" — is untouched and still true. Run and
      confirmed.

- [x] 36.7 `grep -c -F "adds to its Resistance" docs/15-geometry-layers.md`
      returns **0**. Run and confirmed.

- [x] 36.8 `grep -c -F "no component type has an exception" docs/14-glossary.md`
      returns **0**. Run and confirmed.

- [x] 36.9 `python3 scripts/rule.py refs VEH-031 DMG-018` — `VEH-031` gains
      `VEH-024` as a citer. Confirmed: `VEH-004`, `VEH-019`, `VEH-024`, `DMG-002`
      and the glossary's *Wounded*.

      **`DMG-018` still reports "cited by nothing", and the text is right.** The
      glossary's *Component State* now cites it in the comma form the convention
      asks for, and `lint_ruleset.py` accepts it. `scripts/build_index.py` records
      only one citation per glossary entry per document, and that entry cites
      `16-damage-system.md` twice — `DMG-018` inline and `DMG-002` in the closing
      "See". The trailing one wins.

      **A tooling limitation, not a defect in `docs/`**, and not repaired here: a
      change to `build_index.py` needs its own test and its own commit
      (`.claude/rules/tooling.md`). Recorded so `rule.py orphans` is not read as
      evidence that nothing points at `DMG-018`.

- [x] 36.10 `python3 scripts/preflight.py` — every check green. Run: all 12 pass.

- [x] 36.11 Read `VEH-024`, `VEH-031`, `GEO-002`, `GEO-003`, `GEO-004`, `DMG-003`
      and `DMG-018` in that order. Each pair that disagreed now answers its
      question once:

      - A destroyed hover assembly settles the hull and immobilizes the vehicle;
        no threshold is asserted for a vehicle that cannot move.
      - `GEO-002` says material in the path is never discarded and sends the
        reader to `DMG-003` for how it resolves. It states no combination rule.
      - `GEO-003`'s opening no longer sweeps Resistance in with the measured
        values, and `GEO-004` lists it.
      - `DMG-018`'s first sentence is scoped by its second, so a reader knows
        which governs a Wounded Pilot.

## 37. Two of the audit's findings were wrong, and one of my repairs with them

The audit of the applied text raised seven items for the maintainer. **Two were
not defects, and task 36.2 acted on one of them.** The maintainer's rulings:

> The Action Points are guaranteed by rule. Activating a unit gives it Action Points.

> It is construction. A plate and a brick — the Resistances add. Nothing more needs writing.

### Whose Action Points was never open

`CORE-006` says it: *"Every unit activates using Action Points … **The rule
governing an action defines its AP cost.**"* The pool is `CORE-006`'s and every
rule states only the cost — `VEH-008`, `VEH-009`, `VEH-010`, `INF-002`, `TRN-005`,
`CBT-006`, `INF-007`. **Not one names the pool it draws from.** `VEH-013` and
`DMG-018` follow that pattern exactly; naming it in those two would be the
anomaly. Nothing to change.

### `DMG-003` already decides the plate

The clause the audit read as a contradiction is scoped, and the scope is the
answer: *"If an **enclosed structure contains multiple walls**, each wall is a
separate component with its own Resistance."* Beside *"Empty internal space
contributes nothing"*, the separator is the gap. A plate flush against a brick has
none — it is one continuous section of material crossed in one direction, and the
conversion table adds it: 1 + 3 = 4.

`DMG-001` listing **Armour Plate** among targetable components does not contest
this. It lists what an Impact can be assigned to; whether a given piece is a part
of a wall or a part of its own is what the build shows.

- [x] 37.1 In `docs/15-geometry-layers.md`, `GEO-002`, revert task 36.2. Replace
      this anchor:

```
Material an Impact must cross is never ignored, however decorative it looks. What is decorative is the printing on a piece, not the piece. How that material resolves is measured where Resistance is measured (`16-damage-system.md`, DMG-003; `GEO-004`).
```

with:

```
Material an Impact must cross is never ignored: a plate or panel outside a wall is part of what the Impact crosses and adds to its Resistance (`16-damage-system.md`, DMG-003; `GEO-004`). What is decorative is the printing on a piece, not the piece.
```

  **Task 36.2 removed a true sentence to resolve a contradiction that was not
  there.** The maintainer had decided this wording in Decision 17 and it agrees
  with `DMG-003` once that rule's non-combination clause is read with its scope.
  Restoring it puts the answer where a reader meeting decorative armour will look,
  instead of forwarding them to a rule they then have to interpret.

### Verification

- [x] 37.2 `grep -c -F "adds to its Resistance" docs/15-geometry-layers.md`
      returns **1**. Task 36.7 recorded **0** and that state is superseded. Run
      and confirmed.

- [x] 37.3 `python3 scripts/preflight.py` — every check green. Run: all 12 pass.

- [x] 37.4 Read `GEO-002` and `DMG-003` together, in that order. A brick wall
      with one plate outside it, hit head-on, is Resistance 4. Two walls of an
      enclosed hull with space between them are two components of 3 each. Both
      answers must be reachable from these two rules without a third.

---

## 38. Left for the maintainer

**None of these is guessed at. Each changes what a rule means, or picks a
number, and the changes in this file were settled before it was written.**

Section 37 removed the two items that turned out not to be defects. Five remain,
and **none of them changes an outcome at the table** — they are a title, a
definition's axis, and three passages a reader could over-read.

1. **Weapon Width has three candidates.** `WPN-003` says "the Weapon Body's
   smallest dimension" and a body has three. For a body 8 long × 4 wide × 2 tall
   that is 2, giving a `2 × 2` Weapon Front — while `WPN-020`'s worked example
   says an `8 × 4` body has Weapon Width 4 and a `4 × 4` front, which holds only
   if a body is described by two numbers. `WPN-019` requires the front to be
   *square*, which an 8 × 4 × 2 body's front face is not.

   **The wording is `main`'s, restored verbatim by task 25.1**, so this is
   inherited rather than introduced — but section 25 promoted it from a rule
   nothing cited into the definition three rules read. Naming the axis fixes it
   and picks a number.

   Related and also unstated: "firing axis" is used by `WPN-003` and the
   glossary's *Weapon Body* and defined by no rule.

2. **`GEO-005` and the boxed line.** "Build freely without changing the measured
   rules of the model" and the Minimum Representation paragraph are unqualified.
   Both remain true of every measured value — Resistance is no longer one — but a
   reader can take them as promising decoration never matters. `GEO-005:116` and
   the glossary's *Functional Equivalence* read the same way.

3. **The glossary's *Wounded* entry** is the ruleset's fullest statement of that
   state and does not mention that 1 Action Point ends it. Not a contradiction —
   it never claimed to list the exits — but a reader looking the state up will not
   learn how to leave it.

4. **`assets/IMAGES.md` declines `CBT-007`** as "a binary construction check made
   directly on the model". Section 29 gave the rule a reach limit resolved by
   pointing the arm at the target, which is spatial. The claim is not false; the
   reason no longer covers the whole rule.

**Closed since this list was written:** `VEH-031`'s title named one of the two
outcomes it states. Section 39 retitles it *What Damage Does to Movement*.

---

## 39. `VEH-031`'s locomotion threshold, stated as a number

**A rule change, requested by the maintainer on pull request #130** after the
branch was pushed. The threshold section 27 left as "entirely destroyed" is
replaced by a counted one.

> If one or more, but fewer than half, of a vehicle's locomotion components are Dead, its movement is reduced to 2× its length.
> If half or more are Dead, the vehicle cannot move.

> Define locomotion components functionally: wheels, tracks, walker legs, repulsors. Decorative parts do not count.
> Keep the rule generic rather than tying it to specific vehicle types.

**`VEH-031` and nothing else.** The maintainer was explicit: *"solo habla para la
regla VEH-031, no más."*

- [x] 39.1 In `docs/08-vehicles.md`, `VEH-031`, replace this anchor:

```
A vehicle moves **twice its own length** per movement action instead of three times (`VEH-004`) when its Pilot is Wounded (`VEH-013`) or a locomotion component is Dead (`16-damage-system.md`, DMG-002).
```

with:

```
A vehicle moves **twice its own length** per movement action instead of three times (`VEH-004`) when its Pilot is Wounded (`VEH-013`), or when some but fewer than half of its locomotion components are Dead (`16-damage-system.md`, DMG-002).

A vehicle with **half or more** of its locomotion components Dead cannot move and is Immobilized (`VEH-019`).
```

- [x] 39.2 In `docs/08-vehicles.md`, `VEH-031`, replace this anchor:

```
The reduction is not cumulative. A vehicle moves twice its own length whether one cause applies or both, and however many locomotion components are Dead.

A Wounded locomotion component does not change movement distance.

A vehicle whose locomotion is entirely destroyed cannot move and is Immobilized (`VEH-019`).
```

with:

```
The reduction is not cumulative: a vehicle moves twice its own length whether one cause applies or both.

A Wounded locomotion component does not change movement distance.

Locomotion components are the parts that carry the vehicle — wheels, track runs, legs, repulsors (`VEH-012`). Decorative parts are not locomotion (`15-geometry-layers.md`, GEO-002) and are not counted.

Examples:

| Locomotion    | 1 Dead      | 2 Dead      |
| ------------- | ----------- | ----------- |
| 2 wheels      | cannot move | —           |
| 4 wheels      | reduced     | cannot move |
| 2 tracks      | cannot move | —           |
| 4 walker legs | reduced     | cannot move |
| 4 repulsors   | reduced     | cannot move |
```

  **"however many locomotion components are Dead" goes.** It was true when the
  only alternative was total destruction; with a counted threshold it contradicts
  the rule above it.

  The definition is functional and generic, as asked: what carries the vehicle,
  not which vehicle it is. It leans on `VEH-012` for the systems and on `GEO-002`
  for what decoration is, rather than restating either.

  The table is examples, not categories. Every row is the maintainer's, and the
  arithmetic is the rule's: 1 of 2 is half, 1 of 4 is not, 2 of 4 is.

- [x] 39.3 In `docs/08-vehicles.md`, `VEH-004`, replace this anchor — one line
      below the movement table:

```
A Wounded Pilot or a Dead locomotion component reduces this to twice the vehicle's length (VEH-031).
```

with:

```
A Wounded Pilot or locomotion damage changes this (VEH-031).
```

  **"a Dead locomotion component reduces this" is now wrong**, and the maintainer
  asked for it: with two wheels and one Dead the vehicle does not move at all.
  The line stops naming an outcome `VEH-031` owns and points at it instead.

- [x] 39.4 In `docs/08-vehicles.md`, the Summary, replace this anchor:

```
A Wounded Pilot or a Dead locomotion component reduces movement from three lengths to two.
```

with:

```
A Wounded Pilot or locomotion damage changes movement (VEH-031).
```

  **The same false sentence, in the second place it is written.** The maintainer
  named `VEH-004`'s line; this is the same claim in the document's Summary, and
  `system/proposal-review.md` ("The Summary Is Part of the Rule") is explicit that
  a change touching a rule checks the Summary in the same pass. Fixing one and
  leaving the other would leave the defect this whole change exists to remove.

- [x] 39.11 In `docs/08-vehicles.md`, replace this anchor — the rule heading:

```
# VEH-031 — Reduced Movement
```

with:

```
# VEH-031 — What Damage Does to Movement
```

  **The rule now states two outcomes in two paragraphs**, and *Reduced Movement*
  names one of them. The new title follows the pattern of its two neighbours —
  `VEH-029 — Where Height Is Counted From`, `VEH-030 — What Counts Toward
  Height` — and is honest that the answer is sometimes that movement stops.

  **Rejected:** *Movement Penalties* ("penalty" is abstract-statistic vocabulary
  the ruleset uses nowhere), *Locomotion Damage* (leaves out the Wounded Pilot,
  which is half the rule), *Immobilization* (`VEH-019` owns that; this rule says
  when).

  **The rule keeps its number and is retitled** — the thing no script reports
  (`design.md`, Decision 12). It is the fourth retitle in this change, after
  `WPN-003`, `DMG-018` and `VEH-031` itself in section 27. Citations travel by ID,
  so `VEH-004`, `VEH-019`, `VEH-024`, `DMG-002` and the glossary's *Wounded* are
  unaffected.

### Verification

- [x] 39.5 `grep -c -F "entirely destroyed" docs/08-vehicles.md` returns **0**.
      Run and confirmed.

- [x] 39.6 `grep -c -F "half or more" docs/08-vehicles.md` returns **1**. Run and
      confirmed.

- [x] 39.7 `grep -c -F "Dead locomotion component" docs/08-vehicles.md` returns
      **0**. It was 2 — `VEH-004`'s line and the Summary's, both replaced by tasks
      39.3 and 39.4. Run and confirmed.

- [x] 39.8 `python3 scripts/rule.py refs VEH-031 VEH-012 GEO-002` — `VEH-031`
      gains `VEH-012` and `GEO-002` as targets; its own citers are unchanged:
      `VEH-004`, `VEH-019`, `VEH-024`, `DMG-002` and the glossary's *Wounded*.

- [x] 39.9 `python3 scripts/preflight.py` — every check green. Run: all 12 pass.

- [x] 39.12 `grep -c -F "VEH-031 — Reduced Movement" docs/08-vehicles.md` returns
      **0**, and `python3 scripts/rule.py show VEH-031` prints *What Damage Does
      to Movement*. Both run and confirmed.

- [x] 39.13 `python3 scripts/build_index.py` — the index carries rule titles and
      one changed. Run.

- [x] 39.14 `python3 scripts/preflight.py` — every check green after the index is
      rebuilt. Run: all 12 pass.

- [x] 39.10 Read `VEH-031` in full, then `VEH-004`, `VEH-012`, `VEH-019` and
      `VEH-024`. Every example row follows from the rule's own two sentences:
      1 of 2 is half, 1 of 4 is not, 2 of 4 is. The title names both outcomes.

      **`VEH-024` is deliberately untouched.** "If the hover assembly is destroyed
      … Immobilized (`VEH-031`)" stays true: all of it destroyed is half or more.
      A hover vehicle with four repulsors and two Dead is answered by `VEH-031`.

---

## 12. Archive housekeeping — a separate pull request

`a-deployment-volume-is-floor-and-ceiling` (#129) carries an unarchived
`MODIFIED` delta against `unit-base`'s *Unit Base Projections*, which this
change supersedes (`specs/unit-base/spec.md`).

- [ ] 12.1 Move #129's `specs/unit-base/spec.md` to `specs-superseded/` in its
      own directory, with a note naming this change (`system/workflow.md`,
      "When several changes modified the same requirement"). **Not in this pull
      request** — `Docs require OpenSpec proposal` fails a PR touching two
      change directories.

---

# Verification

- [x] V.1 `python3 scripts/preflight.py` — every check green.
- [x] V.2 `python3 scripts/rule.py orphans` — `DMG-011` and `DMG-013` are off
      the list, which is what section 2 fixes.

      **`DMG-012`, `DMG-015` and `DMG-018` will be on it, and that is the
      expected result.** They had inbound edges before section 2 ran, and those
      edges were the mis-aimed citations: `11-combat.md` naming `DMG-012` when
      it meant `DMG-011`, and so on. Correcting each citation moved the edge to
      the rule that earned it and left these three standing alone. `rule.py`
      says it itself — "standalone is legitimate; disconnected is a defect" —
      and Composite Vehicle Targeting, Multiple Impacts and Repairs are each
      reached from the resolution sequence in `DMG-008` rather than by name.

      This verification originally claimed no rule in the document would be
      uncited. That was wrong when written, not broken by the work.
- [x] V.3 Read `06-deployment.md`, `08-vehicles.md`, `11-combat.md`,
      `12-melee.md` and `16-damage-system.md` end to end, Summaries included.
      Every finding in Part B was found by reading, not by a command
      (`system/proposal-review.md`).
