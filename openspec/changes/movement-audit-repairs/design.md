## Context

`docs/07-movement.md` is the last core system never audited. Two earlier passes touched it only where another document forced them to — the round-2 audit added `MOVE-004`'s AP cost and its grid-alignment justification, and `MOVE-016` gained a falling-damage exception when the damage system changed. Neither looked at the document as a whole.

Doing so surfaced sixteen defects, and almost all of them trace to one root: forward movement was written informally and side movement was written precisely, and the two were never reconciled.

## Decisions

### Forward movement is quantised to 3 studs, not left continuous

Two readings could resolve the `MOVE-004` / `MOVE-007` contradiction.

**Continuous** — forward movement is any distance up to 12 studs. This keeps `MOVE-007`'s "Forward 8 studs" example legal and changes nothing mechanically, but it requires deleting `MOVE-004`'s justification paragraph, which explicitly claims forward movement is "aligned with the grid the same way side movement is". Side movement is quantised, so that sentence asserts quantisation.

**Quantised** — forward and backward move in multiples of 3, the Unit Base's depth, exactly as side movement uses multiples of 4, its width. This is what `MOVE-004` already claims, makes the two axes symmetric, and derives both numbers from the base rather than from convention.

Quantised is chosen. It is the reading the document already asserts, and it means every movement number in the game comes from the Unit Base's own dimensions — 12 studs is four base-depths forward or three base-widths sideways, and a player can measure either by laying spare bases end to end, which is the stated Design Philosophy ("free from templates and measuring sticks").

The cost is that `MOVE-007`'s example becomes illegal and must change from 8 studs to 6. That is a two-character edit to an example, against a rule-level inconsistency that would otherwise persist.

### Obstacle heights move to plate layers

`MOVE-009` through `MOVE-011` set thresholds at 1, 2, and 3+ bricks. Nothing covers an obstacle built from plates, and a 4-plate wall — taller than one brick, shorter than two — currently has no rule at all.

`16-damage-system.md` (DMG-003) already faced this and settled on plate layers with a brick counting as 3. Restating the movement thresholds in the same unit closes the gap and removes the last place in the ruleset where a height is measured in a different unit than everywhere else.

Thresholds are unchanged in effect: what was "1 brick" is "up to 3 plate layers", "2 bricks" is "4 to 6", "3 bricks or more" is "7 or more". Every previously legal build resolves exactly as before; builds that had no answer now have one.

### Collision and the three terrain sections get rule IDs

`Collision`, `Doors`, `Ramps` and `Interactive Terrain` are normative — "enemy units block movement" decides games — but carry no identifier, so no other document can cite them. `08-vehicles.md` already cites `MOVE-008` by ID; there is no equivalent handle for collision.

There is precedent for unnumbered normative text (`02-core-rules.md`'s "Universal Rule" sets the rule-priority order and has no ID), so this is a judgement call rather than a violation. It goes the other way here because collision is the more likely thing for a future vehicle or transport rule to need to reference, and because promoting them is additive — `MOVE-017` through `MOVE-020` are new IDs, and nothing is renumbered.

### The three AP-cost restatements are trimmed, not deleted

`Doors`, `Ramps` and `Interactive Terrain` each restate CORE-007's 1 AP. The cost is removed from all three, but the sections stay, because each carries movement-specific content CORE-007 does not: a closed door blocks movement, a lowered ramp becomes valid terrain, and a movable element can become part of a movement path. Deleting the sections outright would lose that; deleting only the duplicated cost keeps one source of truth without losing content.

## Risks / Trade-offs

- **This is a mechanical change, unlike the recent editorial passes.** Forward granularity and the side-movement cap change what is legal at the table. Both tighten rather than loosen, and the uncapped sidestep being closed is almost certainly a fix rather than a nerf, but it deserves playtesting attention in a way the documentation fixes did not.
- **Quantised forward movement adds a constraint players must remember.** Mitigated by symmetry: the rule is "multiples of your base's dimension in that direction", one idea covering both axes, rather than two unrelated numbers.
- **Four new rule IDs in one change.** Each wraps text that already exists and is already being followed, so nothing new must be learned — but the diff will look larger than the change is.
- **No spec delta**, so this change cannot be verified against a capability. Accepted deliberately: creating a `movement` capability means specifying all twenty rules, and doing that inside an audit-repair change would bury the repairs.

## Open Questions

None. Not applied — proposal only.
