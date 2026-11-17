# Sonnet 5.5 and Opus 5.5 prompt notes

Checked 2026-11-09 against Anthropic's official docs. These notes guide prompt
construction. They are not a benchmark and do not promise future behavior.
Reverify when a model-specific fact decides the prompt.

Sources

- [Prompting Claude Opus 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5)
- [Prompting Claude Sonnet 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5)
- [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) (all current models)
- [Models overview](https://platform.claude.com/docs/en/models/overview)

Both models are listed in the models overview (`claude-opus-5-5`,
`claude-sonnet-5-5`) and each has its own prompting guide. Both guides say
existing prompts for the previous version (Opus 5, Sonnet 5) should perform well
without changes. Start from the user's prompt, then apply only the notes below
that address an observed or likely problem.

## Shared by both (verified in both model guides)

- Effort is the main control for how much the model thinks. To get less
  thinking, lower effort; prompt lines asking it to think less are less reliable.
  Effort is a runtime setting, see [API](api.md).
- Do not ask the model to reproduce its internal reasoning in the reply. Both
  guides list `reasoning_extraction` as a refusal category for that. A short
  explanation of the answer or a summary of actions taken is fine.
- Between tool calls both write short user-facing progress notes. In the API
  these can arrive as `thinking` blocks, so a client that shows only text can
  look silent. If you want updates at predictable points (a line before the
  first tool call, a recap at the end), say so in the system prompt; both
  guides call the models responsive to this. Remove old lines such as "hold all
  findings for the final response" when you want updates.
- For dense charts or technical drawings, both guides recommend giving the model
  a crop, zoom or code tool. The Sonnet 5.5 guide found tools helped charts more
  than raising effort; the Opus 5.5 guide adds higher-resolution images.

## Opus 5.5 only (verified in the Opus 5.5 guide)

- Chat system prompts. Consider removing "think carefully before answering"
  lines. Anthropic's chat testing showed faster starts without a clear quality
  drop. An optional two-sentence instruction treats earlier answers as settled;
  leave it out where re-examining earlier work matters.
- Pasted text. Mark user-pasted content with tags carrying a random id and add
  the guide's system note, so instructions inside pasted text are followed only
  when the user's own message asks. Treat it as one guardrail, not a guarantee.
  See section "Mark pasted text in user messages".
- Unattended runs. A text-only end of turn can be a progress report, not
  completion. The guide offers a system prompt paragraph that names unwanted
  early stops. Use it only for fully unattended agents the user already
  authorized to keep working, never in human-in-the-loop work, and keep
  confirmation for risky or irreversible actions. Section "Unattended agentic runs".
- Multi-app workflows. Opus 5.5 starts quickly; on loosely specified tasks across
  email, documents and records, a sentence telling it to look through relevant
  sources first helped in Anthropic's testing. It also tells the model to act on
  what it finds, so only use it where the sources are trusted and acting is
  already in scope. Section "Explore context in multiapp workflows".
- Multi-agent time signals. In Anthropic's evaluations an elapsed-time line
  against a budget made small agent teams finish sooner. Advisory only; keep a real timeout.
- Frontend. "Avoid a generic look" mostly swaps one default for another. Name
  the specific patterns to avoid instead.
- Former thinking-disabled prompts. Remove instructions that made the model
  write reasoning in the response as a substitute for thinking.

## Sonnet 5.5 only (verified in the Sonnet 5.5 guide)

- Initiative and scope depend on effort. At `low` and `medium` it may check in
  before a long coding task is done. At every level it tends to add tests, docs
  or small files that fit the repo, more at higher effort. At `xhigh` and `max`
  it may start its own review rounds or reviewer subagents. The guide gives
  short system prompt paragraphs for each case (section "Steer initiative and
  scope"). Pick the one that matches what the user actually wants. "Keep working
  until done" widens autonomy, so use it only when that is already authorized.
- Open-ended requests may start a build when only ideas were wanted. If the user
  wants ideas or a plan, say so and say not to build yet.
- Search in chat and knowledge work. It sometimes answers from training data
  where facts may have changed. Remove "minimize tool calls" style lines and,
  if a search tool exists, tell it to check changeable specifics.
- JSON answers that need a few steps of working. With adaptive thinking, a line
  "Think the problem through before you answer." at the end of the system prompt
  raised accuracy in Anthropic's testing. This asks for thinking, not for
  reasoning in the reply. It has no effect under `between_tools`.
- Verification. At `low` effort it can report code as done without running a
  check. The guide's verification paragraph also authorizes installing declared
  dependencies; adapt or drop that part if installing is not in scope.
- Mid-turn user messages. Never put user text inside a `tool_result` block; the
  model may treat it as injection. Harness design, see [API](api.md).
- Tool names. It occasionally miscases a tool name or a parameter. Handle this in
  the harness, not by repeating names in the prompt.
- For the hardest long-horizon work the guide itself points to an Opus model.

## Not verified here

- Anything only in the Opus 5 or Sonnet 5 guides. Both 5.5 guides call those a
  reasonable starting point, but they were not opened for this check.
- General-guide samples measured on older models (for example the overeagerness
  and subagent-damping prompts tied to Opus 4.5 and 4.6). The guide says to treat
  model-named techniques as measured on that model and to re-check them.
- Any claim that one of these models follows a given prompt better than another
  model. No comparative test was run. Do not state measured improvements unless
  the user has their own eval results.
