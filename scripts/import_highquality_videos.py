"""Add or refresh video catalog entries for the source videos behind HighQuality.

Usage: PYTHONPATH=. python scripts/import_highquality_videos.py [--zip PATH]

Reads urls.csv and labels.csv from HighLowQualityCounseling.zip (Pérez-Rosas et al., ACL 2019),
downloaded from the University of Michigan unless --zip is given. urls.csv pairs each transcript id
with its source video URL, or NA when none was recorded; NA rows are reported and skipped. Several
transcripts can come from one video. Re-running it replaces only the HighQuality entry in each
file's used_by list; other datasets' entries (for example AnnoMI's, on shared videos) and
hand-edited fields are kept.
"""
import argparse
import csv
import io
import urllib.request
import zipfile
from datetime import date
from pathlib import Path

import yaml

from src.registry.records import load_record
from src.registry.videos import catalog_id, parse_video_url, videos_dir

SOURCE_ZIP = "https://web.eecs.umich.edu/~mihalcea/downloads/HighLowQualityCounseling.zip"
DATASET = "highquality-therapy-dialogues"
EVIDENCE = (
    "Listed as a source video by the High- and Low-Quality Counseling dataset (Pérez-Rosas et al., "
    "ACL 2019), whose README and paper describe its videos as MI counseling demonstrations by "
    "professional counselors and MI role-play counseling by psychology students. The dataset does "
    "not record which of the two a given video is."
)


def read_csv(archive, name):
    member = next(n for n in archive.namelist() if n.endswith("/" + name) and "__MACOSX" not in n)
    return list(csv.DictReader(io.StringIO(archive.read(member).decode("utf-8"))))


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--zip", help="local copy of HighLowQualityCounseling.zip")
    args = p.parse_args()

    if args.zip:
        data = Path(args.zip).read_bytes()
    else:
        with urllib.request.urlopen(SOURCE_ZIP, timeout=120) as resp:
            data = resp.read()
    archive = zipfile.ZipFile(io.BytesIO(data))
    labels = {r["id"]: r["label"] for r in read_csv(archive, "labels.csv")}
    rows = read_csv(archive, "urls.csv")

    videos, skipped = {}, []
    for row in sorted(rows, key=lambda r: r["id"]):
        tid, url = row["id"], row["url"].strip()
        parsed = parse_video_url(url) if url and url.upper() != "NA" else None
        if not parsed:
            skipped.append(tid)
            continue
        platform, video_id, canonical = parsed
        v = videos.setdefault(catalog_id(platform, video_id), {
            "platform": platform, "video_id": video_id, "url": canonical,
            "transcripts": [], "labels": [], "source_urls": [],
        })
        v["transcripts"].append(tid)
        if labels.get(tid) and labels[tid] not in v["labels"]:
            v["labels"].append(labels[tid])
        if url not in v["source_urls"]:
            v["source_urls"].append(url)

    out = videos_dir(Path(__file__).resolve().parents[1])
    out.mkdir(parents=True, exist_ok=True)
    today = date.today().isoformat()
    created = shared = 0
    for cid, v in videos.items():
        path = out / f"{cid}.yaml"
        if path.exists():
            entry = load_record(path)
            if any(u.get("dataset") != DATASET for u in entry.get("used_by") or []):
                shared += 1
        else:
            created += 1
            entry = {
                "id": cid, "platform": v["platform"], "video_id": v["video_id"], "url": v["url"],
                "title_as_listed": None, "channel": None,
                "content_type": "demonstration", "content_type_evidence": EVIDENCE,
                "therapy_modalities": ["motivational_interviewing"], "topics": [], "languages": ["en"],
                "used_by": [], "availability": "not_checked", "availability_checked_on": None,
                "catalogued_on": today, "notes": None,
            }
        use = {
            "dataset": DATASET,
            "transcript_ids": v["transcripts"],
            "notes": f"Quality label: {', '.join(v['labels'])}. The dataset lists no video title.",
        }
        extra_urls = [u for u in v["source_urls"] if u != v["url"]]
        if extra_urls:
            use["source_urls"] = extra_urls
        entry["used_by"] = [u for u in entry.get("used_by") or [] if u.get("dataset") != DATASET] + [use]
        path.write_text(yaml.safe_dump(entry, sort_keys=False, allow_unicode=True, width=100), encoding="utf-8")

    print(f"{len(rows)} HighQuality ids -> {len(videos)} videos: {created} new entries, "
          f"{shared} existing entries shared with other datasets")
    if skipped:
        print(f"skipped {len(skipped)} id(s) with no usable URL: {', '.join(skipped)}")


if __name__ == "__main__":
    main()
