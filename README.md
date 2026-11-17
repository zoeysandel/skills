# Agent skills

Reusable instructions for Codex and Claude Code. Each skill lives in its own directory with a `SKILL.md` and any supporting files. Copy the full directory when installing a skill manually.

| Path | Skills | Where they work |
| --- | --- | --- |
| [`shared/skills/`](shared/skills/) | [Prepare Development](shared/skills/prepare-development/), [Create Subagents](shared/skills/create-subagents/), [Team Up](shared/skills/team-up/) | Codex and Claude Code. Delegation and independent review depend on the tools and permissions the host provides. |
| [`codex/skills/`](codex/skills/) | [Clean Code Standard](codex/skills/clean-code-standard/), [Manage Chat Status](codex/skills/manage-chat-status/), [Prompt Writer](codex/skills/prompt-writer/) | Codex. Manage Chat Status also requires the Codex desktop chat tools and a locally adopted [sidebar policy](codex/rules/codex-sidebar.md). Prompt Writer includes OpenAI model and Codex guidance. |
| [`claude-code/skills/`](claude-code/skills/) | [Prompt Writer for Claude](claude-code/skills/prompt-writer-claude/) | Claude Code, with Anthropic model and API guidance. |
| [`archive/`](archive/) | Continue, Intent Check, Loop Creator, Shadow Run and the example template | Historical reference and template only. |

## Codex

Clone the repository, then copy each desired directory from `shared/skills/` or `codex/skills/` into your Codex user skills directory, usually `~/.codex/skills/` or `$CODEX_HOME/skills/` when customized. For example, from the repository root:

```sh
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R shared/skills/prepare-development "${CODEX_HOME:-$HOME/.codex}/skills/"
```

Start a fresh Codex session and invoke the skill with its name, such as `$prepare-development`. For Manage Chat Status, review and merge the sidebar policy into the active user-level `AGENTS.md` before use. Review any cleanup authorization in that policy for the account where it will run.

To update, pull the repository and replace the complete installed skill directory with the new version. Compare or back up local customizations first. Reconcile the sidebar policy separately if you adopted it.

## Claude Code

Install the development workflows from the `skills` marketplace:

```sh
claude plugin marketplace add zoeysandel/skills
claude plugin install development-workflows@skills
```

In a fresh Claude Code session, use `/development-workflows:prepare-development`, `/development-workflows:create-subagents` or `/development-workflows:team-up`. The plugin contains these three skills and no hooks, executables or MCP servers.

To update:

```sh
claude plugin marketplace update skills
claude plugin update development-workflows@skills
```

Restart Claude Code to load an update. To install Prompt Writer for Claude, copy `claude-code/skills/prompt-writer-claude/` into `~/.claude/skills/` and use `/prompt-writer-claude`. Update that directory manually after pulling changes.

If you previously installed `development-workflows@agent-workflows`, verify the three skills are present under `development-workflows@skills` before removing the old marketplace with `claude plugin marketplace remove agent-workflows`.

## Maintaining this repository

[AGENTS.md](AGENTS.md) explains what belongs in each directory, the privacy rules and what to verify before publishing. [CLAUDE.md](CLAUDE.md) loads the same rules in Claude Code.
