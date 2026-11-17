# Claude Code host notes

How Claude Code wraps the model. This is host behavior, separate from model
guidance and API settings. Checked 2026-11-09.

Sources

- [Model configuration](https://code.claude.com/docs/en/model-config)
- [Subagents](https://code.claude.com/docs/en/sub-agents), section "What loads at startup"
- [Skills](https://code.claude.com/docs/en/skills)

## Models and effort in Claude Code

- Claude Code defaults Opus 5.5 and Sonnet 5.5 to `medium` effort. The Claude
  API default for Sonnet 5.5 is `high`, so the same prompt can behave
  differently in Claude Code and in a direct API call.
- Aliases are provider-dependent. On the Anthropic API, `sonnet` and `opus`
  resolve to Sonnet 5.5 and Opus 5.5. On Bedrock and Google Cloud's Agent
  Platform `sonnet` resolves to Sonnet 4.5, and on Claude Platform on AWS to
  Sonnet 4.6. If the target must be Sonnet 5.5, name it, do not rely on the alias.
- Minimum versions. Opus 5.5 needs Claude Code v2.1.280, Sonnet 5.5 v2.1.284.
- Organizations can cap effort or restrict models. Do not promise a level the
  user's setup may not allow; do not change model or effort settings as part of
  a prompt-only task.

## Subagent handoffs

- A non-fork subagent starts with a fresh context. It gets its own system
  prompt, the delegation message, CLAUDE.md files (not for Explore, Plan or
  `omitClaudeMd` agents) and a git status snapshot. It does not see the
  conversation, earlier tool results or skills already invoked.
- So the delegation message must carry the goal, relevant facts and paths,
  limits and permissions, the completion bar and the expected return format.
  Restate any rule from the conversation that the subagent needs.
- A fork inherits the parent conversation and needs less restating.
- The subagent `description` field decides when Claude delegates to it; write it
  as a clear trigger, like a skill description.

## Skills

- `description` (plus optional `when_to_use`) is what Claude sees when deciding
  to load a skill; the combined text is cut at 1,536 characters in the listing.
  Put the key use case first.
- Once invoked, the skill body stays in the conversation and is not re-read, so
  write standing instructions rather than one-time steps.
- Keep `SKILL.md` under 500 lines and move detail into referenced files.
- `allowed-tools` grants last only for the invoking turn; do not use a skill
  prompt to imply permissions the host has not granted.
