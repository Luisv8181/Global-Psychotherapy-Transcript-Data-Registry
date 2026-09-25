# Dataset Record Guide

Each file in `data/datasets/` represents one dataset or collection. The registry's unit of record is the **dataset**, not an individual transcript.

## Required fields

- `id`: stable lowercase identifier
- `title`: provider's published title
- `canonical_url`: authoritative landing page
- `status`: verification state
- `dataset_type`: real, demonstration, dramatized, peer_support, synthetic, hybrid, or unknown (definitions in `data/vocabularies/dataset-type.yaml`)

## Dialogue structure

`dialogue_structure` records the shape of the text, separately from its provenance: `multi_turn`, `single_turn_qa`, `mixed`, or `unknown`. Single-turn counseling Q&A, such as a help-seeker's post with therapists' answers, is in scope. A real Q&A corpus is `dataset_type: real` with `dialogue_structure: single_turn_qa`.

## Evidence fields

Use `evidence.primary_sources` for the strongest authoritative source. Use `supporting_publications` for papers that describe or use the dataset.

## Access fields

Access describes how a researcher can obtain the dataset. Redistribution describes whether the researcher can redistribute the underlying material. They must not be collapsed into one field.

## Privacy fields

Record only what the evidence supports. A source saying a corpus was anonymized or de-identified should be recorded as a documented claim. Do not upgrade that claim into a guarantee of anonymity or resistance to re-identification.

## Longitudinal data

`longitudinal: true` should mean that repeated observations from the same participant or case are documented as part of the dataset design. If the source does not establish this, use `unknown` rather than inferring it from session counts.

## Counts

Counts are time-sensitive and source-dependent. Record published values with evidence when available. If different authoritative sources report different counts, preserve the discrepancy in `notes` rather than silently selecting one.
