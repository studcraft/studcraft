## 0. Setup

- [ ] 0.1 Work on branch `scenario-defines-victory` (`openspec/config.yaml` requires one branch per proposal).

### How to read the replacement blocks

Replacement text is shown as a markdown blockquote so it is visually separable from the instructions. **The `> ` prefix is not part of the text.** Strip it from every line before writing into the document.

Where a block contains a `#` heading or a numbered list, those are part of the text and must be written as real markdown.

### What "the body of a rule" means

Everything between that rule's `#` heading line and the `---` that ends it. **Never change, remove or renumber an existing heading.** One rule ID is added (`FLOW-013`); none is renumbered. Task 4.2 checks the count.

### Scope

Two documents change: `docs/03-game-flow.md` and `docs/14-glossary.md`. Nothing else — `openspec/specs/` has no game-flow capability, so this change carries no spec delta, and `TODO.md` is **not** touched (see task 4.4).

### Coverage

| Item | Task |
|---|---|
| `FLOW-013` defines a scenario | 1.1 |
| `FLOW-010` states who has won | 1.2 |
| `FLOW-001` gains the objectives step | 1.3 |
| Glossary entry for Scenario | 2.1 |

---

## 1. `docs/03-game-flow.md`

### 1.1 Add `FLOW-013` at the end of the rules

- [ ] 1.1.1 Insert the following **after** `FLOW-012`'s closing `---` and **before** the `# Turn Sequence` heading:

> # FLOW-013 — Scenario
>
> Every game is played under a scenario. The scenario is what makes one game different from another: the ruleset defines how models behave, and the scenario defines what the players are trying to do with them.
>
> A scenario **must** state:
>
> - **How the game ends** — a Turn limit, a condition being met, or both (FLOW-010).
> - **How victory is judged** — what each player must achieve, and how a winner is determined when the game ends. A scenario may declare that a game can be drawn.
>
> A scenario **may** also state:
>
> - The battlefield size (FLOW-001) and the Deployment Area (`06-deployment.md`, DEP-001).
> - Where terrain and structures are placed (`02-core-rules.md`, CORE-005).
> - Restrictions on otherwise-legal actions, such as limiting the weapons a unit may fire in one activation (`10-weapons.md`, WPN-014), restricting reverse movement (`08-vehicles.md`, VEH-006), or restricting how a weapon system's Attack Dice may be split (`11-combat.md`, CBT-007).
> - Additional movement options such as sprinting (`07-movement.md`, MOVE-004).
>
> Scenario rules sit fourth in the rule priority order (`02-core-rules.md`, Universal Rule): they may restrict or extend the ruleset for one game, and never contradict Foundations, Core Rules or Construction Standards.
>
> This ruleset defines no objectives of its own. It states what a scenario must declare, not what it may declare — the same way DEP-001 requires a Deployment Area to be agreed without dictating its size. A scenario that wants objective markers, capture rules or victory points describes them itself.

### 1.2 `FLOW-010` — who has won, not only when it ended

- [ ] 1.2.1 Replace the entire body of `FLOW-010` with:

> The active scenario determines when the game ends and who has won (FLOW-013).
>
> Examples of ending conditions include:
>
> - Survive a fixed number of Turns.
> - Capture objectives.
> - Eliminate a specific target.
> - Escort a convoy.
> - Evacuate the battlefield.
>
> Each of these is an ending condition, not a victory condition. A scenario states both: the game ends when the convoy reaches the far edge *or* Turn 6 passes, and the escorting player wins if it arrived. The ruleset supplies neither — it requires the scenario to supply both.

### 1.3 `FLOW-001` — agree the objectives before building

- [ ] 1.3.1 Replace the numbered list in `FLOW-001` with:

> 1. Select a scenario (FLOW-013).
> 2. Agree the objectives and how victory is judged.
> 3. Agree on the battlefield size.
> 4. Select the deployment size (measured in Unit Bases).
> 5. Build each player's force.
> 6. Deploy all units.
> 7. Determine Priority.
> 8. Begin Turn 1.

- [ ] 1.3.2 Add this line after the list, before the closing `---`:

> Step 2 comes before step 5 deliberately: what a force is trying to achieve shapes what it should bring. If the scenario already states its objectives, this step is confirming them; if the players are inventing a scenario, this is where they do it.

---

## 2. `docs/14-glossary.md`

- [ ] 2.1 Add a `## Scenario` entry at the **end** of the definitions, immediately after the `## Penetration` entry and its `---` separator, and **before** the closing `> **Every Brick Matters.**` line. The glossary is in append order, not alphabetical or thematic order — verify this by reading it rather than assuming, then follow it.

- [ ] 2.2 Match the surrounding style exactly: a `## ` heading, one paragraph, a document-and-ID citation, then a `---` separator.

> ## Scenario
>
> The definition of one particular game: how it ends and how victory is judged, at minimum, and optionally the battlefield, the terrain and any restriction on otherwise-legal actions. The ruleset defines how models behave; the scenario defines what the players are trying to do. See `03-game-flow.md` (FLOW-013).

---

## 3. Verify only — make no edit

- [ ] 3.1 `CORE-005`, `DEP-001`, `MOVE-004`, `VEH-006`, `WPN-014` and `CBT-007` all defer to a scenario and are **not** edited by this change. `FLOW-013` gives them something to cite; retrofitting citations into all six is separate work and is not done here.
- [ ] 3.2 `02-core-rules.md`'s Universal Rule already places Scenario Rules fourth in the priority order. `FLOW-013` cites it; the Universal Rule itself does not change.
- [ ] 3.3 No objective, marker, capture or scoring mechanic is added anywhere.
- [ ] 3.4 **`TODO.md` is not edited.** A scenario library is worth having, but `TODO.md`'s own preamble scopes it to gaps *the documents declare in their own text*, each entry quoting the rule that declares it. "The repository ships no scenarios" is a repository gap, not a gap the ruleset declares — putting it there would break the file's stated contract. It is recorded in this change's `proposal.md` instead, which is what the archive preserves.
- [ ] 3.5 No heading text changes. `FLOW-010`'s title stays **End of Game** even though its body now also covers victory: victory is judged when the game ends, so the title still fits, and heading churn is avoided on principle.

---

## 4. Verify

- [ ] 4.1 Run `python3 scripts/lint_ruleset.py`; confirm no structural issues. This checks that `FLOW-013`'s ID is unique and increasing, and that every `(CORE-NNN)`, `(DEP-NNN)`, `(WPN-NNN)`, `(VEH-NNN)`, `(CBT-NNN)` and `(MOVE-NNN)` reference added above resolves.
- [ ] 4.2 Run `grep -rcE '^#{1,2} [A-Z]{3,4}-[0-9]{3} ' docs/ | awk -F: '{s+=$2} END {print s}'` and confirm **219** — one more than the 218 before, that one being `FLOW-013`.
- [ ] 4.3 Run `grep -n "^# FLOW-" docs/03-game-flow.md` and confirm `FLOW-001` through `FLOW-013` appear once each, in ascending order, with no gaps.
- [ ] 4.4 Run `grep -rniE "\bwins?\b|winner|victory" docs/` and confirm the ruleset now answers how a game is won. Before this change that pattern had **zero** hits across all of `docs/`; the only nearby word was "defeats" in `WPN-021`'s brick shortcut (`docs/10-weapons.md`), which is unrelated, is not matched by this pattern, and must still be there.
- [ ] 4.5 Run `grep -c "FLOW-013" docs/03-game-flow.md docs/14-glossary.md` and confirm `FLOW-013` is cited from `FLOW-001`, from `FLOW-010`, and from the glossary — the definition is reachable from every place that needs it. Note the count for `03-game-flow.md` also includes `FLOW-013`'s own heading.
- [ ] 4.6 Confirm `FLOW-001`'s list has **eight** steps and that the objectives step is second.
- [ ] 4.7 Run `git diff --stat main...HEAD` and confirm exactly these paths changed: `docs/03-game-flow.md`, `docs/14-glossary.md`, plus the four files under `openspec/changes/scenario-defines-victory/`.
- [ ] 4.8 Confirm no numeric value changed anywhere in `docs/`.
- [ ] 4.9 Run `python3 scripts/check_delta_coverage.py` and confirm it passes with zero MODIFIED requirements — this change carries no spec delta.
