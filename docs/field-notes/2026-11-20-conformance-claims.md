# Checkable conformance claims without universal discovery claims

**Recorded:** 2026-11-20
**Label:** Pilot observation
**Evidence type:** Implementation of a claim table and a deterministic checker,
run locally and in this repository's CI.
**Status:** One workspace; the claim set is descriptive, not a protocol.
**Limitations:** The checker validates this repository's own evidence
discipline. It does not prove that any other harness discovers the same files,
and it does not validate claims about sibling repositories in a shallow CI
checkout.
**Reproduce:** `python3 scripts/check_evidence.py` from the repository root —
exit 0 with a count of notes, links and claims; the same command runs as the
required `Validate evidence` check in CI.

## Question

[Issue #11](https://github.com/magitech-ai/agents-home-pattern/issues/11)
asked what testable conformance claims could be made without implying that one
harness's discovery behaviour is universal.

## Decision

Claims are written in `CONFORMANCE.md` as past-tense statements about this
workspace, each carrying one label from the README vocabulary and a proof
target that resolves. A proof is either a relative Markdown link to a field
note or a `check: <path>` to a local script. The checker validates the table's
shape, labels and proof targets, so a claim cannot be added without evidence
that exists in the tree.

This answers the question without asserting that any harness must discover a
particular directory: the claims describe what was observed in the pilot, and
the field notes carry the harness, version and environment alongside each
observation.

## Recorded observations

- The claim table has seven rows; each proof resolves locally and in CI.
- The checker fails on a missing `**Label:**` header and on a label outside the
  controlled vocabulary (verified in a throwaway copy, not in the shipped
  tree).
- Renaming the required CI job blocked a merge until the original job name was
  restored; the workflow note now records that branch protection keys on the
  job name.

## Unresolved questions: none.
