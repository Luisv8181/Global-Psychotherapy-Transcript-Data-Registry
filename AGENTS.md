# Agent protocol

Rules for any AI agent (or person) changing this repository. This is a research registry: its value is that every claim traces to evidence. A fast, confident, wrong record does more harm than a missing one.

Read this whole file before your first change. `CONTRIBUTING.md`, `docs/dataset-record-guide.md` and `docs/video-catalog.md` add detail; where they conflict with this file, this file wins.

## 1. Non-negotiables

1. **Metadata only.** Never commit transcripts, dialogue text, audio, video, thumbnails, participant identifiers, credentials, or anything obtained under a data-use agreement. Small field names and counts are fine; content is not.
2. **Unknown stays unknown.** Write `unknown` or `null` rather than guess. Never fill a field from what a dataset "probably" is, from its language, or from what similar datasets are.
3. **Record only what you read.** Every fact in a record must come from a source you actually opened in this session: a repository file, a dataset card, a paper, a data file you counted. If you could not open the source, say so in `notes`.
4. **Never push to `main`.** Work on a branch and open a pull request. The checks run on pull requests and block broken records. A record pushed straight to `main` with an unquoted colon in its title broke validation for everyone on 2026-09-25.
5. **Never weaken a check to get green.** Do not skip or delete tests, loosen the schema, or add a vocabulary term just to make a record pass. Fix the record, or ask.

## 2. Workflow

1. Start from the latest `main`: `git fetch origin main && git checkout -b <your-branch> origin/main`.
2. Before adding a dataset, search for it: `grep -ril "<name or URL>" data/`. Also check open pull requests, so two agents do not write the same record.
3. Check `docs/candidate-queue.md`. It may already hold what is known about your dataset, and what is missing.
4. Make one coherent change per pull request, for example "add three Korean records" or "fix AVATAR license". Keep record changes separate from code changes.
5. Run the checks (section 7) and make them pass locally before pushing.
6. Open a pull request and fill in the template. Do not merge your own pull request unless the repository owner has asked you to.

## 3. Evidence standards

Use the strongest source you can reach. What you read determines the `status` you may set.

| Source you actually read | Counts as |
|---|---|
| The dataset's own repository files, dataset card, data repository record (Zenodo, OSF, TUdatalib), or the data file itself | **Primary.** Can support `verified`. |
| The paper that introduces the dataset (full text or data availability statement) | **Primary** for design and provenance claims. Not for the dataset's license (section 4). |
| Abstracts, search-result summaries, AI-generated summaries, blog posts, survey papers, secondary catalogs | **Secondary.** Leads only. Never enough for `verified`, and never enough for a license. |

Search summaries are often wrong. On 2026-09-25 a summary reported a CC0 license for CounseLLMe; the project page says "No License". Treat any fact from a summary as a lead to check, and if you record it anyway, say "reported by a secondary source, unconfirmed" in `notes`.

**Status:**
- `verified`: identity, provenance (`dataset_type`), access and license are each confirmed from a primary source.
- `partially-verified`: the dataset exists and some core facts are confirmed from a primary source; the rest are `unknown` or marked unconfirmed.
- `unverified`: only secondary evidence so far.

**Counts:** record the published figure with its source, or count the data file yourself and write "Counted from `<file>` on `<date>`" in `notes`. If sources disagree, record the disagreement instead of picking one. An approximate figure ("about 260") must be described as approximate.

**Dates:** set `last_verified` to the date you checked the primary sources. Do not change it if you only edited wording.

## 4. Licenses

The most common error in this registry has been recording a journal article's open-access license (often CC BY) as the dataset's license. The article license says nothing about the data.

- Read the license where the **data** lives: a `LICENSE` file in the dataset repository, the license field on the dataset card or data repository record, or the access agreement.
- Put that page's URL in `license.source`. Validation warns when `license.verified: true` has no `license.source`.
- A code repository's license (Apache, MIT, GPL) may cover only code. Say so in `license.notes` when the data could have a different owner, for example text scraped from a website.
- "No license" is a finding, not a gap: record `type: none-selected`, and treat redistribution as conditional at most.
- `redistribution` is separate from `access`. Openly downloadable data can still be non-redistributable.

## 5. Classifying a dataset

Choose `dataset_type` from `data/vocabularies/dataset-type.yaml`, using the most specific type the evidence supports:

- Recorded or posted sessions: are they naturally occurring (`real`), or made to teach a method (`demonstration`)? Public counseling videos are frequently demonstrations or role-plays. Do not call them `real` unless the source says the clients were real.
- Crowdworkers or volunteers supporting help-seekers: `peer_support`.
- Human material transformed by translation, paraphrase, LLM expansion or reconstruction: `hybrid`. For example, IndieMH was translated from public counseling conversations and is not an original Hinglish corpus.
- Fully model-generated: `synthetic`.

Set `dialogue_structure` separately: `multi_turn`, `single_turn_qa` or `mixed`. Single-turn counseling Q&A is in scope.

## 6. Writing records safely

- Start from `data/datasets/_TEMPLATE.yaml`. The `id` is lowercase words joined by hyphens and must match the file name.
- **Quote any value containing a colon followed by a space.** `title: "HOPE: Counselling Conversations Dataset"`. Unquoted, it is invalid YAML. This has broken the registry twice.
- Use `>-` block scalars for long `notes` and `source_context`, and still avoid `": "` inside them, or quote the whole value.
- `access.level` and `redistribution` must use terms from `data/vocabularies/access.yaml`. Put nuance in `access.requirements` or `notes`.
- Write notes for a researcher deciding whether to use the data. State what is known, what is not, and why.
- Video catalog entries follow `docs/video-catalog.md`, especially its rules on videos showing real clients. Do not catalog video lists that a dataset releases only under an access agreement.

## 7. Checks

Run these from the repository root before every push:

```bash
pip install -r requirements-dev.txt
PYTHONPATH=. python scripts/validate_registry.py   # must print "passed"
PYTHONPATH=. python -m pytest -q                   # must pass
PYTHONPATH=. python scripts/build_site.py          # must build
```

Validation errors block merging. Warnings are a to-do list for people: do not add new warnings without saying why in the pull request. `PYTHONPATH=. python scripts/audit_registry.py` shows which core fields each record has not established; use it to pick verification work.

## 8. Reporting your work

In the pull request, and in any summary to a person:

- List what you confirmed and from which source.
- List what you could **not** access (blocked sites, paywalls, gated datasets) and what you therefore left unknown.
- Say plainly when something is inferred or unconfirmed. Do not round up "partially checked" to "verified".
- If you change an existing record's classification or license, give the evidence for the change and what it replaces.

## 9. When to stop and ask the repository owner

- Adding, renaming or removing a vocabulary term, schema field, or dataset type.
- Reclassifying a record between `real` and any other type.
- Anything involving videos or data that may show real, identifiable clients.
- A removal or takedown request from anyone who appears in, owns, or published a resource.
- Any conflict between sources that changes what a record claims.
