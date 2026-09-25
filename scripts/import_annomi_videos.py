"""Add or refresh video catalog entries for the source videos listed in AnnoMI.

Usage: PYTHONPATH=. python scripts/import_annomi_videos.py [--csv PATH]

Reads AnnoMI-simple.csv (downloaded from the AnnoMI repository unless --csv is given), groups
transcripts by video, and writes data/videos/<platform>-<id>.yaml. Re-running it replaces only the
AnnoMI entry in each file's used_by list; other datasets' entries and hand-edited fields are kept.
"""
import argparse
import csv
import io
import urllib.request
from datetime import date
from pathlib import Path

import yaml

from src.registry.records import load_record
from src.registry.videos import catalog_id, parse_video_url, videos_dir

SOURCE_CSV = "https://raw.githubusercontent.com/uccollab/AnnoMI/main/AnnoMI-simple.csv"
DATASET = "annomi"
EVIDENCE = (
    "Listed as a source video by AnnoMI, whose repository README describes its transcripts as "
    "demonstrations of high- and low-quality motivational interviewing."
)

p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
p.add_argument("--csv", help="local copy of AnnoMI-simple.csv")
args = p.parse_args()

if args.csv:
    text = Path(args.csv).read_text(encoding="utf-8")
else:
    with urllib.request.urlopen(SOURCE_CSV, timeout=60) as resp:
        text = resp.read().decode("utf-8")

transcripts = {}
for row in csv.DictReader(io.StringIO(text)):
    transcripts.setdefault(row["transcript_id"], row)

videos = {}
for tid, row in sorted(transcripts.items(), key=lambda kv: int(kv[0])):
    parsed = parse_video_url(row["video_url"])
    if not parsed:
        raise SystemExit(f"transcript {tid}: unrecognised video URL {row['video_url']!r}")
    platform, video_id, canonical = parsed
    v = videos.setdefault(catalog_id(platform, video_id), {
        "platform": platform, "video_id": video_id, "url": canonical,
        "titles": [], "topics": [], "transcripts": [], "source_urls": [], "quality": [],
    })
    v["transcripts"].append(int(tid))
    for key, value in (("titles", row["video_title"].strip()), ("source_urls", row["video_url"].strip()),
                       ("quality", row["mi_quality"].strip())):
        if value and value not in v[key]:
            v[key].append(value)
    for topic in row["topic"].split(";"):
        if topic.strip() and topic.strip() not in v["topics"]:
            v["topics"].append(topic.strip())

out = videos_dir(Path(__file__).resolve().parents[1])
out.mkdir(parents=True, exist_ok=True)
today = date.today().isoformat()
for vid, v in videos.items():
    path = out / f"{vid}.yaml"
    entry = load_record(path) if path.exists() else {
        "id": vid, "platform": v["platform"], "video_id": v["video_id"], "url": v["url"],
        "title_as_listed": v["titles"][0], "channel": None,
        "content_type": "demonstration", "content_type_evidence": EVIDENCE,
        "therapy_modalities": ["motivational_interviewing"], "topics": [], "languages": ["en"],
        "used_by": [], "availability": "not_checked", "availability_checked_on": None,
        "catalogued_on": today, "notes": None,
    }
    entry["topics"] = sorted(set(entry.get("topics") or []) | set(v["topics"]))
    use = {
        "dataset": DATASET,
        "transcript_ids": v["transcripts"],
        "notes": f"AnnoMI MI quality label: {', '.join(v['quality'])}."
                 + (f" Also listed under the titles: {'; '.join(v['titles'][1:])}." if len(v["titles"]) > 1 else ""),
    }
    extra_urls = [u for u in v["source_urls"] if u != v["url"]]
    if extra_urls:
        use["source_urls"] = extra_urls
    entry["used_by"] = [u for u in entry.get("used_by") or [] if u.get("dataset") != DATASET] + [use]
    path.write_text(yaml.safe_dump(entry, sort_keys=False, allow_unicode=True, width=100), encoding="utf-8")

print(f"{len(transcripts)} AnnoMI transcripts -> {len(videos)} catalog entries in {out}")
