# Construction Standard states only what it owns

## Why

`docs/04-construction-standard.md` answers two different questions. One is its own: **what must physically be built for a model, terrain piece, mechanism or weapon to be legal.** The other belongs to eight other documents — what a built thing costs to operate, how much it carries, how far it shoots, what happens when it is hit.

Thirteen of its twenty-four rules state something another document already owns, and several say so in their own text: `SCS-019` is one sentence pointing at `WPN-003`, `SCS-020` one sentence pointing at `WPN-004`, `SCS-003` one sentence pointing at `VEH-001`. A pointer-only rule is not a rule; it is a second place a reader has to visit to learn there was nothing there.

`system/documentation-standards.md` ("What `system/` Is For") states the rule this change applies to the ruleset: one owner per rule, a pointer instead of a copy.

The narrow purpose this change enforces:

> **The Construction Standard defines what must be built. It does not define what the built thing does during the game.**

## What Changes

Nine ruleset documents and `TODO.md`. **Thirteen rules are retired, six are trimmed, four sentences move to the documents that own them, and seven citations are retargeted.** `tasks.md` carries the edit-by-edit coverage; sections 1–16 are the change as proposed, section 17 the repairs its own audit found, and section 18 the seven changes the review of pull request #104 asked for.

Review of #104 widened the change in two directions, both of them items this proposal had recorded as Out of Scope and the reviewer asked to close. **`CMP-009` and `CMP-010` stop restating the `1 AP` cost** that `CORE-007` owns, and **`VEH-015` and `DEP-005` stop citing `CORE-001`** for the fit rule it no longer states — retargeted to `TRN-019`, without restoring anything to `CORE-001`. It also asked for three deletions inside the Construction Standard itself: **`SCS-010`, `SCS-011` and `SCS-012` lose their closing sentence** naming `07-movement.md` as the owner of their gameplay consequence. The rule states a construction requirement; that it does not state the movement rule is visible from the rule.

### Retired

Each retirement names the rule that already states the retired text.

- **`SCS-001` — Unit Base.** `CORE-001` defines the Unit Base, its `4 × 3` footprint and its use as the measuring unit for every distance, Deployment Volume and footprint. `SCS-001` restated all three and defined nothing. Cited by nothing.
- **`SCS-003` — Vehicle Footprint.** `VEH-001` owns the footprint examples, the absence of a maximum size, and the Deployment Volume bound — in the same words. `WPN-005` is retargeted to it.
- **`SCS-004` — Facing.** Its one sentence with no other owner — a model whose front is ambiguous is not legal — **moves to `CORE-002`**, which defines Facing. The glossary's *Facing* entry is retargeted.
- **`SCS-005` — Physical Volume.** `TRN-019` states the fit rule and cited `SCS-005` for it; it **absorbs the one clause it did not already carry** and stops citing a retired rule. `GEO-003` owns "measured values come from Gameplay Geometry"; `GEO-004` and `CMP-018` own resolving an opening against the plastic as built.
- **`SCS-014` — Cargo Compartments.** `TRN-003` defines transport capacity as the Unit Base volume available inside the compartment, and `DEP-005` states the rest in its own words: "Transport capacity is not purchased. It is determined entirely by the physical cargo compartment … The LEGO model is the source of truth." Cited by nothing.
- **`SCS-015` — Weapon Mounts.** `WPN-009` states both of its sentences — weapons physically attached to the model, floating weapons not permitted — and adds the list of valid mounts. Cited by nothing.
- **`SCS-018` — Muzzle Placement Standard.** `WPN-019` states the Weapon Front and the prohibition on rear, side, top and bottom faces; `WPN-007` and `WPN-020` own adjacency. Nothing survives a construction-only reading. Cited by nothing.
- **`SCS-019` — Weapon Length.** A pointer to `WPN-003`. Cited by nothing.
- **`SCS-020` — Weapon Size Limit.** A pointer to `WPN-004`. Cited by nothing.
- **`SCS-021` — Equipment.** `CORE-014` states equipment must be physically represented and cannot be used if absent. `SCS-021` restated it and pointed at it in the next line. Cited by nothing.
- **`SCS-022` — Shields.** `CMP-014` defines a Shield as carried infantry equipment that may be targeted or interpose exactly like any other component, requires it to be physically attached, visible and occupying one hand, and states the no-bonus rule; `DMG-007` owns interposition. Its one sentence with no other owner — a shield facing the attacker interposes, one facing away does not — **moves to `CMP-014`**, which is what makes `CORE-002`'s `Shield direction` bullet mean something. Cited by nothing.
- **`SCS-023` — Transparency.** Its visibility clause **moves to `CORE-008`**, the universal Physical Visibility rule. `DMG-008` already owns the mechanical half word for word: every component resolves an Impact identically "regardless of what it represents — glass, metal, wood, infantry, or anything else." `WPN-012` is retargeted.
- **`SCS-024` — Damage Representation.** `CORE-016` states physical representation over markers as the universal rule. `DMG-008` is retargeted — it currently cites `CORE-016` **and** `SCS-024` for the same sentence.

### Trimmed

- **`SCS-007` — Doors.** Loses the `1 AP` cost (`CORE-007`, which `SCS-006` already points at) and "A decorative door cannot be used" (`SCS-006`, and `CMP-009` a third time). Keeps the physical requirement: a functional door must open, and may close.
- **`SCS-008` — Ramps.** Loses the `1 AP` cost (`CORE-007`) and "Once deployed, it becomes valid terrain" (`MOVE-019`: "A lowered ramp immediately becomes usable terrain"). Keeps the mechanism requirement.
- **`SCS-009` — Windows.** Loses visibility, targeting and the destruction procedure (`CMP-011`, `TRN-012`, `CORE-008`, `DMG-006`). Keeps the sentence `CMP-011` and `TRN-012` both cite it for: transparent LEGO elements represent windows.
- **`SCS-010`, `SCS-011`, `SCS-012` — Walls, Slopes, Stairs.** Each loses "How *X* affects movement during a game is defined in `07-movement.md`." Asked for by the review of #104: the sentence explains an ownership the rule already demonstrates, and `07-movement.md` is not made any more the owner by being named here. Each keeps its construction requirement and nothing replaces the deleted line.
- **`CMP-009`, `CMP-010` — Doors, Ramps.** Each loses "Opening or closing … costs **1 Action Point** (see `02-core-rules.md`, CORE-007)". `CORE-007` owns the cost; `MOVE-018` and `MOVE-019` already point at it without repeating the number, and after this change so do these two. The physical requirements — must physically open and close, must physically move — are untouched, and the cost is unchanged.

### `TODO.md`

`TODO.md` records the gaps the ruleset declares in its own text and quotes each one verbatim; `scripts/check_todo_quotes.py` compares them character for character on every `preflight` run. Two of its entries quote text this change edits, so both move with it — a `docs/` edit that leaves them behind turns the pull request red.

- **The *Cosmetic guidance for specific constructions* entry** quotes `DMG-008`'s sentence in full, including the `SCS-024` citation this change removes. The blockquote is updated to the sentence as it will read.
- **The *Energy shields as a transparent-material example* entry** quotes `SCS-023`'s example list, and is removed with the rule. The gap it recorded was declared by a speculative example — "Energy shields (future)" — which `system/documentation-standards.md` ("How a Rule Is Written") excludes from a rule in the first place. Once the example goes, no document declares that gap, and `TODO.md`'s own preamble scopes the file to gaps the ruleset declares. Retiring the entry is what keeps that claim true (`design.md`, Decision 11).

### Kept, unchanged

`SCS-002` (infantry base), `SCS-006` (interactive elements must physically exist), `SCS-010` (walls), `SCS-011` (slopes), `SCS-012` (stairs), `SCS-013` (platforms), `SCS-016` (at least one visible functional muzzle), `SCS-017` (every muzzle connects to a weapon body). Each states a physical requirement no other document states, and each already delegates its gameplay consequences.

## What Does Not Change

- **No rule ID moves, and nothing is renumbered.** Thirteen IDs are retired — deleted outright, left as visible gaps, never reissued. No stub is left behind. `system/documentation-standards.md` (Naming Conventions) permits deletion and forbids renumbering and reuse; `scripts/check_id_stability.py` reports neither a deletion nor a gap.
- **No gameplay value.** No distance, cost, dimension, threshold, capacity or state changes. Every sentence deleted here is left standing where its owner states it, with the four recorded exceptions that move rather than being deleted: `SCS-004`'s legality sentence to `CORE-002`, `SCS-023`'s visibility clause to `CORE-008`, `SCS-022`'s orientation sentence to `CMP-014`, and `SCS-005`'s gap clause to `TRN-019`.
- **`SCS-016` and `SCS-017`.** Both are weapon-shaped and both survive: `WPN-002` defines what a muzzle *is* but never requires a weapon to have one, and no `10-weapons.md` rule requires a muzzle to connect to a body. `docs/14-glossary.md`'s *Weapon Body* entry cites `SCS-017` for exactly that.
- **`CMP-009`'s and `CMP-010`'s physical requirements.** Only the restated cost goes; "Must physically open and close", "Must physically move", the `CMP-018` clearance clauses and the decorative-has-no-effect lines all stay.
- **`openspec/specs/`.** No capability delta. No requirement or scenario stops being true: the rules move nowhere, only the document that states them changes.
- **`CHANGELOG.md` and every `**Version:**` header.** Release-cut-only (`system/documentation-standards.md`, Versioning). No `**Bump:**` line — this removes no rule that was not already stated elsewhere.

## Checked elsewhere

- `python3 scripts/rule.py refs` on all twenty-four `SCS` IDs. Nine of the thirteen retirements are cited by nothing. The four that are cited — `SCS-003` (`WPN-005`), `SCS-005` (`TRN-019`), `SCS-023` (`WPN-012`), `SCS-024` (`DMG-008`) — each get their citation retargeted in this change.
- `grep -rn "SCS-0"` across `docs/`. `rule.py refs` reads the rule graph and does not see `docs/14-glossary.md`, which cites `SCS-004` (retired here, retargeted), `SCS-006` and `SCS-017` (both kept). `docs/07-movement.md` cites `SCS-002` (kept).
- `grep -rn "SCS-0"` across the whole repository, `TODO.md` included — `rule.py refs` reads only the rule graph, and `scripts/lint_ruleset.py` reads only `docs/` and `assets/IMAGES.md`. Two live hits outside `docs/`: `TODO.md`, which quotes `SCS-023` and `DMG-008` and is edited here, and `system/proposal-review.md:182`, which cites `SCS-003` inside a worked example and is repaired on a separate branch — see Out of Scope. The archived changes under `openspec/changes/archive/` cite retired IDs and are left alone: an archive records what was proposed then. `tests/test_build_index.py` uses `SCS-001` as a synthetic fixture string that never reads `docs/`.
- `grep -rn -i "shield" docs/`. `CMP-014` and `DMG-007` cover everything `SCS-022` said except orientation, which nothing else states and which `CORE-002`'s `Shield direction` bullet depends on — hence the move rather than a plain deletion.

## Out of Scope

- **Every other stale cross-reference in `system/`.** There is none — `grep -rn "SCS-0" system/` returns nothing after section 19. `system/proposal-review.md:182` was the only one, and it is fixed here rather than deferred (`design.md`, Decision 11).
- **`CORE-002`'s `Shield direction` bullet.** `CORE-002` lists shield direction among the things Facing determines. After this change `CMP-014` states what shield orientation actually does, and it is geometric: what the shield physically stands between, which is not the same as the Facing a unit's base declares. Whether the bullet should stay, be reworded, or point at `CMP-014` is a `02-core-rules.md` question (`design.md`, Decision 12).
- **`docs/04-construction-standard.md`'s `# Summary`.** "Construction defines gameplay. Gameplay rewards good construction." reads on a document whose eleven surviving rules are all build requirements. Both sentences stay true — the document states what must be built and the other systems read it — and neither restates a rule that left, which is what `system/proposal-review.md` ("The Summary Is Part of the Rule") guards against. Rewriting a document's philosophy is a separate decision from removing what it does not own.
- **`docs/05-construction-components.md`, `CMP-018`.** Longer than every other component rule and mixing width, height, Unit Base measurement, vehicle width, ramps, firing ports, windows, access points and examples. Raised in the review of #104 and deliberately left there: it is a `05-construction-components.md` cleanup, and solving it by expanding the Construction Standard again would undo this change.
- **`SCS-002`'s facing pointer,** which `MOVE-002` states in the same words. Both are pointers at `CORE-002` rather than definitions, and neither is the restatement this change is about.
- **`01-foundations.md`,** whose *Physical Representation* section overlaps `CORE-016` and now carries more of the physical-representation weight. It defines no rules.
- **Renumbering.** Forbidden, and named here because the source brief for this change asked for it.
