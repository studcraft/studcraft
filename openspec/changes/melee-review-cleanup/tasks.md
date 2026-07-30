## 1. Apply valid review feedback

- [x] 1.1 REVIEW-002: `MEL-013` — add "energy-transfer surface" rationale connecting muzzle and striking end.
- [x] 1.2 REVIEW-003: `MEL-014` — remove Spear/Sword/Knife examples; state reach as a universal geometric fact.
- [x] 1.3 REVIEW-004: `MEL-002` — remove redundant "(if exposed)" qualifier from "Vehicle crew".
- [x] 1.4 REVIEW-005 (modified): `MEL-010` — repurpose to an explicit "Merged into Component Targeting" marker instead of deleting the ID outright, per this repo's rule-ID-stability convention.
- [x] 1.5 REVIEW-006: `MEL-012` — simplify to one direct sentence on document scope.

## 2. Reject invalid review feedback, with reasoning recorded

- [x] 2.1 REVIEW-001 (rename "Attack Die" to "Impact attempt"): rejected — contradicts the already-shipped ranged-side split where `10-weapons.md` WPN-006 owns Attack Dice count as a construction concern; applying it would make melee and ranged use different vocabulary for the identical concept. Reasoning recorded in `design.md`.

## 3. No action needed

- [x] 3.1 REVIEW-007, REVIEW-008: praise-only, no concrete edit requested — confirmed no action needed.

## 4. Verify

- [x] 4.1 Run `python3 scripts/lint_ruleset.py` and confirm no structural issues.
- [x] 4.2 Confirm `docs/12-melee.md` still has exactly `MEL-001` through `MEL-014` — no ID added, removed, or renumbered.
- [x] 4.3 `openspec validate --strict` will fail on "no delta found" — expected and documented in `design.md`; this change has no formalized-capability impact to write a delta against.
