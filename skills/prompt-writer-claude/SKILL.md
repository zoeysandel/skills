---
name: prompt-writer-claude
description: Write, rewrite or critique prompts for Claude Sonnet 5.5 and Claude Opus 5.5, including system prompts, subagent and agent handoffs, research or review assignments, and tool descriptions. Use when a prompt for a Claude model has to be drafted or improved and the intent, facts, scope, permissions, writing preferences, completion bar and evidence must survive the rewrite. Grounded in Anthropic's official prompting guides, with model-specific notes kept apart from general principles, API settings and Claude Code host behavior.
---

# Prompt Writer for Claude

Turn a request into a prompt that a Claude model can act on without guessing.
Add only context and constraints that change the result. A short internal
handoff can stay short; no template, phase list or reasoning script is required.

## Core

- State the outcome first, then the context that explains why it matters.
  Anthropic's guidance is that Claude generalizes from a stated reason better
  than from a bare rule, and that a colleague without context should be able to
  follow the prompt.
- Preserve what the user gave you. Keep their facts, numbers, names, paths,
  dates, requested artifact, audience, tone, language and writing preferences
  exactly. Keep an explicitly named model or effort. Infer safe, reversible
  details; ask only when a gap changes the result or the authority. Never turn
  your own assumption into a requirement or add claims the source lacks.
- Carry permissions over unchanged. Say once what the agent may do, what needs
  confirmation and when to stop. Do not widen authority (pushing, sending,
  deleting, installing, spending) and do not invent new approval steps the user
  did not ask for. Read-only stays read-only.
- Be explicit about action versus advice. "Suggest changes" gets suggestions,
  "change this" gets edits. Pick the wording that matches the user's intent.
- Define done. Name the deliverable, its location and shape, and the evidence
  that shows it is finished (tests run, sources cited, files listed). Ask for
  open items and unverified parts to be reported instead of glossed over.
- Ask for a short explanation, a summary of actions or cited evidence when
  useful. Never ask the model to write out its hidden reasoning in the reply;
  on both 5.5 models that can trigger a `reasoning_extraction` refusal
  (see [models](references/models.md)).
- Prefer decision criteria to blanket absolutes, and say what to do rather than
  only what to avoid. Keep an example or a repeated check only when it protects
  a real requirement. Use XML tags to separate instructions, context, examples
  and pasted inputs when a prompt mixes them.
- Separate prompt text from runtime settings. Do not invent model support,
  defaults, pricing or performance gains. A rewrite is a draft until it has been
  run; fewer lines is not evidence of improvement.

## By task

- Plain prompt or system prompt. Goal, audience, relevant context, output shape,
  real boundaries. Add a role sentence only if it changes behavior.
- Rewrite or critique. First list what must survive (facts, scope, permissions,
  deliverable, preferences). Then report which requirements were kept, moved,
  removed or changed and why. Distinguish a behavior-preserving cleanup from an
  intentional behavior change.
- Agent or subagent handoff. A non-fork Claude Code subagent starts without the
  conversation history, so its handoff must stand alone. Forks inherit history;
  include only the missing assignment context for those. Include the goal, what
  is already known or ruled out, files or sources to read, allowed actions and
  limits, the completion bar and what to send back. Restate any rule the
  subagent must follow that it would not otherwise load. See
  [Claude Code host notes](references/claude-code.md).
- Research or review handoff. Name the question that would change a decision,
  the material to inspect, what would support or weaken a conclusion, and how to
  label inference versus verified fact. Give the code or source, not your own
  conclusion, when you want an independent read.
- Tool description. Say what the tool does, when to use it and when not, what
  each parameter means, what it returns, its errors and limits. Anthropic calls
  detailed descriptions the most important factor for tool use and suggests at
  least 3 to 4 sentences. Use `input_examples` for complex inputs, consolidate
  related actions and namespace names across services. Put routing between tools
  in the system prompt, not in each description.

## Read only what the task needs

- Targeting Sonnet 5.5 or Opus 5.5 specifically, or migrating a prompt to one
  of them. Read [models](references/models.md). It separates verified per-model
  guidance from inherited or uncertain claims, with source and check date.
- The prompt goes into an API request, or the advice touches effort, thinking,
  `max_tokens`, tools, structured output or caching. Read [API](references/api.md).
- The prompt runs inside Claude Code (skills, subagents, CLAUDE.md, model or
  effort settings). Read [Claude Code host notes](references/claude-code.md).
- A substantial refactor, a product or high-impact prompt, or a model
  migration. Read [validation](references/validation.md).

If the target model is not Sonnet 5.5 or Opus 5.5, say so and check that
model's own official guide instead of reusing these notes. If documentation
cannot be checked, label model and runtime claims as unverified.

## Delivery

Return the ready-to-use prompt in a fenced block; an internal handoff can go
straight to its agent. Then add only what helps. Meaningful changes and why,
runtime advice kept separate from prompt text, and any missing evidence. Say
plainly whether the prompt was only written and reviewed, or actually run.
