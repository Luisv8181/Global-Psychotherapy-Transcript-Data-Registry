# Roadmap

## Phase 1: Registry foundation
- [x] Repository structure
- [x] Machine-readable dataset records
- [x] Access and redistribution taxonomy
- [x] Verification protocol
- [x] Ethics and privacy guardrails
- [x] Automated validation
- [x] Seed datasets

## Phase 2: Coverage
- [ ] Expand dataset discovery across languages and regions
- [ ] Add psychotherapy modality taxonomy
- [ ] Add population and clinical-topic vocabularies
- [ ] Record longitudinal structure consistently
- [ ] Link datasets to publications and benchmark tasks
- [ ] Add dataset change history

## Phase 3: Evidence graph
- [ ] Dataset-to-publication relationships
- [ ] Dataset-to-annotation relationships
- [ ] Dataset-to-access-provider relationships
- [ ] Privacy/de-identification evidence records
- [ ] Derived and processed-data relationships

## Phase 4: Published synthetic corpus infrastructure
- [ ] Add explicit synthetic-corpus metadata and validation rules
- [ ] Track generation method, source basis, model/tooling, human review, and limitations
- [ ] Track versions and publication lineage
- [ ] Add license-aware publication/distribution checks
- [x] Establish a dedicated published-synthetic-corpus collection
- [x] Define historical lineage and predecessor taxonomy
- [ ] Add historical computational-therapy records beginning with ELIZA
- [ ] Add historical-status evidence fields to the canonical schema

## Phase 5: Research tooling
- [ ] Registry search CLI
- [ ] Structured filtering
- [ ] Dataset comparison reports
- [ ] Research-gap analysis
- [ ] Export to CSV/JSON/JSON-LD
- [ ] API or static query service

## Phase 6: Community infrastructure
- [ ] Maintainer review workflow
- [ ] Automated URL/link checks
- [ ] Scheduled metadata refresh
- [ ] Contributor provenance
- [ ] Dataset owner correction requests

## Multi-function infrastructure direction

The roadmap now treats discovery, historical mapping, modality research, longitudinal research, clinical-process research, cultural/linguistic research, privacy research, AI evaluation, research-gap mapping, and therapy-knowledge evolution as first-class registry functions.

Temporal metadata and evidence provenance are foundational dependencies for these functions.
## Privacy and metadata-linkage safety

The registry is metadata-only, but metadata can become identifying through aggregation and external linkage. The long-term design must therefore treat re-identification risk as a property of the **map and its relationships**, not only of the underlying datasets.

- [ ] Define a metadata-linkage risk framework for registry records
- [ ] Distinguish dataset-level metadata from session-level and participant-level metadata
- [ ] Document a minimum-necessary-metadata principle for sensitive clinical resources
- [ ] Add review guidance for combinations that could create a mosaic/linkage risk (for example institution + dates + geography + unusual population + source media)
- [ ] Audit dataset-to-publication, source-video, derived-corpus, institution, and geography links for unnecessary identity amplification
- [ ] Define when granular metadata should remain unknown, be generalized, or be omitted
- [ ] Add automated checks for prohibited direct identifiers and high-risk metadata patterns where practical
- [ ] Develop a privacy/linkage-risk audit that complements, rather than replaces, source-level de-identification evidence
- [ ] Document that public discoverability does not establish low re-identification risk
- [ ] Explore the registry itself as a research testbed for metadata mosaic risk and privacy-preserving dataset discovery

Design principle: **make the research landscape more discoverable without making individual clinical participants more discoverable.**
