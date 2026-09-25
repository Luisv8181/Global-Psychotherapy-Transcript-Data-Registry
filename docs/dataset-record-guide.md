# Dataset Record Guide

Each file in `data/datasets/` represents one dataset or collection. The registry's unit of record is the **dataset**, not an individual transcript.

## Required fields

- `id`: stable lowercase identifier
- `title`: provider's published title
- `canonical_url`: authoritative landing page
- `status`: verification state
- `dataset_type`: real, synthetic, hybrid, or unknown

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
