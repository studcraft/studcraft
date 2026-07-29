## 1. Document Placement

- [ ] 1.1 Create `docs/16-component-damage.md` for the `component-damage` capability (Components, Resistance, Component State, Universal Destruction, Internal Components) — mirrors the reviewed RFC's Part 1.
- [ ] 1.2 Create `docs/17-damage-resolution.md` for the `damage-resolution` capability (Attack Roll, Geometry Check, Damage Roll, Penetration, Weapon Distribution, Repairs) — mirrors the reviewed RFC's Part 2.
- [ ] 1.3 Use rule prefix `DMG-` across both documents, numbered sequentially starting in `docs/16-component-damage.md` and continuing into `docs/17-damage-resolution.md` (one namespace across both, matching how `10-weapons.md` uses one `WPN-` namespace throughout).

## 2. Write `docs/16-component-damage.md`

- [ ] 2.1 Write Purpose and Design Philosophy, using this change's reviewed proposal/specs (not the original unreviewed RFC) as source.
- [ ] 2.2 Add Component Targeting, Components Have No Hit Points, Geometry Defines Resistance (with the four worked examples: minifig, mounted cannon, brick shield, plate shield), Component State Progression, Universal Destruction, Composite Objects, and Internal Components — per `specs/component-damage/spec.md`.
- [ ] 2.3 Add a "Relationship to Materials" note cross-referencing `13-materials.md`: MAT-001/MAT-005–MAT-010/MAT-012–MAT-015 continue to describe physical/cosmetic response and are unaffected; MAT-003/MAT-004's fixed hit-counts are superseded by Resistance (same typical outcome — two hits for a minifig — different mechanism); MAT-011 (Armour) is fulfilled by the Geometry Check and Damage Roll (`17-damage-resolution.md`); MAT-016 (Cover) is explicitly untouched.
- [ ] 2.4 Add a Summary section per `system/documentation-standards.md`'s required structure.

## 3. Write `docs/17-damage-resolution.md`

- [ ] 3.1 Write Purpose and Design Philosophy (Geometry vs. Dice), using this change's reviewed proposal/specs as source.
- [ ] 3.2 Add Combat Resolution Overview, Generate Impacts, Attack Roll, Select Target Component, Geometry Check, Damage Roll, Multiple Impacts, Penetration, Composite Vehicles targeting, Weapon Distribution, and Repairs — per `specs/damage-resolution/spec.md`.
- [ ] 3.3 Include the four worked Combat Examples (Pistol vs. Minifig, Shotgun vs. Minifig, Heavy Cannon vs. Shield, Jeep Cannon) as non-normative illustrations.
- [ ] 3.4 Add a Summary section per `system/documentation-standards.md`'s required structure.
- [ ] 3.5 Run `python3 scripts/lint_ruleset.py` after writing both docs and fix any structural issues it reports.

## 4. Update Existing Docs (direct edits — no capability exists yet to delta against)

- [ ] 4.1 Update `docs/11-combat.md` CBT-011: weapons no longer "never possess... Strength" — update to state that Impact Strength (WPN-021) is a legitimate, geometry-derived weapon property, while Damage and Armour Penetration still do not exist as weapon properties. Note in the doc why this changed (WPN-021 postdates the original wording).
- [ ] 4.2 Update `docs/11-combat.md` CBT-007: add the free-rotating-mount exception (see `specs/damage-resolution/spec.md`, Weapon Distribution) — fixed mounts keep the existing no-split rule.
- [ ] 4.3 Update `docs/13-materials.md` MAT-003 (Glass) and MAT-004 (Infantry): rework their fixed hit-count wording to derive from Resistance/Component State instead of asserting a fixed count, per the design.md Decisions. Keep their physical/cosmetic description (glass removed, minifig seated/removed) unchanged.
- [ ] 4.4 Update `docs/13-materials.md` MAT-011 (Armour): note that the Geometry Check and Damage Roll (`17-damage-resolution.md`) fulfill the "Defence Dice, Impact cancellation, Component protection" this rule previously deferred to future rules.
- [ ] 4.5 Confirm `docs/13-materials.md` MAT-016 (Cover) is left untouched.
- [ ] 4.6 Confirm no change is needed to `docs/10-weapons.md` (Range/Attack Dice/Impact Strength are consumed as-is).

## 5. Glossary

- [ ] 5.1 Add entries to `docs/14-glossary.md` for: Component, Resistance, Component State (OK/TOUCHED/DESTROYED), Damage Roll, Geometry Check, Penetration (Overrun).

## 6. Validation

- [ ] 6.1 Confirm the four worked Combat Examples in `docs/17-damage-resolution.md` match the scenarios in `specs/damage-resolution/spec.md`.
- [ ] 6.2 Confirm a typical minifig (Resistance 1 per the worked example) still takes exactly two failed Damage Rolls to go from `OK` to `DESTROYED`, matching the outcome `MAT-004` previously asserted directly.
- [ ] 6.3 Confirm no change was made to `docs/10-weapons.md`'s Range, Attack Dice, or Impact Strength formulas.

## 7. Housekeeping

- [ ] 7.1 No `CHANGELOG.md` edit needed — `Release cut` computes the bump automatically from git history. Since this change is **BREAKING** (CBT-011/CBT-007/MAT-003/MAT-004 wording changes), add a `**Bump:** major` line to one commit message as the optional escalation marker (see `system/workflow.md`).
- [ ] 7.2 Remove `delete-me-damage.md` from the repo root now that its (reviewed and corrected) content has been formalized into this OpenSpec change.
- [ ] 7.3 Open a PR from the `component-damage-system` branch for review. Do not archive in the same PR — archiving is a separate, later step (see `system/workflow.md`, Archiving) enforced by the `OpenSpec archive must be separate from apply` CI gate.
