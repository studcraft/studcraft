# Tasks — A Unit Base is thirteen plate layers

## 0. Setup

- [x] 0.1 Work on branch `a-unit-base-is-thirteen-plate-layers` (`openspec/config.yaml` requires one branch per proposal, and `system/repository-strategy.md` requires the branch to be named for the change). The branch already exists and is checked out; do not create another and do not leave it.

### How to read the replacement blocks

Every anchor and every replacement is given inside a fenced block. **The fence is not
part of the text.** Inline backticks, em dashes (`—`), `×` and the bold `**` markers
are part of the text — write them exactly.

Tasks 1.4 and 6.1 use a **four-backtick** fence because their content is a markdown
table; those fence lines are not part of the text either.

No heading is edited by any task, no rule is added, removed or renumbered, and no rule
ID changes.

### The figure

Every `12` this change touches becomes `13`, and every explanation of *why* changes
with it: a Unit Base is a minifigure's 4 bricks plus the one plate of the base it
stands on (`04-construction-standard.md`, SCS-002). Do not convert a figure this
proposal does not name — `docs/09-transport.md`'s 4-plate crate and 8-plate pallet,
`DMG-003`'s plate-counts-1-brick-counts-3, and every terrain threshold stay exactly as
they are.

### Anchors

Every anchor below was checked with exact-substring matching against the pre-change
file and occurs exactly **once in the file its task names**. Three files carry the
identical dimension line, so each of those anchors is given with the lines around it —
replace the whole anchor.

If an anchor returns anything other than 1, **stop and report it** rather than
guessing which occurrence was meant.

### Scope and coverage

Five ruleset documents, two root documents and the image index: **twelve edits and
three verify-only tasks.** One further task, 9.1, stays unchecked until the spec
deltas exist — see below.

| `proposal.md` item | Task | Path |
|---|---|---|
| `CORE-001` states 13, derives it, moves the plane | 1.1, 1.2, 1.3 | `docs/02-core-rules.md` |
| `CORE-001`'s projection rows | 1.4 | `docs/02-core-rules.md` |
| The three overview surfaces | 2.1, 3.1, 4.1 | `docs/01-foundations.md`, `README.md`, `CODE_OF_DESIGN.md` |
| The head stud is named as not counted | 1.3 | `docs/02-core-rules.md` |
| `SCS-002` pins the base at one plate | 1.5 | `docs/04-construction-standard.md` |
| The glossary's *Unit Base* entry | 5.1 | `docs/14-glossary.md` |
| `TRN-013`'s cargo heights stay as they are | 6.1, 6.2 | `docs/09-transport.md` |
| The sentences the new measuring plane touches | 6.3, 6.4, 6.5 | `09-transport.md`, `14-glossary.md`, `08-vehicles.md` |
| The `CORE-001` image brief | 7.1 | `assets/IMAGES.md` |
| The four spec deltas | 9.1 | this change's `specs/` |

**Untouched, deliberately** — every one of these was left in Unit Bases by #80 and
#81 precisely so that this change would not have to open it: `TRN-003`, `TRN-019`,
`TRN-020` and the transport Summary (clearance, all reading "one Unit Base of clear
height"); `VEH-028`, `VEH-029`, `VEH-030` (both height bounds, in Unit Bases);
`DEP-001` through `DEP-009`; `CMP-018` (the vertical projection, no figure);
`DMG-003`, `VEH-021`, `MOVE-009` – `MOVE-011` (material and distance, not volume).
`CHANGELOG.md`, every `**Version:**` header and `openspec/specs/` are untouched.

**The spec deltas are deferred, and task 9.1 holds the change open until they are
written.** Four requirements across two capabilities carry the figure, and they must
be written against a living spec that is currently two changes behind — see
`design.md`, "The spec deltas". Leaving that in prose alone would let
`scripts/archive_cut.py` sweep this change into the archive the moment every other box
is ticked, with no `specs/` directory and no gate able to notice: `openspec-change-coherent.yml`
treats a change without deltas as legitimate. **Do not tick 9.1**, and do not tick it
on anyone's behalf.

---

## 1. `docs/02-core-rules.md` — `CORE-001`

- [x] 1.1 Replace this anchor — **the dimension line with the sentence above it**, so the match cannot land in another file:

```
One **Unit Base (UB)** is a volume measuring:

**4 studs wide × 3 studs deep × 12 plate layers tall**
```

with:

```
One **Unit Base (UB)** is a volume measuring:

**4 studs wide × 3 studs deep × 13 plate layers tall**
```

- [x] 1.2 Replace this anchor:

```
Height is counted in plate layers because that is the ruleset's vertical unit — a plate counts as 1 and a standard brick as 3 (`16-damage-system.md`, DMG-003; `08-vehicles.md`, VEH-021). Twelve plate layers is therefore exactly 4 bricks. Height is measured from the top face of the plate an infantry model stands on: that plate is the model's floor, not part of the space above it.
```

with:

```
Height is counted in plate layers because that is the ruleset's vertical unit — a plate counts as 1 and a standard brick as 3 (`16-damage-system.md`, DMG-003; `08-vehicles.md`, VEH-021). Thirteen plate layers is therefore 4 bricks and a plate. Height is measured from the underside of the base an infantry model stands on: that base is part of the volume, not the floor beneath it.
```

- [x] 1.3 Replace this anchor:

```
The height is read from the model rather than chosen. Infantry occupies exactly one Unit Base whether standing or seated (`09-transport.md`, TRN-002), so a Unit Base must contain a standing minifigure — about 4 bricks from its feet to the top of its head. Twelve plate layers is the smallest whole-brick height that does, and a Unit Base is the minimum operational space an object needs (`09-transport.md`, TRN-001), so it takes exactly that and no more.
```

with:

```
The height is read from the model rather than chosen. Infantry occupies exactly one Unit Base whether standing or seated (`09-transport.md`, TRN-002), so a Unit Base must contain a standing minifigure on the base it is built on (`04-construction-standard.md`, SCS-002): 4 bricks from its feet to the top of its head, and one plate beneath them. Thirteen plate layers is that model exactly, and a Unit Base is the minimum operational space an object needs (`09-transport.md`, TRN-001), so it takes that and no more. **The stud on top of the minifigure's head is not counted.** A stud is not height: it occupies the tube of whatever sits above it, which is why a brick is 3 plate layers and a plate is 1 with their studs already in the count. Counting the minifigure's would make the Unit Base the one measurement in StudCraft that reads a stud as space of its own.
```

Two facts change here and both are read off the plastic. A minifigure is 4 bricks
exactly rather than "about" 4, and the base `SCS-002` requires is inside the volume
rather than under it. The old sentence's "smallest whole-brick height" reasoning goes
with them: 13 is not a whole number of bricks, and the model is not obliged to be.

**The stud sentence claims no precedent and cites none.** `DMG-003` measures material
across an impact's direction of travel, which never meets a stud, so it cannot be the
authority for this and is not cited for it. What the sentence appeals to is the
arithmetic every reader already applies — a brick stacks at 3 plate layers, studs
included in that count because they sit inside the piece above.

- [x] 1.4 In `CORE-001`'s projections table, replace this anchor — **two rows of a markdown table; the horizontal-projection row above them is unchanged and is not part of the anchor**:

````
| The volume itself — `4 × 3` studs by 12 plate layers | Transport capacity, interior space, and the Deployment Volume a model must fit inside |
| Vertical projection — 4 studs by 12 plate layers | Passing through an opening |
````

with:

````
| The volume itself — `4 × 3` studs by 13 plate layers | Transport capacity, interior space, and the Deployment Volume a model must fit inside |
| Vertical projection — 4 studs by 13 plate layers | Passing through an opening |
````

---

## 1b. `docs/04-construction-standard.md` — `SCS-002`

- [x] 1.5 Replace this anchor:

```
Every infantry model must be built on one physical base measuring 4 × 3 studs — one Unit Base read horizontally (`02-core-rules.md`, CORE-001).
```

with:

```
Every infantry model must be built on one physical base measuring 4 × 3 studs and one plate thick — one Unit Base read horizontally (`02-core-rules.md`, CORE-001), and the plate `CORE-001` counts in its height.
```

`SCS-002` constrained the footprint and said nothing about thickness, which did not
matter while the base sat outside the Unit Base. It matters now: `CORE-001`'s height
is 4 bricks of minifigure **plus that plate**, so a base built a brick thick would
put a legal infantry model 15 plate layers tall inside a 13-plate-layer volume. One
plate is what every infantry base in the ruleset's examples already is; this says so.

---

## 2. `docs/01-foundations.md`

- [x] 2.1 Replace this anchor — **three lines, so the match cannot land in another file**:

```
One Unit Base is a volume measuring:

**4 studs wide × 3 studs deep × 12 plate layers tall**

(see `02-core-rules.md`, CORE-001, for the canonical definition, where the height comes from, and which projection each rule reads)
```

with:

```
One Unit Base is a volume measuring:

**4 studs wide × 3 studs deep × 13 plate layers tall**

(see `02-core-rules.md`, CORE-001, for the canonical definition, where the height comes from, and which projection each rule reads)
```

Only the figure changes. The pointer already promises `CORE-001` says where the height
comes from, and after task 1.3 it does.

---

## 3. `README.md`

- [x] 3.1 Replace this anchor:

```
One Unit Base is a volume:

**4 studs wide × 3 studs deep × 12 plate layers tall**

— defined by `docs/02-core-rules.md` (CORE-001), which is the authority on its dimensions, its orientation and which projection a rule reads.
```

with:

```
One Unit Base is a volume:

**4 studs wide × 3 studs deep × 13 plate layers tall**

— defined by `docs/02-core-rules.md` (CORE-001), which is the authority on its dimensions, its orientation and which projection a rule reads.
```

---

## 4. `CODE_OF_DESIGN.md`

- [x] 4.1 In Principle 7, replace this anchor:

```
One Unit Base is a volume:

**4 studs wide × 3 studs deep × 12 plate layers tall**

— defined by `docs/02-core-rules.md` (CORE-001), which is the authority on its dimensions and orientation.
```

with:

```
One Unit Base is a volume:

**4 studs wide × 3 studs deep × 13 plate layers tall**

— defined by `docs/02-core-rules.md` (CORE-001), which is the authority on its dimensions and orientation.
```

Note the difference from task 3.1: this one's closing clause ends "dimensions and
orientation", `README.md`'s adds "and which projection a rule reads". Neither
sentence changes; do not make them match.

---

## 5. `docs/14-glossary.md`

- [x] 5.1 In the *Unit Base* entry, replace this anchor:

```
The universal measurement of StudCraft: a volume 4 studs wide, 3 studs deep and 12 plate layers tall. See `02-core-rules.md` (CORE-001) for the projections a rule reads it through.
```

with:

```
The universal measurement of StudCraft: a volume 4 studs wide, 3 studs deep and 13 plate layers tall — a minifigure's 4 bricks and the plate of the base it stands on. See `02-core-rules.md` (CORE-001) for the projections a rule reads it through.
```

The derivation is added here because a glossary defines the term, and after this
change the figure is no longer self-explanatory as a count of bricks.

---

## 6. `docs/09-transport.md` — `TRN-013`, verify only

- [x] 6.1 **Verify only, change nothing.** `TRN-013`'s cargo table keeps every figure it has, including the drone's, motorbike's and walker's `12 plate layers`. They are heights read from example models, not the unit restated, and moving them by hand would concede the opposite (`design.md`, Decision 3). Confirm the table is unedited.

- [x] 6.2 **Verify only, change nothing.** The sentence below that table — "Three ammo crates of 4 plate layers therefore share one Unit Base" — stays true at 13 (three take 12 of it, a fourth would need 16) and is not edited. Confirm it is unchanged.

---

## 6b. Three sentences the new measuring plane touches

`CORE-001` now measures from the **underside** of an infantry model's base. Three
sentences elsewhere name a surface for the same measurement and would otherwise be
ambiguous by exactly the plate this change adds.

- [x] 6.3 In `docs/09-transport.md`, `TRN-019`, replace this anchor:

```
Clearance is measured from the surface a model stands or sits on, upward to whatever is above it.
```

with:

```
Clearance is measured from the surface a model's base rests on — the floor, the deck or the bench, not the top of the base itself — upward to whatever is above it.
```

Read against the old `CORE-001` the two sentences agreed. Read against the new one,
"the surface a model stands on" is the top of its base, and 13 clear layers above
*that* would count the base twice.

- [x] 6.4 In `docs/14-glossary.md`, the *Interior Clearance* entry, replace this anchor:

```
The clear height inside a closed compartment, measured in plate layers from the surface a model stands or sits on.
```

with:

```
The clear height inside a closed compartment, measured in plate layers from the surface a model's base rests on.
```

- [x] 6.5 In `docs/08-vehicles.md`, `VEH-028`, replace this anchor:

```
An odd narrowest side gives a limit of a whole number of Unit Bases and a half. Nothing is rounded: a vehicle's own height is measured in plate layers (VEH-030) and compared against the limit.
```

with:

```
An odd narrowest side gives a limit of a whole number of Unit Bases and a half, which is not a whole number of plate layers. Nothing is rounded: a vehicle's own height is measured in plate layers (VEH-030) and compared against the limit, so the limit is met by any whole plate count below it.
```

At 13 plate layers a half Unit Base is six and a half of them, so a 3-stud narrowest
side allows nineteen and a half. The rule was already deterministic — it compares
rather than rounds — but a threshold sitting between two plate layers should say so
where a builder meets it rather than leave them to discover it.

---

## 7. `assets/IMAGES.md`

- [x] 7.1 Replace the `CORE-001` entry — one table row, both content cells. Do not reflow the row:

```
| CORE-001 | `assets/images/core-001-unit-base-volume.png` | Five panels. First, the Unit Base as a volume, dimensioned 4 studs wide × 3 studs deep × 12 plate layers tall, with a standing minifigure inside it and the plate it stands on marked as floor, outside the volume. Then one panel per reading of that volume, each labelled: the horizontal projection, 4 × 3 studs; the volume itself, labelled as the reading transport capacity and interior space use; the vertical projection, 4 studs by 12 plate layers, taken across the 4-stud front and drawn against an opening a model passes through. Last, a "2 × 3 UB" footprint measuring 8 × 9 studs, beside a 6 × 12 rectangle marked wrong. | Three geometric facts here are carried by prose alone: that the unit encloses space rather than covering it, that its height starts at the top face of the floor plate, and that different rules read different projections of the same volume. The rule text itself flags the 8×9-vs-6×12 confusion as one readers get wrong. |
```

with:

```
| CORE-001 | `assets/images/core-001-unit-base-volume.png` | Six panels. First, the derivation: a minifigure standing on its base beside a stack of four bricks and one plate, the two flush at the top and their studs aligned, with the minifigure's four bricks and the base's one plate dimensioned separately and the head stud marked as not counted. Second, the Unit Base as a volume, dimensioned 4 studs wide × 3 studs deep × 13 plate layers tall, with that same model inside it and the base plate drawn within the volume rather than below it. Then one panel per reading of that volume, each labelled: the horizontal projection, 4 × 3 studs; the volume itself, labelled as the reading transport capacity and interior space use; the vertical projection, 4 studs by 13 plate layers, taken across the 4-stud front and drawn against an opening a model passes through. Last, a "2 × 3 UB" footprint measuring 8 × 9 studs, beside a 6 × 12 rectangle marked wrong. | Four geometric facts here are carried by prose alone: that the height is the model plus the base it stands on rather than a chosen round number, that the unit encloses space rather than covering it, that the base plate is inside the volume rather than the floor under it, and that different rules read different projections of the same volume. The first panel is the argument for the figure and not an illustration of it — two stacks being the same height is the one claim text cannot make convincingly. The rule text itself flags the 8×9-vs-6×12 confusion as one readers get wrong. |
```

The filename does not change: it is still the image that dimensions the Unit Base
volume, and `scripts/lint_ruleset.py` checks that name against the convention and
against `CORE-001` existing in `docs/02-core-rules.md`.

---

## 8. Verification

Each command below was run against the pre-change tree and the "before" figure is what
it actually returned. Run each one after applying, and report any figure that differs
from "after" **without editing a document to make a check pass**.

- [x] 8.1 `grep -rn "12 plate layers" docs/ assets/ README.md CODE_OF_DESIGN.md | wc -l` — before: **11**, after: **3** — `TRN-013`'s drone, motorbike and walker cargo heights, which task 6.1 deliberately leaves alone.

- [x] 8.2 `grep -rn "13 plate layers" docs/ assets/ README.md CODE_OF_DESIGN.md | wc -l` — before: **0**, after: **8**.

- [x] 8.3 `grep -c "Twelve plate layers" docs/02-core-rules.md` — before: **2**, after: **0**. Both spelled-out occurrences are in `CORE-001` and both are replaced, one by "Thirteen plate layers is therefore 4 bricks and a plate" and one by "Thirteen plate layers is that model exactly".

- [x] 8.4 `grep -c "top face of the plate" docs/02-core-rules.md` — before: **1**, after: **0**. The measuring plane moved to the underside of the base.

- [x] 8.5 `grep -rn "4 plate layers\|8 plate layers" docs/09-transport.md | wc -l` — before: **4**, after: **4**. The crate and pallet example heights are untouched — four lines, because `TRN-013`'s prose mentions the 4-plate crate as well as its table row.

- [x] 8.6 `grep -c "one Unit Base of clear height" docs/09-transport.md` — before: **8**, after: **8**. No clearance rule is touched by this change; that is the whole point of #80 and #81.

- [x] 8.7 `python3 scripts/lint_ruleset.py` — exits 0, no findings.

- [x] 8.8 `python3 scripts/check_delta_coverage.py` — exits 0. This change writes no delta **yet**; see `design.md`.

- [x] 8.9 `git status --porcelain` — exactly ten paths: `docs/01-foundations.md`, `docs/02-core-rules.md`, `docs/04-construction-standard.md`, `docs/08-vehicles.md`, `docs/09-transport.md`, `docs/14-glossary.md`, `README.md`, `CODE_OF_DESIGN.md`, `assets/IMAGES.md`, and this change's own directory. Nothing under `openspec/specs/`, no `CHANGELOG.md`, no `**Version:**` header.

- [x] 8.10 `grep -rn "Version:" docs/*.md | grep -c "0.2.0 Draft"` — before: **15**, after: **15**.

- [x] 8.11 `grep -c "surface a model stands or sits on" docs/09-transport.md docs/14-glossary.md` — before: `1`, `1`. After: `0`, `0`. Both name the surface a model's **base** rests on.

- [x] 8.12 Report anything that had to be interpreted. Every interpretation is a place this proposal was unclear (`system/delegating-to-agents.md`).

---

## 9. Left open on purpose

- [ ] 9.1 **Do not tick.** The four spec deltas — `unit-base`'s *Unit Base Measurement*, *Unit Base Projections* and *Cargo Divides a Unit Base*, and `weapon-capacity`'s *Platform Length Definition* — are written under this change's `specs/` **after** `Archive cut` has run and the living spec has absorbed `deployment-is-a-volume`'s block on *Unit Base Projections*. Until then this box stays unchecked, which is what keeps `scripts/archive_cut.py` from archiving a change whose spec is a version of the ruleset that no longer exists.


---

## 10. Post-audit repairs

The audit of the applied text returned ten findings. Seven are defects in this
proposal's own wording, and two of those are claims that are simply false — the
pattern `system/delegating-to-agents.md` predicts, and the reason the applied text is
read a second time. Every anchor below was checked against the current working tree
and occurs exactly once.

- [x] 10.1 In `CORE-001`, replace this anchor — the last three sentences of the derivation paragraph:

```
Thirteen plate layers is that model exactly, and a Unit Base is the minimum operational space an object needs (`09-transport.md`, TRN-001), so it takes that and no more. **The stud on top of the minifigure's head is not counted.** A stud is not height: it occupies the tube of whatever sits above it, which is why a brick is 3 plate layers and a plate is 1 with their studs already in the count. Counting the minifigure's would make the Unit Base the one measurement in StudCraft that reads a stud as space of its own.
```

with:

```
Thirteen plate layers is that model, base included, and a Unit Base is the minimum operational space an object needs (`09-transport.md`, TRN-001), so it takes that and no more. **The stud on top of the minifigure's head is not counted here.** The counts in the paragraph above are stacking heights: a stud sits inside the piece above it rather than adding to the stack, and this measurement is taken the same way. Nor do headgear, weapons or equipment change the figure — infantry occupies exactly one Unit Base whatever it carries (`09-transport.md`, TRN-002).
```

Three repairs in one paragraph, all of them mine:

- **"the one measurement in StudCraft that reads a stud as space of its own"** was an
  absolute claim about every other height in the ruleset, and `VEH-030` reads the
  other way — "a weapon standing upright is measured by how high its plastic actually
  reaches". `design.md` says the general question is a separate proposal; the sentence
  now says "here" and claims nothing beyond this measurement.
- **The tube argument was inverted for the one stud it was about.** Nothing sits above
  a bare minifigure's head, so that stud occupies no tube. What is true is the general
  fact about stacking, which is what the sentence now states.
- **"that model exactly" was falsified by a hat.** `TRN-002` puts headgear, weapons and
  accessories inside the one Unit Base an infantry model occupies; a plumed helmet
  reaches past 13 and the charge does not change. The paragraph now says so instead of
  claiming a caliper fit.

It also stops restating "a brick is 3 plate layers and a plate is 1", which the
paragraph two above already states **with** its citations — the duplication this
change's own premise is against.

- [x] 10.2 In `VEH-028`, replace this anchor:

```
An odd narrowest side gives a limit of a whole number of Unit Bases and a half, which is not a whole number of plate layers. Nothing is rounded: a vehicle's own height is measured in plate layers (VEH-030) and compared against the limit, so the limit is met by any whole plate count below it.
```

with:

```
An odd narrowest side gives a limit of a whole number of Unit Bases and a half, which is not a whole number of plate layers. Nothing is rounded: a vehicle's own height is measured in plate layers (VEH-030) and compared against the limit, so such a limit is met by the whole plate count below it.
```

The clause said "the limit is met by any whole plate count below it", which reads as
the operative test and **excludes equality**. Every row of this rule's own table has an
even narrowest side, so every limit in it is a whole plate count that a vehicle may
meet exactly — a Bike at 26 is legal, and the old clause said it was not. The clause
belongs to the odd-side case only, and now says so.

- [x] 10.3 In `docs/09-transport.md`, `TRN-019`, replace this anchor:

```
Clearance is measured from the surface a model's base rests on — the floor, the deck or the bench, not the top of the base itself — upward to whatever is above it.
```

with:

```
Clearance is measured from the surface the model rests on — the floor, the deck or the bench, and for infantry the surface under its base rather than the top of it — upward to whatever is above it.
```

`TRN-019` governs cargo and stowed vehicles as well as infantry, and only infantry has
a base (`SCS-002`). The previous wording named a datum two of its three subjects do
not have.

- [x] 10.4 In `docs/14-glossary.md`, the *Interior Clearance* entry, replace this anchor:

```
The clear height inside a closed compartment, measured in plate layers from the surface a model's base rests on.
```

with:

```
The clear height inside a closed compartment, measured in plate layers from the surface the model rests on — for infantry, the surface under its base rather than the top of it.
```

Same defect as 10.3, and worse here: the entry has no enumeration to rescue it, so the
restatement was narrower than the rule it cites.

- [x] 10.5 In `docs/14-glossary.md`, the *Unit Base* entry, replace this anchor:

```
The universal measurement of StudCraft: a volume 4 studs wide, 3 studs deep and 13 plate layers tall — a minifigure's 4 bricks and the plate of the base it stands on. See `02-core-rules.md` (CORE-001) for the projections a rule reads it through.
```

with:

```
The universal measurement of StudCraft: a volume 4 studs wide, 3 studs deep and 13 plate layers tall. See `02-core-rules.md` (CORE-001) for where that height comes from and the projections a rule reads it through.
```

The added clause was a copy of the **derivation**, not of the figure, so a future
change to how the height is derived would have had to move two places. #80's line —
and `design.md` Decision 4's — is that the figure lives where the unit is defined; the
argument lives in `CORE-001` alone. The pointer now promises the derivation instead of
duplicating it.

- [x] 10.6 In `docs/04-construction-standard.md`, `SCS-002`, replace this anchor:

```
Every infantry model must be built on one physical base measuring 4 × 3 studs and one plate thick — one Unit Base read horizontally (`02-core-rules.md`, CORE-001), and the plate `CORE-001` counts in its height.
```

with:

```
Every infantry model must be built on one physical base measuring 4 × 3 studs — one Unit Base read horizontally (`02-core-rules.md`, CORE-001) — and one plate thick, which is the plate `CORE-001` counts in the Unit Base's height.
```

Only the sentence's shape changes. "4 × 3 studs and one plate thick — one Unit Base
read horizontally" attached a horizontal gloss to a clause that had just gained a
vertical dimension.

- [x] 10.7 In `assets/IMAGES.md`'s `CORE-001` entry, replace this anchor — a fragment of the long cell; do not reflow the row:

```
First, the derivation: a minifigure standing on its base beside a stack of four bricks and one plate, the two flush at the top and their studs aligned
```

with:

```
First, the derivation: a minifigure standing on its base beside a stack of four bricks on one plate — the plate at the bottom, mirroring the base — the two flush at the top and their studs aligned
```

Where the plate sits is what makes the panel an argument rather than a coincidence of
totals, and the brief is what an illustrator draws from.

- [x] 10.8 Tick task 0.1. The branch is correct and checked out, every archived change ticks its own 0.1, and leaving two boxes open invites someone to tick 9.1 as well — which is the one box that must stay open.

### Verification after section 10

- [x] 10.9 `grep -c "the one measurement in StudCraft" docs/02-core-rules.md` — before: **1**, after: **0**.

- [x] 10.10 `grep -c "met by any whole plate count" docs/08-vehicles.md` — before: **1**, after: **0**.

- [x] 10.11 `grep -c "a brick is 3 plate layers and a plate is 1" docs/02-core-rules.md` — before: **1**, after: **0**. The equivalence is now stated once, in the paragraph that cites `DMG-003` and `VEH-021` for it.

- [x] 10.12 `grep -rc "surface a model's base rests on" docs/09-transport.md docs/14-glossary.md` — before: `1`, `1`. After: `0`, `0`.

- [x] 10.13 `grep -o "TRN-002" docs/02-core-rules.md | wc -l` — before: **1**, after: **2**. `CORE-001` now cites it for the accessories case as well. Count occurrences, not lines: both citations land in the same paragraph, so `grep -c` returns 1 either way.

- [x] 10.14 `grep -c "^- \[ \]" openspec/changes/a-unit-base-is-thirteen-plate-layers/tasks.md` — after everything in this section is applied and ticked: **1**, and it is task 9.1.

- [x] 10.15 `python3 scripts/lint_ruleset.py` and `python3 scripts/check_delta_coverage.py` — both exit 0, the second reporting one MODIFIED requirement and no dropped scenarios.


---

## 11. Review on PR #82 — the cargo heights move after all

Task 6.1 kept `TRN-013`'s drone, motorbike and walker at `12 plate layers`, following
#80's reasoning that a height read from a model is not the unit restated even when the
two agree. The reviewer overrode it, and the override is right: those three rows were
chosen to **equal** a Unit Base — it is what makes the drone illustrate cargo that
fills one, against the crate's partial slice — so at 12 they quietly stop illustrating
anything. `design.md`, Decision 3, is rewritten to record the reversal rather than
leave the file arguing for the state it no longer describes.

- [x] 11.1 In `TRN-013`, replace this table. **Four-backtick fences; the table inside is real markdown.** Three `Height` cells change and nothing else does:

````
| Cargo | Footprint | Height |
|---|---|---|
| Ammo crate | 1 UB | 4 plate layers |
| Fuel drum pallet | 1 UB | 8 plate layers |
| Drone | 1 UB | 12 plate layers |
| Motorbike | 2 UB | 12 plate layers |
| Walker | 2 UB or more | 12 plate layers |
````

with:

````
| Cargo | Footprint | Height |
|---|---|---|
| Ammo crate | 1 UB | 4 plate layers |
| Fuel drum pallet | 1 UB | 8 plate layers |
| Drone | 1 UB | 13 plate layers |
| Motorbike | 2 UB | 13 plate layers |
| Walker | 2 UB or more | 13 plate layers |
````

The crate and the pallet keep their figures: those are arbitrary example heights, not
the unit in disguise. The other three are the unit, and they follow it.

- [x] 11.2 **Verify only, change nothing.** The sentence below the table — "Three ammo crates of 4 plate layers therefore share one Unit Base" — stays true at 13: three take 12 of the 13, and a fourth would need 16. It is not edited.

### Verification after section 11

- [x] 11.3 `grep -rn "12 plate layers" docs/ assets/ README.md CODE_OF_DESIGN.md | wc -l` — before: **3**, after: **0**. The figure is gone from the ruleset entirely.

- [x] 11.4 `grep -rn "13 plate layers" docs/ assets/ README.md CODE_OF_DESIGN.md | wc -l` — before: **8**, after: **11**.

- [x] 11.5 `grep -c "4 plate layers\|8 plate layers" docs/09-transport.md` — before: **4**, after: **4**. The crate and pallet are untouched. Four lines, not three: `TRN-003`'s example at line 91 and `TRN-013`'s closing sentence both mention the 4-plate crate as well as its table row — the same count section 8.5 states and this task first got wrong.

- [x] 11.6 `python3 scripts/lint_ruleset.py` and `python3 scripts/check_delta_coverage.py` — both exit 0, the second reporting one MODIFIED requirement and no dropped scenarios.

- [x] 11.7 `grep -c "^- \[ \]" openspec/changes/a-unit-base-is-thirteen-plate-layers/tasks.md` — after ticking everything in this section: **1**, and it is still task 9.1.


---

## 12. Review on PR #82 — say which whole plate count meets a fractional limit

The review accepted `VEH-028`'s fractional limits and asked for one thing: that the
rule state explicitly how a fractional limit is compared against a model measured in
whole plate layers. The clause said "met by the whole plate count below it", which
names a direction rather than a value.

The review's worked example — a 3-stud narrowest side giving 19½ plate layers, so 19
legal and 20 not — is arithmetically right, and the rule does **not** print it. That
figure is `1.5 × 13`, and putting it in `VEH-028` would state a Unit Base's worth in
plate layers in a second document, which the review on #81 asked this ruleset not to
do. `CORE-001` owns the conversion; the rule states the comparison, and the reader
does the multiplication with the figure they already have.

- [x] 12.1 In `VEH-028`, replace this anchor:

```
An odd narrowest side gives a limit of a whole number of Unit Bases and a half, which is not a whole number of plate layers. Nothing is rounded: a vehicle's own height is measured in plate layers (VEH-030) and compared against the limit, so such a limit is met by the whole plate count below it.
```

with:

```
An odd narrowest side gives a limit of a whole number of Unit Bases and a half, which is not a whole number of plate layers. Nothing is rounded, in either direction: a vehicle's own height is measured in plate layers (VEH-030) and compared against the limit, so the greatest whole plate count that does not exceed the limit is legal and the next one up is not.
```

### Verification after section 12

- [x] 12.2 `grep -c "greatest whole plate count that does not exceed" docs/08-vehicles.md` — before: **0**, after: **1**.

- [x] 12.3 `grep -rn "19\.5\|19½\|nineteen and a half" docs/` — before: **0 lines**, after: **0 lines**. The worked example stays out of the ruleset; only `CORE-001` converts a Unit Base into plate layers.

- [x] 12.4 `python3 scripts/lint_ruleset.py` and `python3 scripts/check_delta_coverage.py` — both exit 0.

- [x] 12.5 `grep -c "^- \[ \]" openspec/changes/a-unit-base-is-thirteen-plate-layers/tasks.md` — after ticking this section: **1**, and it is still task 9.1.
