# Tiered repo-map drift gate

**Recorded:** 2026-11-23
**Label:** Pilot observation
**Evidence type:** Local reproduction of the PR #82 map-loss failure and of the
replacement gate, plus the gate run on the repaired workspace.
**Status:** One workspace and one checkout layout; the rule describes our gate,
not a requirement for other homes or harnesses.
**Limitations:** Membership ambiguity is still left to a human. The check reads
local remotes only, so it cannot detect an upstream rename or an unlisted
private repository. It does not prove that other harnesses consume the map.
**Reproduce:** from `agents-home`,
`printf '# no map\n' > /tmp/opencode/no-map.md && python3 scripts/check_repo_map.py --agents-md /tmp/opencode/no-map.md`
exits 1; adding `--informational` exits 0; with the repaired 11-entry
`AGENTS.md`, `python3 scripts/check_repo_map.py` exits 0 and
`python3 scripts/check_all.py` reports ALL GREEN.

## Question

The repo-map drift check reported every finding as informational and exited 0.
Should a home-repo standard keep that behaviour so membership stays a human
decision?

## Observation

PR #82 removed the curated `## Other Repos` section from `AGENTS.md` during a
root-documentation cleanup and labelled a four-row navigation table as the map.
The drift check still exited 0 because it parsed the deleted heading and found
no pointers. Three consumers silently saw an empty map: the drift checker, the
`home-swe-home` `add_repo` parser and the `mth-plugins` `add_repo` parser. This
was recorded in decision D-026.

The replacement check separates defects from ambiguity. A missing or empty map
section, or a clone URL that disagrees with the local `origin`, exits 1.
`missing-local` and `local-unmapped` remain informational because a checkout
may be absent, private or intentionally unmapped — workspace presence and map
membership answer different questions (see the earlier repo-map pilots).
`--informational` restores report-only behaviour for a deliberate transition.

The check remains read-only: it reports and fails, never edits the map. This
keeps claim C2's "reported read-only rather than silently repaired" intact
while removing the silent-success failure mode.

## Decision recorded locally

`agents-home/docs/WORKFLOWS.md` and the `factory-contract` bundle's
`repo-map-drift` procedure carry the tiered rule; decision D-026 records why
the canonical map lives in `AGENTS.md`.

## Unresolved questions

Whether other harnesses should treat the same findings identically, and
whether an upstream repository rename should be detectable without network
access, remain open.
