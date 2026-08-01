## Why

An external review (`delete-me-melee-comments.md`, reviewer: ChatGPT) of the just-merged `simplify-melee-combat` change (PR #22) found the document "structurally complete" and "ready for merge after minor cleanup," with eight numbered review comments. This change applies the ones that hold up, and explicitly rejects the one that doesn't, with reasoning.

## What Changes

- **REVIEW-002 applied** — `MEL-013` (Functional Striking End) gains a sentence explaining *why* size matters: a striking end and a muzzle are both "energy-transfer surfaces," just delivered differently.
- **REVIEW-003 applied** — `MEL-014` (Weapon Reach) drops the Spear/Sword/Knife comparison examples; the rule is now stated as a universal geometric fact ("determined entirely by the physical geometry of the LEGO model") rather than example-driven.
- **REVIEW-004 applied** — `MEL-002` (Component Targeting) drops the "(if exposed)" qualifier on "Vehicle crew" — redundant with the rule's own "visible" requirement, which already excludes anything not exposed.
- **REVIEW-005 applied, with a modification** — `MEL-010` added no rule beyond `MEL-002` (confirmed correct by the reviewer), but rather than deleting the ID outright (the reviewer's literal suggestion), it's repurposed to an explicit "merged into MEL-002" marker — this repo's established convention is that rule IDs are never silently deleted; see Decisions below.
- **REVIEW-006 applied** — `MEL-012` (Interaction with Combat Rules) simplified from a three-item list of what melee still defines to one direct sentence: "This document only defines how melee weapons generate Attack Dice. Everything after that belongs to the standard combat system."
- **REVIEW-001 rejected** — the review suggested melee should generate an "Impact attempt" instead of an "Attack Die," reasoning that "dice already belong to the Combat System." This is incorrect relative to the shipped architecture: `10-weapons.md` WPN-006 (ranged) already defines Attack Dice *count* as a weapon-construction concern, with only dice *resolution* (the 4/5/6 threshold) belonging to the Combat/Damage System. `MEL-003` already mirrors that exact split. Applying REVIEW-001 would have made melee use different vocabulary ("Impact attempt") than ranged uses for the identical concept ("Attack Die") — introducing a new terminology inconsistency instead of removing one.
- **REVIEW-007, REVIEW-008** — praise only (the Design Philosophy flow diagram, and the "Delivery Method" unification framing), no concrete edit requested; no action taken.

## Capabilities

### Modified Capabilities
(none — this is purely editorial wording on an un-formalized document; no capability's normative requirement text changes)

## Impact

- `docs/12-melee.md`: `MEL-002`, `MEL-010`, `MEL-012`, `MEL-013`, `MEL-014` edited. No rule ID added, removed, or renumbered.
- No change to any measured rule value, dice mechanic, or resolution sequence — purely editorial tightening, plus one explicit rejection with documented reasoning.
