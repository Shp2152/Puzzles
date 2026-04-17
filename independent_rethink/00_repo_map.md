# Repo Map

## Scope Boundary

This audit uses a strict quarantine boundary.

- Blind phase evidence source: `can u dig it.csv:1-14`
- Duplicate raw grid copy: `canudigitv1/can u dig it.csv:1-14`
- Prior-attempt files are not treated as evidence before `05_compare_to_existing_attempt.md`.

Contamination note:

- During the initial plan-only inventory, I read `README.md:1-120` and `COLLABORATOR_HANDOFF.md:1-114` only to classify repo contents.
- Those files are therefore quarantined as prior-analysis artifacts and are not used as evidence in the blind reconstruction.

## Raw Puzzle Sources

These are the only files treated as raw source material for the blind pass.

- `can u dig it.csv`
  - 14x14 letter grid with one hyphen cell at `G14`; see `can u dig it.csv:14`.
- `canudigitv1/can u dig it.csv`
  - Duplicate copy of the same grid; same content as the root CSV.

## Prior-Analysis Artifacts

These files reflect earlier solving attempts, derived outputs, or hypothesis summaries. They are intentionally excluded from steps 2-5.

- `README.md`
- `COLLABORATOR_HANDOFF.md`
- `HYPOTHESIS_LOG.md`
- `all_found_words.csv`
- `all_found_word_instances.csv`
- `canudig_output/`
  - `found_word_instances.csv`
  - `exact_bigrams.csv`
  - `exact_trigrams.csv`
  - `top_phrases.csv`
  - `top_phrases.txt`
  - `found_words_grouped.txt`
- `canudigitv1/top_phrase_candidates.txt`
- `canudigitv1/top_phrase_candidates_baseten.txt`
- `canudigitv1/top_phrase_candidates_hexadecimal.txt`
- `canudigitv1/chemistry_found_words.csv`
- `canudigitv1/chemistry_term_check.csv`
- `canudigitv1/attachment_experiments/`
- `canudigitv1/operation_experiments/`

## Helper / Solver Code

These files are code, not evidence.

- `canudigitv1/canudig_search.py`
  - Active solver architecture with embedded candidate vocabulary, bridge-word expansion, role tags, and phrase scoring.
  - Hypothesis-heavy and therefore not reused in the blind pass.
- `canudigitv2/canudig_solverv2.py`
  - Retired exact-search branch.
  - Contains generic helpers such as `load_grid`, `coord`, `path_to_coord_string`, and `build_neighbors` at `canudigitv2/canudig_solverv2.py:128-171`.
  - Those helpers only assume a rectangular CSV grid and Boggle-style 8-neighbor adjacency.

## Independent Workspace

All new audit artifacts and helper code for this pass live under `independent_rethink/`.

- `00_repo_map.md`
- `01_blind_reconstruction.md`
- `02_exact_phrase_inventory.md`
- `03_instance_graph.md`
- `04_hypothesis_test.md`
- `05_compare_to_existing_attempt.md`
- `06_candidate_integers.md`
- helper scripts created for this audit
