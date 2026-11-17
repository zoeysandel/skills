# Agent skills

Reusable instructions for Codex and Claude Code. Each skill lives in its own directory with a `SKILL.md` and any supporting files. Copy the full directory when installing a skill manually.

| Path | Skills | Where they work |
| --- | --- | --- |
| [`shared/development-workflows/skills/`](shared/development-workflows/skills/) | [Prepare Development](shared/development-workflows/skills/prepare-development/), [Create Subagents](shared/development-workflows/skills/create-subagents/), [Team Up](shared/development-workflows/skills/team-up/) | Codex and Claude Code. Delegation and independent review depend on the tools and permissions the host provides. |
| [`shared/design-workflows/skills/`](shared/design-workflows/skills/) | [Design Direct](shared/design-workflows/skills/design-direct/), [Design Critic](shared/design-workflows/skills/design-critic/) | Optional in Codex and Claude Code. Editable designs require an available editor such as Paper. Independent critique requires image access and authorized delegation. |
| [`codex/skills/`](codex/skills/) | [Clean Code Standard](codex/skills/clean-code-standard/), [Manage Chat Status](codex/skills/manage-chat-status/), [Prompt Writer](codex/skills/prompt-writer/) | Codex. Manage Chat Status also requires the Codex desktop chat tools and a locally adopted [sidebar policy](codex/rules/codex-sidebar.md). Prompt Writer includes OpenAI model and Codex guidance. |
| [`claude-code/skills/`](claude-code/skills/) | [Prompt Writer for Claude](claude-code/skills/prompt-writer-claude/) | Claude Code, with Anthropic model and API guidance. |
| [`archive/`](archive/) | Continue, Intent Check, Loop Creator, Shadow Run and the example template | Historical reference and template only. |

Use **Prepare Development** for substantial changes. Establish the purpose,
process, architecture, relevant data model, stack and acceptance evidence
before building. For a small fix, clarify the affected scenario and verify it
with a proportionate check. **Create Subagents** defines a bounded assignment.
**Team Up** integrates contributions and obtains an independent final review.

Use **Design Direct** to agree on a visual direction and simplify the user flow
before elaborating screens. Use **Design Critic** to review current renders
against the agreed direction, using its included brief for an independent critic
when supported.

## Codex

Clone the repository, then copy each desired directory from the shared package skill directories or `codex/skills/` into your Codex user skills directory, usually `~/.codex/skills/` or `$CODEX_HOME/skills/` when customized. Compare or back up any installed skill with the same name first. From the
repository root:

```sh
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R shared/development-workflows/skills/prepare-development "${CODEX_HOME:-$HOME/.codex}/skills/"
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

### Optional design package

With the `skills` marketplace added, install:

```sh
claude plugin install design-workflows@skills
```

Start a fresh session and invoke `/design-workflows:design-direct` or
`/design-workflows:design-critic`. To update, run
`claude plugin marketplace update skills` followed by
`claude plugin update design-workflows@skills`.

## Maintaining this repository

[AGENTS.md](AGENTS.md) explains what belongs in each directory, the privacy rules and what to verify before publishing. [CLAUDE.md](CLAUDE.md) loads the same rules in Claude Code.
