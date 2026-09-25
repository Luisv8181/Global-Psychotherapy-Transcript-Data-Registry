# Published Synthetic Therapy Corpus Layer

The registry treats published synthetic psychotherapy and counseling dialogue as a first-class research resource while keeping it distinct from real-session evidence.

## Scope

Records may cover fully synthetic dialogues, clinician roleplay, simulated counseling, LLM-generated therapy dialogue, translated or transformed synthetic dialogue, and hybrid corpora.

The source context should be recorded precisely rather than collapsing everything into one synthetic label.

## Historical lineage

The registry should treat the emergence of synthetic therapy data as a research history of its own.

At present, **CACTUS (2024)** is a strong early documented candidate for a publicly released, dedicated synthetic psychotherapy/counseling dialogue corpus. Lee et al. introduced CACTUS as a multi-turn CBT counseling dataset generated around designed client personas and systematic counselor application of CBT techniques, and made the data, model, and code publicly available.

This should **not** be recorded as a definitive claim that CACTUS was literally the first synthetic therapy transcript ever created. Earlier simulated, roleplay, mental-health, or therapeutic dialogues may exist outside the terminology and publication trail currently indexed by the registry.

The registry should therefore distinguish:

- **earliest verified candidate**: earliest resource the registry can currently support with primary evidence
- **first claimed by authors**: only when the source explicitly makes that claim and the scope is clear
- **historical predecessor**: earlier simulated or generated dialogue that is relevant but does not meet the same corpus definition
- **publication date** vs **generation date** vs **release date**

The historical record should be revisable as earlier primary evidence is discovered.

### Initial lineage

Early simulated/generated dialogue → CACTUS (2024) → modality-specific synthetic corpora → larger/multilingual synthetic corpora → synthetic-vs-real evaluation

This lineage is a research hypothesis and organizing model, not a claim that the field followed one single linear path.

## Provenance

Where documented, record:

- generation method
- model, software, or human process
- prompt or generation protocol
- human or expert review
- whether real data influenced generation
- language and cultural context
- therapy modality or simulated modality
- publication or project
- version or release
- license and redistribution terms
- intended research uses
- known limitations and validation gaps
- collection/generation date where available
- first public release date where available
- historical-status evidence and source

Unknown remains unknown.

## Synthetic is not equivalent to real

Synthetic data can support software testing, benchmark development, controlled experiments, rare-case simulation, multilingual experimentation, privacy research, annotation prototyping, and model evaluation.

Its usefulness depends on the research question and generation/validation process. Scale or accessibility should never be treated as evidence of clinical representativeness.

## Relationship to real-session corpora

The registry should distinguish:

- real therapy: observed human therapeutic interaction
- roleplay/simulation: human-created simulated interaction
- synthetic: machine- or process-generated interaction
- hybrid: multiple source contexts

Derived or translated corpora should retain links to their source resources.

## Publication model

A preferred provenance chain is:

publication/project → synthetic corpus → generation evidence → version → license → research uses

Where licensing permits, the project may eventually publish synthetic corpus artifacts. Restricted, copyrighted, or sensitive source material must not be copied into the repository simply to create a derivative corpus.

## Dathive responsibilities

Agents may discover published synthetic corpora, extract documented generation metadata, link publications and versions, compare characteristics, identify missing provenance, and maintain the historical lineage.

Agents should not infer that a corpus is synthetic solely from writing style, nor certify clinical validity, privacy, licensing, or ethical acceptability.

Human review remains authoritative for consequential classification and publication decisions.

## Research questions

The synthetic layer enables questions such as:

- What are the earliest verifiable examples of synthetic psychotherapy dialogue?
- Which modalities have substantial synthetic dialogue resources but limited real-session resources?
- Which languages have synthetic counseling data without corresponding real-session evidence?
- How often do published synthetic corpora document their generation process?
- Which corpora include expert validation?
- How does synthetic dialogue perform for a specific research task compared with real-session dialogue?
- Which gaps can synthetic data responsibly help fill, and which require human-session evidence?
- How has synthetic therapy generation changed across models, languages, modalities, and evaluation methods?

> **Synthetic therapy data is research infrastructure, not a substitute for evidence from human therapeutic interaction.**