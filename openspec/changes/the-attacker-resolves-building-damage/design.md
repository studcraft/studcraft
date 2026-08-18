## Context

GitHub issue #107. `CBT-008` (Defender Resolution) hands an Impact to the Component Damage System but assumes a defending player exists to carry it out and to apply the resulting physical change. That assumption holds for a unit or vehicle. It does not hold for every building: `TODO.md` ("Structures") already distinguishes "a structure placed by a scenario" from one "brought by a player as part of their army" — so a building can have a controlling player, and the assignment this change makes has to key on that, not on the target's type.

## Goals / Non-Goals

**Goals:**
- State who resolves and physically applies damage when the target has no controlling player, using the Component Damage System `CBT-008` already cites.
- Leave no unqualified "the defender…" statement standing where a reader would arrive at it by following `CBT-008`'s own hand-off.

**Non-Goals:**
- No new damage system, geometry rule, or resistance rule for buildings. `16-damage-system.md` already applies to any component regardless of who controls it (`component-damage` capability, "Geometry Defines Resistance").
- No mechanism for a player-brought structure, and no change to how Deployment Volume or army composition works. That gap is `TODO.md`'s ("Structures"), not this change's.
- No new rules term. "Structure" is `02-core-rules.md` `CORE-005`'s own word for buildings, fortifications and scenery; nothing here introduces a synonym for it.

## Decisions

### The trigger is "no controlling player," not "target is a building"

The issue's own rationale is "a building or other field structure has no defending player — it belongs to the table, not to either side." A first draft of this change keyed the new sentence on the target being a building, which is a stronger claim than that rationale supports: `TODO.md` explicitly contemplates a structure a player brings as part of their army, and for that structure a defending player exists and `CBT-008`'s default applies unchanged. Keying on "no controlling player" instead — with a scenario-placed structure as the example, cited to `CORE-005` — matches the actual reason and does not override `CBT-008`, `CBT-001` step 7, or `DMG-015` for a case the issue never intended to touch.

### "Resolves the Impacts," not only "applies the resulting damage" — so `DMG-015` has to change too

The issue's suggested wording says the attacker "resolves the Impacts through the Component Damage System and physically applies the resulting damage," and separately walks the full procedure — Select Target Component, Geometry Check, Damage Roll, Component State Change, Penetration — as what the attacker follows. For a target with no controlling player, nobody else is available to make the Damage Roll (`DMG-015`) either; limiting this change to the final physical step would leave that roll unassigned. `DMG-015` is the one step in `16-damage-system.md` that names an actor, so it is the one step this change has to touch — intended as a cross-reference to `CBT-008` rather than a restatement of the "no controlling player" condition there, the same one-directional citation pattern `DMG-006`/`CBT-009` already use ("`CBT-009` points here instead of restating it"). The first applied version restated the condition anyway; "Component-level granularity, and one condition stated once" below is the correction.

This is also why `damage-resolution`'s tracked `Damage Roll` requirement needs a `MODIFIED` delta: it states "the defender SHALL roll one D6" with no exception, and this change makes that no longer universally true. `system/proposal-review.md` ("Delta vs. Direct Edit") is explicit that a tracked capability's requirement is not edited without one.

### `CBT-001` step 7 and `WPN-013` stop naming an actor, rather than restating the exception

Both are paraphrases of the Attack Sequence, not the operative rule. `CBT-001`'s eight steps already function as a named-step index into `CBT-002` through `CBT-009` by position — none of the other seven names an actor, and step 7 doing so is what breaks under the new exception. Rewording it to "Resolve Impacts" (matching the imperative, actor-free phrasing of every other step) and `WPN-013`'s matching fragment to "resolve Impacts" removes the false claim without duplicating `CBT-008`'s condition in a second place — consistent with `system/documentation-standards.md`, "reuse existing terminology," and with one owner per rule.

### Two "the defender resolves" statements are left as written; a third turned out not to belong on this list

`docs/11-combat.md`'s Design Philosophy and `16-damage-system.md`'s `DMG-014` ("No dice are rolled by the defender") use "the defender" in a role that is not the operative citation target for this exception:

- The Philosophy statement describes the *default* two-system split's rationale ("keeps weapon rules simple while allowing targets to behave differently") — the same register as `CBT-001`'s own "every attack follows the same procedure," which a later sentence qualifies for melee without rewriting the Philosophy section. `CBT-008` is where the actual mechanism, and its exception, live.
- `DMG-014`'s statement is an absence ("no dice are rolled"), true regardless of which player would have rolled had the Geometry Check passed. Nothing in this change makes it false.

`docs/12-melee.md`'s Purpose statement ("The defender resolves those Impacts using the Component Damage System") was grouped with these two originally, on the same reasoning. The `ruleset-auditor` review of the applied text caught the actual difference: `docs/01-foundations.md` and `CODE_OF_DESIGN.md` Principle 5 state the identical idea as "the target resolves those Impacts" — actor-neutral, not a register choice — so `12-melee.md` was the one place that had drifted, not a third legitimate framing. Corrected in `tasks.md` section 5 (task 5.1) rather than left standing.

### Component-level granularity, and one condition stated once

The applied text initially stated "no controlling player" as a property of *the target* (`CBT-008`) and then restated it, verbatim, in `DMG-015` — both defeating the one-directional citation pattern this change intended (`DMG-006`/`CBT-009`) and picking the wrong granularity: `DMG-015`'s Damage Roll and `DMG-017`'s Penetration both operate per *component*, and Penetration can carry one Impact across a control boundary (a scenario structure's wall into a player's unit standing behind it). `tasks.md` section 5 (tasks 5.2–5.3) restates `CBT-008`'s condition as "a targeted component has no controlling player" — reusing `CBT-008`'s own first-paragraph phrase — and reduces `DMG-015` to a bare pointer at `CBT-008`. The condition now lives in exactly one place, at the granularity where it is actually evaluated.

### `CORE-005` states which structures have a controlling player

`CBT-008` makes "no controlling player" a condition selecting between two resolution procedures. Nothing in `docs/` said which structures have one — `TODO.md` ("Structures") carries the distinction (scenario-placed versus "brought by a player as part of their army") but only as an open item about Deployment Volume accounting, not as a stated rule. `tasks.md` section 5 (task 5.4) adds one sentence to `CORE-005` stating the distinction as a rule. The open item itself — whole-structure damage, Deployment Volume occupation for a scenario-placed structure — is untouched; only "who controls it" is settled.

### No glossary entry

`docs/14-glossary.md`'s obligation for a rule edit, not a new document, is `system/proposal-review.md`'s "The Summary Is Part of the Rule" — check the Summary and glossary against the edited rule, not add an entry by default. Checked both: `docs/11-combat.md`'s Summary ("The target determines everything else") stays true, and the glossary's `Impact` entry ("Targets resolve Impacts using the Component Damage System") is already target-neutral and stays true. No new term ships — "structure" is `CORE-005`'s existing word. "Controlling player" is not a new term either, but it does take on a new, load-bearing role as a rule trigger; `CORE-005` (task 5.4) states what it means for a structure rather than adding a glossary entry, since the definition is short, single-sourced, and belongs beside the rule that already names the category.

### Known interaction with a concurrent proposal — flagged here, not resolved in this branch

`openspec/changes/damage-resolution-drops-legacy-state-names/` also modifies `damage-resolution`'s `Damage Roll` requirement, correcting its stale `OK`/`TOUCHED`/`DESTROYED` state names to `Operational`/`Wounded`/`Dead`. Discovered during this change's own audit, before either change archived: two deltas for the same requirement would clobber each other regardless of archive order (`system/workflow.md`, "When several changes modified the same requirement").

This change's own delta is written complete against `docs/` — both the corrected state names and the actor exception — so it is correct standing alone and is the natural candidate to become the requirement's authoritative version. It does **not**, however, move `damage-resolution-drops-legacy-state-names`'s own `Damage Roll` delta to that change's `specs-superseded/` — `Docs require OpenSpec proposal` enforces one proposal per pull request, on its own branch (`openspec/config.yaml`), and that move touches a second change directory. Reconciling the two — including the `specs-superseded/` relocation `system/workflow.md` describes — is a separate, dedicated change against `damage-resolution-drops-legacy-state-names`'s own branch, not a task this proposal can carry. Flagged here so it is not rediscovered cold at the next Archive cut.

**Whether a batch containing both is safe before that reconciliation lands:** because this delta is a superset of the sibling's post-state (not an alternative to it), only one of the three possible archive orders is unsafe. Both in the same batch, or the sibling alone first, both leave the living spec's `Damage Roll` correct — `scripts/archive_cut.py` processes a batch in directory order with no dependency resolution (`system/workflow.md`, "When several changes modified the same requirement"), and `damage-resolution-drops-legacy-state-names` sorts before `the-attacker-resolves-building-damage`, so this change's superset body lands on top either way. Only this change archiving alone, first, is unsafe: the living spec would then gain a third `Damage Roll` scenario the sibling's still-active two-scenario delta does not carry, and `scripts/check_delta_coverage.py` ("Deltas must not drop scenarios"), which `preflight.py` runs over every active change, refuses that loudly rather than letting it merge silently.

## Risks / Trade-offs

[Two proposals modify `damage-resolution`'s `Damage Roll` requirement concurrently, and this change cannot reconcile them itself — the fix touches a second change directory, which `Docs require OpenSpec proposal` refuses in one PR] → open a small, separate change against `damage-resolution-drops-legacy-state-names` before either archives, moving its `Damage Roll` delta to `specs-superseded/` in favour of this one's. Noted here so it is not rediscovered cold at batch time.

## Open Questions

None outstanding.
