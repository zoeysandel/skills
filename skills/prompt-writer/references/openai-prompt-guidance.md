# OpenAI Prompt Guidance Reference

Use this reference as a compact working summary. When the user asks for current model behavior, parameters, pricing, limits, or feature availability, verify the official docs again before making claims.

Astra sections verified on 2026-09-05 against:
https://developers.openai.com/api/docs/guides/latest-model?model=gpt-6-astra

The surface-neutral sections below are retained workflow guidance, not a new
verification of Chat/Work features. Older GPT-5.6-specific defaults have been
removed from this current reference; fetch exact-model guidance when needed.

## Surface-Neutral Core

- A short prompt is often enough. For larger or important work, add only the useful parts: `Goal`, `Context`, `Output`, and `Boundaries`.
- Start with the result and audience. Describe the process only when the process itself matters.
- Add sources and context that can change the answer. Say what the model should take from each source.
- Use boundaries for real failure prevention: preserve approved values, do not guess missing evidence, stay inside budget or scope, and draft rather than send when review is required.
- Tell the model how the result will be used so it can choose the right length, detail, and organization.
- For important work, request a final check and keep human review before use or sharing.
- Refine with focused follow-ups rather than trying to make the first prompt exhaustive.

## Choose the Right Surface

- Use Chat for questions, ideas, rewrites, comparisons, and lightweight plans.
- Use Work for multi-source, multi-tool, longer-running, recurring, or file-producing tasks. Start with one reviewable result and separate required work from optional polish.
- Use Codex for code or developer-tool work. Name the desired behavior, relevant files or reproduction steps, preservation constraints, allowed edits, and verification.
- Use API prompt guidance when the prompt is part of a product contract and model/config choices affect behavior, latency, cost, state, or tool use.

## GPT-6 Astra: prompting adjustments

- Clarify when to proceed with reasonable assumptions and when missing input
  truly blocks the authorized outcome.
- Audit skill and AGENTS.md conflicts; Astra follows these closely.
- Specify concise, plain writing when detailed formatting is unwanted.
- Define useful delegation opportunities and bounded parallelism.
- Scope tests to meaningful risks; repeat or broaden only for new evidence.

Apply these adjustments to observed needs, not as a compulsory prompt block.
Preserve higher-priority instructions and actual authorization boundaries.

## Personality, Collaboration, and Length

- State required content and useful structure; avoid a blanket brevity rule that removes necessary evidence.
- Use `text.verbosity` for the default detail level. In prompt text, specify required structure, must-keep content, and what can be omitted.
- Separate personality from collaboration style. Personality controls tone and polish; collaboration controls questions, assumptions, initiative, tradeoffs, checks, and uncertainty.
- Define tone through observable writing choices. Avoid relying only on labels such as friendly or empathetic.
- For editing and rewriting, preserve facts, claims, artifact type, length, structure, and genre before improving clarity or flow.
- Avoid blanket language-switching rules unless they are a real product requirement.

## Autonomy and Approval Boundaries

- For answer, explain, review, diagnose, or plan requests, inspect relevant materials and report; do not implement unless the request also asks for change.
- For change, build, or fix requests, allow in-scope local edits and non-destructive validation without unnecessary approval pauses.
- Require confirmation for external writes, destructive actions, purchases, or material scope expansion.
- Name safe local actions and keep the policy in one place. Repeating approval warnings can block safe expected work.
- For long-running tasks, state the current layer: research, design, implementation, review, or external coordination.

## Tools, Grounding, and State

- Expose only relevant tools. Tool descriptions should say what the tool does, when to use it, important return fields, and error behavior.
- Resolve prerequisite retrieval and validation before acting. Parallelize independent reads; keep dependent choices sequential.
- Treat empty or narrow retrieval as uncertain. Try one or two meaningful fallbacks before concluding no evidence exists.
- For grounded answers, define what needs support, cite only retrieved sources, attach citations to the supported claim, label inference, and report source conflicts.
- Use short visible preambles and sparse outcome-based updates for multi-step work. Preserve assistant phase values when replaying history.
- Use persisted reasoning only while objectives and assumptions remain stable. Stale reasoning can anchor later turns incorrectly.
- Keep cacheable prompt prefixes stable. Use explicit cache breakpoints only when measurement shows a real benefit.

## Programmatic Tool Calling

- Use Programmatic Tool Calling for bounded, deterministic reduction of large structured results: filtering, joining, ranking, deduplication, aggregation, batching, or repeated validation.
- Prefer direct calls when one call is enough, intermediate results are small, each result changes the next decision, approval is required, citations or native artifacts must be preserved, or semantic judgment belongs between calls.
- When both routes exist, define the bounded stage, eligible tools, output schema, evidence, retry limit, stop condition, one handoff, and work that must remain direct.
- Test both `program_output` and the final assistant message. A correct program result can still become an incomplete final answer.

## GPT-6 Astra: API compatibility

- Target ID: `gpt-6-astra`. Preserve effort except `none`/`minimal`: start at `low`.
- Tool calling requires Responses, although Chat Completions supports non-tool use.
- Remove `temperature`, `top_p`, `top_logprobs`; remove Chat Completions
  `logprobs` and Responses `message.output_text.logprobs` includes.
- EU residency does not support Astra fast/priority processing.
- Async tools, mid-turn steering, and `configuration_update` need host support;
  they are not prompt instructions or Codex config keys.
- From GPT-5.5 or earlier, review the documented cache-retention migration.

For implementation, fetch the linked feature schemas and compatibility limits.
Do not introduce optional capabilities or change application code during a
prompt-only assignment. Keep API request fields separate from Codex settings.

## Visual and Coding Work

- Provide product context, preserve the existing design system, name required states, and prevent unsolicited features or decoration.
- Render and inspect visual output for clipping, spacing, missing content, responsive behavior, and consistency.
- For code, run targeted tests, type or lint checks, affected builds, and a minimal smoke test when possible. If a check cannot run, say why and name the next best check.

## Prompt Migration Workflow

1. Preserve the current prompt, model behavior, and effective reasoning as a baseline.
2. Use the exact requested target and compatible runtime parameters without adopting optional features automatically.
3. Run representative evals before rewriting the prompt.
4. Remove obsolete scaffolding, repeated instructions, contradictions, and irrelevant tools one group at a time.
5. Add only the smallest targeted instruction or config change that fixes a measured regression.
6. Re-run the same evals after each change so prompt, model, tool, and runtime effects remain distinguishable.

## Common Anti-Patterns

- Rewriting a working prompt stack all at once.
- Repeating the same rule in several sections.
- Prescribing step-by-step reasoning when only the outcome and guardrails matter.
- Using broad absolutes for judgment calls.
- Repeating approval language until safe local work stalls.
- Adding generic `be brief`, `be thorough`, or `think step by step` instructions without an evaluated need.
- Treating missing evidence as a factual no.
- Prompting a JSON schema in prose when structured outputs are available.
- Enabling Pro, `max`, persisted reasoning, explicit caching, Programmatic Tool Calling, or multi-agent behavior merely because a model supports it.
