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

### Rejecting a candidate

Rules considered and turned down go in the final section, each with the reason. That record is the point: without it, the same candidate gets re-proposed by whoever next reads the ruleset and notices the same thing.

### Reclassifying

If a rejected candidate is later accepted, or an accepted one dropped, **do not silently move it.** Leave it in the rejected list struck through, marked reclassified, with a line saying what changed — normally the criterion, not the rule. A reader should be able to see that the earlier judgement was superseded rather than mistaken.

## Naming convention

- For a numbered rule: `assets/images/<rule-id-lowercase>-<short-slug>.png`
  Example: `assets/images/wpn-020-muzzle-placement.png`
- For an unnumbered section: `assets/images/<doc-number>-<short-slug>.png`
  Example: `assets/images/07-terrain-thresholds.png`
- The slug is lowercase, hyphen-separated, 2-4 words, and describes the content shown, not the rule's title.

None of the files listed below exist yet. `assets/images/.gitkeep` holds the directory until they are added.

---

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

There is a fourth notation outside this document. `16-damage-system.md` writes a two-muzzle shotgun as `` `○ ○` `` in DMG-010 and DMG-016 — a hollow circle where WPN-020 uses a filled `●` for the same thing.

**That one is not an image job.** It appears inline, mid-sentence, twice, and an inline image would read worse than the text does. The fix is to write "a shotgun with two muzzles" in words and drop the glyph, which removes the fourth notation without adding anything. Recorded here because it surfaced from the same scan, and because someone tidying the weapon grids will otherwise leave it behind as the last inconsistent one. It needs its own change: `docs/16-damage-system.md` is the ruleset, so it needs a proposal.

## Coverage of the character grids

A full scan of `docs/` for block and shape glyphs (`█ ■ ● ○ · ▪ ▫ ░ ▒ □`) finds nine fenced grid blocks. All nine are in `10-weapons.md`, and all belong to the three rules listed in that section above — one in WPN-007, three in WPN-019, five in WPN-020. No other document represents LEGO geometry as characters, and there is no ASCII minifigure anywhere in the ruleset.

The remaining fenced blocks stay as they are. Formulas are equations and an image would be worse than the text. Directed graphs belong in Mermaid, which stays diffable, rather than in a raster image.

---

## docs/02-core-rules.md

| Rule | Filename | What it must show | Why text alone is not enough |
|---|---|---|---|
| CORE-001 | `assets/images/core-001-unit-base-volume.png` | Six panels. First, the derivation: a minifigure standing on its base beside a stack of four bricks on one plate — the plate at the bottom, mirroring the base — the two flush at the top and their studs aligned, with the minifigure's four bricks and the base's one plate dimensioned separately and the head stud marked as not counted. Second, the Unit Base as a volume, dimensioned 4 studs wide × 3 studs deep × 13 plate layers tall, with that same model inside it and the base plate drawn within the volume rather than below it. Then one panel per reading of that volume, each labelled: the horizontal projection, 4 × 3 studs; the volume itself, labelled as the reading transport capacity and interior space use; the vertical projection, 4 studs by 13 plate layers, taken across the 4-stud front and drawn against an opening a model passes through. Last, a "2 × 3 UB" footprint measuring 8 × 9 studs, beside a 6 × 12 rectangle marked wrong. | Four geometric facts here are carried by prose alone: that the height is the model plus the base it stands on rather than a chosen round number, that the unit encloses space rather than covering it, that the base plate is inside the volume rather than the floor under it, and that different rules read different projections of the same volume. The first panel is the argument for the figure and not an illustration of it — two stacks being the same height is the one claim text cannot make convincingly. The rule text itself flags the 8×9-vs-6×12 confusion as one readers get wrong. |
| CORE-002 | `assets/images/core-002-facing-orientation.png` | An infantry Unit Base with the 4-stud front edge marked, and the four directions (forward, rear, left, right) and firing arcs labelled relative to it. | Facing is the reference frame for movement, firing arcs and shield direction throughout the rest of the ruleset; a single labelled diagram fixes what "front," "rear," "left" and "right" mean before those other rules use them. |

## docs/05-construction-components.md

| Rule | Filename | What it must show | Why text alone is not enough |
|---|---|---|---|
| CMP-018 | `assets/images/cmp-018-clear-opening.png` | A doorway in a vehicle wall, twice. Both times the frame's nominal aperture is dimensioned in studs and plate layers, a hinged element hangs part-way across it, and the measurement that counts is drawn around that element rather than around the frame — labelled as the clear opening. In the first, the Unit Base's vertical projection fits that clear opening; in the second the same frame fails it, with only the hanging element differing between the two. | The frame is what a reader measures and the wrong thing to measure, and no wording of "clear rather than nominal" makes two identical frames visibly different sizes — a drawing of one doorway with two measurements does. It is also the only one of GEO-004's three physical checks that needs an image of its own: Cover is declined separately at CORE-010, and Line of Sight is whatever can physically be seen from where the shooter stands, which no drawing of one build settles. |

## docs/07-movement.md

| Rule | Filename | What it must show | Why text alone is not enough |
|---|---|---|---|
| MOVE-003 | `assets/images/move-003-axis-measurement.png` | A Unit Base measured from its leading edge in each direction: the front edge for forward movement (3-stud steps, MOVE-004), the corresponding side edge for lateral movement (4-stud steps, MOVE-005). | Forward movement steps in multiples of the base's 3-stud depth while side movement steps in multiples of its 4-stud width — two different axes of the same base, with two different step sizes. The rule works this out algebraically; a diagram shows it directly. |
| Terrain Movement (MOVE-009 – MOVE-011) | `assets/images/07-terrain-thresholds.png` | Three obstacle heights next to real LEGO bricks/plates: up to 3 plate layers (crossed freely), 4-6 (climbable for +1 AP), 7 or more (impassable without a slope, stair or ramp). | The three thresholds are defined purely in "plate layers," a unit few readers convert to bricks at a glance. Seeing the three bands next to actual brick heights removes the conversion step. |
| MOVE-016 | `assets/images/move-016-falling-measurement.png` | A unit falling from a height to "the first surface that physically supports it," with the drop marked in plate layers/bricks, showing the free first brick and one Damage Roll die per complete brick beyond it. | The rule measures the fall to the landing surface, not to table level, and exempts the first brick entirely. Both are easy to apply wrongly on an irregular drop without seeing where the measurement starts and ends. |

## docs/08-vehicles.md

| Rule | Filename | What it must show | Why text alone is not enough |
|---|---|---|---|
| VEH-003 | `assets/images/veh-003-length-axis.png` | A vehicle with an irregular or protruding build, with its "longest dimension" axis marked and decorative overhangs excluded from the measurement. | "Longest axis, decorative elements ignored" is simple to state and easy to misjudge on an asymmetric model; an annotated example resolves where the measurement legitimately starts and ends. |
| VEH-008 | `assets/images/veh-008-pivot-points.png` | A wheeled vehicle turning 90° around its rear axle, showing the wide arc the front corner sweeps, next to a tracked/walker/hover vehicle turning around its own centre. | "Pivot point is the rear axle" is one sentence, but a reader cannot picture how far the front of the vehicle swings, or how that differs from a centre-pivot turn (VEH-009 through VEH-011), without seeing both turns drawn. |
| VEH-022 | `assets/images/veh-022-axle-height.png` | A wheel with its axle height (half the wheel's diameter) marked as the Terrain Threshold, plus the fallback measurement (half the track-run height) for a tracked vehicle with no visible axle. | "Axle height" requires identifying the actual rotation point on the model, and the rule supplies a second, different fallback for tracks — both need to be shown against a real build to apply correctly. |
| VEH-023 | `assets/images/veh-023-knee-height.png` | A walker leg with its knee-joint height marked as the Terrain Threshold, plus the fallback (half the leg's standing height) when no distinct knee exists. | Where a "knee" sits on a player-built leg assembly varies model to model; the rule's own fallback shows the answer is meant to be read off the build, which only an image can standardise. |
| VEH-024 | `assets/images/veh-024-hover-assembly-height.png` | A hover vehicle's emitter/pylon/skirt assembly with its full height marked from the ground to the hull, including an enclosed skirt that reaches the ground and leaves no visible gap. | The rule explicitly warns that "measuring the assembly rather than the visible gap matters for enclosed builds" — the intuitive reading (measure the gap) is wrong, and only a picture can pre-empt that mistake. |
| VEH-027 | `assets/images/veh-027-ascent-coverage.png` | A slope/ramp fully covering a rise, resting on both the lower and upper surface, next to an invalid example that leaves a gap at the top or bottom. | The rule turns on whether the ramp "physically covers the entire rise" — a binary construction fact that is easy to get subtly wrong (a ramp that looks close enough but does not actually touch the upper surface). |
| VEH-028 | `assets/images/veh-028-two-height-bounds.png` | A Deployment Volume drawn as an open box, its floor dimensioned in Unit Bases and its ceiling marked at a height in Unit Bases. Inside it, three vehicles measured from the surface they rest on to the top of their Gameplay Geometry, each with its own footprint-derived limit drawn as a second, lower or higher line above its base: a wide hull stopped by the ceiling with its footprint limit above it, a narrow hull stopped by its footprint limit with the ceiling above it, and a walker whose legs and hull together cross its footprint limit, drawn as failing. Mark each measurement's start at the resting surface, and show a flag on the failing walker excluded from the measurement. Beside them, a non-rectangular footprint over a stud grid with the smallest enclosing rectangle of whole Unit Bases drawn around it and its narrowest side dimensioned in studs. | Two bounds apply at once and either can be the one that stops a model, which no single dimension line shows; a reader who sees only the lower of the two concludes the other does not exist. Two further things go wrong without a picture: that locomotion is free, and which rectangle the narrowest side is read from when the outline is not one. |
| VEH-029 | `assets/images/veh-029-resting-surface-datum.png` | A long-legged walker measured from the surface it rests on to the top of its Gameplay Geometry, with the leg assembly shaded as included. The same walker repeated on a slope, and again standing inside a carrier vehicle — each time measured against the same total, with the slope and the carrier's floor marked as changing nothing. | Where the count begins is the whole rule, and everything the model stands up on is part of its height. The repeated panels carry the half prose argues hardest, that terrain and being carried never re-measure a model whose legality was settled at the bench. |

## docs/09-transport.md

| Rule | Filename | What it must show | Why text alone is not enough |
|---|---|---|---|
| TRN-019 | `assets/images/trn-019-clearance-above-bench.png` | A closed compartment in cross-section, three times, with every clear height dimensioned in plate layers. First, a bare floor whose clear height to the roof is exactly one Unit Base — `02-core-rules.md` (CORE-001) gives that height in plate layers — holding one Unit Base. Second, the same compartment with a bench 3 plate layers high on its floor, the measurement starting at the bench's top surface and the Unit Base of clear height it needs marked above that, running past the roof and labelled as failing. Third, the same compartment with a pipe crossing below the roof, the clear height measured under the pipe rather than to the ceiling. | Where the measurement starts is the whole rule, and it runs against intuition twice: a seat raises the roof a compartment needs instead of reducing the space its occupant takes, and an element crossing the ceiling costs clearance exactly as the ceiling does. Both are got wrong by measuring the compartment, which is what a reader without a cross-section measures. Neither neighbouring image carries a datum that moves: CMP-018's doorway measures a fixed aperture, and VEH-029 measures from the surface a vehicle rests on, which a bench inside it does not raise. |

## docs/10-weapons.md

| Rule | Filename | What it must show | Why text alone is not enough |
|---|---|---|---|
| WPN-003 | `assets/images/wpn-003-length-axis-front-face.png` | A weapon body with its firing axis drawn perpendicular through the Weapon Front, and the Weapon Front Footprint (WPN-019) outlined on that face, distinguished from the other five faces of the body. | Weapon Length is defined via an axis "perpendicular to the Weapon Front," and the Weapon Front is itself "the only face from which the weapon may fire" — two spatial definitions that depend on each other and are easy to reverse without a 3D view. |
| WPN-007 | `assets/images/wpn-007-muzzle-adjacency.png` | A Weapon Front Footprint holding two muzzles that share an edge, marked valid, beside the same footprint with two muzzles overlapping, marked invalid. Unused footprint cells visibly distinct from occupied ones. | The rule's `██··` block is the whole explanation and carries no legend, so a reader must infer that `█` is a muzzle and `·` is unused footprint from a later rule that uses the same characters for something narrower. The image also has to show that adjacency is allowed and only overlap is not — a distinction four characters cannot carry. |
| WPN-019 | `assets/images/wpn-019-front-footprint-sizes.png` | The Weapon Front Footprint at Widths 1, 2 and 4 — a square of side Weapon Width — shown against the weapon body so the relationship between body width and available muzzle space is visible. | The rule shows three character squares with no indication of scale or of how they sit on the weapon. The footprint is the space every muzzle competes for, so getting its size wrong invalidates every weapon built from it. |
| WPN-020 | `assets/images/wpn-020-muzzle-placement.png` | Five panels: the unpartitioned Weapon Front Footprint the rule starts from, then that same footprint partitioned as twin barrel, quad barrel, heavy cannon and hybrid, each labelled with the Attack Dice and Impact Strengths it produces. | The rule's own ASCII diagrams compress a genuinely spatial muzzle layout into a flat character grid. A real image showing the same footprint yielding several distinct, valid weapons makes "no fixed weapon profile" concrete. |

## docs/15-geometry-layers.md

| Rule | Filename | What it must show | Why text alone is not enough |
|---|---|---|---|
| GEO-005 | `assets/images/geo-005-functional-equivalence.png` | Two visually distinct weapons — a bare plate with round studs, and a fully greebled brick-built weapon — built to the same Length, Width and muzzle layout, both producing identical Range, Attack Dice and Impact Strength. | This is the concrete demonstration that Gameplay Geometry and Visual Geometry are separate. The claim — two completely different-looking models playing identically — is far more convincing seen side by side than described. |

## docs/16-damage-system.md

| Rule | Filename | What it must show | Why text alone is not enough |
|---|---|---|---|
| DMG-003 | `assets/images/dmg-003-resistance-cross-section.png` | A shield built from bricks (Resistance 3) and a similarly-sized shield built from four stacked plates (Resistance 4), both with the Impact's direction of travel marked, showing Resistance as the layer count crossed, not the external silhouette. | The rule's own text notes that two builds of "similar external bulk" resolve to different Resistance values — the whole point is that the model's outside doesn't tell you the answer. Only a cross-section view can show that. |
| DMG-013 | `assets/images/dmg-013-composite-targeting.png` | A vehicle (e.g. a jeep) with each independent component — chassis, driver, cannon, four wheels — outlined separately as its own targetable component. | Readers coming from other wargames default to treating "the vehicle" as one target. Seeing a single model broken into several independently-resolving components is the fastest way to unlearn that assumption. |
| DMG-017 | `assets/images/dmg-017-penetration.png` | The worked Heavy Cannon vs. Shield example: an Impact of Strength 6 crossing a Shield of Resistance 3, continuing with Remaining Strength 3 toward a Minifig of Resistance 3 positioned behind it. | Penetration is defined algebraically (`Remaining Strength = Current Strength − Component Resistance`) and depends on components being physically arranged one behind another along the Impact's path — immediate in a side-view diagram, laborious to reconstruct from the formula alone. |

---

## Total and rejected candidates

**23 images** specified, across 8 of the 15 ruleset documents (`02-core-rules.md`, `05-construction-components.md`, `07-movement.md`, `08-vehicles.md`, `09-transport.md`, `10-weapons.md`, `15-geometry-layers.md`, `16-damage-system.md`).

The remaining 7 documents (`01-foundations.md`, `03-game-flow.md`, `04-construction-standard.md`, `06-deployment.md`, `11-combat.md`, `12-melee.md`, `14-glossary.md`) need no images of their own: they either restate rules already illustrated above, or are procedural/definitional throughout.

Rules considered and rejected, with reasons:

- **CORE-010 (Cover)** — Binary rule (a component is hidden or it isn't, no partial cover). The nuance is conceptual ("no cover bonus exists"), not spatial; there is nothing to draw that the sentence doesn't already say.
- **MOVE-017 (Collision)** — "Models may not overlap" is a self-evident physical fact from any tabletop photo. Recorded explicitly because a collision diagram is the first thing a reader of `07-movement.md` reaches for; on review it does not meet the bar.
- **VEH-006 (Reverse Movement)** — Just states the same distance as forward movement applies in reverse; no new geometry to show.
- **VEH-009, VEH-010, VEH-011 (Track/Walker/Hover pivot)** — All three pivot around the model's centre, which is the intuitive case (a swivel, not a lever). Covered by the contrast panel in the VEH-008 image rather than three near-identical diagrams.
- **VEH-025 (Stranded), VEH-026 (Vehicle Falling)** — Both are direct consequences of the Terrain Threshold already illustrated (VEH-022 – VEH-024) and the fall mechanic already illustrated (MOVE-016); no independent geometric fact to add.
- **VEH-030 (What Counts Toward Height)** — Two of its three facts are checks read off the model: whether an element can move, and whether it is functional. This list already declines DMG-018 as "a binary construction check made directly on the model" and VEH-013 and CMP-008 as verified by looking at the build. Measuring a movable element in its highest position changes *when* the check is made, not what a reader has to picture, and the Gameplay-versus-Visual contrast the rule's table applies is drawn for GEO-005. The third, that an externally carried model counts, is a counting rule of the kind DEP-006 owns.
- **VEH-013 (Pilot), CMP-008 (Turrets)** — "A visible minifigure in an operating position" and "a mount that physically rotates" are easily verified by looking at the model; nothing in the text is hard to picture.
- **WPN-002 (Functional Muzzle), WPN-018 (Weapon Proportion)** — Neither displays a character grid. WPN-002 is a definition, and WPN-018 states a proportion as an inequality with valid/invalid dimension lists that read perfectly well as text. An image would add nothing to either.
- ~~**WPN-007 (Muzzle Adjacency)**~~ — **Reclassified; now specified above.** Originally folded into the WPN-020 image on the grounds that adjacency is visible in those worked examples. That was correct under the original criterion, which asked whether the *concept* needed illustrating. It was reclassified when the criterion widened: a folded image inside WPN-020 does nothing for a reader of WPN-007, who still meets a bare `██··` and no legend.
- ~~**WPN-019 (Weapon Front Footprint)**~~ — **Reclassified; now specified above.** Originally covered by WPN-003's image, which outlines the footprint on the weapon front. Same reasoning as WPN-007: WPN-019 has three character grids of its own, and an illustration living in another rule does not replace them.
- **WPN-008 / CBT-006, CBT-007 (Weapon Systems, Multiple Targets)** — "Each visible weapon is its own weapon system" is a counting rule, not a spatial one.
- **DMG-007 (Internal Components)** — Introduces the "Armour → Pilot" concept that DMG-017's image already resolves mechanically; a separate diagram would repeat it.
- **DMG-018 (Weapon Distribution)** — Whether a mount rotates is a binary construction check made directly on the model, not something prose obscures.
- **MEL-013 (Functional Striking End)** — Same footprint logic as a muzzle (WPN-020), the only difference being that round pieces aren't required; not enough of a distinct spatial fact to justify a second image.
- **TRN-003 (Cargo Capacity), TRN-010 (Closed Transport)** — Cargo Capacity counts Unit Bases of volume, and that volume is dimensioned in the CORE-001 image with the clearance half of the check drawn for TRN-019; Closed Transport's "impact continues toward internal passengers" is the same mechanism as DMG-017's image, not a new one.
- **TRN-020 (Interior Levels)** — The stacking is arithmetic on a height the CORE-001 image already dimensions: one Unit Base of clear height per level, plus a plate for each floor above the lowest. How many levels fit is then a comparison against whichever of VEH-028's two bounds is lower, both of which the VEH-028 image draws, so nothing is left for a picture to settle.
- **DEP-003, DEP-004 (Vehicle Footprint, Infantry)** — Both are direct multiplication/counting applications of the Unit Base's horizontal projection, already covered by the CORE-001 image. What DEP-003 charges is that floor; the two height bounds it feeds one of are drawn in VEH-028's image, not in a second one here.
- **DEP-006 (Embarked Units)** — The waiver and its limit are counting rules: an embarked model costs no Deployment Volume, an externally carried one costs its own. Nothing about where such a model sits is hard to picture.
- **GEO-002, GEO-004 (Visual Geometry, Physical Checks)** — The structural-vs-decorative distinction and the "Visual Geometry still blocks sight" point are both carried by the GEO-005 image and its accompanying text; a second diagram would restate the same contrast. Of the three physical checks GEO-004 lists, Cover is declined at CORE-010 above and Line of Sight is settled from the shooter's own viewpoint rather than from any diagram; only access-opening clearance needs an image of its own, and it has one under `docs/05-construction-components.md` (CMP-018).
