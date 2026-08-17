# The Construction Standard dissolves into its readers

## Why

`docs/04-construction-standard.md` has five rules left, and three of them say "this thing must be made of LEGO".

| Rule | Text | Stated elsewhere? |
|---|---|---|
| `SCS-002` | infantry base, `4 × 3` studs, one plate thick | Described by `CORE-001`, which cites it for the requirement |
| `SCS-010` | "Walls must be physically built from LEGO elements." | `02-core-rules.md`, *The Battlefield*: "Only physical LEGO elements may affect gameplay." |
| `SCS-011` | "Slopes must be physically built from LEGO slope elements." | No — this one is real content |
| `SCS-012` | "Stairs must be physically built from LEGO plates or bricks." | `MOVE-013`: "Plate-built stairs are valid movement paths." |
| `SCS-013` | any stable surface may support units; it must physically support the model | `MOVE-014` ("Physical construction determines accessibility") and `MOVE-015` ("the first surface that physically supports it") |

Two rules carry content. A document does not survive on that, and `system/documentation-standards.md` ("What `system/` Is For") is explicit about the test: **only content with no other home survives, and a file whose every line has a destination is deleted rather than kept for its organisational role.**

There is a second reason, and it is the one that makes this the right moment. The previous change (#108) had to write a boundary sentence into this document's `# Purpose` — battlefield here, model parts there, structures split by `CORE-005` — because two construction documents with no line between them had produced three rules written twice. **That sentence exists only because the document does.** Delete the document and the boundary needs no stating: components are in `05-construction-components.md`, terrain construction is in `07-movement.md` beside the rules that read it, and the Unit Base's physical base is in `CORE-001` where the Unit Base is.

> **A rule belongs to the document that reads it.**

## What Changes

`docs/04-construction-standard.md` is deleted. Its number is retired like `13-materials.md`'s before it. **Two rules are absorbed by the rules that read them, one by the rule that describes it, two are retired outright, and three citations are retargeted.** Three ruleset documents are edited and one deleted; `README.md`, `CONTRIBUTING.md`, `TODO.md`, `assets/IMAGES.md` and two `system/` documents follow. One spec delta ships, for `unit-base`.

### Absorbed

Each of these three states a requirement no other rule states, so each lands inside the rule that already reads it. **No new rule ID is created** — a construction requirement absorbed into its reader needs no number of its own, which is how `WPN-001` took `SCS-016` and `SCS-017` in #108.

- **`SCS-002` — Infantry Base → `CORE-001`.** The two are a circular pair today: `CORE-001` says "this is the size of the physical base an infantry model is built on — required by `SCS-002`", and `SCS-002` says the base is "one Unit Base read horizontally (`CORE-001`)". Neither is the owner. `CORE-001` absorbs the requirement — the base *is* the Unit Base read horizontally — and the loop closes. `MOVE-002`'s citation is retargeted.
- **`SCS-011` — Slopes → `MOVE-012`.** "Built from LEGO slope elements" is a real construction requirement: a staircase of stacked plates is not a slope, which is what `MOVE-012` and `VEH-027` rely on when they treat a slope as ordinary terrain rather than an obstacle. `MOVE-012` states it in its own first sentence, and `VEH-027`'s citation is retargeted from `SCS-011` to `MOVE-012`.
- **`SCS-012` — Stairs → `MOVE-013`.** `MOVE-013` already says "Plate-built stairs are valid movement paths" and so already states most of it; it gains `SCS-012`'s "or bricks", which is the only thing it did not say.

### Retired

- **`SCS-010` — Walls.** "Walls must be physically built from LEGO elements" is `02-core-rules.md`'s *The Battlefield* section applied to one noun: "Only physical LEGO elements may affect gameplay." A wall's gameplay behaviour is `MOVE-009` – `MOVE-014`, which read its height and never ask what it is made of. Cited by nothing.
- **`SCS-013` — Platforms.** Its accessibility half is `MOVE-014`'s closing line. **Its permissive half — any stable surface may support a unit — turned out to be stated nowhere, and lands in `MOVE-014`** (`tasks.md`, task 13.2): the first draft of this proposal claimed `MOVE-015` covered it, and `MOVE-015` says where a *falling* unit lands, which is not the same claim. The audit of the applied text caught it. Cited by nothing.

### Retargeted

- **`CORE-005`.** After #108 it read "A structure's walls, slopes, stairs and platforms follow `04-construction-standard.md`; its doors, windows and other functional parts follow `05-construction-components.md`." The first destination is gone, so the sentence names the two that remain: components for a structure's functional parts, `07-movement.md` (`MOVE-009` through `MOVE-015`) for how a unit crosses or stands on its walls, slopes, stairs and platforms. **All four nouns survive**, and the range runs to `MOVE-015` because that is the rule stating a unit stands on the first surface that physically supports it. `TODO.md` quotes this paragraph verbatim and moves with it.
- **`MOVE-002` and `VEH-027`.** One citation each: `SCS-002` becomes `CORE-001`, `SCS-011` becomes `MOVE-012`.
- **`MOVE-011`.** Its access-point list says `Plate stairs`, and `MOVE-014` closes that list with "no other construction grants access". Once `MOVE-013` absorbs `SCS-012`'s "or bricks", the bullet becomes `Stairs` — otherwise one document answers "is a brick-built staircase a legal way up a wall?" twice, and the permissive half no longer has another document to live in.

### Outside `docs/`

- **`README.md`** — the structure tree loses a line, the `13-*.md` gap note becomes a `04-*.md` and `13-*.md` gap note, and the Rulebook reading order loses its fifth entry, which renumbers the positions after it. Those numbers are positions in a list, not document numbers.
- **`CONTRIBUTING.md`** — the same document name in its own structure listing. Its `## Construction Standards` contribution heading is untouched: it names a kind of contribution, and new functional components and building standards are still one.
- **`assets/IMAGES.md`** — its coverage paragraph says "8 of the 15 ruleset documents" and lists `04-construction-standard.md` among "the remaining 7" needing no images. Fourteen documents, six remaining.
- **`system/proposal-review.md`** — "Delta vs. Direct Edit" lists this document as an example of one that predates the OpenSpec workflow. `11-combat.md` still does, so the example survives without it.
- **`system/documentation-standards.md`** — its Repository Structure section states "The `13-*.md` gap in `docs/` is deliberate". It is the owner document for that fact and now has two gaps to name. Found by the audit, not by this proposal's greps: it names neither the document nor an `SCS` ID.

## What Does Not Change

- **No distance, cost, dimension, threshold, capacity or state.** None changes. Every requirement the five rules stated is still stated, in the rule that reads it, except the two whose text was already stated twice.
- **One requirement does change, deliberately, and it is the only one.** `MOVE-013` stops requiring stairs to be "built from plates or bricks" and requires a stepped surface whose steps are each no taller than an obstacle a unit crosses freely (`MOVE-009`), whatever it is built from. A staircase made of LEGO's own stair or wedge elements was illegal as an access point and is now legal — the rule read the part label rather than the built geometry, against Principle 1 and Principle 13. It is inherited from the retired `SCS-012`, and this change is the pass that rewrote the sentence, so it is settled here rather than deferred (`design.md`, Decision 8).

  **The step bound is part of the same decision, not an afterthought.** Trading a material list for "a surface a model can climb" moves the question from which piece to how tall a step, and no rule quantified that — so the new wording cites the rule that already does. No number is written into `MOVE-013`: `MOVE-009` owns the three plate layers, exactly as `CORE-001` owns the Unit Base. A flight with taller steps is not a staircase and a unit meets it as ordinary obstacles, at the Action Point `MOVE-010` charges.
- **No rule ID is renumbered or reused.** Five `SCS` IDs are retired; no new ID is created anywhere, because each absorbed requirement lands inside an existing rule. `04` joins `13` as a retired document number, never reissued.
- **`SCS-002`'s substance.** `4 × 3` studs, one physical base, one plate thick, and the 4-stud edge as the front — all four survive in `CORE-001`, which states three of them already.
- **The Universal Rule, minus one level.** It ranked Foundations, Core Rules, **Construction Standards**, Scenario Rules; the third level is deleted and Scenario Rules becomes third, with `FLOW-013`'s paraphrase following. A precedence order can only rank what a reader can point at, and after this change construction requirements are sentences in five documents — so the level named a class nothing could locate, while `CORE`'s own next sentence says a system document is not a level (`design.md`, Decision 9).

  **Nothing decidable is lost.** `FLOW-013` already lists what a scenario may restrict, and every example is a system-document rule — `WPN-014`, `VEH-006`, `CBT-007`, `MOVE-004`. What a scenario still may not contradict is Foundations and Core Rules, which is where the Unit Base (`CORE-001`) and physical representation (`CORE-016`) live.
- **Six of the seven capabilities under `openspec/specs/`.** Only `unit-base` is touched, and it gains rather than loses: task 1.1 moves the infantry-base requirement into `CORE-001`, which is that capability's rule, so a `MODIFIED` delta adds the requirement and one scenario for it. No spec mentions the deleted document or any `SCS` ID, and no existing requirement or scenario stops being true (`design.md`, Decision 7).
- **`CHANGELOG.md` and every `**Version:**` header.** Release-cut-only. No `**Bump:**` line: nothing is removed that is not stated elsewhere afterwards.

## Checked elsewhere

- `grep -rn "SCS-0"` across `docs/`, `system/`, `scripts/`, `assets/`, `README.md`, `CODE_OF_DESIGN.md`, `CONTRIBUTING.md`, `AGENTS.md` and `TODO.md`. **Nine hits, all accounted for:** five rule headings in the document being deleted, its own `# Purpose` line, and three citations — `CORE-001` and `MOVE-002` on `SCS-002`, `VEH-027` on `SCS-011`. `tests/test_build_index.py` uses `SCS-001` as a synthetic fixture that never reads `docs/`; #108's audit established that and it is unchanged.
- `grep -rn "04-construction-standard"` across the same set. **Ten hits:** four `docs/` citations — `CORE-001`, `CORE-005`, `MOVE-002`, `VEH-027` — plus the deleted document's own `# Purpose` line, `README.md` twice, `CONTRIBUTING.md`, `TODO.md`, `system/proposal-review.md` and `assets/IMAGES.md`. Every one is edited here. `scripts/`, `.github/` and `.claude/` have none — #108's task 21.4 removed the last one.
- `grep -rn -i "construction standard"` across `docs/`. **Three hits survive deletion and none dangles:** the Universal Rule's third level in `02-core-rules.md` (in its unnumbered `# Universal Rule` section, not in `CORE-005`), `03-game-flow.md`'s paraphrase of it, and `WPN-017`'s "StudCraft Weapon Construction Standard" — a phrase rather than a document, which `TODO.md` quotes. Outside `docs/`, `CONTRIBUTING.md`'s contribution heading is the fourth and is deliberately left (`design.md`, Decision 5).
- `python3 scripts/rule.py refs` on all five `SCS` IDs. `SCS-002` is cited by `CORE-001` and `MOVE-002`, `SCS-011` by `VEH-027`, and `SCS-010`, `SCS-012` and `SCS-013` by nothing.
- `docs/14-glossary.md` cites no `SCS` ID and no longer names this document — #108's tasks 19.5 and 20.4 retargeted its last two entries.

## Out of Scope

- **Renaming the Universal Rule's third level.** Recorded above as deliberate: it is a class of rule and the deleted document was never what it named. Editing a precedence rule to remove a verbal echo is a change to a rule, and this one is not it (`design.md`, Decision 5).
- **`CONTRIBUTING.md`'s `## Construction Standards` heading.** Same reasoning, for a contribution category.
- **`05-construction-components.md`'s `# Purpose`.** It states what that document holds and needs no boundary clause, because after this change there is no second construction document to draw a boundary against (`design.md`, Decision 1).
- **Whether `07-movement.md` should be renamed** now that it holds two terrain-construction requirements. It held terrain behaviour all along and `MOVE-012`/`MOVE-013` are the rules that read them; a document name is a separate decision.
- **The three unarchived changes under `openspec/changes/`,** which cite `SCS` IDs in their own artifacts. An applied proposal records what was proposed then, and the Archive cut is a separate pull request.
