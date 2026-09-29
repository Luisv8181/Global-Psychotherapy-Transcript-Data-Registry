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
| 2026-09-29 | GitHub official repository / ACL Anthology | ESConv Emotional Support Conversation dataset current 1300 conversations original 1053 qualified conversations | en | 2 | esconv | Codex |
