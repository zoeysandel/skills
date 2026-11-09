# GPT-6.1 Sol and GPT-6 Astra Prompt Notes

Checked 2026-11-09. These notes guide prompt construction; they are not a
benchmark, account-availability check, or guarantee of future runtime support.

## Exact model and source

- [GPT-6.1 Sol model page](https://developers.openai.com/api/docs/models/gpt-6.1-sol)
  directs prompting questions to the shared GPT-6 guide. No separate Sol-specific
  prompt guide was established in this check.
- [GPT-6 prompting best practices](https://developers.openai.com/api/docs/guides/latest-model#prompting-best-practices)
  offers a family starting point based on Astra observations. Test transfer to
  Sol on the actual workload; do not present Astra tendencies as measured Sol behavior.
- [Rethinking skills and prompts for GPT-6 Astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra)
  informs the instruction-maintenance advice below.

## Shared starting point; Astra observations

Use only guidance that addresses the assignment:

- Define the completed outcome and which routine assumptions allow progress.
  Keep necessary user decisions distinct from work already authorized.
- Inspect relevant instruction conflicts when they explain unexpected pauses;
  distinguish an actual rule from the agent's interpretation.
- Specify concrete writing preferences when defaults are unsuitable.
- Set delegation boundaries only for workflows that permit delegation.
- Match verification to the change; extend it for new failures or uncertainty.

Astra's documented tendencies include extra clarification, sensitivity to skill
instructions, detailed formatting, limited delegation, and extensive testing.
They are reasons to tune a prompt when needed, not mandatory boilerplate.

## Maintaining reusable instructions

Keep specialized guidance focused. Route to references by task rather than
requiring a stack of documents before every edit. Revisit old restrictions and
repeated checks; retain those that protect real requirements. Instructions used
by several models need validation across those targets. Removing text alone
does not demonstrate better behavior.

## Runtime and validation boundary

Preserve the explicit target: `gpt-6.1-sol` or `gpt-6-astra`. API support is not
proof of a setting in Codex. Keep configuration separate from prompt text.
Replace the former September API compatibility list with a fresh exact-feature
check when implementing; use [API prompts](api-prompts.md).

Keep the original prompt and effective settings as the baseline. Compare
representative outcomes using [validation](validation.md). This update was
source-checked and statically validated; no downstream Sol/Astra benchmark was run.
