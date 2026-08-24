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
