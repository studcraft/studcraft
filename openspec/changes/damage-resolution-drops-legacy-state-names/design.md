# Design — Damage resolution drops legacy state names

## Why a delta, and not a hand edit of `openspec/specs/`

The tempting shortcut is to open `openspec/specs/damage-resolution/spec.md` and fix the three lines directly — it is a two-word substitution repeated a few times, not a design decision. That shortcut is refused for a mechanical reason before it is refused for a procedural one:

`openspec/specs/` is shared state, written only by the Archive cut (`system/workflow.md`, Archiving). `.claude/hooks/guard_repo_edits.py` refuses a `Write` or `Edit` under `openspec/specs/` from any branch that is not `archive/*`, and the `OpenSpec archive must be separate from apply` CI gate refuses the same thing at PR time — any PR not from an `archive/*` branch that touches `openspec/specs/` is rejected outright. This branch is `damage-resolution-drops-legacy-state-names`, not `archive/*`, so a direct edit would be refused locally and again in CI even before the procedural argument applies.

The procedural reason is the same one every other correction in this repository follows: `openspec/specs/` reflects `docs/` only through the Archive cut applying a change's `MODIFIED` delta. There is no other path that keeps the two in sync, and inventing one for "this edit is small" would be the same shortcut that produced the four-deltas-disagreeing failure `system/workflow.md` records under "Archive close to the merge, not in batches of seventeen." A one-line fix is still a fix, and it still goes through the delta.

This proposal is unusual only in that its delta corrects a **spec-vs-spec** disagreement rather than a **spec-vs-docs** one — the ruleset (`docs/16-damage-system.md`) has been consistent throughout; `openspec/specs/damage-resolution/spec.md` is what drifted, evidently left over from before `DMG-005`'s current names were adopted. That does not change which mechanism applies: the delta is still the only sanctioned way to change what `openspec/specs/` holds, whether the correction target is `docs/` or the spec's own internal consistency.

## Why the scenario names stay as they are

Two scenarios in the *Repairs* requirement name the state they describe: `Repairing a touched component` and `Destroyed components cannot be repaired`. Both headings use the legacy vocabulary this change removes from the requirement bodies, and both are left exactly as written.

`system/workflow.md` ("Scenario names are identifiers") is explicit about why: a `#### Scenario:` heading is matched by name, not reparsed for meaning. `scripts/check_delta_coverage.py` and `openspec archive` both compare scenario headings verbatim against the living spec's set — a `MODIFIED` block that renamed either heading would be indistinguishable from deleting the old scenario and adding a new one, and the archive tool refuses that on sight. The ruleset itself already follows the same convention for rule IDs (`MEL-010`, `CBT-011` in `system/workflow.md`'s own example); a scenario heading is the same kind of stable identifier at the OpenSpec layer.

So the fix is scoped exactly the way `wounded-degrades-capability` scoped its own scenario-body corrections: change what the sentence *says*, never what the heading *is called*. `Repairing a touched component` still means "repairing a component in the state now called `Wounded`" — the heading was never a restatement of the state name in the first place, just a paraphrase ("touched" was descriptive prose even under the old vocabulary, not itself one of `OK`/`TOUCHED`/`DESTROYED`), so nothing about it needs to change to stay accurate.

## Why both requirements are corrected together, in one delta

*Damage Roll* and *Repairs* are both `MODIFIED` in the same `specs/damage-resolution/spec.md` file rather than split across two changes. They share one root cause (both were written against the pre-`DMG-005` vocabulary and never updated when `Attack Roll` was), one capability, and one file — splitting them would produce two changes racing to modify overlapping context in the same living spec for no benefit, the exact shape `system/workflow.md` warns against under "When several changes modified the same requirement."
