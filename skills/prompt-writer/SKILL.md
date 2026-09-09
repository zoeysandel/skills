---
name: prompt-writer
description: Write, rewrite, migrate, or critique prompts, system/developer instructions, agent prompts, and tool descriptions for Chat, Work, Codex, or OpenAI APIs. Use for prompt improvement, model migration, model-aware tuning, eval-ready variants, and current OpenAI prompting guidance.
---

# Prompt Writer

## Overview

Create prompts that are outcome-first, compact, testable, and matched to the target surface and model. Define the result, relevant context, hard boundaries, evidence rules, completion bar, and output shape without prescribing reasoning steps the model can choose itself.

Read `references/openai-prompt-guidance.md` when the request depends on current ChatGPT, Work, or Codex prompting guidance; target-model behavior or migration (including GPT-6 Astra); reasoning effort or Pro mode; response length; tool routing; Programmatic Tool Calling; persisted reasoning; prompt caching; grounded research; long-running workflows; or visual work.

## Workflow

1. Identify the target.
   - Name the surface: Chat, Work, Codex app/IDE/CLI/cloud, Responses API, Chat Completions, or an embedded assistant.
   - Infer the target model from the request, repo config, API call, prompt file, or runtime. Preserve an explicitly named target.
   - If the model is unknown, write for "the configured model" and mark model-specific assumptions as `UNCONFIRMED`.
   - If the user asks for best, latest, current, migration, or OpenAI-docs-based guidance, verify official guidance for the exact target. Use $openai-docs when available; otherwise search and read the relevant official pages on developers.openai.com, platform.openai.com, or learn.chatgpt.com directly. If retrieval is unavailable, disclose that limit. Cached references are dated notes, not proof of current support.
   - For Astra, read the Astra sections of the reference. Keep other explicitly requested models intact; never apply Astra parameters universally.

2. Capture the task contract.
   - Goal and success criteria: what must be true when the work is complete.
   - Context and sources: what information can change the answer and which user-provided values must be preserved.
   - Audience and deliverable: who will use the result, where, and in what format.
   - Boundaries and autonomy: safe local actions, approval-gated actions, side effects, and scope limits.
   - Evidence and quality: correctness, citations, tone, speed, cost, determinism, or visual fidelity.
   - Ambiguity and stop rules: when to infer, ask, retry, fall back, abstain, or finish.

3. Choose the smallest useful structure.
   - For Chat: `Goal` + relevant `Context` + `Output` + real `Boundaries`.
   - For Work: `Goal` + `Sources` + `Deliverable` + `Review/approval` + `Verification`.
   - For tool-using agents: `Objective` + `Context` + `Tool rules` + `Autonomy` + `Evidence` + `Updates` + `Verification` + `Stop rules`.
   - For extraction or classification: `Goal` + `Definitions` + `Decision rules` + `Examples` + `Output schema` + `Ambiguity handling`.
   - For coding agents: `Goal` + `Relevant code or repro` + `Preservation constraints` + `Allowed changes` + `Validation` + `Final response`.
   - For customer-facing or collaborative products, keep `Personality` separate from `Collaboration style`.

4. Make the prompt lean and model-aware.
   - Lead with the outcome and completion bar.
   - State each instruction once. Remove repeated rules, examples, style scaffolding, and irrelevant tools unless they protect a product requirement or measured failure.
   - Use absolute language only for true invariants. Use decision rules for judgment calls such as when to search, ask, use a tool, or keep iterating.
   - Preserve explicit user values. When a value is implicit, provide decision criteria instead of universal defaults or keyword maps.
   - Tell the model which important ambiguity must trigger a question; do not require questions for safe, reversible, in-scope work.
   - Put stable reusable instructions before dynamic case-specific context when caching matters.

5. Define tools, state, and side effects only when relevant.
   - Expose only task-relevant tools. Put return fields, types, and error behavior in tool descriptions.
   - Require prerequisite retrieval or validation when correctness depends on it.
   - Parallelize independent reads; keep dependent decisions sequential; synthesize before acting.
   - For empty, partial, or suspiciously narrow results, define one or two meaningful fallbacks before concluding no evidence exists.
   - Use Programmatic Tool Calling only for bounded deterministic reduction of large structured results. Keep approval, semantic judgment, citations, native artifacts, and final validation in direct model calls.
   - For long-running work, define the current layer, a short opening update, sparse phase updates, verification, and a terminal stop condition.
   - Recommend persisted reasoning or explicit caching only when the host supports it and the workload benefits measurably.

6. Tune API configuration separately from prompt text.
   - Use structured outputs for schemas instead of long schema prose when possible.
   - Read the reference and verify target-specific support before suggesting reasoning, Pro mode, verbosity, persisted reasoning, caching, Programmatic Tool Calling, or multi-agent settings.
   - Preserve the current model and effort as a migration baseline; use a supported equivalent when the target rejects that effort. Keep prompt and runtime changes distinguishable.
   - Treat optional API capabilities as runtime features, not prose instructions or defaults to add merely because the model supports them.

7. Add verification proportional to the failure cost.
   - Ask for checks that can catch meaningful failures: unsupported claims, wrong format, unsafe side effects, skipped prerequisites, missing acceptance criteria, broken code, or visual defects.
   - For important work, include a concise final check and preserve human review before use or sharing.
   - For high-impact or product prompts, include 2-5 representative test cases or an eval checklist.
   - For model migration, compare the old baseline with the requested target using the same prompt and compatible effective effort before making surgical prompt changes; if runtime comparison is unavailable, report that limit rather than claiming behavioral validation.
   - Ask for concise rationale, evidence, assumptions, or checks when needed. Never ask for hidden chain-of-thought.

8. Return usable artifacts.
   - Put the final prompt in a fenced code block.
   - Include only relevant config suggestions.
   - For rewrites or migrations, list meaningful prompt and config changes separately.
   - Label uncertain model or runtime choices `UNCONFIRMED` and name the missing evidence.

## Output Patterns

### Prompt Draft

```markdown
## Prompt

[Ready-to-use prompt text]

## Config Suggestions

- surface: [Chat|Work|Codex|Responses API|Chat Completions, if relevant]
- model: [target model or configured model]
- reasoning.effort: [verified supported value for the exact target, if relevant]
- reasoning.mode: [only if verified for the target and host]
- reasoning.context: [only if verified for the target and host]
- text.verbosity: [low|medium|high, if relevant]
- structured outputs: [yes/no, if relevant]
- tool calling: [direct|programmatic|mixed, if relevant]

## Why This Works

[3-5 bullets, only if useful]
```

### Prompt Critique

```markdown
## Main Issues

- [Highest-impact issue first]

## Rewritten Prompt

[Improved prompt]

## Changes Made

- [Meaningful prompt and config changes only]

## Test Cases

- [Input] -> [Expected behavior]
```

### Prompt Migration

```markdown
## Baseline

[Current model, prompt, config, and measured behavior]

## Migrated Prompt

[Smallest behavior-preserving prompt change]

## Config Changes

- [Model/runtime changes kept separate from prompt text]

## Eval Plan

- [Representative comparison and pass criteria]

## Unconfirmed

- [Missing runtime or model evidence]
```

### Prompt Variants

Return variants only when they help a real decision:

- `lean`: smallest prompt likely to pass the eval.
- `strict`: adds validation, hard constraints, and edge-case handling.
- `agentic`: adds tool routing, autonomy boundaries, progress updates, verification, and stop rules.

## Quality Rules

- Prefer outcomes and decision rules over long procedure stacks.
- Preserve user-provided facts, values, artifact shape, and requested tone before polishing.
- Keep personality, collaboration behavior, and task instructions distinct.
- Define tone through observable writing choices, not broad labels alone.
- Make side effects explicit: local and reversible, approval-gated, external, destructive, costly, or scope-expanding.
- Define how to handle missing context, conflicting evidence, and uncertainty.
- Put task-specific tool behavior in tool descriptions and global routing policy in the prompt.
- Keep examples realistic and only when they improve precision or encode a requirement.
- Never invent model capabilities, parameter defaults, pricing, or feature availability. Verify current official OpenAI docs when those details matter.
