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
| 2026-10-07 | GitHub official project repository / data documentation | Psy-Insight bilingual mental health counseling dataset English Chinese provenance counts license | en/zh | 3 | psy-insight | Codex
| 2026-10-10 | Web search | GeCCo German e-counseling conversations corpus dataset | en | 8 | GEMCo paper arXiv 2607.23621; gecco-dataset repos (th-nuernberg canonical, albrechtje fork) | Subagent session |
| 2026-10-10 | Web search | GEMCo German counseling proxy corpus arXiv 2607.23621 | en | 7 | GEMCo paper + data repo th-nuernberg/GEMCo | Subagent session |
| 2026-10-10 | GitHub official data repository (README, LICENSE) | th-nuernberg/GEMCo repository files | en | 1 repo | gemco | Subagent session |
| 2026-10-10 | GitHub official data repository (README, LICENSE.md, CSV row count) | th-nuernberg/gecco-dataset repository files | en/de | 1 repo | gecco | Subagent session |
| 2026-10-10 | Official institute page | e-beratungsinstitut.de institute profile | de | 1 | psychosocial counseling scope confirmed for GeCCo | Subagent session |
| 2026-10-10 | Web search | GeCCo Albrecht Lehmann German counseling conversation dataset paper | en | 8 | canonical repo th-nuernberg/gecco-dataset; OnCoCo paper same group | Subagent session |
| 2026-10-10 | Web search | CALM-IT synthetic motivational interviewing dataset | en | 6 | paper arXiv 2601.10085 only; no data release found | Subagent session |
| 2026-10-10 | Web search | CALM-IT github repository motivational interviewing dialogues code | en | 4 | no official code or data repository found | Subagent session |
| 2026-10-10 | Web search | MEDIC multimodal empathy counseling video dataset 771 clips | en | 8 | MEDIC paper arXiv 2305.02842; STOPPED: face-to-face counseling videos show clients bodies and faces, no consent documentation found (AGENTS.md section 9) | Subagent session |
| 2026-10-10 | Web search | MindDialog large-scale benchmark counseling dialogue understanding generation | en | 6 | none (no official preprint or author repo found) | scheduled rotation task |
| 2026-10-10 | Web search | "MindDialog" counseling benchmark arXiv Pattern Recognition 2026 | en | 6 | none; survey citations confirm Hu et al. 2026 (Pattern Recognition 179, 113766) but no primary full text | scheduled rotation task |
| 2026-10-10 | Web search | "MindDialog" github He Hu counseling dialogue benchmark | en | 6 | PuLing0/minddialog_infer (third-party inference reproduction, no paper link) | scheduled rotation task |
| 2026-10-10 | GitHub API repo search (gh CLI) | MindDialog | en | 1 repo | PuLing0/minddialog_infer only (third-party; README cites no official paper or dataset release) | scheduled rotation task |
| 2026-10-10 | browser.open on primary source URL | https://www.sciencedirect.com/science/article/pii/S0031320326007314 | en | 1 page | HTTP 403 (access denied), unchanged since 2026-09-26; live-browser read-only recovery task dispatched | scheduled rotation task |
| 2026-10-10 | Web search | MEDIC multimodal counseling empathy dataset 771 video clips | en | 6 | medic (arXiv 2305.02842 found; USTC-AC project page has abstract only, no dataset link) | scheduled rotation task |
| 2026-10-10 | arXiv abs + HTML full text (primary paper) | MEDIC: A Multimodal Empathy Dataset in Counseling (Zhu et al., ACM MM 2023) | en/zh | 1 paper | medic; provenance resolved as demonstration (UM Psychology counselors acted out former real cases; original patient absent); 771 talk turns, 38 videos, 10 cases, 678 min; Chinese; access route and dataset license not stated | scheduled rotation task |
| 2026-10-10 | Web search / official pages | MEDIC multimodal empathy dataset github download dataset code USTC | en | 6 | none; no code repository or dataset release found; paper says "available for research purposes" with no access route named | scheduled rotation task |
| 2026-10-10 | Web search | CALM-IT synthetic motivational interviewing dataset paper | en | 6 | calm-it (arXiv 2601.10085 found; v1 submitted 2026-01-15, v2 revised 2026-05-27) | scheduled rotation task |
| 2026-10-10 | arXiv abs page, v1 (primary paper) | CALM-IT 2601.10085v1 abstract page | en | 1 page | calm-it; authors Viet Cuong Nguyen et al., Georgia Institute of Technology + Northwell Health; no code/data links listed on the page | scheduled rotation task |
| 2026-10-10 | arXiv HTML full text, v1 (primary paper) | CALM-IT 2601.10085v1 full text | en | 1 paper | calm-it; fully synthetic therapist-client MI dialogues; client grounding = anonymized Reddit-derived third-person vignettes (no raw posts released) + DASS-42/TIPI-based profiles; §9 says code and vignettes will be released only upon manuscript acceptance; multi_turn dialogue structure; no data license stated | scheduled rotation task |
| 2026-10-10 | arXiv abs page, v2 (abstract is secondary evidence) | CALM-IT 2601.10085v2 abstract page | en | 1 page | calm-it; v2 abstract says "We release a reproducible generation framework, a MITI-grounded process-level evaluation protocol, and a large-scale synthetic corpus" of 8,232 dialogues; author list changed (Srijan Kumar out, Michael L. Birnbaum in); no linked artifact | scheduled rotation task |
| 2026-10-10 | GitHub code search + Hugging Face datasets API | "CALM-IT" github "Nguyen" code dialogues repository; huggingface.co/api/datasets?search=CALM-IT | en | 10 repos; 1 dataset | none; no official code repository or dataset card found (closest HF hit was unrelated CALM-Dataset/CALM-Italy); arXiv "Code, Data and Media" section lists no URLs | scheduled rotation task |
| 2026-10-10 | Web search | new 2026 therapy counseling dialogue dataset released Hugging Face ACL | en | 6 results screened; registry hits on Psy-Insight, KokoroChat, CPsyCounD, AUGESC | sqpsych (arXiv 2510.25384) new lead | scheduled rotation task |
| 2026-10-10 | Web search | psychotherapy dialogue corpus dataset released 2025 sessions GitHub | en | 6 results screened; registry hits on Psy-Insight, KokoroChat, PsyDTCorpus, SMILE, CACTUS | sqpsych confirmed new lead | scheduled rotation task |
| 2026-10-10 | arXiv abs page (primary paper) | SQPsych 2510.25384v2 abstract page | en | 1 page | sqpsych; authors, design summary, release claim; v2 revised 2026-08-28 | scheduled rotation task |
| 2026-10-10 | arXiv HTML full text v2 (primary paper) | SQPsych 2510.25384v2 full text | en | 1 paper | sqpsych; dual-agent roleplay, questionnaire grounding (HAM-D, HAM-A, BDI), 2,090 anonymized clients, min 15 turns, CBT guidance, multi_turn, synthetic | scheduled rotation task |
| 2026-10-10 | Project release page (primary source) | SQPsych release table ai-mh.github.io/SQPsych | en | 1 page | sqpsych; 28 HF datasets, 2.09k per main variant, 27.8k-47.7k finetune variants, per-dataset turn/token stats | scheduled rotation task |
| 2026-10-10 | Hugging Face dataset card + API (data location) | AIMH/SQPsychConv_qwq card and API; tags on command and llama3_finetune variants | en | 3 variants | sqpsych; license:apache-2.0 in metadata tags, public ungated, train 1,837 + test 253 = 2,090 rows; READMEs empty | scheduled rotation task |
| 2026-10-10 | Web search | CALM-IT synthetic motivational interviewing dataset GitHub | en | 7 results; CALM-IT paper (arXiv 2601.10085) confirmed as new lead | calm-it | scheduled rotation task |
| 2026-10-10 | Web search | CALM-IT "2601.10085" github repository code dataset | en | 6 results; no official release repo found | calm-it lead; searched on | scheduled rotation task |
| 2026-10-10 | arXiv abs page (primary paper) | CALM-IT 2601.10085 abs | en | 1 page | calm-it; v2 revised 2026-05-27; authors, affiliations, abstract | scheduled rotation task |
| 2026-10-10 | arXiv HTML full text v2 (primary paper) | CALM-IT 2601.10085v2 full text | en | 1 paper | calm-it; framework design, 8,232 = 686x3x4, Reddit client grounding, MITI evaluation, release claim with no location | scheduled rotation task |
| 2026-10-10 | GitHub site search | CALM-IT motivational interviewing Nguyen code | en | 7 results; no official repo for the paper's authors | calm-it lead; no release route found | scheduled rotation task |
| 2026-10-10 | Web search | CALM-IT synthetic corpus Hugging Face dataset motivational interviewing | en | 7 results; HF hits are unrelated CALM works (agentic LM, RNA model) | calm-it lead; no HF dataset found | scheduled rotation task |
| 2026-10-10 | Hugging Face papers page | huggingface.co/papers/2601.10085 | en | 1 page; 404, no listing | calm-it lead; no release route found | scheduled rotation task |
| 2026-10-07 | GitHub official project repository / data documentation | Psy-Insight bilingual mental health counseling dataset English Chinese provenance counts license | en/zh | 3 | psy-insight | Codex |
| 2026-10-08 | GitHub official project repository / primary paper | PsychEval multi-session multi-therapy benchmark case-report reconstruction provenance license | en/unknown | 2 | psycheval (re-reviewed existing record) | Codex |
| 2026-10-08 | Web search / Hugging Face official dataset card | mental health counseling response comparison human versus LLM answers empathy appropriateness relevance ratings | en | 4 | mental-health-counseling-responses | Codex |
| 2026-10-08 | GitHub official project repository / ACL Anthology | PsyDial long-term reconstructed Chinese counseling dialogue CC0 repo license | zh | 2 | psydial existing record; duplicate screened | Codex |
| 2026-10-08 | Hugging Face official dataset card / original source link | Amod mental health counseling conversations 3512 Q&A RAIL-D access terms | en | 2 | amod corpus not added as likely existing Counsel Chat/CounselChat lineage; source-level duplication/lineage requires a separate review | Codex |
| 2026-10-08 | Hugging Face official dataset card / arXiv paper | CounselingBench 1612 case-exam questions five counseling competency groups Apache-2.0 | en | 2 | counselingbench lead not added in this pass; case-based exam bank rather than conversation transcript corpus | Codex |
| 2026-10-09 | GitHub repository search; external source access blocked in connector | GeCCo German e-counseling conversations official repository/license follow-up | de | 1 | GeCCo candidate queue; primary source re-open pending | Codex |
| 2026-10-09 | Research lead from arXiv identifier; external source access blocked in connector | GEMCo German counseling proxy corpus arXiv 2607.23621 official data release and licensing | de | 1 | GEMCo candidate queue; primary source re-open pending | Codex |
| 2026-10-11 | arXiv abs page (primary) | arXiv:2601.10085 CALM-IT abs | en | 1 page; still v2 (27 May 2026), no v3, no Code/Data/Media links listed | calm-it; release artifact still absent | scheduled rotation task |
| 2026-10-11 | GitHub API repo search (gh CLI) | CALM-IT motivational interviewing | en | 0 repos | calm-it; no official release repo | scheduled rotation task |
| 2026-10-11 | Hugging Face datasets API | search=CALM-IT | en | 1 hit: CALM-Dataset/CALM-Italy (unrelated) | calm-it; no official dataset card | scheduled rotation task |
| 2026-10-11 | Web search | CALM-IT "Viet Cuong Nguyen" github repository code motivational interviewing dialogues | en | 8 results; paper mirrors and CatalyzeX author page only, no author-hosted repo | calm-it; no release route found | scheduled rotation task |
