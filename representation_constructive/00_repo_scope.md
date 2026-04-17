# Repo Scope

## Plan Mode Note

- This pass started with a plan-only inventory, then moved into execution.
- The raw puzzle files are present locally, so execution proceeded without waiting for more input.

## Evidence Files For This Pass

These are the only files treated as primary evidence.

- `can u dig it.csv:1-14`
  - Primary raw grid source.
- `canudigitv1/can u dig it.csv:1-14`
  - Duplicate raw grid copy.
  - Used only as a consistency cross-check, not as an independent confirmation.

## Context-Only Files

These files may be read for prior conclusions, comparisons, or helper ideas, but not as proof.

- `README.md`
- `COLLABORATOR_HANDOFF.md`
- `HYPOTHESIS_LOG.md`
- `all_found_words.csv`
- `all_found_word_instances.csv`
- `canudig_output/`
- `canudigitv1/`
  - except the duplicate raw grid copy above
- `canudigitv2/`
- `independent_rethink/`

## Method Boundary

- Exact word instances and exact phrase instances only.
- No stripped content cores as evidence.
- No merges based only on shared lemmas or shared word types.
- Disconnected instances of the same word are penalized when a theory assigns them one semantic role.
- Phrases that only become plausible after deleting glue words like `or`, `in`, `to`, `into`, or `by` are penalized.
- No final integer will be forced if the exact evidence stays underdetermined.

## Helper Script Boundary

- New helper scripts for this pass live only under `representation_constructive/`.
- This pass does not import the older solver code directly.
- The new helper does reimplement the same generic low-level grid assumptions used elsewhere in the repo:
  - rectangular CSV grid
  - lowercase cell text matching
  - standard Boggle-style 8-neighbor adjacency
  - no cell reuse inside a single word path
  - no cell reuse across a chained multiword phrase path

## Target Question

- Determine whether a representation-first or representation-plus-place-value story can absorb more of the raw puzzle exactly, and more cleanly, than the older procedure-first story.
