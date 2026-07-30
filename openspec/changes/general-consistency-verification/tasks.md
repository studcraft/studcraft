## 1. REVIEW-018 — Standardize Terminology

- [x] 1.1 Grep every listed term (Weapon, Weapon System, Functional Muzzle, Functional Striking End, Delivery Method, Attack Dice, Attack Roll, Impact, Impact Strength, Component, Resistance, Geometry Check, Damage Roll, Component State, Penetration) across all 15 `docs/*.md` files.
- [x] 1.2 Confirm each term has exactly one canonical owning rule and no unreferenced synonym — all clean, no new issues beyond 2.1 below.

## 2. REVIEW-019 — Consistent Document Ownership

- [x] 2.1 `docs/08-vehicles.md` VEH-014: found restating "Weapon System" independently (a third copy alongside `WPN-008`/`CBT-006`, missed by prior findings which scoped their search to weapons/combat only) — reduced to a cross-reference.
- [x] 2.2 Spot-checked Weapons/Combat/Component Damage/Core Rules boundaries elsewhere — all correctly scoped (confirmed via targeted greps for Resistance, Geometry Check, Penetration, Component State outside their owning documents; every hit was already a cross-reference, not a redefinition).

## 3. REVIEW-020 — Improve Diagram Consistency

- [x] 3.1 `docs/11-combat.md` Combat Flow: added missing "Successful Impacts" step, fixed "Attack Roll" mislabel (was tagged CBT-005, which actually titles "Successful Impacts"; DMG-011 titles "Attack Roll").
- [x] 3.2 `docs/16-damage-system.md` DMG-009: brought fully in line with the canonical flow (added Delivery Method, renamed "Generate Impacts" → "Generate Attack Dice", "Select Component" → "Select Target Component", ended with "Physical Model Changes" instead of "Remaining Strength continues if applicable").
- [x] 3.3 `docs/12-melee.md` Design Philosophy diagram: "Generate Impact" → "Generate Attack Dice", matching MEL-003's own wording.

## 4. REVIEW-021 — Final Language Pass

- [x] 4.1 Checked "physically removed" vs. "removed from the model" usage across `docs/` — legitimate contextual variation (examples vs. canonical rule statements), no change needed.
- [x] 4.2 Checked "determines" vs. "defines" usage — correctly differentiated grammatical roles (causal/derived relationship vs. document/rule scope statement), not synonym drift; no change needed.

## 5. Second pass before merge (requested review)

- [x] 5.1 Re-reviewed the diff: found and fixed an internal inconsistency — `11-combat.md`'s diagram cited CBT-005 on "Successful Impacts" while same-document neighbors went uncited. Removed the citation.

## 6. Third pass: case-insensitive, repo-wide sweep for stale "materials" references

- [x] 6.1 Ran a case-insensitive grep for "material"/"materials" across the entire repo (not just `docs/`) — `remove-materials-document`'s original grep was case-sensitive and docs-scoped, missing several spots.
- [x] 6.2 `docs/14-glossary.md`: removed the stale "Material" entry (contradicted DMG-008); fixed the "Impact" entry's stale "according to their Material" line.
- [x] 6.3 `docs/01-foundations.md`: removed "Materials" from the Universal Systems list; fixed the Impacts section's "material and construction" / "materials behave differently" lines.
- [x] 6.4 `docs/10-weapons.md` WPN-016: dropped "Materials" from its effect-dependency list.
- [x] 6.5 `CODE_OF_DESIGN.md`: fixed Principle 5, Principle 10, Principle 15's stale Materials/Material Responses references.
- [x] 6.6 `CONTRIBUTING.md`: removed `13-materials.md` from its Repository Structure tree; added the missing `15-geometry-layers.md`/`16-damage-system.md` entries (stale independent of the materials removal).
- [x] 6.7 `system/proposal-review.md`: updated its "read every neighboring document" guidance to stop naming the removed document, and added a note recording the VEH-014 lesson.
- [x] 6.8 Confirmed remaining "material" mentions are correctly untouched: `CHANGELOG.md`'s frozen historical entry, `openspec/specs/damage-resolution/spec.md`'s pending-archive citation (already fixed in `remove-materials-document`'s own delta, waiting on Archive cut), and `openspec/changes/*/` files documenting the removal decision historically.

## 7. Verify

- [x] 7.1 Run `python3 scripts/lint_ruleset.py` and confirm no structural issues.
- [x] 7.2 Confirm no rule ID added, removed, or renumbered anywhere.
