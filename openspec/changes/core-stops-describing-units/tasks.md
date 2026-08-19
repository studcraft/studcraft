# Tasks — CORE stops describing units

## How to apply this change

Every anchor below was checked with exact-substring matching against the pre-change files and occurs **exactly once in the file its task names**. Replace the whole anchor.

If an anchor returns anything other than 1, **stop and report it** rather than guessing which occurrence was meant. Never edit a document to make a verification command pass — report the mismatch instead.

### How to read the replacement blocks

The triple-backtick fence marks where the text starts and stops. **The fence is not part of the text** — do not write the backticks into the document.

A `#` heading or a `---` horizontal rule inside a fence is real markdown that must land in the file as markdown, not as quoted text. Task 5.1 runs from one heading to the next and repeats the second as a **landmark** — a line that must stay in the file, not an edit.

### The two things this change must not do

**`CORE-015` is deleted outright and its number is retired.** Do not renumber `CORE-016` into the gap, and do not leave a stub saying a rule used to be there — `system/documentation-standards.md` (Naming Conventions).

**No gameplay value changes.** The Unit Base stays `4 × 3 × 13`. An infantry base stays `4 × 3` studs and one plate. The 4-stud edge stays the front. A shield stays one-handed and a rifle two-handed. If a replacement block would alter any of those, it is wrong — stop and report it.

- [x] 0.1 The branch is `core-stops-describing-units`, named for this change directory, and it is branched from an up-to-date `main`.

### Scope and coverage

Five ruleset documents, no spec delta: **ten anchor pairs and ten verification tasks** (6.1 – 6.10). **Sections 7 and 8 change both figures** — 7 adds two documents and eight pairs from the audit of the applied text, 8 adds one more document, three pairs and the change's only capability delta. Twenty-one pairs across eight documents in total; each section carries its own coverage note.

| `proposal.md` item | Task | Path |
|---|---|---|
| `CORE-001` — the infantry-base sentence | 1.1 | `docs/02-core-rules.md` |
| `CORE-002` — the per-domain split and the list | 2.1 | `docs/02-core-rules.md` |
| `CORE-004` — reworded to match `CORE-003` | 3.1 | `docs/02-core-rules.md` |
| `CORE-009` — the reaction-fire sentence | 4.1 | `docs/02-core-rules.md` |
| `CORE-015` — retired | 5.1 | `docs/02-core-rules.md` |
| `INF-001` — states its base, its front and its hands | 1.2 | `docs/17-infantry.md` |
| `17-infantry.md` — Summary item 1 | 1.3 | `docs/17-infantry.md` |
| `CMP-014` — owns the shield's hand | 5.2 | `docs/05-construction-components.md` |
| `WPN-010` — owns weapon handedness | 5.3 | `docs/10-weapons.md` |
| Glossary ***Facing*** entry | 2.2 | `docs/14-glossary.md` |

**Untouched, deliberately:** `CORE-003`, which already defers to `17-infantry.md` and gained that pointer in the change before this one. `CORE-005`, `CORE-007`, `CORE-008`, `CORE-010`, `CORE-014`, `CORE-016` and the `Universal Rule` section. `CORE-006`'s allotment, action list and "no unit gains additional AP through its profile". Every other `docs/*.md`. `CHANGELOG.md` and every version header.

**Two entries on this list stopped being true, and are corrected here rather than quietly rewritten.** `CORE-006` was listed as untouched "in full"; section 8 removes its size paragraph at the maintainer's decision. `openspec/specs/` was listed as taking no delta; section 8 ships a `REMOVED` one against `action-economy`. `VEH-002` was listed as needing nothing, on a premise the audit found false — section 7.1 is the repair.

---

## 1. The infantry base moves to Infantry

Tasks 1.1 and 1.2 are one edit split across two files. **Apply both.** 1.1 removes the sentence; 1.2 is where it lands. Applying 1.1 alone deletes a rule.

- [x] 1.1 In `docs/02-core-rules.md`, `CORE-001`, replace this anchor — one line:

```
Read horizontally, this is the physical base every infantry model must be built on: one base, 4 × 3 studs, one plate thick. The 4-stud edge is the front (CORE-002).
```

with:

```
Read horizontally it is `4 × 3` studs.
```

  The measurement stays — sixteen rules cite `CORE-001` and they read it for the volume, the plate conversion or the footprint. What goes is the claim that a minifigure must be built on one, which is infantry's, and the front edge, which is `CORE-002`'s subject and answered per domain.

- [x] 1.2 In `docs/17-infantry.md`, `INF-001`, replace this anchor — the rule's second paragraph. The opening line and the closing paragraph, beginning "That orientation is what every direction below", are **not** part of the anchor and are not touched:

```
Every infantry model is built on the base required by `02-core-rules.md` (CORE-001). Which edge of that base is its front is settled by the universal Facing rule (`02-core-rules.md`, CORE-002).
```

with:

```
Every infantry model is built on one base of `4 × 3` studs, one plate thick — the horizontal reading of the Unit Base (`02-core-rules.md`, CORE-001). Its 4-stud edge is the front, which is the facing every unit has (`02-core-rules.md`, CORE-002).

A minifigure has two hands, and may only use equipment it can physically carry in them. Which equipment needs one hand and which needs two is stated where that equipment is defined — weapons by `10-weapons.md` (WPN-010), shields by `05-construction-components.md` (CMP-014).
```

  **No value changes.** The chain was circular: `INF-001` asked `CORE-001` what base it stands on and `CORE-002` which edge faces front, and both answered with infantry facts. It states them now and cites CORE for the two universal things it consumes — the Unit Base's dimensions, and that a unit has a facing at all.

  **The second paragraph is where `CORE-015` lands.** Hands belong to the minifigure, and the minifigure is Infantry's — `design.md` Decision 1's own test says so. Stating the count here is what lets `CMP-014` and `WPN-010` cite it instead of each asserting it. "May only use equipment it can physically carry" is `CORE-015`'s opening sentence, kept rather than dropped: `CORE-014` states that equipment must be *present*, which is a different claim from being *carriable*.

- [x] 1.3 In `docs/17-infantry.md`, the `# Summary` section, replace this anchor — the first item:

```
1. An infantry model is a minifigure on the base `02-core-rules.md` defines.
```

with:

```
1. An infantry model is a minifigure on a base of `4 × 3` studs, one plate thick, whose 4-stud edge is its front.
```

  **`02-core-rules.md` stops defining that base in task 1.1**, which makes this line false the moment 1.1 lands. `system/proposal-review.md` ("The Summary Is Part of the Rule") — a Summary is a restatement and drifts. The count is unchanged: still seven principles, still seven items.

---

## 2. `CORE-002` becomes one universal rule

- [x] 2.1 In `docs/02-core-rules.md`, `CORE-002`, replace this anchor — the whole rule body. The heading is **not** part of the anchor:

```
Every unit has a facing.

Every model must have an obvious front.

For infantry:

The 4-stud side of the base is the front.

For vehicles:

The front is determined by the vehicle construction.

Facing determines:

- Forward movement
- Rear movement
- Left side
- Right side
- Front firing arcs
- Rear firing arcs
```

with:

```
Every unit has a facing, and every model must have an obvious front.

Which part of a model is its front is its own domain's rule — infantry (`17-infantry.md`, INF-001), vehicles (`08-vehicles.md`, VEH-002).
```

  **The six-item list goes, and it was already wrong.** `MOVE-001` states that which directions a unit has is its own domain's rule — infantry has four, a vehicle has two and turns between them — so "Left side / Right side" is not universal. A list of what a rule is consumed for is a snapshot a command can print (`system/documentation-standards.md`, How a Rule Is Written), and no shorter version of it is written here: `MOVE-001` already cites `CORE-002` from the movement side, which is the interface.

  **Front and rear firing arcs leave the ruleset with it.** The list was their only statement — `grep -rn "arc" docs/` finds the word elsewhere only in `WPN-011` ("Weapon position determines firing arc", about mounted vehicle weapons) and `09-transport.md`. Nothing defined what a unit's front or rear arc was, what it spanned, or what it decided. This change does not invent one, and does not leave a pointer at a document that would have to (`design.md`, Decision 4).

- [x] 2.2 In `docs/14-glossary.md`, the `## Facing` entry, replace this anchor — the entry's first two paragraphs. The heading is **not** part of the anchor:

```
The direction a unit is oriented toward.

Determines forward and rear movement, the left and right sides, and front and rear firing arcs. See `02-core-rules.md`, CORE-002. Which way a shield protects is settled by where it physically stands rather than by Facing — see `05-construction-components.md`, CMP-014.
```

with:

```
The direction a unit is oriented toward. Which part of a model is its front is its own domain's rule — see `02-core-rules.md`, CORE-002. Which way a shield protects is settled by where it physically stands rather than by Facing — see `05-construction-components.md`, CMP-014.
```

  `system/proposal-review.md` ("The Summary Is Part of the Rule") — a glossary entry is a restatement and is checked in the same pass as the rule. This one reproduces the list task 2.1 deletes, including the "left and right sides" that is not universal.

---

## 3. `CORE-004` matches `CORE-003`

- [x] 3.1 In `docs/02-core-rules.md`, `CORE-004`, replace this anchor — the rule's second line:

```
How small a vehicle may be built is a vehicle-construction rule — `08-vehicles.md` (VEH-001), with VEH-013 for the reason.
```

with:

```
What a vehicle can do, and how it must be built, is a vehicle rule — `08-vehicles.md`.
```

  `CORE-003` closes "What an infantry model can do is an infantry rule — `17-infantry.md`." This is the same sentence for the other domain. The rule's first line, which classifies a vehicle as a powered model whose footprint is the LEGO model itself, is **not** part of the anchor and stays: that is the classification CORE owns.

---

## 4. `CORE-009` keeps the principle

- [x] 4.1 In `docs/02-core-rules.md`, `CORE-009`, replace this anchor — the blockquote and the sentence below it:

```
> If you can see it, you can shoot it.

This does not grant a shot outside a unit's own activation: StudCraft has no reaction fire, which `11-combat.md` (CBT-014) lists as a possible future extension rather than a current rule.
```

with:

```
> If you can see it, you can shoot it.
```

  The blockquote is a landmark and does not change. **`CBT-014` ends this change cited by nothing, and that is the intended result** — it is Combat's list of what Combat has not built, and whether reaction fire exists is a combat question `11-combat.md` answers (`design.md`, Decision 7). Nothing else in `docs/` cites `CBT-014`.

---

## 5. `CORE-015` is retired

Tasks 5.1, 5.2 and 5.3 are one edit split across three files. **Apply all three.** 5.1 deletes the rule; 5.2 and 5.3 are where its two facts land and where its two citers are re-aimed.

- [x] 5.1 In `docs/02-core-rules.md`, replace this anchor — the whole `CORE-015` rule, from its heading through the `# Physical State` heading that follows it. The `---` above `## CORE-015` stays where it is and becomes the separator before `# Physical State`:

```
## CORE-015 — Hands

A minifigure may only use equipment it can physically carry.

As a general guideline, one hand carries one one-handed item — a shield among them — and two-handed equipment occupies both hands. `10-weapons.md` (WPN-010) states which weapons are which.

The physical model determines what the unit carries.

---

# Physical State
```

with:

```
# Physical State
```

  `# Physical State` is a landmark. **Do not renumber `CORE-016` into the gap and do not leave a stub.** What was universal here is `CORE-014`, which stays: equipment must be physically represented, and a unit cannot use what is not on the model.

- [x] 5.2 In `docs/05-construction-components.md`, `CMP-014`, replace this anchor — the rule's first line:

```
A Shield is defensive equipment physically attached to an infantry model, visible on it, and occupying one hand (`02-core-rules.md`, CORE-015).
```

with:

```
A Shield is defensive equipment physically attached to an infantry model, visible on it, and occupying one of the two hands `17-infantry.md` (INF-001) gives a minifigure. Like all equipment it must be physically present to be used (`02-core-rules.md`, CORE-014).
```

  **A shield is not a weapon.** It is cover, and cover is a component, so how many hands it takes is stated by the shield's own rule rather than by a rule about weapons (`design.md`, Decision 5). How many hands there are to take is `INF-001`'s, which is why this cites it rather than repeating the count.

- [x] 5.3 In `docs/10-weapons.md`, `WPN-010`, replace this anchor — the rule's first line:

```
Infantry weapons must be carried by the minifigure, following the universal Hands rule (`02-core-rules.md`, CORE-015): one-handed weapons (knife, sword, pistol) occupy one hand alongside a shield; two-handed weapons (rifle, machine gun, rocket launcher) occupy both.
```

with:

```
Infantry weapons must be carried by the minifigure in the two hands `17-infantry.md` (INF-001) gives it: one-handed weapons (knife, sword, pistol) occupy one and leave the other free; two-handed weapons (rifle, machine gun, rocket launcher) occupy both.
```

  `WPN-010` reproduced both lists already and cited `CORE-015` as though the answer lived in CORE. It owns them now, and cites `INF-001` for the hand count rather than restating it.

  **"Leave the other free" is deliberately not a permission.** The old text said one-handed weapons "occupy one hand alongside a shield". Saying instead that the free hand may hold a second weapon would newly allow dual-wielding, and `11-combat.md` (CBT-001) charges 1 Action Point per weapon system — a second pistol would be a second attack. This change moves sentences between documents and grants nothing; what may fill the free hand is decided by the rules for whatever goes in it.

---

## 6. Verification

Run each command and write down what it actually returned. If a figure differs from the one stated here, **stop and report it** — do not edit a document to make it match. Every "before" figure below was produced by running the command against the pre-change files.

- [x] 6.1 `grep -rn "CORE-015" docs/` — before: three hits, the heading in `docs/02-core-rules.md` plus `CMP-014` and `WPN-010`. After: **no output at all**.

- [x] 6.2 `grep -c "^## CORE-" docs/02-core-rules.md` — before: **13**, after: **12**. Task 5.1 removes one rule; nothing is renumbered.

- [x] 6.3 `grep -c -F "every infantry model must be built on" docs/02-core-rules.md` — before: **1**, after: **0**. Task 1.1.

- [x] 6.4 `grep -c -F "one plate thick" docs/17-infantry.md` — before: **0**, after: **2**: once in `INF-001` (task 1.2) and once in the Summary (task 1.3). **6.3 and 6.4 are a pair** — if 6.3 is 0 and 6.4 is also 0, the base requirement was deleted rather than moved, and that is the halt-and-report case.

  **This task first said 1, and was written before task 1.3 existed.** Task 1.3 was added after the audit, and its replacement carries the same phrase, so the count it pins moved from one to two. The applier ran it, got 2, left the box unticked and reported the mismatch rather than editing a document to match — which is the standard (`system/delegating-to-agents.md`, "Test the verification commands against the pre-change state").

- [x] 6.5 `grep -c -F "Front firing arcs" docs/02-core-rules.md` — before: **1**, after: **0**. Task 2.1.

- [x] 6.6 `grep -rn "CBT-014" docs/` — before: two hits, `CORE-009`'s citation and the rule's own heading in `docs/11-combat.md`. After: **one**, the heading. Task 4.1, and `design.md` Decision 7 is why.

- [x] 6.7 `python3 scripts/lint_ruleset.py` — before: `Checked 15 docs, no structural issues found.` After: the same line. This is what confirms the retired `CORE-015` breaks no citation and that the re-aimed ones resolve.

- [x] 6.8 `python3 scripts/preflight.py` — **all 12 checks must PASS.** Unlike the change before this one, nothing here is expected to fail: no new document, no file outside `docs/`, and `TODO.md` quotes none of the rules this change touches.

- [x] 6.9 `python3 scripts/check_task_anchors.py core-stops-describing-units` — must **exit 0**.

- [x] 6.10 `git status --short` — five modified files — `docs/02-core-rules.md`, `docs/05-construction-components.md`, `docs/10-weapons.md`, `docs/14-glossary.md`, `docs/17-infantry.md` — plus the untracked change directory as a single `??` entry. Anything else is a mismatch: report it and stage nothing. **Superseded by 7.9**: section 7 brings in `08-vehicles.md` and `11-combat.md`.

---

## 7. Repairs after the audit of the applied text

The applied text was audited and returned nine findings. Eight are repaired here; the ninth needs no `docs/` edit and is recorded at the end.

**One of them is a premise this change asserted without checking.** `tasks.md` said `VEH-002` "already states how a vehicle's front is decided and needs nothing". It does not — it says only that a vehicle must have an obvious front. Deleting `CORE-002`'s "For vehicles: The front is determined by the vehicle construction" therefore dropped the vehicle answer and left `CORE-002` and `VEH-002` citing each other in a loop, which is the exact shape `design.md` Decision 4 refused for firing arcs.

**Every anchor in this section was checked against the applied files**, and each occurs exactly once. Two documents join the change here: `docs/08-vehicles.md` and `docs/11-combat.md`.

- [x] 7.1 In `docs/08-vehicles.md`, `VEH-002`, replace this anchor — the rule's first line:

```
Every vehicle must have an obvious front — the universal Facing rule (`02-core-rules.md`, CORE-002) applies to vehicles exactly like any other unit, and movement is performed relative to it (`07-movement.md`, MOVE-001).
```

with:

```
Every vehicle must have an obvious front, and its construction is what makes it obvious: the end the model is built to lead with. The universal Facing rule (`02-core-rules.md`, CORE-002) applies to vehicles exactly like any other unit, and movement is performed relative to it (`07-movement.md`, MOVE-001).
```

  **This is where `CORE-002`'s deleted vehicle line lands.** `INF-001` names the 4-stud edge; this names the construction. Without it, `CORE-002` deferred to a rule that deferred back.

- [x] 7.2 In `docs/10-weapons.md`, `WPN-010`, replace this anchor — the rule's first line:

```
Infantry weapons must be carried by the minifigure in the two hands `17-infantry.md` (INF-001) gives it: one-handed weapons (knife, sword, pistol) occupy one and leave the other free; two-handed weapons (rifle, machine gun, rocket launcher) occupy both.
```

with:

```
Infantry weapons must be carried by the minifigure in the two hands `17-infantry.md` (INF-001) gives it: one-handed weapons (knife, sword, pistol) occupy one of them, two-handed weapons (rifle, machine gun, rocket launcher) occupy both.
```

  **"Leave the other free" said the second hand *is* free**, which contradicts a sword-and-shield model (`05-construction-components.md`, CMP-014) and a dual-wielding one — `12-melee.md` (MEL-003) tabulates "Two Swords → 2 weapon systems". The rule states what a weapon consumes; what fills the other hand is decided by whatever goes in it.

- [x] 7.3 In `docs/17-infantry.md`, `INF-001`, replace this anchor — the rule's last two paragraphs, in the order the change left them:

```
A minifigure has two hands, and may only use equipment it can physically carry in them. Which equipment needs one hand and which needs two is stated where that equipment is defined — weapons by `10-weapons.md` (WPN-010), shields by `05-construction-components.md` (CMP-014).

That orientation is what every direction below is measured relative to — the general rule is `07-movement.md` (MOVE-001).
```

with:

```
That orientation is what every direction below is measured relative to — the general rule is `07-movement.md` (MOVE-001).

A minifigure has two hands, and may only use equipment it can physically carry in them. Which equipment needs one hand and which needs two is stated where that equipment is defined — weapons by `10-weapons.md` (WPN-010), shields by `05-construction-components.md` (CMP-014).
```

  The two paragraphs swap. Task 1.2 inserted the hands paragraph between "Its 4-stud edge is the front" and "**That orientation** is what every direction below is measured relative to", so the pronoun reached back past a paragraph about equipment. Base, front, orientation is one chain and stays contiguous.

- [x] 7.4 In `docs/05-construction-components.md`, `CMP-014`, replace this anchor — the rule's first line:

```
A Shield is defensive equipment physically attached to an infantry model, visible on it, and occupying one of the two hands `17-infantry.md` (INF-001) gives a minifigure. Like all equipment it must be physically present to be used (`02-core-rules.md`, CORE-014).
```

with:

```
A Shield is defensive equipment physically attached to an infantry model, visible on it, and occupying one of the two hands `17-infantry.md` (INF-001) gives a minifigure.
```

  The added sentence stated the presence requirement a second time — "physically attached to an infantry model, visible on it" is already that requirement — and `WPN-010`, re-aimed in the same edit for the same reason, gained no equivalent. One idea, stated once.

- [x] 7.5 In `docs/02-core-rules.md`, `CORE-003`, replace this anchor — the rule's last line:

```
What an infantry model can do is an infantry rule — `17-infantry.md`.
```

with:

```
What an infantry model can do, and how it must be built, is an infantry rule — `17-infantry.md`.
```

  `CORE-004` says "What a vehicle can do, **and how it must be built**, is a vehicle rule" after task 3.1. This change moved infantry construction — the base, its front edge — into `17-infantry.md`, so the same clause is now true of infantry and the two Unit Types rules should not delegate in mismatched scopes.

- [x] 7.6 In `docs/17-infantry.md`, the `# Summary` section, replace this anchor — the first item:

```
1. An infantry model is a minifigure on a base of `4 × 3` studs, one plate thick, whose 4-stud edge is its front.
```

with:

```
1. An infantry model is a minifigure with two hands, on a base of `4 × 3` studs, one plate thick, whose 4-stud edge is its front.
```

  `INF-001` is now the ruleset's only statement of the hand count, and `CMP-014` and `WPN-010` both lean on it. The Summary restates the rule and had not caught up. **The count stays seven.**

- [x] 7.7 In `docs/14-glossary.md`, the `## Facing` entry, replace this anchor — the entry's body:

```
The direction a unit is oriented toward. Which part of a model is its front is its own domain's rule — see `02-core-rules.md`, CORE-002. Which way a shield protects is settled by where it physically stands rather than by Facing — see `05-construction-components.md`, CMP-014.
```

with:

```
The direction a unit is oriented toward, and what movement is performed relative to — see `07-movement.md`, MOVE-001. Which part of a model is its front is its own domain's rule — see `02-core-rules.md`, CORE-002. Which way a shield protects is settled by where it physically stands rather than by Facing — see `05-construction-components.md`, CMP-014.
```

  Task 2.2 trimmed the entry to two pointers, one of which delegates again and one of which is an exception, so a reader looking the term up learned what facing is not used for and never what it is. The deleted "determines forward and rear movement" was correct and lives in `MOVE-001`; the entry now names it.

- [x] 7.8 In `docs/11-combat.md`, `CBT-014`, replace this anchor — the rule's first line:

```
Future versions may include:
```

with:

```
None of the following exists in StudCraft today, and no rule grants it.

Future versions may include:
```

  **"Future versions may include:" stays on its own line, and that is not cosmetic.** `TODO.md` quotes this rule's block verbatim and `scripts/check_todo_quotes.py` compares it line by line; folding the new sentence into that line would break the quote and turn a green check red.

  **`CORE-009` stopped answering a question `CODE_OF_DESIGN.md` sends readers to it for.** Principle 9 says "Whether that produces a shot outside a unit's own activation is a rule, not a principle — `docs/02-core-rules.md` (CORE-009) decides it", and task 4.1 removed the sentence that decided it. Listing Reaction Fire as a future extension did not by itself say it is absent now. This makes the list say so, in the document that owns combat entitlement, and `CODE_OF_DESIGN.md` is re-aimed at it outside `docs/` — see the note below.

### Verification after section 7

- [x] 7.9 `git status --short` — **seven** modified files: the five from 6.10 plus `docs/08-vehicles.md` and `docs/11-combat.md`, plus `CODE_OF_DESIGN.md` and the change directory.

- [x] 7.10 `grep -c -F "leave the other free" docs/10-weapons.md` — before: **1**, after: **0**. Task 7.2.

- [x] 7.11 `grep -rn "CBT-014" docs/ CODE_OF_DESIGN.md` — before: one hit, the heading. After: **two** — the heading and `CODE_OF_DESIGN.md`'s re-aimed Principle 9. `CBT-014` stops being uncited, which was a consequence of task 4.1 and is now resolved rather than accepted.

- [x] 7.12 `python3 scripts/lint_ruleset.py` — `Checked 15 docs, no structural issues found.`

- [x] 7.13 `python3 scripts/preflight.py` — all 12 checks PASS.

### Outside `docs/`, and not a task

**`CODE_OF_DESIGN.md`, Principle 9** is re-aimed from `CORE-009` to `11-combat.md` (CBT-014) in this same commit. It is not a `docs/*.md` file, so `system/repository-strategy.md` (Branch Naming) would put it on its own branch; shipping a pointer this change knowingly breaks is worse, and the maintainer folded the same class of file into one pull request last time. It is called out here and in `proposal.md` so the choice is visible rather than silent.

**Not repaired: "firing arc" is a term no rule defines.** `WPN-011` and `TRN-011` each derive an arc from a physical thing — where a weapon is mounted, where an opening is — and neither depended on `CORE-002`'s bullets, so no outcome changes. The audit confirms the reading `design.md` Decision 4 states: nothing was lost, because nothing was ever defined. Giving the term an owner is Combat's change to make.

---

## 8. `CORE-006` stops banning a pricing scheme no rule uses

**This section ships a capability delta, and it is the only part of this change that does.** Everything before it moves sentences between documents; this removes a requirement from `openspec/specs/action-economy` (`design.md`, Decision 8).

The maintainer's call, made against the recommendation recorded in Decision 8 and after the evidence for keeping it was put twice: **the paragraph goes.** The reasoning is that a prohibition on something the ruleset never does is not a rule, and an exception cannot be made to a scheme that is never established.

What that costs, stated plainly so the reviewer sees it: `TRN-005` and `TRN-006` cite `CORE-006` for "whatever the unit occupies", and after this they state their own flat cost without deferring. The third sentence of the paragraph — the one naming an obstacle's height for infantry and a Terrain Threshold for a vehicle — goes with the first two, because it exists only to qualify the ban and qualifies nothing once the ban is gone.

- [x] 8.1 In `docs/02-core-rules.md`, `CORE-006`, replace this anchor — the rule's last paragraph, together with the blank line and the `---` below it. The `**3 Action Points**` paragraph above is **not** part of the anchor:

```
**No Action Point cost scales with size** — not with the size of the unit paying it, and not with the size of an interactive element it operates (CORE-007). An action's cost is set by the rule that governs that action, and where more than one Action Point is spent that rule states why; the reason is never size. A measurement may still decide **which** rule applies, and which measurement is read is the unit's own domain's rule — an obstacle's height for infantry (`17-infantry.md`, INF-006 through INF-008), a Terrain Threshold for a vehicle (`08-vehicles.md`, VEH-021).

---
```

with:

```
---
```

  The `---` is a landmark. `CORE-006` keeps the allotment, the action list and the statement that no unit gains AP through its profile — which is the part `FLOW-004`, `FLOW-005`, `FLOW-012`, `VEH-004`, `CBT-001`, `DMG-019`, `INF-002` and `INF-009` all cite it for.

- [x] 8.2 In `docs/09-transport.md`, `TRN-005`, replace this anchor — the rule's first line:

```
Embarking costs **1 Action Point**, whatever the unit occupies (`02-core-rules.md`, CORE-006) — an infantry model of one Unit Base and a motorcycle of two pay the same, matching Disembarking (TRN-006).
```

with:

```
Embarking costs **1 Action Point** — an infantry model of one Unit Base and a motorcycle of two pay the same, matching Disembarking (TRN-006).
```

  The flat cost stays and is stated here, with its own worked contrast. What goes is the deferral: `CORE-006` no longer says anything about what a unit occupies, so citing it for that would point at a rule that has stopped answering.

- [x] 8.3 In `docs/09-transport.md`, `TRN-006`, replace this anchor — one line:

```
The cost is the same whatever the unit occupies (`02-core-rules.md`, CORE-006), matching Embarking (TRN-005).
```

with:

```
The cost is the same whatever the unit occupies, matching Embarking (TRN-005).
```

  Same edit from the other side. `TRN-006` keeps the claim and stops sourcing it from CORE.

### Verification after section 8

- [x] 8.4 `grep -rn "scales with size" docs/` — before: one hit in `docs/02-core-rules.md`. After: **no output at all**.

- [x] 8.5 `grep -c -F "CORE-006" docs/09-transport.md` — before: **2**, after: **0**. Tasks 8.2 and 8.3.

- [x] 8.6 `grep -c "^## CORE-006" docs/02-core-rules.md` — **1**, before and after. The rule keeps its number and its other three paragraphs; only the last one goes. A **0** means the whole rule was deleted — stop and report it.

- [x] 8.7 `python3 scripts/check_delta_coverage.py` — must **exit 0**. It audits `## MODIFIED Requirements` blocks only, and this delta is `## REMOVED`, so it has nothing to check here; running it is what confirms that.

- [x] 8.8 `python3 scripts/lint_ruleset.py` — `Checked 15 docs, no structural issues found.`

- [x] 8.9 `python3 scripts/preflight.py` — all 12 checks PASS. **`openspec validate` now has a delta to read**, where before this section the change carried none; a failure there is about the delta's shape, not about `docs/`.
