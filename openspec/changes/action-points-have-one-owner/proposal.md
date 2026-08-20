# Action Points have one owner

## Why

`system/documentation-standards.md` states the doctrine in four words: **a pointer instead of a copy, always.** The Action Point economy is the place `docs/` breaks it hardest.

Six rules across two documents talk about Action Points, and between them they say the same things four separate times:

| Duplication | Where |
|---|---|
| **"3 Action Points per activation"** | `CORE-006`, `FLOW-004`, `FLOW-005` |
| **"No unit gains additional AP through its profile"** — *word for word* | `CORE-006`, `FLOW-005` |
| **"Differences emerge from construction, not hidden statistics"** | `FLOW-005`, `FLOW-012` |
| **A list of the actions AP is spent on** | `CORE-006` (9 items), `FLOW-006` (11), `FLOW-011` (8), `01-foundations.md` (7) |

**The four lists disagree with each other.** `CORE-006` has *Stand up* and *Reload*; `FLOW-006` has *Rotate* and *Operate scenario objectives*; `FLOW-011` has none of those four; the foundations list has *Rotate* but not *Operate mechanisms*. Four snapshots of one set, each incomplete in a different way, and nothing keeps them in step — a new action added to the ruleset lands in none of them, or in one.

**Two entries in those lists are not actions at all.** `CORE-006`'s *Stand up* is `DMG-019`'s repair, which reads back into the list to name itself; and *Reload (future rule)* is a declared gap that `TODO.md` quotes verbatim — the ruleset saying what it has not built, filed among things it has.

`FLOW-004` is the clearest single instance: it prints **3 Action Points (AP)** in bold and then, on the next line, *"(see `02-core-rules.md`, CORE-006, for the canonical definition)"*. It names where the truth lives while copying it.

The narrow purpose:

> **`CORE-006` owns what an Action Point is and how many a unit has. What any one action costs is owned by the rule that governs that action. Nothing else states either.**

`CODE_OF_DESIGN.md` Principle 10 is one responsibility per document, and Principle 12 is consistency.

## What Changes

Three documents. **Three rules are retired; nothing is renumbered.**

- **`CORE-006`** — keeps everything eight rules and two glossary entries cite it for: AP exists, every unit receives exactly 3 per activation, no unit gains more through its profile. **Loses its nine-item example list**, and gains one clause in its place — what an action costs is stated by the rule that governs that action, which is `FLOW-006`'s one true sentence.
- **`FLOW-004`** — keeps the activation *procedure*, which is Flow's own and stated nowhere else: a unit receives its AP, spends them in any legal order, the activation ends when they are spent or the player stops, and a unit activates once per Turn. **Stops printing the number** and cites `CORE-006` for it instead of alongside it.
- **`FLOW-005`** — **retired.** Every claim in it is `CORE-006`'s or `FLOW-012`'s. Its unit-type list (*Infantry, Vehicles, Walkers, Hovercraft, Future unit types*) is what `CORE-006`'s "regardless of its type or construction" already covers, without needing to be kept current.
- **`FLOW-006`** — **retired.** Its list is the third copy; its one real sentence moves into `CORE-006`.
- **`FLOW-011`** — **retired.** "Action Points are the universal resource" is `CORE-006`. "Players must decide how to spend their limited AP" is an observation, not a rule.
- **`FLOW-012`** — keeps "no hidden activation values" and that construction determines capability, which is its own subject. **Loses its three-step activation list**, which restates `FLOW-004`.
- **`docs/14-glossary.md`, the *AP* entry** — cites `FLOW-011`, which stops existing. Re-aimed at `CORE-006` alone. **The *Activation* entry** prints the number beside a citation of `FLOW-004`, which after this change no longer holds it, and is re-aimed too.
- **`DMG-019`** — says the repair is "the same action `02-core-rules.md` CORE-006 lists as *Stand up*", reading back into a list that stops existing. It describes standing up in its own words instead. **Nothing mechanical would have caught this**: the ID survives, so `lint_ruleset.py` stays green while the claim about what that ID *lists* goes false.
- **`docs/01-foundations.md`** — carries the fourth action list, and the same bold-number-plus-citation pattern this proposal calls the clearest instance of the defect. The list goes; the number and its citation stay, because foundations defines no rules and may cite.
- **`WPN-017` and `TODO.md`** — *Reload* stops being an action in `CORE-006` and becomes what it is: a weapons gap, declared in the weapons document. `TODO.md`'s entry is re-sourced to it, which `scripts/check_todo_quotes.py` requires in the same commit.
- **`TRN-005` and `TRN-006`** — one cites `FLOW-004` directly against the number, the other restates the number citing nothing. Both cite `CORE-006` for it.
- **`CODE_OF_DESIGN.md`, Principle 8** — names `CORE-006` the authority "on the amount **and on what may be spent**". This change relocates the second half, so the principle says so.
- **`scripts/check_todo_quotes.py`** — its docstring uses `FLOW-005` as an example of a passage that declares no gap. The example goes with the rule.

## What Does Not Change

- **No gameplay value.** Three Action Points per activation, spent in any legal order, one activation per unit per Turn, no AP from a profile. Every action still costs what its own rule says it costs.
- **No rule ID is renumbered or reused.** `FLOW-005`, `FLOW-006` and `FLOW-011` are retired and their numbers are never reissued — `system/documentation-standards.md` (Naming Conventions). `FLOW-007` is not moved down into the gap.
- **`CORE-006`'s eight citers.** `FLOW-004`, `FLOW-005` (retired), `FLOW-012`, `VEH-004`, `CBT-001`, `DMG-019`, `INF-002`, `INF-009` all read it for the allotment or the no-profile rule, and both survive intact.
- **`openspec/specs/action-economy`.** Its one requirement — every unit receives exactly 3 AP, none gained through a profile — is exactly what `CORE-006` keeps. No requirement and no scenario stops being true, so this change carries **no delta** (`system/proposal-review.md`, Delta vs. Direct Edit).
- **`03-game-flow.md`'s Summary and its Turn Sequence diagram**, which both state the number as part of describing the turn. **`MOVE-007` and `INF-009`**, which derive a consequence from it — "a unit with 3 AP can make at most three movement legs" — rather than restating the allotment. The line this change holds is that the number is **defined once and may be mentioned elsewhere**; what it removes is a rule restating another rule's definition. `design.md`, Decision 5, and it is a narrower line than the first draft of this proposal claimed.
- **`CHANGELOG.md` and every version header.** Release-cut-only.

## Checked elsewhere

- `python3 scripts/rule.py refs FLOW-005 FLOW-006 FLOW-011` — **all three are cited by nothing.** Retiring them strands no rule.
- `grep -rln FLOW-005 FLOW-006 FLOW-011` across the **whole repository**, `scripts/` included — four live files: `03-game-flow.md`, where they live; `14-glossary.md`'s *AP* entry; and `scripts/check_todo_quotes.py`'s docstring, which uses `FLOW-005` as an example. All three are handled. The archived changes under `openspec/changes/archive/` name them too and are history, correctly left alone. **The first draft of this proposal grepped `docs/`, `system/`, `assets/` and the root documents and claimed completeness; it had not read `scripts/`.**
- `python3 scripts/rule.py refs DMG-019` — cited by `CORE-006` and `DMG-005`. `CORE-006`'s citation is inside the list this change deletes, so `DMG-019` loses one citer and keeps the other. **It does not become uncited.**
- `assets/IMAGES.md` names none of the three.

## Out of Scope

- **The other twenty-one rules `rule.py orphans` lists.** A sweep of all fifteen documents found twenty-four rules that cite nothing and are cited by nothing. Most are legitimately standalone — `CBT-014` and `WPN-017` are lists of what StudCraft does *not* have, and `MOVE-017`, `TRN-015`, `MEL-006` and `GEO-006` each decide something nothing needs to point back at. Separating those from genuine disconnection is a reader's job and its own change.
- **Rules whose examples outweigh their statement.** Thirty-one rules carry more list lines than statement lines; `VEH-017` illustrates "vehicles are collections of components" with seven bullets. Real, and a different campaign.
- **`FLOW-007 — Combining Actions`**, which sits between two retirements and carries nineteen list lines of its own. It states something the others do not — that actions may be combined freely — and trimming it is not this change's subject.
