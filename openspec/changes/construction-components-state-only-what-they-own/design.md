# Design — Construction Components state only what they own

## Context

This is the third document cut to one owner per rule, after `02-core-rules.md` (#103) and `04-construction-standard.md` (#104). The two earlier changes are what make this one possible and what constrain it: #104 left `SCS-006` – `SCS-009` owning the door, ramp and window construction requirements, and #104's own review moved a shield sentence *into* `CMP-014` and pointed the glossary at it.

The source brief for this change is a review of `docs/05-construction-components.md` written outside the repository. It is followed where it agrees with `system/documentation-standards.md` and departed from where it does not — Decision 2 records the one systematic departure.

---

## Decision 1 — The test applied to every rule

A `CMP` rule survives if, after every gameplay consequence is removed, it still states a **physical construction requirement no other document states**.

Three outcomes follow from that test, and they are not a matter of degree:

- **Trim** — something survives. Nine rules: `CMP-001`, `CMP-003` – `CMP-006`, `CMP-008`, `CMP-014`, `CMP-016`, `CMP-018`.
- **Retire** — nothing survives. Eight rules: `CMP-007`, `CMP-009` – `CMP-013`, `CMP-015`, `CMP-017`.
- **Move, then retire** — one clause survives but belongs to another document. One rule: `CMP-002`.

Nine plus eight plus one is the eighteen rules the document has, so no rule is unclassified. `proposal.md` counts the last two together as nine retirements, because a retirement is what both are in `docs/`.

Rejected: a fourth outcome where a rule is kept as a one-line pointer at its owner. #104 retired `SCS-019` and `SCS-020` for being exactly that, and reintroducing the pattern here would undo the argument it made.

---

## Decision 2 — Retirement where the brief asked for a short rule

The brief marks `CMP-002`, `CMP-007`, `CMP-009`, `CMP-010`, `CMP-011` and `CMP-015` as "keep, but simplify". Applying Decision 1 to each of them yields nothing to keep:

| Rule | What the brief would keep | Who already states it |
|---|---|---|
| `CMP-002` | visible pilot position, crew minifigure, operating position | `VEH-013` (all three) — except *minifigure*, see Decision 3 |
| `CMP-007` | a functional weapon must be physically represented | `WPN-001`, `WPN-015`, `CORE-014`, `SCS-016` |
| `CMP-009` | a functional door must physically open and close | `SCS-007`, and the opening clause is `CMP-018` |
| `CMP-010` | a functional ramp must physically move | `SCS-008`, and the opening clause is `CMP-018` |
| `CMP-011` | transparent LEGO elements represent windows | `SCS-009`, which `CMP-011` cited for it |
| `CMP-015` | accessories are decorative unless a rule says otherwise | `CMP-001` as rewritten here, `GEO-002` |

Keeping a shortened restatement is the specific failure `system/documentation-standards.md` names: "a shortened restatement silently drops what it left out". The brief's own architecture diagram argues for the same outcome — it puts *general construction legality* in the Construction Standard, which is where `SCS-006` – `SCS-009` already are.

The divergence is recorded in `proposal.md` (Out of Scope) rather than left implicit, because a reader comparing the brief to the result will otherwise read six retirements as overreach.

---

## Decision 3 — `CMP-002`'s minifigure sentence moves to `VEH-013`

`VEH-013` requires "a crew member (`VEH-015`) occupying a visible operating position". Nothing in `08-vehicles.md`, `09-transport.md` or `02-core-rules.md` says that crew member is a **minifigure** — `VEH-015` says vehicles "may carry one or more crew members" and `TRN-014` says crew occupy their own Unit Bases. `CORE-003` makes infantry minifigures, and a crew member is not stated to be infantry.

So one clause of `CMP-002` has no other owner and is moved rather than deleted, in the same shape as #104's four moves. It lands in `VEH-013` because `VEH-013` is the rule that requires a Pilot at all.

The "decorative empty seat" half moves with it. On its own it is a consequence of the first half, but it is the sentence that makes the requirement checkable at the table, and deleting it would leave `VEH-013` requiring a Pilot without saying what one looks like.

Rejected: moving it to `VEH-015` (Crew), which would state it for every crew member rather than for the one the rules read. `VEH-015` is about crew fitting, not about what crew are.

---

## Decision 4 — `CMP-014` keeps the orientation paragraph

The brief asks for interposition and protection behaviour to leave `CMP-014` for Combat/Damage. Applied literally that would delete the paragraph #104's second review deliberately moved here from the retired `SCS-022`, and orphan the glossary's ***Facing*** entry, which now ends "Which way a shield protects is settled by where it physically stands rather than by Facing — see `05-construction-components.md`, CMP-014."

Rejected for two reasons:

1. **It would be the third home for one sentence in two pull requests.** `SCS-022` → `CMP-014` → `DMG-007` is churn, not ownership.
2. **The sentence states a physical fact about the model**, not a step of damage resolution: where the shield stands relative to the attacker. `DMG-007` owns what a component in the way *does* — the impact cannot reach what it protects — and `CMP-014` cites it for that. The two are not the same claim.

What does leave `CMP-014` is the restatement: "may be targeted or may interpose … exactly like any other component (`DMG-007`, `DMG-012`)" and "its own Resistance (`DMG-003`) determines what it takes to get through it". Both are `16-damage-system.md` stated twice. The clause "not for any separate defensive bonus" stays, so no reader concludes a shield grants one.

---

## Decision 5 — What `CMP-018` must keep, derived from its citers

`CMP-018` has more inbound citations than the rest of the document combined, so its trim is bounded by them rather than by taste. Each surviving element is there because something reads it:

| Kept | Read by |
|---|---|
| The opening must pass the model's Unit Base, measured with the component open | `TRN-007`, `MOVE-018`, `MOVE-019`, glossary *Access Opening* |
| Measured against the front edge the model leads with | nothing cites it; nothing else states it either — see below |
| The *clear* opening, not the nominal frame | `GEO-004`, `VEH-030` ("decoration obstructs passage, so it counts there") |
| Opening rather than approach | `MOVE-019` (a ramp leading to an opening), `VEH-027` |
| Functional for one model, decorative for another | glossary *Access Opening*, `TRN-007` |
| Checked when the model is built | nothing cites it; it is what stops the check being re-run in play |

What goes is arithmetic the rule was redoing rather than consuming: infantry's 1 Unit Base and 4 studs (`TRN-002`, `CORE-003`), the Unit Base's 13 plate layers and the `W × 4` conversion (`CORE-001`). `CORE-001` is still cited — for the Unit Base, which is what it defines.

**One clause of the deleted Width paragraph is not arithmetic and is kept:** the opening is measured against the front edge the model leads with. `CORE-001` gives the Unit Base a `4 × 3` footprint and `CORE-002` names the 4-stud edge the front of an infantry base, but neither says which face a model presents to an opening, and `MOVE-003` explicitly allows a model to travel sideways — "the corresponding side edge moving left or right". Without the clause, a 3-stud opening can be argued to pass infantry edgeways, and the rule's own claim that width "is not a judgment call" stops being true. Keeping it costs one subordinate clause and is what keeps the check a measurement (Principle 1).

Two whole paragraphs go for restating other documents. The ramp paragraph works an example out of `VEH-022` – `VEH-024` and `MOVE-019`; the declared-role paragraph states `TRN-007`'s access points and `TRN-011`'s firing-port exemption, and `TRN-011` states that exemption itself, citing `CMP-018` for the requirement it is exempt from. The direction of that citation is what makes the paragraph redundant rather than load-bearing.

The windows sentence — "Windows (`CMP-011`) are exempt unless declared as access points" — goes with `CMP-011`. Nothing declares a window an access point, and a window that is not one is not an access opening, so the exemption was answering a question the first sentence already answers.

---

## Decision 6 — `CMP-001` absorbs `CMP-015`'s qualifier

`CMP-001` currently ends "Decorative elements have no gameplay effect", flatly. Two rules contradict that as written: `WPN-002` (a decorative-looking round piece is a functional muzzle if it meets the requirement) and `GEO-002` (a decorative-looking plate inside the structural cross-section is Gameplay Geometry). `CMP-015` carried the qualifier — "unless another rule specifically defines them" — for accessories only.

Merging the qualifier into `CMP-001` and retiring `CMP-015` fixes the absolute claim and removes the duplicate in one edit. This is `system/proposal-review.md`'s "absolute claims falsified by a later fix" and "the same rule asserted twice", in the same rule.

Rejected: keeping `CMP-015` as the place where the qualifier lives. `CMP-001` comes fourteen rules earlier and would go on stating the unqualified version, which is the version a reader hits first.

`CMP-001`'s defining sentence is otherwise left word for word. Rewriting "affects gameplay" into "provides a gameplay capability" was considered — the source brief phrases it that way — and rejected: it narrows the term every other rule leans on, and `docs/14-glossary.md`'s ***Functional Component*** entry restates the old wording, so the edit would have to propagate there for a gain nothing needs.

---

## Decision 7 — The `# Purpose` line is edited, `# Design Philosophy` and `# Summary` are not

`system/proposal-review.md` ("The Summary Is Part of the Rule") requires checking both in the same pass. Checked, with three different outcomes:

- **`# Purpose`**, third line: "A component only has a game effect if it complies with the construction rules defined in this document." False after this change — a door complies with `SCS-007`, a weapon with `WPN-001`. Replaced with the split the change enforces.
- **`# Design Philosophy`**: unchanged. "Players should be able to identify the purpose of every important component simply by looking at the model" is the aspiration `CMP-017` tried to state as a rule. It is true, unenforceable, and correctly placed in a philosophy section — which is also the argument for retiring `CMP-017` rather than rewriting it into something objective.
- **`# Summary`**: unchanged. Its four lines describe components providing gameplay through physical construction and the model changing what a unit can do — which is `CMP-001` and `CMP-016`, both kept.

---

## Decision 8 — No spec delta

`grep -rn "CMP-"` and `grep -rn "construction-components"` over `openspec/specs/` return nothing: this document predates the OpenSpec workflow and was never formalised. `system/proposal-review.md` ("Delta vs. Direct Edit") is explicit that inventing a delta against a capability that does not exist is the wrong move, so the work is tracked as ordinary doc-edit tasks.

No capability changes in any case. Nine rules stop being stated in this document and go on being stated by their owners.

---

## Decision 9 — Nine rules are deleted outright, not stubbed

`system/documentation-standards.md` (Naming Conventions): a deleted rule's number is retired, never reissued, and no stub is left — the diff records that the rule was there. `MEL-010` is the one stub in the ruleset and exists because its rule *merged* into another, which is not what happens here.

`CMP-002`'s move to `VEH-013` is the closest case and still is not a merge: one clause changes documents, and the rule as a whole stops existing.

---

## Decision 10 — `docs/14-glossary.md`'s ***Functional Component*** entry

The entry restates `CMP-001` and cites it. Because `CMP-001` gains the "unless another rule gives them one" qualifier, the entry gains it too — otherwise the glossary states the absolute claim Decision 6 just removed from the rule, which is exactly how a restatement drifts.

The other two glossary entries citing this document were checked and need no edit: ***Facing*** points at `CMP-014` for shield orientation, which stays; ***Access Opening*** paraphrases `CMP-018`'s first sentence, which survives in the same words.

---

## Decision 11 — The door requirement is settled in `SCS-007`'s favour

`CMP-009` requires a functional door to "physically open **and** close". `SCS-007`, after #104 trimmed it, requires one to "must open physically" and "may close physically". Those are different requirements and both have been in `docs/` the whole time: a door that opens but jams shut is illegal under one and legal under the other.

Retiring `CMP-009` resolves the contradiction toward the looser rule, and that is a decision rather than a transcription — so it is recorded here and in `proposal.md` rather than left inside a retirement bullet.

**This decision was first argued on a ground Decision 13 then removed.** It read: `SCS-007` survives because `04-construction-standard.md` owns construction legality. Section 19 moves door construction *out* of that document, so ownership decides nothing here and the argument has to stand on the merits — which it does, and which is why the outcome is unchanged:

- **Nothing in the ruleset reads whether a door can close.** `MOVE-018` reads whether it is open, `CORE-007` and `TRN-008` charge the same Action Point for either operation, `TRN-015` reads whether an access point is usable. A requirement no rule consumes is a legality check with no consequence.
- **The model already charges for it.** A transport whose door cannot close fails `TRN-009`'s physical test for a closed transport, so its passengers are visible, targetable, able to be shot at, and without the hull protection `TRN-010` gives them. That is a real cost, paid in survivability rather than in a construction ruling — Principle 1.

The alternative, carrying `and close` into `CMP-020`, would tighten a requirement nothing reads and would make a jammed door an illegal model rather than a worse one.

Rejected: keeping `CMP-009` alive purely to preserve the stricter modality. That would keep a rule whose every other clause is owned elsewhere in order to carry one word, which is the pattern this change removes.

---

## Decision 12 — What the audit of the applied text changed

Five repairs, in `tasks.md` section 18. Three are defects in this change's own new text, and the pattern `system/proposal-review.md` predicts held exactly: the transcription was faithful and the proposal was wrong.

**`CMP-018`'s first paragraph decided nothing for a vehicle.** "Must pass the Unit Base of each model that uses it" fits infantry, which occupies one; a vehicle occupies `W × D` Unit Bases (`VEH-001`) and stands several tall (`VEH-028`). The deleted Width and Height paragraphs were the only place the check was said to scale with the model, and `MOVE-018`, `TRN-007` and `VEH-030` all read this rule for vehicles. Fixed by requiring the opening to pass the Unit Bases the model occupies, as wide as its front edge and as tall as it stands — the scaling restored in a clause, with the arithmetic still `CORE-001`'s.

**"the front edge that model leads with" was the wrong repair to Decision 5's problem.** It reads either as forbidding a model to enter an opening other than front-first — a constraint contradicting `MOVE-001` and `MOVE-003` — or as "whichever edge it happens to lead with", which reopens the sideways loophole the clause exists to close. The pre-change rule stated the edge unconditionally ("at least as wide as the front edge of whatever passes through it"), and that is what is restored. The lesson is narrow and worth keeping: a clause added to close a loophole has to be checked against the rule that opened it, not only against the rule it is written into.

**`CMP-016` and `CMP-018` became adjacent and disagreed.** "Gameplay always reflects the current physical model" now sits immediately above "Openings are checked when the model is built" — `CMP-017` used to separate them. Both sentences predate this change; deleting the rule between them is what made the collision visible. `CMP-018`'s last line now says the check reads the plastic as it stands, at the bench and again whenever the model changes, which decides nothing `CMP-016` did not already decide.

**`assets/IMAGES.md` cited the retired `CMP-002` twice.** The proposal's "Checked elsewhere" greps covered `system/`, `README.md`, `CODE_OF_DESIGN.md`, `CONTRIBUTING.md`, `AGENTS.md` and `TODO.md`, and `assets/` was not among them — a gap in the check, not in the retirement. `scripts/lint_ruleset.py` reads `assets/IMAGES.md` but validates only the rule named beside a filename, so the declined-candidates list is checked by nothing. Both bullets are retargeted to `VEH-013`.

**`MOVE-011` and `VEH-021` were cited side by side undifferentiated.** `VEH-021` exists partly to warn that `MOVE-011` is the infantry rule and permits stairs, which no vehicle may climb. Each citation is now labelled with the kind of model it governs.

---

## Decision 13 — The boundary between the two construction documents

Retiring `CMP-009` – `CMP-011` raised the question the duplication was hiding: `04-construction-standard.md` and `05-construction-components.md` were both answering "what must be physically built", and nothing said which one owned what. Three rules had been written twice in the same order — `SCS-007`/`CMP-009`, `SCS-008`/`CMP-010`, `SCS-009`/`CMP-011` — which is what an unstated boundary produces. Removing the copies without stating the line leaves the next contributor to guess the same way.

The criterion, decided by the maintainer:

> **`04-construction-standard.md` is the battlefield and the base every model stands on. `05-construction-components.md` is every functional part of a model.**

**Why Components is the survivor, not the Standard.** The rest of the ruleset already treats a door as a component: `DMG-001` lists `Door` and `Window` among the components an Impact is assigned to, `DMG-006` removes a destroyed one, and `CMP-016` says removing a functional component changes what the model can do — which is a door being blown off, exactly. No rule anywhere reads a door *as a construction standard*. The boundary also survives the case that broke it before: a building is a model (`CORE-005`), so a door on a wall and a door on a hull fall on the same side.

**`SCS-002` stays where it is.** Under a literal reading of the criterion an infantry base is part of a model. It stays because it is the standard base every model is built on rather than a part providing a capability, and because `CORE-001` and `MOVE-002` both cite it there — moving it would pull the Unit Base's own definition into the churn for no gain. The `# Purpose` line names it explicitly rather than leaving it as an exception a reader has to infer.

**New IDs, appended.** `system/documentation-standards.md` forbids renumbering and reuse, so a rule that changes document retires its old number and takes a new one — and a new one may only append above its document's highest, or `scripts/check_id_stability.py` reports a reuse. That is why the four interactive-element rules land as `CMP-019` – `CMP-022` after `CMP-018` rather than beside the components they resemble, and why `WPN-022` is the last weapon rule. Reading order loses a little; ID stability is worth more, and it is the invariant citations depend on.

**Rejected: merging the two documents.** It removes the boundary permanently, which is tempting — the mirror is evidence the boundary was not learnable. The cost is that every remaining `SCS` rule needs a new ID, `13-materials.md`'s precedent means the retired document number is never reused, and `README.md`'s reading order is positional so everything after it renumbers. That is a large change to avoid writing one sentence in a `# Purpose`. If the criterion turns out not to hold, merging stays available.

**Rejected: leaving `SCS-016` and `SCS-017` in the Standard.** They are weapon-construction rules, so the criterion sends them to `10-weapons.md` — and leaving them would make the new `# Purpose` line false on the day it was written.

**Both are absorbed by `WPN-001`, and neither becomes a new rule.** `WPN-001` already lists a weapon body, at least one functional muzzle and a physical mounting point as what every ranged weapon must include. `SCS-016` adds one word to that — `visible`. `SCS-017` adds the definition of the body the bullet already names, and its "every muzzle must connect to a weapon body" is unreachable anyway: `WPN-019` puts the Weapon Front on the body and sizes it from the body's own width, and `WPN-020` requires every muzzle to fit inside that footprint.

`SCS-017` was going to become `WPN-022` until the audit of these sections pointed out that this is the same ground `SCS-016` was absorbed on, applied inconsistently one task later — a new rule stating what `WPN-001`, `WPN-019`, `WPN-020` and `WPN-003` already state, inside a change whose entire subject is that pattern. Absorbing both is Principle 11 and Principle 12 answering together.

**One requirement would have fallen out, and does not.** `SCS-016` governed "every weapon"; `WPN-001`'s bullets govern ranged weapons, and its next sentence hands melee weapons a striking end instead of a muzzle. Task 20.3 therefore carries the same visibility onto that sentence. `MEL-013` states none of its own and `CORE-014` states presence rather than visibility, so without it a melee striking end would quietly lose a requirement it had.

---

## Decision 14 — A move is not a licence to import what the change removed

The audit of sections 19–20 caught the failure this whole change exists to prevent, committed by the change itself: `SCS-006` transcribed "word for word" would have landed `CMP-019` twelve lines below `CMP-001` carrying **the unqualified** "Decoration alone has no gameplay effect" — the exact sentence task 2.1 qualified, for the exact reason it qualified it — plus a six-item example list of the kind task 2.1 deleted from `CMP-001` and task 12.1 deleted with `CMP-015`.

So a moved rule is trimmed on arrival like any other. `CMP-019` keeps its requirement and drops both; the glossary's ***Interactive Element*** entry already lists the same six elements for a reader who wants them. `CMP-020` and `CMP-021` gain the `CMP-018` pointer their retired counterparts carried, which task 10.1 removed only because the owner was about to be in another document.

**Three more things the move falsified, all outside the two documents:**

- **`04-construction-standard.md`'s `# Construction Principles`** governs "every functional game element", and after sections 19 and 20 that document holds no rule about one. Its `Visible — Players can immediately identify it` is word for word the adjudication this change retires `CMP-017` for; deleting one for being subjective while the other survives in a second document is the inconsistency the change is meant to remove. Deleted. The aspiration lives in `05-construction-components.md`'s `# Design Philosophy`, and `CORE-008` and `CORE-014` own the two halves that can actually be checked.
- **`CORE-005` — "Structures follow the Construction Standard"** is the ruleset's only sentence routing structure construction, and after the move half of what a structure is built from is elsewhere. It now names both documents. This pulls in `TODO.md`, which quotes the paragraph verbatim and is compared character for character by `scripts/check_todo_quotes.py` — the quote moves with the rule, as it did in #104.
- **`scripts/lint_ruleset.py`'s cross-reference comment** used `VEH-027`'s sentence as its worked example, naming `SCS-011` and `SCS-008`. Task 19.3 rewrites that sentence and task 19.1 retires `SCS-008`. The comment now describes the shape instead of quoting a rule, so it cannot go stale the same way again. This is the third directory a retired ID was found in after the greps had been declared complete — `assets/` in section 18, `scripts/` here — and task 20.8 now covers both.

---

## Decision 15 — What the audit of the moved text changed

Six repairs, in `tasks.md` sections 22 and 22b. **None is in a moved rule**; all six are prose that went on describing rules its document no longer holds — the same defect this change exists to remove, committed against the document it emptied.

- **`WPN-001`'s absorbed body definition read "the structure carrying the muzzle"**, two lines above the sentence giving melee weapons a striking end *instead of* a muzzle. `MEL-014` reads melee reach from Weapon Length and `WPN-003` measures Weapon Length on the body, so the ruleset's only definition of a weapon body was one no sword could satisfy. It now names both, as `WPN-002` and `MEL-013` already do.
- **`CMP-021` required the opening unconditionally** where `MOVE-019` requires it "where the ramp leads to an opening" — and `VEH-027` cites `CMP-021` for a ramp a vehicle climbs to reach a height, which leads to no opening at all. The unconditional form came in from the retired `CMP-010`, which predates `MOVE-019`'s hedge. Moving a rule imports its age.
- **The boundary's own sentence was wrong twice.** "The base every model stands on" is false — `SCS-002` is infantry-only and nothing requires a vehicle to be built on a base — and the criterion returned *two* answers for a building, which is battlefield and model at once. That is precisely the case that produced the `SCS`/`CMP` mirror, so the `# Purpose` line now points at `CORE-005`, which already splits a structure between the two documents.
- **`04-construction-standard.md` kept two more orphans**: `# Design Philosophy`'s "Every functional element should be physically represented", which is the deleted `# Construction Principles`' `Physical` condition in one sentence, and a `# Summary` whose first four lines summarise the ruleset's construction ethos rather than the five rules above them. Both were on the "untouched, deliberately" list — kept as structural boxes the linter checks rather than re-read as prose, which is the exact miss `system/proposal-review.md` ("The Summary Is Part of the Rule") records.
- **The repaired `# Purpose` line then failed the linter.** `CROSS_REF_RE` binds a parenthesised rule ID to a filename in backticks up to 80 characters earlier, and the sentence put `` `10-weapons.md` `` between `` `02-core-rules.md` `` and `(CORE-005)`, so the linter read it as claiming `10-weapons.md` states `CORE-005`. The linter is right and the sentence was wrong: reordered so nothing sits in that window. Prose in `docs/` is parsed, not just read.

---

## What was checked and found clean

- Every one of the eighteen `CMP` IDs, through `scripts/rule.py refs` and a repository-wide `grep`. No retired ID is cited from outside `docs/`; `TODO.md`, `system/`, `README.md`, `CODE_OF_DESIGN.md`, `CONTRIBUTING.md` and `AGENTS.md` contain no `CMP` reference at all.
- `TODO.md` quotes no text from `docs/05-construction-components.md`, so `scripts/check_todo_quotes.py` cannot be broken by this change — unlike #104, where two entries had to move with it.
- The eleven documents that own the removed text, read in full rather than grepped. Each removal names an owner in `proposal.md`, and each named owner states the rule in its current text.
- `VEH-023` and `VEH-024` cite `CMP-006` and `CMP-005` for the very sentences this change keeps ("as built", "visually distinguishable"). Both citations still resolve, and neither rule is edited.
