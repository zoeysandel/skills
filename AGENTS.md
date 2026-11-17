# Repository maintenance

- Put reusable skills in `shared/skills/`. Put skills that depend on Codex or Claude Code in `codex/skills/` or `claude-code/skills/`. Keep deprecated skills and templates in `archive/`, outside installable skill directories and plugin packages.
- Keep personal names and identifiers, client or project details, machine-specific home paths, credentials, conversation logs and private examples out of tracked files. Use neutral examples. Review the publication tree and reachable Git history for exposure before changing visibility. A real secret in history blocks publication until it is remediated.
- Make required host capabilities explicit and state what can be done when a capability is missing. Preserve the user's task authority. A skill cannot grant permission to delegate, publish, deploy, or make external changes.
- The `skills` Claude marketplace packages the three shared development skills as `development-workflows`. Check skill frontmatter, relative links, package inventory and Claude marketplace validation when changing their sources or manifests.
