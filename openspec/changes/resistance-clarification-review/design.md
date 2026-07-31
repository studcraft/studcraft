## Context

This review's six points map almost one-to-one onto work already completed across three prior changes in this repo (`full-audit-repairs`, `audit-round2-repairs`, `remove-materials-document`). The design work here is mostly verification — checking each claimed gap against the actual current text — plus a small, additive documentation improvement for the one item not fully covered.

## Decisions

### Verify against current text before assuming a gap exists

Every one of REVIEW-001, 002, 004, 005, 006 was checked directly against the currently shipped `docs/16-damage-system.md` and `docs/04-construction-standard.md` text rather than assumed to be a real gap because the review said so. This matches the pattern already established in this repo's audit-response changes (`combat-review-cleanup` did the same thing for a prior review round, finding most items already resolved). Treating a review as ground truth without checking current state risks re-doing work that already shipped, or worse, reverting a more recent, more correct fix (e.g. `audit-round2-repairs`' fixed-piece exception for minifigs, which this review's suggested wording — "Resistance must always be measured in Plates, never in Bricks," stated with no exception — would silently undo if applied literally).

### Do not apply the "always measured in Plates, never in Bricks" wording literally

The review's Conclusion states this as an absolute with no exception. Applied literally, it would remove `DMG-003`'s fixed-piece carve-out for minifigs — reintroducing the exact R-01 bug `audit-round2-repairs` fixed (a real minifig measures ~3 plate layers if measured as a constructed component, but infantry weapons are capped at Impact Strength 2, so no infantry weapon could ever damage a minifig). The review's own examples (Wall, Shield, Bunker) are all about *constructed* components, which is exactly where the "always Plates" rule already applies correctly — the review simply never considered the fixed-piece case, since it predates (or didn't discover) that finding. No wording change proposed here; the existing `DMG-003` exception stands.

### Additive-only enrichment for REVIEW-003

Rather than rewriting `DMG-004`'s existing four examples (which are already correct and already demonstrate the plate-layer rule), two new examples are proposed alongside them: a multi-brick case and a transparent-component case. This is chosen over replacing or renumbering the existing examples, consistent with this repo's general preference for additive, non-disruptive documentation changes when the underlying rule doesn't need to change.

## Risks / Trade-offs

None — this proposal makes no mechanical change. The only risk avoided (not introduced) is applying the review's un-exceptioned wording literally, which would have reintroduced a bug already fixed.

## Open Questions

None. Awaiting a follow-up instruction to apply the additive `DMG-004` examples, per the user's request to produce the proposal only this round.
