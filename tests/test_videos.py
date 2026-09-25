import json
import shutil
from datetime import date
from pathlib import Path

import pytest
import yaml

from src.registry.validator import validate_registry
from src.registry.videos import load_videos, parse_video_url

ROOT = Path(__file__).resolve().parents[1]
TODAY = date(2026, 9, 25)


@pytest.mark.parametrize("url, expected", [
    ("https://www.youtube.com/watch?v=MOVj0FoOxpk&t=279s", ("youtube", "MOVj0FoOxpk")),
    ("https://www.youtube.com/watch?v=8m5-MXX372w&list=PL08E228806AE7CB30&index=8&t=0s", ("youtube", "8m5-MXX372w")),
    ("https://youtu.be/NAHJRdKY4dI", ("youtube", "NAHJRdKY4dI")),
    ("https://vimeo.com/109546082", ("vimeo", "109546082")),
])
def test_parse_video_url(url, expected):
    platform, video_id, canonical = parse_video_url(url)
    assert (platform, video_id) == expected
    assert "&" not in canonical and "t=" not in canonical.split("?v=")[-1]


def test_parse_video_url_rejects_other_hosts():
    assert parse_video_url("https://example.org/watch?v=MOVj0FoOxpk") is None


def test_catalog_links_only_known_datasets():
    ids = {p.stem for p in (ROOT / "data" / "datasets").glob("[!_]*.yaml")}
    videos = load_videos(ROOT)
    assert videos
    assert all(use["dataset"] in ids for v in videos for use in v["used_by"])


def test_vocabulary_matches_schema():
    vocab = yaml.safe_load((ROOT / "data" / "vocabularies" / "dataset-type.yaml").read_text(encoding="utf-8"))
    props = json.loads((ROOT / "schema" / "dataset.schema.json").read_text(encoding="utf-8"))["properties"]
    assert set(vocab["dataset_types"]) == set(props["dataset_type"]["enum"])
    assert set(vocab["dialogue_structures"]) == set(props["dialogue_structure"]["enum"])


@pytest.fixture
def registry(tmp_path):
    shutil.copytree(ROOT / "schema", tmp_path / "schema")
    shutil.copytree(ROOT / "data" / "vocabularies", tmp_path / "data" / "vocabularies")
    (tmp_path / "data" / "datasets").mkdir()
    (tmp_path / "data" / "videos").mkdir()
    shutil.copy(ROOT / "data" / "datasets" / "annomi.yaml", tmp_path / "data" / "datasets")
    shutil.copy(ROOT / "data" / "videos" / "youtube-MOVj0FoOxpk.yaml", tmp_path / "data" / "videos")
    return tmp_path


def edit_video(registry, **changes):
    path = registry / "data" / "videos" / "youtube-MOVj0FoOxpk.yaml"
    video = yaml.safe_load(path.read_text(encoding="utf-8"))
    video.update(changes)
    path.write_text(yaml.safe_dump(video, sort_keys=False), encoding="utf-8")


def test_video_fixture_is_valid(registry):
    assert validate_registry(registry, today=TODAY).errors == []


def test_video_must_reference_existing_dataset(registry):
    edit_video(registry, used_by=[{"dataset": "no-such-dataset"}])
    assert any("no-such-dataset" in e for e in validate_registry(registry, today=TODAY).errors)


def test_video_url_must_be_canonical(registry):
    edit_video(registry, url="https://www.youtube.com/watch?v=MOVj0FoOxpk&t=279s")
    assert any("canonical form" in e for e in validate_registry(registry, today=TODAY).errors)


def test_video_content_type_is_controlled(registry):
    edit_video(registry, content_type="therapy")
    assert any("content_type" in e for e in validate_registry(registry, today=TODAY).errors)
