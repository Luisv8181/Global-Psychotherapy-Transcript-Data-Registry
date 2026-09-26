# Candidate queue

Leads found during discovery that are not yet registry records. Each lists what has been confirmed, where, and what is still needed before a record can be written. A candidate becomes a record only when its primary source has been read. Promote it by copying `data/datasets/_TEMPLATE.yaml`.

Last reviewed: 2026-09-25. PsyQA and Counsel Chat were promoted to records, and the Q&A and dataset-type scope questions were settled. MESC, SimPsyDial and PsyDTCorpus were added in the next batch, and `dramatized` was added as a dataset type for MESC. On 2026-09-26 CACTUS, AugESC, SoulChatCorpus, MAGneT and MIDAS were promoted to records.

| Candidate | Language | Type (provisional) | Confirmed so far | Still needed |
|---|---|---|---|---|
| **Eeyore** | English | synthetic profiles | Listed in the Graph2Counsel README (character cards for client simulation). The Hugging Face dataset `liusiyang/eeyore_profile` is gated (auto-approval), states no license, and its card needs a login to read. | Whether it contains dialogues or only profiles; its license. It may belong outside a transcript registry. |
| **Anno-AugMI / Anno-FairMI** | English | hybrid | [GitHub README](https://github.com/vsrana-ai/Augmenting-AnnoMI): augmented AnnoMI therapist utterances balanced for MI quality, overall or per topic (SDAIH 2023). | The repository's file list (not readable without repository access in the 2026-09-26 session) and whether the release holds dialogues or isolated utterances. Utterance-level data may fall outside `dialogue_structure`. |
| **MEMO** | English | unknown | [GitHub README](https://github.com/LCS2-IIITD/MEMO): counseling-summarization dataset from KDD 2022, released through an access agreement form. | Data sits behind an access-request form. Its source conversations (possibly HOPE, from the same group; unconfirmed), size and content. |

## Review flags from this pass

Now that `demonstration` is a dataset type, three existing records built from public counseling videos should be re-read against their sources:

- **HOPE** (`real`): built from publicly available counseling videos. Check whether these were real sessions or demonstrations. This also decides IndieMH, which the LREC 2026 paper confirms is HOPE translated into Hinglish.
- **MindDialog** (`real`, partially verified): its source is described as demonstration videos featuring real therapists.
- **HighQuality** (`real`, partially verified): 258 therapist-patient dialogues annotated for MI quality. Check whether this is the high- and low-quality MI video collection from Pérez-Rosas et al., which overlaps AnnoMI's sources.

## Video catalog leads

- MindDialog reports more than 325 hours of public psychotherapy demonstration videos. If the authors publish a video list, import it as AnnoMI's was.
- MIDAS's README states its conversation IDs are the original YouTube video IDs. The paper describes the videos as educational demonstrations and student role-plays, so they fall within `docs/video-catalog.md`; an importer like `scripts/import_annomi_videos.py` would add them. Some are no longer public.
- HOPE's video list is released only under its access agreement and must not be catalogued (see `docs/video-catalog.md`).

## Access notes

Until 2026-09-25, cloud sessions on this repository could reach only GitHub. The network policy now allows Hugging Face, arXiv, the ACL Anthology, OSF, Zenodo, ModelScope, Crossref and PubMed Central. MDPI still refuses automated requests (HTTP 403), so the AnnoMI data availability statement remains unconfirmed.
