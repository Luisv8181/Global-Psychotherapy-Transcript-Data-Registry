# Search Tooling: Query Planner

The deterministic planner in `src/registry/search_planner.py` helps research agents choose which discovery query to run next. It uses the existing registry and search log as a local baseline; it does not scrape websites, access gated resources, or change dataset records.

## Quick start

From the repository root:

```bash
PYTHONPATH=. python scripts/plan_search.py \
  --gap "German real-world psychotherapy dialogue" \
  --channel "institutional repositories" \
  --undercovered \
  --primary-source-likely 2 \
  --lineage-likely 1 \
  --query "Psychotherapie echte Beratungsgespräche Korpus Datensatz" \
  --json
```

Supply multiple `--query` arguments to rank a batch. The common flags give every query the same channel, gap, under-coverage, source-access expectation, and lineage expectation. Use `--proposals proposals.json` when candidates need different metadata. The JSON file is an array of objects:

```json
[
  {
    "query": "German psychotherapy corpus data availability",
    "gap_tokens": ["German", "real-world", "psychotherapy"],
    "channel": "institutional repositories",
    "undercovered": true,
    "primary_source_likely": 2,
    "lineage_likely": 1,
    "known_failure": false
  }
]
```

## How ranking works

Each query receives a deterministic score for gap fit, novelty against previously logged query wording, likely primary-source inspectability, lineage discovery potential, and coverage balance. Known failure and repetition penalties reduce score; a channel-dominance penalty nudges exploration toward alternative channels. Ties resolve by query text, so the result is reproducible.

The score is a transparent heuristic for allocating research effort. It is not a probability, relevance truth, quality rating, or verification status. Inspect source material and apply the repo's existing evidence and licensing rules independently.

## Duplicate review

`detect_duplicates` identifies candidate pairs that share normalized canonical URLs, DOI, IDs, or normalized titles. Pairs are review suggestions only. The tool must not automatically merge candidates: similarly titled resources may be distinct, and derivatives may deserve separate records with explicit lineage.

## Outcome reports

`summarize_search_outcomes` accepts a list of query outcome dictionaries with non-negative integer counts for `screened`, `unique_leads`, `primary_opened`, `scope_passed`, `blocked`, `duplicate_or_derivative`, and `out_of_scope`. It emits raw totals plus smoothed planning rates. Rates are only comparable when the screening effort and count definitions are comparable.

## Safety and limits

- It never reads transcript content or any licensed/gated corpus.
- It never alters, verifies, or assigns evidence status to canonical records.
- It relies on manually entered expectations; it does not yet learn calibrated probabilities from prior outcomes. Query overlap and title/URL/DOI matching are transparent review hints, not identity proofs.
- It parses the current Markdown log table. If the table format changes, update parser tests.
- Before any registry record is added, continue to follow `AGENTS.md`, especially primary-source checks, data-license verification, privacy/ethics review, and owner escalation rules.
