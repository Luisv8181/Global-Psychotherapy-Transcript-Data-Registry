# Historical Analysis

## Purpose

The registry should support temporal analysis of psychotherapy data and computational therapeutic dialogue without turning a collection of datasets into an unsupported history of psychotherapy.

## Two related histories

The registry should distinguish two overlapping timelines:

1. **Observed psychotherapy evidence**: recorded human therapeutic interaction and associated datasets.
2. **Computational therapeutic dialogue**: systems that simulate, generate, or structure therapeutic-style interaction.

These timelines should be connected where evidence supports the relationship, but never collapsed into one category.

## Computational therapeutic dialogue timeline

### ELIZA: historical predecessor

ELIZA is an important historical predecessor for synthetic therapy research, but it should not be treated as a modern synthetic corpus. Joseph Weizenbaum's 1966 Communications of the ACM paper describes ELIZA as a program running on MIT's MAC time-sharing system that enabled natural-language conversation between a person and a computer. Its DOCTOR script simulated a Rogerian psychotherapist through keyword-triggered decomposition and response-reassembly rules.

Primary source:
- Weizenbaum, J. (1966), “ELIZA—a computer program for the study of natural language communication between man and machine,” Communications of the ACM, 9(1), 36–45. https://doi.org/10.1145/365153.365168

The historical object should be treated as versioned rather than singular. Archival reconstruction documents multiple ELIZA versions beginning in 1965, including the 1965a and 1965b versions, the 1966 CACM version, and later versions. The recovered archive also documents multiple contemporaneous DOCTOR scripts. These archival claims are useful for historical mapping, but the registry should preserve the distinction between the original surviving evidence and later reconstruction.

Archival source:
- Finding ELIZA, “The versions.” https://findingeliza.org/versions.html
- Finding ELIZA, “The DOCTOR script.” https://findingeliza.org/doctor.html

ELIZA therefore occupies the taxonomy position computational therapeutic dialogue system / historical predecessor, not synthetic in the modern corpus sense. Its human-machine interactions may be represented as historical dialogue artifacts when primary evidence supports the specific artifact.

### Later synthetic and simulated dialogue resources

The registry can now trace a documented modern progression from early rule-based therapeutic dialogue systems to published synthetic counseling corpora. Current examples include:

- **CACTUS (2024)**: a published synthetic psychotherapy corpus generated around CBT-oriented client personas and counselor behavior.
- **MusPsy (2026)**: multi-session counseling dialogues constructed from client profiles in publicly available psychological case reports. The dataset is longitudinal in design but is not observed therapy-session evidence.
- **StoryMI (2026)**: 6,000 simulated motivational-interviewing dialogues grounded in 1,000 questionnaire-story pairs, with explicit MI coding and multi-agent strategy control.
- **PhaseMI (2026)**: a phase-structured MI dataset generated with therapist, client and supervisor LLMs to control transitions across counseling phases.

These are not a single linear technological lineage. They represent different research designs: rule-based therapeutic simulation, persona-seeded longitudinal reconstruction/simulation, multi-agent MI generation, and phase-controlled MI generation.

## Historical claim policy

The registry should avoid unsupported "first" claims.

For historical priority, record:

- earliest verified candidate
- first claim made by authors, when applicable
- historical predecessor
- generation date
- collection/interactions date
- publication date
- public release date
- primary evidence supporting the classification

A historical lineage is revisable when earlier primary evidence is discovered.

## Time model

A dataset may have several distinct dates:

- collection_start_year
- collection_end_year
- publication_year
- release_year
- last_verified

For computational systems and synthetic corpora, add where available:

- generation_start_year
- generation_end_year
- first_public_release_year
- historical_status

Collection or interaction period is the primary temporal variable for studying observed clinical interaction.

## Historical metadata

Where evidence permits, records may describe historical period, therapy era, therapeutic school, modality, clinical setting, population, country/region, language, recording technology, transcription method, generation technology, synthetic-generation method, and historical significance.

## Methodological safeguards

Historical comparisons must account for sampling differences, modality composition, clinical population, country and cultural context, language and translation, recording/transcription technology, generation technology, changing diagnostic terminology, consent/privacy practices, unequal longitudinal availability, and publication/access bias.

A pattern in the registry is evidence about indexed resources, not automatically about psychotherapy or computational therapy as a whole.

## Future views

- computational-therapy timeline
- synthetic-corpus timeline
- real-vs-synthetic evidence timeline
- modality-by-era matrix
- language-by-era matrix
- historical coverage heatmap
- therapy-school evidence graph
- dataset-to-publication timeline
- privacy-method timeline
- generation-method timeline

The registry should store evidence first and generate these views second.
