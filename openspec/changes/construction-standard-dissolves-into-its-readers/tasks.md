# Tasks — The Construction Standard dissolves into its readers

## How to apply this change

Every anchor below is pre-change text, checked with exact-substring matching and occurring **exactly once in the file its task names**. Replace the whole anchor.

If an anchor returns anything other than 1, **stop and report it** rather than guessing which occurrence was meant. Never edit a document to make a verification command pass — report the mismatch instead.

### How to read the replacement blocks

The triple-backtick fence marks where the text starts and stops. **The fence is not part of the text** — do not write the backticks into the document.

A `#` heading, a `---` rule, a `> ` blockquote or a numbered list inside a fence is real markdown that must land in the file as markdown, not as quoted text. Tasks 2.2, 8.1, 8.3 and 9.1 contain real markdown of that kind.

**One task deletes a whole file: task 7.1 removes `docs/04-construction-standard.md`.** Use `git rm docs/04-construction-standard.md`. Every other task is a replacement inside a file that stays.

**Five rule IDs are retired and no new rule ID is created.** `SCS-002`, `SCS-010`, `SCS-011`, `SCS-012` and `SCS-013` go with the file. Three of them are absorbed into the body of an existing rule — `CORE-001`, `MOVE-012`, `MOVE-013` — which is why nothing is numbered `MOVE-022` or `CMP-023`. Do not create a rule to hold absorbed text, and do not renumber anything.

**Do not delete the file before applying tasks 1.1 – 6.1.** Five of those seven tasks retarget a citation that points into it, and a citation left behind is a reader sent to a file that is not there.

**No check catches that mistake, which is why the ordering matters.** `scripts/lint_ruleset.py` verifies a cited rule ID only when the cited *file* is present — `if target_file not in ids_by_file: continue`, twice — so once the file is deleted, every surviving citation of it is skipped in silence. Tasks 12.2 and 12.3's greps are the only net. Do not read a clean `preflight` as proof the retargets landed.

**Three tasks edit a file at the repository root, and each names it with a `./` prefix** — `./TODO.md` in 2.2, `./README.md` in 8.1 – 8.3, `./CONTRIBUTING.md` in 9.1. That is not decoration: `scripts/check_task_anchors.py` only recognises a path with a directory component in it, so a bare `README.md` is invisible to the checker and its anchors get attributed to whichever `docs/` file a previous task named. Keep the prefix.

**`TODO.md` is edited by exactly one task, 2.2.** It quotes `CORE-005` verbatim, `scripts/check_todo_quotes.py` compares that blockquote character for character on every `preflight` run, and task 2.1 edits the sentence it quotes. Applying 2.1 without 2.2 turns the pull request red.

- [x] 0.1 The branch is `construction-standard-dissolves-into-its-readers`, named for this change directory, and it is branched from an up-to-date `main` — the merge commit of pull request #108.

### Scope and coverage

Three ruleset documents edited and one deleted; `README.md`, `CONTRIBUTING.md`, `TODO.md`, `assets/IMAGES.md` and two `system/` documents. **Sixteen edits and eight non-edit tasks** (0.1 and 12.1 – 12.7).

**One spec delta ships with this change**, at `specs/unit-base/spec.md` in this directory: task 1.1 moves a requirement into `CORE-001`, which is the tracked `unit-base` capability's rule, so the requirement is added to that capability rather than left to fall out at the Archive cut (`design.md`, Decision 7). **The applier does not write it** — it is already in the change directory, and `scripts/check_delta_coverage.py` reads it on every `preflight` run.

| `proposal.md` item | Task | Path |
|---|---|---|
| `CORE-001` absorbs `SCS-002` | 1.1 | `docs/02-core-rules.md` |
| `CORE-005` drops the deleted route | 2.1 | `docs/02-core-rules.md` |
| `TODO.md`'s `CORE-005` quote follows it | 2.2 | `TODO.md` |
| `MOVE-002` retargeted to `CORE-001` | 3.1 | `docs/07-movement.md` |
| `MOVE-012` absorbs `SCS-011` | 4.1 | `docs/07-movement.md` |
| `MOVE-013` absorbs `SCS-012` | 5.1 | `docs/07-movement.md` |
| `MOVE-011`'s access list stops saying `Plate stairs` | 5.2 | `docs/07-movement.md` |
| `VEH-027` retargeted from `SCS-011` to `MOVE-012` | 6.1 | `docs/08-vehicles.md` |
| The document is deleted | 7.1 | `docs/04-construction-standard.md` |
| Structure tree, gap note, reading order | 8.1, 8.2, 8.3 | `README.md` |
| Structure listing | 9.1 | `CONTRIBUTING.md` |
| Image coverage counts and list | 10.1 | `assets/IMAGES.md` |
| The untracked-document example | 11.1 | `system/proposal-review.md` |
| The `docs/` gap note | 11.2 | `system/documentation-standards.md` |

**Untouched, deliberately:** the Universal Rule's third level in `docs/02-core-rules.md` and `03-game-flow.md`'s paraphrase of it, and `CONTRIBUTING.md`'s `## Construction Standards` contribution heading — each names a class of rule rather than the deleted file (`design.md`, Decision 5). `docs/05-construction-components.md`, which needs no boundary clause once there is no second construction document (`design.md`, Decision 1). `docs/14-glossary.md`, which cites no `SCS` ID. `docs/10-weapons.md`, whose `WPN-017` names the "StudCraft Weapon Construction Standard" as a phrase. `openspec/specs/`. `CHANGELOG.md` and every `**Version:**` header. Every change directory under `openspec/changes/`.

---

## 1. `docs/02-core-rules.md` — `CORE-001` absorbs `SCS-002`

- [x] 1.1 In `CORE-001`, replace this anchor — one line:

```
Read horizontally, this is the size of the physical base an infantry model is built on — required by `04-construction-standard.md`, SCS-002. The 4-stud edge is the front (CORE-002).
```

with:

```
Read horizontally, this is the physical base every infantry model must be built on: one base, 4 × 3 studs, one plate thick — the plate this rule counts in the Unit Base's height. The 4-stud edge is the front (CORE-002).
```

  The rule stops citing a document that is about to be deleted and states the requirement instead. It is the same requirement in the same words `SCS-002` used, minus `SCS-002`'s pointer back at `CORE-001` — the loop the two of them formed (`design.md`, Decision 2). The lines above and below are untouched, including the plate-layer sentence that already explains the one plate.

---

## 2. `docs/02-core-rules.md` — `CORE-005`, and the `TODO.md` quote

- [x] 2.1 In `CORE-005`, replace this anchor — the rule's first sentence:

```
A structure's walls, slopes, stairs and platforms follow `04-construction-standard.md`; its doors, windows and other functional parts follow `05-construction-components.md`.
```

with:

```
A structure's doors, windows and other functional parts follow `05-construction-components.md`, like any other model's; its walls, slopes, stairs and platforms are terrain, and how a unit crosses or stands on them is `07-movement.md` (MOVE-009 through MOVE-015).
```

  The rest of `CORE-005` — the sentence about structure-specific damage and Deployment Volume — is untouched. **Task 2.2 must be applied with this one.**

  Two details in the replacement are deliberate. **All four nouns survive**, platforms included: `MOVE-015` is what states that a unit stands on the first surface that physically supports it, so the range runs to `MOVE-015` rather than stopping at `MOVE-014`. And the range is written **"through"**, not with a dash: that is the form every rule range in `docs/` uses, and it is the one `scripts/lint_ruleset.py` checks — a dashed range is a citation no checker reads.

- [x] 2.2 In `./TODO.md`, under the ***Structure-wide damage and Deployment Volume occupation*** heading, replace this anchor — the blockquote that quotes `CORE-005`. The `> ` prefix is real markdown, `TODO.md`'s own format, and must land in the file:

```
> A structure's walls, slopes, stairs and platforms follow `04-construction-standard.md`; its doors, windows and other functional parts follow `05-construction-components.md`. Structure-specific damage (collapse, breaching walls) and Deployment Volume occupation for scenario-placed structures are not yet defined — a structure's individual components (doors, windows, walls) already resolve Impacts through the standard Component Damage System (`16-damage-system.md`) like any other component; only structure-wide consequences (e.g. a building collapsing) remain future work.
```

with:

```
> A structure's doors, windows and other functional parts follow `05-construction-components.md`, like any other model's; its walls, slopes, stairs and platforms are terrain, and how a unit crosses or stands on them is `07-movement.md` (MOVE-009 through MOVE-015). Structure-specific damage (collapse, breaching walls) and Deployment Volume occupation for scenario-placed structures are not yet defined — a structure's individual components (doors, windows, walls) already resolve Impacts through the standard Component Damage System (`16-damage-system.md`) like any other component; only structure-wide consequences (e.g. a building collapsing) remain future work.
```

  **The path is `TODO.md` at the repository root — not under `docs/`.** The quote must match `CORE-005` as task 2.1 leaves it, character for character. The gap itself does not close, so the entry stays.

---

## 3. `docs/07-movement.md` — `MOVE-002`

- [x] 3.1 In `MOVE-002`, replace this anchor — the rule's first line:

```
Every infantry model is built on the base required by `04-construction-standard.md`, SCS-002.
```

with:

```
Every infantry model is built on the base required by `02-core-rules.md` (CORE-001).
```

  One citation moves document, to where task 1.1 puts the requirement. The two lines below it — which edge is the front, and what the base's orientation defines — are untouched.

---

## 4. `docs/07-movement.md` — `MOVE-012` absorbs `SCS-011`

- [x] 4.1 In `MOVE-012`, replace this anchor — the rule's first line:

```
Slopes are valid climbing surfaces.
```

with:

```
A slope is built from LEGO slope elements, and is a valid climbing surface.
```

  `SCS-011`'s requirement lands inside the rule that reads it. It is load-bearing rather than decorative: a flight of stacked plates is not a slope, which is what lets `MOVE-012` treat a slope as ordinary terrain and `VEH-027` accept one as a vehicle ascent while forbidding stairs (`design.md`, Decision 3). The paragraph below, about Action Point cost and distance, is untouched.

---

## 5. `docs/07-movement.md` — `MOVE-013` absorbs `SCS-012`

- [x] 5.1 In `MOVE-013`, replace this anchor — the rule's first line:

```
Plate-built stairs are valid movement paths.
```

with:

```
Stairs built from plates or bricks are valid movement paths.
```

  `MOVE-013` already stated most of `SCS-012`; "or bricks" is the only thing it did not say. The paragraph below is untouched. **Task 5.2 must be applied with this one.**

- [x] 5.2 In `MOVE-011`, replace this anchor — one bullet of its `Examples:` list:

```
- Plate stairs
```

with:

```
- Stairs
```

  Without this, one document answers the same question twice: task 5.1 makes a brick-built staircase a valid movement path, while `MOVE-011` still lists only `Plate stairs` among the three legal access points and `MOVE-014` closes that list with "no other construction grants access". The permissive half used to live in `SCS-012`, in another document; this change deletes that document, so both halves have to agree here. The `- Slopes` and `- Ramps` bullets around it are landmarks and are not edited.

---

## 6. `docs/08-vehicles.md` — `VEH-027`

- [x] 6.1 In `VEH-027`, replace this anchor:

```
The angle does not matter and is never measured: LEGO slope elements (`04-construction-standard.md`, SCS-011) and a lowered ramp (`05-construction-components.md`, CMP-021) bound it by their own construction.
```

with:

```
The angle does not matter and is never measured: LEGO slope elements (`07-movement.md`, MOVE-012) and a lowered ramp (`05-construction-components.md`, CMP-021) bound it by their own construction.
```

  One citation changes, to where task 4.1 puts the requirement. Both parenthesised IDs still sit immediately after their own filename, which is what `scripts/lint_ruleset.py` reads.

---

## 7. Delete `docs/04-construction-standard.md`

- [x] 7.1 Delete the whole file, with `git rm docs/04-construction-standard.md`. **This task has no fenced block on purpose:** `scripts/check_task_anchors.py` reads every fenced block in this file as an anchor it should find in a document, and a fenced shell command is one it never will.

  **Apply tasks 1.1 – 6.1 first.** They remove the four citations that point into this file; deleting it while one survives leaves a dangling reference the linter reports.

  Its five rules are accounted for: `SCS-002` in `CORE-001` (task 1.1), `SCS-011` in `MOVE-012` (4.1), `SCS-012` in `MOVE-013` (5.1), and `SCS-010` and `SCS-013` retired because `02-core-rules.md`'s *The Battlefield* section, `MOVE-014` and `MOVE-015` state both (`design.md`, Decision 4). The document number is retired, never reused — like `13-materials.md`'s before it.

---

## 8. `README.md`

- [x] 8.1 In `./README.md`, in the repository-structure tree, replace this anchor — two lines. **Their leading spaces and the box-drawing characters are part of the text**:

```
    ├── 04-construction-standard.md
    ├── 05-construction-components.md
```

with:

```
    ├── 05-construction-components.md
```

  The second line is a landmark and stays in the file exactly once, where it already is.

- [x] 8.2 In `./README.md`, replace this anchor — the gap note below the tree:

```
`13-*.md` is a deliberate gap, not a missing file — `docs/13-materials.md` was removed (its content folded into `16-damage-system.md`), and per this repo's rule-ID-stability convention, document numbers are not reused or renumbered after removal.
```

with:

```
`04-*.md` and `13-*.md` are deliberate gaps, not missing files — `docs/04-construction-standard.md` was removed (its five rules folded into `02-core-rules.md` and `07-movement.md`) and `docs/13-materials.md` before it (its content folded into `16-damage-system.md`), and per this repo's rule-ID-stability convention, document numbers are not reused or renumbered after removal.
```

- [x] 8.3 In `./README.md`, in the Rulebook reading order, replace this anchor — four `##` sections and their numbered lists, from Part II to the end of Reference. **Every `##` heading, `---` rule and numbered list item is real markdown.** It is long; copy it whole:

```
## Part II — Construction

5. `04-construction-standard.md`
6. `05-construction-components.md`

Learn how legal models are built.

---

## Part III — Deployment & Movement

7. `06-deployment.md`
8. `07-movement.md`
9. `08-vehicles.md`
10. `09-transport.md`

Learn how armies are deployed and how units move across the battlefield.

---

## Part IV — Combat

11. `10-weapons.md`
12. `11-combat.md`
13. `12-melee.md`
14. `16-damage-system.md`

Learn how attacks are generated and resolved, and how components take and resist damage.

---

## Reference

15. `14-glossary.md`

Quick lookup for core terms.
```

with:

```
## Part II — Construction

5. `05-construction-components.md`

Learn how legal models are built.

---

## Part III — Deployment & Movement

6. `06-deployment.md`
7. `07-movement.md`
8. `08-vehicles.md`
9. `09-transport.md`

Learn how armies are deployed and how units move across the battlefield.

---

## Part IV — Combat

10. `10-weapons.md`
11. `11-combat.md`
12. `12-melee.md`
13. `16-damage-system.md`

Learn how attacks are generated and resolved, and how components take and resist damage.

---

## Reference

14. `14-glossary.md`

Quick lookup for core terms.
```

  **Only two things change: Part II loses one entry, and every number after it drops by one.** All four Parts and the Reference section stay, with the same headings and the same descriptive lines. These numbers are positions in a reading list, not document numbers — no document is renumbered by this task (`design.md`, Decision 6). Task 12.4 counts the result.

---

## 9. `CONTRIBUTING.md`

- [x] 9.1 In `./CONTRIBUTING.md`, under `# Repository Structure`, replace this anchor — two document names and the blank line between them, inside the fenced block. **The fence itself stays; only these three lines are the anchor**:

```
04-construction-standard.md

05-construction-components.md
```

with:

```
05-construction-components.md
```

  The last line is a landmark and stays. `CONTRIBUTING.md`'s `## Construction Standards` heading, further up, is a contribution category and is **not** edited (`design.md`, Decision 5).

---

## 10. `assets/IMAGES.md`

- [x] 10.1 Under `## Total and rejected candidates`, replace this anchor — two paragraphs:

```
**23 images** specified, across 8 of the 15 ruleset documents (`02-core-rules.md`, `05-construction-components.md`, `07-movement.md`, `08-vehicles.md`, `09-transport.md`, `10-weapons.md`, `15-geometry-layers.md`, `16-damage-system.md`).

The remaining 7 documents (`01-foundations.md`, `03-game-flow.md`, `04-construction-standard.md`, `06-deployment.md`, `11-combat.md`, `12-melee.md`, `14-glossary.md`) need no images of their own: they either restate rules already illustrated above, or are procedural/definitional throughout.
```

with:

```
**23 images** specified, across 8 of the 14 ruleset documents (`02-core-rules.md`, `05-construction-components.md`, `07-movement.md`, `08-vehicles.md`, `09-transport.md`, `10-weapons.md`, `15-geometry-layers.md`, `16-damage-system.md`).

The remaining 6 documents (`01-foundations.md`, `03-game-flow.md`, `06-deployment.md`, `11-combat.md`, `12-melee.md`, `14-glossary.md`) need no images of their own: they either restate rules already illustrated above, or are procedural/definitional throughout.
```

  Two counts and one list entry. The image count is unchanged: this document specified none.

---

## 11. `system/proposal-review.md`

- [x] 11.1 Under "Delta vs. Direct Edit", replace this anchor — two lines. **Their line break is part of the text**:

```
A `MODIFIED` or `REMOVED` delta can only target a capability that already
exists under `openspec/specs/`. Several ruleset documents (`11-combat.md`,
`04-construction-standard.md`, ...) predate the OpenSpec workflow and were
never formalised, so there is nothing to delta against.
```

with:

```
A `MODIFIED` or `REMOVED` delta can only target a capability that already
exists under `openspec/specs/`. Several ruleset documents (`11-combat.md`,
`03-game-flow.md`, ...) predate the OpenSpec workflow and were
never formalised, so there is nothing to delta against.
```

  One example is swapped for another that is still true. `03-game-flow.md` has no entry under `openspec/specs/` either.

- [x] 11.2 In `system/documentation-standards.md`, under `# Repository Structure`, replace this anchor:

```
`ls` is the authority on contents. The `13-*.md` gap in `docs/` is deliberate:
`13-materials.md` was removed and its number retained, per Naming Conventions
below.
```

with:

```
`ls` is the authority on contents. The `04-*.md` and `13-*.md` gaps in `docs/`
are deliberate: `04-construction-standard.md` and `13-materials.md` were
removed and their numbers retained, per Naming Conventions below.
```

  **The line breaks are part of the text** — this file wraps at 79 columns and the replacement keeps that. This is the owner document for Repository Structure, so it states the same fact `README.md` states in task 8.2; both were written when `13` was the only gap. The greps in `proposal.md` could not find it: it names neither the document nor an `SCS` ID.

---

## 12. Verification

Run these after every edit above. Each is a bare command; none of them edits anything.

- [x] 12.1 `python3 scripts/preflight.py` passes, all 12 checks. It runs `scripts/check_todo_quotes.py`, which fails if task 2.2 was skipped, and `scripts/check_delta_coverage.py`, which reads this change's `specs/unit-base/spec.md`. **It does not check for a surviving citation of the deleted document** — see the preamble; tasks 12.2 and 12.3 are what cover that.

- [x] 12.2 `grep -rn "SCS-0" docs/ system/ scripts/ assets/ README.md CODE_OF_DESIGN.md CONTRIBUTING.md AGENTS.md TODO.md` returns **nothing**. Before this change it returned nine lines. `tests/` is deliberately excluded: `tests/test_build_index.py` uses `SCS-001` as a synthetic fixture that never reads `docs/`.

- [x] 12.3 `grep -rn "04-construction-standard" docs/ system/ scripts/ assets/ README.md CODE_OF_DESIGN.md CONTRIBUTING.md AGENTS.md TODO.md` returns **exactly two lines, and both are gap notes** — `README.md`'s, from task 8.2, and `system/documentation-standards.md`'s, from task 11.2. Before this change it returned ten.

  **Two hits are correct, and zero would be wrong.** A gap note explains a retired number by naming the document that held it, which is how the existing `13-materials.md` note is written; a note that could not say what was removed would explain nothing. **What must not appear is a third line, and above all a citation** — anything of the form `` `04-construction-standard.md`, SCS-0NN ``. Read the output rather than counting it: `grep -c -F "SCS-0" README.md` and the same against `system/documentation-standards.md` must both return `0`, which is what separates a gap note from a live reference.

  **This task was written wrong and is corrected here.** It first demanded nothing at all, which tasks 8.2 and 11.2 make impossible — they put the filename into prose on purpose. The applier ran it, reported the mismatch and edited neither gap note, which is the required behaviour and worked.

  Hits inside `openspec/changes/` are expected and are not covered by this command — a proposal records what was proposed then.

- [x] 12.4 `grep -c -E "^[0-9]+\. " README.md` returns `14`. It returned `15` before task 8.3. `grep -n "^## Part" README.md` lists `Part I`, `Part II`, `Part III` and `Part IV`, in that order — all four survive. Read the numbered entries: they must run `1.` to `14.` with no repeated and no skipped number.

- [x] 12.5 `ls docs/` lists fourteen files, with no `04-*.md` and no `13-*.md`.

- [x] 12.6 `python3 scripts/check_id_stability.py` reports **no moved and no reused ID**, and prints `5 retired` in its summary line. A retirement is not an error; no ID is added by this change, so nothing can be a reuse.

- [x] 12.7 `python3 scripts/rule.py refs CORE-001 CORE-005 MOVE-002 MOVE-012 MOVE-013 VEH-027` — every citer printed must name a rule that still exists, and none may name an `SCS` ID.
