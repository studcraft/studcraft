# Example Images Index

This file indexes the example images the StudCraft ruleset needs. It does not contain images — it specifies which ones are needed, what each must show, and why the rule cannot be fully understood from prose alone, so that a later process can create and insert them.

Entries are selective by design. A rule only appears here if the rule *is* a spatial or geometric fact — something a reader genuinely cannot picture correctly from text — not because an image would be a nice illustration. Purely procedural rules (action costs, turn order) and purely definitional rules are left out even when they are important, because an image adds nothing to them. The final section records the rules that were considered and rejected, and why, so they are not re-proposed without cause.

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
| CORE-001 | `assets/images/core-001-unit-base-grid.png` | The Unit Base as a 4 × 3 stud LEGO plate, dimensioned, plus a worked example of a "2 × 3 UB" footprint expanding to 8 × 9 studs (not 6 × 12). | CORE-001 states the width/depth multiplication rule in words only, and the rule text itself flags the 8×9-vs-6×12 confusion as something readers get wrong. A dimensioned diagram removes the arithmetic. |
| CORE-002 | `assets/images/core-002-facing-orientation.png` | An infantry Unit Base with the 4-stud front edge marked, and the four directions (forward, rear, left, right) and firing arcs labelled relative to it. | Facing is the reference frame for movement, firing arcs and shield direction throughout the rest of the ruleset; a single labelled diagram fixes what "front," "rear," "left" and "right" mean before those other rules use them. |

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

**19 images** specified, across 6 of the 15 ruleset documents (`02-core-rules.md`, `07-movement.md`, `08-vehicles.md`, `10-weapons.md`, `15-geometry-layers.md`, `16-damage-system.md`).

The remaining 9 documents (`01-foundations.md`, `03-game-flow.md`, `04-construction-standard.md`, `05-construction-components.md`, `06-deployment.md`, `09-transport.md`, `11-combat.md`, `12-melee.md`, `14-glossary.md`) need no images of their own: they either restate rules already illustrated above, or are procedural/definitional throughout.

Rules considered and rejected, with reasons:

- **CORE-010 (Cover)** — Binary rule (a component is hidden or it isn't, no partial cover). The nuance is conceptual ("no cover bonus exists"), not spatial; there is nothing to draw that the sentence doesn't already say.
- **MOVE-017 (Collision)** — "Models may not overlap" is a self-evident physical fact from any tabletop photo. Included here explicitly because it maps to this document's own naming-convention example (`07-collision.png`); on review it does not meet the bar.
- **VEH-006 (Reverse Movement)** — Just states the same distance as forward movement applies in reverse; no new geometry to show.
- **VEH-009, VEH-010, VEH-011 (Track/Walker/Hover pivot)** — All three pivot around the model's centre, which is the intuitive case (a swivel, not a lever). Covered by the contrast panel in the VEH-008 image rather than three near-identical diagrams.
- **VEH-025 (Stranded), VEH-026 (Vehicle Falling)** — Both are direct consequences of the Terrain Threshold already illustrated (VEH-022 – VEH-024) and the fall mechanic already illustrated (MOVE-016); no independent geometric fact to add.
- **CMP-002 (Pilot), CMP-008 (Turrets)** — "A visible minifigure in an operating position" and "a mount that physically rotates" are easily verified by looking at the model; nothing in the text is hard to picture.
- **WPN-002 (Functional Muzzle), WPN-018 (Weapon Proportion)** — Neither displays a character grid. WPN-002 is a definition, and WPN-018 states a proportion as an inequality with valid/invalid dimension lists that read perfectly well as text. An image would add nothing to either.
- ~~**WPN-007 (Muzzle Adjacency)**~~ — **Reclassified; now specified above.** Originally folded into the WPN-020 image on the grounds that adjacency is visible in those worked examples. That was correct under the original criterion, which asked whether the *concept* needed illustrating. It was reclassified when the criterion widened: a folded image inside WPN-020 does nothing for a reader of WPN-007, who still meets a bare `██··` and no legend.
- ~~**WPN-019 (Weapon Front Footprint)**~~ — **Reclassified; now specified above.** Originally covered by WPN-003's image, which outlines the footprint on the weapon front. Same reasoning as WPN-007: WPN-019 has three character grids of its own, and an illustration living in another rule does not replace them.
- **WPN-008 / CBT-006, CBT-007 (Weapon Systems, Multiple Targets)** — "Each visible weapon is its own weapon system" is a counting rule, not a spatial one.
- **DMG-007 (Internal Components)** — Introduces the "Armour → Pilot" concept that DMG-017's image already resolves mechanically; a separate diagram would repeat it.
- **DMG-018 (Weapon Distribution)** — Whether a mount rotates is a binary construction check made directly on the model, not something prose obscures.
- **MEL-013 (Functional Striking End)** — Same footprint logic as a muzzle (WPN-020), the only difference being that round pieces aren't required; not enough of a distinct spatial fact to justify a second image.
- **TRN-003 (Cargo Capacity), TRN-010 (Closed Transport)** — Cargo Capacity is arithmetic on the Unit Base grid already shown for CORE-001; Closed Transport's "impact continues toward internal passengers" is the same mechanism as DMG-017's image, not a new one.
- **DEP-003, DEP-004 (Vehicle Footprint, Infantry)** — Both are direct multiplication/counting applications of the Unit Base grid already covered by the CORE-001 image.
- **GEO-002, GEO-004 (Visual Geometry, Physical Checks)** — The structural-vs-decorative distinction and the "Visual Geometry still blocks sight" point are both carried by the GEO-005 image and its accompanying text; a second diagram would restate the same contrast.
