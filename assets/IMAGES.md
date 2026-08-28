# Example Images Index

This file indexes the example images the StudCraft ruleset needs. It does not contain images — it specifies which ones are needed, what each must show, and why the rule cannot be fully understood from prose alone, so that a later process can create and insert them.

Entries are selective by design. A rule only appears here if the rule *is* a spatial or geometric fact — something a reader genuinely cannot picture correctly from text — not because an image would be a nice illustration. Purely procedural rules (action costs, turn order) and purely definitional rules are left out even when they are important, because an image adds nothing to them. The final section records the rules that were considered and rejected, and why, so they are not re-proposed without cause.

## Entry format

Every document that needs images gets its own `## docs/<file>.md` section holding one table. The table always has these four columns, in this order:

| Rule | Filename | What it must show | Why text alone is not enough |
|---|---|---|---|

**Rule** — the rule ID exactly as it appears in `docs/` (`WPN-020`, `CORE-001`). For an unnumbered section, its heading text.

**Filename** — the full path in backticks, following the naming convention below.

**What it must show** — an instruction to whoever draws the image, and nothing else. Name the elements, their arrangement, and any labelling the image needs. Write it so someone who has not read the rule could still produce a correct drawing from it.

This column must not contain:

- the rule itself restated — that belongs in `docs/`, and a second copy here drifts;
- justification for the image existing — that is the next column;
- bookkeeping about the entry, such as how many blocks it replaces or when it was added.

**Why text alone is not enough** — the argument. What is genuinely hard to picture, ambiguous, or unstated in the prose. This is where reasoning goes, and it is what a reviewer checks when deciding whether the entry belongs at all.

### An entry describes a rule as it currently reads

So **check the entry whenever the rule it names is reworded**, and re-check it before drawing. Nothing mechanical reports the drift: the linter verifies that the rule ID exists in the document the section names, and a reworded rule keeps its ID. Five entries here were describing rules that had moved on, and every one had passed every check the whole time.

An entry drifting is worse than a stale argument. The *What it must show* column is an instruction to an illustrator, so an image drawn from a stale entry contradicts the rule it was drawn for.

### Rejecting a candidate

Rules considered and turned down go in the final section, each with the reason. That record is the point: without it, the same candidate gets re-proposed by whoever next reads the ruleset and notices the same thing.

### Reclassifying

If a rejected candidate is later accepted, or an accepted one dropped, **do not silently move it.** Leave it in the rejected list struck through, marked reclassified, with a line saying what changed — normally the criterion, not the rule. A reader should be able to see that the earlier judgement was superseded rather than mistaken.

## Naming convention

- For a numbered rule: `assets/images/<rule-id-lowercase>-<short-slug>.<ext>`
  Example: `assets/images/wpn-020-muzzle-placement.png`
- For an unnumbered section: `assets/images/<doc-number>-<short-slug>.<ext>`
  Example: `assets/images/07-terrain-thresholds.png`
- The slug is lowercase, hyphen-separated, 2-4 words, and describes the content shown, not the rule's title.

**A filename follows its rule.** The prefix is the rule ID, or the document number where the Rule cell names a heading — so a rule that is renumbered into another document takes its image's filename with it, and `scripts/lint_ruleset.py` rejects the old name from the moment the entry moves. Rename the drawn file in the same change, or there is nothing to place.

**Format: `.png`, `.jpg`, `.jpeg`, `.gif`, `.svg` or `.webp`.** The rule is about one thing — that a reader can see the image where the ruleset is read. Those are what GitHub and any ordinary Markdown renderer draw inline; a `.psd`, a `.blend` or a `.pdf` is a source file, and belongs somewhere that is not `assets/images/`.

**Weight: 3 MB per image.** Git keeps every version of a binary for ever and stores no deltas between them, so each re-export is a whole new copy — and `system/repository-strategy.md` forbids rewriting history, which is the only way to take one back out. The number sits far above ordinary work on purpose: it is an accident guard, not a budget. A flat render of a build is a few hundred kilobytes, so nothing legitimate meets it.

**Neither rule is a quality bar, and neither must be used as one.** An illustration arrives in whatever its author works in, and lossy compression is a fact about how an image was made rather than about its container. What decides whether an image is good enough is reading it against its entry, and the maintainer accepting it — the `add-image` skill, steps 3 and 4. As guidance and not as a gate: where a reader counts something, plate layers or studs, a lossless export keeps the edges countable.

Files are added as they are drawn, and `scripts/insert_images.py` places each one under the section that specifies it. The rule it keeps is exact in both directions: **an image is embedded in `docs/` exactly when the file exists in `assets/images/` and this file lists it for that section.** An embed placed by hand, with no entry here, is therefore removed — the entry is where the argument for the image is written, and the *Why text alone is not enough* column is that argument. `--check` reports each departure and prints the row to add; `--write` repairs them, and because it edits `docs/` it runs on a proposal branch. `assets/images/.gitkeep` holds the directory.

## When an image appears, or disappears

**The procedure is the `add-image` skill** — `.claude/skills/add-image/SKILL.md`. It owns the order: where the drawn file goes, reading it against its entry, asking the maintainer, the proposal that places the image and nothing else, and who is raised for each remaining step.

The split is the one this repository makes everywhere. **This file owns what an entry is; the skill owns what to do about one.** A procedure written down here would be read only by whoever was already reading the index — and the flow begins with a file appearing in `git status`, which sends nobody anywhere.

---

## docs/02-core-rules.md

| Rule | Filename | What it must show | Why text alone is not enough |
|---|---|---|---|
| CORE-001 | `assets/images/core-001-unit-base-volume.png` | One Unit Base built as a stack of plates: 4 studs across the front face, 3 studs deep, 13 plate layers tall, with the layers alternating in colour so a reader can count them. Beside it, on the surface it stands on, the two measures as loose pieces — one 4 studs long for the width, one 3 studs long for the depth. | The height is given in plate layers, and thirteen of them is a quantity nobody converts to a brick in the hand at a glance — the same conversion this file accepts an image for at `Terrain (INF-006 – INF-008)`. Alternating layers make the count readable off the build, and the loose pieces put each horizontal figure beside a real element rather than beside the other number. The rule also calls a Unit Base a volume, which a reader arriving from a game of flat bases reads as a footprint. |

## docs/05-construction-components.md

| Rule | Filename | What it must show | Why text alone is not enough |
|---|---|---|---|
| CMP-018 | `assets/images/cmp-018-clear-opening.png` | A doorway in a vehicle wall, twice. Both times the frame's nominal aperture is dimensioned, a hinged element hangs part-way across it, and the measurement that counts is drawn around that element rather than around the frame — labelled as the clear opening, and dimensioned against the model beside it: at least as wide as that model's front edge and as tall as it stands. In the first the model passes; in the second the same frame fails, with only the hanging element differing between the two. | The frame is what a reader measures and the wrong thing to measure, and no wording of "clear rather than nominal" makes two identical frames visibly different sizes — a drawing of one doorway with two measurements does. It is one of GEO-004's physical checks that needs an image of its own: Cover is declined separately at CORE-010, and Line of Sight is whatever can physically be seen from where the shooter stands, which no drawing of one build settles. |

## docs/08-vehicles.md

| Rule | Filename | What it must show | Why text alone is not enough |
|---|---|---|---|
| VEH-003 | `assets/images/veh-003-length-axis.png` | A vehicle with an irregular or protruding build, with its "longest dimension" axis marked and decorative overhangs excluded from the measurement. | "Longest axis, decorative elements ignored" is simple to state and easy to misjudge on an asymmetric model; an annotated example resolves where the measurement legitimately starts and ends. |
| VEH-008 | `assets/images/veh-008-pivot-points.png` | A wheeled vehicle turning 90° around its rear axle, showing the wide arc the front corner sweeps, next to a tracked/walker/hover vehicle turning around its own centre. | "Pivot point is the rear axle" is one sentence, but a reader cannot picture how far the front of the vehicle swings, or how that differs from a centre-pivot turn (VEH-009 through VEH-011), without seeing both turns drawn. |
| VEH-022 | `assets/images/veh-022-axle-height.png` | A wheel with its axle height (half the wheel's diameter) marked as the Terrain Threshold, plus the fallback measurement (half the track-run height) for a tracked vehicle with no visible axle. | "Axle height" requires identifying the actual rotation point on the model, and the rule supplies a second, different fallback for tracks — both need to be shown against a real build to apply correctly. |
| VEH-023 | `assets/images/veh-023-knee-height.png` | A walker leg with its knee-joint height marked as the Terrain Threshold, plus the fallback (half the leg's standing height) when no distinct knee exists. | Where a "knee" sits on a player-built leg assembly varies model to model; the rule's own fallback shows the answer is meant to be read off the build, which only an image can standardise. |
| VEH-024 | `assets/images/veh-024-hover-assembly-height.png` | A hover vehicle's emitter/pylon/skirt assembly with its full height marked from the ground to where it meets the hull, including an enclosed skirt that reaches the ground and leaves no visible gap. | The threshold is the assembly's height, and the intuitive reading is the gap under the hull. On an enclosed skirt the two differ by the whole assembly and the gap is zero, so the wrong reading produces a legal-looking answer rather than an obviously absent one. |
| VEH-027 | `assets/images/veh-027-ascent-coverage.png` | A slope/ramp fully covering a rise, resting on both the lower and upper surface, next to an invalid example that leaves a gap at the top or bottom. | The rule turns on whether the ramp covers the entire rise and rests on both surfaces — a binary construction fact that is easy to get subtly wrong (a ramp that looks close enough but does not actually touch the upper surface). The angle is not measured, so nothing but contact decides it. |
| VEH-029 | `assets/images/veh-029-resting-surface-datum.png` | A long-legged walker measured from the surface it rests on to the top of its Gameplay Geometry, with the leg assembly shaded as included. The same walker repeated on a slope, and again standing inside a carrier vehicle — each time measured against the same total, with the slope and the carrier's floor marked as changing nothing. | Where the count begins is the whole rule, and everything the model stands up on is part of its height. The repeated panels carry the half prose argues hardest, that terrain and being carried never re-measure a model whose legality was settled at the bench. |

## docs/09-transport.md

| Rule | Filename | What it must show | Why text alone is not enough |
|---|---|---|---|
| TRN-019 | `assets/images/trn-019-clearance-above-bench.png` | A closed compartment in cross-section, three times, with every clear height dimensioned in plate layers. First, a bare floor whose clear height to the roof is exactly one Unit Base — `02-core-rules.md` (CORE-001) gives that height in plate layers — holding one Unit Base. Second, the same compartment with a bench 3 plate layers high on its floor, the measurement starting at the bench's top surface and the Unit Base of clear height it needs marked above that, running past the roof and labelled as failing. Third, the same compartment with a pipe crossing below the roof, the clear height measured under the pipe rather than to the ceiling. | Where the measurement starts is the whole rule, and it runs against intuition twice: a seat raises the roof a compartment needs instead of reducing the space its occupant takes, and an element crossing the ceiling costs clearance exactly as the ceiling does. Both are got wrong by measuring the compartment, which is what a reader without a cross-section measures. Neither neighbouring image carries a datum that moves: CMP-018's doorway measures a fixed aperture, and VEH-029 measures from the surface a vehicle rests on, which a bench inside it does not raise. |

## docs/10-weapons.md

| Rule | Filename | What it must show | Why text alone is not enough |
|---|---|---|---|
| WPN-003 | `assets/images/wpn-003-length-axis-front-face.png` | A weapon body with its firing axis drawn along the body and Weapon Length measured along it, the Weapon Front (WPN-019) outlined on the face the axis exits and distinguished from the other five, and Weapon Width dimensioned as the side of that front face — square, with both of its sides marked equal. Beside it, a body whose front face is `4 × 4` on a body measuring `8 × 4`, the 8 labelled as Length and the 4 as Width. | Width is read off one named face rather than off the body, and a body has three dimensions a reader could reach for instead. The worked `8 × 4` body is the case that separates them: its smallest dimension and its front-face side happen to agree, so a diagram has to show *which* the rule reads, not merely what the number comes to. |
| WPN-020 | `assets/images/wpn-020-muzzle-placement.png` | Five panels: the unpartitioned Weapon Front Footprint the rule starts from, then that same footprint partitioned as twin barrel, quad barrel, heavy cannon and hybrid, each labelled with the Attack Dice and Impact Strengths it produces. | The rule lists its configurations as text and the layout they describe is spatial. One footprint shown yielding four distinct, valid weapons is what makes "no fixed weapon profile" concrete. |

## docs/15-geometry-layers.md

| Rule | Filename | What it must show | Why text alone is not enough |
|---|---|---|---|
| GEO-005 | `assets/images/geo-005-functional-equivalence.png` | Two visually distinct weapons — a bare plate with round studs, and a fully greebled brick-built weapon — built to the same Length, Width and muzzle layout, both producing identical Range, Attack Dice and Impact Strength. | This is the concrete demonstration that Gameplay Geometry and Visual Geometry are separate. The claim — two completely different-looking models playing identically — is far more convincing seen side by side than described. |

## docs/16-damage-system.md

| Rule | Filename | What it must show | Why text alone is not enough |
|---|---|---|---|
| DMG-003 | `assets/images/dmg-003-resistance-cross-section.png` | A shield built from bricks (Resistance 3) and a similarly-sized shield built from four stacked plates (Resistance 4), both with the Impact's direction of travel marked, showing Resistance as the layer count crossed, not the external silhouette. | Resistance is the thickness an Impact crosses in its direction of travel, so two shields of the same external size resolve differently depending on what they are built from. The outside of the model does not carry the answer, and only a cross-section shows it. |
| DMG-012 | `assets/images/dmg-012-composite-targeting.png` | A vehicle (e.g. a jeep) with each independent component — chassis, driver, cannon, four wheels — outlined separately as its own targetable component. | Readers coming from other wargames default to treating "the vehicle" as one target. Seeing a single model broken into several independently-resolving components is the fastest way to unlearn that assumption. |
| DMG-016 | `assets/images/dmg-016-penetration.png` | The worked Heavy Cannon vs. Shield example: an Impact of Strength 6 crossing a Shield of Resistance 3, continuing with Remaining Strength 3 toward a Minifig of Resistance 3 positioned behind it. | Penetration is defined algebraically (`Remaining Strength = Current Strength − Component Resistance`) and depends on components being physically arranged one behind another along the Impact's path — immediate in a side-view diagram, laborious to reconstruct from the formula alone. |

## docs/17-infantry.md

| Rule | Filename | What it must show | Why text alone is not enough |
|---|---|---|---|
| INF-001 | `assets/images/inf-001-base-and-front.png` | An infantry base of `4 × 3` studs, one plate thick, with its 4-stud edge marked as the front and the four directions — forward, rear, left, right — labelled relative to it. | Every infantry distance is counted along one of two axes of this base, and every direction in the document is read from its front edge; a single labelled diagram fixes what "front", "rear", "left" and "right" mean before `INF-002` through `INF-004` use them. Which edge is the front is the kind of fact a reader assumes rather than checks, and assuming the 3-stud edge inverts every measurement that follows. |
| INF-002 | `assets/images/inf-002-axis-measurement.png` | Two moves drawn from one Unit Base, each measured from the face that leads it. Forward: four bases laid end to end along the 3-stud depth, from the front face, dimensioned `4 UB` and `12 studs`. Sideways (INF-003): three bases laid end to end along the 4-stud width, from the corresponding side face, dimensioned `3 UB` and `12 studs`. The two totals drawn to the same length. | `4 UB` forward and `3 UB` sideways are the same distance, and the numbers say the opposite. Each rule names its axis, but a reader comparing the two limits sees 4 against 3 before reading either — and the whole point is that the count differs because the axes do. Two runs drawn to visibly equal length settle it where arithmetic has to be trusted. |
| Terrain (INF-006 – INF-008) | `assets/images/17-terrain-thresholds.png` | Three obstacle heights next to real LEGO bricks/plates: up to 3 plate layers (crossed freely), 4-6 (climbable for +1 AP), 7 or more (impassable without a slope, stair or ramp). | The three thresholds are defined purely in "plate layers," a unit few readers convert to bricks at a glance. Seeing the three bands next to actual brick heights removes the conversion step. |
| INF-011 | `assets/images/inf-011-falling-measurement.png` | A unit falling from a height to "the first surface that physically supports it," with the drop marked in plate layers/bricks, showing the free first brick and one Damage Roll die per complete brick beyond it. | The rule measures the fall to the landing surface, not to table level, and exempts the first brick entirely. Both are easy to apply wrongly on an irregular drop without seeing where the measurement starts and ends. |

---

## Rules considered and rejected


- **CORE-010 (Cover)** — Binary rule (a component is hidden or it isn't, no partial cover). The nuance is conceptual ("no cover bonus exists"), not spatial; there is nothing to draw that the sentence doesn't already say.
- **MOVE-017 (Collision)** — "Models may not overlap" is a self-evident physical fact from any tabletop photo. Recorded explicitly because a collision diagram is the first thing a reader of `07-movement.md` reaches for; on review it does not meet the bar.
- **VEH-006 (Reverse Movement)** — Just states the same distance as forward movement applies in reverse; no new geometry to show.
- **VEH-009, VEH-010, VEH-011 (Track/Walker/Hover pivot)** — All three pivot around the model's centre, which is the intuitive case (a swivel, not a lever). Covered by the contrast panel in the VEH-008 image rather than three near-identical diagrams.
- **VEH-025 (Stranded), VEH-026 (Vehicle Falling)** — Both are direct consequences of the Terrain Threshold already illustrated (VEH-022 – VEH-024) and the fall mechanic already illustrated (INF-011); no independent geometric fact to add.
- **VEH-030 (What Counts Toward Height)** — Two of its three facts are checks read off the model: whether an element can move, and whether it is functional. This list already declines CBT-007 as "a binary construction check made directly on the model" and VEH-013 and CMP-008 as verified by looking at the build. Measuring a movable element in its highest position changes *when* the check is made, not what a reader has to picture, and the Gameplay-versus-Visual contrast the rule's table applies is drawn for GEO-005. The third, that an externally carried model counts, is a counting rule of the kind DEP-006 owns.
- **VEH-013 (Pilot), CMP-008 (Turrets)** — "A visible minifigure in an operating position" and "a mount that physically rotates" are easily verified by looking at the model; nothing in the text is hard to picture.
- **WPN-002 (Functional Muzzle), WPN-018 (Weapon Proportion)** — WPN-002 is a definition, and WPN-018 states a proportion as an inequality with valid/invalid dimension lists that read perfectly well as text. An image would add nothing to either.
- **WPN-007 (Muzzle Adjacency)** — Adjacency and overlap are visible in WPN-020's worked examples, and whether two muzzles overlap is a check made on the built weapon. It was specified for a while, on the grounds that a reader met a bare `██··` block with no legend; the block is gone and the grounds with it.
- **WPN-019 (Weapon Front Footprint)** — Covered by WPN-003's image, which outlines the footprint on the weapon front. It was specified for a while, because the rule carried three character grids of its own; those are gone and the grounds with them.
- **WPN-008 / CBT-006, CBT-007 (Weapon Systems, Multiple Targets)** — "Each visible weapon is its own weapon system" is a counting rule, not a spatial one.
- **DMG-006 (Internal Components)** — Introduces the "Armour → Pilot" concept that DMG-016's image already resolves mechanically; a separate diagram would repeat it.
- **CBT-007 (Multiple Targets)** — Whether a mount rotates is a binary construction check made directly on the model, not something prose obscures.
- **MEL-013 (Functional Striking End)** — Same footprint logic as a muzzle (WPN-020), the only difference being that round pieces aren't required; not enough of a distinct spatial fact to justify a second image.
- **TRN-003 (Cargo Capacity), TRN-010 (Closed Transport)** — Cargo Capacity counts Unit Bases of volume, and that volume is dimensioned in the CORE-001 image with the clearance half of the check drawn for TRN-019; Closed Transport's "impact continues toward internal passengers" is the same mechanism as DMG-016's image, not a new one.
- **TRN-020 (Interior Levels)** — The stacking is arithmetic on a height the CORE-001 image already dimensions: one Unit Base of clear height per level, plus a plate for each floor above the lowest. How many levels fit is then a comparison against the agreed Deployment Volume ceiling, which is a number the players chose rather than a geometry a picture can settle.
- **DEP-003, DEP-004 (Vehicle Footprint, Infantry)** — Both are direct multiplication/counting applications of the Unit Base's horizontal projection, already covered by the CORE-001 image. What DEP-003 occupies is that floor; height is checked separately against the agreed ceiling and needs no image of its own.
- **DEP-006 (Embarked Units)** — The waiver and its limit are counting rules: an embarked model costs no Deployment Volume, an externally carried one costs its own. Nothing about where such a model sits is hard to picture.
- **GEO-002, GEO-004 (Visual Geometry, Physical Checks)** — The structural-vs-decorative distinction and the "Visual Geometry still blocks sight" point are both carried by the GEO-005 image and its accompanying text; a second diagram would restate the same contrast. Of the physical checks GEO-004 lists, Cover is declined at CORE-010 above and Line of Sight is settled from the shooter's own viewpoint rather than from any diagram; access-opening clearance needs an image of its own, and it has one under `docs/05-construction-components.md` (CMP-018).
