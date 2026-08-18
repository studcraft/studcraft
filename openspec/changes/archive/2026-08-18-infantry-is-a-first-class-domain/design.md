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

**Rejected: leaving Movement with no forward pointers at all.** The stairs contrast — infantry climb them, vehicles never do — is the single most-confused point between the two documents and had to survive somewhere. It ended up in `MOVE-013` itself, which is where a reader of the stairs rule meets it. `07-movement.md`'s `# Vehicle Movement` section, renamed `# Unit Movement` and then deleted outright, carried it for two intermediate states and was itself the defect: an index of another document's rule IDs (`tasks.md`, task 11.7).

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

`VEH-007` gets the same treatment for the same reason: "StudCraft does not use diagonal movement" is `MOVE-007`, stated universally. `VEH-007` keeps its own sentence — vehicles combine forward movement with turns — and points at `MOVE-007` for the ban itself. `MOVE-001`'s trailing "Diagonal movement is never allowed" is the third statement of the same ban in the same document and is dropped, and `VEH-005`'s is the fourth.

**An intermediate draft had `VEH-007` add "where infantry combines forward with lateral movement".** That clause went the same way, one review later (`tasks.md`, task 11.6): `MOVE-007` already draws the contrast, drew it more accurately — it says infantry combines forward **or backward** with sideways, where `VEH-007` said only forward — and two statements of one derivation had disagreed inside a single change before either shipped.

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

**`CORE-003` keeps infantry identity and gains a signpost.** It states that infantry are minifigures occupying one Unit Base, which is universal and belongs where the other unit types are classified. `INF-001` opens with that one sentence and cites `CORE-003` inside it.

**An earlier draft tried to have it both ways** — it stated the fact and then added "and this document does not restate it", which is a promise about the document contradicted by the words in front of it, and the same species as the three disclaimers `proposal.md` indicts in its opening argument. Review of pull request #112 caught it (`tasks.md`, section 14). One sentence with its citation attached is not a second owner: a document called Infantry that never says what an infantry model is does not stand alone, and the alternative was a rule whose entire body was a forwarding address.

What `CORE-003` lacked is the pointer `CORE-004` already has at `08-vehicles.md`; task 3.3 adds it, so the rule that names infantry names the infantry document.

## Decision 8 — One glossary entry, added on review rather than up front

`system/documentation-standards.md` ("Adding a New Ruleset Document") asks for "the new terms a reader cannot infer". The first draft concluded that `docs/17-infantry.md` introduces none — *infantry*, *step*, *obstacle* and *access point* all appeared in `07-movement.md` already, and none was in the glossary.

**That was right about the words and wrong about one of them.** The audit of the applied text found *step* carrying three senses within fifty lines of the new document: a Unit Base increment (`INF-012`), a stair tread (`INF-009`), and a Component State advancing one step (`DMG-005`). The collision was inherited, but extraction is what put all three in front of one reader — and the load-bearing sense is stated only inside `INF-012` while the Summary uses it at a distance. `Terrain Threshold`, its counterpart on the vehicle side, has had an entry all along. `## Step` was added by `tasks.md`, task 11.15.

The glossary's *Wounded* entry is also edited, because it cites `MOVE-021` and that ID retires. That one is a re-aim, not a new entry.

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

**One value was later added to the ruleset by this change and is not in the table above**, because it is a decision rather than a transposition: what a staircase with a 4-to-6-plate step costs infantry. Decision 16.

## Decision 10 — No `openspec/specs/` delta

`system/proposal-review.md` ("Delta vs. Direct Edit"): a `MODIFIED` delta can only target a capability that already exists. No capability under `openspec/specs/` describes which document states a movement rule, and nothing under it describes stairs at all — the three capabilities in play are `unit-base`, `action-economy` and `component-damage`, and every requirement and scenario in them survives untouched: a Wounded infantry model still moves two steps, an obstacle of 4 plate layers still costs the extra Action Point, and a fall of one brick still rolls nothing.

**One behaviour does change**, and it is deliberately not covered by that list: Decision 16 makes a staircase with a 4-to-6-plate step cost 1 additional Action Point per such step where it used to be impassable. No spec requirement stated the old answer, because no rule did — that is what made it an ambiguity rather than a rule. **So the delta-free decision stands on "no capability describes this", not on "no behaviour changed".**

This change also introduces no new capability. Infantry movement is not new behaviour; it is existing behaviour with an owner.

## Decision 11 — Adding a new ruleset document was impossible; the fix is to require less

`docs/17-infantry.md` is created without a version header, and three mechanisms then contradicted each other. This is the finding that changed the change's shape, so it is written out in full.

1. `.claude/hooks/guard_repo_edits.py:154` denies any edit writing that header from a branch that is not `release/v*`. `system/documentation-standards.md` (Versioning) is why: several proposal branches are in flight and each would pick a colliding number.
2. `scripts/release_cut.py` rewrote the header where `DOC_VERSION_RE` matched and skipped the file where it did not. A document created without one never acquired one.
3. `scripts/lint_ruleset.py` **required** one on any document that defines rules, and it is the `Docs ruleset linter`, the required check.

So the ruleset could not gain a new rule-bearing document at all. Both halves are fixed here:

- **`release_cut.py` inserts the header** into a rule-bearing document that has none, below the title and as **exactly one line**. Not a style choice: `.github/workflows/docs-require-proposal.yml` constrains the `release/v*` exemption by content — every added or removed line in the `docs/*.md` diff that is not `^[+-]\*\*Version:\*\*` fails the check, and a bare `+` for a blank line is one. Getting this wrong breaks the first release cut after the change, not the change's own pull request.
- **`lint_ruleset.py` stops requiring the header.** The disagreement check stays.

**The first draft kept the requirement and added `VERSION_DEBT`**, a closed list of documents awaiting their first cut, in the shape `SECTION_DEBT` already uses. It was rejected on review, and the reason is worth keeping: an exemption list is a standing obligation. Someone has to add the entry before the document lands and delete it after the next cut, and the deletion is the half that gets forgotten. Making the list self-clearing — a listed document that already carries a header is an error — only converts forgetting into a broken build later.

**Ask instead what the check was protecting.** Nothing in the repository reads a version header: `release_cut.py` writes it, the linter compared them, the hook and two workflows forbid writing it by hand. Nothing computes with it. So a document without one costs a reader a version number until the next cut, and costs the checks nothing — and the cut now supplies it, which makes the situation self-healing rather than merely tolerated.

What is worth checking survives untouched: **two different project versions across `docs/*.md`** is the repository being wrong. A missing header is the repository being new.

**Rejected: deriving the exemption from git** — asking whether the file existed at the latest `v*` tag, the way `scripts/check_id_stability.py` compares against a base revision. It is the most precise answer and it does not work where it has to: `.github/workflows/docs-ruleset-linter.yml` uses `actions/checkout@v4` at its default depth, with no history and no tags, so the linter would have to fail open in CI — which is the case it exists to cover.

**Rejected: writing the header by hand at `0.2.0 Draft` to match its siblings.** The hook refuses it, `scripts/apply_tasks.py` refuses it a second time, and the workflow forbids it. Three independent refusals is the repository saying this is not the route.

**Rejected: shipping `docs/17-infantry.md` with no rule IDs**, as prose the ruleset links to, so the linter never asks. That is not a ruleset document, and the point is that infantry rules should be numbered rules in a document of their own.

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

## Decision 16 — A stair's step is an obstacle, and there is no stair mechanic

**This is the one decision in the change that alters play.** Everything else moves text. It was made by the maintainer on review of pull request #112, after the extraction surfaced a contradiction the split had inherited rather than caused.

`INF-009` said a stepped surface carries infantry only where no step is taller than one infantry crosses freely — 3 plate layers (`INF-006`). `INF-007` says an obstacle of 4 to 6 plate layers is climbed for 1 additional Action Point. A staircase with 5-plate steps was therefore either no path at all or a series of climbable obstacles, and nothing chose. `MOVE-013` and `MOVE-010` had the same contradiction in the same words; putting the two rules four apart in one short document is what made it visible.

**The resolution: a step is an obstacle, read exactly like any other.** 3 plate layers or fewer crossed freely, 4 to 6 for 1 additional Action Point, 7 or more not climbable at all — the same three bands `INF-006`, `INF-007` and `INF-008` already state, applied per step.

What that buys is the removal of a mechanic rather than the addition of one. There is no stair rule now, because there never needed to be: the obstacle bands answer the question at any height, and `INF-009`'s special clause was an exception carrying a contradiction. `CODE_OF_DESIGN.md` Principle 11 — the simpler of two solutions — and Principle 12, since the same physical fact is now read the same way wherever it appears.

**What changes in play, precisely:** a staircase with a step of 4 to 6 plate layers was impassable and now costs 1 additional Action Point. A step of 7 or more still stops the climb. Ordinary stairs, built from steps of a plate or two, cost nothing exactly as before — the common case is untouched, and the case that moves is the one no rule had decided.

**The asymmetry with `VEH-027` is deliberate and now stated in `INF-009`.** A vehicle reads a staircase as one obstacle of its total rise, never as a series of small ones; infantry reads it step by step. Two documents giving different answers about the same plastic looks like a defect until the reason is written down, so it is: infantry takes the steps and a vehicle cannot.

**Rejected: leaving it open and shipping the contradiction.** Section 11 of `tasks.md` did exactly that, on the grounds that closing it decides a rule and this change transposes. That was the right default and the wrong outcome — the change put the two rules in one document, where a reader meets both within fifty lines, and shipping a document whose own rules disagree is worse than deciding.

**Rejected: a per-staircase total rise for infantry, matching `VEH-027`.** It would need a rule of its own, would make a tall staircase impassable to infantry that can plainly walk up it, and would answer a question the obstacle bands already answer.
