# Design — CORE states only what it owns

## The test each deletion had to pass

A sentence is deleted only when another `docs/*.md` rule already states it. Not "another document could state it", and not "another document mentions the topic" — the surviving text was read and confirmed to carry the same content.

Three candidates failed that test and are **not** deleted. That is the useful output of applying the test rather than a list.

**Two things pass without meeting it, and both are recorded rather than waved through.** Decision 4 accepts one inference — a component removed from the table blocks nothing — in place of an owner. Decision 11 deletes the symmetry clause with no `docs/` rule stating it, on the strength of `CODE_OF_DESIGN.md` Principle 9. Everything else in this change meets the test as written.

---

## Decision 1 — `CORE-006`'s size rule stays; only its argument goes

The brief that prompted this change called `CORE-006`'s size paragraph a "design essay" and listed it for deletion. `grep -rn "scale with\|scales with" docs/` returns exactly one hit for Action Points: `CORE-006` itself. Nothing else in the ruleset says an Action Point cost does not scale with size, and `openspec/specs/action-economy` carries it as a requirement with four scenarios.

So the paragraph is not a redundancy. It is a rule wearing six sentences of argument.

The replacement keeps every clause the requirement asserts — no scaling with the payer's size, no scaling with the operated element's size, the cost set by the rule that governs the action, a measurement may select *which* rule applies — and drops the motorcycle example, the hatch-versus-ramp example, the argument from arithmetic, and the enumeration of `CBT-001`, `VEH-008` and `MOVE-010`. Those three rules state their own costs; `CORE-006` listing them is the restatement pattern this change exists to remove.

**Rejected:** deleting the paragraph and relying on `FLOW-012` ("No Hidden Statistics"). `FLOW-012` is about activation values, not action costs, and says nothing about size.

---

## Decision 2 — `CORE-002` keeps `Shield direction`

Listed for deletion in the brief on the assumption that the Shield or Combat system owns it. `grep -rni "shield direction" docs/` returns two hits: `CORE-002`'s bullet, and `docs/14-glossary.md`'s *Facing* entry, which lists shield direction among what Facing determines and cites `CORE-002` for it.

No combat, melee or component rule owns shield direction. Deleting the bullet would remove the only statement of it and leave the glossary citing a rule that no longer says it — the "dangling cross-reference" failure class in `system/proposal-review.md`.

---

## Decision 3 — `CORE-005` is a tracked gap, not a redundancy

The brief listed `CORE-005`'s future-work sentence for removal. `TODO.md` quotes that sentence verbatim, and `scripts/check_todo_quotes.py` — run by `scripts/preflight.py` — compares the two character for character. `docs/06-deployment.md` restates the same gap and cites `CORE-005` for it.

Removing the sentence would break a required check and delete the ruleset's only declaration of the structure-damage gap. `TODO.md` exists precisely so that a declared gap is recorded rather than forgotten; a gap the ruleset declares in its own text is content with an owner, which is the opposite of a restatement.

**Rejected:** rewriting `CORE-005` and updating `TODO.md`'s quote to match. The `TODO.md` entry would then quote a rule that declares no gap, which defeats the entry.

---

## Decision 4 — the three rules go, and the pose moves to `DMG-005`

The three rules go. One sentence of their content moves; the rest is already stated as a rule elsewhere:

| `CORE-011`/`012`/`013` says | Where it is after this change |
|---|---|
| The minifigure stands upright / is seated; the pose is the marker, no token | **Moved** into `DMG-005` by task 11.1 |
| The unit functions normally | `DMG-005`, `Operational` |
| Movement reduced, unarmed attack degraded | `MOVE-021`, `CBT-015`, both cited by `CORE-012` rather than defined by it |
| Removed from the battlefield; removal is the marker | `DMG-006` ("Destroy a minifig → remove the minifig"), `MEL-011` |
| No longer blocks movement, Line of Sight or Cover | *Accepted inference, not an owner* — `DMG-005` says "No dead component remains on the battlefield", and what is not on the table is not seen |

The last row is the one place this change accepts a derivation instead of naming an owner, and it is labelled so a later reader does not go hunting for the rule.

**The pose is moved rather than deleted, and the first draft of this change got that wrong.** It claimed `MEL-011` owned the seated pose. `MEL-011` lists "Wounded minifigure sits" as an *example*, under a rule scoped to combat results, and `01-foundations.md` lists it in a section that defines no rules. `grep -rn "stands upright" docs/` returns exactly one hit — `CORE-011` itself — and `DMG-005` says only that an Operational component "functions normally". Two example bullets are not the same content as "The seated position is the game marker. No additional token is required.", so the stated test was failing on this row.

`DMG-005` is where it goes: the pose is how one component type shows the Component State that rule defines. This also keeps `CORE-006`'s surviving "Stand up" action legible, which would otherwise refer to a posture the ruleset no longer mentions.

**Rejected: a single pose-only rule kept in `02-core-rules.md`.** This is the strongest alternative and the one worth answering, because a pose-only rule describes no state machine and so does not carry the duplication that condemns the current `CORE-011`/`012`/`013`.

It is refused on ownership. The pose is meaningless without the states it displays, and those are `DMG-005`'s: a reader who finds "a Wounded minifigure is seated" in CORE has to go to `16-damage-system.md` to learn what Wounded is, and a reader who finds `DMG-005` has to know CORE exists to learn what a Wounded minifigure looks like. One of the two documents has to hold both halves, and it is the one that defines the states. `CORE-016` already gives CORE the general principle — represent state on the model — which is the part that is genuinely universal; how one component type does it is not.

**Rejected: keeping the pose in `02-core-rules.md` as a shortened `CORE-011`/`012`,** two rules rather than one. That leaves the state machine described in two documents, which is the duplication this change exists to remove.

**`MEL-011` is left alone, deliberately.** It lists "Wounded minifigure sits" among its examples of representing combat results on the model, and after this change that is what it is — an example of `CORE-016`'s principle, in the document about melee, not a competing statement of the pose. The new `DMG-005` sentence deliberately does not cite it: `CORE-016` is cited two paragraphs above for the no-marker principle, and pointing at a second place for the same principle inside one rule is the near-duplicate `system/proposal-review.md` warns about.

**Rejected:** keeping the three IDs as stubs reading "Reserved for rule-ID stability", the form `MEL-010` takes. A rule that says only that it is gone is a rule a reader has to read before discovering there is nothing there, in the document this change exists to shorten. The gap is legible on its own — `CORE-010` is followed by `CORE-014` — and `docs/` records the current ruleset, not its history.

**The three numbers are retired, not reissued.** `CORE-014`, `CORE-015` and `CORE-016` keep their numbers, and no future rule takes `CORE-011`, `CORE-012` or `CORE-013`. The brief offered renumbering as an option; it is refused, because renumbering breaks every citation aimed at the rules that moved.

**Prerequisite:** deleting a rule ID outright is not permitted by the repository as it stands — `scripts/check_id_stability.py` reports an ID present in the base revision and absent now as an error, and `system/documentation-standards.md` (Naming Conventions) states identifiers are permanent. The `rule-ids-may-be-retired` change relaxes exactly that one case and must merge first. It is a separate branch because a proposal branch may touch `docs/*.md` and its own change directory only (`system/repository-strategy.md`, Branch Naming).

---

## Decision 5 — `CORE-001` keeps the height derivation, compressed

Three documents cite `CORE-001` specifically for *where the height comes from* — `01-foundations.md`, `04-construction-standard.md` (SCS-001) and the glossary's *UB* entry — and `VEH-028` states that `CORE-001` is the only place a Unit Base becomes a count of plate layers.

Deleting the derivation would dangle all four. It is compressed from two paragraphs to one instead: the minifigure, the four bricks and the plate, the uncounted head stud, and the underside of the base as the measuring point. What goes is the material restated from elsewhere — infantry occupying one Unit Base standing or seated and whatever it carries (`TRN-002`, `CMP-018`), and the Unit Base as minimum operational space (`TRN-001`).

---

## Decision 6 — the projections table stays; the Line of Sight sentence goes

The table is cited by `CMP-018` (openings), `DEP-001` (deployment floors), `WPN-004` (Platform Length) and `VEH-028`. It stays whole.

The sentence below it — Line of Sight and Cover resolved against the plastic, never against a silhouette — is stated by `GEO-004` at length, by `CORE-008` and by `CORE-010`, all in the same ruleset. `CORE-001` keeps the half that is its own ("a projection supplies a measured value and nothing else, and never replaces a physical check") and points at `GEO-003` and `GEO-004` for the rest.

The glossary's *Projection* entry asserts the same clause and cited only `CORE-001`. It gains a `GEO-004` pointer in the same pass, per `system/proposal-review.md` ("The Summary Is Part of the Rule" — a glossary entry is a restatement and drifts the same way).

---

## Decision 7 — no capability delta

`unit-base`, `action-economy` and `component-damage` are live capabilities whose requirements touch text this change moves or deletes. None gets a delta, because a requirement describes what the rules do, not which document says it:

| Requirement | Still held by |
|---|---|
| `unit-base` — "the volume that must fit SHALL be the Unit Base" | `SCS-005`, unchanged |
| `unit-base` — "a projection SHALL NOT replace a physical check" | `GEO-004`, `CORE-008`, `CORE-010`, and `CORE-001`'s surviving clause |
| `action-economy` — "Action Point cost SHALL NOT scale with size" | `CORE-006`, kept by Decision 1 |
| `component-damage` — the three-state progression | `DMG-005`, whose three states task 11.1 does not alter |

Task 11.1 adds a sentence to `DMG-005` and still owes no delta. The sentence is `CORE-011`'s and `CORE-012`'s, moved: the states, their order and what each costs are untouched. A relocation inside `docs/` is invisible to a requirement that describes behaviour.

`grep -rn "seat\|upright" openspec/specs/` returns one line — `unit-base/spec.md:15`, "it occupies exactly one Unit Base, whether standing or seated". That is occupancy, owned by `TRN-002`, and it says nothing about how a state is displayed; `component-damage`, which owns the state machine, carries no pose requirement to contradict.

Writing a delta here would record a behaviour change that did not happen. `system/proposal-review.md` ("Delta vs. Direct Edit") is the standing instruction: no delta invented for a capability whose behaviour is unchanged.

---

## Decision 8 — `Universal Rule` states authority, not plastic-wins

The current wording — a conflict "between written rules and physical construction", resolved by a four-level list — reads as though physical construction sits somewhere in that ranking and can override a written rule. The four levels are all written rules: Foundations, Core Rules, Construction Standards, Scenario Rules.

The replacement says the order governs rules against rules, and states the physical model's actual role separately: it supplies the physical facts, and the rules decide what those facts mean. That clause also preserves the one sentence worth keeping from the deleted `Design Notes` ("The physical model is always the primary source of truth").

The direction is not invented here. `03-game-flow.md` (FLOW-013) already reads: "Scenario rules sit fourth in the rule priority order (`02-core-rules.md`, Universal Rule): they may restrict or extend the ruleset for one game, and never contradict Foundations, Core Rules or Construction Standards." Higher-in-the-list already won; the section simply did not say so. `scripts/rule.py` cannot surface that corroboration, because the Universal Rule carries no rule ID of its own.

---

## Decision 9 — the document keeps its linter exemption

`02-core-rules.md` has no `Design Philosophy` and no `Summary`, recorded in `scripts/lint_ruleset.py` as `SECTION_DEBT`. This change does not add them. It also means there is no Summary to fall out of date, so the usual "check the Summary in the same pass" step has nothing to check in `02-core-rules.md` — the glossary entries are the only restatements it has to keep true, and Decision 6 covers the one that moves. `16-damage-system.md` does have a Summary, and task 11.1 leaves it alone for the reason `tasks.md` states: it already names Structural States and gains no new definition.

---

## Decision 10 — `CORE-009` keeps the disclaiming form

Making the four levels explicitly ordered has a consequence for `CORE-009`. The first draft replaced "It does not grant a shot outside of a unit's own activation" with "A unit shoots only during its own activation", which is a different claim: a prohibition rather than a disclaimer about this rule's own reach.

Two rules already contemplate the prohibited case. `CBT-010` says two attacks resolve together only when "something else already declares them so (e.g. a future scenario rule for mutual engagement)", and `FLOW-013` lets a scenario extend the ruleset. A Core Rule reading "a unit shoots only during its own activation" would outrank both under the precedence Decision 8 makes explicit — closing a path `CBT-014` lists as a future extension, which is Principle 15 and the "absolute claims" failure class in `system/proposal-review.md`.

The applied text therefore reads "This does not by itself grant a shot outside a unit's own activation".

---

## Decision 11 — the symmetry sentence is dropped, and `CODE_OF_DESIGN.md` owns it

"This is symmetric: if it can see you, you can be its target during its own activation" is deleted with no `docs/` rule stating it, which makes it the one deletion the test in this document does not pass as written.

It is dropped anyway, deliberately. `CODE_OF_DESIGN.md` Principle 9 states it — "Visibility is symmetric: what can see you can target you" — and it is derivable in the ruleset: `CBT-002` routes every attacker's targeting through `CORE-008`'s physical-visibility check, which is symmetric because seeing is. A principle both stated in the principles document and implied by two rules does not need a third statement in the rule a reader reaches first.

**Recorded because it will recur:** a future reader finding `CORE-009` bare may want the clause back. The reason it is not there is this decision, not an oversight.
