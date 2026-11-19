# Repo Map Drift Check Pilot

**Recorded:** 2026-11-17
**Evidence type:** Pilot observation from a read-only script run in the
Magitech workspace
**Status:** One workspace snapshot; the script reports differences, not truth

**Limitations:** One workspace snapshot; the script reports differences, not truth; shallow scheme/path checks.

## Setup exercised

`agents-home/scripts/check_repo_map.py` was run against the curated
"Other Repos" pointers in `agents-home/AGENTS.md` and the sibling git
checkouts under the same parent directory. The script:

- joins wrapped markdown list lines so each pointer is parsed once
- reads a local path from either a backticked path or a markdown link target
- reads an optional clone URL from angle brackets
- compares each mapped clone URL with the local checkout's `origin`, after
  normalizing scheme, `git@host:path` form, `.git`, and case
- lists local git checkouts that have no map pointer
- excludes the home repo itself from that list
- never edits the map; exits 0 with an informational report

Eight unit tests cover both path formats, URL normalization, missing-local
entries, URL mismatches, unmapped local repos, no-drift, and report wording.

## Recorded output

At the time of the run the script reported one finding:

```
[local-unmapped] magecode: local checkout at .../magecode, no map pointer
(may be intentionally pending publication)
```

There were no `missing-local` or `url-mismatch` findings at that snapshot.
`magecode` was a substantial local repo created during the session but not
yet published, matching the user's stated reason for omitting it.

## What this pilot suggests

- The read-only drift-report approach (candidate approach 2 in the
  [repository map maintenance pilot](2026-11-repository-map-maintenance.md))
  is practical to implement with the tools already present: markdown parsing,
  `git remote get-url`, and no network access.
- The three categories answer different questions. `url-mismatch` is the
  clearest signal of actionable drift; `missing-local` and `local-unmapped`
  are ambiguous without human context — a local-only repo can be
  intentionally unpublished, and a mapped repo may be read without a local
  checkout. Treating all findings as errors would be wrong.
- The report's value is surfacing differences for a human, not deciding
  membership. This matches the earlier pilot's conclusion that workspace
  presence, git remotes, and organization membership each answer a different
  question.

## Limitations

- The comparison uses only local remotes and the curated map. It does not
  query GitHub, so it cannot detect renamed/deleted remote repos, transferred
  ownership visible only upstream, or map entries whose remote changed while
  the local checkout is stale.
- Normalization is deliberately shallow (scheme, `.git`, `git@` form, case).
  SSH/HTTPS credential variants beyond that are not handled.
- The script reads `AGENTS.md` format assumptions (a `## Other Repos` heading
  and `- **name**` bullets). A different map layout would need parser changes.
- One workspace and one run. Repeated runs over time would be needed to know
  whether the report is noisy or useful in practice.