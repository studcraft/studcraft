# AGENTS.md

> Instructions for AI agents contributing to StudCraft.

---

# Purpose

This document defines how AI agents should interact with the StudCraft repository.

StudCraft is a specification-driven project.

Agents are expected to preserve the project's philosophy, maintain consistency and extend the rules without introducing unnecessary complexity.

Before making any contribution, every agent should read:

1. `README.md`
2. `CODE_OF_DESIGN.md`
3. `CONTRIBUTING.md`
4. This file, plus the relevant `system/*.md` documents below.

These documents define the project's identity.

---

# Project Philosophy

StudCraft is founded on one central idea:

> **The Model Is The Rules.**

Gameplay should emerge from the physical LEGO model whenever possible.

Avoid replacing physical representation with abstract mechanics.

---

# Core Principles

Every contribution should reinforce the following principles:

- The Model Is The Rules
- Every Brick Matters
- Construction Over Abstraction
- Components Over Statistics
- Impacts Over Damage
- Physical State Over Tokens
- Modular Design
- Simplicity Before Complexity

If a proposal conflicts with these principles, redesign it.

---

# System Documents

Detailed rules live in `system/`. Read the ones relevant to the task at hand.

| Document | Covers |
|---|---|
| [`system/agent-responsibilities.md`](system/agent-responsibilities.md) | What agents should and shouldn't do |
| [`system/design-process.md`](system/design-process.md) | Design Process, Rule Hierarchy, Preferred Design Patterns, Decision Filter |
| [`system/documentation-standards.md`](system/documentation-standards.md) | Repository Structure, Documentation Guidelines, Naming Conventions, Versioning |
| [`system/workflow.md`](system/workflow.md) | OpenSpec Workflow, Git Workflow, Versioning (release-cut), Archiving (archive-cut) |
| [`system/proposal-review.md`](system/proposal-review.md) | How to review a proposal before applying/archiving: cross-document checks, common failure classes, reviewing the applied text, delta vs. direct edit |
| [`system/ci-gates.md`](system/ci-gates.md) | Required-check design pitfalls, branch-naming exemptions and why the name alone is not enough, concurrency guards, checking late-firing failures early, batch-vs-per-PR pattern for shared state |
| [`system/delegating-to-agents.md`](system/delegating-to-agents.md) | Writing a change a less capable model can apply perfectly, and what the reviewer still has to do |
| [`system/repository-strategy.md`](system/repository-strategy.md) | BLOCKER git history rules: no force-push, no rewriting history, linear-only; squash-merge consequences for branch cleanup and conflicts |
| [`system/communication.md`](system/communication.md) | Language, tone, proposal framing |
| [`system/vision.md`](system/vision.md) | Long-term direction |

---

# Delegating Work

Three roles are defined as repository agents in `.claude/agents/`, so their constraints live in the repository rather than in whoever is driving the session:

| Agent | Model | When |
|---|---|---|
| [`ruleset-auditor`](.claude/agents/ruleset-auditor.md) | Opus, read-only | **Twice per change** — on the proposal before it is applied, and on the applied text afterwards. Also on `docs/` at any time. |
| [`proposal-applier`](.claude/agents/proposal-applier.md) | Sonnet | Once the proposal has passed its audit. Transcription only. |
| [`git-operator`](.claude/agents/git-operator.md) | Haiku | After you have read the result. Branch, commit, push, open the PR. Decides nothing. |

Design the change, audit the proposal, apply it, audit the result, then **read it yourself**. That step never belongs to an agent.

Deciding the result is fit to push is therefore yours. Issuing the commands afterwards is not — `git-operator` is handed the paths, the branch name and the message text, and selects none of them. Delegating the typing is not delegating the judgement.

`system/delegating-to-agents.md` explains why the split works and how to write a change a less capable model applies perfectly.

---

# Final Principle

Whenever an agent is uncertain about a design decision, return to the project's central philosophy:

> **The Model Is The Rules.**

If the LEGO model can express the rule, let the model do the work.

---

> **Every Brick Matters.**
