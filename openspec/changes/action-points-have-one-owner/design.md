# Design — Action Points have one owner

## The test applied throughout

For each of the six rules: **what does this say that nothing else says?** A rule with no answer is retired; a rule with one is trimmed to it.

| Rule | What only it says | Outcome |
|---|---|---|
| `CORE-006` | AP exists; every unit gets exactly 3; none through a profile | The owner |
| `FLOW-004` | The activation procedure: receive, spend in any order, ends when spent or the player stops, once per Turn | Kept, trimmed |
| `FLOW-005` | — | Retired |
| `FLOW-006` | An action's cost is stated by the rule that governs it | Sentence moved, rule retired |
| `FLOW-011` | — | Retired |
| `FLOW-012` | No hidden activation values; construction determines capability | Kept, trimmed |

---

## Decision 1 — The four action lists all go, and none is kept as canonical

**There are four, not three.** `01-foundations.md` carries a fifth statement of
the allotment and a seven-item list, and the first draft of this design never
opened that file. The audit found it. Its list goes with the others; its number
and citation stay, because foundations defines no rules and is allowed to
mention what `CORE-006` defines — Decision 5.

The obvious alternative was to keep one list and delete the other two. Rejected, and the reason is already recorded in this repository.

`core-stops-describing-units` deleted `CORE-002`'s six-item **Facing determines** list on exactly this ground: *"A list of what a rule is consumed for is a snapshot a command can print"* (`system/documentation-standards.md`, How a Rule Is Written). An action list is the same shape — it enumerates what other rules do, so it goes stale the moment one of them is added or renamed, and nothing checks it.

**The evidence that it already went stale is the four lists themselves.** They were presumably in step once. `CORE-006` has *Stand up* and *Reload*; `FLOW-006` has *Rotate* and *Operate scenario objectives*; `FLOW-011` has neither; foundations has *Rotate* but not *Operate mechanisms*. Keeping one would preserve whichever drift that one happens to carry.

**Every item was traced to an owning rule before deleting the lists.** Move (`INF-002`, `VEH-004`), Rotate (`INF-005`, `VEH-009`, `VEH-010`), Fire and Attack (`CBT-001`), doors and ramps (`CORE-007`, `TRN-008`), Embark (`TRN-005`), Disembark (`TRN-006`), Stand up (`DMG-019`), Operate mechanisms (`CORE-007`, `CMP-019`). Two own nothing: *Interact with terrain*, which states nothing normative and goes; and *Reload*, which is not an action at all — Decision 8.

What replaces them is not a shorter list but a rule about ownership: an action's cost is stated where that action is defined. That is checkable by reading the rule you care about, which a list never was.

## Decision 2 — `FLOW-004` keeps the procedure and loses the number

`FLOW-004` prints **3 Action Points (AP)** and then cites `CORE-006` "for the canonical definition". Both cannot be right: either it is canonical here or it is canonical there.

It is there — eight rules and two glossary entries cite `CORE-006` for the allotment, and none cites `FLOW-004` for it. So `FLOW-004` states that a unit receives its Action Points, cites `CORE-006`, and stops.

**What it keeps is the half nothing else states**: the AP may be spent in any legal order, the activation ends when they are gone or the player stops, and a unit activates once per Turn. That is the activation procedure and it is Flow's subject. `TRN-005` cites `FLOW-004`, and for that.

Rejected: retiring `FLOW-004` too and moving the procedure into `CORE-006`. `CORE-006` is the anchor eight rules read for one number; growing it into the turn structure is the opposite of what this change is for.

## Decision 3 — Three retirements in one change

Each of `FLOW-005`, `FLOW-006` and `FLOW-011` is cited by no *rule*. Two live references exist outside the rule graph: `14-glossary.md`'s *AP* entry, and `scripts/check_todo_quotes.py`'s docstring, which uses `FLOW-005` as an example of a passage that declares no gap. Both are re-aimed here. **The first draft said "cited by nothing, in `docs/` and outside it" without having read `scripts/`** — the claim was right about rules and wrong as stated.

Splitting them into three proposals was considered and rejected. They are one subject and they overlap each other, not just `CORE-006` — `FLOW-006` and `FLOW-011` both carry an action list, and `FLOW-005` and `FLOW-012` both carry the construction-not-statistics claim. Retiring one at a time would leave each audit reading a half-deduplicated document and would make the second and third proposals argue from a state nobody intended.

**What retirement costs, stated plainly:** three numbers leave the ruleset permanently. `system/documentation-standards.md` (Naming Conventions) — never renumbered, never reused, and `FLOW-007` is not moved down into the gap. `docs/` already carries a document-number gap at `13-*` for the same reason.

## Decision 4 — No `openspec/specs/` delta

`openspec/specs/action-economy` holds one requirement: every unit SHALL receive exactly 3 AP regardless of type or construction, and no unit SHALL gain additional AP through its profile. Two scenarios back it.

**`CORE-006` keeps both claims verbatim.** No requirement and no scenario stops being true; what changes is how many documents restate them. `system/proposal-review.md` (Delta vs. Direct Edit) is explicit that a change of this shape is tracked as ordinary doc-edit tasks, and that inventing a delta for it is itself a defect.

## Decision 5 — The number is defined once and may be mentioned

The first draft drew this line as *"rules do not restate rules; prose may cite"* and used `MOVE-007` as its example of prose. **`MOVE-007` is a rule.** The argument cited a counterexample as support, and the audit caught it.

The line that survives:

> **The allotment is defined in one place — `CORE-006` — and any other passage that needs the number mentions it while citing that definition.**

That is narrower than "prose may cite" and wider than "nothing else says three". It separates the two things cleanly:

- **`FLOW-004`** printed the number in bold *and* said `CORE-006` was canonical. Two definitions, one document apart. Fixed.
- **`TRN-006`** restated "the same 3 AP allotment" citing nothing. Fixed.
- **`TRN-005`** cited `FLOW-004` directly against the number — a citation aimed at a rule that, after this change, does not hold it. Re-aimed.
- **`MOVE-007`** writes "a unit with 3 AP can make at most three movement legs". That derives a consequence; the number is the input to its own rule, not a second definition. **Left.**
- **`INF-009`** the same. **Left.**
- **`01-foundations.md`**, the Summary and the Turn Sequence diagram all mention the number while explaining the turn, and foundations already cites `CORE-006`. **Left.**

Counted honestly, the number survives in ten places after this change and that is not a defect. What was a defect was three rules holding a definition each.

## Decision 6 — `FLOW-005`'s unit-type list is not preserved anywhere

It reads *Infantry, Vehicles, Walkers, Hovercraft, Future unit types* — five entries, one of which is "future ones".

`CORE-006` says "regardless of its type or construction", which covers every entry including the fifth without having to be edited when a sixth appears. The list is a maintenance liability standing in for a phrase that already exists. It goes with the rule.

## Decision 7 — "Every meaningful action consumes AP" is dropped, not preserved

`FLOW-011`'s middle sentence is the one claim in the three retirements that lands nowhere else, and it is not kept.

**As an absolute it was already false.** `INF-006` crosses an obstacle of three plate layers or less with "no additional movement cost"; `INF-009` takes a connected slope "at no additional Action Point cost"; `INF-004` requires no rotation to move backward. Actions that cost nothing exist, and a rule saying every action consumes AP contradicts three that say otherwise.

`CORE-006`'s "Action Points represent everything a unit can do during its activation" is the true version and stays. That is a statement about scope, not about every action having a price.

## Decision 8 — Reload is a declared gap, and gaps belong with their subject

`- Reload (future rule)` sat in `CORE-006`'s list among things a unit may spend AP on. **It is not one.** No weapon in the construction rules has ammunition, so nothing reloads; the entry was the ruleset admitting a hole, filed among things it had built.

`TODO.md` quotes it verbatim, and `scripts/check_todo_quotes.py` matches by exact substring — so deleting the list without moving the declaration turns a required check red. That is the mechanical reason this had to be handled. The design reason is better: **a gap should be declared in the document that would fill it.** `WPN-017 — Future Weapon Types` is a list of what weapons may one day do, in the document that would define them, and it gains *Reloading* plus the sentence explaining why nothing reloads today.

Rejected: deleting the `TODO.md` entry. The gap is real and `TODO.md`'s contract is to record gaps the ruleset declares about itself — removing the declaration to simplify a list would lose a question someone still has to answer.

## What this change does not claim

It does not make `03-game-flow.md` a tidy document. `FLOW-007 — Combining Actions` sits between two of the retirements with nineteen list lines of its own, and `FLOW-001` and `FLOW-006`'s neighbours carry the same habit. That is real and it is a different change — `proposal.md`, Out of Scope. This one is about a single subject stated in six places, and stops there.
