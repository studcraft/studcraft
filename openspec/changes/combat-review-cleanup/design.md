## Context

Third review file in the same thread (`delete-me-melee-comments.md` → `delete-me-melee-comments.md` addendum → `delete-me-combat-comments.md`), this time reviewing `11-combat.md` as a whole rather than melee specifically. Its overall framing — "Combat should become a thinner orchestrator" — largely describes work already completed by `ruleset-consistency-fixes` (Finding 10 fixed CBT-003/004/006/008's duplication with Weapons; Finding 11 fixed CBT-012's duplication with Core Rules) before this review was written. The review reads as if evaluating an earlier revision of the document; verifying each item against the actual current file, rather than assuming the review is current, was the bulk of this change's work.

## Decisions

### "Impact Attempt" rejected a third time, same reasoning each time

REVIEW-002 (introduce "Impact Attempt"), REVIEW-003 (attack sequence using "Generate Impact Attempts"), and REVIEW-012/014 (flow diagrams using "Impact Attempt") all repeat the same terminology proposal already rejected twice in the melee review threads (`delete-me-melee-comments.md` REVIEW-001 and its REVIEW-009 follow-up). The reasoning doesn't change with repetition: `10-weapons.md` WPN-006 already names the pre-resolution unit a weapon generates "Attack Die," and every rule that generates one (`WPN-006` for ranged, `MEL-003` for melee) already uses that exact term. A second term for the identical concept is drift, not clarity — rejecting it here keeps this repo's terminology decisions consistent across all three review rounds rather than caving to volume of repetition.

### REVIEW-003's Attack Sequence abstraction rejected; the real underlying gap (melee accuracy) fixed differently

REVIEW-003 wants `CBT-001` rewritten from 8 concrete steps to 6 abstract ones, reasoning that the concrete version "exposes internal mechanics." Checked against the actual current file: `CBT-001`'s 8 steps already map one-to-one onto `CBT-002` through `CBT-009`, each of which fully owns its own mechanic (Line of Sight → CBT-002, Weapon Range → CBT-003 → WPN-005, Attack Dice → CBT-004 → WPN-006, and so on) — `CBT-001` is a named-step table of contents, not a restatement, the same pattern `16-damage-system.md` DMG-009 already uses successfully. There's no duplication left here to remove; abstracting the step names to "Verify Attack Legality" etc. would only make it harder to know which specific rule a step maps to.

The review's implicit correct observation — that `CBT-001` claims universality ("every attack follows the same procedure") while its own steps 3–4 are ranged-only — is real, though. Melee doesn't check Line of Sight or Weapon Range; it checks Physical Contact (`12-melee.md` MEL-001/MEL-014). Fixed with one added sentence noting the substitution, rather than restructuring the whole sequence around abstract categories.

### CBT-011 (No Damage Values): REVIEW-009 applied, list dropped in favor of citing 10-weapons.md's own Summary

`CBT-011`'s "Weapons only define: Range / Number of Attack Dice / Impact Strength / Firing Position" is, on inspection, a near-duplicate of `10-weapons.md`'s own Summary section (Length → Range/Capacity, Muzzle Count → Attack Dice, Muzzle Size → Impact Strength) — the exact "same fact in two documents" pattern this repo's review process exists to catch, just not caught until this review pointed at it. Applied with one modification: kept the historical note about Impact Strength/WPN-021 (a real prior contradiction-fix worth preserving, not something `10-weapons.md`'s Summary mentions) rather than deleting it along with the list, since the review's own suggested wording would have discarded that context too.

### CBT-008 (Defender Resolution): REVIEW-006 applied, but not all the way to a single sentence

The review's suggested replacement — "Each successful Impact is resolved using the Component Damage System" — would drop the ordered sub-steps (assign component → check Resistance → Damage Roll → possible Dead) entirely. Those sub-steps don't restate any mechanic in detail (no thresholds, no dice values, purely named steps with DMG- citations) — they're signposting, the same value `CBT-001`'s own step list and the Combat Flow diagram provide. Tightened the wording instead of removing the structure.

## Risks / Trade-offs

None — small wording edits, no rule ID changes, no mechanic changes.

## Open Questions

None outstanding.
