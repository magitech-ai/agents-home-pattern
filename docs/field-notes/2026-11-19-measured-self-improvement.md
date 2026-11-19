# Measured self-improvement and multi-provider evidence

**Recorded:** 2026-11-19
**Evidence type:** Pilot observation with CI/test output and live A/B runs;
model behaviour is stochastic and single-user.
**Status:** Infrastructure is verified; the benefit claim is not established.

**Limitations:** Single user/machine/provider account; small self-authored task suite; checker bugs found repeatedly; no independent human review.

## Setup

`magecode` implements a Propose–Probe–Compose loop outside the agent as a
library (`improve.py`, `eval.py`, `library.py`, `utils/selection.py`). A candidate
harness is a copy of the editable data tree (`systemprompt.md`,
`tool_guidance.md`) selected with `MAGECODE_HARNESS_DIR`. `eval.HARD_TASKS` uses
outcome checkers over CLI transcripts. `compare_arms()` interleaves base and
candidate so provider rate limits and time drift affect both equally;
infrastructure errors (429, timeout) are excluded from the pass-rate
denominator rather than scored as task failures.

## Recorded observations

- An interleaved run under NVIDIA hit sustained HTTP 429: 34/36 trials were
  infrastructure errors, leaving too little data for a decision. The evaluator
  now reports such trials separately and paces calls.
- Gemini's OpenAI-compatible endpoint exposed only an encrypted
  `thought_signature`; readable `thought_summary` deltas required the native
  Interactions API. The client now defaults to native Interactions with
  stateful `previous_interaction_id` and translates all 8 documented event
  types and 24 delta types; unrecognised types are printed as `UNKNOWN:`.
- With the default Gemini hydrogen model at medium effort, base scored 18/18 on
  `HARD_TASKS`: at ceiling, so no candidate could beat it. New probe tasks were
  then constructed; several apparent failures were checker bugs, and after
  fixing them the base again saturated the tasks.
- A candidate that encoded a fact in its own prompt beat base by +0.2, but it
  was a synthetic canary, not a general capability gain. It was not adopted.
- Live tool workflows (repo lookup, verification, skill loading, shell
  commands, native thought-summary display) completed end to end under both
  providers.

## Implication for the pattern

The experiment demonstrates a negative result worth recording: **a
self-improvement loop can be fully instrumented and still have nothing to
adopt**. Evidence-driven development requires the harness to refuse adoption
in that case. The pattern's open question about what repeated independent
implementations would prove remains open; this note adds one implementation
and its negative measurement, not a validation of the approach.

## Limitations

- Single user, single machine, one provider account per model.
- Task suite is small and built by the same agent it evaluates; checker bugs
  were found repeatedly, so pass rates depend on checker quality.
- No independent human review of the candidate-adoption decision.