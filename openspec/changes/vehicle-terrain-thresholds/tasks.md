## 0. Setup

- [ ] 0.1 Work on branch `vehicle-terrain-thresholds` (`openspec/config.yaml` requires one branch per proposal).

### How to read the replacement blocks

Replacement text is shown as a markdown blockquote so it is visually separable from the instructions. **The `> ` prefix is not part of the text.** Strip it from every line before writing into the document.

Where a block contains a `#` heading, that heading is part of the text and must be written as a real heading, not left inside a quote.

### New rule headings must match the linter's format

`scripts/lint_ruleset.py` parses rule headings with `^#{1,2} ([A-Z]{2,6})-(\d{3}) — `. Every new heading must use a level-1 `#`, a three-digit number, and a real **em dash** (`—`, U+2014) surrounded by single spaces — not a hyphen, not an en dash. Copy the punctuation from an existing heading such as `# VEH-019 — Immobilized Vehicles` if in doubt.

Rule IDs must be strictly increasing within a document, so `VEH-021` … `VEH-025` go **after** `VEH-020`, at the end of the rules, before the `# Summary` section.

### Scope

Three documents change: `docs/08-vehicles.md` (five new rules), `docs/07-movement.md` (one paragraph narrowed), `docs/05-construction-components.md` (four cross-references), plus `docs/14-glossary.md` (two entries). No existing rule ID is renumbered, and no numeric value anywhere changes.

### Defect coverage

| Item | Task |
|---|---|
| General threshold principle | 1.1 |
| Wheeled and tracked threshold | 1.2 |
| Walker threshold | 1.3 |
| Hover threshold and drop immunity | 1.4 |
| Stranded reuses VEH-019 | 1.5 |
| `07-movement.md` deferral narrowed | 2.1 |
| Component cross-references | 3.1 – 3.4 |
| Glossary entries | 4.1, 4.2 |

---

## 1. `docs/08-vehicles.md` — five new rules

Insert all five **after** `VEH-020 — Construction Priority` and its closing `---`, and **before** the `# Summary` heading. Keep them in the order given; the linter requires ascending IDs.

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
> A drop is not a fall. This rule covers driving into a depression, ditch or trench. Vehicle falling damage — a vehicle leaving a height entirely — is not yet defined (`07-movement.md`, MOVE-016 covers infantry only).

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
> For a hover vehicle, the Terrain Threshold is **ground clearance**: the gap between the underside of the hull and the ground, as built (`05-construction-components.md`, CMP-005).
>
> This is usually the lowest threshold of any locomotion type — a hover vehicle is stopped by walls that a wheeled vehicle drives over.
>
> In exchange, a hover vehicle is **never stranded by a drop** (VEH-025). It passes over depressions instead of entering them, and its ground clearance is irrelevant to how deep they are.
>
> This immunity has one limit: a hover vehicle cannot cross a gap wider than its own footprint (VEH-001). There must be a surface beneath it to hover above.

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

- [ ] 1.6 Confirm the five rules sit between `VEH-020`'s closing `---` and the `# Summary` heading, each separated by its own `---`, and that `# Summary` is unchanged.

---

## 2. `docs/07-movement.md` — narrow the deferral

The Vehicle Movement section currently says vehicle terrain is entirely undefined. Obstacles and drops now are; slopes, stairs, vertical access and falling still are not. The note must not imply the whole gap closed.

- [ ] 2.1 Replace the sentence beginning "Vehicle-specific rules are described in `08-vehicles.md`." and everything after it in that paragraph — through "...if the LEGO model can answer the question, the model decides." — with:

> Vehicle-specific rules are described in `08-vehicles.md`. Obstacles and drops are defined there by the Terrain Threshold rules (VEH-021 through VEH-025), which give each locomotion type its own limit read from the model.
>
> Slopes, stairs, vertical access and falling damage for vehicles are still not defined — `08-vehicles.md` has no equivalent to MOVE-012, MOVE-013, MOVE-014 or MOVE-016. Until dedicated rules exist, resolve those questions using the same Physical Priority principle infantry uses: if the LEGO model can answer the question, the model decides.

- [ ] 2.2 Leave `MOVE-016`'s infantry-only line unchanged. Vehicle falling is still undefined, and this change does not close it.

---

## 3. `docs/05-construction-components.md` — cross-references

Each component rule gains one pointer, matching the style `CMP-004` already uses for `VEH-009`. Add only the sentence shown; change nothing else in these rules.

- [ ] 3.1 `CMP-003` (Wheels): replace the line "Movement is resolved using the Vehicle Movement Rules." with:

> Movement is resolved using the Vehicle Movement Rules. Terrain behaviour follows `08-vehicles.md` (VEH-022) — a wheel's axle height is its Terrain Threshold.

- [ ] 3.2 `CMP-004` (Tracks): replace the line "Pivot behavior follows `08-vehicles.md` (VEH-009)." with:

> Pivot behavior follows `08-vehicles.md` (VEH-009), and terrain behaviour (VEH-022).

- [ ] 3.3 `CMP-005` (Hover System): replace the line "Hover vehicles ignore wheel requirements. Pivot and movement behavior follows `08-vehicles.md` (VEH-011)." with:

> Hover vehicles ignore wheel requirements. Pivot and movement behavior follows `08-vehicles.md` (VEH-011), and terrain behaviour (VEH-024) — a hover vehicle's ground clearance is its Terrain Threshold.

- [ ] 3.4 `CMP-006` (Walkers): replace the line "Pivot behavior follows `08-vehicles.md` (VEH-010)." with:

> Pivot behavior follows `08-vehicles.md` (VEH-010), and terrain behaviour (VEH-023) — a walker's knee height is its Terrain Threshold.

---

## 4. `docs/14-glossary.md` — two entries

Insert both in the same style as the surrounding entries: a `## ` heading, the definition, then a `---` separator. Place them anywhere sensible among the existing terms; the glossary is not alphabetised.

- [ ] 4.1 Add:

> ## Terrain Threshold
>
> The height a vehicle can cross or descend without being blocked or stranded, read from its locomotion rather than assigned: axle height for wheels and tracks, knee height for walkers, ground clearance for hover. Measured in plate layers. See `08-vehicles.md` (VEH-021 through VEH-024).

- [ ] 4.2 Add:

> ## Stranded
>
> A vehicle that has entered a drop deeper than its Terrain Threshold. A stranded vehicle is Immobilized (`08-vehicles.md`, VEH-019, VEH-025) and keeps operating its remaining systems. Hover vehicles cannot be stranded.

---

## 5. Verify

- [ ] 5.1 Run `python3 scripts/lint_ruleset.py`; confirm no structural issues. This checks the new headings' em dashes, the ascending IDs, and that every `(VEH-0NN)` cross-reference resolves.
- [ ] 5.2 Run `grep -n "^# VEH-" docs/08-vehicles.md` and confirm `VEH-001` through `VEH-025` appear once each, in ascending order, with no gaps.
- [ ] 5.3 Confirm no existing rule ID was renumbered and no existing rule was deleted — `VEH-021` … `VEH-025` are purely additive.
- [ ] 5.4 Run `git diff --stat main...HEAD` and confirm exactly these paths changed: `docs/08-vehicles.md`, `docs/07-movement.md`, `docs/05-construction-components.md`, `docs/14-glossary.md`, and the four new files under `openspec/changes/vehicle-terrain-thresholds/`.
- [ ] 5.5 Run `grep -c "Terrain Threshold" docs/08-vehicles.md` and confirm at least 5 hits — the term appears in every one of the five new rules. Separately confirm one hit in `docs/14-glossary.md`.
- [ ] 5.6 Confirm `docs/07-movement.md` still states that vehicle falling damage is undefined. This change must not appear to close that gap.
- [ ] 5.7 Confirm no numeric value changed anywhere: this change adds thresholds that are *measured*, and assigns no number to any vehicle.
- [ ] 5.8 Run `git diff main...HEAD -- docs/ | grep -E "^-" | grep -v "^---"` and confirm every removed line is one of the four cross-reference lines replaced in section 3, or the Vehicle Movement paragraph replaced in 2.1. Nothing else should be deleted.
