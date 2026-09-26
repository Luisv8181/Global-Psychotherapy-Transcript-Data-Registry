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

## 6. Estimating how much exists

Use three methods and report each with its assumptions.

**Capture–recapture.** Take two discovery channels that are as independent as possible, for example the dataset tables of two survey papers by different groups, or a Hugging Face search and a literature search. For one resource class, let `n1` and `n2` be the relevant resources each channel finds and `m` the number found by both. The Chapman estimate of the class total is

    N ≈ (n1 + 1)(n2 + 1) / (m + 1) − 1

Channels are rarely independent, and famous datasets are easier to find than obscure ones. Both effects make N too low, so treat it as a lower bound. Estimate each class separately (real, demonstration, synthetic and so on, and by language), because they are found through different channels.

**Discovery curve.** Plot cumulative new relevant resources against searches logged. When further searches in a channel return only known resources, that channel is near saturation.

**Layered counts.** Report three layers separately. Public resources are countable. Unreleased resources can be counted from papers. Raw material never assembled into datasets (video archives, clinical records) can only be bounded. Never add the layers into one number.

State every estimate with its date, channels, counts and assumptions. An estimate is a finding about the search, not a record.
