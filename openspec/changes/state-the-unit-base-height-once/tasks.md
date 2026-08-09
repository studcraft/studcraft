# Tasks — State the Unit Base's height once

## 0. Setup

- [x] 0.1 Work on branch `state-the-unit-base-height-once` (`openspec/config.yaml` requires one branch per proposal, and `system/repository-strategy.md` requires the branch to be named for the change). The branch already exists and is checked out; do not create another and do not leave it.

### How to read the replacement blocks

Every anchor and every replacement is given inside a fenced block. **The fence is not
part of the text.** Inline backticks, em dashes (`—`), `×` and the bold `**` markers
are part of the text — write them exactly.

Two tasks (5.6 and 5.13) replace a block that itself contains a markdown table, and
5.13's anchor contains a fenced code block. Those two use a **four-backtick** fence so
the inner fence survives; the four-backtick lines are not part of the text either. A
`|` table inside a block is real markdown, not quoted text.

Unless a task says otherwise, it replaces one paragraph with one paragraph, adds no
blank line and removes none.

### The three phrases

This change replaces figures with exactly three phrases, and never with a variant of
one (`design.md`, Decision 1):

- **`one Unit Base of clear height`** — for a compartment's clearance. Not "a full
  Unit Base", not "the full Unit Base", not "one Unit Base of clearance", and never a
  bare "one Unit Base": a clearance is a height, and a Unit Base on its own is a
  volume.
- **`the Unit Base's height`** — for the slice budget in `TRN-013` and the glossary.
- **`the Unit Base's vertical projection`** — for an opening, in `CMP-018` only.

If a replacement below appears to want a fourth phrasing, it is a defect in this
proposal: **stop and report it** rather than choosing one.

### Anchors

Every anchor below was checked with exact-substring matching against the pre-change
file and occurs exactly **once** in it. If an anchor returns anything other than 1,
**stop and report it** rather than guessing which occurrence was meant.

Never change, remove or renumber a heading. No heading is edited by any task below.

### Citation form

`scripts/lint_ruleset.py` pairs a backticked filename with any **parenthesised** rule
ID that follows it within 80 characters and resolves that ID against that file. Every
citation added below is either the comma form (`` `02-core-rules.md`, CORE-001 ``) or
a parenthesised ID that already resolves correctly in its own file. Do not convert one
form to the other.

### Scope and coverage

Six ruleset documents and one index file change, across 22 edits. Four further tasks
are verify-only. Every item in `proposal.md`'s What Changes maps to a task here, and
no task adds material `proposal.md` does not describe.

| `proposal.md` item | Task | Path |
|---|---|---|
| `CORE-001` stops citing `CMP-018` | 2.1 | `docs/02-core-rules.md` |
| `CMP-018` stops restating the projection and its derivation | 3.1 | `docs/05-construction-components.md` |
| `VEH-028` stops reprinting `TRN-020`'s formula | 4.1 | `docs/08-vehicles.md` |
| `TRN-001`, `TRN-003`, `TRN-019`, Summary express clearance as one Unit Base of clear height | 5.1, 5.2, 5.3, 5.8, 5.9, 5.10, 5.12, 5.14 | `docs/09-transport.md` |
| `TRN-003`'s crates share rather than fill | 5.4 | `docs/09-transport.md` |
| `TRN-013` states the slice budget and drops `Space` | 5.5, 5.6, 5.7 | `docs/09-transport.md` |
| `TRN-019`'s cargo bullet drops "three quarters" | 5.11 | `docs/09-transport.md` |
| `TRN-020` loses its formula and two table columns | 5.13 | `docs/09-transport.md` |
| `WPN-004`'s note stops quoting the height | 6.1 | `docs/10-weapons.md` |
| Glossary *Interior Clearance* and *Slice* | 7.1, 7.2 | `docs/14-glossary.md` |
| `assets/IMAGES.md` stops quoting the deleted formula | 8.1 | `assets/IMAGES.md` |
| `assets/IMAGES.md`'s `TRN-019` brief matches the rewritten rule | 8.2 | `assets/IMAGES.md` |

**Untouched, deliberately.** Do not edit any of these, even though they contain the
figure or a phrasing of it. Four are checked by a verify-only task (1.1, 4.2, 7.3,
8.3):

- `CORE-001`'s dimension line and both rows of its projections table
  (`docs/02-core-rules.md`) — it is the owner.
- `docs/01-foundations.md`'s Unit Base overview, `README.md` and `CODE_OF_DESIGN.md`
  (Principle 7) — all three introduce the unit and name `CORE-001` as the authority
  in the next breath (`design.md`, Decision 4).
- `docs/14-glossary.md`'s *Unit Base* entry — a glossary defines the term.
- `docs/08-vehicles.md`'s two `VEH-028` derivations — "A Unit Base is 12 plate layers
  tall on a narrowest side of 3 studs — 4 plate layers for every stud" and "one Unit
  Base of height for every two studs" — and the glossary's *Maximum Height* entry,
  which restates the second as "half a Unit Base". Out of scope (`proposal.md`).
- `assets/IMAGES.md`'s `CORE-001` image entry — the figure and the measurement plane
  belong to the next change.
- `CHANGELOG.md`, every `**Version:**` header, and `openspec/specs/`
  (`system/documentation-standards.md`, Versioning; `system/workflow.md`, Archiving).

No spec delta is written — `design.md`, "Why no spec delta".

---

## 1. `docs/01-foundations.md` — verify only

- [x] 1.1 **Verify only, change nothing.** The Unit Base overview states `**4 studs wide × 3 studs deep × 12 plate layers tall**` and then points at `02-core-rules.md`, CORE-001. It keeps both (`design.md`, Decision 4). Confirm the file is unedited at the end of the change.

---

## 2. `docs/02-core-rules.md` — `CORE-001`

- [x] 2.1 In `CORE-001`, replace this anchor:

```
The height is read from the model rather than chosen. Infantry occupies exactly one Unit Base whether standing or seated (`09-transport.md`, TRN-002), so a Unit Base must contain a standing minifigure — about 4 bricks from its feet to the top of its head (`05-construction-components.md`, CMP-018). Twelve plate layers is the smallest whole-brick height that does, and a Unit Base is the minimum operational space an object needs (`09-transport.md`, TRN-001), so it takes exactly that and no more.
```

with:

```
The height is read from the model rather than chosen. Infantry occupies exactly one Unit Base whether standing or seated (`09-transport.md`, TRN-002), so a Unit Base must contain a standing minifigure — about 4 bricks from its feet to the top of its head. Twelve plate layers is the smallest whole-brick height that does, and a Unit Base is the minimum operational space an object needs (`09-transport.md`, TRN-001), so it takes exactly that and no more.
```

One citation is removed and nothing else changes. `CORE-001` states the minifigure
height itself, so citing `CMP-018` for it made each document the other's source
(`design.md`, Decision 5). Every figure in this paragraph stays.

---

## 3. `docs/05-construction-components.md` — `CMP-018`

- [x] 3.1 In `CMP-018`, replace this anchor:

```
**Height** is measured the same way. The Unit Base's vertical projection is 4 studs by 12 plate layers (`02-core-rules.md`, CORE-001), so an opening that passes infantry must be at least that clear. A minifigure on its base stands about 4 bricks tall, which is where those 12 plate layers come from. A model taller than one Unit Base is measured by its own height in plate layers.
```

with:

```
**Height** is measured the same way. An opening that passes infantry must be at least as clear as the Unit Base's vertical projection — see `02-core-rules.md`, CORE-001, which dimensions that projection and says where its height comes from. A model taller than one Unit Base is measured by its own height in plate layers.
```

The paragraph keeps its own rule and loses both the figures and the derivation. The
paragraph beginning "**Width** is not a judgment call" and every other paragraph of
`CMP-018` are untouched.

---

## 4. `docs/08-vehicles.md` — `VEH-028`

- [x] 4.1 In `VEH-028`, replace this anchor:

```
It also bounds how many interior levels a footprint carries, while saying nothing about capacity. N levels need `12N + (N − 1)` plate layers above the lowest floor (`09-transport.md`, TRN-020), so a vehicle 4 studs across has room for one level, 8 studs for three, and 12 studs for five. A wide vehicle may still stack decks; a narrow one cannot.
```

with:

```
It also bounds how many interior levels a footprint carries, while saying nothing about capacity. Each level needs one Unit Base of clear height and each floor above the lowest a plate of its own (`09-transport.md`, TRN-020), so a vehicle 4 studs across has room for one level, 8 studs for three, and 12 studs for five. A wide vehicle may still stack decks; a narrow one cannot.
```

**One level, three, five — those three answers are unchanged and were re-derived. Do
not recompute or "correct" them.**

- [x] 4.2 **Verify only, change nothing.** Two paragraphs elsewhere in `VEH-028` keep their figures, both out of scope (`proposal.md`): the one beginning "Six plate layers is two standard bricks, and one Unit Base of height for every two studs", and the one beginning "The multiplier is read off the Unit Base rather than chosen". Locate each by its opening words rather than by position. Confirm both are unedited.

---

## 5. `docs/09-transport.md` — `TRN-001`, `TRN-003`, `TRN-013`, `TRN-019`, `TRN-020`, Summary

- [x] 5.1 In `TRN-001`, replace this anchor:

```
Every transported object occupies Unit Base volume — one or more whole Unit Bases, or a share of one where the object is cargo shorter than a Unit Base (TRN-013). See `02-core-rules.md` (CORE-001) for the Unit Base definition: a volume of 4 × 3 studs by 12 plate layers.
```

with:

```
Every transported object occupies Unit Base volume — one or more whole Unit Bases, or a share of one where the object is cargo shorter than a Unit Base (TRN-013). See `02-core-rules.md` (CORE-001) for the Unit Base definition.
```

- [x] 5.2 In `TRN-003`, replace this anchor:

```
Count the Unit Bases its floor holds, then check its clearance (TRN-019): a position with less than 12 plate layers above it is a partial Unit Base, not a whole one.
```

with:

```
Count the Unit Bases its floor holds, then check its clearance (TRN-019): a position with less than one Unit Base of clear height above it is a partial Unit Base, not a whole one.
```

- [x] 5.3 In `TRN-003`'s example, replace this anchor:

```
2 × 4 UB, 12 plate layers of clearance
```

with:

```
2 × 4 UB, one Unit Base of clear height
```

- [x] 5.4 In `TRN-003`'s list of possible loads, replace this anchor:

```
- 6 infantry + six ammo crates of 4 plate layers each — three crates fill one Unit Base, so six fill two
```

with:

```
- 6 infantry + six ammo crates of 4 plate layers each — three crates share one Unit Base, so six take two
```

"Fill" asserted that three crates come to exactly a Unit Base's height, which is
arithmetic on the figure. "Share" is what `TRN-013` actually permits. The other three
bullets of that list are untouched.

- [x] 5.5 In `TRN-013`, replace this anchor:

```
A Unit Base divides into **slices**. A slice measures 4 × 3 studs by the height of the object standing in it, and the slices sharing one Unit Base may total no more than 12 plate layers — see `02-core-rules.md` (CORE-001).
```

with:

```
A Unit Base divides into **slices**. A slice measures 4 × 3 studs by the height of the object standing in it, and the slices sharing one Unit Base may total no more than the Unit Base's height — see `02-core-rules.md` (CORE-001).
```

One phrase changes. **Add no sentence about what happens when cargo exceeds that
budget** — that question is open and out of scope (`design.md`, Decision 3). The two
bullets that follow this paragraph are untouched.

- [x] 5.6 In `TRN-013`, replace this table. **Four-backtick fences; the table inside is real markdown.** The `Space` column is removed; **every `Footprint` and `Height` cell keeps its exact current text**:

````
| Cargo | Footprint | Height | Space |
|---|---|---|---|
| Ammo crate | 1 UB | 4 plate layers | ⅓ UB |
| Fuel drum pallet | 1 UB | 8 plate layers | ⅔ UB |
| Drone | 1 UB | 12 plate layers | 1 UB |
| Motorbike | 2 UB | 12 plate layers | 2 UB |
| Walker | 2 UB or more | 12 plate layers | its footprint |
````

with:

````
| Cargo | Footprint | Height |
|---|---|---|
| Ammo crate | 1 UB | 4 plate layers |
| Fuel drum pallet | 1 UB | 8 plate layers |
| Drone | 1 UB | 12 plate layers |
| Motorbike | 2 UB | 12 plate layers |
| Walker | 2 UB or more | 12 plate layers |
````

The three `12 plate layers` heights are measured values read from a model, not
restatements of `CORE-001`, and they stay (`design.md`, Decision 3). The sentence
below the table is untouched.

- [x] 5.7 In `TRN-013`, replace this anchor:

```
Three ammo crates of 4 plate layers therefore fill one Unit Base exactly. A crate and a minifigure never share one: the minifigure occupies a whole Unit Base standing or seated (TRN-002), and 4 + 12 plate layers does not fit in 12.
```

with:

```
Three ammo crates of 4 plate layers therefore share one Unit Base. A crate and a minifigure never share one: the minifigure occupies a whole Unit Base standing or seated (TRN-002), leaving no slice for the crate.
```

- [x] 5.8 In `TRN-019`, replace this anchor:

```
A Unit Base is 12 plate layers tall, and what must fit inside a vehicle is the Unit Base itself rather than the loose model (`02-core-rules.md`, CORE-001; `04-construction-standard.md`, SCS-005). A closed compartment offering less than 12 plate layers of clear height therefore holds no whole Unit Base.
```

with:

```
What must fit inside a vehicle is the Unit Base itself rather than the loose model (`02-core-rules.md`, CORE-001; `04-construction-standard.md`, SCS-005). A closed compartment is therefore measured by the clear height above the surface a model stands on, not by the space its contents could be squeezed into: a position offering less than one Unit Base of clear height is a partial Unit Base (TRN-003), and holds no whole one.
```

The old paragraph's "therefore" rested on the figure in its first clause. Removing the
figure without replacing the premise would leave a sentence that restates itself, so
the criterion — clear height, not the loose model — is stated instead.

- [x] 5.9 In `TRN-019`, replace this anchor:

```
Clearance is measured from the surface a model stands or sits on, upward to whatever is above it. That surface is the model's floor, not an obstruction: a bench 3 plate layers high needs 12 clear layers *above the bench*. Seating raises the roof a compartment needs rather than shrinking its occupant — which is what TRN-017 already means by "benches reduce available cargo space".
```

with:

```
Clearance is measured from the surface a model stands or sits on, upward to whatever is above it. That surface is the model's floor, not an obstruction: a bench 3 plate layers high needs one Unit Base of clear height *above the bench*. Seating raises the roof a compartment needs rather than shrinking its occupant — which is what TRN-017 already means by "benches reduce available cargo space".
```

- [x] 5.10 In `TRN-019`, replace this anchor:

```
- **Infantry and crew need the full 12 plate layers.** An infantry model occupies exactly one Unit Base whether standing or seated (TRN-002), and a crew member occupies one like any other passenger (TRN-014). A compartment shorter than that carries neither.
```

with:

```
- **Infantry and crew need one Unit Base of clear height.** An infantry model occupies exactly one Unit Base whether standing or seated (TRN-002), and a crew member occupies one like any other passenger (TRN-014). A compartment shorter than that carries neither.
```

- [x] 5.11 In `TRN-019`, replace this anchor:

```
- **Cargo needs only its own height.** Cargo divides a Unit Base (TRN-013), so a compartment 9 plate layers high carries cargo up to 9 plate layers — three quarters of a Unit Base per position.
```

with:

```
- **Cargo needs only its own height.** Cargo divides a Unit Base (TRN-013), so a compartment 9 plate layers high carries cargo up to 9 plate layers — a partial Unit Base per position, in TRN-003's sense.
```

- [x] 5.12 In `TRN-019`, replace this anchor:

```
**What this costs an existing model.** A closed compartment built under 12 plate layers stops carrying infantry, and that includes a closed cockpit: a Pilot with no Unit Base is no Pilot, and a vehicle without a Pilot cannot move — see `08-vehicles.md` (VEH-013). Raising the roof by a plate or two, or opening it, is the whole repair.
```

with:

```
**What this costs an existing model.** A closed compartment built under one Unit Base of clear height stops carrying infantry, and that includes a closed cockpit: a Pilot with no Unit Base is no Pilot, and a vehicle without a Pilot cannot move — see `08-vehicles.md` (VEH-013). Raising the roof by a plate or two, or opening it, is the whole repair.
```

- [x] 5.13 In `TRN-020`, replace this block. **Four-backtick fences: the anchor contains a three-backtick fenced block, and both blocks contain a markdown table.** The anchor runs from the rule's first paragraph to the paragraph ending "It is one plate short." — six paragraphs including the fenced formula and the table, replaced by four:

````
A vehicle may stack interior levels, and each level above the lowest must pay for its own floor.

N levels require:

```
12N + (N − 1) plate layers
```

measured above the lowest interior floor.

| Levels | Plate layers | Bricks |
|---|---|---|
| 1 | 12 | 4 |
| 2 | 25 | 8 + 1 plate |
| 3 | 38 | 12 + 2 plates |

The `(N − 1)` term is the intermediate floors at their thinnest, one plate each; a floor built thicker costs what it actually measures. The lowest level rests on the vehicle's own hull and pays nothing for it — which is why a vehicle exactly 8 bricks tall does not hold two levels. It is one plate short.
````

with:

````
A vehicle may stack interior levels, and each level above the lowest must pay for its own floor.

Each level needs one Unit Base of clear height above its own floor (`02-core-rules.md`, CORE-001), and each floor above the lowest costs what it measures — one plate at its thinnest.

| Levels | Clear height needed above the lowest interior floor |
|---|---|
| 1 | one Unit Base |
| 2 | two Unit Bases + 1 plate |
| 3 | three Unit Bases + 2 plates |

The lowest level rests on the vehicle's own hull and pays nothing for it — which is why an interior exactly two Unit Bases tall does not hold two levels. It is one plate short.
````

The column header carries "clear height", so the cells do not repeat it. The
`Plate layers` and `Bricks` columns both go: they are `CORE-001` arithmetic
(`design.md`, Decision 2). The two paragraphs that follow — "Each level is a cargo
compartment like any other…" and "How many levels a vehicle has room for…" — are
**not** part of the anchor and are untouched.

- [x] 5.14 In the Summary, replace this anchor:

```
4. A closed compartment shorter than 12 plate layers carries cargo but no infantry, crew included.
```

with:

```
4. A closed compartment shorter than one Unit Base of clear height carries cargo but no infantry, crew included.
```

The other eight numbered items are untouched.

---

## 6. `docs/10-weapons.md` — `WPN-004`

- [x] 6.1 Replace this anchor:

```
Platform Length is the largest **horizontal** dimension of the Unit Base or vehicle carrying the weapons. A Unit Base is a volume — see `02-core-rules.md` (CORE-001) — and this reads its horizontal projection, so infantry's Platform Length stays 4 studs and the Unit Base's 12 plate layers of height never enter the calculation.
```

with:

```
Platform Length is the largest **horizontal** dimension of the Unit Base or vehicle carrying the weapons. A Unit Base is a volume — see `02-core-rules.md` (CORE-001) — and this reads its horizontal projection, so infantry's Platform Length stays 4 studs and the Unit Base's height never enters the calculation.
```

Note the verb: "layers … never enter" becomes "height … never enters".

---

## 7. `docs/14-glossary.md` — *Interior Clearance* and *Slice*

- [x] 7.1 Replace this anchor:

```
The clear height inside a closed compartment, measured in plate layers from the surface a model stands or sits on. Less than 12 plate layers — one Unit Base — carries cargo but no infantry. See `09-transport.md` (TRN-019).
```

with:

```
The clear height inside a closed compartment, measured in plate layers from the surface a model stands or sits on. Less than one Unit Base of clear height carries cargo but no infantry. See `09-transport.md` (TRN-019).
```

The entry still says clearance is *measured* in plate layers, which is true and is not
the figure this change removes.

- [x] 7.2 Replace this anchor:

```
The share of a Unit Base one cargo object occupies: 4 × 3 studs by that object's own height. Slices sharing a Unit Base may total no more than 12 plate layers, and infantry never occupies a slice — it occupies the whole Unit Base. See `09-transport.md` (TRN-013).
```

with:

```
The share of a Unit Base one cargo object occupies: 4 × 3 studs by that object's own height. Slices sharing a Unit Base may total no more than the Unit Base's height, and infantry never occupies a slice — it occupies the whole Unit Base. See `09-transport.md` (TRN-013).
```

- [x] 7.3 **Verify only, change nothing.** Three entries keep what they have: *Unit Base* ("a volume 4 studs wide, 3 studs deep and 12 plate layers tall") because a glossary defines the term; *Maximum Height* ("6 plate layers — two bricks, half a Unit Base — for every stud") because it restates a `VEH-028` derivation that is out of scope; and *Cargo Bay*, which already reads "less than one Unit Base of clearance". Confirm all three are unedited.

---

## 8. `assets/IMAGES.md`

- [x] 8.1 In the rejected-candidates list, replace this anchor:

```
- **TRN-020 (Interior Levels)** — The stacking is arithmetic on a height the CORE-001 image already dimensions: N levels need `12N + (N − 1)` plate layers. VEH-028 works the answer out in its own text for footprints 4, 8 and 12 studs across, so nothing is left for a picture to settle.
```

with:

```
- **TRN-020 (Interior Levels)** — The stacking is arithmetic on a height the CORE-001 image already dimensions: one Unit Base of clear height per level, plus a plate for each floor above the lowest. VEH-028 works the answer out in its own text for footprints 4, 8 and 12 studs across, so nothing is left for a picture to settle.
```

The rejection stands; only the quotation of the deleted formula changes.

- [x] 8.2 In the `TRN-019` image entry, replace this anchor. It is a fragment of one long table cell — do not reflow the row, and change nothing else in it:

```
First, a bare floor with 12 clear layers to the roof, holding one Unit Base. Second, the same compartment with a bench 3 plate layers high on its floor, the measurement starting at the bench's top surface and the 12 layers it needs marked above that, running past the roof and labelled as failing.
```

with:

```
First, a bare floor whose clear height to the roof is exactly one Unit Base, holding one Unit Base. Second, the same compartment with a bench 3 plate layers high on its floor, the measurement starting at the bench's top surface and the Unit Base of clear height it needs marked above that, running past the roof and labelled as failing.
```

The cell's opening sentence — "with every clear height dimensioned in plate layers" —
is untouched: the drawing still carries numbers, and the illustrator reads them from
`CORE-001` like every other figure in the brief.

- [x] 8.3 **Verify only, change nothing.** The `CORE-001` image entry ("dimensioned 4 studs wide × 3 studs deep × 12 plate layers tall … the plate it stands on marked as floor, outside the volume") is out of scope (`design.md`, Decision 6). Confirm it is unedited.

---

## 9. Verification

Each command below was run against the pre-change tree and the "before" figure is what
it actually returned. Run each one after applying, and report any figure that differs
from "after" **without editing a document to make a check pass**.

- [x] 9.1 `grep -rn "12 plate layers" docs/ | wc -l` — before: **22**, after: **9**: three lines in `docs/02-core-rules.md`, three in `docs/09-transport.md` (the cargo table's `Height` cells, task 5.6), and one each in `docs/01-foundations.md`, `docs/08-vehicles.md` and `docs/14-glossary.md`. Counting occurrences rather than lines — `grep -ro "12 plate layers" docs/ | wc -l` — the figures are **24** before and **9** after.

- [x] 9.2 `grep -c "12 plate layers" docs/05-construction-components.md docs/10-weapons.md` — before: `1`, `1`. After: `0`, `0`. (`grep -c` counts lines; `docs/05-construction-components.md` holds two occurrences on its one line.)

- [x] 9.3 `grep -c "12 plate layers" docs/09-transport.md` — before: **12** (13 occurrences), after: **3** — the three `Height` cells of `TRN-013`'s cargo table, which task 5.6 keeps.

- [x] 9.4 `grep -rn "12N" docs/ assets/IMAGES.md | wc -l` — before: **3**, after: **0**.

- [x] 9.5 `grep -rn "⅓\|⅔\|three quarters" docs/ | wc -l` — before: **3**, after: **0**.

- [x] 9.6 `grep -c "one Unit Base of clear height" docs/09-transport.md docs/08-vehicles.md docs/14-glossary.md` — before: `0`, `0`, `0`. After: **8**, **1**, **1**.

- [x] 9.7 No variant phrasing was introduced: `grep -rn "a full Unit Base\|the full Unit Base\|Unit Base of clearance" docs/` — before: **1** (`docs/14-glossary.md`'s *Cargo Bay*, "less than one Unit Base of clearance", which no task edits), after: **1**, the same line.

- [x] 9.8 The out-of-scope derivations survive: `grep -c "one Unit Base of height for every two studs" docs/08-vehicles.md` and `grep -c "half a Unit Base" docs/14-glossary.md` — before: `1`, `1`. After: `1`, `1`.

- [x] 9.9 `python3 scripts/lint_ruleset.py` — exits 0, no findings. It checks `assets/IMAGES.md`'s filenames too (`.claude/rules/assets.md`); tasks 8.1 and 8.2 change no filename.

- [x] 9.10 `python3 scripts/check_delta_coverage.py` — exits 0. This change writes no delta.

- [x] 9.11 `git status --porcelain` — exactly eight paths modified or added: `docs/02-core-rules.md`, `docs/05-construction-components.md`, `docs/08-vehicles.md`, `docs/09-transport.md`, `docs/10-weapons.md`, `docs/14-glossary.md`, `assets/IMAGES.md`, and this change's own directory. **`docs/01-foundations.md`, `README.md` and `CODE_OF_DESIGN.md` must not appear.** Nothing under `openspec/specs/`, no `CHANGELOG.md`, no `**Version:**` header.

- [x] 9.12 `grep -rn "Version:" docs/*.md | grep -c "0.2.0 Draft"` — before: **15**, after: **15**. No header moves.

- [x] 9.13 Report anything that had to be interpreted. Every interpretation is a place this proposal was unclear (`system/delegating-to-agents.md`).
