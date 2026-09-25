# Dathive

## Working definition

**Dathive** is the name for an evidence-grounded research structure built from many specialized agents.

A database primarily stores structured records.

A knowledge graph primarily represents relationships.

A data lake primarily aggregates data.

A Dathive adds an active maintenance layer: agents continuously discover sources, verify claims, extract metadata, connect entities, detect gaps, audit provenance, and surface questions for human researchers.

The Dathive does not replace the underlying database, evidence store, or knowledge graph. It coordinates them.

## The first Dathive

This repository can serve as the first concrete Dathive implementation:

**Global Psychotherapy Transcript Dathive**

Its domain is psychotherapy and counseling dialogue resources.

Its job is not to collect therapy transcripts indiscriminately. Its job is to build an evidence-backed map of where those resources exist, what they contain, how they can be accessed, what restrictions apply, what research they support, and where the evidence is weak or missing.

## Core architecture

```text
                    DISTRIBUTED WORLD
                           |
          +----------------+----------------+
          |                |                |
       papers         repositories     institutions
          |                |                |
          +----------------+----------------+
                           |
                    DISCOVERY AGENTS
                           |
                    EVIDENCE CAPTURE
                           |
                    EXTRACTION AGENTS
                           |
                  +--------+--------+
                  |                 |
            CANONICAL RECORDS   EVIDENCE STORE
                  |                 |
                  +--------+--------+
                           |
                    VERIFICATION
                           |
                    LINKAGE / GRAPH
                           |
          +----------------+----------------+
          |                |                |
       SEARCH          TIMELINE        GAP MAP
          |                |                |
          +----------------+----------------+
                           |
                    HUMAN RESEARCHER
```

The key rule is that derived outputs never become more authoritative than the evidence-backed canonical record.

## Agent roles

### 1. Discovery Agent

Finds candidate datasets, papers, repositories, institutional pages, catalogs, and related resources.

Output:
- candidate URL
- candidate type
- discovery source
- query used
- date discovered
- confidence that the source is relevant

It does not declare a dataset verified.

### 2. Verification Agent

Checks candidate claims against authoritative sources.

Questions include:
- Does the dataset actually exist?
- Is it real, synthetic, or hybrid?
- Are transcripts available?
- What is the access model?
- What license is documented?
- Is redistribution permitted?
- What privacy/de-identification claims are actually documented?

Output:
- evidence citations
- field-level verification status
- contradictions
- unresolved questions

Human review remains authoritative for consequential interpretation.

### 3. Extraction Agent

Converts evidence into the canonical dataset schema.

It should extract rather than invent.

If a field is absent, it should return `unknown`, `not_reported`, or leave the field unresolved according to the schema.

### 4. Linkage Agent

Connects:
- datasets
- publications
- institutions
- repositories
- annotations
- therapy modalities
- languages
- countries/regions
- privacy methods
- derived datasets

The linkage layer turns a list into a research map.

### 5. Gap Analysis Agent

Looks for systematic absences.

Examples:
- languages with very little real-session data
- regions represented mostly by synthetic data
- modalities without longitudinal corpora
- datasets with transcripts but no documented privacy evaluation
- populations repeatedly missing from the public research landscape

A gap is an observation about registry coverage, not proof that data do not exist.

### 6. Privacy Audit Agent

Tracks what privacy information is documented.

It can flag:
- explicit PII-only de-identification
- missing contextual re-identification assessment
- unclear longitudinal linkage policy
- unclear consent or data-use conditions
- stylometric/privacy concerns not addressed by the source

It must never convert absence of evidence into a claim of privacy failure.

### 7. Provenance Audit Agent

Checks whether important claims have supporting evidence.

Example:

```text
"133 sessions"
       |
       +--> official dataset source
       |
       +--> publication
       |
       +--> verification date
```

Unsupported facts are downgraded or escalated.

### 8. Synthesis Agent

Creates research-facing summaries from verified records.

Examples:
- "Show longitudinal English and Spanish psychotherapy datasets."
- "Show resources with therapist-strategy annotations."
- "Show datasets whose raw transcripts are restricted but processed outputs are public."
- "Show where multilingual real-session evidence is sparse."

Synthesis must preserve uncertainty and provenance.

## The Dathive loop

```text
DISCOVER
   ↓
CAPTURE EVIDENCE
   ↓
EXTRACT
   ↓
RECONCILE
   ↓
VERIFY
   ↓
CONNECT
   ↓
AUDIT
   ↓
PUBLISH DERIVED VIEWS
   ↓
REVISIT WHEN SOURCES CHANGE
   ↺
```

This loop is what distinguishes the concept from a static dataset directory.

## What makes it different

A Dathive should be:

- **evidence-grounded** rather than hallucination-driven
- **provenance-aware** rather than citation-after-the-fact
- **multi-agent** rather than one general-purpose scraper
- **continuously revisable** rather than a frozen catalog
- **uncertainty-preserving** rather than forced-complete
- **domain-aware** rather than generic metadata collection
- **human-governed** rather than autonomous authority

## What it must not become

The Dathive should not become:
- a scraper that republishes restricted therapy transcripts
- an autonomous license lawyer
- an ethics/IRB authority
- a privacy-certification system
- a machine that silently converts guesses into facts
- a replacement for researchers or clinicians

## Long-term abstraction

The psychotherapy Dathive can become a template for other domains:

```text
DATHIVE
├── psychotherapy
├── rehabilitation
├── language + culture
├── medical research
├── AI privacy
└── other evidence-heavy domains
```

The domain-specific registry remains responsible for its own schema and governance.

## Design thesis

> **A database stores knowledge. A Dathive cultivates an evidence-grounded map of knowledge.**

The word is intentionally conceptual. It is not being presented here as an established technical standard.
