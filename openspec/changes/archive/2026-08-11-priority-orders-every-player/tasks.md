# Tasks — Priority orders every player

## How to apply this change

Every anchor below was checked with exact-substring matching against the pre-change files and
occurs **exactly once in the file its task names**. Replace the whole anchor.

If an anchor returns anything other than 1, **stop and report it** rather than guessing which
occurrence was meant. Never edit a document to make a verification command pass — report the
mismatch instead.

### How to read the replacement blocks

The triple-backtick fence marks where the text starts and stops. **The fence is not part of the
text** — do not write the backticks into the document.

A `#` heading, a `|` table row or a `---` rule inside a fence is real markdown that must land in
the file as markdown, not as quoted text. Tasks 3.2's block contains a `## Activation Order`
heading, a `---` and the document's closing `> **Every Brick Matters.**` line, and all three are
real.

Task 2.4 replaces lines that live inside a ```` ```text ```` fence already present in
`docs/03-game-flow.md`. That existing fence is **not** part of the anchor and must not be
touched — only the lines quoted in the anchor are replaced. The `↓` and `•` characters are part
of the text on both sides.

No rule heading is edited, no rule is added, removed or renumbered, and no rule ID changes.

- [x] 0.1 The branch is `priority-orders-every-player`, named for this change directory, and it
  is branched from an up-to-date `main`.

### Scope and coverage

Three ruleset documents, no spec delta: **ten edits and sixteen non-edit tasks** (0.1 and
5.1 – 5.15), before the repairs recorded in section 6.

| `proposal.md` item | Task | Path |
|---|---|---|
| `FLOW-001` states the player count | 1.1 | `docs/03-game-flow.md` |
| `FLOW-002` steps 2 and 3 | 2.1 | `docs/03-game-flow.md` |
| `FLOW-003` — the whole mechanism | 2.2 | `docs/03-game-flow.md` |
| `FLOW-009` — "both players" | 2.3 | `docs/03-game-flow.md` |
| The Turn Sequence diagram | 2.4 | `docs/03-game-flow.md` |
| The Summary, points 1 to 3 | 2.5 | `docs/03-game-flow.md` |
| Glossary *Priority* corrected | 3.1 | `docs/14-glossary.md` |
| Glossary *Activation Order* added | 3.2 | `docs/14-glossary.md` |
| `06-deployment.md` Design Philosophy | 4.1 | `docs/06-deployment.md` |
| `06-deployment.md` Design Notes | 4.2 | `docs/06-deployment.md` |

**Untouched, deliberately:** `03-game-flow.md`'s Purpose and Design Philosophy, including the
name *alternating unit activation system* (`design.md`, Decision 9) and the Summary's closing
paragraph that repeats it — both lines are checked by task 5.10 rather than assumed;
`FLOW-004` – `FLOW-008`, `FLOW-010` – `FLOW-013`; `CORE-006`, `CORE-009`, `CBT-010` and the
glossary's *Turn*, all of which cite or describe the turn sequence and were read against the new
text — each is true at any player count; `MOVE-017`'s friendly and enemy units; every rule in
`06-deployment.md`, both edits there being narrative sentences; `openspec/specs/` (no delta —
`design.md`, Decision 10); `CHANGELOG.md` and every `**Version:**` header.

---

## 1. `docs/03-game-flow.md` — `FLOW-001`

- [x] 1.1 Replace this anchor — one line, the sentence introducing the numbered list:

```
Before the first Turn:
```

with:

```
StudCraft is played by **two or more players**, each fielding their own force. No upper limit is stated because one already exists and is physical: how many armies fit on a table is settled by the battlefield and the Deployment Volume the players agree below (steps 3 and 4; `06-deployment.md`, DEP-001, DEP-002), with the models in front of them.

Before the first Turn:
```

  The numbered list below it is not touched, and no step is added or renumbered — the paragraph
  after the list ("Step 2 comes before step 5 deliberately") still names the right steps.

---

## 2. `docs/03-game-flow.md` — `FLOW-002`, `FLOW-003`, `FLOW-009`, the diagram and the Summary

- [x] 2.1 In `FLOW-002`, replace this anchor — steps 2 and 3 together:

```
2. Players alternate activating one unit at a time.
3. Continue until every unit has been activated once. If a player has no unactivated units remaining, the other player continues activating their own remaining units consecutively, with no alternation, until they too have all been activated.
```

with:

```
2. Players activate one unit each, in the Activation Order (FLOW-003).
3. Continue until every unit has been activated once. A player with no unactivated units left is skipped, and the order carries on without them.
```

  Steps 1, 4 and 5 are not touched. The anchor starts at `2.` deliberately: the line
  `1. Determine Priority.` occurs twice in this file (here and in the Summary) and is not a
  usable anchor on its own.

  Step 3 is now the only place a **rule** states the skip: task 2.2's `FLOW-003` does not repeat
  it. Task 2.5's Summary point 3 does mention it, which is what a Summary is for.

- [x] 2.2 Replace this anchor — the entire body of `FLOW-003`, from the first line after its
  heading to the last line before the `---` that closes it. The heading `# FLOW-003 — Priority`
  is **not** part of the anchor and is not touched:

```
At the beginning of every Turn, both players roll **1D6**.

The player with the highest result gains **Priority**.

On a tie, both players roll again until the tie is broken.

The player with Priority chooses one of the following:

- Activate one of their own units now, keeping the activation.
- Cede Priority, letting the other player activate first instead.

This is a single choice made once, at the start of the Turn. Whichever player activates first, both players then alternate activating one unit at a time (per FLOW-002) for the remainder of the Turn, until one player has no unactivated units left — at which point the other continues activating consecutively (FLOW-002).

Priority is determined again at the beginning of every Turn.
```

with:

```
At the beginning of every Turn, every player rolls **1D6**, simultaneously.

The results set the **Activation Order** for that Turn, read from the highest result to the lowest. The player who takes first place in it holds **Priority**. A player with no units left on the battlefield does not roll and takes no place in the order.

Where players tie, each set of players who rolled the same result rolls again, and that roll orders their places among themselves and no others — every other place stands as the first roll left it, so no lower result can overtake a higher one. A tie inside a re-roll is broken the same way.

The player with Priority chooses one of the following:

- Activate one of their own units now, keeping the activation.
- Cede Priority, moving to the last place in the Activation Order. Every other player moves up one place, so the player who was second activates first.

This is a single choice, made once, at the start of the Turn, and only the player holding Priority makes it. A player who reaches first place because someone else ceded does not inherit the choice — otherwise a Turn could open with every player ceding in sequence and the order arriving back where it started.

Players then activate one unit each in Activation Order, cycling through it for the remainder of the Turn (FLOW-002).

Priority and the Activation Order are determined again at the beginning of every Turn.
```

  Three clauses here are load-bearing and must land exactly as written. Priority is attached to
  **first place in the order**, not to the highest roll, so a tie for the top place has an answer.
  The cede bullet names **the player who was second**, not the second-highest roll, because after
  a re-roll those need not be the same player. And the skip is not restated here at all —
  `FLOW-002` step 3 owns it, and this rule points at `FLOW-002` for the activation procedure that
  contains it.

- [x] 2.3 In `FLOW-009`, replace this anchor — one line:

```
A Turn ends when every unit from both players has completed one activation.
```

with:

```
A Turn ends when every unit from every player has completed one activation.
```

- [x] 2.4 In the `Turn Sequence` diagram, replace this anchor — the twelve lines running from
  `Determine Priority` down to and including `Alternate Unit Activations`. `Start Turn` and the
  `↓` beneath it sit **above** the anchor, inside the same fence, and are not touched; everything
  from the next `↓` below the anchor onward is not touched either; and the fence's own backtick
  lines are not touched:

```
Determine Priority

↓

Priority player chooses:
• Activate own unit now (continue)
or
• Cede Priority (opponent activates first)

↓

Alternate Unit Activations
```

with:

```
Determine Priority
(every player rolls 1D6 — highest to lowest sets the Activation Order)

↓

Priority player chooses:
• Activate own unit now (continue)
or
• Cede Priority (moves to last place; the player who was second activates first)

↓

One Unit Each, In Activation Order
```

- [x] 2.5 In the `Summary`, replace this anchor — points 1, 2 and 3 together:

```
1. Determine Priority.
2. The Priority player chooses who activates first.
3. Players alternate activating one unit at a time.
```

with:

```
1. Determine Priority — every player rolls 1D6, and the results set the Activation Order.
2. The Priority player chooses whether to activate first or to cede and take the last place.
3. Players activate one unit each in that order, skipping any player with nothing left to activate.
```

  Points 4 to 8 and the closing paragraph below them are not touched. That paragraph keeps the
  phrase **alternating unit activations** — see `design.md`, Decision 9.

---

## 3. `docs/14-glossary.md` — *Priority*, and a new *Activation Order*

This glossary is in **append order**, not alphabetical and not thematic. So the corrected entry
stays where it is and the new one goes at the end of the file, after *Interactive Element*.

- [x] 3.1 Replace this anchor — the single-line body of the `## Priority` entry. The `## Priority`
  heading itself is **not** part of the anchor and is not touched, and nothing moves:

```
The right to choose whether to activate first or second in a Turn, held by the player who rolled highest and cedable to the opponent. See `03-game-flow.md`, FLOW-003.
```

with:

```
The right, held by the player who takes first place in the Activation Order, to choose whether to activate first or to move to the last place instead. See `03-game-flow.md`, FLOW-003.
```

- [x] 3.2 At the end of the file, replace this anchor — the document's closing motto, which is
  the last non-empty line:

```
> **Every Brick Matters.**
```

with:

```
## Activation Order

The order in which players activate their units through a Turn, set at the start of each Turn when Priority is determined and read from the highest result to the lowest, and changed by a cede (`03-game-flow.md`, FLOW-003). A player with no units left on the battlefield takes no place in it.

---

> **Every Brick Matters.**
```

  The `---` already above the anchor stays where it is and becomes the separator before
  *Activation Order*. The motto must remain the last non-empty line of the file:
  `scripts/lint_ruleset.py` checks exactly that.

---

## 4. `docs/06-deployment.md` — two narrative sentences

Neither edit touches a rule. Both remove a two-player assumption from prose that would otherwise
contradict the `FLOW-001` sentence task 1.1 adds.

- [x] 4.1 In the `Design Philosophy` section, replace this anchor — the end of one line:

```
the second thing bounding it is a ceiling both players agreed to (DEP-001), not a price one of them pays.
```

with:

```
the second thing bounding it is a ceiling the players agreed to (DEP-001), not a price any one of them pays.
```

- [x] 4.2 In the `Design Notes` section — **not** the `Summary`, which is a separate section below
  it and contains no such sentence — replace this anchor, the end of one line:

```
again by the volume both players agreed to.
```

with:

```
again by the volume the players agreed to.
```

---

## 5. Verification

Run each command and write down what it actually returned. If a figure differs from the one
stated here, **stop and report it** — do not edit a document to make it match. Every "before"
figure below was produced by running the command against the pre-change files.

- [x] 5.1 `grep -c "both players" docs/03-game-flow.md` — before: **4**, after: **0**.

- [x] 5.2 `grep -c "the other player" docs/03-game-flow.md` — before: **2**, after: **0**.

- [x] 5.3 `grep -c "opponent" docs/03-game-flow.md` — before: **1**, after: **0**.

- [x] 5.4 `grep -c "opponent" docs/14-glossary.md` — before: **1**, after: **0**.

- [x] 5.5 `grep -c "both players agreed to" docs/06-deployment.md` — before: **2**, after: **0**.

- [x] 5.6 `grep -c "two or more players" docs/03-game-flow.md` — before: **0**, after: **1**.

- [x] 5.7 `grep -c "simultaneously" docs/03-game-flow.md` — before: **0**, after: **1**.

- [x] 5.8 `grep -c "^## Activation Order$" docs/14-glossary.md` — before: **0**, after: **1**.

- [x] 5.9 `grep -c "does not roll and takes no place" docs/03-game-flow.md` — before: **0**,
  after: **1**. This is the clause that keeps an eliminated player out of the order, and out of
  Priority with it.

- [x] 5.10 `grep -c "alternating unit activation" docs/03-game-flow.md` — before: **2**, after:
  **2**. Two lines carry it, the Purpose (line 13) and the Summary's closing paragraph, and both
  are deliberately kept — this check is what makes "untouched" verifiable rather than asserted.

- [x] 5.11 `python3 scripts/lint_ruleset.py` — `Checked 15 docs, no structural issues found.`

- [x] 5.12 `python3 scripts/check_task_anchors.py priority-orders-every-player` — must **exit 0**.
  Report the line it printed. Every anchor above is expected to report **zero** matches once the
  change has been applied and its boxes are ticked; on an unticked task a zero match is a defect.

- [x] 5.13 `python3 scripts/check_delta_coverage.py` — must **exit 0**. This change adds no delta,
  so the count it prints is whatever other unarchived changes contribute; report the line and do
  not check the number.

- [x] 5.14 `python3 scripts/preflight.py` — must **exit 0**; report the summary line. This is the
  repository's required local gate and it is what covers this change.

  **Do not run `openspec validate priority-orders-every-player`.** It exits 1 on this change with
  `Change must have at least one delta. No deltas found.` — the CLI treats a delta-free change as
  an error, and this change is deliberately delta-free (`design.md`, Decision 10).
  `scripts/preflight.py` already works around exactly this, validating a change only when it
  ships deltas.

- [x] 5.15 `git status --short` — three modified documents, `docs/03-game-flow.md`,
  `docs/06-deployment.md` and `docs/14-glossary.md`, plus the untracked change directory
  `openspec/changes/priority-orders-every-player/` reported as a single `??` entry. Anything else
  in the list is a mismatch: report it and stage nothing.

---

## 6. Repairs after the audit of the applied text

The applied text was audited and returned five findings and one observation. All five are
repaired here. Every anchor in this section was checked against the **applied** files, not the
pre-change ones, and occurs exactly once.

Two of the repairs are wording the change itself introduced; three are places where the new text
leans on something it should not. The reasoning for each is recorded in `design.md` by tasks
6.7 – 6.9 rather than only here.

- [x] 6.1 In `FLOW-003`, replace this anchor — the first two paragraphs of the rule, together:

```
At the beginning of every Turn, every player rolls **1D6**, simultaneously.

The results set the **Activation Order** for that Turn, read from the highest result to the lowest. The player who takes first place in it holds **Priority**. A player with no units left on the battlefield does not roll and takes no place in the order.
```

with:

```
At the beginning of every Turn, every player with units still on the battlefield rolls **1D6**, simultaneously. A player with none does not roll, and takes no place in the order those rolls set.

The results set the **Activation Order** for that Turn, read from the highest result to the lowest. The player in first place **when the order is determined** holds **Priority**.
```

  Two repairs in one anchor, both about where a qualifier sits. The exclusion now qualifies the
  sentence it is an exception to, instead of arriving a paragraph later attached to the sentence
  that grants Priority. And Priority is fixed to first place **at the moment of determination**,
  because a cede moves everyone up a place and the rule says four lines below that the player who
  inherits first place does not inherit the choice.

- [x] 6.2 In `FLOW-002`, replace this anchor — step 2:

```
2. Players activate one unit each, in the Activation Order (FLOW-003).
```

with:

```
2. Players activate one unit each, one at a time, in the Activation Order (FLOW-003).
```

  `11-combat.md`, `CBT-010` cites `FLOW-002` for the claim that StudCraft's default activation is
  "strictly one unit at a time", and the pre-change step 2 said so in those words. The words are
  restored so the citation lands on text that carries it.

- [x] 6.3 In `FLOW-003`, replace this anchor — the paragraph after the cede rule:

```
Players then activate one unit each in Activation Order, cycling through it for the remainder of the Turn (FLOW-002).
```

with:

```
Activation then follows the Activation Order for the remainder of the Turn, as FLOW-002 sets out.
```

  This sentence and `FLOW-002` step 2 stated the same procedure in the same words, each citing
  the other. `FLOW-002` owns the Turn's structure, so it keeps the statement and `FLOW-003`
  becomes a pointer — the same consolidation `design.md` Decision 7 already applied to the skip.

- [x] 6.4 In `FLOW-001`, replace this anchor — the paragraph task 1.1 added:

```
StudCraft is played by **two or more players**, each fielding their own force. No upper limit is stated because one already exists and is physical: how many armies fit on a table is settled by the battlefield and the Deployment Volume the players agree below (steps 3 and 4; `06-deployment.md`, DEP-001, DEP-002), with the models in front of them.
```

with:

```
StudCraft is played by **two or more players**, each fielding their own force. No upper limit is written here. The players agree the battlefield and the Deployment Volume before any force is built (steps 3 and 4; `06-deployment.md`, DEP-001), and how many forces the table will hold is settled in that agreement, with the models in front of them — a number written into this rule would settle it again in advance, for tables it has never seen.
```

  The replaced sentence asserted that the battlefield and the Deployment Volume *bound* the
  player count. No rule states that relation: `DEP-001` says a Deployment Volume "may have any
  dimensions agreed upon by the players" and `DEP-009` says "No upper limit exists". The new
  wording rests on the agreement itself, which `DEP-001` does establish, and asserts no
  inequality the ruleset has not written down.

- [x] 6.5 In `docs/14-glossary.md`, replace this anchor — the body of the *Priority* entry:

```
The right, held by the player who takes first place in the Activation Order, to choose whether to activate first or to move to the last place instead. See `03-game-flow.md`, FLOW-003.
```

with:

```
The right, held by the player in first place when the Activation Order is determined, to choose whether to activate first or to move to the last place instead. See `03-game-flow.md`, FLOW-003.
```

  Same repair as 6.1, in the restatement. As it stood, the entry granted the right to whoever is
  first at any moment, which after a cede is a player `FLOW-003` explicitly denies it to.

- [x] 6.6 In `docs/14-glossary.md`, replace this anchor — the body of the *Activation Order*
  entry:

```
The order in which players activate their units through a Turn, set at the start of each Turn when Priority is determined and read from the highest result to the lowest, and changed by a cede (`03-game-flow.md`, FLOW-003). A player with no units left on the battlefield takes no place in it.
```

with:

```
The order in which players activate their units through a Turn: every player rolls 1D6 at its start, and the order runs from the highest result to the lowest. A player who cedes Priority moves to its last place. A player with no units left on the battlefield takes no place in it at all. See `03-game-flow.md`, FLOW-003.
```

  Two defects. The entry defined the order by reference to Priority while the *Priority* entry
  defined Priority by reference to the order, so neither resolved inside the glossary. And "a
  cede" is a noun no rule uses — `FLOW-003` says "Cede Priority" and "someone else ceded".

### Records in the change's own documents

- [x] 6.7 In `openspec/changes/priority-orders-every-player/design.md`, Decision 8, replace this
  anchor — the paragraph after the chain block:

```
Note that it is the **second** link that does the work, not the first. `DEP-001` charges a
Deployment Volume **per player** and `DEP-002` spends it per army, so N armies do not fit inside
one volume and no inequality of the form "players × army ≤ volume" is available. What bounds the
player count is how many volumes the agreed battlefield holds — a question the players answer
when they agree the battlefield, with the models in front of them, which is what Principle 1
asks for. Placement is not the ruleset's at all (`CORE-005`).
```

with:

```
Note that it is the **second** link that does the work, not the first. `DEP-001` charges a
Deployment Volume **per player** and `DEP-002` spends it per army, so N armies do not fit inside
one volume and no inequality of the form "players × army ≤ volume" is available. What bounds the
player count is how many volumes the agreed battlefield holds — a question the players answer
when they agree the battlefield, with the models in front of them, which is what Principle 1
asks for. Placement is not the ruleset's at all (`CORE-005`).

**The second link is not written down either, and `FLOW-001` therefore does not lean on it.**
`DEP-001` says a Deployment Volume "may have any dimensions agreed upon by the players" and
`DEP-009` says "No upper limit exists"; nothing relates either to the battlefield. `WPN-005`
already asserts the relation and cites `FLOW-001` for it — "the Deployment Volume [is bounded] by
the battlefield the players agree on before it" — and `FLOW-001` has never said so. An earlier
draft of this change's `FLOW-001` paragraph made the same assertion, which would have left the
same unwritten relation asserted in two rules and defined in none. Task 6.4 rewrote it to rest on
the agreement itself, which `DEP-001` does establish. Writing the link down properly, and
re-aiming `WPN-005` at wherever it lands, is a change of its own and is named under *What this
change deliberately leaves open* below.
```

- [x] 6.8 In `openspec/changes/priority-orders-every-player/design.md`, replace this anchor — the
  last bullet of the list under *What this change deliberately leaves open*:

```
- **Turn-order effects a scenario might want.** A scenario may already restrict otherwise-legal
  actions (`FLOW-013`). Whether it may also fix, seed or freeze the Activation Order is not stated
  here, in either direction.
```

with:

```
- **Turn-order effects a scenario might want.** A scenario may already restrict otherwise-legal
  actions (`FLOW-013`). Whether it may also fix, seed or freeze the Activation Order is not stated
  here, in either direction.
- **Whether the Deployment Volume is bounded by the battlefield.** `WPN-005` says it is and cites
  `FLOW-001`; `FLOW-001` does not say it, `DEP-001` lets the players agree any dimensions, and
  `DEP-009` says no upper limit exists. The relation is real at the table and unwritten in the
  ruleset. This change declined to write it — a rule about deployment does not belong in a
  proposal about turn order, and `WPN-005`'s citation needs re-aiming in the same pass. Task 6.4
  removed this change's own dependence on it.
- **Reading the Activation Order off the table.** The dice are rolled simultaneously and openly
  and then, in the current rules, forgotten — the order becomes something the players remember,
  which is easy at two and is state at five. Leaving each die where it fell, and moving your own
  to the end of the line when you cede, would make the order physical. Principle 1 and Principle 6
  both point that way and no rule currently says either. It is left open rather than adopted
  because it is a new rule about components on the table, not a repair to this one, and nothing
  here is undecided without it.
```

- [x] 6.9 In `openspec/changes/priority-orders-every-player/proposal.md`, replace this anchor —
  the `FLOW-001` bullet under *What Changes*:

```
- **`FLOW-001`** states the player count for the first time: **two or more**, with no upper limit. The limit is not written because it already exists — the battlefield agreed in step 3 and the Deployment Volume agreed in step 4 (`06-deployment.md`, DEP-001) bound how many forces fit on a table, and a number written into `FLOW-001` would bound it a second time and worse.
```

with:

```
- **`FLOW-001`** states the player count for the first time: **two or more**, with no upper limit. The limit is not written because the players already settle it when they agree the battlefield and the Deployment Volume (steps 3 and 4; `06-deployment.md`, DEP-001), with the models in front of them. The rule asserts no relation between those two that the ruleset has not written down — see `design.md`, Decision 8, which records why not, and what a later change would have to write.
```

### Verification after section 6

- [x] 6.10 `grep -c "one at a time" docs/03-game-flow.md` — before: **0**, after: **1**. The phrase
  `CBT-010` cites is back in `FLOW-002` step 2.

- [x] 6.11 `grep -c "when the order is determined" docs/03-game-flow.md` — before: **0**, after:
  **1**.

- [x] 6.12 `grep -c "when the Activation Order is determined" docs/14-glossary.md` — before: **0**,
  after: **1**.

- [x] 6.13 `grep -c "changed by a cede" docs/14-glossary.md` — before: **1**, after: **0**.

- [x] 6.14 `grep -c "does not roll" docs/03-game-flow.md` — before: **1**, after: **1**. The clause
  moved paragraph; it was not duplicated and was not dropped.

- [x] 6.15 `grep -c "cycling through it" docs/03-game-flow.md` — before: **1**, after: **0**.

- [x] 6.16 `grep -c "would settle it again in advance" docs/03-game-flow.md` — before: **0**,
  after: **1**.

- [x] 6.17 `python3 scripts/lint_ruleset.py` — `Checked 15 docs, no structural issues found.`

- [x] 6.18 `python3 scripts/preflight.py` — must **exit 0**; report the summary line. Do **not**
  run `openspec validate` directly, for the reason given in task 5.14.

- [x] 6.19 `grep -c "^- \[ \]" openspec/changes/priority-orders-every-player/tasks.md` — after
  ticking every box in this section: **0**.
