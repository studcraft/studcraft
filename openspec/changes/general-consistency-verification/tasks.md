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

## 5. Verify

- [x] 5.1 Run `python3 scripts/lint_ruleset.py` and confirm no structural issues.
- [x] 5.2 Confirm no rule ID added, removed, or renumbered anywhere.
