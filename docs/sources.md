# Sources

Sources checked for the initial pilot notes on 2026-11-15. Vendor documentation
describes intended behavior; it is not a substitute for testing the relevant
product version and surface.

## Pattern and standards

- Matt Pocock, [The Home Repo Pattern](https://www.aihero.dev/the-home-repo-pattern)
  — describes one repository for skills, `AGENTS.md`, shared docs, and pointers
  to other repositories.
- [Agent Skills specification](https://agentskills.io/specification) — defines
  the skill directory and `SKILL.md` format; it does not define a universal
  global discovery location.
- [`.agents` Protocol](https://dotagentsprotocol.com/) — a separate project
  describing a broader `.agents/` configuration directory; its site labels
  the protocol as a draft.

## Harness discovery documentation

- [OpenCode: Skills](https://opencode.ai/docs/skills/) — lists global
  `~/.agents/skills` and project `.agents/skills` as compatibility sources,
  alongside OpenCode- and Claude-specific directories.
- [GitHub Copilot CLI: Adding agent skills](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills)
  — lists personal `~/.agents/skills` and project `.agents/skills`, while
  warning that supported locations can vary by surface.
- [Antigravity: Agent skills](https://antigravity.google/docs/skills) — lists
  global `~/.gemini/config/skills`, project `.agents/skills`, and ancestor
  workspace directories for the App.
- [OpenAI Codex: Skills](https://developers.openai.com/codex/skills/) —
  describes repository `.agents/skills` scanning from the current working
  directory through the repository, plus other skill scopes.
- [DeepSeek Harness repository](https://github.com/deepseek-ai/deepseek-harness)
  — its current tree includes skills under `.agents/skills`; this alone does
  not establish a general user-level discovery contract.
