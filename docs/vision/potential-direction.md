# Potential Direction

**Status:** Exploratory vision document

This document captures possible future directions for the Global Psychotherapy Transcript Data Registry. It is intentionally exploratory and does not make every idea here a committed roadmap requirement.

## 1. Central direction

The Registry should evolve from a dataset list into a **versioned, evidence-grounded research instrument for studying the psychotherapy-data landscape**.

The core product is not a collection of transcripts. It is structured evidence about where psychotherapy and counseling dialogue resources exist, what those resources actually represent, how they were produced, how they can be accessed, what rights and restrictions apply, what privacy information is documented, and how confidently each claim can be established.

A useful description is:

> The Global Psychotherapy Transcript Data Registry is an evidence-grounded, continuously maintainable map of psychotherapy dialogue research, where datasets are only the starting point and provenance, relationships, uncertainty, and historical context are first-class data.

The project should avoid claiming that it contains all psychotherapy data or that it proves a dataset does not exist. Its stronger and more defensible claim is that it documents **what can currently be established about the landscape from the sources and search procedures recorded by the Registry**.

## 2. What is already working

### Provenance taxonomy

The source taxonomy is one of the Registry's most important contributions:

- real
- demonstration
- peer support
- hybrid
- synthetic
- dramatized
- unknown

This is not merely organizational. Provenance changes what a corpus can legitimately support.

A transcript that resembles clinical therapy is not automatically evidence of a naturally occurring therapeutic encounter. Demonstrations, role-play, reconstructed dialogues, translated corpora, LLM-expanded material, and fully synthetic dialogues need to remain distinguishable from observed human therapeutic interaction.

Recent corrections to AnnoMI, HOPE, HighQuality, MindDialog, IndieMH, and other records demonstrate why this distinction matters.

### Unknown is a legitimate result

The Registry should continue to expose its own uncertainty.

A missing value can mean that the reviewed primary sources did not establish the fact. That is different from the fact being false.

Unknown provenance, unknown longitudinal structure, unknown redistribution rights, unknown license, and inaccessible sources are useful research information rather than defects to hide.

### Evidence-backed correction

The Registry should treat correction as a feature.

A growing Registry should not merely accumulate records. It should become more accurate as new evidence is reviewed.

An earlier classification must be revisable when stronger primary evidence changes what can be established.

> A fast, confident, wrong record does more harm than a missing one.

## 3. Make evidence provenance explicit

A future evidence model should distinguish at least three levels of claims.

### Author-reported claim

Example: The dataset authors report that direct identifiers were removed.

This records what the source says.

### Registry verification

Example: The Registry confirmed that the dataset documentation makes this claim.

This means the Registry actually inspected the source.

### Independent evaluation

Example: An independent publication evaluated re-identification risk.

This is evidence beyond the dataset owner's own assertion.

These should not be collapsed into one field called "verified."

The Registry is not a privacy-certification authority. It should document evidence about privacy and de-identification without converting an author's claim into an independent guarantee.

The same principle can apply to provenance, licensing, access, clinical characteristics, and other consequential claims.

## 4. Licensing, access, and redistribution remain separate

The Registry should make it easy to answer four different questions:

1. Does the dataset exist?
2. Can I access it?
3. What license or terms govern it?
4. Can I redistribute what I obtain?

These are not interchangeable.

Public discoverability does not establish free access. Access does not establish redistribution permission. An article license does not necessarily license the dataset. A code repository license does not necessarily license the data.

Future interfaces should make these distinctions highly visible rather than burying them in prose.

## 5. Verification freshness

The existing last-verified concept should become increasingly important as the collection grows.

Dataset pages and future search interfaces could make freshness visible so researchers can distinguish recently verified information, older verification, information that has not been recently rechecked, and claims whose original source is currently inaccessible.

This matters because datasets can change versions, licenses, access procedures, URLs, or availability.

A future historical model should preserve previous states rather than simply overwriting them.

## 6. Search and filtering

As the Registry grows, discovery should become structured rather than requiring researchers to open every dossier.

Potential filters include:

- provenance / dataset type
- language
- geography
- therapy modality
- dialogue structure
- session count
- longitudinal structure
- annotation types
- audio / video / transcript availability
- access level
- license status
- redistribution status
- privacy/de-identification evidence
- publication year
- release year
- historical period
- synthetic generation method
- source lineage
- verification freshness

The goal is not merely to make browsing prettier. The goal is to let a researcher ask a reproducible question against the evidence model.

## 7. Research characteristics before subjective suitability scores

A possible future layer is task-oriented discovery.

However, the Registry should be cautious about labels such as "best dataset for cultural research" or "suitable for therapy modeling." Those can turn contextual research judgments into seemingly objective classifications.

A safer direction is to expose underlying research characteristics:

- therapist/client turn labels
- emotion annotations
- outcome annotations
- cultural metadata
- language metadata
- dialect information
- longitudinal structure
- timestamps
- audio
- clinical topic labels
- psychotherapy modality
- de-identification documentation
- privacy evaluation
- source-video provenance
- expert annotation

A future research-task matcher could then explain why a dataset matches a task.

For example:

> Matched because the dataset contains therapist/client turn annotations, emotion labels, and longitudinal session structure.

The Registry should show evidence rather than declare a universal judgment about what a dataset is "good for."

## 8. Relationships and lineage

The Registry should increasingly represent relationships among resources rather than treating every dataset as an isolated record.

Potential relationships include:

- dataset to publication
- dataset to source video
- dataset to annotation scheme
- dataset to access provider
- dataset to derived dataset
- dataset to translated dataset
- dataset to reconstructed dataset
- dataset to synthetic derivative
- dataset to benchmark
- dataset to privacy/de-identification study
- dataset to predecessor or historical system

This is where the evidence graph and Dathive architecture become particularly valuable.

A derived corpus should retain a visible relationship to the material from which it was derived.

## 9. Historical research infrastructure

The historical layer should continue beyond modern datasets.

The Registry can eventually document the evolution of computational therapeutic dialogue:

> early therapeutic dialogue systems → human-machine therapeutic interactions → role-play and demonstration corpora → machine-generated synthetic dialogue → modern research corpora and derived datasets

ELIZA is an important historical predecessor, but the Registry should avoid presenting this as a simplistic single-line history.

Historical records should distinguish:

- generation date
- publication date
- public release date
- version history
- historical significance
- what was actually documented at the time
- later interpretations of the system

The goal is to make the evolution of computational therapeutic dialogue research traceable.

## 10. Coverage gaps as research findings

One of the most useful outputs of the Registry may eventually be evidence-backed descriptions of what researchers could not find.

However, the Registry should not claim:

> No dataset exists.

unless that proposition can genuinely be established.

A defensible formulation is:

> We did not identify a dataset meeting these criteria within the sources and search procedures documented by the Registry as of [date].

This distinction should be built into research-gap tooling.

A research gap is therefore not simply an empty search result. It is a documented result of a defined search and evidence process.

## 11. Versioned and citable research artifact

A long-term direction is to make the Registry itself a citable research artifact.

Potential future infrastructure includes:

- versioned releases
- archival snapshots
- DOI-backed releases
- reproducible registry statistics
- changelogs
- release-specific dataset counts
- historical comparison between Registry versions
- a formal survey or meta-research publication

A future paper could describe the Registry methodology and report the state of the psychotherapy-data landscape at a specific point in time.

The important property is reproducibility.

Someone should be able to cite a Registry version and understand what the Registry knew, what it did not know, and what evidence supported its records at that time.

## 12. Possible future research paper

A mature Registry could support a paper such as:

> **Mapping the Psychotherapy Dialogue Data Landscape: Provenance, Access, Licensing, Privacy, and Research Structure**

The paper would not need to claim that the Registry is exhaustive.

Instead, it could describe:

- search methodology
- inclusion and exclusion criteria
- provenance taxonomy
- evidence protocol
- access and licensing taxonomy
- privacy-evidence model
- historical model
- dataset relationships
- observed coverage gaps
- limitations and uncertainty

The Registry would remain the living research artifact, while the paper would document the methodology and a particular snapshot.

## 13. Dathive as the maintenance architecture

The Dathive concept may become most valuable as the Registry grows.

The database stores canonical records.

The evidence layer stores provenance.

Specialized processes can discover, verify, extract, link, audit, and synthesize information.

Humans retain authority over consequential interpretation.

The distinction is:

> A database stores knowledge. A Dathive cultivates an evidence-grounded map of knowledge.

The Dathive should therefore be judged by whether it improves evidence quality, traceability, coverage analysis, and maintenance rather than by how many agents or automated actions it contains.

## 14. What not to rush

These ideas should remain deliberately out of scope until the evidence foundation is mature:

- dataset scoring or rankings
- "best dataset" labels
- broad subjective suitability scores
- privacy certification
- clinical validity certification
- ethical or IRB certification
- claims of complete global coverage
- large taxonomies created before there is evidence that they are useful
- automated provenance classification based on transcript style alone

The Registry should resist becoming an authority that makes decisions researchers should make themselves.

## 15. Potential development sequence

### Near term

Strengthen the existing evidence model:

- explicit claim provenance
- clearer author-reported versus Registry-verified distinctions
- stronger license/access/redistribution visibility
- verification freshness
- continued provenance correction
- better evidence audits

### Medium term

Make the evidence navigable:

- structured filters
- relationship and lineage graph
- historical versioning
- research-characteristic search
- source-video relationship views
- research-gap maps

### Later

Make the Registry a durable research artifact:

- versioned releases
- archival snapshots
- DOI
- reproducible statistics
- formal methodology paper
- machine-readable exports
- broader Dathive maintenance infrastructure

## 16. Guiding principle

The Registry should not try to look complete.

It should try to be **trustworthy about what it knows, transparent about what it does not know, and useful for discovering what should be investigated next.**

That is potentially the strongest long-term identity for the project.
