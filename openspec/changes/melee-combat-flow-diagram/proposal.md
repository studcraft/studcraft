## Why

A second review addendum (`delete-me-melee-comments.md`, REVIEW-009/REVIEW-010) followed up on the melee review cleanup (PR #23). REVIEW-010 correctly noticed that `11-combat.md`'s "Combat Flow" diagram still reads as ranged-only ("Generate Attack Dice" straight from "Weapon," no mention of how melee fits in) despite `simplify-melee-combat` having already unified ranged and melee resolution.

## What Changes

- `docs/11-combat.md`'s "Combat Flow" diagram updated in place to show the shared **Delivery Method** fork (Line of Sight + Range for ranged, Physical Contact for melee — `12-melee.md` MEL-001/MEL-014) before Attack Dice generation, and collapses the detailed resolution steps into a single "Combat Resolution" box citing `16-damage-system.md` DMG-009 through DMG-017 (already the single owning sequence) instead of re-listing them.
- REVIEW-009 is **not applicable**: it proposes refining wording ("The Combat System already determines how an Impact attempt is resolved") that only exists in the reviewer's own REVIEW-001 suggestion from the first review pass — a suggestion this repo already rejected in `melee-review-cleanup` (PR #23) because it would have introduced "Impact attempt" as new melee-only vocabulary inconsistent with the shipped ranged-side terminology ("Attack Die," `10-weapons.md` WPN-006). Since the wording REVIEW-009 wants to refine was never adopted, there's nothing to refine.

## Impact

- One diagram updated in `docs/11-combat.md`, no rule ID touched, no capability requirement changed.
- Avoids adding a fourth, separate architecture diagram (REVIEW-010's literal suggestion) alongside the existing ones in `11-combat.md` (this one), `16-damage-system.md` (DMG-009, more granular), and `12-melee.md` (melee-specific framing) — updating the existing combat.md diagram in place, rather than adding a new one, keeps exactly one top-level flow diagram instead of two competing ones.
