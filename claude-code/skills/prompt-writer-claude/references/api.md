# API configuration for Sonnet 5.5 and Opus 5.5

Runtime settings, not prompt text. Checked 2026-11-09. Recommend a setting only
when it addresses the task, and fetch the exact schema before implementing.

Sources

- [Claude Opus 5.5 migration guide](https://platform.claude.com/docs/en/models/opus-5-5/migration-guide), section "What every request to Claude Opus 5.5 must satisfy"
- [Claude Sonnet 5.5 migration guide](https://platform.claude.com/docs/en/models/sonnet-5-5/migration-guide)
- [Models overview](https://platform.claude.com/docs/en/models/overview)
- [Effort](https://platform.claude.com/docs/en/build-with-claude/effort)
- [Define tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools)
- The two model prompting guides listed in [models](models.md)

## Facts per model

| | Opus 5.5 | Sonnet 5.5 |
| --- | --- | --- |
| API ID | `claude-opus-5-5` | `claude-sonnet-5-5` |
| Thinking | adaptive, always on; `disabled` and `budget_tokens` rejected | adaptive by default; `between_tools` turns off up-front thinking; `disabled` and `budget_tokens` rejected |
| API default effort | `medium` | `high` |
| Effort levels | `low` `medium` `high` `xhigh` `max` | same |
| Context window, max output | 1M, 128K | 1M, 128K |

Rejected on both (400 error). `temperature`, `top_p`, `top_k`, a prefilled final
assistant turn, and forced `tool_choice` (`any` or a named tool). So steer with
prompt text, structured outputs or system prompt instructions, not sampling or
prefill, and do not write tool advice that relies on forcing a tool.

## Effort

- Set effort explicitly and sweep levels on your own evals; level names do not
  mean the same thinking across models.
- Opus 5.5 guide. Start at `medium`; reserve `xhigh` and `max` for measured gains.
- Sonnet 5.5 guide. Start at `high` in general; for agentic coding start at
  `medium` for well-specified tasks; for chat or latency-sensitive work start at
  `medium` or `low`.
- Changing top-level effort between requests invalidates the prompt cache. A
  per-message effort change (beta) keeps it. On Sonnet 5.5 that needs adaptive
  thinking, not `between_tools`.
- `between_tools` on Sonnet 5.5 is accepted only at `high` or below and takes no
  other thinking fields. Without tools it means no thinking before answering.

## Output and blocks

- Thinking counts toward `max_tokens`. For long agentic coding turns both guides
  suggest 128,000 (the maximum); the Sonnet 5.5 guide adds streaming.
- Read responses by block type; the first block may be `thinking`, empty under
  the default `display: "omitted"`.
- Progress notes between tool calls come back as `thinking` blocks;
  `display: "updates"` (beta) returns their summaries. Declare any "message the
  user" tool in the first request so `tools` does not change mid-session.
- For JSON on reasoning tasks prefer structured outputs. Treat
  `stop_reason: "max_tokens"` as failed even if the JSON parses.

## Tools

- Detailed descriptions matter most. Cover what the tool does, when and when
  not to use it, each parameter, returns and caveats, in at least 3 to 4 sentences.
- Use `input_examples` for complex or format-sensitive inputs.
- Consolidate related operations behind an `action` parameter and namespace tool
  names across services.
- Harness tolerance (Sonnet 5.5 guide). Accept unambiguous miscased tool names,
  or return `is_error: true` naming the exact expected name.
- Never place user text inside `tool_result`; append it as user text after the
  last `tool_result`, and keep harness notices in a separate system message.

## History and caching

Keep conversation history append-only and pass thinking blocks back unchanged.
Editing earlier messages or rebuilding `system` or `tools` mid-session
invalidates later thinking blocks (general guide, migration considerations).
Put stable instructions first and add anything that must change mid-session as
a mid-conversation system message.
