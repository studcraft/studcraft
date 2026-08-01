## Context

`system/proposal-review.md` documents a failure class found repeatedly in this repo's proposals: "same rule asserted twice, independently, in two different documents." This proposal applies that same lens to the existing ruleset itself rather than a new proposal — a `docs/*.md` audit turned up two foundational facts (Unit Base dimensions, Action Points per activation) restated independently far more than the two-document cases already fixed this session (`CBT-009`/`MAT-017`). `05-construction-components.md` (CMP-009, CMP-010) already demonstrates the fix pattern this repo wants: cross-reference the canonical rule instead of restating it.

## Goals / Non-Goals

**Goals:**
- One canonical statement each for "Unit Base = 4×3 studs" and "3 Action Points per activation," with every other mention reduced to a cross-reference plus whatever document-specific elaboration is genuinely unique to that document.
- Zero change to any measured rule value, formula, or player-facing behavior.
- Fix the adjacent staleness bug in `01-foundations.md`'s reading-order list while touching that document anyway.

**Non-Goals:**
- Consolidating any other repeated pattern not specifically audited here (e.g. root-level docs like `CODE_OF_DESIGN.md`/`CONTRIBUTING.md` restating design philosophy multiple times — out of scope, this proposal is `docs/*.md` only, per the user's explicit scope).
- Renumbering or removing any existing rule ID. Every touched document keeps its rule IDs; content is trimmed, not deleted, except where noted.

## Decisions

**`02-core-rules.md` CORE-001/CORE-006 are the canonical sources, not `01-foundations.md`.**
Alternative considered: make `01-foundations.md` (the very first document players read) canonical instead, since it's the natural "definitions live here" location. Rejected — `01-foundations.md` has no rule-ID scheme at all (no `FOU-001` or similar), while CORE-001/CORE-006 are already formal, numbered, cross-referenceable rules. Every other document already cites `CORE-` rules by ID elsewhere (e.g. `05-construction-components.md` citing CORE-007) — reusing the same canonical source keeps one consistent citation style instead of introducing a second one just for these two facts.

**Trim, don't delete, every redundant restatement.**
Each affected section still has a real job beyond stating "4×3 studs" or "3 AP" — `08-vehicles.md`'s Unit Base section also anchors its vehicle-footprint examples; `07-movement.md`'s anchors infantry movement math. Deleting the section entirely would lose that context. The fix is narrower: replace the sentence(s) that restate the raw fact with a cross-reference, keep everything else.

**`FLOW-005` keeps its ID but loses its redundant content.**
`FLOW-004` and `FLOW-005` in `03-game-flow.md` both independently assert "every unit receives exactly 3 AP" — almost word-for-word duplicates of each other, on top of also duplicating `CORE-006`. Alternative considered: delete `FLOW-005` outright. Rejected, per "rule identifiers should remain stable" (`system/documentation-standards.md`) — instead, `FLOW-005` keeps its ID and keeps the one piece of content it has that `FLOW-004` doesn't: the explicit list of unit types this applies to (Infantry, Vehicles, Walkers, Hovercraft, future types) and "no unit gains additional AP through its profile." The bare "3 AP" restatement is what gets cut, cross-referencing `CORE-006` instead.

**`01-foundations.md`'s reading order becomes a pointer to `README.md`, not a fourth independently-maintained copy.**
Alternative considered: just fix the current list by adding `15-geometry-layers.md` and `16-damage-system.md`. Rejected as a half-fix — that would leave a fourth copy of "reading order" (after `README.md`, `system/documentation-standards.md`'s tree, and `CONTRIBUTING.md`'s tree, all outside this proposal's `docs/*.md` scope but demonstrating the same staleness risk) that will go stale again the next time a document is added, exactly like it already did. Since `README.md` is the reader's natural entry point and already carries the full reading-order list, `01-foundations.md` points to it instead of maintaining a parallel copy.

## Risks / Trade-offs

- [Risk] Cross-referencing instead of restating could make a document feel incomplete to a reader who hasn't read `02-core-rules.md` yet, especially since StudCraft's own learning order puts Foundations before Core Rules. → Mitigation: every trimmed section keeps a short inline restatement of the fact itself (e.g. "One Unit Base measures 4×3 studs — see CORE-001") rather than a bare "see CORE-001" with no value shown. Only the elaboration/justification is removed, not the number itself.
- [Risk] This proposal touches 7 documents for a purely editorial change, which is a wide diff for something with zero gameplay effect. → Mitigation: accepted — the diff is wide because the duplication was wide; `python3 scripts/lint_ruleset.py` and a manual re-read confirm no rule ID, cross-reference, or Version-header regressions before merging.

## Open Questions

- Should this same audit be repeated periodically (e.g. as part of `system/proposal-review.md`'s checklist) rather than as a one-time cleanup? Deferred — worth revisiting if a third independently-duplicated fact turns up in a future proposal review.
