"""Video catalog: publicly posted therapy and counseling videos that registry datasets draw on.

One YAML file per video lives in data/videos/, named <platform>-<video id>.yaml. The catalog
stores metadata and links only; it never stores video, audio or transcripts.
"""

import json
import re
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from jsonschema import Draft202012Validator, FormatChecker

from src.registry.records import RecordLoadError, load_record

_YOUTUBE_ID = re.compile(r"^[\w-]{11}$")


def videos_dir(root):
    return Path(root) / "data" / "videos"


def video_paths(root):
    return sorted(videos_dir(root).glob("*.yaml"))


def load_videos(root):
    return [load_record(p) for p in video_paths(root)]


def parse_video_url(url):
    """Return (platform, video_id, canonical_url) for a YouTube or Vimeo URL, else None."""
    parsed = urlparse(url.strip())
    host = parsed.netloc.lower().removeprefix("www.").removeprefix("m.")
    video_id = None
    if host == "youtube.com" and parsed.path == "/watch":
        video_id = (parse_qs(parsed.query).get("v") or [None])[0]
    elif host == "youtu.be":
        video_id = parsed.path.lstrip("/").split("/")[0]
    if video_id and _YOUTUBE_ID.match(video_id):
        return "youtube", video_id, f"https://www.youtube.com/watch?v={video_id}"
    if host == "vimeo.com":
        match = re.match(r"^/(\d+)", parsed.path)
        if match:
            return "vimeo", match.group(1), f"https://vimeo.com/{match.group(1)}"
    return None


def catalog_id(platform, video_id):
    return f"{platform}-{video_id}"


def validate_videos(root, dataset_ids, report):
    """Append video-catalog errors and warnings to a validator Report."""
    schema_path = Path(root) / "schema" / "video.schema.json"
    if not schema_path.exists():
        return
    schema = Draft202012Validator(json.loads(schema_path.read_text(encoding="utf-8")), format_checker=FormatChecker())
    for path in video_paths(root):
        name = f"videos/{path.name}"
        try:
            video = load_record(path)
        except RecordLoadError as exc:
            report.errors.append(f"videos/{exc}")
            continue
        report.checked += 1
        for err in sorted(schema.iter_errors(video), key=lambda e: list(e.absolute_path)):
            where = ".".join(str(p) for p in err.absolute_path) or "(record)"
            report.errors.append(f"{name}: {where}: {err.message}")

        parsed = parse_video_url(str(video.get("url", "")))
        if not parsed:
            report.errors.append(f"{name}: url is not a recognised YouTube or Vimeo video URL")
        else:
            platform, video_id, canonical = parsed
            if video.get("id") != catalog_id(platform, video_id) or path.stem != video.get("id"):
                report.errors.append(f"{name}: id and file name must both be '{catalog_id(platform, video_id)}'")
            if video.get("url") != canonical:
                report.errors.append(f"{name}: url must be the canonical form {canonical}")

        for use in video.get("used_by") or []:
            if use.get("dataset") not in dataset_ids:
                report.errors.append(f"{name}: used_by dataset '{use.get('dataset')}' has no record in data/datasets/")
