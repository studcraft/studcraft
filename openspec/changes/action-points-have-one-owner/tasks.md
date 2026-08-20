# Tasks — Action Points have one owner

## How to apply this change

Every anchor below was checked with exact-substring matching against the
pre-change files and occurs **exactly once in the file its task names**.
Replace the whole anchor.

If an anchor returns anything other than 1, **stop and report it** rather than
guessing which occurrence was meant. Never edit a document to make a
verification command pass — report the mismatch instead.

### How to read the replacement blocks

The triple-backtick fence marks where the text starts and stops. **The fence is
not part of the text** — do not write the backticks into the document.

A `#` heading or a `---` horizontal rule inside a fence is real markdown that
must land in the file as markdown, not as quoted text. Tasks 2.2 and 2.3 each
run from a retired rule's heading through the heading of the rule that follows
it, and repeat that second heading as a **landmark** — a line that must stay in
the file, not an edit.

### This file was revised after its audit

The audit returned twelve findings, two of them blockers, and **all of them are
folded into the tasks below rather than added as a repair section** — nothing
had been applied yet, so there was nothing to repair. What the audit found:

- **`TODO.md` quotes `CORE-006`'s list verbatim.** Deleting the list breaks
  `check_todo_quotes.py`, which is preflight check 5 and a CI gate. Underneath
  the mechanical break: **`Reload (future rule)` is not an action, it is a
  declared gap** — the only one in the three lists. Tasks 4.1 and 4.2 move that
  declaration to `WPN-017`, where a weapons gap belongs, and re-source the
  `TODO.md` entry to it.
- **`DMG-019` reads back into the list.** It says the repair action is "the
  same action `02-core-rules.md` CORE-006 lists as 'Stand up'". Task 3.1
  rewords it. Nothing in the original verification caught this: `lint_ruleset`
  passes because the *ID* still exists.
- **`01-foundations.md` holds a fourth action list** and the same bold-number
  pattern the proposal calls the clearest instance of the defect. Task 3.2.
- **`CODE_OF_DESIGN.md` Principle 8** names `CORE-006` the authority "on the
  amount **and on what may be spent**" — the half this change relocates. Task
  5.1.
- **`TRN-005`, `TRN-006` and the glossary *Activation* entry** each state or
  cite the number against `FLOW-004`. Tasks 3.3, 3.4, 3.5.
- `scripts/check_todo_quotes.py`'s docstring names `FLOW-005` as an example.
  Task 5.2.

### The three things this change must not do

**Three rule IDs are retired, and their numbers are never reissued.**
`FLOW-005`, `FLOW-006` and `FLOW-011` are deleted outright. Do not renumber
`FLOW-007` down into the gap, and do not leave a stub — `system/documentation-standards.md`
(Naming Conventions).

**`CORE-006` keeps both of its claims.** Every unit receives exactly **3**
Action Points per activation, and no unit gains additional AP through its
profile. Eight rules and two glossary entries read it for those. If a
replacement block would alter either, it is wrong — stop and report it.

**No gameplay value changes.** Three AP, spent in any legal order, one
activation per unit per Turn. Every action still costs what its own rule says,
and nothing gains or loses an AP cost here.

- [x] 0.1 The branch is `action-points-have-one-owner`, named for this change
  directory, and it is branched from an up-to-date `main`.

### Scope and coverage

Seven ruleset documents, `TODO.md`, `CODE_OF_DESIGN.md` and one script:
**fifteen anchor pairs across ten files.** No spec delta — `design.md`,
Decision 4.

| `proposal.md` item | Task | Path |
|---|---|---|
| `CORE-006` — the example list goes, the ownership clause arrives | 1.1 | `docs/02-core-rules.md` |
| `FLOW-004` — stops printing the number | 2.1 | `docs/03-game-flow.md` |
| `FLOW-005` and `FLOW-006` — retired | 2.2 | `docs/03-game-flow.md` |
| `FLOW-011` — retired | 2.3 | `docs/03-game-flow.md` |
| `FLOW-012` — loses its three-step list and its repeated closing line | 2.4 | `docs/03-game-flow.md` |
| `DMG-019` — stops reading back into a deleted list | 3.1 | `docs/16-damage-system.md` |
| `01-foundations.md` — the fourth action list goes | 3.2 | `docs/01-foundations.md` |
| `TRN-005` — cites the allotment, not `FLOW-004`, for the number | 3.3 | `docs/09-transport.md` |
| `TRN-006` — stops restating the number uncited | 3.4 | `docs/09-transport.md` |
| Glossary ***Activation*** entry | 3.5 | `docs/14-glossary.md` |
| Glossary ***AP*** entry | 3.6 | `docs/14-glossary.md` |
| Reload is declared in `WPN-017` | 4.1 | `docs/10-weapons.md` |
| `TODO.md`'s Reload entry re-sourced | 4.2 | `./TODO.md` |
| `check_todo_quotes.py`'s docstring example | 5.1 | `scripts/check_todo_quotes.py` |
| `CODE_OF_DESIGN.md` Principle 8 | 5.2 | `./CODE_OF_DESIGN.md` |

**Untouched, deliberately:** `CORE-006`'s allotment and no-profile sentence.
`FLOW-004`'s activation procedure. `FLOW-012`'s "no hidden activation values"
and "construction determines what a unit can do". `FLOW-007`, which sits
between two retirements and is not renumbered. **`MOVE-007` and `INF-009`**,
which derive a consequence from the number rather than restating the allotment
— `design.md`, Decision 5. `03-game-flow.md`'s Summary and its Turn Sequence
diagram, for the same reason. `openspec/specs/`. `CHANGELOG.md` and every
version header.

---

## 1. `docs/02-core-rules.md` — `CORE-006` becomes the sole owner

- [x] 1.1 In `docs/02-core-rules.md`, `CORE-006`, replace this anchor — the second line and the example list below it. The rule's opening line and its closing paragraph are **not** part of the anchor and are not touched:

```
Action Points represent everything a unit can do during its activation.

Examples include:

- Move
- Fire
- Open a door
- Close a door
- Embark
- Disembark
- Stand up (see `16-damage-system.md`, DMG-019, Repairs)
- Reload (future rule)
- Operate mechanisms
```

with:

```
Action Points represent everything a unit can do during its activation, and what any one action costs is stated by the rule that governs that action.
```

  **The list is deleted, not moved.** It is one of four that disagree with each other, and a list of what other rules do is a snapshot a command can print (`system/documentation-standards.md`, How a Rule Is Written) — the same ground `core-stops-describing-units` deleted `CORE-002`'s six-item list on.

  **Two items in it are not actions, and both are handled elsewhere in this change.** *Stand up* is `DMG-019`'s repair action, and `DMG-019` reads back into this list — task 3.1. *Reload (future rule)* is a declared gap that `TODO.md` quotes verbatim — tasks 4.1 and 4.2.


---

## 2. `docs/03-game-flow.md`

Tasks 2.1 to 2.4 are one edit split four ways. **Apply all four.**

- [x] 2.1 In `docs/03-game-flow.md`, `FLOW-004`, replace this anchor — the rule's opening through the line about spending order. The three lines after it are **not** part of the anchor and stay:

```
When a unit is activated, it immediately receives:

**3 Action Points (AP)**

(see `02-core-rules.md`, CORE-006, for the canonical definition)

The player may spend these AP in any legal order.
```

with:

```
When a unit is activated it immediately receives its Action Points (`02-core-rules.md`, CORE-006), and the player may spend them in any legal order.
```

  **The rule named where the truth lived and copied it anyway** — it printed the number in bold and cited `CORE-006` "for the canonical definition" on the next line. It now cites and stops. **The player spends, the unit receives**, and the replacement keeps that distinction the original made.


- [x] 2.2 In `docs/03-game-flow.md`, replace this anchor — the whole of `FLOW-005` and the whole of `FLOW-006`, through the heading of the rule that follows them. **`# FLOW-007 — Combining Actions` is a landmark**: it must stay in the file, at the same level, and is in the anchor only to bound it. The `---` above `# FLOW-005` stays and becomes the separator before `FLOW-007`:

```
# FLOW-005 — Universal Action Points

The 3 AP defined in CORE-006 apply identically to every unit type in StudCraft, with no exceptions:

- Infantry
- Vehicles
- Walkers
- Hovercraft
- Future unit types

No unit gains additional AP through its profile.

Differences between units emerge from their physical construction, not from hidden statistics.

---

# FLOW-006 — Common Actions

Action Points may be spent on actions such as:

- Move
- Rotate
- Attack
- Open a door
- Close a door
- Open a ramp
- Close a ramp
- Embark
- Disembark
- Interact with terrain
- Operate scenario objectives

Each action's AP cost is defined in its corresponding rule document.

---

# FLOW-007 — Combining Actions
```

with:

```
# FLOW-007 — Combining Actions
```

  **Two rules leave in one edit, and neither number is ever reissued.** `FLOW-005`'s three claims are `CORE-006`'s allotment, `CORE-006`'s no-profile sentence *word for word*, and `FLOW-012`'s construction-not-statistics. Its unit-type list survives where it belongs: `openspec/specs/action-economy` enumerates the same five in its scenario. `FLOW-006`'s one real sentence went into `CORE-006` in task 1.1.

  **Do not renumber `FLOW-007` into the gap and do not leave a stub.**


- [x] 2.3 In `docs/03-game-flow.md`, replace this anchor — the whole of `FLOW-011`, through the heading of the rule that follows it. **`# FLOW-012 — No Hidden Statistics` is a landmark** and does not change:

```
# FLOW-011 — Action Economy

Action Points are the universal resource in StudCraft.

Every meaningful action consumes AP.

Examples include:

- Moving
- Attacking
- Opening doors
- Closing doors
- Operating ramps
- Embarking
- Disembarking
- Interacting with objectives

Players must decide how to spend their limited AP each activation.

---

# FLOW-012 — No Hidden Statistics
```

with:

```
# FLOW-012 — No Hidden Statistics
```

  "Action Points are the universal resource in StudCraft" is `CORE-006`. "Players must decide how to spend their limited AP" is an observation about playing well, not a rule.

  **"Every meaningful action consumes AP" is dropped and not preserved**, deliberately: the ruleset contains actions that cost nothing — `INF-006` crosses low obstacles freely, `INF-009` takes slopes "at no additional Action Point cost", `INF-004` requires no rotation — so as an absolute it was already false (`design.md`, Decision 7).


- [x] 2.4 In `docs/03-game-flow.md`, `FLOW-012`, replace this anchor — the rule's opening through its closing line. **The closing line is inside the anchor on purpose**: leaving it would have it restate the sentence directly above it:

```
StudCraft does not use hidden activation values.

Every unit follows the same activation sequence:

- Gain AP (CORE-006).
- Spend AP.
- End activation.

Construction determines what a unit can do.

The activation system remains identical for all units.
```

with:

```
StudCraft does not use hidden activation values: every unit receives the same allotment (`02-core-rules.md`, CORE-006) and follows the same activation sequence (FLOW-004). Construction determines what a unit can do.
```

  **The three-step list restates `FLOW-004`**, which owns the activation procedure. The citation of `CORE-006` lived inside that list and is kept — `FLOW-012` is one of the rules that cite `CORE-006`, and dropping the list without keeping the citation would have removed one.

  **The closing line goes with it.** "The activation system remains identical for all units" says what the new sentence says; keeping it would introduce the defect this change removes, inside the change that removes it.


---

## 3. What reads back into the deleted lists

Each of these states or cites the number, or points at a list that stops
existing. All five were found by the audit, not by the original pass.

- [x] 3.1 In `docs/16-damage-system.md`, `DMG-019`, replace this anchor — the rule's first line:

```
A unit may spend **1 Action Point**, once per activation, to repair its own Wounded component, restoring it to Operational (`Wounded → Operational`) — for infantry, this is the same action `02-core-rules.md` CORE-006 lists as "Stand up."
```

with:

```
A unit may spend **1 Action Point**, once per activation, to repair its own Wounded component, restoring it to Operational (`Wounded → Operational`). For an infantry model that repair is standing up.
```

  **Task 1.1 deletes the list this sentence points at.** `lint_ruleset.py` would not have caught it — the ID still exists; only the claim about what it *lists* becomes false. "Stand up" stops being a named action in `CORE-006` and becomes what it always was: this rule's own repair, described here.


- [x] 3.2 In `docs/01-foundations.md`, the `# Action Points (AP)` section, replace this anchor — the list and the line introducing it. The bold number above and "The same resource is shared across every unit type." below are **not** part of the anchor and stay:

```
Action Points are spent to perform actions such as:

- Move
- Rotate
- Attack
- Open doors
- Close doors
- Embark
- Disembark
```

with:

```
What any one action costs is stated by the rule that governs that action.
```

  **The fourth list.** `01-foundations.md` defines no rules, so it may *mention* the number while citing `CORE-006` — which it already does, and which task 2.1 leaves standing. What it may not do is carry a fifth copy of an enumeration that goes stale, which is Decision 1's argument and does not depend on the container being a rule.


- [x] 3.3 In `docs/09-transport.md`, `TRN-005`, replace this anchor — the rule's second paragraph, first sentence:

```
The AP is spent from the embarking unit's own pool, during its own activation (`03-game-flow.md`, FLOW-004) — the same 3 AP it can also spend moving, attacking, or otherwise acting that same activation (`FLOW-007`).
```

with:

```
The AP is spent from the embarking unit's own pool, during its own activation (`03-game-flow.md`, FLOW-004) — the same allotment (`02-core-rules.md`, CORE-006) it can also spend moving, attacking, or otherwise acting that same activation (`FLOW-007`).
```

  The citation of `FLOW-004` sat directly against the number, and after task 2.1 a reader following it lands on a rule that points elsewhere. `FLOW-004` keeps the citation it earns — the activation — and the number cites its owner.


- [x] 3.4 In `docs/09-transport.md`, `TRN-006`, replace this anchor — one line:

```
The AP is spent from the disembarking unit's own pool, during its own activation — a unit that begins its activation already embarked spends AP to disembark, then may spend any AP remaining from the same 3 AP allotment to move, attack, or otherwise act.
```

with:

```
The AP is spent from the disembarking unit's own pool, during its own activation — a unit that begins its activation already embarked spends AP to disembark, then may spend whatever remains of its allotment (`02-core-rules.md`, CORE-006) to move, attack, or otherwise act.
```

  **A rule restating the number with no citation at all**, which is the same defect as `FLOW-004`'s and was not in the original pass.


- [x] 3.5 In `docs/14-glossary.md`, the `## Activation` entry, replace this anchor — the entry's body:

```
The period during which one unit receives 3 AP and performs actions. See `03-game-flow.md`, FLOW-004 and `02-core-rules.md`, CORE-006.
```

with:

```
The period during which one unit receives its Action Points (`02-core-rules.md`, CORE-006) and performs actions. The procedure is `03-game-flow.md`, FLOW-004.
```

  `system/proposal-review.md` ("The Summary Is Part of the Rule") — a glossary entry is a restatement and is checked in the same pass as the rule. This one printed the number beside a citation of `FLOW-004`, which after task 2.1 no longer holds it.


- [x] 3.6 In `docs/14-glossary.md`, the `## AP` entry, replace this anchor — the entry's second line:

```
The universal action economy. See `02-core-rules.md`, CORE-006 and `03-game-flow.md`, FLOW-011.
```

with:

```
The universal action economy. See `02-core-rules.md`, CORE-006.
```

  `FLOW-011` stops existing in task 2.3.


---

## 4. Reload is a declared gap, not an action

`- Reload (future rule)` was the one item in `CORE-006`'s list that named no
rule anywhere. It is a gap the ruleset declares about itself, and `TODO.md`
quotes it verbatim — `scripts/check_todo_quotes.py` matches by exact substring,
so task 1.1 breaks that check unless the declaration moves.

**It moves to the weapons document, where a weapons gap belongs.** Apply 4.1
before 4.2.

- [x] 4.1 In `docs/10-weapons.md`, `WPN-017`, replace this anchor — the whole rule body:

```
Future supplements may introduce:

- Flamethrowers
- Explosive Weapons
- Beam Weapons
- Energy Weapons
- Indirect Fire
- Smoke Launchers

These must continue to follow the StudCraft Weapon Construction Standard.
```

with:

```
Future supplements may introduce:

- Flamethrowers
- Explosive Weapons
- Beam Weapons
- Energy Weapons
- Indirect Fire
- Smoke Launchers
- Reloading

These must continue to follow the StudCraft Weapon Construction Standard. No weapon in the current construction rules runs out of ammunition, so nothing reloads today.
```

  **This is where the Reload gap now lives.** `CORE-006` declared it as an action a unit might spend AP on; it is not one — no weapon has ammunition to spend. Stated here it sits beside the other things weapons may one day do, in the document that would define it. The closing sentence is what `TODO.md` needs to keep quoting a live declaration.


- [x] 4.2 In `./TODO.md`, the `### Reload` entry, replace this anchor — the sentence and the quote under it. The paragraph below them, "What would have to be decided…", is **not** part of the anchor and stays:

```
`CORE-006` (`docs/02-core-rules.md`) lists, among the actions Action Points can be spent on:

> - Reload (future rule)
```

with:

```
`WPN-017` (`docs/10-weapons.md`) lists, among the weapon types future supplements may introduce:

> - Reloading
```

  `scripts/check_todo_quotes.py` resolves an entry's source as **the last `docs/*.md` path named on a non-quoted line before the blockquote**, then matches the quote as an exact substring. Both halves change together or the check fails, and 4.1 must land first or there is nothing in `docs/10-weapons.md` to match.

  **The path is written `./TODO.md` on purpose — do not "tidy" the prefix away.** `scripts/tasks_format.py`'s `TARGET_PATH_RE` only recognises a path containing a `/`, a deliberate guard against matching the bare `design.md` and `proposal.md` every change mentions in its own prose. Written as `TODO.md` this task resolves to whichever `docs/` file was named above it, and `apply_tasks.py` refuses it. The same applies to `./CODE_OF_DESIGN.md` in task 5.2.


---

## 5. Outside `docs/`

Three files name what this change removes. None is `docs/`, so
`system/repository-strategy.md` (Branch Naming) would put them on their own
branch; shipping a pointer this change knowingly breaks is worse, and the same
call was made in `core-stops-describing-units` for `CODE_OF_DESIGN.md`.

- [x] 5.1 In `scripts/check_todo_quotes.py`, the module docstring, replace this anchor — the parenthesis giving two examples:

```
    (`FLOW-005`'s "Future unit types" promises AP coverage; `WPN-016`'s
    "allowing future expansion" is a closing remark). Telling those apart means
```

with:

```
    (`WPN-016`'s "allowing future expansion" is a closing remark that
    declares nothing). Telling those apart means
```

  `FLOW-005` is retired by task 2.2, and an example naming a rule that no longer exists teaches a reader nothing. `WPN-016` carries the point on its own. **No logic changes** — this is the docstring only.


- [x] 5.2 In `./CODE_OF_DESIGN.md`, Principle 8, replace this anchor — one line:

```
— defined by `docs/02-core-rules.md` (CORE-006), which is the authority on the amount and on what may be spent.
```

with:

```
— defined by `docs/02-core-rules.md` (CORE-006), which is the authority on the amount. What any one action costs is stated by the rule that governs that action.
```

  **Principle 8 owns this subject, and `proposal.md` measured itself against Principles 10 and 12 instead.** The principle named `CORE-006` the authority on "what may be spent" — exactly the half task 1.1 relocates. The amount stays `CORE-006`'s; the cost of an action follows the action.

  **The `./` prefix is required**, for the reason task 4.2 explains.


---

## 6. Verification

Run each command and write down what it actually returned. If a figure differs
from the one stated here, **stop and report it** — do not edit a document to
make it match. Every "before" figure was produced against the pre-change files.

- [x] 6.1 `grep -rn "FLOW-005" docs/ scripts/` — before: **two hits**, its own heading and `scripts/check_todo_quotes.py`'s docstring. After: **no output at all**.

- [x] 6.2 `grep -rn "FLOW-006" docs/` — before: **one hit**, its own heading. After: **no output at all**.

- [x] 6.3 `grep -rn "FLOW-011" docs/` — before: **two hits**, its own heading and the glossary's *AP* entry. After: **no output at all**.

- [x] 6.4 `grep -c "^# FLOW-" docs/03-game-flow.md` — before: **13**, after: **10**. Three rules retired; nothing renumbered.

- [x] 6.5 `grep -rn -F "No unit gains additional AP through its profile" docs/` — before: **two hits**, `02-core-rules.md` and `03-game-flow.md`. After: **one**, in `02-core-rules.md`. **This is the change's central figure**: the sentence was written word for word in two documents. **Zero** means `CORE-006` lost it — stop and report that.

- [x] 6.6 `grep -c -F "3 Action Points" docs/02-core-rules.md` — **1**, before and after. `CORE-006` keeps the allotment.

- [x] 6.7 `grep -rn -F "Stand up" docs/` — before: **one hit**, `CORE-006`'s list item. After: **no output at all**. `DMG-019` describes standing up in its own words after task 3.1 rather than quoting a list.

- [x] 6.8 `python3 scripts/rule.py refs CORE-006` — **eight before and eight after, and the list is what matters, not the count.** Two leave: `FLOW-005`, retired by task 2.2, and `DMG-019`, whose citation lived in the sentence task 3.1 rewrites. Two arrive: `TRN-005` and `TRN-006`, tasks 3.3 and 3.4. `FLOW-004`, `FLOW-012`, `VEH-004`, `CBT-001`, `INF-002` and `INF-009` are unchanged. **If `FLOW-012` is missing, task 2.4 dropped the citation instead of keeping it** — that is the one to check.

- [x] 6.9 `python3 scripts/rule.py refs DMG-019` — before: `CORE-006` and `DMG-005`. After: **`DMG-005` alone.** It loses a citer and does not become uncited.

- [x] 6.10 `python3 scripts/check_todo_quotes.py` — must **exit 0**. This is the gate tasks 4.1 and 4.2 exist to keep green, and running it before them fails.

- [x] 6.11 `python3 scripts/check_id_stability.py` — must **exit 0** and report **194** rule IDs, `3 retired`.

- [x] 6.12 `python3 scripts/lint_ruleset.py` — before: `Checked 15 docs, no structural issues found.` After: the same line.

- [x] 6.13 `python3 scripts/check_task_anchors.py action-points-have-one-owner` — must **exit 0**.

- [x] 6.14 `.venv/bin/pytest` — the whole suite. `scripts/check_todo_quotes.py` is covered by `tests/test_preflight.py`; task 5.2 touches only its docstring and must break nothing.

- [x] 6.15 `python3 scripts/preflight.py` — **all 12 checks PASS.**

- [x] 6.16 `git status --short` — **nine modified files**: `docs/01-foundations.md`, `docs/02-core-rules.md`, `docs/03-game-flow.md`, `docs/09-transport.md`, `docs/10-weapons.md`, `docs/14-glossary.md`, `docs/16-damage-system.md`, `TODO.md`, `CODE_OF_DESIGN.md`, `scripts/check_todo_quotes.py` — plus the untracked change directory. Anything else is a mismatch: report it and stage nothing.

---

## 7. Repairs after applying

Two checks went red after the fifteen pairs landed, and the applier reported
both rather than editing anything to pass. **Both are this change's fault and
neither was in the audit** — they are consequences of task 4.1, which nothing
had reason to look for.

**What went red, and why.** These two paragraphs are the findings, not tasks —
they were first written as checkboxes numbered 7.1 and 7.2, which collided with
the real tasks of those numbers below.

`python3 scripts/check_todo_quotes.py` returned `TODO.md:109 no longer matches
docs/10-weapons.md.` **`TODO.md` has a *second* entry quoting `WPN-017`.**
Section 4 handled the `### Reload` entry and never grepped `TODO.md` for the
rule it was writing into. `### Future weapon types` quotes `WPN-017`'s whole
body verbatim, so inserting `- Reloading` and a closing sentence broke a quote
that has nothing to do with Action Points.

`.venv/bin/pytest` returned 1 failed, 234 passed. `tests/test_build_index.py`
pins `assert len(new) == 197`; retiring three IDs makes it 194, which task 6.11
confirms is correct. **That assertion was scaffolding in a test about body
spans**, written into the AST migration two changes ago, and a rule count in it
means every future retirement breaks a test that has nothing to do with
retirement.

- [x] 7.1 In `./TODO.md`, the `### Future weapon types` entry, replace this anchor — the quote's last three lines. The list above them is **not** part of the anchor and stays:

```
> - Indirect Fire
> - Smoke Launchers
>
> These must continue to follow the StudCraft Weapon Construction Standard.
```

with:

```
> - Indirect Fire
> - Smoke Launchers
```

  **The quote is shortened rather than extended, and that is the right direction.** `scripts/check_todo_quotes.py` matches by exact substring, so a shorter quote that is still a substring of the new `WPN-017` body passes — and this entry is about *how each weapon type generates Impacts*, which is the list. `- Reloading` is not a weapon type and the closing sentence is not a gap; pulling them into this quote to satisfy the checker would have made the entry say something it does not mean.


- [x] 7.2 In `tests/test_build_index.py`, `TestTheMigrationMovesNothingButDEP009`, replace this anchor — one assertion:

```
        assert len(new) == 197
```

with:

```
        # Not a rule count. Retiring an ID is legal — `system/documentation-standards.md`
        # (Naming Conventions) — and a hardcoded total makes every retirement
        # break a test about body spans. What this pins is that both readings
        # see the same rules, which is what makes the cites comparison below
        # mean anything.
        assert set(old) == set(new)
```

  The test's subject is that the AST migration moved `cites` for nobody and grew one body. The count was incidental and is replaced by the thing the comparison actually needs. **`action-points-have-one-owner` is the first change to retire a rule since that test was written**, which is why it surfaced here.


### Verification after section 7

- [x] 7.3 `python3 scripts/check_todo_quotes.py` — must **exit 0**. This is the check 7.1 repairs.

- [x] 7.4 `.venv/bin/pytest` — **235 passed**, the whole suite.

- [x] 7.5 `grep -c -F "Reloading" TODO.md` — **1**. The Reload gap is quoted in the `### Reload` entry; a **0** means that entry is missing. **This task said 0 and contradicted its own next clause** — see 8.7.

- [x] 7.6 `python3 scripts/check_todo_quotes.py` prints how many quotes it matched — **15**: the fifteen it matched before, plus nothing new. If it reports fewer, an entry stopped being found rather than stopped matching. **This task said 16 and contradicted its own explanation** — see 8.8.

- [x] 7.7 `python3 scripts/preflight.py` — **all 12 checks PASS.** This is what tasks 6.10, 6.14 and 6.15 asserted and could not reach; tick those three once this passes.

- [x] 7.8 `git status --short` — **eleven modified files**: the ten `6.16` actually lists plus `tests/test_build_index.py`, and the change directory. **This task said ten, inheriting 6.16's own miscount** — see 8.6, and read the list rather than the word.

---

## 8. The checker cannot tell a quoted blockquote from a written one

Task 7.7 did not pass. `Task anchors are unique` — a required check — reports
task 7.1's anchor as *"replacement text written as a `> ` blockquote"*.

**It is not.** It is a triple-backtick fence whose contents happen to be
`TODO.md`'s own blockquote markup, quoted verbatim because that is what an
anchor is. `check_replacement_format` scans every line of `tasks.md` and counts
runs of three or more beginning with `>`, without tracking whether it is inside
a fence.

The check exists to catch the **pre-2026-08-10 convention**, where replacement
text was written as a bare `> ` blockquote with no fence at all — its own
docstring says so. Those runs are never fenced. Skipping fenced content
therefore keeps every case the check was written for and stops it firing on the
one shape it cannot express: a change that edits a file which itself contains
blockquotes.

`TODO.md` is built entirely out of blockquotes. **Any future change touching it
hits this**, which is why this is repaired rather than worked around.

- [x] 8.1 In `scripts/check_task_anchors.py`, `check_replacement_format`, replace this anchor — the run detector:

```
    # A run of quoted lines long enough to be a replacement body, rather than a
    # single quoted motto such as "> **Every Brick Matters.**" being discussed.
    runs: list[int] = []
    run_start = None
    for number, line in enumerate(lines, start=1):
        if line.startswith(">"):
            run_start = run_start if run_start is not None else number
        elif run_start is not None:
            if number - run_start >= 3:
                runs.append(run_start)
            run_start = None
```

with:

```
    # A run of quoted lines long enough to be a replacement body, rather than a
    # single quoted motto such as "> **Every Brick Matters.**" being discussed.
    #
    # Fenced content is skipped, and that is not a loophole: the convention this
    # catches wrote its replacements as a bare `> ` blockquote with *no* fence,
    # so a run inside one was never the thing being looked for. What lives
    # inside a fence is an anchor or a replacement quoted verbatim, and a change
    # editing a file that itself contains blockquotes — TODO.md is built out of
    # them — would otherwise be reported for quoting its own target correctly.
    runs: list[int] = []
    run_start = None
    in_fence = False
    for number, line in enumerate(lines, start=1):
        if FENCE_RE.match(line):
            in_fence = not in_fence
            run_start = None
            continue
        if in_fence:
            continue
        if line.startswith(">"):
            run_start = run_start if run_start is not None else number
        elif run_start is not None:
            if number - run_start >= 3:
                runs.append(run_start)
            run_start = None
```

  **The `fenced` count above is untouched.** It answers a different question — whether the file uses fences at all — and the "mixes both conventions" finding below it still needs it.


### Verification after section 8

- [x] 8.2 `python3 scripts/check_task_anchors.py action-points-have-one-owner` — must **exit 0**, with the informational line about anchors already gone and no error.

- [x] 8.3 `.venv/bin/pytest tests/test_check_task_anchors.py` — the existing coverage of this function must pass unchanged. **If a test asserted the old behaviour on fenced content, stop and report it** rather than editing the test: that would mean the old behaviour was deliberate and this repair is wrong.

- [x] 8.4 `python3 scripts/preflight.py` — **all 12 checks PASS.** This is what 7.7 asserted and could not reach; tick 6.10, 6.14, 6.15 and 7.7 once it does.

- [x] 8.5 `.venv/bin/pytest` — the whole suite.

- [x] 8.6 `git status --short` — **thirteen modified files**, the eleven observed at 7.8 plus `scripts/check_task_anchors.py` and `tests/test_check_task_anchors.py`, and the change directory.

  **This figure said twelve and was wrong.** It assumed `check_replacement_format` already had test coverage; it had none — that function was untested, which is why the fenced case could regress unnoticed in the first place. Task 8.3 required adding one, so the test file is a consequence of this section rather than something outside it.

  **Tasks 6.16 and 7.8 both state a figure lower than the list they print** — 6.16 says "nine" over ten paths, and 7.8 inherited it. Three wrong counts in one change: read the list, not the word.

### Two figures in section 7 were wrong, and the applier was right not to tick them

- [x] 8.7 Task **7.5** states `grep -c -F "Reloading" TODO.md` should return **0**, while its own explanatory sentence says a 0 means the entry is missing. The correct expectation is **1** — the `### Reload` entry quotes `> - Reloading`. Read 7.5 as expecting 1.

- [x] 8.8 Task **7.6** states `check_todo_quotes.py` should match **16** quotes, while its own explanation says "the fifteen it matched before, plus nothing new". The correct expectation is **15**. Read 7.6 as expecting 15.

  Both are transcription errors in the bolded figure, contradicted by the prose beside them in the same task. `system/delegating-to-agents.md` ("Fix every value in a table, never let it be derived") is the rule they break — and the applier reporting the mismatch instead of ticking is exactly the behaviour that rule exists to produce.

---

## 9. Repairs after the audit of the applied text

Four findings. Two of them convict this change by its own stated line, and one
carries a proof that was sitting inside `tasks.md` the whole time.

**`03-game-flow.md` now has no rule that states the allotment, and its Summary
asserts it in bold, uncited, 170 lines below.** That is the identical shape task
2.1 deleted from `FLOW-004` in the same file. `design.md` Decision 5 exempted the
Summary and the Turn Sequence diagram on the grounds that they "mention the
number while explaining the turn, and foundations already cites `CORE-006`" —
true of foundations, false of both of these. The rule was *mention while citing*;
neither cites. Tasks 9.1 and 9.2.

**`- Reloading` was filed in a list of weapon types, and reloading is not one.**
The proof is task 7.1's own note: *"`- Reloading` is not a weapon type and the
closing sentence is not a gap."* That sentence was written to justify shortening
a `TODO.md` quote around the item — while leaving the item in the list. One rule
now needs two `TODO.md` entries carving one list because the list stopped being
homogeneous. Tasks 9.3 to 9.5 take it out of the list and state it as prose,
which restores the other entry's quote too.

**Task 9.5 is possible only because of section 8.** Its replacement is four
consecutive `> ` lines, which `check_replacement_format` would have reported
before the fenced-content fix landed.

- [x] 9.1 In `docs/03-game-flow.md`, the `# Summary` section, replace this anchor — item 4:

```
4. Each activated unit receives **3 AP**.
```

with:

```
4. Each activated unit receives its **3 AP** (`02-core-rules.md`, CORE-006).
```

  **The Summary asserted what no rule in its own document says any more.** `system/proposal-review.md` ("The Summary Is Part of the Rule") in its exact shape. The number stays — a Summary that made a reader open another document to learn the most basic fact about a turn would be worse — and it now carries the citation that makes it a mention rather than a second definition.


- [x] 9.2 In `docs/03-game-flow.md`, the Turn Sequence diagram, replace this anchor — one line:

```
Each Activated Unit receives 3 AP
```

with:

```
Each Activated Unit receives 3 AP (CORE-006)
```

  Same reason as 9.1, in the diagram. **The bare ID is the form a diagram can carry**; the surrounding block is ASCII flow, not prose, and a full `` `02-core-rules.md`, CORE-006 `` citation would not fit the column.


- [x] 9.3 In `docs/10-weapons.md`, `WPN-017`, replace this anchor — the list's last item and the closing paragraph:

```
- Smoke Launchers
- Reloading

These must continue to follow the StudCraft Weapon Construction Standard. No weapon in the current construction rules runs out of ammunition, so nothing reloads today.
```

with:

```
- Smoke Launchers

These must continue to follow the StudCraft Weapon Construction Standard.

Reloading is future work of its own: no weapon in the current construction rules runs out of ammunition, so nothing reloads today.
```

  **The list is six weapon types again, and the gap is its own sentence.** Two things were wrong with the item. The sentence under the list binds what is in it — "*These* must continue to follow the StudCraft Weapon Construction Standard" — and a construction standard governs how a weapon is built, not whether it reloads. And a non-homogeneous list forced `TODO.md` to quote around one of its items, which task 9.5 undoes.


- [x] 9.4 In `./TODO.md`, the `### Reload` entry, replace this anchor — the quote:

```
> - Reloading
```

with:

```
> Reloading is future work of its own: no weapon in the current construction rules runs out of ammunition, so nothing reloads today.
```

  `scripts/check_todo_quotes.py` matches an exact substring, and a prose sentence is as quotable as a list item. **This entry now quotes a declaration rather than an item**, which is what it was always about — the sentence says what the gap is, where the bullet only named it.


- [x] 9.5 In `./TODO.md`, the `### Future weapon types` entry, replace this anchor — the quote's last two lines. Task 7.1 shortened this quote to work around `- Reloading` sitting in the list; task 9.3 took the item out, so the quote can be whole again:

```
> - Indirect Fire
> - Smoke Launchers
```

with:

```
> - Indirect Fire
> - Smoke Launchers
>
> These must continue to follow the StudCraft Weapon Construction Standard.
```

  **This undoes task 7.1**, and that is the point: 7.1 was a workaround for a category error, not a fix. With the list homogeneous again the entry quotes the whole of what it is about, and the two `TODO.md` entries stop carving one rule between them.


- [x] 9.6 In `docs/14-glossary.md`, the `## AP` entry, replace this anchor — the entry's second line:

```
The universal action economy. See `02-core-rules.md`, CORE-006.
```

with:

```
The resource every unit spends during its activation. See `02-core-rules.md`, CORE-006.
```

  **"The universal action economy" was `FLOW-011`'s title**, which is where the phrase came from and which task 2.3 retires. Pointed at `CORE-006` it defined the term with words that rule never uses; the only surviving "action economy" in `docs/` is in `01-foundations.md`, which defines no rules. The entry now uses `CORE-006`'s own language.


- [x] 9.7 In `docs/16-damage-system.md`, `DMG-019`, replace this anchor — the rule's second sentence:

```
For an infantry model that repair is standing up.
```

with:

```
For an infantry model that repair is standing up — `DMG-005` is where the two poses are defined.
```

  `DMG-005` states that an infantry model is upright while Operational and seated once Wounded, and cites `DMG-019`; nothing pointed back. The old sentence at least aimed somewhere, and after task 3.1 removed that aim the phrase floated. One citation restores it, pointing at the rule that actually defines the poses.


- [x] 9.8 In `docs/09-transport.md`, `TRN-005`, replace this anchor — the citation at the end of the second paragraph's first sentence:

```
acting that same activation (`FLOW-007`).
```

with:

```
acting that same activation (`03-game-flow.md`, FLOW-007).
```

  A cross-document citation carries its filename in this ruleset; the bare form is for a rule in the same document. Pre-existing, and task 3.3 rewrote the rest of this sentence while leaving it — which makes it this change's to fix.


- [x] 9.9 In `docs/01-foundations.md`, the `# Action Points (AP)` section, replace this anchor — the sentence task 3.2 put here, and the line above it:

```
(see `02-core-rules.md`, CORE-006, for the canonical definition)

What any one action costs is stated by the rule that governs that action.
```

with:

```
(see `02-core-rules.md`, CORE-006, for the canonical definition)
```

  **A triplication created by the change that removed a quadruplication.** The sentence now reads verbatim in `CORE-006`, in `CODE_OF_DESIGN.md` Principle 8 and here. The constitution paraphrasing a rule is its job; foundations repeating it two lines under "see `CORE-006` for the canonical definition" is the copy this change exists to remove. The list task 3.2 deleted is gone either way.


### Verification after section 9

- [x] 9.10 `grep -rn -F "3 AP" docs/03-game-flow.md` — **two hits**, the Summary and the diagram, **and both now name CORE-006**. No rule in the document states the number.

- [x] 9.11 `grep -c -F "Reloading" docs/10-weapons.md` — **1**, in the prose sentence, not in the list. `grep -c -F "- Reloading" docs/10-weapons.md` — **0**.

- [x] 9.12 `python3 scripts/check_todo_quotes.py` — must **exit 0** and report **15** quotes matched. Both entries quoting `WPN-017` change in this section; running it between 9.3 and 9.5 fails.

- [x] 9.13 `grep -rn -F "any one action costs is stated by the rule that governs that action" docs/ CODE_OF_DESIGN.md` — **two hits**, `docs/02-core-rules.md` and `CODE_OF_DESIGN.md`. Three means task 9.9 did not land.

  **This task first grepped for the capitalised standalone sentence and expected two, and that could never have matched two.** `CORE-006` embeds the clause mid-sentence in lower case — "…during its activation, **and what** any one action costs is stated by…" — while `CODE_OF_DESIGN.md` writes it as a capitalised sentence of its own. Case-sensitive `-F` on the capital form reaches only the second. The pattern above drops the leading word, which is the part that differed.

  **So it was never "verbatim in three places", as task 9.9's own rationale claimed.** It was verbatim in two — `01-foundations.md` and Principle 8 — and a lower-case variant in `CORE-006`. Task 9.9 is still right for the reason that mattered: foundations repeated Principle 8's sentence two lines under "see `CORE-006` for the canonical definition". The count in the rationale was wrong; the removal was not.

- [x] 9.14 `python3 scripts/lint_ruleset.py` — `Checked 15 docs, no structural issues found.`

- [x] 9.15 `python3 scripts/rule.py refs CORE-006` — **eight**, unchanged from 6.8. Section 9 adds citations in a Summary, a diagram and `TODO.md`, none of which is a rule.

- [x] 9.16 `python3 scripts/rule.py refs DMG-005` — gains `DMG-019`, task 9.7.

- [x] 9.17 `python3 scripts/preflight.py` — **all 12 checks PASS.**

- [x] 9.18 `.venv/bin/pytest` — **237 passed.**

### One more, found by reading the applied text

- [x] 9.19 In `./TODO.md`, the `### Reload` entry, replace this anchor — the line introducing the quote:

```
`WPN-017` (`docs/10-weapons.md`) lists, among the weapon types future supplements may introduce:
```

with:

```
`WPN-017` (`docs/10-weapons.md`), after the weapon types future supplements may introduce, declares:
```

  **Task 9.4 changed the quote and left the sentence introducing it.** Task 9.3 had just taken `- Reloading` out of the list precisely because it is not a weapon type — and this line still says the quote below it is one. `scripts/check_todo_quotes.py` cannot see this: it matches the blockquote against the named document and never reads the lead-in, so the entry passed while saying something false about its own quote.

- [x] 9.20 `python3 scripts/check_todo_quotes.py` — must **exit 0**, `15` quotes matched, unchanged. This task edits a line the checker does not read; if the figure moves, the anchor took the `docs/*.md` path with it.

- [x] 9.21 `python3 scripts/preflight.py` — **all 12 checks PASS.**

### Two `skip` lines from `apply_tasks.py` that are correct

Running `python3 scripts/apply_tasks.py --check` on the finished change reports:

```
skip    task 4.1     ticked, and its pre-change anchor is still in docs/10-weapons.md.
skip    task 7.1     ticked, and its pre-change anchor is still in TODO.md.
```

**Both are right, and the script is right not to guess.** Task 9.3 put
`WPN-017`'s list back to the six weapon types task 4.1 had added a seventh item
to, and task 9.5 restored the `TODO.md` quote task 7.1 had shortened. So each of
those two pre-change anchors exists in its file again — not because the task was
never applied, but because a later task in the same change deliberately undid
it.

That is the shape the script's message describes: *"either a later task restored
the text, or the tick is wrong — a reader decides."* A reader has, and the ticks
stand. Section 4 and section 7 are the record of what was tried; section 9 is
the record of why it was wrong.
