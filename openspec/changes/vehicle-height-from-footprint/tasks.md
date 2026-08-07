## 0. Setup

- [x] 0.1 Work on branch `vehicle-height-from-footprint` (`openspec/config.yaml` requires one dedicated branch per proposal, and `system/repository-strategy.md` requires it to be named for the change). The branch already exists and is checked out. Do not create another, do not leave it, do not commit, do not push.

### How to read the replacement blocks

Replacement text is shown as a markdown blockquote so it is visually separable from the instructions around it. **The `> ` prefix is not part of the text.** Strip it from every line before writing into the document.

Where a block contains a `#` heading, a `|` table, a `---` separator, a fenced code span or bold markers, those are part of the text and must be written as real markdown.

Exactly one line in this document is a blockquote in the finished text as well: the closing motto in task 6.1, which is shown there as `> > ` for that reason and is called out in the task itself. Everywhere else, a written line that still starts with `> ` was stripped wrongly.

### What "the body of a rule" means

Everything between that rule's `#` heading line and the `---` that ends it. **Never change, remove or renumber an existing heading.** Three rule IDs are added — `VEH-028`, `VEH-029`, `VEH-030` — and none is renumbered. Task 7.2 checks the count.

### Anchors

Every quoted anchor below was checked with `grep -cF` against the pre-change files and returns exactly **1**. If an anchor returns anything other than 1, stop and report it instead of guessing which occurrence was meant.

### Scope

| Path | What changes |
|---|---|
| `docs/08-vehicles.md` | three new rules after `VEH-027`; one line in `VEH-001`; one line in the Summary |
| `docs/02-core-rules.md` | one sentence at the end of `CORE-001` |
| `docs/06-deployment.md` | one paragraph in `DEP-003`; one paragraph in `DEP-006` |
| `docs/09-transport.md` | one cross-reference line at the end of `TRN-020` (task 8.7) |
| `docs/14-glossary.md` | two entries appended, before the closing motto |

Nothing else. No `**Version:**` header and no `CHANGELOG.md` entry (`system/documentation-standards.md`, Versioning). `openspec/specs/` is untouched — archiving is a separate PR (`system/workflow.md`), and this change writes no spec delta at all: `08-vehicles.md` and `06-deployment.md` have never been formalised as capabilities, and the `CORE-001` sentence being edited is not in `openspec/specs/unit-base/spec.md` (`system/proposal-review.md`, "Delta vs. Direct Edit"). The three files in this change directory are not edited either.

### One idea, stated once

- The ratio, its derivation, the worked table and what an illegal build means live in **`VEH-028`**. Everything else cites it.
- The datum lives in **`VEH-029`**. Nothing else re-derives it.
- What counts, and when it is measured, lives in **`VEH-030`**. Do not restate the Gameplay/Visual split in `VEH-028`, and do not add a parts list to either — `15-geometry-layers.md` (GEO-001, GEO-002) owns that test.
- The **height** half of an externally carried model is `VEH-030`'s; the **Deployment Area** half is `DEP-006`'s. Each states its own half and points at the other. Neither states both.
- `VEH-028` does **not** restate what a plate and a brick count as. `VEH-021` already does, in the same document, and `VEH-028` cites it.
- `VEH-001`, the Summary, `CORE-001`, `DEP-003` and both glossary entries carry a one-line cross-reference and no reasoning of their own.

### Coverage

| Item in `proposal.md` / `design.md` | Task |
|---|---|
| `VEH-028` Maximum Height: ratio, derivation on the narrowest side, footprint as operand, table, orientation, illegal builds, interior-level bound (decisions 1, 2, 8) | 1.1 |
| `VEH-029` Base Plane: datum, unpowered vehicles, vehicle-in-vehicle, ground clearance (decision 3) | 1.1 |
| `VEH-030` What Counts Toward Height: Gameplay Geometry, plastic measured in plate layers, movable elements, external models, when the check is made (decisions 2, 4, 5, 6) | 1.1 |
| `VEH-001` gains a cross-reference and keeps its wording | 2.1 |
| `08-vehicles.md` Summary gains one line, keeps six characteristics (decision 7) | 3.1 |
| `CORE-001`'s "says nothing about a model's height" is qualified | 4.1 |
| `DEP-003` gains a cross-reference | 5.1 |
| `DEP-006` owns the Deployment Area half of an externally carried model (decision 6) | 5.2 |
| That paragraph sits at the end of `DEP-006`, not ahead of its "strategic advantages" line | 5.3 |
| Glossary gains `Maximum Height` and `Base Plane` | 6.1 |
| Structural checks | 7.1 |
| Rule-ID count | 7.2 |
| Cross-reference phrasing lands in three places | 7.3 |
| Glossary term count | 7.4 |
| Applier's report | 7.5 |
| Post-apply audit findings 2 – 10 | 8.1 – 8.9 |

---

## 1. New rules in `docs/08-vehicles.md`

- [x] 1.1 Insert three new rules **after the `---` that closes `VEH-027`, and before the `# Summary` heading**.

  Anchor (`grep -cF` returns 1): `This needs no separate walker rule.`

  That sentence opens `VEH-027`'s final paragraph. The document currently reads:

  ```
  This needs no separate walker rule. A walker whose knee clears the whole rise simply crosses it under VEH-021 — a tall enough walker steps over a flight of stairs the same way it steps over a wall.

  ---

  # Summary
  ```

  Write the block below between that `---` and `# Summary`, keeping one blank line either side of it. **`VEH-027`'s text is not touched, and the `# Summary` heading is not touched** — the new rules go above it, not inside it.

  > # VEH-028 — Maximum Height
  >
  > A vehicle's footprint (VEH-001) governs how high it may build, as well as how much Deployment Area it costs (`06-deployment.md`, DEP-003).
  >
  > **For every stud across the narrowest side of its footprint, a vehicle may rise 6 plate layers.**
  >
  > The footprint is the Unit Bases the vehicle covers — the ones DEP-003 charges. Written `A × B` UB it measures `4A × 3B` studs (`02-core-rules.md`, CORE-001), so its narrowest side is the smaller of those two numbers. Where an outline is not rectangular, read `A × B` as the smallest rectangle of Unit Bases enclosing it. That rectangle serves this measurement only and changes no vehicle's Deployment Area, which DEP-003 still charges per Unit Base actually covered.
  >
  > Six plate layers is two standard bricks, and one Unit Base of height for every two studs (CORE-001). The limit is stated in plate layers because that is the unit VEH-021 already uses for vertical distance, and because a hull with plates in it reaches heights no whole brick count expresses: a vehicle 22 plate layers tall is legal where the limit is 24, and no count of bricks says so.
  >
  > The multiplier is read off the Unit Base rather than chosen. A Unit Base is 12 plate layers tall on a narrowest side of 3 studs, so the standing minifigure that fills one stands 4 plate layers for every stud of its own narrowest side (CORE-001). A vehicle is allowed half as much again. That is this rule's only design decision.
  >
  > Footprints below are VEH-001's; only the two right-hand columns belong to this rule.
  >
  > | Vehicle | Footprint | Studs | Narrowest side | Maximum Height |
  > |---|---|---|---:|---:|
  > | Bike | 1 × 2 UB | 4 × 6 | 4 | 24 plate layers (8 bricks) |
  > | Buggy | 2 × 2 UB | 8 × 6 | 6 | 36 plate layers (12 bricks) |
  > | Jeep | 2 × 3 UB | 8 × 9 | 8 | 48 plate layers (16 bricks) |
  > | Tank | 2 × 5 UB | 8 × 15 | 8 | 48 plate layers (16 bricks) |
  > | Heavy Transport | 3 × 8 UB | 12 × 24 | 12 | 72 plate layers (24 bricks) |
  >
  > Tank and Jeep share a limit because they share a narrowest side. Stretching a vehicle along its long axis buys it nothing: a long thin vehicle is still a thin vehicle.
  >
  > The same two Unit Bases give different limits depending on how they are arranged — side by side (2 × 1 UB, 8 × 3 studs) they allow 18 plate layers, front to back (1 × 2 UB, 4 × 6 studs) 24. That is not an exploit to close. The arrangement is built into the model, chosen once at the bench and paid for in the shape of the vehicle. Turning the finished model on the table changes nothing, because the narrowest side is a property of the rectangle and not of which way it points.
  >
  > A vehicle taller than its Maximum Height is not a legal vehicle. It cannot be deployed until it is rebuilt, either by lowering the construction or by widening the footprint, which raises the limit. There is no penalty, no marker and no in-game state: this is a construction check made once before the game, exactly like the two-Unit-Base minimum (`02-core-rules.md`, CORE-004; VEH-013). Legality is settled before deployment and never revisited, so a vehicle whose construction is altered in play (VEH-018) is not measured again.
  >
  > This caps no dimension of its own. VEH-001's "No maximum vehicle size exists" stays true as written — a footprint may be any size, and the height allowed grows with it. What this rule fixes is the relationship between the two, and it introduces no height statistic, vehicle class or size category to do it.
  >
  > It also bounds how many interior levels a footprint carries, while saying nothing about capacity. N levels need `12N + (N − 1)` plate layers above the lowest floor (`09-transport.md`, TRN-020), so a vehicle 4 studs across has room for one level, 8 studs for three, and 12 studs for five. A wide vehicle may still stack decks; a narrow one cannot.
  >
  > ---
  >
  > # VEH-029 — Base Plane
  >
  > Maximum Height (VEH-028) is counted from the vehicle's own **Base Plane**: the lowest surface on which one of its Unit Bases rests — its interior floor. Where a vehicle has floors at several heights, the lowest governs. It is the same surface interior levels are measured from (`09-transport.md`, TRN-020).
  >
  > A powered vehicle always has one, because it carries a Pilot occupying a Unit Base of its own (VEH-013; `09-transport.md`, TRN-014), and that Unit Base rests on something. A vehicle with no Pilot and no interior — a trailer, a towed gun, an open flatbed — takes its lowest structural floor instead: the surface its load rests on.
  >
  > The Base Plane is a property of the model, not of the table. A vehicle on a hill, in a depression or part-way up a ramp measures exactly as it does on flat ground, so terrain elevation never changes what is legal. A vehicle carried inside another vehicle (`09-transport.md`, TRN-001, TRN-003) is read the same way: each vehicle is measured against its own Base Plane, and the carrier's floor is the carried vehicle's ground.
  >
  > **Ground clearance is not height.** Everything below the Base Plane is locomotion, measured by its own rules: a wheel by its axle (VEH-022), a leg by its knee (VEH-023), a hover assembly by its full height (VEH-024). Those rules already price height in silhouette — VEH-024 calls it "the same trade a walker makes with long legs" — and charging it twice here would make the walkers and hover vehicles they describe illegal. A long-legged walker stays legal however tall its legs. What it may not do is build a tower on top of them.
  >
  > Height is counted straight up from the Base Plane, never along a leaning element. A mast raked backwards is measured by how high it reaches, not by how long it is.
  >
  > ---
  >
  > # VEH-030 — What Counts Toward Height
  >
  > Maximum Height (VEH-028) is counted to the highest point of the vehicle's **Gameplay Geometry** (`15-geometry-layers.md`, GEO-001). Visual Geometry above that point is unrestricted and never makes a vehicle illegal.
  >
  > Height is plastic, measured above the Base Plane (VEH-029) in plate layers. Nothing is converted into anything else: a weapon's Length is a horizontal reading in studs (`10-weapons.md`, WPN-003, WPN-004), and a weapon standing upright is measured by how high its plastic actually reaches.
  >
  > This rule adds no classification of its own, and writes no list of functional and decorative parts — a second list would drift from `15-geometry-layers.md` (GEO-002)'s. Which layer an element belongs to is GEO-001 and GEO-002's question, settled by the test those rules already apply: Gameplay Geometry is the minimum physical information required to play the game, and Visual Geometry is what remains when an element's purpose is purely aesthetic. The table below is that test applied to height, not a new one.
  >
  > | Element | Layer | Counts |
  > |---|---|---|
  > | Bare mast, flag, ornament, non-functional antenna | Visual | No |
  > | Mast carrying an observation post | Gameplay | Yes |
  > | Turret mounting a weapon (`10-weapons.md`, WPN-009) | Gameplay | Yes |
  > | Superstructure holding a crew station (`09-transport.md`, TRN-014) | Gameplay | Yes |
  > | Transport space (`09-transport.md`, TRN-003) | Gameplay | Yes |
  > | Decorative armour bolted onto a structural wall | Visual | No |
  >
  > An element holding a crew position is Gameplay Geometry because a crew member occupies a Unit Base of its own (TRN-014). A mast holding nothing carries no Unit Base and feeds no measured value — GEO-002 lists antennas among its own examples of Visual Geometry for exactly that reason. A mast is therefore measured to the height of whatever it carries, and everything below that point is included automatically; only plastic continuing *above* the last functional element is free.
  >
  > This is not an exception to `15-geometry-layers.md` (GEO-004). GEO-007 settles it: a model does not become invalid, and its measured values do not change, solely as a result of adding Visual Geometry — and a height limit that counted decoration would invalidate a legal vehicle the moment a flag went on it. Access openings ask a different question, whether a model physically passes through (`05-construction-components.md`, CMP-018), and decoration obstructs passage, so it counts there. This rule asks how much functional construction one footprint carries, and a flag carries nothing.
  >
  > Decoration is never free in play, only in legality. A tall decorative mast is real plastic: visible, blocking sight lines and shootable (`02-core-rules.md`, CORE-008; GEO-004). The player who builds one pays in silhouette rather than in a rules violation.
  >
  > **A movable element is measured in the highest position it can physically be placed in during play**, not the position it happens to occupy when checked. A turret that rotates, a barrel that elevates and a ramp that lifts are Gameplay Geometry wherever they are placed; measured as found, the check would be answered by lowering the barrel first and raising it again afterwards.
  >
  > **A model carried on the outside counts too.** Transported models occupy a physically constructed interior space measured in Unit Bases (`09-transport.md`, TRN-001, TRN-003); a model on a roof, bonnet, hull top or the outside of a turret is not in such a space and is not embarked. Nothing forbids placing it there. It counts toward this height, measured in the highest position it can be placed in, because it can see, be seen and be shot at (`02-core-rules.md`, CORE-008, CORE-009) — and it costs Deployment Area of its own, which `06-deployment.md` (DEP-006) owns. The outside of a vehicle is never a cheaper way to carry a model than the inside.
  >
  > The whole check, every externally carried model included, is made once before deployment (VEH-028). A model that mounts, dismounts or is removed in play never causes the vehicle to be measured again.
  >
  > ---

---

## 2. Cross-reference from `VEH-001`

- [x] 2.1 In `docs/08-vehicles.md`, replace the single line

  Anchor (`grep -cF` returns 1): `No maximum vehicle size exists.`

  with:

  > No maximum vehicle size exists. The footprint does bound how high the vehicle may build on it — 6 plate layers for every stud of its narrowest side (VEH-028) — but no dimension of the footprint itself is capped.

  Nothing else in `VEH-001` changes. Its example table is not touched.

---

## 3. `08-vehicles.md` Summary

- [x] 3.1 In the `# Summary` section of `docs/08-vehicles.md`, insert one paragraph **immediately after** the line

  Anchor (`grep -cF` returns 1): `Terrain capability is read from the locomotion like everything else: a wheel's axle, a walker's knee, a hover assembly's height (VEH-021 through VEH-024).`

  leaving a blank line between the two:

  > Height is read from the footprint the same way: a vehicle may rise 6 plate layers for every stud of its narrowest side, counted from its own Base Plane and measured to the top of its Gameplay Geometry (VEH-028 through VEH-030).

  **Verify-only, and deliberate:** the Summary's list of **six** physical characteristics is left exactly as it is. Every entry on that list is read during play; Maximum Height is checked once before deployment and never consulted again, which is why it is not a seventh (`design.md`, decision 7). Do not add an entry and do not change the word "six".

---

## 4. `CORE-001` stops ruling out what `VEH-028` establishes

- [x] 4.1 In `docs/02-core-rules.md`, replace the sentence

  Anchor (`grep -cF` returns 1): `A footprint is a horizontal reading, and says nothing about a model's height.`

  with:

  > A footprint is a horizontal reading, and says nothing about how tall a model actually is — though for a vehicle it does bound how tall the model may be (`08-vehicles.md`, VEH-028).

  It is the last sentence of `CORE-001`'s final paragraph. Nothing else in `CORE-001` changes: the volume, the derivation, the projections table and the physical-check boundary are all untouched.

---

## 5. `docs/06-deployment.md`

- [x] 5.1 Insert one paragraph **immediately after** the line

  Anchor (`grep -cF` returns 1): `This area is unavailable for any other model.`

  leaving a blank line between the two:

  > That same footprint bounds the vehicle's height: 6 plate layers for every stud of its narrowest side (`08-vehicles.md`, VEH-028). The Unit Bases charged here are the ones measured there.

  `DEP-003`'s example and its heading are not touched.

- [x] 5.2 Insert one paragraph **immediately after** the line

  Anchor (`grep -cF` returns 1): `Their occupied space is the transport interior, not additional Deployment Area.`

  leaving a blank line between the two:

  > The waiver is for **embarked** units. A model carried on the outside — on a roof, a bonnet, a hull top or the outside of a turret — is not embarked, so it is deployed individually and costs its own Unit Base (DEP-004). Embarking means occupying a constructed interior space measured in Unit Bases (`09-transport.md`, TRN-001), and an externally carried model counts toward the vehicle's height as well (`08-vehicles.md`, VEH-030).

  `DEP-006`'s example, further down the rule, is not touched.

  **Placement is settled by task 5.3, not by this task.** 5.2 owns the paragraph's text; 5.3 owns where it sits. Apply 5.2 first, then 5.3.

  **Word order in this paragraph is load-bearing, and an earlier draft got it wrong.** That draft read "... is not embarked (`09-transport.md`, TRN-001), so it is deployed individually and costs its own Unit Base (DEP-004)", which fails `scripts/lint_ruleset.py` with `06-deployment.md: references 09-transport.md (DEP-004), which does not exist`. The linter's `CROSS_REF_RE` pairs a backticked filename with the first `(RULE-ID)` within 80 characters after it, whichever document that ID belongs to, so the bare same-document `(DEP-004)` was read as a citation into `09-transport.md`. The same-document bare form is correct and is used untouched elsewhere in this file; the fix is to keep every bare same-document ID more than 80 characters away from any backticked filename that precedes it, which is what the wording above does. **Do not re-order these sentences**, and if the check fails again, report it rather than moving the citation.

- [x] 5.3 Move the paragraph written by task 5.2 to the **end** of `DEP-006`.

  Task 5.2 put it directly after `Their occupied space is the transport interior, not additional Deployment Area.`, which leaves it sitting between that line and `This represents one of the main strategic advantages of transport vehicles.` — so "This" now reads as referring to the exterior-model charge rather than to the waiver, and the document says that charging a model is a strategic advantage. That is the displaced-paragraph failure `system/proposal-review.md` records ("`DMG-004`'s closing paragraph ... was displaced three times as later examples were each inserted ahead of it").

  Delete the paragraph from its current position, and re-insert it — **text completely unchanged, down to the punctuation** — immediately after the last line of `DEP-006`:

  Anchor (`grep -cF` returns 1): `The infantry do not consume additional Deployment Area while embarked.`

  leaving a blank line between that line and the paragraph, and leaving the `---` that closes the rule where it is. `DEP-006` then reads: the waiver, why it is an advantage, the worked example, and last the waiver's boundary.

  Afterwards `grep -cF 'The waiver is for **embarked** units.' docs/06-deployment.md` must return **1**, not 2 — if it returns 2 the paragraph was copied instead of moved. Re-run task 7.1 as well: `scripts/lint_ruleset.py` must still print `Checked 15 docs, no structural issues found.`

---

## 6. Glossary

- [x] 6.1 In `docs/14-glossary.md`, replace the final line

  Anchor (`grep -cF` returns 1): `> **Every Brick Matters.**`

  with the block below. It appends the two new entries after the existing `Projection` entry and keeps the motto as the last line of the file.

  **This is the one block where a `> ` line survives**: the motto is itself a markdown blockquote. In the block below it therefore appears as `> > **Every Brick Matters.**` — after stripping the one blockquote level this task adds, it must be written back as exactly `> **Every Brick Matters.**`.

  > ## Maximum Height
  >
  > The greatest height a vehicle's Gameplay Geometry may reach above its Base Plane: 6 plate layers — two bricks, half a Unit Base — for every stud of its narrowest footprint side. A construction check made before deployment, never an in-game state. See `08-vehicles.md` (VEH-028).
  >
  > ---
  >
  > ## Base Plane
  >
  > A vehicle's lowest interior floor — the surface its own Unit Bases rest on — and the datum its Maximum Height is counted from. A property of the model rather than of the ground beneath it; everything below it is locomotion. See `08-vehicles.md` (VEH-029).
  >
  > ---
  >
  > > **Every Brick Matters.**

  The file currently ends **without** a trailing newline after the motto. Do not add one, and do not reflow anything above the `Projection` entry.

---

## 7. Verification

Each command below was run against the pre-change tree and the number it printed is recorded. Run them again after applying and compare. **If a command disagrees with the expected figure, report it — do not edit any document to make a check pass.**

- [x] 7.1 Structural checks, both required in CI:

  ```bash
  python3 scripts/lint_ruleset.py
  python3 scripts/check_delta_coverage.py
  ```

  Before: `Checked 15 docs, no structural issues found.` and `Checked 3 MODIFIED requirement(s) across all changes. No dropped scenarios.` Both must print the same afterwards — this change adds no document and no delta.

- [x] 7.2 Rule-ID count in the vehicle document:

  ```bash
  grep -c '^# VEH-' docs/08-vehicles.md
  ```

  Before: `27`. After: `30`.

- [x] 7.3 The cross-reference phrasing, shared by the three places that cite the ratio without restating its derivation:

  ```bash
  grep -rcF '6 plate layers for every stud of its narrowest side' docs/
  ```

  Before: `0` in every file. After: `2` in `docs/08-vehicles.md` (`VEH-001` and the Summary) and `1` in `docs/06-deployment.md` (`DEP-003`) — three occurrences across two files. Every other file stays at `0`. `VEH-028`'s own headline reads "across the narrowest side of its footprint" and the glossary reads "narrowest footprint side"; neither is matched by this pattern, and that is expected rather than a miss.

- [x] 7.4 Glossary term count:

  ```bash
  grep -c '^## ' docs/14-glossary.md
  ```

  Before: `46`. After: `48`.

- [x] 7.5 Report, for the session that raised you: what was applied, any check that disagreed with the figure above and how, and every point at which this document left you to interpret something.

---

## 8. Corrections from the post-apply audit

These nine tasks repair defects found by reading the applied text, not the diff (`system/proposal-review.md`). **Every one is a replacement of text that is already in the document.** In each, the anchor is the text as it stands now, and it was checked with `grep -cF` against the applied tree — each returns exactly **1**. Replace, do not insert; the surrounding paragraphs are untouched in every case.

The citation wording in 8.1, 8.2 and 8.7 was tested against `scripts/lint_ruleset.py`'s own `CROSS_REF_RE` and `COMMA_REF_RE` before being written here, and each resolves to the file it names. Do not re-order any of these sentences (see task 5.2's note on why word order is load-bearing here).

- [x] 8.1 `docs/06-deployment.md`, `DEP-003` — the second sentence contradicts `VEH-028`'s non-rectangular clause, which says the enclosing rectangle "changes no vehicle's Deployment Area". Replace the whole paragraph

  Anchor: `That same footprint bounds the vehicle's height: 6 plate layers for every stud of its narrowest side (`08-vehicles.md`, VEH-028). The Unit Bases charged here are the ones measured there.`

  with:

  > That same footprint bounds the vehicle's height: 6 plate layers for every stud of its narrowest side (`08-vehicles.md`, VEH-028). Where an outline is not rectangular the height is read from the smallest rectangle of Unit Bases enclosing it, which never changes what is charged here.

- [x] 8.2 `docs/06-deployment.md`, `DEP-006` — `DEP-004` is the **infantry** rule, and "costs its own Unit Base" prices a walker on a roof as one Unit Base when `CORE-004` gives it two or more. Replace the whole paragraph written by tasks 5.2 and 5.3

  Anchor: `The waiver is for **embarked** units. A model carried on the outside — on a roof, a bonnet, a hull top or the outside of a turret — is not embarked, so it is deployed individually and costs its own Unit Base (DEP-004). Embarking means occupying a constructed interior space measured in Unit Bases (`09-transport.md`, TRN-001), and an externally carried model counts toward the vehicle's height as well (`08-vehicles.md`, VEH-030).`

  with:

  > The waiver is for **embarked** units. A model carried on the outside — on a roof, a bonnet, a hull top or the outside of a turret — is not embarked, so it is deployed individually and costs Deployment Area of its own: one Unit Base for an infantry model (DEP-004), its own footprint for a vehicle (DEP-003). Embarking means occupying a constructed interior space measured in Unit Bases (`09-transport.md`, TRN-001), and an externally carried model counts toward the carrier's height as well (`08-vehicles.md`, VEH-030).

  Its **position** is whatever task 5.3 left it at — the end of `DEP-006`. This task changes the text only; it does not move it again.

- [x] 8.3 `docs/08-vehicles.md`, `VEH-028` — the derivation attributes to the minifigure a proportion the plastic does not have. A minifigure is about one stud deep; the 3 studs are the base's depth, not the figure's. Replace

  Anchor: `The multiplier is read off the Unit Base rather than chosen. A Unit Base is 12 plate layers tall on a narrowest side of 3 studs, so the standing minifigure that fills one stands 4 plate layers for every stud of its own narrowest side (CORE-001). A vehicle is allowed half as much again. That is this rule's only design decision.`

  with:

  > The multiplier is read off the Unit Base rather than chosen. A Unit Base is 12 plate layers tall on a narrowest side of 3 studs — 4 plate layers for every stud, which is the proportion of the volume one person occupies (CORE-001). A vehicle is allowed half as much again. That is this rule's only design decision.

- [x] 8.4 `docs/08-vehicles.md`, `VEH-030` — `WPN-003` measures Weapon Length **along the firing axis**, not horizontally; the word "horizontal" belongs to `WPN-004`'s Platform Length. Replace

  Anchor: `Height is plastic, measured above the Base Plane (VEH-029) in plate layers. Nothing is converted into anything else: a weapon's Length is a horizontal reading in studs (`10-weapons.md`, WPN-003, WPN-004), and a weapon standing upright is measured by how high its plastic actually reaches.`

  with:

  > Height is plastic, measured above the Base Plane (VEH-029) in plate layers. Nothing is converted into anything else: a weapon's Length is measured in studs along its own firing axis (`10-weapons.md`, WPN-003), and a weapon standing upright is measured by how high its plastic actually reaches.

- [x] 8.5 `docs/08-vehicles.md`, `VEH-029` — nothing in the ruleset requires the space below the Base Plane to be locomotion, so the tower this change stops can be rebuilt underneath the datum. It is not being bounded (that would need a leg-versus-lattice classification, and would make `VEH-023`'s walker illegal); it is being **stated**, with the chain that does price it. Insert one paragraph **immediately after**

  Anchor: `A long-legged walker stays legal however tall its legs. What it may not do is build a tower on top of them.`

  leaving a blank line between the two. That sentence ends the "Ground clearance is not height" paragraph; the new paragraph goes between it and `Height is counted straight up from the Base Plane`:

  > A vehicle can therefore gain reach by standing on tall locomotion instead of by building upward, and this limit never sees it. That is deliberate rather than overlooked: it is the walker VEH-023 describes, and it is paid for in silhouette (`02-core-rules.md`, CORE-008) and in legs that are components like any other, destroyed like any other (VEH-017, VEH-018). It is not paid for here.

- [x] 8.6 `docs/08-vehicles.md`, `VEH-030` — its closing paragraph re-derives `VEH-028`'s "checked once, never again" instead of citing it. Replace

  Anchor: `The whole check, every externally carried model included, is made once before deployment (VEH-028). A model that mounts, dismounts or is removed in play never causes the vehicle to be measured again.`

  with:

  > Externally carried models are counted at the one check VEH-028 describes, so a model that mounts, dismounts or is removed in play never causes the vehicle to be measured again.

- [x] 8.7 `docs/09-transport.md`, `TRN-020` — this is the rule the change bounds, and it says nothing back. Insert one line **immediately after**

  Anchor: `Each level is a cargo compartment like any other: its capacity is read from TRN-003 and its clearance from TRN-019.`

  leaving a blank line between the two, and leaving the `---` that closes `TRN-020` where it is:

  > How many levels a vehicle has room for is bounded by its footprint rather than by this rule: a vehicle may rise 6 plate layers for every stud of its footprint's narrowest side (`08-vehicles.md`, VEH-028).

  This is the only edit to `docs/09-transport.md`. Nothing else in `TRN-020`, and no other rule in that document, changes.

- [x] 8.8 `docs/14-glossary.md`, `Base Plane` — "lowest interior floor" excludes the flatbed `VEH-029` wrote a clause for. Replace

  Anchor: `A vehicle's lowest interior floor — the surface its own Unit Bases rest on — and the datum its Maximum Height is counted from.`

  with:

  > A vehicle's lowest floor — the surface its own Unit Bases rest on — and the datum its Maximum Height is counted from.

  The rest of the entry is unchanged, and the `Maximum Height` entry is not touched.

- [x] 8.9 `docs/08-vehicles.md` Summary — "its narrowest side" binds to *a vehicle*, but `VEH-028`'s operand is the footprint's narrowest side, and `design.md` decision 8 records that the two give different answers. Replace

  Anchor: `Height is read from the footprint the same way: a vehicle may rise 6 plate layers for every stud of its narrowest side, counted from its own Base Plane and measured to the top of its Gameplay Geometry (VEH-028 through VEH-030).`

  with:

  > Height is read from the footprint the same way: a vehicle may rise 6 plate layers for every stud of its footprint's narrowest side, counted from its own Base Plane and measured to the top of its Gameplay Geometry (VEH-028 through VEH-030).

  The list of **six** physical characteristics above it is still not touched (task 3.1).

- [x] 8.10 Re-run every check in section 7. Three expectations change because of the edits above, and they are the only three:

  ```bash
  python3 scripts/lint_ruleset.py
  python3 scripts/check_delta_coverage.py
  grep -c '^# VEH-' docs/08-vehicles.md
  grep -rcF '6 plate layers for every stud of its narrowest side' docs/
  grep -rcF "footprint's narrowest side" docs/
  grep -c '^## ' docs/14-glossary.md
  ```

  Expected afterwards: lint and delta coverage print exactly what task 7.1 records; `30`; **`1` in `docs/08-vehicles.md` (`VEH-001` only) and `1` in `docs/06-deployment.md`** — the Summary's occurrence moves to the second pattern, which must return `1` in `docs/08-vehicles.md` and `1` in `docs/09-transport.md`; and `48`.
