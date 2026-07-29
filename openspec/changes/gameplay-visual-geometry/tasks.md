## 0. Sequencing Dependency

- [ ] 0.1 Confirm `weapon-construction-system` (PR #7) has merged to `main` before archiving this change — this change's `MODIFIED Requirements` delta on `weapon-construction` needs that capability to already exist in `openspec/specs/weapon-construction/spec.md`. Applying/writing the ruleset doc (tasks below) can proceed in parallel; only the archive step has this hard dependency.

## 1. Resolve Document Placement

- [ ] 1.1 Decide between a new `docs/15-geometry-layers.md` versus appending a section to `docs/01-foundations.md` (see design.md Open Questions). Default to the new file unless there's a strong reason not to, per `system/documentation-standards.md` ("large systems should receive their own document").
- [ ] 1.2 Confirm the chosen placement doesn't require renumbering any existing `docs/*.md` file or rule ID.

## 2. Write the Ruleset Doc

- [ ] 2.1 Write Purpose, Design Philosophy, and the Gameplay Geometry / Visual Geometry definitions, using the reviewed content in this change's proposal/specs (not the original unreviewed draft) as source.
- [ ] 2.2 Add the Line of Sight / Cover carve-out as its own clearly-labeled rule, cross-referencing `02-core-rules.md` (CORE-008, CORE-009, CORE-010) by ID.
- [ ] 2.3 Add Functional Equivalence, scoped to measured values only (not total behavioral equivalence) — include the worked weapon example (Length 4, Width 2, four Size-1 muzzles) and a note that Line of Sight/Cover can still differ.
- [ ] 2.4 Add Minimum Representation and Detailed Representation rules.
- [ ] 2.5 Add a Summary section consistent with `system/documentation-standards.md`'s required structure (Purpose, Design Philosophy, Rule Definitions, Summary).
- [ ] 2.6 Run `python3 scripts/lint_ruleset.py` after writing the doc and fix any structural issues it reports (rule ID uniqueness/ordering, cross-references, Version header).

## 3. Glossary and Cross-References

- [ ] 3.1 Add entries to `docs/14-glossary.md` for: Gameplay Geometry, Visual Geometry, Functional Equivalence, Minimum Representation, Detailed Representation.
- [ ] 3.2 Update `docs/10-weapons.md` WPN-003 per the `MODIFIED Requirements` delta in `specs/weapon-construction/spec.md`: reword "excluding decorative elements" to reference Visual Geometry / the new doc by name. Check WPN-015 and `docs/08-vehicles.md` (VEH-003) for the same kind of optional cross-reference (no rule text change needed there, just a pointer if it improves clarity).
- [ ] 3.3 Check `docs/02-core-rules.md` (CORE-008, CORE-009, CORE-010) for the same kind of cross-reference back to the new doc's Line of Sight/Cover carve-out.

## 4. Validation

- [ ] 4.1 Confirm no measured rule value or formula changes anywhere in the existing ruleset as a result of this change (this proposal is classificatory only, per design.md Non-Goals).
- [ ] 4.2 Walk through the Functional Equivalence and Minimum Representation scenarios in `specs/geometry-layers/spec.md` against the written doc to confirm consistency.

## 5. Housekeeping

- [ ] 5.1 Do not edit `CHANGELOG.md` — `Release cut` computes the bump automatically from git history and defaults to minor, which is correct here (see `system/workflow.md`). No commit-message marker is needed either; this isn't a breaking change.
- [ ] 5.2 Remove `delete-me-spec.md` from the repo root now that its (reviewed and corrected) content has been formalized into this OpenSpec change.
- [ ] 5.3 Open a PR from the `gameplay-visual-geometry` branch for review before archiving this change.
