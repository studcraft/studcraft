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

- **No gameplay value, with one decision recorded separately.** 12 studs forward in 3s, 12 sideways in 4s, 12 backward in 3s, 1 AP a move, 1 AP a rotation, the 3 / 4–6 / 7+ plate-layer bands, +1 AP to climb, one free brick of falling and one D6 per brick beyond it, two steps for a Wounded model. Every number is transposed character for character; `design.md`, Decision 9 tabulates them.

  **The exception is stairs**, and it is a rule decision rather than a transposition: `INF-009` used to make a stepped surface impassable if any step exceeded 3 plate layers, which contradicted `INF-007`'s 1 additional Action Point for an obstacle of 4 to 6. A step is now an obstacle read like any other. A staircase with a 4-to-6-plate step was impassable and now costs 1 AP; ordinary stairs, built from steps of a plate or two, still cost nothing. Review of pull request #112 closed it — `tasks.md`, section 15, and `design.md`, Decision 16.
- **Vehicle movement stays in `08-vehicles.md`.** `VEH-004` through `VEH-012`, `VEH-021` through `VEH-028` are the vehicle implementation and are already where they belong. Nothing moves out of that document.
- **Transport rules stay in `09-transport.md`.** `TRN-002` states how much room an infantry model takes in a transport. That is Transport defining its own relationship, not an infantry rule filed wrongly (`design.md`, Decision 7).
- **No rule ID is renumbered or reused.** Ten numbers are retired; `MOVE-012`, `MOVE-013` and `MOVE-014` keep theirs while losing text; `MOVE-003` is not renumbered into the `MOVE-002` gap.
- **`docs/04-*.md` and `docs/13-*.md` stay empty.** Both numbers are retired (`README.md`; `system/documentation-standards.md`, Repository Structure). The new document is `17-`, the next unused number, because a retired number is never reissued (`design.md`, Decision 1).
- **`openspec/specs/`.** No capability delta. No requirement changes behaviour; what changes is which document states it (`design.md`, Decision 10).
- **`CHANGELOG.md` and every version header.** Release-cut-only. `docs/17-infantry.md` is created **without** one — writing that line by hand is refused by the `PreToolUse` hook and by the workflow, and the first prerequisite is what makes a header-less new document legal until the next cut supplies it (`design.md`, Decision 11).
- **`CORE-003`.** Infantry identity — a minifigure occupying one Unit Base — stays in `docs/02-core-rules.md`, where the other unit types are classified. `INF-001` states it in one sentence and cites `CORE-003` in the same breath, which is a reader's convenience and not a second owner: a document called Infantry that never says what an infantry model is does not stand alone, and one sentence carrying its own citation cannot drift far from the rule it names.

## Checked elsewhere

- `python3 scripts/rule.py refs MOVE-002 MOVE-004 MOVE-005 MOVE-006 MOVE-008 MOVE-009 MOVE-010 MOVE-011 MOVE-016 MOVE-021` — every inbound citation is accounted for by a task. Outside `07-movement.md` they are `FLOW-013`, `CORE-005`, `CORE-006`, `CMP-018`, `VEH-008`, `VEH-021`, `VEH-026`, `VEH-027`, `DMG-005` and the glossary's *Wounded* entry.
- `grep -rn "MOVE-" README.md TODO.md CODE_OF_DESIGN.md system/ assets/` — three files outside `docs/` cite `MOVE-` IDs, and `README.md` is **not** one of them: it names documents, not rules. `TODO.md` and `assets/IMAGES.md` are handled by the companion changes below. `system/proposal-review.md` cites `MOVE-016` and `MOVE-004` in its worked examples of past defects; **those stay as they are.** They are history, and `system/documentation-standards.md` treats a retired ID recorded in a postmortem the same way `openspec/changes/archive/` is treated — the text is about what happened, not about what the ruleset says now.
- `python3 scripts/rule.py refs` for `MOVE-012`, `MOVE-013`, `MOVE-014`, `MOVE-015` and `MOVE-019` — the five rules that survive with changed text. Every outside citer reads the half that stays: `VEH-027` reads `MOVE-012` for what a LEGO slope element is, and `MOVE-019`'s own citation of `MOVE-014` stays true of `MOVE-014`'s new text.

## What travels with it, outside `docs/`

`system/repository-strategy.md` (Branch Naming) would put these on separate branches. They are here instead, in one pull request, at the maintainer's decision — `design.md`, Decision 12 records what that buys and what it costs.

- **`scripts/lint_ruleset.py`** — gains `VERSION_DEBT`, the closed-list shape it already uses for `SECTION_DEBT`, so a rule-bearing document waiting for its first Release cut is not failed for having no version line. The list clears itself: a listed document that already carries a header is an error, so the cut that supplies one forces the entry out.
- **`scripts/release_cut.py`** — inserts that line into a rule-bearing document that has none, below the title and as **exactly one line**. Not a style choice: `Docs require OpenSpec proposal` constrains the release-branch exemption by content and fails any added line in the `docs/*.md` diff that is not the header itself, which a blank line would be.
- **`tests/test_lint_ruleset.py`, `tests/test_release_cut_e2e.py`** — eleven tests over both, including the one that pins the single-line insertion and the one that proves the exemption clears itself.
- **`system/documentation-standards.md`** — three lines in "Adding a New Ruleset Document", because the next person to add one hits this and should not have to rediscover it.
- **`assets/IMAGES.md`** — `07-movement.md`'s three entries move to `17-infantry.md` and are renamed. The renames are forced: `check_image_index` requires a filename to start with the lowercased rule ID for a single-ID row and with the document number otherwise, so `move-003-…`, `move-016-…` and `07-…` all fail under a document numbered 17. `MOVE-003`'s entry moves although `MOVE-003` survives — the image shows a base measured from its leading face, which is now `INF-002`'s claim.
- **`README.md`** — the structure tree, the Rulebook reading order (Infantry between Movement and Vehicles, with a line saying the file numbers are creation order and not reading order), and Current Status.
- **`TODO.md`** — the two entries quoting `CORE-005` and the sprint sentence, which is now `INF-002`'s.

Adding a new ruleset document turned out to be impossible before this change, and `design.md` Decision 11 is the write-up: the `PreToolUse` hook refuses to write a version header outside a release branch, `release_cut.py` only rewrote headers it already found, and `lint_ruleset.py` required one. Three mechanisms, each correct alone.

## Out of Scope

- **Extracting vehicle movement into a separate document.** `08-vehicles.md` is already the vehicle domain, movement included. Nothing about it needs fixing.
- **The `VEH-001` / `VEH-013` cross-reference loop**, and the split of `VEH-013`'s Pilot rules between Vehicles, Transport and Damage. Both are real and both are Vehicle cleanups, not infantry ones.
- **`TRN-002` possibly duplicating `CORE-003`.** A Transport cleanup.
- **A shared fall-damage rule owned by Movement or Damage.** The two falls are not the same mechanic — infantry's first brick is free and a vehicle's free height is its own Terrain Threshold — and only the dice procedure is common, which `DMG-015` already owns and both already cite (`design.md`, Decision 5).
- **Renumbering the ruleset so Infantry sits beside Vehicles.** Document numbers are never renumbered after removal, and `04-` and `13-` are retired gaps. Reading order is `README.md`'s job and belongs to the follow-up change.
- **A glossary entry for *Infantry*.** The document introduces no term a reader cannot infer (`design.md`, Decision 8).
- **Folding `INF-010` into `INF-008`.** The two overlap, inherited from `MOVE-011` and `MOVE-014`, and the "Examples:" heading over what the next rule calls a closed set of three is worth settling. Not here: this change transposes and does not redesign (`design.md`, Decision 14).
