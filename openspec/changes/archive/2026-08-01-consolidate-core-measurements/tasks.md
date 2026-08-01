## 1. Trim Unit Base Restatements

- [x] 1.1 `01-foundations.md` "Unit Base (UB)" section: keep the short restatement ("4 × 3 studs") but add a cross-reference to `02-core-rules.md` (CORE-001); trim the elaboration to what isn't already covered there.
- [x] 1.2 `04-construction-standard.md` SCS-001: keep the rule ID, trim the restatement to a one-line cross-reference to CORE-001, keep the construction-standard-specific framing (this is *the* fundamental building unit for construction purposes). → Also found and fixed SCS-002 (Infantry Base) during verification, which independently restated "4 × 3 studs" a second time in the same document — not caught in the original audit, missed because the audit only checked SCS-001.
- [x] 1.3 `06-deployment.md`: trim its Unit Base restatement to a cross-reference to CORE-001, keep the deployment-specific context (deployment areas measured in UB).
- [x] 1.4 `07-movement.md`: trim its Unit Base restatement to a cross-reference to CORE-001, keep the movement-specific context (infantry mounted on standard UB, movement math derived from it).
- [x] 1.5 `08-vehicles.md` VEH-001: keep the rule ID and the vehicle-footprint examples (Motorbike, Jeep, Tank, Heavy Transport), trim only the "One Unit Base measures 4×3 studs" restatement to a cross-reference to CORE-001.
- [x] 1.6 `09-transport.md` TRN-001: keep the rule ID, trim the restatement to a cross-reference to CORE-001, keep the transport-specific framing.

## 2. Trim Action Points Restatements

- [x] 2.1 `01-foundations.md` "Action Points (AP)" section: keep the short restatement ("3 Action Points") but add a cross-reference to `02-core-rules.md` (CORE-006); trim the elaboration to what isn't already covered there.
- [x] 2.2 `03-game-flow.md` FLOW-004 (Unit Activation): keep the procedural content (receives AP on activation, spends in any legal order, activation ends when done or player stops, once per Turn) but cross-reference CORE-006 for the "3" instead of asserting it fresh.
- [x] 2.3 `03-game-flow.md` FLOW-005 (Universal Action Points): keep the rule ID, but trim to only its content not already in FLOW-004/CORE-006 — the explicit list of unit types this applies to (Infantry, Vehicles, Walkers, Hovercraft, future types) and "no unit gains additional AP through its profile" — cross-referencing CORE-006 for the "3" itself.
- [x] 2.4 `03-game-flow.md` FLOW-011 (Action Economy) and FLOW-012 (No Hidden Statistics): lightly trim any bare "3 AP"/"gain 3 AP" restatement to reference CORE-006, keep the philosophy/rationale content (AP as universal resource, no hidden activation values) which is genuinely unique to these rules. → FLOW-011 never actually restated the number, only FLOW-012 did ("Gain 3 AP." in its activation-sequence list) — fixed that one line. The Turn Sequence diagram and the closing Summary still mention "3 AP" as part of a process overview/recap; left as-is, same non-normative-restatement convention used throughout the rest of the ruleset (e.g. Weapon System summaries restate Range = 2 × Length without being a duplication problem).

## 3. Fix the Reading-Order Staleness Bug

- [x] 3.1 `01-foundations.md` "Learning StudCraft" section: replace the independent 14-item reading-order list (already stale — missing `docs/15` and `docs/16`) with a pointer to `README.md`'s Rulebook section.

## 4. Validation

- [x] 4.1 Run `python3 scripts/lint_ruleset.py` after all edits and fix any structural issues it reports. → Passes, 16 docs, no issues.
- [x] 4.2 Confirm no measured rule value, formula, or Version header changed anywhere — this is a pure editorial consolidation (per design.md Goals). → Confirmed via diff review.
- [x] 4.3 Spot-check that every trimmed section still reads coherently on its own (per design.md's "keep a short inline restatement" mitigation) — a reader shouldn't hit a bare "see CORE-001" with no value shown. → Confirmed; this pass is what caught the missed SCS-002 duplicate (see 1.2).

## 5. Housekeeping

- [x] 5.1 No `CHANGELOG.md` edit needed — `Release cut` computes the bump automatically from git history. This change is purely editorial (no rule value changes), so the automatic minor default is correct; no `**Bump:**` marker needed.
- [x] 5.2 Open a PR from the `consolidate-core-measurements` branch for review. Do not archive in the same PR — archiving is a separate, later step (see `system/workflow.md`, Archiving), via the batched `Archive cut` action.

> Ticked during the 2026-08-01 archive reconciliation. These boxes recorded process steps that had already happened — the PR merged long ago, or the task states that no action was required. They were blocking `archive_cut.py`, which refuses to archive a change with unchecked tasks. No ruleset work was left undone.
