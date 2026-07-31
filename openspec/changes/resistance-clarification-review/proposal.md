## Why

`delete-me-comments.md` is an external review of the Damage System's Resistance measurement, raising six points (REVIEW-001 through REVIEW-006). Checked against the current shipped ruleset, five of the six are already fully implemented — by `full-audit-repairs` (A-02: Resistance measured in plate layers, brick = 3 plates), `audit-round2-repairs` (R-01: the fixed-piece exception for minifigs), and `remove-materials-document` (SCS-023 already routes transparent-component Resistance through the universal Geometry Check, no material table). The reviewer appears to have evaluated a version of the ruleset that predates those three changes, or arrived at the same conclusions independently.

The one item not already covered is a genuine, if small, opportunity: `DMG-004`'s worked examples (Minifig, Mounted Cannon, Shield/Bricks, Shield/Plates) don't yet include a multi-brick case (the reviewer's suggested "Bunker, 2 Bricks thick, Resistance 6") or a transparent-component case, both of which would make the already-correct general rule more immediately obvious to a reader, per the reviewer's own stated goal for REVIEW-003.

## What Changes

**Confirmed already implemented (no action needed), with the current text cited for each:**
- **REVIEW-001 (Define the Structural Unit)**: `DMG-003` already states "measured in plate layers (the finest LEGO unit of height) — a standard brick is 3 plates tall."
- **REVIEW-002 (Bricks and Plates Become Equivalent)**: same `DMG-003` sentence, demonstrated concretely by `DMG-004` Example 3 (a brick-built shield resolves to Resistance 3, the same 3-plate-layer count a plate-built equivalent would).
- **REVIEW-004 (Transparent Components Should Follow Geometry)**: `docs/04-construction-standard.md` SCS-023 already states "Resistance and the Geometry Check... determine whether they stop an Impact — the same as any other component." No material-specific transparency table exists anywhere in the current ruleset (removed along with `13-materials.md`).
- **REVIEW-005 (Penetration Already Handles Multiple Transparent Layers)**: `DMG-017` (Penetration) is already fully generic — it doesn't special-case transparency, glass, or any component type. Multiple transparent components in sequence already resolve as independent components under the existing rule; this needs no addition, matching the reviewer's own conclusion ("No additional transparency rules are required").
- **REVIEW-006 (Remove Material-Based Resistance)**: `DMG-008` ("No Material-Specific Mechanics") already states this as its own dedicated rule: "StudCraft does not define material-specific hit thresholds, Resistance modifiers, or damage tables of any kind."

**Proposed addition (REVIEW-003, partially open):**
- `docs/16-damage-system.md` DMG-004: add two illustrative examples — a multi-brick case (matching the reviewer's "Bunker" suggestion: 2 bricks thick → Resistance 6) and a transparent-component case (a window built 1 plate thick → Resistance 1, same as any other 1-plate component) — to make the already-correct general rule more immediately obvious without restating it. These are additive only: no existing example's value changes, and no new mechanic is introduced.

## Impact

- No mechanical change. This proposal is confirmation-plus-illustration, not a rule change — the five already-implemented items get no diff at all; the sixth gets two additional worked examples in `DMG-004`.
- Not yet applied — the user asked for the proposal only this round.
