# Grounding "the repo is the agent and the agent is the repo"

**Research date:** 2026-11-19. **Mode:** read-only primary-source research; this file is the
only file written. **Thesis under test** (user's words): "the repo is the agent and the agent is
the repo; each repo has a specialized agent; an agents-home/org agent orchestrates them; the user
talks only to the home agent."

**How to read this report.** `[FACT]` means the statement is quoted or closely paraphrased from
the linked primary source or local file, checked on the date above. `[INFERENCE]` means our
reasoning from those facts and is explicitly not a claim made by the source. Vendor docs are a
moving target; re-check URLs before relying on them. Where a source is affiliated with the idea
it describes, that is called out rather than hidden. This report complements
`SOFTWARE_FACTORY_GROUNDING.md` (in `agents-home/docs/research/`); it does not repeat its GitHub
Issues/Discussions analysis.

---

## 1. Five distinctions the thesis blurs

These are analytical definitions (`[INFERENCE]`) anchored to facts where a source uses the same
concept. They matter because the thesis is only defensible if each term is kept separate.

| Term | Precise meaning | Nearest primary-source anchor | Does the source actually say this? |
| :--- | :--- | :--- | :--- |
| **repo-as-state** | The repository is durable, versioned state: code, history, issues, `AGENTS.md`, skills, CI. It is *read* by an agent; it does not itself act. | `[FACT]` "Code stays where it is, and each repo keeps its history, remote and issue tracker." (<https://www.aihero.dev/the-home-repo-pattern>); `[FACT]` "each repository remains the source of truth for its code" (`/mnt/storage/projects/magitech/agents-home/AGENTS.md`) | Yes. |
| **repo-as-agent** | Repo *contents* (instructions, skills, workflow files) configure an agent that runs when triggered. The repo is the agent's definition and memory, not a literal reasoning entity. | `[FACT]` "GitHub Agentic Workflows are AI-powered repository automations that you define in markdown and run as GitHub Actions workflows." (<https://docs.github.com/en/copilot/concepts/agent-capabilities/agent-powered-workflows-and-operations/about-github-agentic-workflows>) | Yes, in this limited sense; no vendor says a repo *is* an agent. |
| **agent-per-repo** | A distinct, persistent agent identity/service bound to one repo, as a member of a fleet of such agents. | `[FACT]` project-scoped `.claude/agents/` are "ideal for subagents specific to a codebase. Check them into version control so your team can use and improve them collaboratively." (<https://code.claude.com/docs/en/subagents>); `[FACT]` Copilot automations are "scoped to" and act "within the repository where they are configured" (<https://docs.github.com/en/copilot/concepts/agent-capabilities/agent-powered-workflows-and-operations/about-automations>) | No. Sources offer repo-*scoped* agents and automations, not an autonomous agent per repo with cross-repo identity. |
| **orchestrator / router** | A component that decides which specialist runs next, either by model decision or by code. | `[FACT]` "There are two main ways to orchestrate agents: 1. Allowing the LLM to make decisions ... 2. Orchestrating via code." (<https://openai.github.io/openai-agents-python/multi_agent/>); `[FACT]` ADK collaborative workflows let "a single agent to act in a dynamic coordinator role" (<https://google.github.io/adk-docs/workflows/>) | Yes, as a first-class pattern. |
| **user-facing single point of contact** | One conversation the human talks to, while specialists work behind it and return results. | `[FACT]` "Use agents as tools when a specialist should help with a bounded subtask but should not take over the user-facing conversation." (<https://openai.github.io/openai-agents-python/multi_agent/>); `[FACT]` subagents "do that work in its own context and returns only the summary" (<https://code.claude.com/docs/en/subagents>) | Yes, as a first-class pattern. |

`[INFERENCE]` The phrase "the repo is the agent and the agent is the repo" is a rhetorical
compression of **repo-as-state + repo-as-agent**. It is not a claim any vendor makes, and it
hides the hard part: an agent needs a runtime, credentials, a session, a tool budget and a
verification gate — none of which a repository supplies by itself.

---

## 2. What primary sources actually establish

### 2.1 A repo can carry an agent's definition and run it on triggers

- `[FACT]` GitHub Agentic Workflows: "You still define guardrails in frontmatter, such as
  triggers, permissions, and safe outputs." Each workflow has "**Frontmatter** (YAML between
  `---` markers): Configures when the workflow runs, what permissions it has, and what write
  operations are allowed" and a "**Markdown body**: Contains your natural language instructions
  that the AI agent follows." Steps: "Compile the markdown workflow file into a `.lock.yml`
  GitHub Actions workflow file"; "Commit and push both files to the default branch."
  (<https://docs.github.com/en/copilot/concepts/agent-capabilities/agent-powered-workflows-and-operations/about-github-agentic-workflows>)
- `[FACT]` Same page, example tasks: "Triaging incoming issues and labeling them by type and
  priority"; "Investigating CI failures and suggesting fixes"; "Keeping documentation up to date
  with code changes." Engines: "GitHub Copilot ... Anthropic Claude, OpenAI Codex, Google
  Gemini" chosen via the `engine` property.
- `[FACT]` Copilot automations: "Automations let you run Copilot cloud agent automatically on a
  schedule, in response to events in a repository, or programmatically via the API." Triggers
  include "When an issue is created", "When a pull request is opened", "When a pull request is
  synchronized", "On a schedule." (<https://docs.github.com/en/copilot/concepts/agent-capabilities/agent-powered-workflows-and-operations/about-automations>)
- `[FACT]` Same page, an important scoping limit: "GitHub tools can only take action in the
  single repository the automation is scoped to. Tools from MCP servers aren't limited to that
  repository." Also: "Automations are stored separately from your repository's contents. They
  are not committed to Git, so they are not versioned alongside your code or managed through pull
  requests." (Contrast with Agentic Workflows, which *are* committed.)
- `[FACT]` Cross-repo execution exists but as a *session property*, not a fleet: cloud sandbox
  sessions "can span across repositories in one organization. Changes can be made across
  multiple repositories"; GitHub Actions-based sessions "require a repository. Changes are made
  only in the specific, single repository context."
  (<https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent>)
- `[FACT]` Codex Cloud: "Each task has its own workspace and can keep working while your
  computer is asleep"; "ask Codex to check out any repository available to Codex through your
  connected GitHub or GitLab account"; "a published environment lets you reuse the same setup
  across tasks"; you "commit or open a pull request when you're ready."
  (<https://developers.openai.com/codex/cloud/>)
- `[INFERENCE]` This is the strongest support for the thesis: the "repo carries its own agent"
  idea is a real, shipped GitHub feature. But it is an **automation scoped to a repo**, not an
  autonomous peer agent that another agent delegates to. Note also that Codex Cloud's PR step is
  explicitly "when you're ready" — human-gated, not autonomous.

### 2.2 Specialization, routing and a single front door are standard patterns

- `[FACT]` Claude Code subagents: "Subagents are specialized AI assistants that handle specific
  types of tasks... Each subagent runs in its own context window with a custom system prompt,
  specific tool access, and independent permissions." "Claude uses each subagent's description
  to decide when to delegate tasks." "The first filter removes these tools from every subagent";
  a coordinator example uses `tools: Agent(worker, researcher), Read, Bash` described as
  "Coordinates work across specialized agents."
  (<https://code.claude.com/docs/en/subagents>)
- `[FACT]` Same page, scope and isolation: subagent files can be "Managed settings"
  (organization-wide), project (`.claude/agents/`), user (`~/.claude/agents/`) or plugin-scoped;
  "To give the subagent an isolated copy of the repository instead, set `isolation: worktree`."
  Also: "Subagents work within a single session" — separate/multi-session coordination is a
  *different* feature (background agents, cross-session messaging, agent teams), not the same
  primitive.
- `[FACT]` OpenAI Agents SDK: "Handoffs allow an agent to delegate tasks to another agent. This
  is particularly useful in scenarios where different agents specialize in distinct areas."
  "Handoffs are represented as tools to the LLM... `transfer_to_refund_agent`." Example:
  `triage_agent = Agent(name="Triage agent", handoffs=[billing_agent, handoff(refund_agent)])`.
  "Handoffs stay within a single run." (<https://openai.github.io/openai-agents-python/handoffs/>)
- `[FACT]` OpenAI orchestration table: "**Agents as tools** — A manager agent keeps control of
  the conversation and calls specialist agents through `Agent.as_tool()`"; "**Handoffs** — A
  triage agent routes the conversation to a specialist, and that specialist becomes the active
  agent for the rest of the turn." Guidance: "Use **agents as tools** when a specialist should
  help with a bounded subtask but should not take over the user-facing conversation."
  (<https://openai.github.io/openai-agents-python/multi_agent/>)
- `[FACT]` Google ADK: "structuring [agents] as a single, monolithic agent can become challenging
  to develop, evaluate, and maintain"; workflows give "Predictability", "Reliability" and
  "Structure"; types include graph, dynamic, collaborative ("a single agent to act in a dynamic
  coordinator role"), sequential/loop/parallel templates, and "**Experimental: Agent Routing**
  ... allows you to select between multiple agents at runtime using router functions."
  (<https://google.github.io/adk-docs/workflows/>)
- `[FACT]` A2A: "The A2A protocol is an open standard for communication between AI agents...
  whatever framework or vendor built them." Its example: "The AI assistant now acts as an
  orchestrator. It gathers the results from every A2A-enabled agent and presents a single,
  complete travel plan in response to the user's prompt." (<https://a2a-protocol.org/latest/topics/what-is-a2a/>)
- `[INFERENCE]` The thesis' "home agent orchestrates them; user talks only to the home agent" is
  almost exactly OpenAI's *manager/triage agent* pattern plus A2A's orchestrator example. The
  difference is the **unit of specialization**: vendors specialize by *task/domain* (billing,
  refunds, flight booking), whereas the thesis specializes by *repository*. We found no source
  endorsing repo boundaries as the right specialization axis.

### 2.3 Protocol boundaries: MCP is not A2A, and neither is an org chart

- `[FACT]` MCP: "MCP focuses solely on the protocol for context exchange—it does not dictate
  how AI applications use LLMs or manage the provided context"; "MCP follows a client-server
  architecture where an MCP host ... establishes connections to one or more MCP servers"; three
  server primitives — "Tools", "Resources", "Prompts". "Clients that federate many servers can
  use progressive tool discovery rather than loading every tool upfront."
  (<https://modelcontextprotocol.io/docs/concepts/architecture>)
- `[FACT]` A2A: "A2A crosses the boundary between agents; MCP stays within one agent, connecting
  it to APIs and enterprise applications." "Wrapping [agents] as tools ... is inefficient ...
  A2A exposes agents as they are, with no wrapping." "Opaque Execution: Agents collaborate
  without exposing their internal logic, memory, or proprietary tools."
  (<https://a2a-protocol.org/latest/topics/what-is-a2a/>)
- `[INFERENCE]` A repo exposes **tools and context** (MCP-shaped) more naturally than it exposes
  a negotiable peer agent (A2A-shaped). If each repo agent must be a peer that can clarify and
  negotiate, MCP alone will not carry it; if it only needs to expose `verify_repo`-style
  operations, MCP/tool-style federation is sufficient and much cheaper. The thesis does not
  choose between these, which is a design decision, not a fact.

### 2.4 Safety, trust and verification boundaries vendors actually require

- `[FACT]` Agentic Workflows: "Agents run in firewalled containers with read-only tokens by
  default. Write actions are limited to declared 'safe outputs' that you have defined, and
  checked by agentic threat detection." "Secrets stay outside the agent runtime"; "Threat
  detection: Proposed outputs are scanned... before write actions are applied"; "Role-based
  access"; "default cap is 1,000 AIC per run"; "`max-ai-credits` ... to cap inference usage."
  (URL in §2.1.)
- `[FACT]` Copilot automations: "Selecting tools is the main way you control the scope of an
  automation"; "automations ignore GitHub events triggered by users who don't have write access
  to the repository by default. This helps prevent untrusted users from causing Copilot to take
  action"; "GitHub Actions workflows don't run on a pull request until a user with write access
  approves them"; "If your repository requires at least one pull request approval, an additional
  approval is required by default for pull requests created by a shared automation."
  (URL in §2.1.)
- `[FACT]` Copilot in the cloud: "Without write access to a repository, your Copilot session is
  read-only"; "Copilot can only work on one branch at a time and can open one pull request per
  task"; "Each Copilot session that runs on GitHub Actions has a maximum execution time of 59
  minutes. This limit cannot be extended or bypassed"; "A ruleset or branch protection rule can
  prevent Copilot from creating or updating pull requests"; "Copilot can produce incorrect or
  suboptimal code, including code that contains security vulnerabilities. Review and test the
  output before using it in production."
  (<https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent>)
- `[FACT]` Claude Code subagents: `tools`/`disallowedTools` allow/deny lists, `permissionMode`,
  per-subagent `mcpServers`, `maxTurns`, `isolation: worktree`, and "Claude Code also checks the
  command itself" to block redirects into the main checkout. (URL in §2.2.)
- `[FACT]` OpenAI handoffs: "Nested handoff history changes how the transcript is represented;
  it does not redact sensitive data. Tool-call arguments and tool outputs can remain in the
  generated assistant summary... Treat the receiving agent and its model provider as recipients
  of the forwarded history." (URL in §2.2.)
- `[FACT]` Our earlier grounding recorded vendor convergence on "read-only planning → written
  definition of done → bounded execution in a sandbox/worktree → machine-checkable gate → PR →
  protected-branch human approval" (`SOFTWARE_FACTORY_GROUNDING.md` §4.4).
- `[INFERENCE]` Every safety control above is **per session/run/repo**, enforced by the runtime
  and the host (Actions, sandbox, branch protection) — not by the repository's prose. A
  "repo-as-agent" design that trusts the repo's own `AGENTS.md` to enforce privilege is
  inverted; the host must enforce least privilege and the repo must only declare intent.

---

## 3. Our current achieved state, in facts

| Area | Achieved state | Source |
| :--- | :--- | :--- |
| Home repo | Map of other repos, shared skills, shared standards and gates. Guidance: "Start sessions here when work may span repositories; each repository remains the source of truth for its code." | `/mnt/storage/projects/magitech/agents-home/AGENTS.md`; `README.md`; `docs/WORKFLOWS.md`; `CODING_STANDARDS.md` |
| CI in home repo | One workflow, `CI`, triggered only on `push`/`pull_request` to `main`, with `contents: read`, validating skills and linting workflows. No issue/label/schedule agent trigger. | `/mnt/storage/projects/magitech/agents-home/.github/workflows/ci.yml` |
| Harness | "Every capability is an anima Service mounted by ... `AGENT_SERVICES`"; "the core loop and all 15 tools" (including `load_skill`, `add_repo`, `verify_repo`, `run_command`, `web_search`). | `/mnt/storage/projects/magitech/home-swe-home/AGENTS.md`, `README.md`, `DESIGN.md` |
| Home-first behavior | Home resolved from config → env → walk-up; "Multi-repo work is map-driven ... missing repos are cloned as siblings only after confirmation; map edits go through a PR; each target repo's `AGENTS.md` is layered into the session; each affected repo's own checks must pass before the task is done." | `home-swe-home/DESIGN.md` ("Home-first agent architecture") |
| Sub-agents | Explicitly deferred: "Execution uses one context initially — no sub-agents until evidence demands isolation." A grep across `home-swe-home/src` found no sub-agent/handoff code; the only "orchestrator" mention is a comment that `improve.py` is "a library for an external orchestrator." | `home-swe-home/DESIGN.md`; local grep, 2026-11-19 |
| Sandbox | "Shell commands run unsandboxed on the host by default. Pass `--sandbox` ... to run them inside an isolated Docker container." Sandbox is fail-closed when enabled and Docker is unavailable. | `home-swe-home/README.md`, `DESIGN.md` |
| Improvement loop | A/B eval over `HARD_TASKS`; "No harness candidate has produced a reproducible general-capability gain; the only positive result was a synthetic canary whose answer was encoded in the candidate prompt. No candidate was adopted." One 3-trial run was 34/36 NVIDIA 429s. | `home-swe-home/DESIGN.md`; field note `2026-11-19-magecode-native-home-agent.md` |
| Pattern repo | Descriptive only: "These are descriptive statements about one workspace, not requirements for other users... Nothing here is a protocol or certification." Claims C1–C9 are "Pilot observation." "Status: incubation. This repository is exploratory and non-normative." "Not a protocol or conformance target." | `agents-home-pattern/CONFORMANCE.md`, `README.md` |
| Harness evidence | Only OpenCode, Antigravity, Magecode; "A cell holds the strongest recorded claim, not a capability estimate. 'Open question' means no field note recorded the behaviour; it is not a claim that the harness cannot do it." Several cells (Antigravity pointer resolution/cross-repo; Magecode skill loading) are open. | `agents-home-pattern/docs/harness-matrix.md` |
| Other repo agents | None exist. No autonomous issue→PR loop: the only home-repo workflow is plain CI, and no `ready-for-agent` trigger was found in local `.github` files. | Local inspection/grep, 2026-11-19; `SOFTWARE_FACTORY_GROUNDING.md` §6 |

`[FACT]` The pattern repo's own open question: "What repeated independent implementations would
demonstrate that this is a protocol-worthy pattern rather than a useful convention?"
(`agents-home-pattern/docs/open-questions.md`). `[FACT]` A field note states: "The claim that
home-first is beneficial is a design inference, not a controlled user study."
(`docs/field-notes/2026-11-19-magecode-native-home-agent.md`).

---

## 4. Verdict: useful north star **and** premature leap

`[INFERENCE]` **Both, and the two verdicts apply to different layers.** As a *steering
heuristic* ("start from the home; keep per-repo truth; make one conversational front door;
specialize by domain") the thesis is well aligned with current vendor patterns and with our own
pilots. As a *fleet architecture* ("one autonomous specialized agent per repo, orchestrated by a
home/org agent") it is premature: we have one working harness, no second repo agent, no
delegation protocol, no autonomous issue→PR loop, and no measured benefit.

### 4.1 Supported by evidence today

- `[INFERENCE]` repo-as-state: directly supported (§1, §3). Each repo owns code, history, issues
  and checks; the home owns steering and navigation.
- `[INFERENCE]` repo-as-agent in the weak sense: GitHub ships repo-committed natural-language
  agent automations running on repo events (§2.1). This is the closest literal instance of the
  slogan and it is real.
- `[INFERENCE]` orchestrator + single front door: standard, documented patterns (§2.2) —
  triage/manager agent, `Agent.as_tool()` vs handoffs, ADK coordinator, A2A orchestrator.
- `[INFERENCE]` our home harness implements a *single* version of the front door: one session that
  resolves the home, layers each repo's `AGENTS.md`, clones on confirmation and runs per-repo
  checks (`DESIGN.md`).

### 4.2 Design hypotheses (plausible, not yet evidenced by us)

- `[INFERENCE]` **Repo boundaries are the right specialization axis.** Vendors specialize by
  task; our evidence does not show repo-scoped agents outperforming task-scoped ones. The
  cross-repo work-phase pilot did show a single session using multiple repos and a shared skill,
  which is evidence *for* the home session, not for per-repo agents.
- `[INFERENCE]` **A home/org agent can reliably route work to child agents** with enough context
  and without leaking credentials. OpenAI's docs explicitly warn that handoff history "does not
  redact sensitive data" (§2.4), which makes "single front door + many repositories" a real
  trust-boundary problem, not just a routing problem.
- `[INFERENCE]` **Per-repo agents reduce context cost.** Claude Code's subagent rationale is
  context preservation ("returns only the summary"), but our harness has "no sub-agents until
  evidence demands isolation" and its measured improvement work found no adoptable gain. There is
  no local measurement that the fleet shape helps.
- `[INFERENCE]` **A2A-style peer agents are needed between repo agents.** Not established: MCP
  tool-style federation may suffice. Choosing A2A now would be protocol-first, need-first later.

### 4.3 Speculative / marketing-flavoured

- `[INFERENCE]` "The repo is the agent and the agent is the repo" as identity, not metaphor. No
  primary source makes this claim; it compresses a runtime, a session and credentials into a
  git checkout.
- `[INFERENCE]` "Each repo has a specialized agent" as an inevitable end state. This is an
  extrapolation from general "specialized agents are good" advice (§2.2) to a specific
  organizational boundary; vendors do not endorse that boundary.
- `[INFERENCE]` Claiming the architecture is industry-validated. Our earlier report already
  recorded a coverage gap: "no independent primary source was found that endorses the combined
  'home repo + GitHub control plane + autonomous factory' design." The sources here validate the
  *primitives* (repo-committed workflows, handoffs, coordinators, A2A, safe outputs), not the
  *combination*.

---

## 5. Staged adoption recommendation

### Build now (cheap, reversible, evidence-generating)

1. **Keep the front door single, but keep execution single-context.** Continue using the one home
   session; do not add sub-agents or a fleet. This matches `DESIGN.md`'s explicit stance and
   Claude Code's own advice that subagents are for when a side task "would flood your main
   conversation" (<https://code.claude.com/docs/en/subagents>).
2. **Close the one-repo loop first:** one `ready-for-agent` issue → one bounded session in a
   worktree → one PR → one required check → human approval. GitHub Agentic Workflows and Copilot
   automations both document exactly this shape with read-only defaults and safe outputs (§2.1,
   §2.4); our own earlier grounding recommends the narrowest loop first.
3. **Make repo-scoped automation explicit and versioned if adopted.** Prefer GitHub Agentic
   Workflows (committed `.md` + compiled `.lock.yml`, frontmatter guardrails) over unversioned
   Copilot automations when we want reviewable, PR-managed agent definitions — the latter are
   "not committed to Git" (§2.1).
4. **Enforce least privilege at the host:** read-only tokens by default, declared safe outputs,
   firewalled execution, secrets outside the agent runtime, spend caps — all documented defaults
   in §2.4. For our harness specifically, flip the default away from "shell commands run
   unsandboxed on the host" for any unattended run.
5. **Instrument before claiming improvement.** Base every adoption decision on the harness A/B
   method already in `DESIGN.md`; record failures and refusals honestly, as the pattern repo's
   evidence labels require.
6. **File the fleet idea as a labelled *Hypothesis*** in `agents-home-pattern` with a `Done when`
   and a `Reproduce` block, per that repo's workflow — not as a standard or roadmap commitment.

### Later (only after the prerequisites in §6)

7. **Add a second specialized agent** (task-scoped first, e.g. a read-only reviewer) and measure
   whether routing reduces context or error rate versus one context. Specialize by *task*, not
   by repo, until a repo-boundary hypothesis is tested.
8. **Choose an inter-agent contract deliberately:** tool-style (`Agent.as_tool()` / MCP-shaped
   operations) for bounded subtasks; handoffs only when routing itself is the workflow; A2A only
   if genuine cross-boundary, opaque, multi-turn negotiation is required (§2.1–2.3).
9. **Introduce an org/home orchestrator** only when there are at least two real child agents and
   an observed routing problem. Use code orchestration for deterministic parts (OpenAI's "more
   deterministic and predictable, in terms of speed, cost and performance") and LLM routing for
   the open-ended parts.
10. **Revisit per-repo agents** only with multi-user evidence and a measured failure mode that
    repo-scoped identity solves.

### What would falsify the idea

- `[INFERENCE]` The fleet adds no measurable gain over one home session on a fixed task suite
  (our harness already refuses adoptions without a reproducible gain).
- `[INFERENCE]` Context/cost per task rises faster than quality improves — Claude Code warns that
  subagent descriptions consume context and shows a 15,000-token warning threshold (§2.2).
- `[INFERENCE]` Handoff history leaks secrets across repo boundaries, or one repo's untrusted
  issue content triggers writes in another; vendors' "does not redact" and "ignore untrusted
  events by default" controls exist precisely because this risk is real (§2.4).
- `[INFERENCE]` Repo map drift or private-repo access makes "one agent per repo" unmaintainable —
  our own drift-check and private-access limitations are already recorded (CONFORMANCE C2; field
  note limitations).
- `[INFERENCE]` Required checks and small-batch discipline degrade as autonomous PR volume rises
  — the 2024 DORA finding warns about exactly this (`SOFTWARE_FACTORY_GROUNDING.md` §3.2).

### Required safety / trust boundaries

- Least privilege: read-only by default; explicit tool allowlists; declared safe outputs; scoped
  MCP servers; one branch and one PR per task (§2.4).
- Sandbox: firewalled execution, opt-in Docker sandbox, fail-closed, spend/turn/time caps
  (`max-ai-credits`, `maxTurns`, 59-minute Actions limit) (§2.4).
- PR gates: protected branches, required unique-name status checks, "do not allow bypassing"
  where agents get write access (`SOFTWARE_FACTORY_GROUNDING.md` §2.3, §6).
- Human approval: a person approves plan → merge; shared automations need an extra approval by
  default; "Review and test the output before using it in production" (§2.4).
- Audit: transparent sessions/logs, recorded prompts and tool use, evidence notes with date,
  label, status and limitations; treat an agent's own summary as not independent proof
  (pattern repo `README.md`, field-note headers).
- Context hygiene: explicit handoff `input_filter`/redaction rather than assuming delegation
  sanitizes history (§2.4).

---

## 6. "Cart before the horse": missing prerequisites

`[INFERENCE]` A multi-agent fleet only matters after these exist; none is complete locally:

1. **A proven single-agent loop with a real PR gate.** Today: bounded session + per-repo checks
   exist, but no issue→PR trigger and no measured end-to-end success rate
   (`ci.yml`, `DESIGN.md`, §3).
2. **A trustworthy verification signal.** The improvement suite was at ceiling / confounded by
   bad checkers and provider 429s; "no harness candidate has produced a reproducible general-
   capability gain" (`DESIGN.md`, field note). Routing decisions need a signal that discriminates.
3. **A delegation contract with context and trust rules.** Nothing in `home-swe-home/src` defines
   sub-agents, handoffs or a message protocol (local grep, §3).
4. **Identity and permission model per repo.** Who is the child agent, what token does it use,
   and what can it write? Vendors make this explicit (scoped automations, per-subagent tools,
   safe outputs); we have only a repo map and a confirmation prompt.
5. **Cost/latency budget.** No measured per-task cost or token budget for a fleet; Claude Code's
   description-token warning and GitHub's `max-ai-credits` cap are reminders that routing is not
   free (§2.2, §2.4).
6. **Cross-repo PR mechanics.** A child agent that edits repo B from a home session must produce
   reviewable changes in repo B with B's checks passing; our harness does `verify_repo`, but no
   fleet has done this repeatedly.
7. **Map health over time.** Drift is "reported read-only rather than silently repaired"
   (CONFORMANCE C2) and private access gates collaborators (field-note limitations); a fleet
   multiplies these maintenance costs.
8. **Independent/multi-user validation.** Pattern claims are explicitly one workspace, one user,
   three harnesses, with open cells (`CONFORMANCE.md`, `harness-matrix.md`); the pattern repo asks
   what repeated implementations would make it protocol-worthy (`open-questions.md`).
9. **A reason to specialize by repo rather than by task.** Not evidenced (§4.2).

`[INFERENCE]` In short: **repo-as-state is done; repo-as-agent is partially done in one harness;
agent-per-repo and the orchestrating home agent are not started.** Building the fleet now would
be cart before horse — but the phrase is still useful as a north star because it points at the
three real gaps: delegation, trust boundaries, and measured verification.

---

## 7. Unresolved questions

- Does any primary source endorse **repository boundaries** as the agent-specialization axis, or
  is that purely our extrapolation from task-specialization advice? (§2.2, §4.2)
- Is "repo-as-agent" best implemented as committed GitHub Agentic Workflows (versioned,
  frontmatter-guardrailed) or as a persistent service with identity (neither of which vendors
  currently ship per repo)? (§2.1)
- Which inter-agent contract is right for us — tool-style/MCP, handoffs, or A2A — and at what
  threshold does each become worth its cost? (§2.3, §5.8)
- Can a single front door safely forward context across repos without leaking secrets, given
  that handoff history is explicitly not redacting? (§2.4)
- What is the smallest measurable task suite that could show a fleet beating one context? Our
  current suite was confounded by ceiling effects and provider 429s. (§3, §6.2)
- Would a second repo agent be task-scoped (reviewer) or repo-scoped, and what evidence would
  decide? (§6.9)
- Does the "publishable-minimum gate" for mapping new repos scale to a fleet, or does it become a
  bottleneck? (`2026-11-cross-repo-work-phase.md`)
- Would making the first factory loop autonomous change the DORA stability/rework picture, and
  what baseline do we compare against? (`SOFTWARE_FACTORY_GROUNDING.md` §3.2)
- Research-coverage gap: no source found that validates the *combined* home-repo + per-repo-agent
  + orchestrator architecture end to end; only its primitives are validated.

---

## Source index (all fetched 2026-11-19)

Primary web sources:

- <https://code.claude.com/docs/en/subagents>
- <https://modelcontextprotocol.io/docs/concepts/architecture>
- <https://openai.github.io/openai-agents-python/handoffs/>
- <https://openai.github.io/openai-agents-python/multi_agent/>
- <https://developers.openai.com/codex/cloud/>
- <https://google.github.io/adk-docs/workflows/>
- <https://a2a-protocol.org/latest/topics/what-is-a2a/>
- <https://docs.github.com/en/copilot/concepts/agent-capabilities/agent-powered-workflows-and-operations/about-github-agentic-workflows>
- <https://docs.github.com/en/copilot/concepts/agent-capabilities/agent-powered-workflows-and-operations/about-automations>
- <https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent>
- <https://www.aihero.dev/the-home-repo-pattern> (same publisher as the "software factory" definition; not independent corroboration)

Local sources:

- `/mnt/storage/projects/magitech/agents-home/AGENTS.md`, `README.md`, `docs/WORKFLOWS.md`,
  `CODING_STANDARDS.md`, `.github/workflows/ci.yml`
- `/mnt/storage/projects/magitech/agents-home/docs/research/SOFTWARE_FACTORY_GROUNDING.md`
- `/mnt/storage/projects/magitech/home-swe-home/AGENTS.md`, `README.md`, `DESIGN.md`
- `/mnt/storage/projects/magitech/agents-home-pattern/README.md`, `CONFORMANCE.md`,
  `docs/harness-matrix.md`, `docs/open-questions.md`, `docs/WORKFLOW.md`,
  `docs/field-notes/2026-11-19-magecode-native-home-agent.md`,
  `docs/field-notes/2026-11-cross-repo-work-phase.md`
- Local greps of `home-swe-home/src` and `agents-home/.github` (2026-11-19)
