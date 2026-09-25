import shutil
from datetime import date
from pathlib import Path

import pytest
import yaml

from src.registry.records import load_records
from src.registry.validator import validate_registry

ROOT = Path(__file__).resolve().parents[1]
TODAY = date(2026, 9, 25)


def test_registry_records_validate():
    report = validate_registry(ROOT, today=TODAY)
    assert report.errors == []
    assert report.checked == len(list((ROOT / "data" / "datasets").glob("*.yaml")))


def test_template_is_skipped_by_loader():
    assert "example-dataset" not in {r["id"] for r in load_records(ROOT)}


def test_dates_load_as_iso_strings():
    record = next(r for r in load_records(ROOT) if r["id"] == "annomi")
    assert record["last_verified"] == "2026-09-24"


@pytest.fixture
def registry(tmp_path):
    """A copy of the schema, vocabularies and one known-good record."""
    shutil.copytree(ROOT / "schema", tmp_path / "schema")
    shutil.copytree(ROOT / "data" / "vocabularies", tmp_path / "data" / "vocabularies")
    (tmp_path / "data" / "datasets").mkdir()
    shutil.copy(ROOT / "data" / "datasets" / "annomi.yaml", tmp_path / "data" / "datasets")
    return tmp_path


def write(registry, name, text):
    (registry / "data" / "datasets" / name).write_text(text, encoding="utf-8")


def rewrite(registry, old, new):
    path = registry / "data" / "datasets" / "annomi.yaml"
    text = path.read_text(encoding="utf-8")
    assert old in text
    path.write_text(text.replace(old, new), encoding="utf-8")


def test_unquoted_colon_in_title_is_reported_not_crashed(registry):
    rewrite(registry, "title: AnnoMI", "title: AnnoMI: Motivational Interviewing")
    report = validate_registry(registry, today=TODAY)
    assert any("annomi.yaml: invalid YAML" in e for e in report.errors)


def test_id_must_match_file_name(registry):
    rewrite(registry, "id: annomi", "id: anno-mi")
    assert any("must match the file name" in e for e in validate_registry(registry, today=TODAY).errors)


def test_duplicate_canonical_url(registry):
    text = (registry / "data" / "datasets" / "annomi.yaml").read_text(encoding="utf-8")
    write(registry, "annomi-copy.yaml", text.replace("id: annomi", "id: annomi-copy"))
    assert any("canonical_url duplicates" in e for e in validate_registry(registry, today=TODAY).errors)


def test_verified_status_requires_primary_sources(registry):
    path = registry / "data" / "datasets" / "annomi.yaml"
    record = yaml.safe_load(path.read_text(encoding="utf-8"))
    record["evidence"]["primary_sources"] = []
    path.write_text(yaml.safe_dump(record, sort_keys=False), encoding="utf-8")
    errors = validate_registry(registry, today=TODAY).errors
    assert any("requires at least one evidence.primary_sources" in e for e in errors)


def test_schema_rejects_bad_enum(registry):
    rewrite(registry, "dataset_type: unknown", "dataset_type: realistic")
    assert any("dataset_type" in e for e in validate_registry(registry, today=TODAY).errors)


def test_unknown_is_valid_for_sessions_and_longitudinal(registry):
    rewrite(registry, "sessions: 133", "sessions: unknown")
    rewrite(registry, "longitudinal: false", "longitudinal: unknown")
    assert validate_registry(registry, today=TODAY).errors == []


def test_future_verification_date_is_an_error(registry):
    rewrite(registry, "last_verified: 2026-09-24", "last_verified: 2027-01-01")
    assert any("in the future" in e for e in validate_registry(registry, today=TODAY).errors)


def test_stale_verification_is_a_warning(registry):
    report = validate_registry(registry, today=date(2028, 1, 1))
    assert report.errors == []
    assert any("more than 365 days ago" in w for w in report.warnings)


def test_off_vocabulary_access_is_an_error(registry):
    rewrite(registry, "level: open", "level: public")
    assert any("access.level 'public'" in e for e in validate_registry(registry, today=TODAY).errors)


def test_off_vocabulary_redistribution_is_an_error(registry):
    rewrite(registry, "redistribution: conditional", "redistribution: public_release_reported")
    assert any("redistribution 'public_release_reported'" in e for e in validate_registry(registry, today=TODAY).errors)


def test_verified_license_without_source_is_a_warning(registry):
    rewrite(registry, "  verified: false\n  source: https://www.mdpi.com/1999-5903/15/3/110\n", "  verified: true\n")
    report = validate_registry(registry, today=TODAY)
    assert report.errors == []
    assert any("license.source" in w for w in report.warnings)
