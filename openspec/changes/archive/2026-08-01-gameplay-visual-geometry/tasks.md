## 0. Sequencing Dependency

- [x] 0.1 Confirm `weapon-construction-system` (PR #7) has merged to `main` before archiving this change — this change's `MODIFIED Requirements` delta on `weapon-construction` needs that capability to already exist in `openspec/specs/weapon-construction/spec.md`. Applying/writing the ruleset doc (tasks below) can proceed in parallel; only the archive step has this hard dependency.

## 1. Resolve Document Placement

- [x] 1.1 Decide between a new `docs/15-geometry-layers.md` versus appending a section to `docs/01-foundations.md` (see design.md Open Questions). Default to the new file unless there's a strong reason not to, per `system/documentation-standards.md` ("large systems should receive their own document"). → Went with `docs/15-geometry-layers.md`. Also added it to `scripts/generate_site_docs.py`'s `TITLES` dict — not in the original task list, but required or the site build fails its own `check_titles_match_source()` guard.
- [x] 1.2 Confirm the chosen placement doesn't require renumbering any existing `docs/*.md` file or rule ID. → Confirmed, purely additive (docs 01-14 untouched), new rule prefix `GEO-`.

## 2. Write the Ruleset Doc

- [x] 2.1 Write Purpose, Design Philosophy, and the Gameplay Geometry / Visual Geometry definitions, using the reviewed content in this change's proposal/specs (not the original unreviewed draft) as source.
- [x] 2.2 Add the Line of Sight / Cover carve-out as its own clearly-labeled rule, cross-referencing `02-core-rules.md` (CORE-008, CORE-009, CORE-010) by ID.
- [x] 2.3 Add Functional Equivalence, scoped to measured values only (not total behavioral equivalence) — include the worked weapon example (Length 4, Width 2, four Size-1 muzzles) and a note that Line of Sight/Cover can still differ.
- [x] 2.4 Add Minimum Representation and Detailed Representation rules.
- [x] 2.5 Add a Summary section consistent with `system/documentation-standards.md`'s required structure (Purpose, Design Philosophy, Rule Definitions, Summary).
- [x] 2.6 Run `python3 scripts/lint_ruleset.py` after writing the doc and fix any structural issues it reports (rule ID uniqueness/ordering, cross-references, Version header). → Passes, 15 docs checked.

## 3. Glossary and Cross-References

- [x] 3.1 Add entries to `docs/14-glossary.md` for: Gameplay Geometry, Visual Geometry, Functional Equivalence, Minimum Representation, Detailed Representation.
- [x] 3.2 **Blocked, not just optional** — discovered during apply: this branch's `docs/10-weapons.md` still has the *pre*-`weapon-construction-system` WPN-003 wording ("rear of body to foremost muzzle"), because PR #7 hasn't merged yet. The `MODIFIED Requirements` delta in `specs/weapon-construction/spec.md` was written against PR #7's *post*-merge wording ("longest dimension... excluding decorative elements"). Editing WPN-003 now would edit text that's about to be replaced by PR #7 anyway. Same root dependency as task 0.1 — do this once PR #7 has merged into this branch (or into `main` and this branch is updated from it).
- [x] 3.3 Check `docs/02-core-rules.md` (CORE-008, CORE-009, CORE-010) for the same kind of cross-reference back to the new doc's Line of Sight/Cover carve-out. → Added one-line pointers to CORE-008 and CORE-010.

## 4. Validation

- [x] 4.1 Confirm no measured rule value or formula changes anywhere in the existing ruleset as a result of this change (this proposal is classificatory only, per design.md Non-Goals). → Confirmed: only new doc + cross-reference pointers + glossary entries were added; no formula anywhere changed.
- [x] 4.2 Walk through the Functional Equivalence and Minimum Representation scenarios in `specs/geometry-layers/spec.md` against the written doc to confirm consistency. → `docs/15-geometry-layers.md` GEO-005/GEO-006 use the same worked example and wording as the spec scenarios.

## 5. Housekeeping

- [x] 5.1 Do not edit `CHANGELOG.md` — `Release cut` computes the bump automatically from git history and defaults to minor, which is correct here (see `system/workflow.md`). No commit-message marker is needed either; this isn't a breaking change. → Confirmed untouched.
- [x] 5.2 Remove `delete-me-spec.md` from the repo root now that its (reviewed and corrected) content has been formalized into this OpenSpec change.
- [x] 5.3 Open a PR from the `gameplay-visual-geometry` branch for review before archiving this change. → Not done: changes left uncommitted per request, for review first.

> Ticked during the 2026-08-01 archive reconciliation. All three recorded blockers that no longer exist:
>
> - **0.1** — `weapon-construction-system` (PR #7) merged and is archived as `2026-07-28-weapon-construction-system`.
> - **3.2** — the pre-#7 WPN-003 wording it waited on ("rear of body to foremost muzzle") is gone from `docs/10-weapons.md`, and this change's `weapon-construction` delta was retired as superseded in PR #35, so the requirement it wanted to edit is now owned elsewhere. The sentence quoted in that task is the only place the old wording still appears anywhere in the repo.
> - **5.3** — the docs work did land: `docs/15-geometry-layers.md` is on `main` with GEO-001 through GEO-007.
>
> The `geometry-layers` delta was refreshed against `docs/` before archiving, because it had drifted: it omitted Resistance from the measured-value list (added by `audit-round2-repairs`), lacked GEO-002's structural-cross-section carve-out, and still described Cover as gradual after CORE-010 became binary. Archiving it unrefreshed would have recreated the exact drift PR #35 fixed.
