# Design — Infantry is a first-class domain

## Decision 1 — The document is `docs/17-infantry.md`

Infantry belongs beside Movement and Vehicles, and `08-` would say so. It is not available, and neither is any gap.

`system/documentation-standards.md` (Naming Conventions): "A removed document's number is never reused either." `README.md` says the same of `04-` and `13-`, naming `docs/04-construction-standard.md` and `docs/13-materials.md` as the removed documents whose numbers those gaps preserve. Renumbering the existing sequence is forbidden by the same convention and would rewrite the rule-ID prefixes of six documents to buy a tidier table of contents.

`17-` is the next unused number. It puts Infantry after Damage, which reads oddly in a directory listing and is the price of a convention that has already been paid twice.

**Rejected: `13-infantry.md`.** The revision this change grew out of called the `13-` gap "a plausible home without renumbering" and made it the preferred implementation. The gap is not free space; it is a retired number, and reissuing it is the exact case the convention forbids.

**Rejected: renumbering to `08-infantry.md`.** Forbidden, and it would move `VEH-`, `TRN-`, `WPN-`, `CBT-` and `MEL-` document numbers for presentation.

**The ordering problem is solved in `README.md`, not in the filename.** Its Rulebook reading order lists Infantry immediately after Movement and before Vehicles, and says outright that the file numbers are creation order rather than reading order. A reader meets the three in the order that makes sense; only `ls` shows Infantry last.

## Decision 2 — Retiring ten `MOVE-` IDs, not renaming them

`MOVE-004` does not become `INF-002`. It is deleted, its number is retired, and `INF-002` is a new rule whose text happens to be `MOVE-004`'s.

The distinction is not pedantry. `scripts/check_id_stability.py` reports an ID that changed document as `moved` — "a renumbering wearing the same number" — so carrying `MOVE-004` into `docs/17-infantry.md` under its old number is the one thing the checker exists to catch. And each document owns its own prefix namespace: a document called Infantry containing a list of `MOVE-` rules would leave `07-movement.md` unable to add a rule without checking another file for collisions.

The ten: `MOVE-002`, `MOVE-004`, `MOVE-005`, `MOVE-006`, `MOVE-008`, `MOVE-009`, `MOVE-010`, `MOVE-011`, `MOVE-016`, `MOVE-021`. No stub replaces any of them — the diff records that they were there (`system/documentation-standards.md`, Naming Conventions).

`MOVE-003` is **not** renumbered into the `MOVE-002` gap, and no surviving rule moves. The document ends with a gapped sequence, which is what the convention produces.

## Decision 3 — `MOVE-012`, `MOVE-013` and `MOVE-014` are split, not moved

Each of the three states two things: what a construction is, and what infantry does when it meets one.

| Rule | Generic half — stays in `07-movement.md` | Infantry half — moves |
|---|---|---|
| `MOVE-012` Slopes | a slope is built from LEGO slope elements and is a valid climbing surface | infantry crosses connected slopes at no extra AP, distance counting against the limit → `INF-009` |
| `MOVE-013` Stairs | a stepped surface is a movement path whatever it is built from | no step taller than a freely-crossed obstacle, no extra AP, distance counts → `INF-009` |
| `MOVE-014` Vertical Access | any stable LEGO surface may support a unit; physical construction determines accessibility | with no slope, stair or ramp the wall cannot be climbed, and no other construction grants access → `INF-010` |

`VEH-027` reads `MOVE-012` for what a slope is built from and `MOVE-013` for what a stair is — exactly the halves that stay. That is why these three keep their numbers: the generic half is load-bearing for a second domain and deleting the ID would strand it.

**The step-height qualification goes with the infantry half deliberately.** `MOVE-013` today defines a stair partly by reference to `MOVE-009`, an infantry threshold. Leaving that in the generic rule would leave Movement depending on Infantry, which is the defect this change exists to remove. What a stair *is* is its construction; how tall a step a given unit can take is that unit's rule.

## Decision 4 — Movement points at both domains, never at one

Four surviving rules cited a rule that is about to retire. Each is re-aimed to name **both** unit domains, or neither:

- `MOVE-012` → infantry `INF-009`, vehicles `VEH-027`. `MOVE-013` → infantry `INF-009`, vehicles `VEH-027` (never). `MOVE-014` → infantry `INF-008` and `INF-010`, vehicles `VEH-021` and `VEH-027`. Each closes by naming whose question the ascent is, and names both sides.
- `MOVE-001`, `MOVE-003`, `MOVE-007` — the same treatment, for the same reason (Decision 13).
- `MOVE-015` — "at the risk described in `MOVE-016`" becomes the risk each domain's own rule describes, naming `INF-011` and `VEH-026`.
- `MOVE-019` — loses "and is a legal access point (`MOVE-011`, `MOVE-014`)". A ramp being usable terrain is generic; being one of three access points is `INF-008`'s list, and `INF-008` names ramps.

A generic rule naming both implementations is a signpost between siblings, not a dependency on one. A generic rule naming only infantry is the defect.

**Rejected: leaving Movement with no forward pointers at all.** `07-movement.md` currently ends its `# Vehicle Movement` section with "Vehicles and infantry differ most at stairs: infantry climb them (`MOVE-013`), vehicles never do (`VEH-027`)". That sentence earns its place — it is the single most-confused point in the two documents — and the change keeps it, aimed at `INF-009`.

## Decision 5 — Falling stays two rules, not one shared rule

`INF-011` and `VEH-026` are not the same mechanic wearing two names:

| | Infantry (`INF-011`) | Vehicle (`VEH-026`) |
|---|---|---|
| Free height | the first brick, fixed | the vehicle's own Terrain Threshold, read from the model |
| Dice | one D6 per complete brick beyond the free height | one D6 per complete brick past the threshold |
| Resolution | each die a Damage Roll (`DMG-015`) | each die a Damage Roll (`DMG-015`) |

The only common part is the last row, and `16-damage-system.md` already owns it — both rules already cite `DMG-015` by name. `VEH-026`'s "resolved exactly as infantry falling is (`07-movement.md`, MOVE-016)" adds a second citation for something `DMG-015` states in the same sentence, and it is the citation this change deletes.

**Rejected: a generic `Fall Damage Resolution` rule in Movement or Damage.** It would restate `DMG-015` under a new number so that two rules could cite it instead of citing `DMG-015`. `CODE_OF_DESIGN.md` Principle 11 and `system/documentation-standards.md` ("What `system/` Is For") both say not to: one owner per rule, a pointer instead of a copy. Vehicle falling stops depending on infantry falling because it stops citing it, not because a third rule is invented.

## Decision 6 — `VEH-008` states its own cost

`VEH-008` reads "each costing **1 Action Point** (matching MOVE-008's infantry rotation cost)". The parenthetical is deleted and nothing replaces it.

The cost is already stated in the sentence. `CORE-006` already states the governing principle — "An action's cost is set by the rule that governs that action" — so a vehicle turn costing 1 AP needs no corroboration from an infantry rule. What the parenthetical bought was reassurance that the two costs agree, which is a fact about the ruleset rather than a rule.

`VEH-007` gets the same treatment for the same reason: "StudCraft does not use diagonal movement" is `MOVE-007`, stated universally. `VEH-007` keeps its own sentence — vehicles combine forward movement with turns, where infantry combines forward with lateral — and points at `MOVE-007` for the ban itself. `MOVE-001`'s trailing "Diagonal movement is never allowed" is the third statement of the same ban in the same document and is dropped.

## Decision 7 — What mentions infantry is not thereby an infantry rule

The test applied to every candidate: **who owns the relationship?**

| Rule | Mentions infantry | Owner | Why |
|---|---|---|---|
| `MOVE-004` | infantry moves 12 studs | **Infantry** | the distance is a property of the unit |
| `TRN-002` | infantry occupies 1 UB in a transport | Transport | the capacity relationship is Transport's |
| `DMG-005` | infantry model's pose shows its state | Damage | the state machine is Damage's |
| `MOVE-021` | Wounded infantry moves two steps | **Infantry** | what the unit can still do |
| `CBT-015` | a Wounded attacker's dice | Combat | attack resolution is Combat's |
| `CMP-018` | an opening that passes infantry | Components | the opening is a component |

Nothing moves out of `09-transport.md`, `16-damage-system.md`, `11-combat.md` or `05-construction-components.md`. Three of them have one citation re-aimed and nothing else.

**`CORE-003` keeps infantry identity and gains a signpost.** It states that infantry are minifigures occupying one Unit Base, which is universal and belongs where the other unit types are classified. `INF-001` cites it rather than restating it — a change arguing for one owner per domain does not get to create a second owner for the thing it is about. What `CORE-003` lacked is the pointer `CORE-004` already has at `08-vehicles.md`; task 3.3 adds it, so the rule that names infantry names the infantry document.

## Decision 8 — No glossary entry is added

`system/documentation-standards.md` ("Adding a New Ruleset Document") asks for "the new terms a reader cannot infer". `docs/17-infantry.md` introduces none: *infantry*, *step*, *obstacle* and *access point* all already appear in `07-movement.md` today and none of them is in `docs/14-glossary.md` now.

The glossary's *Wounded* entry **is** edited, because it cites `MOVE-021` and that ID retires. That is a re-aim, not a new entry.

## Decision 9 — Every number is transposed, not restated

`system/proposal-review.md` ("Verify the Number, Not Just the Direction") and ("Multipliers Set Early Get Falsified by Numbers Added Later"). This change adds no number and computes none. The full set, before and after:

| Quantity | Value | From | To |
|---|---|---|---|
| Forward distance | up to 12 studs, multiples of 3 | `MOVE-004` | `INF-002` |
| Side distance | up to 12 studs, multiples of 4 | `MOVE-005` | `INF-003` |
| Backward distance | up to 12 studs, multiples of 3 | `MOVE-006` | `INF-004` |
| Movement action | 1 AP | `MOVE-004`/`005`/`006` | `INF-002`/`003`/`004` |
| Rotation | 1 AP | `MOVE-008` | `INF-005` |
| Freely crossed obstacle | up to 3 plate layers | `MOVE-009` | `INF-006` |
| Climbable obstacle | 4 to 6 plate layers, +1 AP | `MOVE-010` | `INF-007` |
| Obstacle needing access | 7 or more plate layers | `MOVE-011` | `INF-008` |
| Free fall height | 1 brick / 3 plate layers | `MOVE-016` | `INF-011` |
| Fall dice | 1 D6 per complete brick beyond the first | `MOVE-016` | `INF-011` |
| Wounded limit | 2 steps — 6 studs forward or backward, 8 sideways | `MOVE-021` | `INF-012` |
| Off-axis worked example | forward 6 studs (1 AP), then left 4 studs (1 AP) | `MOVE-007` | `INF-003` |

`tasks.md` carries each as verbatim replacement text, so no value is retyped from this table.

## Decision 10 — No `openspec/specs/` delta

`system/proposal-review.md` ("Delta vs. Direct Edit"): a `MODIFIED` delta can only target a capability that already exists. No capability under `openspec/specs/` describes which document states a movement rule, and no requirement or scenario stops being true — a Wounded infantry model still moves two steps, an obstacle of 4 plate layers still costs the extra Action Point, and a fall of one brick still rolls nothing.

This change also introduces no new capability. Infantry movement is not new behaviour; it is existing behaviour with an owner.

## Decision 11 — Adding a new ruleset document is currently impossible, and one prerequisite fixes it

`docs/17-infantry.md` is created without a version header, and three mechanisms then contradict each other. This is the finding that changed this change's shape, so it is written out in full.

1. `.claude/hooks/guard_repo_edits.py:154` denies any edit writing that header from a branch that is not `release/v*`. `system/documentation-standards.md` (Versioning) is why: nobody writes it by hand, because several proposal branches are in flight and each would pick a colliding number.
2. `scripts/release_cut.py:186` rewrites the header where `DOC_VERSION_RE` matches and skips the file where it does not (`if count:`). A document created without one never acquires one.
3. `scripts/lint_ruleset.py:248` **requires** one on any document that defines rules, and `:255` requires every document's to agree. `docs/17-infantry.md` defines twelve, so the linter reports `missing or malformed` and exits 1 — and it is the `Docs ruleset linter`, the required check.

So the ruleset cannot gain a new rule-bearing document at all. Nothing on this branch resolves it: writing the header is denied, and `scripts/` is out of a proposal branch's scope.

**This change closes it in the two places that can.** It was drafted as a separate prerequisite and folded in when the delivery was consolidated (Decision 12); the code is the same either way:

- `release_cut.py` inserts the header into a `docs/*.md` that has rule IDs and lacks one, below the document's title, at the version it is already computing for that cut. That is the only code in the repository allowed to write the line. **It must insert exactly one line and change nothing else** — not the blank line that would make the file match its siblings. `.github/workflows/docs-require-proposal.yml` constrains the `release/v*` exemption by content: every added or removed line in the `docs/*.md` diff that is not `^[+-]\*\*Version:\*\*` fails the check, and a bare `+` for a blank line is one of them. Getting this wrong breaks the first release cut after the prerequisite merges, not the prerequisite's own pull request.
- `lint_ruleset.py` gains a closed list of documents awaiting their first cut, in the shape it already uses for `SECTION_DEBT`, and does not fail those for the missing header. `docs/17-infantry.md` goes on it. **The list is self-clearing: a listed document that already carries a header is an error.** So the cut that supplies the header turns the exemption into a failure, and the entry has to be deleted by the next ordinary change — which is the only kind of branch allowed to edit `scripts/` anyway. Without that inversion the entry outlives its reason, and the one document most likely to lose its header again is the one the linter has stopped watching.

Both halves are needed. Without the first, the document never gets a header; without the second, this change never merges.

**Rejected: writing the header anyway, at `0.2.0 Draft` to match its siblings.** The hook refuses it, `scripts/apply_tasks.py` refuses it a second time, and the workflow forbids it. Three independent refusals is the repository saying this is not the route.

**Rejected: shipping `docs/17-infantry.md` with no rule IDs** — as prose that `07-movement.md` links to — so the linter does not ask for a header. That is not a ruleset document, and the whole point is that infantry rules should be numbered rules in a document of their own.

## Decision 12 — One change, not four

`system/repository-strategy.md` (Branch Naming) confines a `<change-name>` branch to `docs/*.md` plus that one change, so this was designed as four pull requests: two prerequisites, the ruleset, and a follow-up. **The maintainer decided it ships as one**, and the split is not worth defending, because of what it was for.

It was never about scope. It was a workaround for one fact: `scripts/lint_ruleset.py` is the only checker that runs in a workflow, and it fails on every intermediate state this change passes through. A document with no version header. An image entry naming a retired rule. An image entry naming a document that does not exist yet. The four-way split was the sequence that kept each pull request green — at the cost of three merges during which the repository was, in small documented ways, wrong.

One pull request has no intermediate state, so the workaround has nothing left to work around. Three things got simpler rather than merely fewer:

- **`assets/IMAGES.md` makes no round trip.** The plan was to delete two entries, land the ruleset, then restore them under the new document with new filenames. They now move once. `MOVE-003`'s entry moves with them, which the split would have left behind: the image shows a base measured from its leading face, and after this change that is `INF-002`'s claim and not `MOVE-003`'s. An entry follows the claim it illustrates, not the number it was filed under.
- **`TODO.md` is never stale.** Its two quotes were going to be wrong for the length of one merge, with `preflight.py` red and a note in `tasks.md` telling the applier to ignore it. Nobody has to be told to ignore a check now.
- **`VERSION_DEBT` never names a file that does not exist.** The prerequisite would have listed `17-infantry.md` one merge before the document arrived.

**What the split would still have bought, and what it costs to give up:** one reviewable concern per pull request. This one is large — sixteen paths, a ruleset document, two scripts and their tests. A reviewer cannot check the `scripts/` change without scrolling past two hundred lines of ruleset. That is the real trade, and it is the maintainer's to make.

**On the Branch Naming table.** It is a convention, not a gate: `branch-naming.yml` checks only that the branch is kebab-case and names the single change directory it touches, and `guard_repo_edits.py` denies non-`docs/` edits only on `main`, `develop`, `release/*` and `archive/*`. An earlier draft of this decision claimed both would refuse the edit; they would not, and that claim was wrong. The rule is still the rule, and departing from it is a decision recorded here rather than an accident.

## Decision 13 — Three surviving rules are generalised, not just left alone

An earlier draft moved the ten obvious rules and declared the rest generic. Reading what was left showed three that are not:

| Rule | What it says now | Why that is infantry-only |
|---|---|---|
| `MOVE-001` | "Every unit has four possible movement directions: Forward / Backward / Left / Right" | A vehicle has two and turns between them — `VEH-005`, `VEH-006`, `VEH-008` – `VEH-011`. No vehicle moves left. |
| `MOVE-003` | measured "from the edge of the **base** that leads in that direction", enumerating four | The base is `CORE-001`'s Unit Base, which only infantry stands on, and a vehicle has no side face to lead with. |
| `MOVE-007` | "Players combine forward and lateral movement instead", with a 6-studs-then-4-studs example | Lateral movement is the thing `VEH-007` says vehicles do **not** have, and 3 and 4 are the infantry base's two axes. |

Each replacement states the mechanic and defers the enumeration, rather than swapping one unit's list for a longer one. `MOVE-003` measures from whichever face leads and lets each domain say which faces it has; `MOVE-007` says a unit combines "the moves and turns its own domain gives it", because a vehicle's second component is a turn (`VEH-008` – `VEH-011`) and not a second axis. Citing `VEH-004` alone for vehicle measurement would have been wrong the same way: that rule's "Measure from the vehicle's front, along its facing" is its *forward* instruction, so `VEH-006` is cited beside it for reverse.

`MOVE-007` is the sharpest: task 6.1 makes it the rule every vehicle is sent to for the no-diagonal ban, so leaving an infantry-only remedy inside it would recreate, in the generic document, exactly the defect this change removes from `VEH-021`. Each of the three now names both domains or neither, and `MOVE-007`'s worked example is transposed into `INF-003` unchanged.

**A fourth was found the same way and is also fixed:** `VEH-005` states "Diagonal movement does not exist", which with `MOVE-001`, `MOVE-007` and `VEH-007` made four statements of one ban. `VEH-007` keeps the vehicle-side sentence and the pointer; the other two restatements go.

**Rejected: leaving all four, on the grounds that they are true today.** They are true today because infantry is the only unit type whose movement is written here. The change's own test — "does this rule describe the mechanics of movement, or what a particular unit can do?" — fails all four, and a test applied only to the rules that are easy to move is not a test.

## Decision 14 — `INF-008` and `INF-010` stay two rules

They overlap. `INF-008` lists slopes, stairs and ramps under "Examples:" and closes "Without one of these, the obstacle is impassable"; `INF-010` says those are "the three legal access points listed in INF-008, and no other construction grants access". In one twelve-rule document, four rules apart, a reader will notice — and the "Examples:" heading sits awkwardly over what the next rule calls a closed set of three.

They stay separate anyway, because this change transposes and does not redesign. `MOVE-011` and `MOVE-014` have that overlap today; folding them would change a rule's content in a change whose claim is that no rule's content changes, and it would be the one edit a reviewer could not check against a before-text.

**Recorded for a later Infantry cleanup:** fold `INF-010` into `INF-008` and settle whether the three access points are examples or an exhaustive list. That question predates this change and is not made worse by it.

## Decision 15 — Two citations on one line can make the linter read the wrong owner

Found by applying the change, not by auditing it, and worth recording because the next author will write the same sentence.

`scripts/lint_ruleset.py:41` pairs a filename with the first parenthesised rule ID within eighty characters of it:

```
CROSS_REF_RE = re.compile(r"`([\w.-]+\.md)`[^\n]{0,80}?\(([A-Z]{2,6}-\d{3})\)")
```

The scanner does not stop at the end of a citation. `VEH-007` as this change first wrote it read `` …lateral movement (`17-infantry.md`, INF-003). Neither moves diagonally — `07-movement.md` (MOVE-007) states… ``. The comma-form citation of `17-infantry.md` carries no parentheses, so the scanner kept reading, found `(MOVE-007)` about fifty characters later, and reported `08-vehicles.md: references 17-infantry.md (MOVE-007), which does not exist`. A false positive against a sentence that is correct for a reader — and the `Docs ruleset linter` is the required check, so a correct sentence would have blocked the merge.

**The rule to follow: on a line carrying two citations, the parenthesised one goes first.** Then the only `(ID)` sits immediately after the document that owns it, and the comma-form citation has nothing after it to swallow. Section 10 of `tasks.md` applies that to `VEH-007` by splitting the sentence in two.

**Not proposed: widening or anchoring the regex.** It would be a `scripts/` change on another branch, the eighty-character window is what lets the common `` `08-vehicles.md`, see (VEH-013) `` shape resolve at all, and one ordering convention costs nothing. What this change owes is the note, which is here.
