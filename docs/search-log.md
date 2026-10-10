# Search log

One row per query and channel, as described in `docs/search-protocol.md` section 4. Log searches that found nothing too. Add rows at the bottom; do not edit old rows except to correct a mistake, and say so in the pull request.

"Screened" is how many results were read at title or description level. "Relevant hits" names registry ids, new leads, or "none".

## Channels that could not be searched on 2026-09-26

From the cloud session's network: ICPSR search (HTTP 403), Zenodo records API (HTTP 403), the DAIC-WOZ site and its download pages at dcapswoz.ict.usc.edu (HTTP 403, Cloudflare; its documentation PDF was reachable) and the Ulmer Textbank site (TLS handshake failure). Searches there need another route or a person.

## Log

| Date | Channel | Query (exact) | Language | Screened | Relevant hits | By |
|---|---|---|---|---|---|---|
| 2026-09-26 | Harvard Dataverse API (datasets) | psychotherapy transcripts | en | 10 of 2,240 | none | Claude Code session |
| 2026-09-26 | Harvard Dataverse API (datasets) | counseling session transcripts | en | 10 of 5,121 | none | Claude Code session |
| 2026-09-26 | Harvard Dataverse API (datasets) | therapy session recordings | en | 10 of 24,631 | none | Claude Code session |
| 2026-09-26 | LDC catalog search | counseling | en | 0; the results page loads through JavaScript and was not parsed | not established; rerun in a browser | Claude Code session |
| 2026-09-26 | TalkBank, PsychosisBank home page | (browsed) | en | 1 page | PsychosisBank (lead: clinical speech in psychosis, members only) | Claude Code session |
| 2026-09-26 | Web search | DAIC-WOZ database request access End User License Agreement dcapswoz.ict.usc.edu | en | 10 | daic-woz (official documentation PDF and Extended DAIC agreement found; search summary used only as a lead) | Claude Code session |
| 2026-09-26 | TalkBank, PsychosisBank access, membership and agreement pages | (browsed) | en | 3 pages | psychosisbank | Claude Code session |
| 2026-09-26 | Crisis Text Line data philosophy and research pages | (browsed) | en | 2 pages | crisis-text-line | Claude Code session |
| 2026-09-26 | Psychotherapy.net about, FAQ and universities pages | (browsed) | en | 3 pages | psychotherapy-net-library | Claude Code session |
| 2026-09-26 | Deep Research / web archives | psychotherapy transcripts 1900 1950 historical case dialogue Freud Jung Ferenczi journals | en/de | multiple primary/archival leads reviewed | freud-dora; freud-little-hans; jnmd-historical-archive; american-journal-insanity-archive | Claude session |
| 2026-09-26 | Web search / institutional archives | historical psychotherapy dialogue 1800 1900 Anna O Balmanno Gartnavel Crichton Augusta Manhattan | en/de | multiple primary institutional and scholarly sources reviewed | anna-o-breuer; balmanno-asylum-anecdotes; gartnavel-dynamic-case-notes; crichton-royal-case-books; augusta-mental-health-patient-records; manhattan-state-hospital-case-books | Claude session |
| 2026-09-27 | Web search / official project pages and dataset cards | MyMentorLLM psychotherapy dataset Italian 2100 sessions | it | 3 | mymentorllm | Claude session |
| 2026-09-27 | Web search / official project pages and dataset cards | CPCD Psy-Chronicle 90000 counseling dialogue units 100 student profiles | zh | 4 | cpcd | Claude session |
| 2026-09-27 | Web search / ACL Anthology and dataset card | TheraPhase CPsyCoun 400 pairs 800 sessions | zh | 3 | theraphase | Claude session |
| 2026-09-27 | Web search / ACL Anthology | CFlowPsyD 1700 Chinese asynchronous counseling conversations | zh | 2 | cflowpsyd | Claude session |
| 2026-09-27 | Web search / ACL Anthology | PsyChainD 10456 Chinese counseling dialogues | zh | 3 | psychaind | Claude session |
| 2026-09-27 | Web search / primary research papers | Alexander Street psychotherapy transcript corpus 1398 2354 sessions | en | 4 | alexander-street-general-psychotherapy-corpus | Claude session |
| 2026-09-27 | Web search / primary research papers | UCLA UW couples therapy corpus 134 couples 574 sessions | en | 4 | couples-therapy-corpus | Claude session |
| 2026-09-27 | Web search / primary research papers | motivational interviewing clinical trials corpus 145 real patient interactions | en | 4 | mi-clinical-trials-corpus | Claude session |
| 2026-09-27 | Web search / primary research papers | university counseling center psychotherapy corpus 2017 2020 5097 recordings | en | 4 | university-counseling-center-2017-2020 | Claude session |
| 2026-09-28 | ACL Anthology / OSF | German Counseling Grounding-Act Corpus GRACO 196 German counseling conversations | de | 1 paper; OSF blocked | graco | Claude session |
| 2026-09-28 | Hugging Face / official GitHub / arXiv | Graph2Counsel 760 synthetic counseling sessions psychological graphs | en | 3 | graph2counsel | Claude session |
| 2026-09-28 | Mendeley Data / Hugging Face | AntEngage Empathy Conversation Dataset 4008 synthetic conversations | en | 2 | antengage-empathy-conversation | Claude session |
| 2026-09-30 | Web search / official project repository and paper | OnCoCo German synthetic psychosocial counseling dataset human review license | de/en | 2 | oncoco | Codex |
| 2026-09-30 | Web search / official project repository and dataset host | OpenR1-Psy Chinese counseling dialogues derived from research datasets LLM generation MIT | zh | 2 | openr1-psy | Codex |
| 2026-09-30 | Web search / primary paper | Psy-Insight Chinese English counseling dialogue dataset psychotherapy annotations | zh/en | 1 paper; dataset host not established | psy-insight lead only; not added | Codex |
| 2026-09-30 | Web search / primary paper | MEDIC multimodal counseling empathy video dataset 771 clips provenance | en | 1 paper; provenance/classification unresolved | medic lead only; not added | Codex |
| 2026-09-30 | Web search / primary paper | CALM-IT synthetic motivational interviewing dataset generation framework | en | 1 paper; released dataset access/license not established | calm-it lead only; not added | Codex |
| 2026-10-02 | GitHub official project repository / ACL Anthology | KokoroChat Japanese counseling dialogue role-play provenance 6589 | ja | 2 | kokorochat | Codex |
| 2026-10-02 | GitHub official derivative repository | Multilingual KokoroChat translation lineage English and Chinese | ja/en/zh | 1 | multilingual-kokorochat lead; not added because current primary repository identity/license evidence was not sufficiently resolved | Codex |
| 2026-10-03 | GitHub official project repository / AAAI paper | CPsDD Chinese Psychological Support Dialogue Dataset 68136 PGSim synthetic counseling | zh | 2 | cpsdd | Codex |
| 2026-10-03 | GitHub official project repository / EMNLP paper / ModelScope | SoulChat-R1 SST multi-turn psychological counseling CoT synthetic dataset | zh | 2 | soulchat-r1 | Codex |
| 2026-10-03 | GitHub official project repository / LREC paper | Multilingual KokoroChat English Chinese translation lineage 6565 6582 | ja/en/zh | 2 | multilingual-kokorochat | Codex |
| 2026-10-03 | ScienceDirect primary publication | PARRY 1972 psychiatric simulation dialogue algorithm Colby | en | 2 | historical computational-therapy timeline | Codex |
| 2026-10-06 | GitHub official project repository / primary paper | MentalBench-100k mental health dialogue benchmark 10000 conversations 100000 responses | en | 2 | mentalbench-100k | Codex |
| 2026-10-07 | GitHub official project repository / data documentation | Psy-Insight bilingual mental health counseling dataset English Chinese provenance counts license | en/zh | 3 | psy-insight | Codex || 2026-10-10 | Web search | new 2026 therapy counseling dialogue dataset released Hugging Face ACL | en | 6 results screened; registry hits on Psy-Insight, KokoroChat, CPsyCounD, AUGESC | sqpsych (arXiv 2510.25384) new lead | scheduled rotation task |
| 2026-10-10 | Web search | psychotherapy dialogue corpus dataset released 2025 sessions GitHub | en | 6 results screened; registry hits on Psy-Insight, KokoroChat, PsyDTCorpus, SMILE, CACTUS | sqpsych confirmed new lead | scheduled rotation task |
| 2026-10-10 | arXiv abs page (primary paper) | SQPsych 2510.25384v2 abstract page | en | 1 page | sqpsych; authors, design summary, release claim; v2 revised 2026-08-28 | scheduled rotation task |
| 2026-10-10 | arXiv HTML full text v2 (primary paper) | SQPsych 2510.25384v2 full text | en | 1 paper | sqpsych; dual-agent roleplay, questionnaire grounding (HAM-D, HAM-A, BDI), 2,090 anonymized clients, min 15 turns, CBT guidance, multi_turn, synthetic | scheduled rotation task |
| 2026-10-10 | Project release page (primary source) | SQPsych release table ai-mh.github.io/SQPsych | en | 1 page | sqpsych; 28 HF datasets, 2.09k per main variant, 27.8k-47.7k finetune variants, per-dataset turn/token stats | scheduled rotation task |
| 2026-10-10 | Hugging Face dataset card + API (data location) | AIMH/SQPsychConv_qwq card and API; tags on command and llama3_finetune variants | en | 3 variants | sqpsych; license:apache-2.0 in metadata tags, public ungated, train 1,837 + test 253 = 2,090 rows; READMEs empty | scheduled rotation task |
