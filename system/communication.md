# Communication Style

Agents should:

- Reply in the same language the user writes their prompts in, using neutral/standard variety (e.g. neutral Spanish, not regional dialects like Argentinian or Chilean; standard English, not regional dialects).
- Explain **why** a proposal improves the design, not only what it changes. A proposal that states its reasoning can be argued with; one that states only its result can only be accepted or refused.
- Avoid unnecessary rewrites. Rewriting text that was already correct hides the real change inside a large diff, and on this repo it also causes artificial merge conflicts with every concurrent branch (`system/repository-strategy.md`).

*Prefer evolution over replacement* and *preserve backwards compatibility* used
to be on that list. They are Principle 15 (Future Compatibility) in
`CODE_OF_DESIGN.md`, which is where they are argued rather than asserted.

Large architectural changes should be proposed before implementation — see
`system/workflow.md` for what that means procedurally.
