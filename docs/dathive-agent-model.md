# Dathive Agent Model

This document defines the first agent protocol for the psychotherapy Dathive.

## Principle

Agents should have narrow jobs.

The system should prefer several verifiable transformations over one agent being asked to browse, interpret, verify, write, and publish a dataset record in one step.

## Agent pipeline

```text
Discovery
   ↓
Candidate
   ↓
Evidence Capture
   ↓
Extraction
   ↓
Reconciliation
   ↓
Verification
   ↓
Linkage
   ↓
Audit
   ↓
Human Review
   ↓
Canonical Record
```

## Shared task envelope

Each agent task should eventually carry:

```yaml
task_id: unique-task-id
agent_role: discovery
input:
  source_url: https://example.org
  query: psychotherapy transcript dataset
evidence:
  - source_url: https://example.org
    retrieved_at: 2026-09-24
    locator: page-or-section
output:
  claims: []
  unresolved: []
  proposed_changes: []
confidence: unknown
requires_human_review: true
provenance:
  parent_task: null
```

The exact implementation can evolve. The important invariant is that every transformation retains provenance.

## Agent contracts

### Discovery

Allowed:
- search public sources
- identify candidates
- record discovery evidence

Not allowed:
- mark a candidate verified
- infer license permissions

### Verification

Allowed:
- compare claims with authoritative sources
- identify contradictions
- assign field-level verification state

Not allowed:
- silently resolve material contradictions
- infer missing legal permissions

### Extraction

Allowed:
- map supported facts into schema fields

Not allowed:
- fabricate values to complete a record

### Linkage

Allowed:
- propose relationships supported by evidence

Not allowed:
- merge datasets solely because names look similar

### Gap analysis

Allowed:
- compute coverage gaps from registry contents

Not allowed:
- claim that an absent resource does not exist globally

### Privacy audit

Allowed:
- classify documented privacy methods and unknowns
- flag missing threat-model dimensions

Not allowed:
- certify anonymity or regulatory compliance

### Synthesis

Allowed:
- answer research queries from verified records
- preserve uncertainty
- link claims to evidence

Not allowed:
- suppress contradictory evidence for a cleaner narrative

## Consensus model

For high-impact fields, the future system should support:

```text
Agent A: claim
Agent B: independent verification
Agent C: provenance check
             ↓
        agreement / conflict
             ↓
        human review when needed
```

Not every field needs three agents. Verification depth should depend on consequence.

Suggested levels:

- L0: discovery only
- L1: single-source extraction
- L2: authoritative-source verification
- L3: independent corroboration
- L4: human adjudication

## Evidence precedence

When sources conflict, prefer:

1. current dataset owner or repository
2. institutional repository
3. publisher or DOI metadata
4. original dataset paper
5. later scholarly descriptions
6. secondary catalogs
7. search snippets or informal summaries

The precedence is a research workflow heuristic, not a legal rule.

## Continuous maintenance

A mature Dathive should periodically revisit records whose:
- access status may change
- licenses may change
- URLs may move
- repositories may update
- dataset versions may change
- privacy documentation may be revised

The system should record what changed and why.

## Human control

Humans retain authority over:
- final verification
- legal/license interpretation
- ethics and consent interpretation
- publication of sensitive metadata
- disputed evidence
- consequential research conclusions
