"""Add or refresh video catalog entries for the source videos behind MIDAS.

Usage: PYTHONPATH=. python scripts/import_midas_videos.py [--json PATH]

Reads Spanish_MI.json (downloaded from the MIDAS repository unless --json is given). Its README
says each conversation key is the original YouTube video ID; in the released file the keys look
like '<video id>.html' or '<video id>_<suffix>.html' when one video yields several conversations.
Keys that do not start with a well-formed YouTube ID are reported and skipped, not guessed.
Re-running it replaces only the MIDAS entry in each file's used_by list; other datasets' entries
and hand-edited fields are kept.
"""
import argparse
import json
import re
import urllib.request
from datetime import date
from pathlib import Path

import yaml

from src.registry.records import load_record
from src.registry.videos import catalog_id, parse_video_url, videos_dir

SOURCE_JSON = "https://raw.githubusercontent.com/MichiganNLP/MIDAS/main/Spanish_MI.json"
DATASET = "midas"
EVIDENCE = (
    "Listed as a source video by MIDAS. Its paper (NAACL 2025, arXiv 2502.08458) describes the "
    "videos as educational, possibly scripted to some extent, and showing either MI demonstrations "
    "by professional counselors or MI role-play counseling by psychology students. MIDAS does not "
    "record which of the two a given video is, so a video may be a student role-play."
)
_KEY = re.compile(r"^(?P<video>[\w-]{11})(?:_(?P<suffix>[\w-]+))?\.html$")


def video_id_from_key(key):
    """Return the YouTube video ID encoded in a Spanish_MI.json key, or None if malformed."""
    match = _KEY.match(key)
    return match.group("video") if match else None


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--json", help="local copy of Spanish_MI.json")
    args = p.parse_args()

    if args.json:
        text = Path(args.json).read_text(encoding="utf-8")
    else:
        with urllib.request.urlopen(SOURCE_JSON, timeout=60) as resp:
            text = resp.read().decode("utf-8")
    conversations = json.loads(text)

    videos, skipped = {}, []
    for key in sorted(conversations):
        vid = video_id_from_key(key)
        parsed = parse_video_url(f"https://www.youtube.com/watch?v={vid}") if vid else None
        if not parsed:
            skipped.append(key)
            continue
        platform, video_id, canonical = parsed
        v = videos.setdefault(catalog_id(platform, video_id),
                              {"platform": platform, "video_id": video_id, "url": canonical, "keys": []})
        v["keys"].append(key)

    out = videos_dir(Path(__file__).resolve().parents[1])
    out.mkdir(parents=True, exist_ok=True)
    today = date.today().isoformat()
    for cid, v in videos.items():
        path = out / f"{cid}.yaml"
        entry = load_record(path) if path.exists() else {
            "id": cid, "platform": v["platform"], "video_id": v["video_id"], "url": v["url"],
            "title_as_listed": None, "channel": None,
            "content_type": "demonstration", "content_type_evidence": EVIDENCE,
            "therapy_modalities": ["motivational_interviewing"], "topics": [], "languages": ["es"],
            "used_by": [], "availability": "not_checked", "availability_checked_on": None,
            "catalogued_on": today, "notes": None,
        }
        if "es" not in (entry.get("languages") or []):
            entry["languages"] = (entry.get("languages") or []) + ["es"]
        use = {
            "dataset": DATASET,
            "transcript_ids": v["keys"],
            "notes": "MIDAS lists no video title."
                     + (f" MIDAS holds {len(v['keys'])} conversations from this video." if len(v["keys"]) > 1 else ""),
        }
        entry["used_by"] = [u for u in entry.get("used_by") or [] if u.get("dataset") != DATASET] + [use]
        path.write_text(yaml.safe_dump(entry, sort_keys=False, allow_unicode=True, width=100), encoding="utf-8")

    print(f"{len(conversations)} MIDAS conversations -> {len(videos)} catalog entries in {out}")
    if skipped:
        print(f"skipped {len(skipped)} key(s) without a well-formed YouTube video ID: {', '.join(skipped)}")


if __name__ == "__main__":
    main()
