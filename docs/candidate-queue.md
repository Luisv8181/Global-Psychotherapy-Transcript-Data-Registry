# Candidate queue

Leads found during discovery that are not yet registry records. Each lists what has been confirmed, where, and what is still needed before a record can be written. A candidate becomes a record only when its primary source has been read. Promote it by copying `data/datasets/_TEMPLATE.yaml`.

Last reviewed: 2026-09-25.

| Candidate | Language | Type (provisional) | Confirmed so far | Still needed |
|---|---|---|---|---|
| **CACTUS** | English | synthetic | [GitHub README](https://github.com/coding-groot/cactus): EMNLP 2024 Findings; CBT-grounded counseling conversations; dataset on Hugging Face (DLI-Lab collection). Code is GPL. | Dialogue count and dataset license from the Hugging Face card. |
| **SoulChatCorpus** | Chinese | synthetic / hybrid | [GitHub README](https://github.com/scutcyr/SoulChat): EMNLP 2023 Findings; open-source version on ModelScope (June 2024) with about 90,000 dialogues filtered out for privacy, safety and quality; single-turn corpus of more than 150,000 instructions. Project restricted to non-commercial research. | Multi-turn dialogue count, how the dialogues were generated, and the dataset's own license on ModelScope. |
| **MAGneT** | English | synthetic | Listed in the [Graph2Counsel README](https://github.com/UKPLab/graph2counsel) with Hugging Face and [TUdatalib](https://tudatalib.ulb.tu-darmstadt.de/handle/tudatalib/5072) links. | Paper, generation method, size and license. |
| **Eeyore** | English | synthetic profiles | Listed in the Graph2Counsel README (character cards for client simulation); arXiv 2306.09742. | Whether it contains dialogues or only profiles. It may belong outside a transcript registry. |
| **MIDAS** | Spanish | unknown | Title found by search, "Examining Spanish Counseling with MIDAS: a Motivational Interviewing Dataset in Spanish" (arXiv 2502.08458). | Everything; its repository was not found. It would be the registry's first Spanish motivational-interviewing resource. |
| **PsyQA** | Chinese | real (single-turn) | [GitHub repository](https://github.com/thu-coai/PsyQA) exists. Named in the SoulChat README as a common counseling Q&A dataset. | Access terms. It is question-answer data, not dialogue, so it may need a `clinical_qa` record type. |
| **Counsel Chat** | English | real (single-turn) | [GitHub repository](https://github.com/nbertagnolli/counsel-chat) exists; MIT license file. | Whether the MIT license covers the scraped therapist answers. Same Q&A scope question as PsyQA. |

## Scope questions to settle

- **Single-turn counseling Q&A** (PsyQA, Counsel Chat) is a large, heavily used resource type. Decide whether the registry covers it, and if so under which `source_context` (the vocabulary already has `clinical_qa`).
- **Peer and crowdsourced emotional support** (ESConv) and **demonstration recordings** (AnnoMI) currently use `dataset_type: unknown`, because `real / synthetic / hybrid` has no category for them. Adding categories such as `demonstration` and `peer_support` would make the registry's populations countable.

## Access notes for this environment

Hugging Face, arXiv, the ACL Anthology, OSF, MDPI and ModelScope were not reachable from the cloud session that built this queue. GitHub repositories were readable. Candidates hosted outside GitHub need a check from a browser, or from a session whose network policy allows those hosts.
