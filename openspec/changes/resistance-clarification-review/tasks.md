## 1. Verify the external review against current shipped text

- [x] 1.1 REVIEW-001 (Define the Structural Unit): already satisfied by `DMG-003`'s "measured in plate layers... a standard brick is 3 plates tall."
- [x] 1.2 REVIEW-002 (Bricks and Plates Become Equivalent): already satisfied by the same `DMG-003` text plus `DMG-004` Example 3.
- [x] 1.3 REVIEW-004 (Transparent Components Should Follow Geometry): already satisfied by `docs/04-construction-standard.md` SCS-023; no material table exists anywhere.
- [x] 1.4 REVIEW-005 (Penetration Already Handles Multiple Transparent Layers): `DMG-017` confirmed fully generic; no addition needed.
- [x] 1.5 REVIEW-006 (Remove Material-Based Resistance): already satisfied by `DMG-008`.
- [x] 1.6 Confirmed the review's un-exceptioned "always Plates, never Bricks" wording cannot be applied literally against the current `DMG-003` fixed-piece exception.
- [x] 1.7 Traced the exception to its cause: `DMG-014` compares Impact Strength (studs) against Resistance (plate layers). Scope widened to fix the unit mismatch.

## 2. Align the scale — `docs/10-weapons.md`

- [x] 2.1 WPN-021: change Impact Strength to `muzzle size × 3`. Table lists Muzzle Size against Impact Strength only — `1×1` → 3, `2×2` → 6, `3×3` → 9, `4×4` → 12, `N×N` → 3N. No intermediate brick column: Resistance cannot be expressed in bricks without loss, so a brick column would invite a mixed-unit comparison.
- [x] 2.2 WPN-021: add the unit rationale in prose — one stud of muzzle width represents one brick of material, and a brick is 3 plate layers (`16-damage-system.md`, DMG-003), so both sides of the Geometry Check are counts of plate layers.
- [x] 2.3 WPN-021: add the brick relationship as an explicitly labelled shortcut ("a muzzle N studs wide defeats a component N bricks thick"), stated together with its limit — it stops dividing evenly once a component is built from plates rather than whole bricks.
- [x] 2.4 WPN-021: rewrite the "no maximum size" paragraph — the escalation argument stands, but its worked reasoning must use the new scale.
- [x] 2.5 WPN-020: update the four worked configurations' stated Impact Strengths (Twin Barrel, Quad Barrel, Heavy Cannon, Hybrid).

## 3. Reference values — apply exactly as written

Every numeric change in this proposal is listed here. Do not derive any value independently; use this table. Weapon muzzle sizes are fixed here because the shipped documents never stated them and they cannot be inferred reliably.

### 3.0 Weapon muzzle sizes (fixed by this change)

| Weapon named in examples | Muzzle size | Impact Strength |
|---|---:|---:|
| Pistol | 1×1 | 3 |
| Shotgun (per muzzle, 2 muzzles) | 1×1 | 3 |
| Heavy Cannon | 2×2 | 6 |
| Enemy Cannon (Combat Example 4) | 1×1 | 3 |

**Name collision to resolve while applying:** `WPN-020` defines "Heavy Cannon" as a 2×2 muzzle, while `DMG-017` and Combat Example 3 currently use "Heavy Cannon" at `Strength 4`, implying a 4×4 muzzle. These are two different weapons sharing one name. Unify on `WPN-020`'s definition — Heavy Cannon is 2×2, Impact Strength 6 — in every location.

### 3.1 Every numeric value, before and after

| Location | Currently | Apply |
|---|---|---|
| `DMG-004` Ex 1 — Minifig | baseline `Resistance = 1` | measured `Resistance = 3` |
| `DMG-004` Ex 2 — Cannon housing | `Resistance = 2` | unchanged |
| `DMG-004` Ex 3 — Shield, bricks | `Resistance = 3` | unchanged |
| `DMG-004` Ex 4 — Shield, 4 plates | `Resistance = 4` | unchanged |
| `DMG-004` closing paragraph | 3 vs 4 comparison | **unchanged — verify only** |
| `DMG-004` Ex 5 — Bunker (new) | — | 2 bricks thick → `Resistance = 6` |
| `DMG-004` Ex 6 — moulded (new) | — | windscreen, 1 plate thick → `Resistance = 1` |
| `DMG-008` ¶2 | "minifig (Resistance 1)" + baseline clause | "minifig (Resistance 3)", clause deleted |
| `DMG-016` shotgun example | no explicit numbers | **unchanged — verify only** (3 ≥ 3 still passes) |
| `DMG-017` example | HC `Strength 4` vs Shield `R 3` → remaining 1, minifig `R 1` | HC `Strength 6` vs Shield `R 3` → remaining 3, minifig `R 3`, `3 ≥ 3` |
| Combat Ex 1 — Pistol vs Minifig | `R 1`, `S 1`, `1 ≥ 1` | `R 3`, `S 3`, `3 ≥ 3` |
| Combat Ex 2 — Shotgun vs Minifig | no explicit numbers | state 2 muzzles at `S 3` each vs minifig `R 3` |
| Combat Ex 3 — HC vs Shield | `R 3`, `S 4`, remaining 1 | `R 3`, `S 6`, remaining 3 |
| Combat Ex 4 — Jeep Cannon | Mounted Cannon `R 2`, Enemy Cannon `S 2` | `R 2`, Enemy Cannon `S 3`, remaining 1 |
| `MEL-008` unarmed | `Impact Strength 1` | size-1 striking end → 3 |
| `WPN-020` Twin Barrel | 2 dice, Muzzle Size 1 | Impact Strength 3 each |
| `WPN-020` Quad Barrel | 4 dice, Muzzle Size 1 | Impact Strength 3 each |
| `WPN-020` Heavy Cannon | 1 die, Muzzle Size 2 | Impact Strength 6 |
| `WPN-020` Hybrid | Muzzle Sizes 2, 1, 1 | Impact Strengths 6, 3, 3 |
| `WPN-021` table | 1, 2, 3, 4, N | 3, 6, 9, 12, 3N |

`DMG-017`'s revised example is chosen deliberately: `6 − 3 = 3` against a minifig of `Resistance 3` preserves the original example's "just barely enough to continue" teaching point, which a 4×4 muzzle (remaining 9) would lose.

Combat Example 4 gains a second teaching point from the revision: remaining strength 1 continues past the destroyed cannon but stops at the Jeep's hull (`Resistance 3`, one brick), because `1 < 3`. Say so explicitly — it demonstrates penetration terminating, which no other example currently shows. The existing conclusion ("the Jeep remains operational but without its weapon") stays true.

## 4. Remove the exception — `docs/16-damage-system.md`

- [x] 4.1 DMG-003: delete the fixed-piece paragraph entirely (the one beginning "A fixed piece that offers no construction choice").
- [x] 4.2 DMG-003: state the conversion once and generally — a plate counts 1, a brick counts 3, any other element counts as the plate-equivalent of its own thickness in the direction of travel. Name no component type.
- [x] 4.3 DMG-003: add the cross-reference that Impact Strength (`10-weapons.md`, WPN-021) is expressed in the same unit, so the Geometry Check compares like with like.
- [x] 4.4 DMG-004 Example 1 (Minifig): replace the baseline wording with a normal measurement per the table in 3.1. Word it as a measurement of the piece, not as an assigned value.
- [x] 4.5 DMG-004: add Example 5 (Bunker) and Example 6 (moulded windscreen) per the table in 3.1.
- [x] 4.6 DMG-004: verify the closing paragraph needs no change (it compares Resistance 3 vs 4 only, and never referenced the baseline).
- [x] 4.7 DMG-008: delete the trailing clause "whether that Resistance comes from construction or, for a fixed piece like a minifig, its set baseline (DMG-003)".
- [x] 4.8 DMG-008: update "A typical minifig (Resistance 1, per DMG-004 Example 1)" to Resistance 3.
- [x] 4.9 DMG-017: apply the revised example per the table in 3.1.
- [x] 4.10 Combat Examples 1–4: apply per the table in 3.1, including Example 4's new penetration-stops point.
- [x] 4.11 DMG-016: verify the shotgun example still reads correctly with no edit.

## 5. Dependent rules

- [x] 5.1 `docs/12-melee.md` MEL-008: replace the hardcoded `Impact Strength 1` with "counts as a size-1 striking end", deriving Strength from WPN-021.
- [x] 5.2 `docs/12-melee.md` MEL-013: verify it still defers correctly to WPN-021 with no restated number (expected: no change needed).
- [x] 5.3 `docs/15-geometry-layers.md` GEO-001: remove the "for constructed components only; a fixed piece like a minifig uses a set baseline" clause.
- [x] 5.4 `docs/14-glossary.md`: update `Impact Strength`, `Muzzle Size`, and `Resistance` entries.
- [x] 5.5 `docs/11-combat.md` CBT-011 and CBT-013: confirm neither states a numeric Impact Strength (expected: no change needed).
- [x] 5.6 `docs/04-construction-standard.md` SCS-023: confirm it still resolves correctly with no exception in `DMG-003` (expected: no change needed).

## 6. Spec deltas

- [x] 6.1 `specs/weapon-construction/spec.md`: MODIFIED requirement "Impact Strength From Muzzle Size" — new formula and scenarios. Already written; verify it matches the applied text.
- [x] 6.2 `specs/component-damage/spec.md`: MODIFIED requirement "Geometry Defines Resistance" — unified measurement, exception removed, moulded-piece scenario added. Already written; verify it matches the applied text.

## 7. Verify

- [x] 7.1 Run `python3 scripts/lint_ruleset.py`; confirm no structural issues.
- [x] 7.2 Confirm no rule ID added, removed, or renumbered.
- [x] 7.3 Run `grep -rn "Strength \`\?[0-9]\|Impact Strength [0-9]" docs/` and confirm every hit matches the table in 3.1.
- [x] 7.4 Run `grep -rniE "baseline|fixed piece|set value|exempt" docs/` and confirm no surviving reference to an exempt Resistance.
- [x] 7.5 Run `grep -rn "Heavy Cannon" docs/` and confirm every occurrence now means a 2×2 muzzle at Impact Strength 6.
- [x] 7.6 Walk the matchup table in `proposal.md` against the applied text and confirm each row resolves as stated.
