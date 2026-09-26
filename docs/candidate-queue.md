# Candidate queue

Leads found during discovery that are not yet registry records. Each lists what has been confirmed, where, and what is still needed before a record can be written. A candidate becomes a record only when its primary source has been read. Promote it by copying `data/datasets/_TEMPLATE.yaml`.

Last reviewed: 2026-09-26. PsyQA and Counsel Chat were promoted to records, and the Q&A and dataset-type scope questions were settled. MESC, SimPsyDial and PsyDTCorpus were added in the next batch, and `dramatized` was added as a dataset type for MESC. On 2026-09-26 CACTUS, AugESC, SoulChatCorpus, MAGneT and MIDAS were promoted to records, and MIDAS's 63 source videos were added to the video catalog. Later that day MEMO and Eeyore were promoted to records, and Anno-AugMI was checked and held for an owner decision.

| Candidate | Language | Type (provisional) | Confirmed so far | Still needed |
|---|---|---|---|---|
| **Anno-AugMI / Anno-FairMI** | English | hybrid | [GitHub repository](https://github.com/vsrana-ai/Augmenting-AnnoMI), cloned on 2026-09-26: `Anno-AugMI.csv` has 5,302 rows and `Anno-FairMI.csv` 9,154, each row one therapist utterance with an MI-quality label (0 or 1) and a topic, and no conversation ID or turn order. The preprint says the rows are AnnoMI therapist utterances augmented with NL-Augmenter (noising, paraphrasing and similar), to balance quality overall or per topic. No license file. | **Owner decision.** These are isolated utterances, not dialogues, so no `dialogue_structure` term fits. Registering them would need a new term (AGENTS.md section 9), or they could stay out of scope as an AnnoMI derivative. |

## Review flags from this pass

Now that `demonstration` is a dataset type, three existing records built from public counseling videos should be re-read against their sources:

- **HOPE** (`real`): built from publicly available counseling videos. Check whether these were real sessions or demonstrations. This also bears on IndieMH, which the LREC 2026 paper confirms is HOPE translated into Hinglish, on MEMO, which extends HOPE with annotations and summaries (recorded as `unknown` type until HOPE is settled), and on Eeyore, which draws on HOPE among other sources.
- **MindDialog** (`real`, partially verified): its source is described as demonstration videos featuring real therapists.
- **HighQuality** (`real`, partially verified): 258 therapist-patient dialogues annotated for MI quality. Check whether this is the high- and low-quality MI video collection from Pérez-Rosas et al., which overlaps AnnoMI's sources.

## Video catalog leads

- MindDialog reports more than 325 hours of public psychotherapy demonstration videos. If the authors publish a video list, import it as AnnoMI's was.
- HOPE's video list is released only under its access agreement and must not be catalogued (see `docs/video-catalog.md`).

## Access notes

Until 2026-09-25, cloud sessions on this repository could reach only GitHub. The network policy now allows Hugging Face, arXiv, the ACL Anthology, OSF, Zenodo, ModelScope, Crossref and PubMed Central. MDPI still refuses automated requests (HTTP 403), so the AnnoMI data availability statement remains unconfirmed.
