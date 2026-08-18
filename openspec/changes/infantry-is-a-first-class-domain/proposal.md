# Infantry is a first-class domain

## Why

Vehicles are a rules domain. `docs/08-vehicles.md` states what a vehicle is, how far it moves, how it turns, what terrain it crosses, how it ascends and what happens when it falls — thirty-one rules, all of them about vehicles, in the document named for them.

Infantry has no such document. Its identity, its three movement distances, its rotation, its three obstacle thresholds, its slope and stair behaviour, its access rules, its falling damage and its Wounded limit are all written in `docs/07-movement.md`, the document named for the universal mechanic.

That is not a filing accident, and `07-movement.md` already knows it. Three passages in that file exist only to warn a reader which paragraphs are not for them:

- `MOVE-012` — "That paragraph is the infantry rule. A vehicle reads this rule for what a slope is built from and nothing else."
- `MOVE-016` — "This rule covers infantry only. Vehicle falling is defined separately in `08-vehicles.md` (VEH-026)."
- The `# Infantry Damage Effects` heading — "Unlike the rules above this heading, these are infantry-only."

`08-vehicles.md` carries the same warning from the other side. `VEH-021` tells a vehicle **not** to use `MOVE-011`, "it is the infantry rule". `VEH-008` sources a vehicle's turn cost from "`MOVE-008`'s infantry rotation cost". `VEH-026` resolves vehicle falling "exactly as infantry falling is (`07-movement.md`, MOVE-016)".

Two sibling domains, and one of them reaches into the other for an Action Point cost and a dice procedure. The disclaimers are a document apologising for its own shape.

The narrow purpose this change enforces:

> **Movement defines the mechanics every unit shares. Each unit domain defines what its own units do with them. No unit domain reads a rule belonging to another.**

`CODE_OF_DESIGN.md` Principle 10 states it as "each document in the repository should have one clear responsibility", and Principle 12 as consistency: the problem was solved for vehicles and left unsolved for infantry.

## What Changes

A new `docs/17-infantry.md`, and seven existing documents.

**Ten `MOVE-` rules are retired and reappear as `INF-` rules.** Rule identifiers are never renumbered (`system/documentation-standards.md`, Naming Conventions), so this is a deletion and a new authorship, not a rename: `MOVE-002`, `MOVE-004`, `MOVE-005`, `MOVE-006`, `MOVE-008`, `MOVE-009`, `MOVE-010`, `MOVE-011`, `MOVE-016` and `MOVE-021` are retired, left as gaps, and never reissued. No stub is left where they were.

**Three `MOVE-` rules keep their numbers and shrink to their generic half.** `MOVE-012`, `MOVE-013` and `MOVE-014` each state a terrain construction — what a slope is built from, what a stepped surface is, what physically supports a unit — and then state what infantry does about it. The first half is what `VEH-027` already reads them for and stays; the second half moves to `INF-009` and `INF-010`.

**Eight `MOVE-` rules keep their number and their rule.** Three are untouched — `MOVE-017`, `MOVE-018`, `MOVE-020`. Five are edited, none of them changing what it decides: `MOVE-015` and `MOVE-019` lose a citation aimed at a rule that no longer exists, and `MOVE-001`, `MOVE-003` and `MOVE-007` stop stating an infantry-only capability as though it were universal. That last group matters more than it looks. `MOVE-001` gives "every unit" four movement directions, which no vehicle has; `MOVE-003` measures from "the base", which only infantry has; and `MOVE-007` tells a reader to combine forward and lateral movement, which is exactly what `VEH-007` says a vehicle does *not* do — and `MOVE-007` is the rule this change makes every vehicle read for the no-diagonal ban.

- **`docs/17-infantry.md`** — new. Twelve rules, `INF-001` through `INF-012`, carrying the retired text with its citations re-aimed. Identity (`INF-001`), the three distances and rotation (`INF-002` – `INF-005`), the three obstacle thresholds (`INF-006` – `INF-008`), slopes and stairs (`INF-009`), vertical access (`INF-010`), falling damage (`INF-011`), Wounded movement (`INF-012`).
- **`docs/07-movement.md`** — loses the ten rules, keeps eleven, and its `# Vehicle Movement` section and `# Summary` are rewritten. The document stops being an infantry rulebook with a generic preamble and becomes the generic layer both domains read.
- **`docs/08-vehicles.md`** — seven edits. Four stop the document reading infantry rules: `VEH-008` states its own Action Point cost, `VEH-021` names the infantry rule as a contrast instead of borrowing its list, `VEH-026` resolves its dice against `DMG-015`, which owns the procedure, and `VEH-027` keeps the stairs contrast and aims it at `INF-009`. One is the opposite and is correct: `VEH-026`'s disembarked infantry are pointed at `INF-008` and `INF-010`, because that sentence really is about infantry. And `VEH-007` and `VEH-005` stop restating the universal no-diagonal ban, which `MOVE-007` owns and `VEH-007` now points at — it was stated four times across the two documents.
- **`docs/02-core-rules.md`** — two citations re-aimed, in `CORE-005` and `CORE-006`. `CORE-005` also gains the vehicle side it was missing: it sent every unit, vehicles included, to the infantry obstacle rules.
- **`docs/03-game-flow.md`, `docs/05-construction-components.md`, `docs/16-damage-system.md`, `docs/14-glossary.md`** — one citation each, re-aimed from a retired `MOVE-` ID to the `INF-` rule that now carries the text.

## What Does Not Change

- **No gameplay value.** 12 studs forward in 3s, 12 sideways in 4s, 12 backward in 3s, 1 AP a move, 1 AP a rotation, the 3 / 4–6 / 7+ plate-layer bands, +1 AP to climb, one free brick of falling and one D6 per brick beyond it, two steps for a Wounded model. Every number is transposed character for character. `design.md`, Decision 9 tabulates them.
- **Vehicle movement stays in `08-vehicles.md`.** `VEH-004` through `VEH-012`, `VEH-021` through `VEH-028` are the vehicle implementation and are already where they belong. Nothing moves out of that document.
- **Transport rules stay in `09-transport.md`.** `TRN-002` states how much room an infantry model takes in a transport. That is Transport defining its own relationship, not an infantry rule filed wrongly (`design.md`, Decision 7).
- **No rule ID is renumbered or reused.** Ten numbers are retired; `MOVE-012`, `MOVE-013` and `MOVE-014` keep theirs while losing text; `MOVE-003` is not renumbered into the `MOVE-002` gap.
- **`docs/04-*.md` and `docs/13-*.md` stay empty.** Both numbers are retired (`README.md`; `system/documentation-standards.md`, Repository Structure). The new document is `17-`, the next unused number, because a retired number is never reissued (`design.md`, Decision 1).
- **`openspec/specs/`.** No capability delta. No requirement changes behaviour; what changes is which document states it (`design.md`, Decision 10).
- **`CHANGELOG.md` and every version header.** Release-cut-only. `docs/17-infantry.md` is created **without** one — writing that line by hand is refused by the `PreToolUse` hook and by the workflow, and the first prerequisite is what makes a header-less new document legal until the next cut supplies it (`design.md`, Decision 11).
- **`CORE-003`.** Infantry identity — a minifigure occupying one Unit Base — stays in `docs/02-core-rules.md`. `INF-001` cites it and states only the base, the facing and what the orientation decides. A change arguing for one owner per domain does not get to create a second owner for the thing it is about.

## Checked elsewhere

- `python3 scripts/rule.py refs MOVE-002 MOVE-004 MOVE-005 MOVE-006 MOVE-008 MOVE-009 MOVE-010 MOVE-011 MOVE-016 MOVE-021` — every inbound citation is accounted for by a task. Outside `07-movement.md` they are `FLOW-013`, `CORE-005`, `CORE-006`, `CMP-018`, `VEH-008`, `VEH-021`, `VEH-026`, `VEH-027`, `DMG-005` and the glossary's *Wounded* entry.
- `grep -rn "MOVE-" README.md TODO.md CODE_OF_DESIGN.md system/ assets/` — three files outside `docs/` cite `MOVE-` IDs, and `README.md` is **not** one of them: it names documents, not rules. `TODO.md` and `assets/IMAGES.md` are handled by the companion changes below. `system/proposal-review.md` cites `MOVE-016` and `MOVE-004` in its worked examples of past defects; **those stay as they are.** They are history, and `system/documentation-standards.md` treats a retired ID recorded in a postmortem the same way `openspec/changes/archive/` is treated — the text is about what happened, not about what the ruleset says now.
- `python3 scripts/rule.py refs` for `MOVE-012`, `MOVE-013`, `MOVE-014`, `MOVE-015` and `MOVE-019` — the five rules that survive with changed text. Every outside citer reads the half that stays: `VEH-027` reads `MOVE-012` for what a LEGO slope element is, and `MOVE-019`'s own citation of `MOVE-014` stays true of `MOVE-014`'s new text.

## The three companion changes, and the order

`system/repository-strategy.md` (Branch Naming) allows a `<change-name>` branch `docs/*.md` plus that one change. Everything else this change breaks lives outside that scope, and two of the repairs have to land **first** because `scripts/lint_ruleset.py` — the `Docs ruleset linter`, the one required check among the checkers — fails without them.

1. **Prerequisite — `release-cut-owns-new-document-versions`, a kebab-case branch, merged BEFORE this change.** `lint_ruleset.py` requires every rule-bearing `docs/*.md` to carry a release-cut version line and requires all of them to agree, and `docs/17-infantry.md` cannot be born with one: the `PreToolUse` hook refuses to write that line outside a `release/v*` branch, and `scripts/release_cut.py` only rewrites the line where it already finds one. The two rules are individually correct and jointly make a new ruleset document impossible to add. This change teaches `release_cut.py` to insert the line into a document that lacks it, and gives `lint_ruleset.py` a closed list — the shape it already uses for `SECTION_DEBT` — naming the document that is waiting for its first cut (`design.md`, Decision 11).
2. **Prerequisite — `images-index-releases-the-infantry-rules`, a kebab-case branch, merged BEFORE this change.** `lint_ruleset.py` also fails on any rule ID named in an `assets/IMAGES.md` entry that does not exist in the document the entry sits under. Two table rows under `## docs/07-movement.md` name `MOVE-009`, `MOVE-011` and `MOVE-016`, producing three errors. They are removed rather than re-aimed, because re-aiming them at `INF-` IDs before `docs/17-infantry.md` exists fails the same check from the other side. `assets/images/` is empty — the index specifies images to draw, and none has been drawn — so nothing but text moves.
3. **Follow-up — `infantry-references-outside-docs`, a kebab-case branch, merged AFTER this change.** `README.md` (structure list, Rulebook reading order, Current Status — this is also where Infantry is placed next to Movement for a reader, whatever the file is numbered); `TODO.md` (the two entries quoting `CORE-005` and `MOVE-004`); and `assets/IMAGES.md`, where the two rows return under `## docs/17-infantry.md` — **renamed as well as re-aimed**, because the linter requires each filename to start with its rule ID or its document number, so `move-016-falling-measurement.png` becomes `inf-011-…` and `07-terrain-thresholds.png` becomes `17-…`. That change also repairs the two prose citations of retired IDs at `assets/IMAGES.md` lines 96 and 156, which the linter does not read.

Two consequences are accepted rather than solved:

- **Until the follow-up merges, `README.md` does not list `docs/17-infantry.md`**, so `system/documentation-standards.md` ("Adding a New Ruleset Document") is briefly unmet. The branch scope leaves no alternative; the glossary half of that checklist **is** met here, by Decision 8.
- **Until the follow-up merges, `python3 scripts/preflight.py` reports `TODO.md quotes the ruleset verbatim` as FAIL on this branch.** That checker runs in no workflow, so it blocks nothing, and `tasks.md` section 9 says so where the applier will read it.

## Out of Scope

- **Extracting vehicle movement into a separate document.** `08-vehicles.md` is already the vehicle domain, movement included. Nothing about it needs fixing.
- **The `VEH-001` / `VEH-013` cross-reference loop**, and the split of `VEH-013`'s Pilot rules between Vehicles, Transport and Damage. Both are real and both are Vehicle cleanups, not infantry ones.
- **`TRN-002` possibly duplicating `CORE-003`.** A Transport cleanup.
- **A shared fall-damage rule owned by Movement or Damage.** The two falls are not the same mechanic — infantry's first brick is free and a vehicle's free height is its own Terrain Threshold — and only the dice procedure is common, which `DMG-015` already owns and both already cite (`design.md`, Decision 5).
- **Renumbering the ruleset so Infantry sits beside Vehicles.** Document numbers are never renumbered after removal, and `04-` and `13-` are retired gaps. Reading order is `README.md`'s job and belongs to the follow-up change.
- **A glossary entry for *Infantry*.** The document introduces no term a reader cannot infer (`design.md`, Decision 8).
- **Folding `INF-010` into `INF-008`.** The two overlap, inherited from `MOVE-011` and `MOVE-014`, and the "Examples:" heading over what the next rule calls a closed set of three is worth settling. Not here: this change transposes and does not redesign (`design.md`, Decision 14).
