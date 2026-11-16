# Open Questions

This list tracks questions to answer with pilot evidence, not requirements for
a future protocol.

## Scope and ownership

- Is the pattern primarily personal, team-shared, or useful in both cases?
- What should be canonical in an agent home repository, and what should
  remain local to each code repository?
- Should one repository hold both human-facing home guidance and machine
  discovery adapters, or should those concerns be split?
- How should a private canonical repository serve collaborators or machines
  that cannot access it?

## Discovery and distribution

- Which harnesses discover the same locations, and which require adapters?
- Should adapters be symlinks, copies, generated files, native configuration,
  or a mix? How should Windows, containers, remote workspaces, and managed
  machines be handled?
- How should installation handle collisions, updates, removals, stale links,
  and a moved canonical checkout?
- What are each harness's reload, precedence, duplicate-name, and
  project-versus-user-scope rules?
- Is a directory named `home` materially different from `.agents` or another
  name, beyond navigation and harness-specific discovery?

## Interoperability and maturity

- What can be delegated to existing standards such as Agent Skills,
  `AGENTS.md`, and MCP, and what—if anything—remains a distinct contract?
- What repeated independent implementations would demonstrate that this is a
  protocol-worthy pattern rather than a useful convention?
- What testable conformance claims could be made without implying that one
  harness's discovery behavior is universal?
- Which user experiences should count as validation, and how should version
  changes in harnesses be tracked?
