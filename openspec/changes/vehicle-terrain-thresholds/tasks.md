## 0. Setup

- [ ] 0.1 Work on branch `vehicle-terrain-thresholds` (`openspec/config.yaml` requires one branch per proposal).

### How to read the replacement blocks

Replacement text is shown as a markdown blockquote so it is visually separable from the instructions. **The `> ` prefix is not part of the text.** Strip it from every line before writing into the document.

Where a block contains a `#` heading, that heading is part of the text and must be written as a real heading, not left inside a quote.

### New rule headings must match the linter's format

`scripts/lint_ruleset.py` parses rule headings with `^#{1,2} ([A-Z]{2,6})-(\d{3}) — `. Every new heading must use a level-1 `#`, a three-digit number, and a real **em dash** (`—`, U+2014) surrounded by single spaces — not a hyphen, not an en dash. Copy the punctuation from an existing heading such as `# VEH-019 — Immobilized Vehicles` if in doubt.

Rule IDs must be strictly increasing within a document, so `VEH-021` … `VEH-027` go **after** `VEH-020`, at the end of the rules, before the `# Summary` section.

### Scope

Four documents change: `docs/08-vehicles.md` (seven new rules), `docs/07-movement.md` (one paragraph narrowed), `docs/05-construction-components.md` (four cross-references), plus `docs/14-glossary.md` (two entries). No existing rule ID is renumbered, and no numeric value anywhere changes.

### Defect coverage

| Item | Task |
|---|---|
| General threshold principle | 1.1 |
| Wheeled and tracked threshold | 1.2 |
| Walker threshold | 1.3 |
| Hover threshold and drop immunity | 1.4 |
| Stranded reuses VEH-019 | 1.5 |
| Vehicle falling damage | 1.6 |
| Vehicle ascent: slopes and ramps only | 1.7 |
| `07-movement.md` deferral replaced by a pointer | 2.1 |
| Component cross-references | 3.1 – 3.4 |
| Glossary entries | 4.1, 4.2 |

---

## 1. `docs/08-vehicles.md` — seven new rules

Insert all seven **after** `VEH-020 — Construction Priority` and its closing `---`, and **before** the `# Summary` heading. Keep them in the order given; the linter requires ascending IDs.

- [ ] 1.1 Insert:

> # VEH-021 — Terrain Threshold
>
> Every vehicle has a single **Terrain Threshold**, read from its locomotion system (VEH-012) rather than assigned as a statistic. It is measured in plate layers, the same unit obstacles and Resistance use (`16-damage-system.md`, DMG-003): a plate counts as 1 and a standard brick as 3.
>
> The threshold governs two things:
>
> - An obstacle **taller** than the threshold blocks movement. The vehicle cannot cross it and must go around, or use a legal access point (`07-movement.md`, MOVE-011).
> - A drop **deeper** than the threshold strands the vehicle (VEH-025).
>
> An obstacle or drop equal to the threshold is crossed normally. Each locomotion type reads its own threshold: VEH-022 for wheels and tracks, VEH-023 for walkers, VEH-024 for hover.
>
> A drop is not a fall. This rule covers driving into a depression, ditch or trench; a vehicle that leaves a height entirely is falling, and VEH-026 covers that. Both measure against this same threshold.

- [ ] 1.2 Insert:

> # VEH-022 — Wheeled and Tracked Thresholds
>
> For a wheeled or tracked vehicle, the Terrain Threshold is **axle height**: the height of the wheel or road wheel's axle above the ground.
>
> On a LEGO model this is the wheel's radius, so the threshold is half the wheel's own diameter — a wheel cannot climb a step taller than its own centre. Where a tracked build shows no visible axle, use half the height of the track run instead.
>
> Wheeled and tracked vehicles are stranded by drops deeper than this threshold (VEH-025).

- [ ] 1.3 Insert:

> # VEH-023 — Walker Thresholds
>
> For a walker, the Terrain Threshold is **knee height**: the height of the leg's knee joint above the ground, as built (`05-construction-components.md`, CMP-006).
>
> A walker steps over obstacles below its knee and steps down into depressions below its knee without difficulty. Where a leg has no distinct knee joint, use half the leg's standing height.
>
> Walkers are stranded by drops deeper than this threshold (VEH-025).

- [ ] 1.4 Insert:

> # VEH-024 — Hover Thresholds
>
> For a hover vehicle, the Terrain Threshold is the height of the **hover assembly** — the emitters, pylons or skirt that hold the hull clear of the ground (`05-construction-components.md`, CMP-005) — measured in plate layers from the ground to where that assembly meets the hull.
>
> This is the hover equivalent of a wheel's axle. In every locomotion type you measure the part that carries the vehicle, never the body it carries: the wheel to its axle (VEH-022), the leg to its knee (VEH-023), the hover assembly to its full height.
>
> Measuring the assembly rather than the visible gap matters for enclosed builds. A skirt that reaches the ground leaves no gap to see, but its own height is still the threshold.
>
> A hover model built with its hull flat on the ground has no assembly to measure and a Terrain Threshold of 0 — every obstacle blocks it. Nothing forbids that build; it simply cannot cross anything, which is the model telling you it is not finished. `CMP-005` already requires hover components to be visually distinguishable, and this is why: the assembly is the vehicle's terrain capability, so it has to be visible to be measured.
>
> A taller assembly clears more terrain at the cost of a taller silhouette, which is easier to see and therefore to shoot (`02-core-rules.md`, CORE-008) — the same trade a walker makes with long legs.
>
> Hover thresholds are usually the lowest of any locomotion type: a hover vehicle is stopped by walls a wheeled vehicle drives over. In exchange it is **never stranded by a drop** (VEH-025) — it passes over depressions instead of entering them, and their depth is irrelevant.
>
> That immunity has one limit: a hover vehicle cannot cross a gap wider than its own footprint (VEH-001). There must be a surface beneath it to hover above.
>
> Hover emitters are components like any other. If the assembly is destroyed the hull settles, the Terrain Threshold becomes 0, and the vehicle can still move across flat ground but is blocked by everything else.

- [ ] 1.5 Insert:

> # VEH-025 — Stranded Vehicles
>
> A vehicle that enters a drop deeper than its Terrain Threshold (VEH-021) becomes **stranded** and is Immobilized, resolved exactly as VEH-019 already defines: it remains on the battlefield and may continue operating any remaining functional systems.
>
> Stranded introduces no new state and no marker — the vehicle's position in the depression is the physical representation (`02-core-rules.md`, CORE-016).
>
> Freeing a stranded vehicle is not yet defined, in the same way VEH-013 leaves crew replacement to future rules.
>
> Hover vehicles cannot be stranded (VEH-024).

- [ ] 1.6 Insert:

> # VEH-026 — Vehicle Falling
>
> A vehicle that leaves a height and comes down under gravity — rather than descending a slope or ramp (VEH-027) — falls. Measure the fall in plate layers, from the surface it left to the surface it lands on.
>
> A fall no deeper than the vehicle's Terrain Threshold (VEH-021) causes no damage. The vehicle has dropped a kerb, not fallen.
>
> Beyond that, roll one D6 for every complete brick (3 plate layers) fallen **past the threshold**. Each die is an independent Damage Roll (`16-damage-system.md`, DMG-015), resolved exactly as infantry falling is (`07-movement.md`, MOVE-016): a result of 4, 5 or 6 means nothing happens, and a result of 1, 2 or 3 advances one component by one state.
>
> Every failed die is applied to a component that physically touches the ground when the vehicle lands — a wheel, a track, or a foot. The controlling player chooses which. Failures beyond the number of such components are lost: a vehicle whose locomotion is already destroyed is Immobilized (VEH-019) and cannot be immobilized twice.
>
> **Crew and passengers are never harmed by a vehicle's fall.** This is a deliberate simplification rather than an oversight — the case is rare, and the consequence below is the real cost.
>
> Hover vehicles take no falling damage. They descend under power rather than falling, consistent with their immunity to being stranded (VEH-024).
>
> A vehicle at the bottom of a drop may be a trap. Infantry inside it disembark normally (`09-transport.md`, TRN-006), but then face the drop's walls as ordinary terrain: 7 or more plate layers requires a slope, stair or ramp (`07-movement.md`, MOVE-011, MOVE-014). Driving into a ravine can strand a squad as effectively as it strands the vehicle.

- [ ] 1.7 Insert:

> # VEH-027 — Vehicle Ascent
>
> A vehicle crosses any rise no greater than its Terrain Threshold (VEH-021) by driving over it, whatever it is built from.
>
> To reach a height **greater** than its Terrain Threshold, a vehicle needs a slope or a ramp that physically covers the entire rise, resting on both the lower and the upper surface. The angle does not matter and is never measured: LEGO slope elements (`04-construction-standard.md`, SCS-011) and a lowered ramp (SCS-008) bound it by their own construction.
>
> If no slope or ramp covers the full rise, the height is impassable to that vehicle. It must go around.
>
> **Stairs are never a legal ascent for a vehicle**, however shallow each step is. Infantry climb stairs (`07-movement.md`, MOVE-013); vehicles do not. What matters is the total rise, not the individual steps — a staircase is one obstacle, not a series of small ones.
>
> A vehicle that descends a slope or ramp covering the full drop is driving, not falling, and takes no falling damage (VEH-026). A vehicle that leaves a height by any other route is falling.
>
> This needs no separate walker rule. A walker whose knee clears the whole rise simply crosses it under VEH-021 — a tall enough walker steps over a flight of stairs the same way it steps over a wall.

- [ ] 1.8 Confirm the seven rules sit between `VEH-020`'s closing `---` and the `# Summary` heading, each separated by its own `---`, and that `# Summary` is unchanged.

---

## 2. `docs/07-movement.md` — replace the deferral

The Vehicle Movement section says vehicle terrain is entirely undefined. After this change none of it is: VEH-021 through VEH-027 cover obstacles, drops, falling, and ascent. The deferral note is replaced by a pointer rather than kept as a narrowed gap.

- [ ] 2.1 Replace the sentence beginning "Vehicle-specific rules are described in `08-vehicles.md`." and everything after it in that paragraph — through "...if the LEGO model can answer the question, the model decides." — with:

> Vehicle-specific rules are described in `08-vehicles.md`, including terrain. The Terrain Threshold rules (VEH-021 through VEH-024) give each locomotion type its own limit, read from the model; VEH-025 covers being stranded, VEH-026 falling, and VEH-027 ascent.
>
> Vehicles and infantry differ most at stairs: infantry climb them (MOVE-013), vehicles never do (VEH-027).

- [ ] 2.2 `MOVE-016`'s closing line currently reads "This rule covers infantry only; vehicle falling is not yet defined (`07-movement.md`, Vehicle Movement)." Vehicle falling is now defined, so replace the whole line with:

> This rule covers infantry only. Vehicle falling is defined separately in `08-vehicles.md` (VEH-026), which scales from each vehicle's own Terrain Threshold rather than from a fixed first brick.

**If PR #33 (`movement-audit-repairs`) has already landed**, that line will instead end "— see the Vehicle Movement section below". Replace it with the same text either way; match on "This rule covers infantry only" rather than on the citation that follows it, which differs between the two states.

---

## 3. `docs/05-construction-components.md` — cross-references

Each component rule gains one pointer, matching the style `CMP-004` already uses for `VEH-009`. Add only the sentence shown; change nothing else in these rules.

- [ ] 3.1 `CMP-003` (Wheels): replace the line "Movement is resolved using the Vehicle Movement Rules." with:

> Movement is resolved using the Vehicle Movement Rules. Terrain behaviour follows `08-vehicles.md` (VEH-022) — a wheel's axle height is its Terrain Threshold.

- [ ] 3.2 `CMP-004` (Tracks): replace the line "Pivot behavior follows `08-vehicles.md` (VEH-009)." with:

> Pivot behavior follows `08-vehicles.md` (VEH-009), and terrain behaviour (VEH-022).

- [ ] 3.3 `CMP-005` (Hover System): replace the line "Hover vehicles ignore wheel requirements. Pivot and movement behavior follows `08-vehicles.md` (VEH-011)." with:

> Hover vehicles ignore wheel requirements. Pivot and movement behavior follows `08-vehicles.md` (VEH-011), and terrain behaviour (VEH-024) — the height of the hover assembly is the vehicle's Terrain Threshold, which is why these components must be visible.

- [ ] 3.4 `CMP-006` (Walkers): replace the line "Pivot behavior follows `08-vehicles.md` (VEH-010)." with:

> Pivot behavior follows `08-vehicles.md` (VEH-010), and terrain behaviour (VEH-023) — a walker's knee height is its Terrain Threshold.

---

## 4. `docs/14-glossary.md` — two entries

Insert both in the same style as the surrounding entries: a `## ` heading, the definition, then a `---` separator. Place them anywhere sensible among the existing terms; the glossary is not alphabetised.

- [ ] 4.1 Add:

> ## Terrain Threshold
>
> The height a vehicle can cross or descend without being blocked or stranded, read from its locomotion rather than assigned: axle height for wheels and tracks, knee height for walkers, hover assembly height for hover. In every case you measure the part that carries the vehicle, not the body it carries. Measured in plate layers. See `08-vehicles.md` (VEH-021 through VEH-024).

- [ ] 4.2 Add:

> ## Stranded
>
> A vehicle that has entered a drop deeper than its Terrain Threshold. A stranded vehicle is Immobilized (`08-vehicles.md`, VEH-019, VEH-025) and keeps operating its remaining systems. Hover vehicles cannot be stranded.

---

## 5. Verify

- [ ] 5.1 Run `python3 scripts/lint_ruleset.py`; confirm no structural issues. This checks the new headings' em dashes, the ascending IDs, and that every `(VEH-0NN)` cross-reference resolves.
- [ ] 5.2 Run `grep -n "^# VEH-" docs/08-vehicles.md` and confirm `VEH-001` through `VEH-027` appear once each, in ascending order, with no gaps.
- [ ] 5.3 Confirm no existing rule ID was renumbered and no existing rule was deleted — `VEH-021` … `VEH-027` are purely additive.
- [ ] 5.4 Run `git diff --stat main...HEAD` and confirm exactly these paths changed: `docs/08-vehicles.md`, `docs/07-movement.md`, `docs/05-construction-components.md`, `docs/14-glossary.md`, and the four new files under `openspec/changes/vehicle-terrain-thresholds/`.
- [ ] 5.5 Run `grep -c "Terrain Threshold" docs/08-vehicles.md` and confirm at least 7 hits — the term appears in every one of the five new rules. Separately confirm one hit in `docs/14-glossary.md`.
- [ ] 5.6 Confirm `docs/07-movement.md` no longer claims any part of vehicle terrain is undefined. This change closes the whole declared gap — obstacles, drops, falling and ascent — so the deferral paragraph becomes a pointer, not a narrowed caveat.
- [ ] 5.7 Confirm no numeric value changed anywhere: this change adds thresholds that are *measured*, and assigns no number to any vehicle.
- [ ] 5.8 Run `git diff main...HEAD -- docs/ | grep -E "^-" | grep -v "^---"` and confirm every removed line is one of the four cross-reference lines replaced in section 3, or the Vehicle Movement paragraph replaced in 2.1. Nothing else should be deleted.
