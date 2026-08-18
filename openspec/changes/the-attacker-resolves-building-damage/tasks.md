# Tasks — The attacker resolves building damage

## How to apply this change

Every anchor below is pre-change text, checked with exact-substring matching and occurring **exactly once in the file its task names**. Replace the whole anchor.

If an anchor returns anything other than 1, **stop and report it** rather than guessing which occurrence was meant. Never edit a document to make a verification command pass — report the mismatch instead.

The triple-backtick fence marks where the text starts and stops. **The fence is not part of the text** — do not write the backticks into the document.

**No rule ID is added, removed, or renumbered.**

- [x] 0.1 The branch is `the-attacker-resolves-building-damage`, named for this change directory, and it is branched from an up-to-date `main`.

### Coverage

| `proposal.md` item | Task | Path |
|---|---|---|
| `CBT-008` gains the "no controlling player" paragraph | 1.1 | `docs/11-combat.md` |
| `CBT-001` step 7 stops naming an actor | 1.2 | `docs/11-combat.md` |
| `WPN-013` stops naming an actor, stays consistent with `CBT-001` | 2.1 | `docs/10-weapons.md` |
| `DMG-015` cross-references `CBT-008`'s exception | 3.1 | `docs/16-damage-system.md` |
| `damage-resolution`'s `Damage Roll` requirement, `MODIFIED` delta — complete against `docs/` (`design.md`, "Known interaction with a concurrent proposal") | — | `specs/damage-resolution/spec.md` (this change directory; no task — the file is the deliverable) |
| `docs/12-melee.md` Purpose stops naming an actor (audit repair) | 5.1 | `docs/12-melee.md` |
| `CBT-008`'s condition restated at component granularity (audit repair) | 5.2 | `docs/11-combat.md` |
| `DMG-015` reduced to a pointer, condition stated once (audit repair) | 5.3 | `docs/16-damage-system.md` |
| `CORE-005` states which structures have a controlling player (audit repair) | 5.4 | `docs/02-core-rules.md` |

**Untouched, deliberately** (`design.md`, "Two 'the defender resolves' statements are left as written; a third turned out not to belong on this list"): `docs/11-combat.md` Design Philosophy, `docs/16-damage-system.md` `DMG-014`. `CBT-008`'s heading stays "Defender Resolution" — it names the rule's default case; the added paragraph states the cited exception within the same rule.

**Not touched, deliberately:** `openspec/changes/damage-resolution-drops-legacy-state-names/`. It also modifies `damage-resolution`'s `Damage Roll` requirement (a state-name correction), and this change's own delta already carries that correction alongside the actor exception — but reconciling the two changes' deltas (moving the sibling's to `specs-superseded/`) is its own change, on its own branch, per `Docs require OpenSpec proposal`'s one-proposal-per-PR rule. `design.md` ("Known interaction with a concurrent proposal") records why and what that follow-up change needs to do.

---

## 1. `docs/11-combat.md`

- [x] 1.1 In `CBT-008`, replace this anchor:

```
After counting successful Impacts, responsibility passes to the Component Damage System (`16-damage-system.md`), which determines how each Impact affects the targeted component (see the Combat Flow diagram below for the full step sequence).
```

with:

```
After counting successful Impacts, responsibility passes to the Component Damage System (`16-damage-system.md`), which determines how each Impact affects the targeted component (see the Combat Flow diagram below for the full step sequence).

When the target has no controlling player — for example, a structure placed by a scenario (`02-core-rules.md`, CORE-005) — the attacking player resolves the Impacts through the Component Damage System, including the Damage Roll (`16-damage-system.md`, DMG-015), and physically applies the resulting damage.
```

  The first paragraph is unchanged and is the anchor's landmark. The added second paragraph triggers on the absence of a controlling player, not on the target being a building — `TODO.md` ("Structures") already contemplates a structure a player brings as part of their army, which keeps `CBT-008`'s default for it (`design.md`, "The trigger is 'no controlling player'").

- [x] 1.2 In `CBT-001`, replace this anchor — the numbered list item:

```
7. Defender resolves Impacts.
```

with:

```
7. Resolve Impacts.
```

  Matches the imperative, actor-free phrasing of every other step in the list (`Declare the weapon system.`, `Verify Line of Sight.`, `Count successful Impacts.`, `Update the LEGO model.`). The list is a named-step index into `CBT-002` through `CBT-009` by position; `CBT-008` is where the actor question is answered, and task 1.1 is what answers it.

---

## 2. `docs/10-weapons.md`

- [x] 2.1 In `WPN-013`, replace this anchor:

```
Resolving a ranged attack follows the universal Attack Sequence defined in `11-combat.md` (CBT-001): declare weapon, declare target, verify Line of Sight, verify Range, roll Attack Dice, count Impacts, defender resolves Impacts, update the model.
```

with:

```
Resolving a ranged attack follows the universal Attack Sequence defined in `11-combat.md` (CBT-001): declare weapon, declare target, verify Line of Sight, verify Range, roll Attack Dice, count Impacts, resolve Impacts, update the model.
```

  One paraphrase of `CBT-001`'s step 7, kept in step with task 1.2's wording so the two lists do not diverge.

---

## 3. `docs/16-damage-system.md`

- [x] 3.1 In `DMG-015`, replace this anchor:

```
The defender rolls one D6 for that impact.
```

with:

```
The defender — or the attacker, when the target has no controlling player (`11-combat.md`, CBT-008) — rolls one D6 for that impact.
```

  A one-directional cross-reference: `CBT-008` states and cites the "no controlling player" condition, `DMG-015` only points at it, the same pattern `DMG-006`/`CBT-009` already use. The rest of `DMG-015` — the 4-5-6/1-2-3 thresholds and the state names — is untouched.

---

## 4. Verification

- [x] 4.1 `grep -c -F "When the target has no controlling player" docs/11-combat.md` returns `1`. It returned `0` before task 1.1.

- [x] 4.2 `grep -c -F "7. Resolve Impacts." docs/11-combat.md` returns `1`.

- [x] 4.3 `grep -c -F "Defender resolves Impacts" docs/11-combat.md` returns `0`.

- [x] 4.4 `grep -c -F "count Impacts, resolve Impacts, update the model" docs/10-weapons.md` returns `1`.

- [x] 4.5 `grep -c -F "or the attacker, when the target has no controlling player" docs/16-damage-system.md` returns `1`.

- [x] 4.6 `python3 scripts/preflight.py` passes.

---

## 5. Repairs from the audit of the applied text

Four edits from the `ruleset-auditor` review of sections 1–4 as applied. **Their anchors are post-change text** — each names a sentence sections 1–3 already put there, or a sibling sentence sections 1–3 left standing. Apply after section 4, not before.

- [x] 5.1 In `docs/12-melee.md`, replace this anchor:

```
The defender resolves those Impacts using the Component Damage System (`16-damage-system.md`).
```

with:

```
The target resolves those Impacts using the Component Damage System (`16-damage-system.md`).
```

  Matches `docs/01-foundations.md` ("The target resolves those Impacts according to its construction") and `CODE_OF_DESIGN.md` Principle 5 ("The target resolves those Impacts according to its components' construction") — both already actor-neutral. `docs/12-melee.md`'s own Purpose was the one sentence among these four parallel statements still naming "the defender", which task 1.1 makes untrue for a target with no controlling player.

- [x] 5.2 In `docs/11-combat.md`, `CBT-008`, replace this anchor — the sentence task 1.1 added:

```
When the target has no controlling player — for example, a structure placed by a scenario (`02-core-rules.md`, CORE-005) — the attacking player resolves the Impacts through the Component Damage System, including the Damage Roll (`16-damage-system.md`, DMG-015), and physically applies the resulting damage.
```

with:

```
When a targeted component has no controlling player — for example, a component of a structure placed by a scenario (`02-core-rules.md`, CORE-005) — the attacking player resolves it through the Component Damage System, including the Damage Roll (`16-damage-system.md`, DMG-015), and physically applies the resulting damage.
```

  "The target" is model-level (`CBT-001` step 2, "Declare the target"); the Damage Roll this sentence hands to `DMG-015` is made per component (`16-damage-system.md`, "Select Target Component"), and `DMG-017` (Penetration) can carry one Impact through components across a control boundary — the shield-then-minifig example is one model, but nothing stops a chain from a scenario structure's wall into a player's unit standing behind it. Stating the condition at component granularity, using "targeted component" — the same phrase `CBT-008`'s first, unchanged paragraph already uses — resolves the roll the same way regardless of which model started the attack.

- [x] 5.3 In `docs/16-damage-system.md`, `DMG-015`, replace this anchor — the rule's first sentence:

```
The defender — or the attacker, when the target has no controlling player (`11-combat.md`, CBT-008) — rolls one D6 for that impact.
```

with:

```
The defender — or the attacker, where `11-combat.md` (CBT-008) directs — rolls one D6 for that impact.
```

  `CBT-008` (as task 5.2 leaves it) is the sole statement of the "no controlling player" condition; `DMG-015` now only points at it instead of restating it, the same one-directional pattern `DMG-006`/`CBT-009` use. A future refinement of what counts as "no controlling player" — `TODO.md` ("Structures") already has one pending — then changes one sentence, not two.

- [x] 5.4 In `docs/02-core-rules.md`, `CORE-005`, replace this anchor — the rule's first sentence:

```
Buildings, fortifications and scenery are permanent battlefield elements.
```

with:

```
Buildings, fortifications and scenery are permanent battlefield elements.

A structure a player brings as part of their army is controlled by that player, like any other model; a structure placed by the scenario has no controlling player (`11-combat.md`, CBT-008).
```

  `CBT-008` (task 5.2) makes "no controlling player" a condition that selects between two resolution procedures, and nothing in `docs/` said which structures have one before this sentence. `TODO.md` ("Structures") already distinguishes a scenario-placed structure from one "brought by a player as part of their army"; this states the distinction as a rule rather than leaving it implicit in an open item. The open item itself — whole-structure damage, Deployment Volume occupation for a scenario-placed structure — is untouched.

## 6. Verification of the repairs

- [x] 6.1 `grep -c -F "The target resolves those Impacts using the Component Damage System" docs/12-melee.md` returns `1`, and `grep -c -F "The defender resolves those Impacts" docs/12-melee.md` returns `0`.

- [x] 6.2 `grep -c -F "When a targeted component has no controlling player" docs/11-combat.md` returns `1`.

- [x] 6.3 `grep -c -F "where \`11-combat.md\` (CBT-008) directs" docs/16-damage-system.md` returns `1`, and `grep -c -F "when the target has no controlling player" docs/16-damage-system.md` returns `0`.

- [x] 6.4 `grep -c -F "a structure placed by the scenario has no controlling player" docs/02-core-rules.md` returns `1`.

- [x] 6.5 `python3 scripts/preflight.py` passes.
