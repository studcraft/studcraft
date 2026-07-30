## Context

Second addendum to the melee review thread (`delete-me-melee-comments.md`), following `simplify-melee-combat` (PR #22) and `melee-review-cleanup` (PR #23).

## Decisions

### Update the existing Combat Flow diagram in place, don't add REVIEW-010's proposed new one

REVIEW-010 suggested documenting a new, more complete flow diagram (Weapon → Delivery Method → Impact → Combat System → Component Damage System → Physical Consequences) as "a high-level reference across the documentation." Adding it verbatim, in a new location, would have created a **fourth** flow diagram describing combat resolution at yet another level of granularity, alongside: `11-combat.md`'s existing "Combat Flow," `16-damage-system.md` DMG-009's "Combat Resolution Overview" (the actual detailed sequence), and `12-melee.md`'s Design Philosophy diagram (melee-specific framing). That's exactly the "same fact restated in multiple places, no cross-reference" pattern this repo's review process exists to catch — the fix is to correct the existing, already-canonical diagram (`11-combat.md`'s "Combat Flow"), not add a new one next to it.

The updated diagram keeps the same shape as before (`Weapon` → ... → `Physical Model Changes`) and adds exactly one thing that was missing: an explicit **Delivery Method** fork between ranged and melee, citing `MEL-001`/`MEL-014` for melee's side and the existing Line of Sight + Range rules for ranged's. The detailed resolution steps (Attack Roll, Geometry Check, Damage Roll, Component State Change, Penetration) are collapsed into one "Combat Resolution" box citing `DMG-009` through `DMG-017` rather than re-listed — `DMG-009` already owns that exact sequence in full detail; restating it here would be the same duplication this proposal is trying to avoid.

### REVIEW-009 is not applicable

REVIEW-009 proposes refining the wording "The Combat System already determines how that attempt becomes a successful Impact" to "...how an Impact attempt is resolved" — but that sentence only ever existed inside REVIEW-001's own suggested wording in the first review pass (`delete-me-melee-comments.md`'s original REVIEW-001), which `melee-review-cleanup` explicitly rejected (see that change's `design.md`): melee never adopted "Impact attempt" as a term, and still says "Attack Die," matching `10-weapons.md` WPN-006. REVIEW-009 refines wording that was never shipped. No action taken; recorded here so the rejection reasoning carries forward to this follow-up round.

## Risks / Trade-offs

None — single-diagram edit, no mechanic or rule-ID change.

## Open Questions

None outstanding.
