## 1. Document Placement

- [x] 1.1 Create a single `docs/16-damage-system.md` covering both the `component-damage` and `damage-resolution` capabilities. Do not split into two files: the two capabilities are tightly coupled (Resistance only matters because Geometry Check reads it; Geometry Check only matters because it feeds the Damage Roll), and `weapon-construction-system` already established the precedent that one OpenSpec change can span multiple capabilities while still shipping as one reader-facing document (`10-weapons.md` covers both `weapon-construction` and `weapon-capacity`).
- [x] 1.2 Structure the document as two clearly labeled sections: "Component Damage" (structure — mirrors the reviewed RFC's Part 1) and "Damage Resolution" (sequence — mirrors Part 2), so the two OpenSpec capabilities stay traceable within the one file.
- [x] 1.3 Use rule prefix `DMG-` numbered sequentially across the whole document (one namespace, matching how `10-weapons.md` uses one `WPN-` namespace throughout).

## 2. Write "Component Damage" Section

- [x] 2.1 Write Purpose and Design Philosophy, using this change's reviewed proposal/specs (not the original unreviewed RFC) as source.
- [x] 2.2 Add Component Targeting, Components Have No Hit Points, Geometry Defines Resistance (with the four worked examples: minifig, mounted cannon, brick shield, plate shield), Component State Progression, Universal Destruction, Composite Objects, and Internal Components — per `specs/component-damage/spec.md`.
- [x] 2.3 Add a "Relationship to Materials" note cross-referencing `13-materials.md`: MAT-001/MAT-005–MAT-010/MAT-012–MAT-015 continue to describe physical/cosmetic response and are unaffected; MAT-003/MAT-004's fixed hit-counts are superseded by Resistance (same typical outcome — two hits for a minifig — different mechanism); MAT-011 (Armour) is fulfilled by the Geometry Check and Damage Roll (Damage Resolution section, same document); MAT-016 (Cover) is explicitly untouched.

## 3. Write "Damage Resolution" Section

- [x] 3.1 Write a short intro (Geometry vs. Dice), using this change's reviewed proposal/specs as source.
- [x] 3.2 Add Combat Resolution Overview, Generate Impacts, Attack Roll (briefly restate the existing 4/5/6 threshold, citing `11-combat.md` CBT-005 as authoritative — do not move CBT-004/CBT-005 out of `11-combat.md`; they belong to "does an Impact get generated," which is squarely `11-combat.md`'s Attack Sequence, not this document's concern), Select Target Component, Composite Vehicle Targeting, Geometry Check, Damage Roll, Multiple Impacts, Penetration, Weapon Distribution, and Repairs — per `specs/damage-resolution/spec.md`.
- [x] 3.3 Include the four worked Combat Examples (Pistol vs. Minifig, Shotgun vs. Minifig, Heavy Cannon vs. Shield, Jeep Cannon) as non-normative illustrations.
- [x] 3.4 Add one Summary section for the whole document (covering both sections) per `system/documentation-standards.md`'s required structure.
- [x] 3.5 Run `python3 scripts/lint_ruleset.py` after writing the document and fix any structural issues it reports.

## 4. Update Existing Docs (direct edits — no capability exists yet to delta against)

- [x] 4.1 Update `docs/11-combat.md` CBT-011: weapons no longer "never possess... Strength" — update to state that Impact Strength (WPN-021) is a legitimate, geometry-derived weapon property, while Damage and Armour Penetration still do not exist as weapon properties. Note in the doc why this changed (WPN-021 postdates the original wording).
- [x] 4.2 Update `docs/11-combat.md` CBT-007: add the free-rotating-mount exception (see `specs/damage-resolution/spec.md`, Weapon Distribution) — fixed mounts keep the existing no-split rule.
- [x] 4.3 Update `docs/13-materials.md` MAT-003 (Glass) and MAT-004 (Infantry): rework their fixed hit-count wording to derive from Resistance/Component State instead of asserting a fixed count, per the design.md Decisions. Keep their physical/cosmetic description (glass removed, minifig seated/removed) unchanged.
- [x] 4.4 Update `docs/13-materials.md` MAT-011 (Armour): note that the Geometry Check and Damage Roll (`16-damage-system.md`) fulfill the "Defence Dice, Impact cancellation, Component protection" this rule previously deferred to future rules.
- [x] 4.5 Confirm `docs/13-materials.md` MAT-016 (Cover) is left untouched.
- [x] 4.6 Confirm no change is needed to `docs/10-weapons.md` (Range/Attack Dice/Impact Strength are consumed as-is).
- [x] 4.7 Update `docs/11-combat.md` CBT-008 (Defender Resolution): the hand-off currently points only to `13-materials.md`/`08-vehicles.md`. Update it to route through `16-damage-system.md` first (component/resistance/state resolution), with Materials now describing the physical/cosmetic result rather than the resolution itself.
- [x] 4.8 Update `docs/11-combat.md` CBT-013 (Armour): currently just says "Armour belongs to the defending model." Update it to point at the Geometry Check and Damage Roll (`16-damage-system.md`) as the mechanism, per MAT-011/design.md.
- [x] 4.9 Consolidate the duplicate "prefer physical representation" rule: `CBT-009` (`11-combat.md`) and `MAT-017` (`13-materials.md`) already assert nearly the same thing independently, predating this change. Make `16-damage-system.md`'s Universal Destruction the canonical statement (destroyed = physically removed), and rework CBT-009 and MAT-017 into one-line pointers to it instead of each restating the full rule.

## 5. Glossary

- [x] 5.1 Add entries to `docs/14-glossary.md` for: Component, Resistance, Component State (OK/TOUCHED/DESTROYED), Damage Roll, Geometry Check, Penetration (Overrun).

## 6. Repository-Wide Navigation (README and site build)

- [x] 6.1 `README.md`'s Repository Structure tree and Rulebook reading order are already stale — they never got `15-geometry-layers.md` added when that change shipped. Add it now (Part I — Foundations reads naturally, since it's a cross-cutting "how to interpret any model" concept, same spirit as `01-foundations.md`), alongside adding `16-damage-system.md` (Part IV — Combat, after `13-materials.md`).
- [x] 6.2 Add `16-damage-system.md` (and, while fixing this, confirm `15-geometry-layers.md` is present) to `README.md`'s "Current Status" implemented-systems list.
- [x] 6.3 Add `"16-damage-system.md": "Damage System"` to `scripts/generate_site_docs.py`'s `TITLES` dict (`15-geometry-layers.md` is already present from that earlier change). Run the script or otherwise confirm `check_titles_match_source()` passes.

## 7. Validation

- [x] 7.1 Confirm the four worked Combat Examples in `docs/16-damage-system.md` match the scenarios in `specs/damage-resolution/spec.md`.
- [x] 7.2 Confirm a typical minifig (Resistance 1 per the worked example) still takes exactly two failed Damage Rolls to go from `OK` to `DESTROYED`, matching the outcome `MAT-004` previously asserted directly.
- [x] 7.3 Confirm no change was made to `docs/10-weapons.md`'s Range, Attack Dice, or Impact Strength formulas.

## 8. Housekeeping

- [x] 8.1 No `CHANGELOG.md` edit needed — `Release cut` computes the bump automatically from git history. Since this change is **BREAKING** (CBT-011/CBT-007/MAT-003/MAT-004 wording changes), add a `**Bump:** major` line to one commit message as the optional escalation marker (see `system/workflow.md`).
- [x] 8.2 Remove `delete-me-damage.md` from the repo root now that its (reviewed and corrected) content has been formalized into this OpenSpec change.
- [ ] 8.3 Open a PR from the `component-damage-system` branch for review. Do not archive in the same PR — archiving is a separate, later step (see `system/workflow.md`, Archiving) enforced by the `OpenSpec archive must be separate from apply` CI gate.
