# Component-creation gap: no autonomous plugin factory in mth-plugins

**Recorded:** 2026-11-19
**Evidence type:** Read-only code and ADR audit of `mth-plugins` and
`magitech-harness`, plus local comparison with `magecode`
**Status:** Verified file-level facts; the "deepseek-harness-style self-creation"
comparison is inference from the user's description, not from that repository.

## What was checked

`mth-plugins` contains no component, factory, or meta-tool that creates or
installs new Skills/Services/plugins at runtime. The relevant code is:

- `src/mth_plugins/bridges/skills/service.py` — `SkillsBridgeService` exposes
  `activate_skill(name)` and `run_skill_script(...)` only. `discover_skills()`
  is called once from `apply()` at startup; no tool re-runs it.
- `src/mth_plugins/index.py` and `index.json` — a static catalog of 20
  components for harness discovery, not runtime installation.
- `docs/adr/0013-service-contract-dependencies-and-capability-declarations.md`
  proposes advisory auto-installation via `recommended_plugins`, but the
  shipped `recommended_components` field in
  `magitech-harness/src/magitech_harness/components/manifest.py` has no consumer.
- `magitech-harness/src/magitech_harness/cli.py` — `mth component install`
  only prints a profile row for a human to add; it does not mount anything.

`ComponentService.mount_component()` does exist and has a disposer-based
lifecycle, but only tests call it in `mth-plugins`; there is no model-facing
tool wired to it.

## Safeguards that already exist (relevant to any future implementation)

- `docs/adr/0012-workspace-trust-gate-and-integrity-verification.md` — human
  approval for project skills/custom plugins, fail closed when no broker exists.
- `docs/adr/0014` — AST write protection forbids reassigning registered tool
  names or control keywords in model-written code.
- `docs/adr/0008` — sandbox ladder; `run_skill_script` rejects `..` and
  absolute script names.
- Anima `inject`/`requires_services` gates components until dependencies exist.

## Dependency constraint

`magecode` depends on `anima` and `google-genai` but not on `magitech-harness`
or `mth-plugins`, and it has no `ctx.components` service. It cannot use the
harness component runtime today without new dependencies. It does have
`write_file`, `reload_module` (read-before-reload guard), and its own
`SkillsService`, but none of them register newly created components into a
running session.

## Implication for the pattern

Autonomous component creation requires more than file writing: a discovery
re-run, validation, registration, lifecycle disposers, trust gating, and an
AST/tool-name safety layer. Those pieces exist as *ADRs and static mechanisms*
in the ecosystem but are not assembled into an agent-callable capability.
This is a concrete, investigated gap — not something to assume is already
solved.

## Limitations

- One local checkout per repo; several were on non-default branches during the
  audit, though the component facts were checked against source files present.
- `deepseek-harness` was not available locally; the comparison rests on the
  user's description.
