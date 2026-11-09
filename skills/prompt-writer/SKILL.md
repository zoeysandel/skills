---
name: prompt-writer
description: Write or improve prompts, agent instructions, and tool descriptions. Use for drafting, critique, migration, and substantive investigation or review handoffs where the question, context, evidence, or authority needs to be made precise.
---

# Prompt Writer

Create a usable, outcome-first prompt with only the context and constraints that
change the result. For an ordinary prompt or subagent handoff, this core is enough.

## Core

- Define the desired result, relevant context and sources, scope and authority,
  evidence needed, completion bar, and useful output shape. Omit parts that do
  not help the task; no fixed template or reasoning sequence is required.
- Preserve the user's facts, values, requested artifact, tone, and explicit model.
  Infer safe, reversible details; ask when missing information materially changes
  the intended result or authority. Do not turn assumptions into requirements.
  Do not add claims or external effects that the source does not establish.
- State real boundaries once: allowed actions, approval-gated effects, and when
  to stop or escalate. For ongoing execution, retain the authorized objective
  until verified completion or a genuine boundary.
- Prefer decision criteria to broad absolutes. Keep examples, repeated checks,
  and procedural detail only when they protect a requirement or observed failure.
- Distinguish a behavior-preserving refactor from an intentional behavior change.
  For material edits, explain which important requirements were retained, moved,
  removed, or changed and why; fewer lines alone are not evidence of improvement.
- For tools, specify relevant prerequisites, meaningful failure handling, and
  evidence for consequential claims. Put field types and return behavior in
  tool descriptions; keep global routing in the prompt.
- Separate prompt text from runtime configuration. Do not invent capabilities,
  defaults, support, pricing, or model-performance claims. Preserve a configured
  model and effort unless the request calls for a verified change.
- Request concise rationale, evidence, or checks when useful, never hidden
  chain-of-thought. Match validation to failure cost; distinguish an untested
  draft from observed behavior.

## Connect purpose, investigation, and the assignment

Use the established purpose and boundaries from `understand-intent`, and the
selected questions and evidence needs from `investigate`, when available. Load
either skill only when installed and that part is unresolved; do not create a
compulsory chain of skill calls. If unavailable, establish the purpose, boundaries,
and evidence needs directly using the core above. Prompt writing should make a useful inquiry executable, rather
than substitute polished phrasing for missing domain knowledge.

For substantive investigation and review handoffs, specify what finding could
change the decision, which actual material to inspect, and what would support or
weaken a conclusion. If complementary questions can be delegated with existing
authority, give each assignment its distinct question and integration context.
Do not invent extra agents, requirements, user interests, or evidence.

Carry the user's intended result through the rewrite. If a stronger proposed
assignment changes an important tradeoff or scope, expose that change instead of
silently including it. A small internal instruction can remain small; there is
no requirement to rewrite every user message or create a separate prompt file.

## Conditional guidance

Read only the reference needed by the task:

- When current model behavior or runtime compatibility matters, verify the exact
  provider's official guidance; use `$openai-docs` for OpenAI facts when installed,
  otherwise use official provider documentation through available search tools.
  If documentation cannot be checked, label runtime claims unverified. Provider-neutral
  or offline prompt-only preparation does not require model documentation.
- GPT-6.1 Sol or GPT-6 Astra prompting:
  read the dated [OpenAI model notes](references/openai-prompt-guidance.md).
  Distinguish shared family advice from observations about one model; reverify
  current guidance when model-specific facts affect the assignment.
- API prompts, runtime parameters, tool/state design, or caching:
  read [API prompts](references/api-prompts.md).
- A deliverable needing a template or genuine alternative variants:
  read [output patterns](references/output-patterns.md).
- Substantial prompt refactors, product/high-impact prompts, behavioral testing,
  or a model migration:
  read [validation](references/validation.md).

## Delivery

Return ready-to-use prompt text, normally in a fenced block; an internal handoff
can go directly to its agent. Explain only meaningful changes. Keep any relevant
config advice separate, and name missing evidence without claiming a test ran.
