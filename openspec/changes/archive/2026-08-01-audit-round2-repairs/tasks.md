## 1. R-01 (design decision, confirmed with user)

- [x] 1.1 `docs/16-damage-system.md` DMG-003: scoped plate-layer measurement to constructed components; added the fixed-piece exception (minifig = Resistance 1 by baseline, not measurement).
- [x] 1.2 `docs/16-damage-system.md` DMG-004 Example 1: reworded to state the fixed baseline instead of a physically-false "built 1 plate thick" claim.
- [x] 1.3 `docs/16-damage-system.md` DMG-008: adjusted "only how it's built does" to account for fixed-baseline components.
- [x] 1.4 `docs/16-damage-system.md` DMG-004 Example 2: fixed header/body mismatch found in the same area (M-02).

## 2. Regressions (R-02 through R-05)

- [x] 2.1 `docs/11-combat.md` CBT-012: fixed to match the binary cover rule (CORE-010/WPN-016) instead of contradicting it.
- [x] 2.2 `docs/15-geometry-layers.md` GEO-004: fixed stale gradual-cover wording ("physical amount hidden," "grant extra cover").
- [x] 2.3 `docs/09-transport.md` Summary: fixed "Embarking costs 1 AP" to match the per-UB cost TRN-005 already uses.
- [x] 2.4 `docs/09-transport.md` TRN-005: removed the self-contradictory "complete activation... like any other action" line; aligned with TRN-006.

## 3. New findings (N-01 through N-07)

- [x] 3.1 `docs/15-geometry-layers.md` GEO-001/GEO-003: added Resistance to the Gameplay Geometry taxonomy.
- [x] 3.2 `docs/15-geometry-layers.md` GEO-002: added the structural-vs-decorative carve-out (a plate in the structural cross-section is Gameplay Geometry regardless of appearance).
- [x] 3.3 `docs/16-damage-system.md` DMG-019: added equipment requirement for repairing another unit; limited self-repair to once per activation.
- [x] 3.4 `docs/11-combat.md` CBT-007: added the split-target procedure (verify each sub-target individually, cost stays 1 AP per weapon system).
- [x] 3.5 `docs/12-melee.md` MEL-003: clarified dual-wielding is 2 weapon systems / 2 AP / 2 dice, not 1 attack producing 2 dice; updated the example table. MEL-008: same AP-cost clarification for unarmed combat.
- [x] 3.6 `docs/07-movement.md` MOVE-016: declared the Geometry Check exception explicitly; scoped to infantry (vehicle falling already an acknowledged gap).
- [x] 3.7 `docs/03-game-flow.md` FLOW-003: fixed "strictly alternate" to match FLOW-002's uneven-forces exception.
- [x] 3.8 `docs/11-combat.md` CBT-010: marked its example as explicitly hypothetical (no current rule produces mutual melee attacks).

## 4. Minor (M-01 through M-12)

- [x] 4.1 M-01: `docs/16-damage-system.md` — last "armor" spelling fixed to "armour."
- [x] 4.2 M-02: folded into task 1.4 above.
- [x] 4.3 M-03: `docs/14-glossary.md` "Weapon Reach" entry reworded to match MEL-014 (not a looked-up value).
- [x] 4.4 M-04: `docs/14-glossary.md` "Closed Transport" entry reworded to match the penetration-via-hull mechanic.
- [x] 4.5 M-05: `docs/08-vehicles.md` VEH-011 no longer double-charges movement already covered by VEH-004.
- [x] 4.6 M-06: `docs/06-deployment.md` DEP-004 reworded so it can't be misread as contradicting DEP-006.
- [x] 4.7 M-07: `docs/04-construction-standard.md` SCS-003 — trimmed residual "no maximum vehicle size" duplication.
- [x] 4.8 M-08: `docs/10-weapons.md` WPN-002 — added a note on round-piece manufacturing availability (3×3/5×5 aren't standard sizes).
- [x] 4.9 M-09: `docs/07-movement.md` MOVE-004 — added a correct geometric note (12 is a multiple of both the UB's 3-stud and 4-stud axes).
- [x] 4.10 M-10: `system/documentation-standards.md` — documented the intentional closing-quote split.
- [x] 4.11 M-11: `README.md` Part III retitled "Deployment & Movement."
- [x] 4.12 M-12: `docs/06-deployment.md` — cross-referenced CORE-005's acknowledged structure-damage gap.

## 5. Spec delta

- [x] 5.1 `openspec/specs/component-damage/spec.md`: added a further `MODIFIED` delta (on top of `full-audit-repairs`'s pending one) for "Geometry Defines Resistance," adding the fixed-piece exception.

## 6. Verify

- [x] 6.1 Run `python3 scripts/lint_ruleset.py` after every batch of edits and confirm no structural issues.
- [x] 6.2 Confirm no rule ID added, removed, or renumbered anywhere in `docs/`.
