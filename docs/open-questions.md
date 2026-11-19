# Open Questions

This list tracks questions to answer with pilot evidence, not requirements for
a future protocol.

## Scope and ownership

- Is the pattern primarily personal, team-shared, or useful in both cases?
- What should be canonical in an agent home repository, and what should
  remain local to each code repository?
- How should a curated repo map stay accurate as repositories are added,
  transferred, renamed, unpublished, or present only as local checkouts?
  Should it describe the workspace, the organization, or an explicitly
  selected subset? Candidate approaches include a human maintenance
  checklist, a read-only drift report, or a generated inventory with curated
  annotations; what evidence would justify choosing among them?
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

## Decisions

The following choices are recorded as revisable decisions with explicit reopen
conditions in
[`../agents-home/docs/DECISIONS.md`](../../agents-home/docs/DECISIONS.md), not
permanent doctrine:

- **GitHub Discussions scope (D-003):** Discussions are scoped to
  `agents-home-pattern`, not enabled org-wide or on product repos by default.
  GitHub describes Discussions as open-form, often without a clear owner, and
  often not resulting in an actionable task, whereas product repos rely on the
  deterministic `ready-for-agent` issue queue. Revisit when opening public
  repos that need an external community or when cross-repo public dialogue
  emerges.
- **GitHub Projects / roadmap (D-004):** No GitHub Projects board is added yet
  because no roadmap exists and no autonomous issue→PR loop produces work to
  visualize (adding a board now would duplicate state). Revisit when a single
  issue→PR loop produces frequent real work and cross-repo visibility becomes
  a pain point.
