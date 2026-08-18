## Why

`docs/11-combat.md` `CBT-008` (Defender Resolution) hands responsibility for an Impact to the Component Damage System but never states who performs the resulting physical model change. For a unit or vehicle, that is implicitly the defending player, because they control the model. A target with no controlling player — most commonly a structure placed by a scenario rather than brought by a player as part of their army (`TODO.md`, "Structures") — has nobody assigned. GitHub issue #107 asks for the assignment to be stated.

## What Changes

- `CBT-008` gains one clarifying addition: when a targeted component has no controlling player, the attacking player resolves it through the Component Damage System — including the Damage Roll — and physically applies the resulting damage. The rest of `CBT-008`'s hand-off to `16-damage-system.md` is unchanged.
- `16-damage-system.md` `DMG-015` (Damage Roll) is the one step that names an actor ("the defender rolls one D6"). It gains a short cross-reference to `CBT-008` for the same exception, so a reader following `CBT-008`'s hand-off does not arrive at a sentence naming an actor that does not exist for their target.
- `CBT-001` step 7 and `10-weapons.md` `WPN-013`, which both paraphrase the Attack Sequence, currently say "defender resolves Impacts." Both drop the named actor ("Resolve Impacts" / "resolve Impacts") — they already function as a table of contents pointing at `CBT-008`, which is where the actor question is answered, and naming the actor twice is what would go stale.
- The `damage-resolution` capability's tracked `Damage Roll` requirement is modified to match (delta below) — it currently states "the defender SHALL roll one D6" with no exception. This delta is written complete against `docs/`: both the corrected `Operational`/`Wounded`/`Dead` state names and the actor exception. A concurrent proposal, `damage-resolution-drops-legacy-state-names`, also modifies the same requirement (that state-name correction, unrelated to this change) — see `design.md` ("Known interaction with a concurrent proposal") for why reconciling the two is a separate change, not a task here.
- No other damage mechanic changes. Impact generation, the Geometry Check, Resistance, Penetration, and Component State Change all read exactly as `16-damage-system.md` already states them.

`tasks.md` section 5 carries four repairs from the audit of the applied text: `docs/12-melee.md`'s own "the defender resolves" statement is brought in line with its actor-neutral siblings, `CBT-008` and `DMG-015` are reworded so the "no controlling player" condition is stated once (at `CBT-008`, at component granularity, since that is where `DMG-015`'s Damage Roll and a Penetration chain actually operate) and only pointed at from `DMG-015`, and `02-core-rules.md` `CORE-005` gains the one sentence stating which structures have a controlling player — a condition `CBT-008` now leans on that nothing previously defined.

## Capabilities

### New Capabilities

(none)

### Modified Capabilities

- `damage-resolution`: the `Damage Roll` requirement's actor changes from "the defender" (unqualified) to "the defender, or the attacker when the target component has no controlling player." No dice threshold changes. The delta is written complete against `docs/`, so it also carries the `Operational`/`Wounded`/`Dead` state-name correction a concurrent proposal separately targets (see What Changes, above, and `design.md`) — no other requirement in this capability changes.

## Impact

- `docs/11-combat.md`: `CBT-008` and `CBT-001` (step 7 only) edited. No rule ID added, removed, or renumbered.
- `docs/16-damage-system.md`: `DMG-015` edited (one clause added).
- `docs/10-weapons.md`: `WPN-013` edited (two words, to stay consistent with `CBT-001`).
- `docs/12-melee.md`: its Purpose statement edited (`tasks.md`, section 5).
- `docs/02-core-rules.md`: `CORE-005` gains one sentence (`tasks.md`, section 5).
- `openspec/specs/damage-resolution/spec.md`: one `MODIFIED` delta, `Damage Roll` requirement.
- No change to any dice threshold, state name in `docs/`, or resolution order.

## Deliberately left as written

Two places state "the defender resolves" as general framing rather than as the operative rule, and are not the citation target for this exception — `CBT-008` is:

- `docs/11-combat.md`, Design Philosophy ("The attacker produces impacts." / "The defender resolves them.") — states the default-case rationale for the two-system split.
- `docs/16-damage-system.md`, `DMG-014` ("No dice are rolled by the defender.") — states an absence that holds regardless of which player would have rolled.

`docs/12-melee.md`'s own "The defender resolves those Impacts…" was originally grouped with these two, but its sibling statements in `docs/01-foundations.md` and `CODE_OF_DESIGN.md` Principle 5 already say "the target resolves" — `12-melee.md` was the one outlier, not a third register choice, so it is corrected in `tasks.md` section 5 rather than left standing.
