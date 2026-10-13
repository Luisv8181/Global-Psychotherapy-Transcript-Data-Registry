# Search protocol

How to look for resources, record what was searched, decide what enters the registry, and estimate how much exists. `docs/global-discovery-strategy.md` sets the principles (search in layers, many languages, translation is not provenance); this file makes them operational. AGENTS.md still governs every record written from what you find.

## 1. Scope

The registry covers psychotherapy and counseling dialogue, and, since 2026-09-26, these **adjacent materials**, by decision of the repository owner:

| Class | Examples | How to record |
|---|---|---|
| Therapy and counseling sessions | real, demonstration, dramatized, synthetic, hybrid corpora | Normal records (AGENTS.md section 5). |
| Clinical interviews | depression-screening interviews, psychiatric assessment conversations, speech corpora from clinical populations | Normal records. `domain` says what the conversations are, for example `clinical_interview`. They are not therapy sessions; say so in `source_context`. |
| Crisis-line and peer-support platforms | text crisis lines, peer-support apps and forums released for research | Normal records, usually `peer_support`. Access is often a research partnership; record that, never the data. |
| Unreleased corpora | session collections described in papers or project pages but not released | Records with `access.level: metadata-only`, `transcript.available: false` unless the source says otherwise, and the reason given in `access.requirements`. They make the gap between what exists and what is shared visible. |
| Training and demonstration video libraries | licensed or subscription libraries of demonstration sessions | One collection-level record per library. Never catalogue its individual videos or copy its title lists. |

**What keeps this safe.** The registry holds facts about a resource and a link to its official access route. It never holds the resource. Concretely:

- Record metadata and counts only. No transcripts, dialogue, audio, video, thumbnails, participant details or credentials (AGENTS.md section 1).
- Never copy anything released under an agreement: data, file lists, video lists, or the agreement's text beyond a short quotation needed to record its terms.
- Do not register for access, sign agreements or create accounts in order to inspect gated material. Record what the public pages say and leave the rest `unknown`.
- Respect robots rules and rate limits. Use official APIs where they exist.
- Add no identifying detail beyond what the resource's own public description states.
- Honour removal requests from anyone who appears in, owns or published a resource (AGENTS.md section 9).

This is the registry's operating practice, not legal advice. When a resource's terms are unclear, record less and ask the repository owner.

## 2. Where to search

Search every tier. Real, de-identified material is concentrated in tiers B to E, which earlier passes did not search.

**A. Code and model hubs.** GitHub, Hugging Face datasets, ModelScope, Kaggle, Papers with Code.

**B. Research data archives.** NIMH Data Archive (NDA), ICPSR, UK Data Service, Harvard Dataverse and other Dataverse installations, Zenodo, OSF, Figshare, Mendeley Data, Databrary (video), the Qualitative Data Repository, and national archives such as DANS (Netherlands), GESIS (Germany) and FSD (Finland).

**C. Language-resource catalogues.** Linguistic Data Consortium (LDC), ELRA/ELDA, CLARIN centres, TalkBank (including its clinical banks, such as PsychosisBank, AphasiaBank and DementiaBank), AI Hub (Korea).

**D. Clinical and psychotherapy-process literature.** Psychotherapy Research, Journal of Consulting and Clinical Psychology, Journal of Counseling Psychology, Counselling and Psychotherapy Research, Behavior Research Methods, and proceedings of the Society for Psychotherapy Research. Look for corpora of recorded sessions used for coding studies (MI fidelity, alliance, empathy). Most are unreleased; record them as metadata-only when a primary source describes them. Read data availability statements.

**E. Licensed and institutional libraries.** Alexander Street (Counseling and Psychotherapy Transcripts, Client Narratives, video collections), APA PsycTherapy, Psychotherapy.net, university training-clinic archives.

**F. NLP literature.** ACL Anthology, arXiv, LREC, ICASSP and Interspeech proceedings, and survey papers. Survey tables are leads, never evidence (AGENTS.md section 3).

**G. Non-English sources.** National repositories and journals in each language, searched in that language (section 3).

## 3. Queries

Combine a resource term with a data term, in each language. Record the exact string used.

| Language | Resource terms | Data terms |
|---|---|---|
| English | psychotherapy, counseling, counselling, therapy session, clinical interview, crisis line | transcripts, corpus, dataset, recordings, dialogues |
| Chinese | 心理咨询, 心理治疗, 心理对话 | 数据集, 语料库, 逐字稿 |
| Japanese | カウンセリング, 心理療法 | データセット, コーパス, 逐語録 |
| Korean | 심리상담, 상담 대화 | 데이터셋, 말뭉치 |
| Spanish | psicoterapia, consejería, sesión terapéutica | transcripciones, corpus, conjunto de datos |
| Portuguese | psicoterapia, aconselhamento | transcrições, corpus, conjunto de dados |
| German | Psychotherapie, Beratungsgespräch | Transkripte, Korpus, Datensatz |
| French | psychothérapie, entretien thérapeutique | transcriptions, corpus, jeu de données |

Terms for other languages in `docs/global-discovery-strategy.md` should be added here by a speaker of the language before use, and the adder named in the log.

Archive keyword search is noisy. On 2026-09-26, "psychotherapy transcripts" returned 2,240 Harvard Dataverse datasets, nearly all unrelated. Screen by title and description, then open only plausible hits.

## 4. The search log

Record every search session in `docs/search-log.md`, one row per query and channel: date, channel, exact query, language, results screened, relevant hits (registry ids or new leads) and who searched. Log searches that found nothing too; they show where the registry has looked. Without the log, the registry cannot say how complete it is.

## 5. Screening

1. **Relevant?** It contains dialogue or conversation of a kind in section 1, or a primary source describes such a collection.
2. **Already known?** `grep -ril "<name or URL>" data/`, check open pull requests and `docs/candidate-queue.md`.
3. **Primary source reachable?** If not, add it to the candidate queue with what is known and what is missing.
4. **Record.** Follow AGENTS.md. Set `status` from the evidence actually read.


## 7. Search algorithm: adaptive discovery and evidence gates

Use a repeatable loop rather than a flat list of broad queries. The goal is to maximize **new, in-scope resources with inspectable primary evidence**, not raw search-result volume.

### 7.1 Build a query matrix before searching

For each pass, select at least three dimensions and combine them deliberately:

- **Resource form:** dataset, corpus, transcript, session recording, archive, data availability, benchmark, annotation corpus.
- **Clinical/process term:** psychotherapy, counseling/counselling, motivational interviewing, alliance, empathy, supervision, crisis line, psychiatric interview.
- **Provenance term:** real session, demonstration, role-play, simulated, synthetic, reconstructed, translated, de-identified, longitudinal.
- **Discovery channel:** code/model hubs, research-data archives, language-resource catalogues, clinical-process literature, licensed libraries, NLP proceedings.
- **Language/region:** use native-language query terms from the global discovery strategy, not only English queries translated mechanically.

Avoid submitting many near-identical queries to the same index. Each query should test a distinct hypothesis, such as whether a language has public datasets, whether a paper describes an unreleased corpus, or whether a known corpus has a derived version.

### 7.2 Run broad-to-narrow search passes

1. **Discovery:** use two independent channel families where possible, such as a dataset hub and a publication index.
2. **Candidate extraction:** capture title, canonical URL, language, apparent resource form, likely source, and which query found it. Treat all search snippets as leads only.
3. **Deduplication:** normalize URLs (remove tracking parameters and fragments), then compare canonical title, repository owner, paper DOI/arXiv ID, dataset IDs, and known lineage. Check `data/`, the candidate queue, and all open PRs before creating a record.
4. **Primary-source verification:** open the official dataset page/repository and the paper's methods/data-availability section when available. For licenses, open the license attached to the data itself. If a source cannot be opened, keep the item in the queue and state exactly what was inaccessible.
5. **Scope gate:** verify the actual conversation domain. Exclude or flag legal, financial, academic, sales, general medical, and generic emotional-support resources unless the content fits the registry's declared scope.
6. **Evidence extraction:** capture each claim with its own source: identity, provenance, language, structure/count, access, license, redistribution, privacy, consent/ethics, and lineage. Conflicting evidence stays visible.
7. **Decision:** promote only claims supported by primary evidence. Otherwise queue, reject with a reason, or leave unknown.
8. **Change and validate:** write metadata only, update the search log, run validator/tests/site build, then open a branch-based PR.

### 7.3 Prioritize candidates by expected value, not popularity

Use this lightweight score only to order *research effort*, never to assign evidence status:

- +2: a primary source is reachable and directly describes the resource.
- +2: fills a clear language, geography, modality, longitudinal, or provenance gap.
- +1: supplies an official persistent identifier or canonical data URL.
- +1: provides a distinct lineage or modality not already represented.
- −2: likely duplicate or derivative with no new lineage value.
- −2: likely out of scope after inspecting the actual content/domain.
- −1: only secondary sources are reachable.
- −1: no identifiable official access route.

Break ties in favor of under-covered languages and resource classes, not larger advertised row counts. A high score is not permission to mark a record verified; the evidence table in AGENTS.md remains the gate.

### 7.4 Track search yield and stop intelligently

For every query, log the exact query string, language, channel, results screened, unique relevant leads, duplicates, out-of-scope hits, inaccessible primary sources, and next action. If the current log schema cannot represent these fields, preserve the existing table shape and put concise counts in the relevant cells rather than silently changing the schema.

After each batch, compute:
- **Unique yield:** new plausible in-scope leads / results screened.
- **Verification yield:** candidates whose primary sources were actually opened / candidates selected.
- **Duplicate rate:** already-known or derivative leads / plausible leads.
- **Evidence completion:** core fields established from primary sources / core fields checked.

Use these to adapt the next batch. Low unique yield in one channel means switch query vocabulary, language, or channel; it does not prove the corpus class is exhausted. Stop a channel only after multiple distinct query families return almost entirely known or out-of-scope results, and state the date and coverage limitations.

### 7.5 Keep lineage as a graph

For translated, reconstructed, expanded, annotated, or benchmark derivatives, record the upstream resource(s) and transformation separately from the derived resource. Search both directions: from a known dataset to its citations/forks/derivatives, and from a new dataset's data card back to the original source. Do not count multiple derivatives as independent underlying conversation collections when estimating registry coverage.

### 7.6 Measure the algorithm itself

At the end of each substantial pass, summarize query families tried, channel/language coverage, unique leads, duplicates, inaccessible sources, primary-source verification rate, and changes made. Periodically compare channels using unique verified yield rather than raw hits. Do not claim a search is comprehensive from search-engine result counts alone.

## 7.7 Reproducible query selection and adaptation

This is a manual decision procedure, not a claim that a tested ranking model already exists. Use the same sequence and record each choice so separate agents can reproduce the pass.

### A. Define the gap first

Before writing queries, state one target gap in a sentence, such as "German-language real-world counseling dialogue with primary-source access evidence" or "unreleased motivational-interviewing corpora used in alliance studies." Pick one primary axis and one secondary axis from language, geography, modality, provenance, population, and access state. Avoid a pass that simply searches for "more datasets."

### B. Generate a diverse query batch

Build queries from at least three families:
1. **Native terms:** language-specific clinical and conversational terms paired with corpus/data terms.
2. **Research methods:** process terms (for example, motivational interviewing, therapeutic alliance, session coding, empathy ratings) paired with study-design and data-availability terms.
3. **Access and provenance:** archive, repository, supplementary material, data availability statement, restricted access, role-play, simulation, de-identification, or consent terms.
4. **Citation/lineage:** known dataset names, author groups, benchmark papers, citations, forks, and upstream-source terms.

Choose different channel families where possible. Repeated queries on the same index are not independent channels. Log the exact query before moving on, including queries that return no relevant candidates.

### C. Score the next search, not candidate truth

For each proposed query, estimate each item below from prior logged searches. Use 0, 1, or 2 and add the points:
- **Gap fit:** 0 = repeats covered areas; 1 = partial fit; 2 = directly targets a documented gap.
- **Novelty:** 0 = near-duplicate query; 1 = new term or source; 2 = different query family or channel.
- **Expected inspectability:** 0 = likely snippets/blocked secondary pages; 1 = mixed evidence; 2 = likely official repository, data card, archive record, or primary paper is accessible.
- **Lineage value:** 0 = likely duplicates; 1 = unclear; 2 = likely upstream, derivative, or new resource class.
- **Coverage balance:** 0 = overrepresented language/class; 1 = neutral; 2 = under-covered language, region, modality, or provenance.

Subtract 2 for a known query/index failure that has not changed and subtract 1 for a close duplicate of a query already run. This prioritizes research effort only; it is not a probability, evidence score, or candidate quality rating. The score must never change status, license, or provenance. Break ties in favor of under-covered dimensions and a different channel.

### D. Update estimates from observed outcomes

After each query, count:
- `screened`: result titles/descriptions actually reviewed, not the hit count shown by an index;
- `unique_leads`: plausible new leads not already in records, queue, or open PRs;
- `primary_opened`: candidates whose official dataset page/repository or primary paper was opened in this pass;
- `scope_passed`: candidates whose mental-health dialogue relevance is supported;
- `blocked`: candidates with an attempted but inaccessible primary source;
- `duplicate_or_derivative`: known items or items adding no independent underlying corpus;
- `out_of_scope`: screened items excluded with a reason.

Never infer precision or recall from search-engine hit counts. A query with no results differs from a query that could not execute. Mark API failures, access blocks, JavaScript-only results, and rate limits separately. Retry using an alternate official route only when it could change the available evidence.

For planning only, use smoothed rates: unique-lead yield = `(unique_leads + 1) / (screened + 2)`; primary-open rate = `(primary_opened + 1) / (unique_leads + 2)`. Always show raw numerators and denominators. These are not validated predictive metrics. Compare families only when screening effort and counting rules are reasonably similar.

### E. Choose the next move with explicit rules

- **Good unique yield and good primary access:** run one more differently worded query or adjacent channel, then assess saturation.
- **Good unique yield but poor primary access:** stop broadening discovery temporarily; use author pages, institutional repositories, DOI records, or official data-host links to verify existing leads.
- **Poor unique yield while a gap remains:** change both term family and channel, not merely punctuation or word order.
- **High duplicate rate:** trace upstream citations and lineage once; if no independent collection emerges, deprioritize the family.
- **High out-of-scope rate:** add exclusion terms or more precise clinical/process vocabulary.
- **Repeated technical failure:** log the failure and alternate route; do not count it as evidence that no dataset exists.
- **Two or more distinct query families with very low unique yield:** record a provisional plateau for that channel/gap, list attempts and date, then move to another under-covered gap. Never label the whole field exhausted.

### F. Keep candidate evidence separate from prioritization

For each candidate, maintain a checklist for identity, mental-health scope, dialogue type, source/provenance, language, size/count, access, data license, redistribution, consent/ethics, privacy/de-identification, and lineage. Each claim should be `confirmed`, `conflicting`, `unknown`, or `not applicable`, with a primary-source URL and brief evidence note when confirmed or conflicting. This can be a working checklist; do not invent schema fields without owner approval. Keep code license and data license separate.

A reachable source confirms access to that page, not permission to use or redistribute data. A primary paper can support design/provenance but does not settle the data license. A dataset appearing on multiple hubs is not independent provenance or multiple underlying collections.

### G. Close each batch with a reproducible report

After a substantial pass, summarize the target gap and query families; channels and languages actually reached plus failures; screened, unique, blocked, duplicate, and out-of-scope counts; primary sources opened and claims verified; the strongest next action and why; remaining blind spots and pass date.

Do not rewrite old log entries to make comparisons easier. If historical counts are inconsistent or not comparable, flag that limitation and start a comparable series. Do not claim the algorithm improved until later passes show higher unique verified yield, broader coverage, or lower screening effort under comparable conditions.

## 8. Estimating how much exists

Use three methods and report each with its assumptions.

**Capture–recapture.** Take two discovery channels that are as independent as possible, for example the dataset tables of two survey papers by different groups, or a Hugging Face search and a literature search. For one resource class, let `n1` and `n2` be the relevant resources each channel finds and `m` the number found by both. The Chapman estimate of the class total is

    N ≈ (n1 + 1)(n2 + 1) / (m + 1) − 1

Channels are rarely independent, and famous datasets are easier to find than obscure ones. Both effects make N too low, so treat it as a lower bound. Estimate each class separately (real, demonstration, synthetic and so on, and by language), because they are found through different channels.

**Discovery curve.** Plot cumulative new relevant resources against searches logged. When further searches in a channel return only known resources, that channel is near saturation.

**Layered counts.** Report three layers separately. Public resources are countable. Unreleased resources can be counted from papers. Raw material never assembled into datasets (video archives, clinical records) can only be bounded. Never add the layers into one number.

State every estimate with its date, channels, counts and assumptions. An estimate is a finding about the search, not a record.
