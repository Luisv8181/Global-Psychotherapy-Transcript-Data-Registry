# Candidate queue

Leads found during discovery that are not yet registry records. Each lists what has been confirmed, where, and what is still needed before a record can be written. A candidate becomes a record only when its primary source has been read. Promote it by copying `data/datasets/_TEMPLATE.yaml`.

Last reviewed: 2026-09-25. PsyQA and Counsel Chat were promoted to records, and the Q&A and dataset-type scope questions were settled. MESC, SimPsyDial and PsyDTCorpus were added in the next batch, and `dramatized` was added as a dataset type for MESC.

| Candidate | Language | Type (provisional) | Confirmed so far | Still needed |
|---|---|---|---|---|
| **CACTUS** | English | synthetic | [GitHub README](https://github.com/coding-groot/cactus): EMNLP 2024 Findings; CBT-grounded counseling conversations; dataset on Hugging Face (DLI-Lab collection). Code is GPL. | Dialogue count and dataset license from the Hugging Face card. |
| **SoulChatCorpus** | Chinese | synthetic / hybrid | [GitHub README](https://github.com/scutcyr/SoulChat): EMNLP 2023 Findings; open-source version on ModelScope (June 2024) with about 90,000 dialogues filtered out for privacy, safety and quality; single-turn corpus of more than 150,000 instructions. Project restricted to non-commercial research. | Multi-turn dialogue count, how the dialogues were generated, and the dataset's own license on ModelScope. |
| **MAGneT** | English | synthetic | Listed in the [Graph2Counsel README](https://github.com/UKPLab/graph2counsel) with Hugging Face and [TUdatalib](https://tudatalib.ulb.tu-darmstadt.de/handle/tudatalib/5072) links. | Paper, generation method, size and license. |
| **Eeyore** | English | synthetic profiles | Listed in the Graph2Counsel README (character cards for client simulation); arXiv 2306.09742. | Whether it contains dialogues or only profiles. It may belong outside a transcript registry. |
| **AugESC** | English | synthetic | [GitHub README](https://github.com/thu-coai/AugESC): Findings of ACL 2023, "Dialogue Augmentation with Large Language Models for Emotional Support Conversation"; data on Hugging Face (thu-coai/augesc). | Size, generation method and license from the Hugging Face card. |
| **Anno-AugMI / Anno-FairMI** | English | hybrid | [GitHub README](https://github.com/vsrana-ai/Augmenting-AnnoMI): augmented AnnoMI therapist utterances balanced for MI quality, overall or per topic (SDAIH 2023). | Whether the release holds dialogues or isolated utterances. Utterance-level data may fall outside `dialogue_structure`. |
| **MEMO** | English | unknown | [GitHub README](https://github.com/LCS2-IIITD/MEMO): counseling-summarization dataset from KDD 2022, released through an access agreement form. | Its source conversations (possibly HOPE, from the same group; unconfirmed), size and content. |
| **MIDAS** | Spanish | unknown | Title found by search, "Examining Spanish Counseling with MIDAS: a Motivational Interviewing Dataset in Spanish" (arXiv 2502.08458). | Everything; its repository was not found. It would be the registry's first Spanish motivational-interviewing resource. |

## Review flags from this pass

Now that `demonstration` is a dataset type, three existing records built from public counseling videos should be re-read against their sources:

- **HOPE** (`real`): built from publicly available counseling videos. Check whether these were real sessions or demonstrations. This also decides IndieMH, which the LREC 2026 paper confirms is HOPE translated into Hinglish.
- **MindDialog** (`real`, partially verified): its source is described as demonstration videos featuring real therapists.
- **HighQuality** (`real`, partially verified): 258 therapist-patient dialogues annotated for MI quality. Check whether this is the high- and low-quality MI video collection from Pérez-Rosas et al., which overlaps AnnoMI's sources.

## Video catalog leads

- MindDialog reports more than 325 hours of public psychotherapy demonstration videos. If the authors publish a video list, import it as AnnoMI's was.
- HOPE's video list is released only under its access agreement and must not be catalogued (see `docs/video-catalog.md`).

## Access notes

Until 2026-09-25, cloud sessions on this repository could reach only GitHub. The network policy now allows Hugging Face, arXiv, the ACL Anthology, OSF, Zenodo, ModelScope, Crossref and PubMed Central. MDPI still refuses automated requests (HTTP 403), so the AnnoMI data availability statement remains unconfirmed.
