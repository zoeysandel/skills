# GPT-6 Astra Prompt and Compatibility Notes

Dated guidance is context, not proof of current support. Read these notes only
for an exact GPT-6 Astra target. Use `$openai-docs` to verify relevant current
support before making runtime claims; do not apply these settings to other models.

## GPT-6 Astra: dated prompting notes

Verified on 2026-09-05 against:
https://developers.openai.com/api/docs/guides/latest-model?model=gpt-6-astra

These notes are not a fresh verification:

- Clarify when reasonable assumptions permit progress and when missing input
  blocks the authorized outcome.
- Audit actual skill and AGENTS.md conflicts when they affect the request.
- Specify observable writing choices when the default style is unsuitable.
- Define useful delegation opportunities and bounded parallelism when relevant.
- Scope tests to meaningful risks; repeat or broaden for new evidence.

Apply these only to observed needs, not as a compulsory prompt block.
Preserve higher-priority instructions and authorization boundaries.

## Migration

Keep the current prompt, model, and effective effort as a baseline. Use
[validation](validation.md) for behavioral comparison and [API prompts](api-prompts.md)
for runtime changes. When comparisons cannot run, report a proposed migration,
not demonstrated equivalence or improvement.

## Dated API compatibility notes

These also came from official guidance checked on 2026-09-05, not a fresh
support check. Reverify exact feature schemas before implementation.

- Target ID: `gpt-6-astra`. Preserve effort except `none`/`minimal`: start at `low`.
- Tool calling requires Responses; Chat Completions supports non-tool use.
- Remove `temperature`, `top_p`, `top_logprobs`; remove Chat Completions
  `logprobs` and Responses `message.output_text.logprobs` includes.
- EU residency does not support Astra fast/priority processing.
- Async tools, mid-turn steering, and `configuration_update` need host support;
  they are not prose instructions or Codex config keys.
- From GPT-5.5 or earlier, review documented cache-retention migration.
