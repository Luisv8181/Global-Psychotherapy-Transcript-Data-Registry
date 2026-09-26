# Candidate queue

Leads found during discovery that are not yet registry records. Each lists what has been confirmed, where, and what is still needed before a record can be written. A candidate becomes a record only when its primary source has been read. Promote it by copying data/datasets/_TEMPLATE.yaml.

Last reviewed: 2026-09-26. PsyQA and Counsel Chat were promoted to records, and the Q&A and dataset-type scope questions were settled. MESC, SimPsyDial and PsyDTCorpus were added in the next batch, and dramatized was added as a dataset type for MESC. On 2026-09-26 CACTUS, AugESC, SoulChatCorpus, MAGneT and MIDAS were promoted to records, and MIDAS's 63 source videos were added to the video catalog. Later that day MEMO and Eeyore were promoted to records, Anno-AugMI was checked and, after the repository owner added the `utterance_level` dialogue structure, recorded as anno-augmi, HOPE was reviewed and reclassified as unknown, HighQuality was reclassified as demonstration and its 199 source videos were added to the video catalog, MindDialog was reclassified as unknown, and MusPsy was audited against its author repository and ACL 2026 paper. StoryMI and PhaseMI were added as new synthetic records from their official repositories and ACL 2026 papers.

No candidates are waiting. Add new leads as rows of this table:

| Candidate | Language | Type (provisional) | Confirmed so far | Still needed |
|---|---|---|---|---|

## Review flags from this pass

Now that demonstration is a dataset type, existing records built from public counseling videos were re-read against their sources:

- **HOPE**: reviewed on 2026-09-26 and changed from real to unknown by the repository owner. The paper does not say whether its clients were real, and 110 of the 314 source-video titles that could still be retrieved say role play, demonstration, mock or simulated. Settling it further would need a statement from the authors or a link-to-session mapping. MEMO, IndieMH and Eeyore draw on HOPE.
- **MindDialog**: changed from real to unknown by the repository owner on 2026-09-26. The description recorded earlier does not establish real clients. The paper could not be re-read because ScienceDirect refused automated access, and no preprint or data release was found. Someone with access should read its data section.
- **HighQuality**: resolved on 2026-09-26. It is Pérez-Rosas et al. (ACL 2019), whose README and paper say the videos are MI demonstrations by professional counselors and role-plays by psychology students. Reclassified as demonstration by the repository owner. 42 of its 199 source videos are also AnnoMI source videos.
- **MusPsy**: the author repository and ACL 2026 paper were re-read on 2026-09-26. The paper says the dialogues are constructed from client profiles in public psychological case reports, with 1,400 training profiles and 100 test profiles averaging 6.17 sessions. The repository exposes dialogue, memory and user-card directories. The record now proposes hybrid rather than synthetic because human-derived case-report profiles are transformed into generated longitudinal dialogues. Owner review is required before this provenance correction is treated as settled.

## Video catalog leads

- MindDialog reports more than 325 hours of public psychotherapy demonstration videos. If the authors publish a video list, import it as AnnoMI's was.
- HOPE's public repository includes a list of 348 source-video links (HOPE_data/HOPE_data_source/URL_sources.txt). It is not catalogued. The list maps to no sessions, the paper documents no consent, and some videos may show real clients, so cataloguing it needs a decision by the repository owner (AGENTS.md section 9).

## Access notes

Until 2026-09-25, cloud sessions on this repository could reach only GitHub. The network policy now allows Hugging Face, arXiv, the ACL Anthology, OSF, Zenodo, ModelScope, Crossref and PubMed Central. MDPI still refuses automated requests (HTTP 403), so the AnnoMI data availability statement remains unconfirmed.
