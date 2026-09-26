"""Check whether catalogued videos are still publicly viewable, using YouTube's and Vimeo's oEmbed endpoints.

Usage: PYTHONPATH=. python scripts/check_video_availability.py [--dataset ID] [--all]

By default only entries still marked `not_checked` are checked; --all re-checks every entry.
--dataset limits the check to videos used by one registry dataset.

oEmbed answers without playing the video. The responses are recorded as follows:
  200       -> available.
  404       -> unavailable (removed, or never public).
  other     -> left unchanged. YouTube and Vimeo return 401 or 403 both for private videos and for
               videos whose owner restricts embedding, so those codes do not settle availability.
Only the status is recorded. The response also carries the uploader's name and the current title,
but many uploaders are private individuals (for example students posting class role-plays), so
this script does not copy them into the catalog. Nothing else is fetched: no video, audio,
thumbnail or transcript.
"""
import argparse
import urllib.error
import urllib.parse
import urllib.request
from datetime import date
from pathlib import Path

import yaml

from src.registry.records import load_record
from src.registry.videos import video_paths

OEMBED = {
    "youtube": "https://www.youtube.com/oembed?format=json&url=",
    "vimeo": "https://vimeo.com/api/oembed.json?url=",
}


def oembed_status(platform, url):
    """Return the HTTP status of the platform's oEmbed response for a video URL."""
    try:
        with urllib.request.urlopen(OEMBED[platform] + urllib.parse.quote(url, safe=""), timeout=30) as resp:
            return resp.status
    except urllib.error.HTTPError as err:
        return err.code


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--dataset", help="only videos used by this registry dataset")
    p.add_argument("--all", action="store_true", help="re-check entries already checked")
    args = p.parse_args()

    root = Path(__file__).resolve().parents[1]
    today = date.today().isoformat()
    tally = {}
    for path in video_paths(root):
        entry = load_record(path)
        if entry.get("platform") not in OEMBED:
            continue
        if args.dataset and not any(u.get("dataset") == args.dataset for u in entry.get("used_by") or []):
            continue
        if not args.all and entry.get("availability") != "not_checked":
            continue
        status = oembed_status(entry["platform"], entry["url"])
        tally[status] = tally.get(status, 0) + 1
        if status == 200:
            entry["availability"] = "available"
            entry["availability_checked_on"] = today
        elif status == 404:
            entry["availability"] = "unavailable"
            entry["availability_checked_on"] = today
        else:
            print(f"{path.name}: oEmbed returned {status}; left unchanged")
            continue
        path.write_text(yaml.safe_dump(entry, sort_keys=False, allow_unicode=True, width=100), encoding="utf-8")

    print("oEmbed responses: " + (", ".join(f"{k} x{v}" for k, v in sorted(tally.items())) or "none checked"))


if __name__ == "__main__":
    main()
