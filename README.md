# Global Psychotherapy Transcript Data Registry

> A research-grade, machine-readable map of psychotherapy and counseling dialogue datasets.

**Discover the data landscape without redistributing sensitive or restricted therapy data.**

The registry records where psychotherapy dialogue datasets exist, what they contain, who can access them, what licenses and redistribution conditions apply, what privacy/de-identification information is documented, and which research tasks the datasets support.

## Why this exists

Psychotherapy dialogue data is unusually difficult to discover systematically. Relevant corpora are distributed across open repositories, institutional archives, commercial databases, university projects, controlled-access programs, supplementary materials, and papers describing datasets that are not directly downloadable.

This project is intended to become a dedicated, evidence-backed registry for psychotherapy transcript corpora with access, licensing, privacy, longitudinal structure, therapy modality, annotation, and research-use metadata.

## What the registry stores

| Area | Examples |
|---|---|
| Identity | title, ID, canonical source, DOI |
| Data type | real, synthetic, hybrid |
| Dialogue | transcript, audio, video |
| Therapy | modality, setting, intervention |
| Population | age group, population, country/region |
| Language | language, dialect, multilingual status |
| Structure | sessions, participants, longitudinal design |
| Clinical scope | conditions, concerns, topics |
| Annotation | therapist/client labels, outcomes, turns, emotions |
| Access | open, registration, institutional, restricted |
| License | license type, research/commercial terms |
| Redistribution | allowed, prohibited, conditional, unknown |
| Privacy | de-identification, privacy evaluation, known limitations |
| Ethics | consent, ethics/IRB information, data-use requirements |
| Evidence | official sources, DOI, publications |
| Verification | status and date last checked |

Unknown information stays unknown. The registry does not infer missing facts.

## Critical distinction

**Publicly discoverable does not mean freely redistributable.**

The registry deliberately separates access, license, redistribution rights, research-use restrictions, and commercial-use restrictions. A restricted or copyrighted corpus may have a complete registry record without any transcript being stored here.

## Registry principles

1. **Metadata first.** The registry maps datasets; it does not become a mirror of sensitive psychotherapy data.
2. **Primary evidence.** Prefer dataset owners, publishers, institutional repositories, DOI records, and original papers.
3. **No false certainty.** Unknown is a valid value.
4. **Verification is time-bounded.** Access and licensing can change.
5. **Privacy claims require evidence.** A documented de-identification claim is not treated as proof of anonymity.
6. **Research discovery is not ethical approval.** Users remain responsible for their own ethics, consent, data-use, and legal requirements.
7. **Original sources remain authoritative.** Always check the provider's current terms before obtaining or using a dataset.

## Current records

The registry now includes verified or provisionally verified real-session resources spanning North America, Europe, and Asia:

- **Counseling and Psychotherapy Transcripts**, an institutional/licensed collection of real psychotherapy and counseling transcripts.
- **AVATAR Therapy Dialogue Corpus**, a specialized therapy dialogue corpus.
- **HOPE**, 212 real counseling conversations from publicly available counseling videos, with dialogue-act annotations and controlled research access.
- **CUEMPATHY**, 156 actual counseling sessions involving 39 therapist-client dyads, with speech, transcripts, and ratings.
- **BiMISC**, bilingual English-Dutch motivational-interviewing conversations sourced from real counseling sessions.
- **Mental Health Counseling Dialogue**, 1,661 Korean counseling-session transcripts collected at accredited mental-health counseling centers.
- **Online Mental Health Counseling Dataset (Westlake/Zhejiang University)**, a large-scale text-based counseling resource collected over two years from an online welfare counseling platform.
- **MindDialog**, a 2026 corpus built from more than 325 hours of publicly available psychotherapy demonstration videos featuring real therapists; it remains provisionally verified because the distinction between clinical encounters and educational demonstrations requires further provenance review.

Two resources are deliberately kept out of the real-session population:

- **AnnoMI** is excluded because its repository describes the 133 transcripts as *demonstrations* of high- and low-quality motivational interviewing, not naturally occurring clinical encounters.
- **IndieMH** is recorded as hybrid, because its LREC 2026 paper describes counseling conversations from publicly available sources that were manually *translated* into code-mixed Hinglish. They are not original Hinglish sessions.

These are seed records. The goal is substantially broader coverage. Leads that are found but not yet verified are tracked in `docs/candidate-queue.md`.

## Registry functions

The registry is designed to support multiple functions from the same evidence-backed records:

- dataset discovery
- historical and temporal mapping
- therapy-modality research
- longitudinal research
- clinical-process research
- cultural and linguistic research
- privacy and de-identification research
- AI benchmark discovery
- research-gap mapping
- therapy-knowledge evolution
- provenance-aware systematic review and meta-research

See `docs/functions.md`, `docs/historical-analysis.md`, and `docs/research-functions.md`.

## Search vision

The registry should eventually support queries such as:

> Find real psychotherapy datasets with longitudinal sessions, at least 100 sessions, English or Spanish dialogue, and research access.

> Find datasets containing therapist-client turn annotations and emotion labels.

> Find psychotherapy corpora where raw transcripts are restricted but processed or derived data are publicly available.

> Find datasets with documented de-identification methods and known privacy evaluations.

> Find multilingual or culturally specific psychotherapy dialogue resources.

## Research infrastructure vision

The registry is intentionally more than a static list.

**Registry → Dataset → Evidence → Publications → Annotations → Access → Privacy → Research tasks**

This can support dataset discovery, systematic reviews, evidence mapping, corpus comparison, research-gap analysis, privacy-method comparison, longitudinal-data discovery, clinical NLP benchmarking, and meta-research on psychotherapy datasets.

## Data model

Canonical records live under `data/datasets/`.
The video catalog lives under `data/videos/` (see `docs/video-catalog.md`).
The schema is maintained under `schema/`.
Controlled vocabularies live under `data/vocabularies/`.
Methodology and governance documentation lives under `docs/`.
Validation and automation live under `src/`, `scripts/`, `tests/`, and `.github/`.

### Running the checks

```bash
pip install -r requirements-dev.txt
PYTHONPATH=. python scripts/validate_registry.py   # schema, identity, evidence, dates
PYTHONPATH=. python -m pytest -q                   # tests
PYTHONPATH=. python scripts/audit_registry.py      # which core fields each record has not yet established
PYTHONPATH=. python scripts/build_site.py          # site/data/*.json for the Pages site
```

Validation **errors** block merges and deployment: unreadable YAML, schema violations, an `id` that does not match its file name, duplicate IDs or canonical URLs, `access.level` or `redistribution` values outside `data/vocabularies/access.yaml`, and `verified`/`partially-verified` records without primary sources or a `last_verified` date. **Warnings** are for a human reviewer: verification dates older than a year, and licenses marked verified without a `license.source` saying where the dataset's own license was read.

The audit lists evidence gaps, not dataset defects: an unestablished field means the reviewed sources have not documented it yet. The same view is published on the site under *Research views → Evidence gaps*.

## Dataset types and Q&A

Each record separates **provenance** (`dataset_type`) from **shape** (`dialogue_structure`):

| `dataset_type` | Meaning |
|---|---|
| `real` | Naturally occurring sessions, or real help-seekers' questions answered by practitioners |
| `demonstration` | Sessions made to teach a method, usually with actors or trainees as clients |
| `peer_support` | Non-clinicians supporting help-seekers, such as crowdsourced emotional-support chats |
| `synthetic` | Generated by a model, with no human session behind each dialogue |
| `hybrid` | Derived from human material by translation, LLM expansion, paraphrase or reconstruction |

`dialogue_structure` is `multi_turn`, `single_turn_qa` or `mixed`. Single-turn counseling Q&A, such as PsyQA and Counsel Chat, is in scope.

## Video catalog

Many corpora are transcribed from public therapy videos. `data/videos/` lists those videos, with metadata and links only, and records which datasets use each one. That makes shared source material across corpora visible. It currently holds the 119 source videos behind AnnoMI. See `docs/video-catalog.md` for scope and the rules for videos showing real clients.

## Published synthetic therapy corpora

Synthetic psychotherapy and counseling dialogue is a first-class part of the registry, while remaining explicitly distinct from real-session corpora. Records can document generation method, source basis, publication, version, license, intended uses, validation, and known limitations.

Where licensing permits, a future release may also publish synthetic corpus artifacts. Synthetic does not automatically mean clinically representative, privacy-safe, unbiased, or suitable for a particular research question.

See `docs/synthetic-corpora.md`.

## Dathive architecture

This registry is also the first concrete implementation of the **Dathive** concept: an evidence-grounded research structure maintained through specialized discovery, verification, extraction, linkage, audit, and synthesis agents.

A Dathive is not just another database or knowledge graph. The database stores canonical records; the evidence layer preserves provenance; the agents maintain and interrogate the map; humans retain authority over verification, ethics, licensing, privacy, and consequential research decisions.

The psychotherapy Dathive is defined in `dathive.yaml`, with the architecture in `docs/dathive.md`, the agent protocol in `docs/dathive-agent-model.md`, and the machine-readable task contract in `schema/dathive-task.schema.json`.

The first design principle is simple:

> **A database stores knowledge. A Dathive cultivates an evidence-grounded map of knowledge.**

The term is intentionally conceptual and is not presented as an established technical standard.

## Contributing

Submit **metadata and official links**, not restricted transcripts. If a dataset is controlled, copyrighted, or otherwise unavailable for redistribution, record its access pathway and restrictions rather than copying the data.

See `AGENTS.md` (the protocol for AI agents working in this repository), `CONTRIBUTING.md`, `docs/verification-protocol.md`, `docs/access-taxonomy.md`, `docs/ethics-and-governance.md`, and `docs/project-charter.md`.

## Safety and privacy

Do not submit therapy transcripts, PHI, participant identifiers, therapy recordings, credentials, access tokens, or private data obtained under a data-use agreement.

See `SECURITY.md`.

## Status

**Early research infrastructure.** The registry is not a certification authority, privacy certification, legal opinion, IRB determination, or guarantee that a listed dataset remains available under the recorded terms.

## License

Registry software and original metadata are released under the repository's MIT license unless a file states otherwise. Third-party dataset names, descriptions, publications, and linked resources remain subject to their original rights and terms.
