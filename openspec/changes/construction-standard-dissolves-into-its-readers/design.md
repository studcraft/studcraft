# Design — The Construction Standard dissolves into its readers

## Context

#103 cut `02-core-rules.md` to what no other document states, #104 did the same to `04-construction-standard.md`, and #108 did it to `05-construction-components.md` and then moved six rules to match a boundary the maintainer set. Each pass left the Construction Standard smaller: twenty-four rules, then eleven, then five.

This change asks the question the third pass raised and did not answer. #108's `design.md` (Decision 13) rejected merging the two construction documents, and it rejected it on one cost that is real and one that is not:

- **Real:** `README.md`'s reading order is positional, so removing an entry renumbers the entries after it. Task 8.3 does exactly that, to ten of them. It is prose, not an identifier, and no document is renumbered.
- **Not real:** "every remaining `SCS` rule needs a new ID". None does. #108's own last section proved it, when `WPN-001` absorbed `SCS-016` and `SCS-017` into its existing bullets rather than becoming `WPN-022` — a construction requirement absorbed into the rule that reads it needs no number.

#108 also licensed this change explicitly: "If the criterion turns out not to hold, merging stays available." The criterion held for components, and the audit of that change then found the boundary sentence itself wrong twice in one line — false for vehicles, ambiguous for structures. A boundary that took three attempts to state is one worth not having.

---

## Decision 1 — Delete the document rather than shrink it again

The test is `system/documentation-standards.md`'s, applied to a file instead of a rule: **only content with no other home survives, and a file whose every line has a destination is deleted rather than kept for its organisational role.**

Three of the five rules restate "only physical LEGO affects gameplay" for one noun — a wall, a stair, a platform. Two carry content: the infantry base, and a slope being built from slope elements. Both have an obvious reader.

There is a second argument, and it is the stronger one. #108 had to write a boundary sentence into this document's `# Purpose` because two construction documents with no line between them had produced `SCS-007`/`CMP-009`, `SCS-008`/`CMP-010` and `SCS-009`/`CMP-011` — the same rule written twice, three times over. A boundary is a maintenance obligation: it has to be stated, kept true, and applied by every future contributor. **Deleting one side removes the obligation instead of documenting it.** That is Principle 11 applied to the repository rather than to the game.

Rejected: retiring `SCS-010`, `SCS-012` and `SCS-013` and keeping a two-rule document. It preserves the boundary, the `# Purpose` sentence, the reading-order entry and the file, in exchange for keeping two rules away from the rules that read them.

---

## Decision 2 — `SCS-002` is absorbed by `CORE-001`, not moved to Components

Under #108's boundary an infantry base is part of a model, which points at `05-construction-components.md`. It goes to `CORE-001` instead, for a reason that outranks the boundary: **`CORE-001` and `SCS-002` are a circular pair.**

- `CORE-001`: "Read horizontally, this is the size of the physical base an infantry model is built on — **required by `SCS-002`**."
- `SCS-002`: "one physical base measuring 4 × 3 studs — **one Unit Base read horizontally (`CORE-001`)** — and one plate thick, which is the plate `CORE-001` counts in the Unit Base's height."

Each defers to the other for the same fact. Moving the rule to a third document as `CMP-023` would keep the loop and lengthen it. Absorbing it into `CORE-001` closes it: the Unit Base read horizontally **is** the base every infantry model is built on, stated once, by the rule that defines the unit.

This does not reopen #103. That change cut `CORE` to what no other document states, and after this one no other document states the base.

Rejected: `CMP-023` in `05-construction-components.md` — circularity survives, and a base is the measuring unit made physical rather than a component providing a capability. Rejected: leaving `SCS-002` in place as a one-rule document, which is the "organisational role" Decision 1 rules out.

Rejected: `CORE-003` ("Infantry are represented by LEGO minifigures. Infantry occupy one Unit Base."), which is the rule about infantry and reads more naturally as the home of "every infantry model must be built on…". It loses to `CORE-001` on the circularity argument — `CORE-003` is not one of the two rules deferring to each other — and because the base's dimensions are the Unit Base's horizontal reading, so stating them anywhere but `CORE-001` splits one fact across two rules. The cost is real and worth recording: `CORE-001` now carries a measurement definition *and* a construction obligation.

---

## Decision 3 — The two terrain rules land in `07-movement.md`, inside their readers

`MOVE-012` and `MOVE-013` are the rules that read a slope and a stair, and both already describe what they are made of — `MOVE-013` says "Plate-built stairs" in its first sentence. So the requirements land inside those two sentences rather than as new `MOVE` rules:

- `MOVE-012`: "Slopes are valid climbing surfaces." → "A slope is built from LEGO slope elements, and is a valid climbing surface."
- `MOVE-013`: "Plate-built stairs are valid movement paths." → "Stairs built from plates or bricks are valid movement paths."

`SCS-011`'s content is load-bearing and worth naming: a flight of stacked plates is not a slope, which is what lets `MOVE-012` treat a slope as ordinary terrain and `VEH-027` accept it as a vehicle ascent while forbidding stairs. Without it, "slope" is a shape a player asserts.

Rejected: two new `MOVE` rules. Each would state one clause the neighbouring rule already half-states, which is the pattern #108 spent five sections removing.

Rejected: `15-geometry-layers.md`, which owns what counts as measurable, not what terrain is built from.

---

## Decision 4 — `SCS-010` and `SCS-013` are retired, not relocated

`SCS-010` is `02-core-rules.md`'s *The Battlefield* section — "Only physical LEGO elements may affect gameplay" — narrowed to walls. `MOVE-009` – `MOVE-014` read a wall's height and never ask what it is made of, so no reader is missing anything.

`SCS-013` is two halves, both stated: `MOVE-014` closes with "Physical construction determines accessibility", and `MOVE-015` places a falling unit "at the first surface that physically supports it". Its permissive half — any stable surface may support a unit — grants what the plastic already grants; `VEH-030` already assumes it when it counts a model carried on a vehicle's roof.

Rejected: folding either into `MOVE-014` "for completeness". A sentence added to make a deletion feel smaller is the copy this series removes.

---

## Decision 5 — The Universal Rule's "Construction Standards" level stays

`02-core-rules.md` ranks Foundations, Core Rules, Construction Standards, Scenario Rules, and `03-game-flow.md` paraphrases it. Deleting a document called the Construction Standard leaves a level with a familiar name and no file behind it.

It stays, because the level never named the file. `CORE`'s own note says "The order ranks these four levels only. A system document — Movement, Vehicles, Damage and the rest — is not a level in it." Construction standards are what `05-construction-components.md` and `10-weapons.md` state, before and after this change; the level says such rules outrank a scenario and yield to Core Rules, which is still true.

Rejected: renaming the level to "Construction rules". It edits a precedence rule in two documents to remove a verbal echo, and a precedence rule is the last thing to touch for cosmetics. Recorded here so the question is not re-proposed as an oversight.

**One consequence is real and is accepted rather than denied.** Two requirements change level. The slope and stair construction requirements land in `07-movement.md`, and `CORE-001`'s own note says a system document "is not a level in it" — so those two now rank as Movement rules rather than as Construction Standards, and `FLOW-013`'s "never contradict Foundations, Core Rules or Construction Standards" no longer reaches them. The infantry base moves the other way, up into Core Rules. Nothing in the ruleset turns on either move: no scenario rule anywhere overrides a construction requirement, and the level ordering has never been invoked to resolve a conflict. Naming it is cheaper than pretending the level list is untouched.

---

## Decision 6 — The document number is retired, not reused

`system/documentation-standards.md` (Naming Conventions): "A removed document's number is never reused either." `13-materials.md` is the precedent and `README.md` documents it. So `docs/` will have gaps at `04` and `13`, `README.md`'s note covers both, and no document is renumbered.

The Rulebook reading order is different: its numbers are positions in a list, not document numbers, so removing the fifth entry renumbers the entries after it. That is `README.md` prose and not an identifier.

---

## Decision 7 — `unit-base` gets a delta, because a requirement enters a tracked capability

`CORE-001` is the rule of the tracked `unit-base` capability. Its spec **presupposes** the infantry base without defining it: one requirement measures the Unit Base's height "from the underside of the base an infantry model stands on", and one scenario reads "WHEN an infantry model is placed on its standard base". Neither says what that base is.

Task 1.1 puts the definition there. So a requirement crosses from an untracked document into a tracked capability's rule, and the test this repository applies is whether a capability's requirements change — not whether a spec happens to name the document being deleted. Without a delta, the Archive cut would write back a `unit-base` spec that still only presupposes the base, and the requirement would exist in `docs/` and nowhere in `openspec/specs/`.

The delta is `MODIFIED` on **Requirement: Unit Base Measurement**, adding one sentence to the requirement and one scenario (*The standard base is the horizontal reading*). Every existing scenario is carried through unchanged, which is what `scripts/check_delta_coverage.py` checks.

This is the one place this change differs from its three predecessors, all of which shipped no delta. They were moving rules between untracked documents; this one moves a requirement into a tracked one.

Rejected: no delta plus a sentence in `proposal.md` saying no requirement stops being true. It is true and it is not the point — nothing stops being true, and something starts being true that the spec would never learn.

---

## What was checked and found clean

- All five `SCS` IDs through `scripts/rule.py refs` and a repository-wide grep. Three are cited by nothing; `SCS-002`'s two citers and `SCS-011`'s one are retargeted here.
- Every reference to the document by name, in `docs/`, `README.md`, `CONTRIBUTING.md`, `TODO.md`, `assets/IMAGES.md` and `system/proposal-review.md`. `scripts/` has none — #108 removed the last one from a comment in `scripts/lint_ruleset.py`.
- `docs/14-glossary.md`, which cites no `SCS` ID and names no removed document: #108's tasks 19.5 and 20.4 retargeted its last two entries to `CMP-019` and `WPN-001`.
- `TODO.md`, which quotes `CORE-005` verbatim and is compared character for character by `scripts/check_todo_quotes.py`. The quote is edited with the rule, in the same task set.
- `openspec/specs/` — no `SCS` ID, no mention of the document, no delta needed (`system/proposal-review.md`, "Delta vs. Direct Edit").
- The four surviving uses of the phrase "Construction Standard" after deletion, each of which is a level name, a paraphrase of one, a weapon-standard phrase, or a contribution category — none a pointer at a file.
