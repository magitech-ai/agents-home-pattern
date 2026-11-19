# Evidence workflow

One loop, driven by GitHub, usable by a human or an autonomous agent. The
canonical record stays in this repository; GitHub supplies the queue, the
state transitions and the proof links.

```
open question / claim → pilot issue → evidence PR → CI gate → close with proof
```

## 1. Queue

Each unit of work is an issue created from `.github/ISSUE_TEMPLATE/`. Pick the
matching label from the four evidence labels; the vocabulary is fixed so an
agent can query the frontier deterministically:

```sh
gh issue list --label "Open question" --state open --json number,title
```

Every issue body states **Done when** — the observable condition that closes
it. An issue without that criterion is not startable. External questions and
feedback go to Discussions; promote a discussion into an issue only when it
becomes a concrete pilot.

## 2. Pilot

Run the pilot in one harness and one environment. Record the harness version,
the exact steps and the limitations in the issue. Never generalise one setup's
behaviour to all users. Tools are harness-agnostic by construction: `gh`,
`git` and `python3 scripts/check_evidence.py` are the only required commands.

## 3. Evidence PR

Turn the result into a field note under `docs/field-notes/` and link it from
`README.md`. Add or update a row in `CONFORMANCE.md` only for observed or
documented behaviour. Every PR links its source issue and CI run.

## 4. Gate

`python3 scripts/check_evidence.py` runs in CI as the required check named
**Validate evidence** and locally before every PR. It validates note headers,
the controlled label vocabulary, local links, forward-looking Reproduce blocks
and claim proofs. The check name is part of branch protection: **never rename
the job**, only its step labels. A rename makes required checks unsatisfiable.

## 5. Close

Post a comment on the source issue containing the proof link (note and green
CI run), then close it. An issue closed without a proof comment is unfinished.
If the pilot fails to establish the claim, close it with the negative result
recorded — a negative result is evidence too.

## Unresolved questions: none.
