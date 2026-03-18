# skills

This is my public collection of **agent skills**: reusable instructions (and sometimes scripts/resources) that help an AI agent perform specialized tasks more reliably.

Skills are meant to be **portable**. You can use them with different agent runtimes and tools (for example Cursor, Codex, Claude Code, etc.) by pointing your agent at the relevant `skills/<skill-id>/` folder.

## What’s a skill?

A skill is a self-contained folder with a `SKILL.md` file that includes:

- **YAML frontmatter**: metadata like `name` and `description`
- **Instructions**: the behavior, constraints, and workflow the agent should follow when the skill is active

## Repo structure

- `skills/<skill-id>/SKILL.md`: one folder per skill, following the `SKILL.md` convention