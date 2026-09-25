# Video catalog

The video catalog lists publicly posted therapy and counseling videos, on YouTube and Vimeo, that registry datasets transcribe or cite. It answers questions a dataset record cannot:

- Which videos underlie a corpus, and are they still online?
- Do two corpora draw on the same videos? If so, their "independent" results may share source material.
- How much of the public therapy-video record consists of demonstrations, role-plays or real sessions?

Entries live in `data/videos/<platform>-<video id>.yaml`, validated against `schema/video.schema.json`.

## What the catalog stores

**Metadata and a link, nothing else.** The registry never downloads, rehosts, clips or transcribes a video, and never stores thumbnails, audio or transcripts. Each entry records:

| Field | Meaning |
|---|---|
| `url` | Canonical video URL, with timestamps and playlist parameters removed. |
| `title_as_listed` | The title as recorded by the dataset that lists the video. It may differ from the platform's current title. |
| `content_type` | `demonstration`, `role_play`, `real_session`, `lecture` or `unknown`. |
| `content_type_evidence` | Why that type was chosen, and on whose authority. |
| `used_by` | Each registry dataset that uses the video, with its transcript IDs and the original URLs it cited, which may carry timestamps marking the transcribed segment. |
| `availability` | `not_checked` until someone confirms the video still plays. Then `available`, `unavailable` or `private`, with `availability_checked_on`. |

## Content types

- **demonstration**: made to teach or illustrate a method, usually with an actor, trainee or volunteer as the client.
- **role_play**: an explicitly role-played session, for example a training exercise.
- **real_session**: a session with a real client, posted publicly.
- **lecture**: talking about therapy rather than conducting it.
- **unknown**: not established.

Use the most specific type the evidence supports. A dataset calling its sources "demonstrations" is evidence for `demonstration`; a title containing "role play" is weaker evidence and belongs in `content_type_evidence`, not as a silent upgrade.

## Real clients

Videos showing real clients need the most care.

1. Catalog a `real_session` video only when the evidence says the client consented to public posting, for example a statement by the channel or the dataset authors. Record that evidence.
2. Never add information about a client beyond what the published title already shows. Do not add names, locations or diagnoses drawn from watching the video.
3. When a dataset links a video that appears to show an identifiable client without documented consent, do not create an entry. Note the concern in the dataset record instead.
4. Anyone who appears in or owns a video can ask for its entry to be removed through the correction issue template. Removal requests are honoured without debate.

## Adding videos

- **From a dataset:** write an import script like `scripts/import_annomi_videos.py`. It should read the dataset's own published video list, normalize URLs with `parse_video_url`, and merge into existing entries without overwriting other datasets' `used_by` items or hand-edited fields.
- **By hand:** copy an existing entry, set every field from evidence, and leave `availability: not_checked` until checked.
- Do not catalog video lists that a dataset releases only under an access agreement, such as HOPE's. Publishing them here would circumvent that agreement.

Run `PYTHONPATH=. python scripts/validate_registry.py` afterwards. It checks the schema, the canonical URL and file name, and that every `used_by` dataset has a registry record.

## Current contents

119 videos from AnnoMI's source list, all `demonstration`, catalogued on 2026-09-25. Their availability has not been checked yet.
