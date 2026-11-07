# skills

This is my public collection of **agent skills**: reusable instructions (and sometimes scripts/resources) that help an AI agent perform specialized tasks more reliably.

Skills are meant to be **portable**. You can use them with different agent runtimes and tools (for example Cursor, Codex, Claude Code, etc.) by pointing your agent at the relevant `skills/<skill-id>/` folder.

## What’s a skill?

A skill is a self-contained folder with a `SKILL.md` file that includes:

- **YAML frontmatter**: metadata like `name` and `description`
- **Instructions**: the behavior, constraints, and workflow the agent should follow when the skill is active

## Skill status

Compared with the owner's local skills on **2026-11-07**, at repository baseline
`754af6a`. This is a dated source comparison, not a runtime validation or an
ongoing synchronization guarantee. Local alternatives listed below are not yet
published here.

| Skill | Status | Finding / local alternative |
| --- | --- | --- |
| [Prompt Writer](skills/prompt-writer/) | Active; local sync pending | Still installed locally, but the published instructions differ materially. The local version uses a shorter core and separate API, output-pattern and validation references. |
| [Shadow Run](skills/shadow-run/) | Active | Local workflow and timebox script are aligned. The published edition adds portable setup, a bundled watchdog role and relative paths; delegation wording differs slightly. |
| [Continue](skills/continue/) | **Deprecated** | No longer installed locally. Continuation/completion behavior is covered by `follow-through` and active task instructions. |
| [Intent Check](skills/intent-check/) | **Deprecated** | No longer installed locally. Use `understand-intent` for alignment; ask for confirmation explicitly when wanted. |
| [Loop Creator](skills/loop-creator/) | **Deprecated** | No longer installed locally. Functional alternatives: `prepare-development` for preparation and `graph-engineering` for coordination; not a drop-in replacement. |
| [Example Skill](skills/example-skill/) | Template only | Not installed locally; retained as a starter template, not a maintained operational skill. |

Deprecated folders remain available for historical reference and existing links.
They are not recommended for new installations. Their original workflow text is
retained below a deprecation notice.

### Active skills

- [Prompt Writer](skills/prompt-writer/) — write and improve prompts and agent
  assignments. See the synchronization caveat above.
- [Shadow Run](skills/shadow-run/) — unattended creative exploration and isolated
  prototypes within an explicit time and usage window.
  [Requirements and usage](skills/shadow-run/references/setup.md).

## Repo structure

- `skills/<skill-id>/SKILL.md`: one folder per skill, following the `SKILL.md` convention
