# Candidate queue

Leads found during discovery that are not yet registry records. Each lists what has been confirmed, where, and what is still needed before a record can be written. A candidate becomes a record only when its primary source has been read. Promote it by copying `data/datasets/_TEMPLATE.yaml`.

Last reviewed: 2026-09-25. PsyQA and Counsel Chat were promoted to records, and the Q&A and dataset-type scope questions were settled.

| Candidate | Language | Type (provisional) | Confirmed so far | Still needed |
|---|---|---|---|---|
| **CACTUS** | English | synthetic | [GitHub README](https://github.com/coding-groot/cactus): EMNLP 2024 Findings; CBT-grounded counseling conversations; dataset on Hugging Face (DLI-Lab collection). Code is GPL. | Dialogue count and dataset license from the Hugging Face card. |
| **SoulChatCorpus** | Chinese | synthetic / hybrid | [GitHub README](https://github.com/scutcyr/SoulChat): EMNLP 2023 Findings; open-source version on ModelScope (June 2024) with about 90,000 dialogues filtered out for privacy, safety and quality; single-turn corpus of more than 150,000 instructions. Project restricted to non-commercial research. | Multi-turn dialogue count, how the dialogues were generated, and the dataset's own license on ModelScope. |
| **MAGneT** | English | synthetic | Listed in the [Graph2Counsel README](https://github.com/UKPLab/graph2counsel) with Hugging Face and [TUdatalib](https://tudatalib.ulb.tu-darmstadt.de/handle/tudatalib/5072) links. | Paper, generation method, size and license. |
| **Eeyore** | English | synthetic profiles | Listed in the Graph2Counsel README (character cards for client simulation); arXiv 2306.09742. | Whether it contains dialogues or only profiles. It may belong outside a transcript registry. |
| **MIDAS** | Spanish | unknown | Title found by search, "Examining Spanish Counseling with MIDAS: a Motivational Interviewing Dataset in Spanish" (arXiv 2502.08458). | Everything; its repository was not found. It would be the registry's first Spanish motivational-interviewing resource. |

## Review flags from this pass

Now that `demonstration` is a dataset type, three existing records built from public counseling videos should be re-read against their sources:

- **HOPE** (`real`): built from publicly available counseling videos. Check whether these were real sessions or demonstrations.
- **MindDialog** (`real`, partially verified): its source is described as demonstration videos featuring real therapists.
- **HighQuality** (`real`, partially verified): 258 therapist-patient dialogues annotated for MI quality. Check whether this is the high- and low-quality MI video collection from Pérez-Rosas et al., which overlaps AnnoMI's sources.

## Video catalog leads

- MindDialog reports more than 325 hours of public psychotherapy demonstration videos. If the authors publish a video list, import it as AnnoMI's was.
- HOPE's video list is released only under its access agreement and must not be catalogued (see `docs/video-catalog.md`).

## Access notes for this environment

Hugging Face, arXiv, the ACL Anthology, OSF, MDPI and ModelScope were not reachable from the cloud session that built this queue. GitHub repositories were readable. Candidates hosted outside GitHub need a check from a browser, or from a session whose network policy allows those hosts.
