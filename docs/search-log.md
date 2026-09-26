# Search log

One row per query and channel, as described in `docs/search-protocol.md` section 4. Log searches that found nothing too. Add rows at the bottom; do not edit old rows except to correct a mistake, and say so in the pull request.

"Screened" is how many results were read at title or description level. "Relevant hits" names registry ids, new leads, or "none".

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

## Channels that could not be searched on 2026-09-26

From the cloud session's network: ICPSR search (HTTP 403), Zenodo records API (HTTP 403), the DAIC-WOZ site and its download pages at dcapswoz.ict.usc.edu (HTTP 403, Cloudflare; its documentation PDF was reachable) and the Ulmer Textbank site (TLS handshake failure). Searches there need another route or a person.

| 2026-09-26 | Deep Research / web archives | psychotherapy transcripts 1900 1950 historical case dialogue Freud Jung Ferenczi journals | en/de | multiple primary/archival leads reviewed | freud-dora; freud-little-hans; jnmd-historical-archive; american-journal-insanity-archive | Claude session |
