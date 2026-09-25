"""Registry validation.

Errors block a merge: unreadable files, schema violations, identity problems,
access/redistribution values outside the controlled vocabularies, and
verification claims without evidence.

Warnings are editorial signals for a human reviewer: verification dates that
have gone stale, and verified licenses that do not cite where they were read. Validation never rewrites a record, because the registry does
not infer missing facts.
"""

import json
import re
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator, FormatChecker

from src.registry.records import RecordLoadError, is_template, load_record, record_paths
from src.registry.videos import validate_videos

__all__ = ["Report", "validate_registry", "STALE_AFTER_DAYS"]

STALE_AFTER_DAYS = 365
VERIFIED_STATES = {"verified", "partially-verified"}


@dataclass
class Report:
    errors: list = field(default_factory=list)
    warnings: list = field(default_factory=list)
    checked: int = 0

    @property
    def ok(self):
        return not self.errors


def load_schema(root):
    return json.loads((Path(root) / "schema" / "dataset.schema.json").read_text(encoding="utf-8"))


def load_vocabularies(root):
    vocab_dir = Path(root) / "data" / "vocabularies"
    access = yaml.safe_load((vocab_dir / "access.yaml").read_text(encoding="utf-8"))
    return {
        "access.level": set(access["access_levels"]),
        "redistribution": set(access["redistribution"]),
    }


def validate_registry(root, today=None):
    root = Path(root)
    today = today or date.today()
    report = Report()
    schema = Draft202012Validator(load_schema(root), format_checker=FormatChecker())
    vocab = load_vocabularies(root)
    ids, urls = {}, {}

    for path in record_paths(root, include_templates=True):
        name = path.name
        try:
            record = load_record(path)
        except RecordLoadError as exc:
            report.errors.append(str(exc))
            continue
        report.checked += 1

        for err in sorted(schema.iter_errors(record), key=lambda e: list(e.absolute_path)):
            where = ".".join(str(p) for p in err.absolute_path) or "(record)"
            report.errors.append(f"{name}: {where}: {err.message}")

        if is_template(path):
            continue

        rid = record.get("id")
        if rid and rid != path.stem:
            report.errors.append(f"{name}: id '{rid}' must match the file name '{path.stem}'")
        if rid in ids:
            report.errors.append(f"{name}: duplicate id '{rid}' (also in {ids[rid]})")
        ids.setdefault(rid, name)

        url = record.get("canonical_url")
        if isinstance(url, str):
            if not re.match(r"^https?://", url):
                report.errors.append(f"{name}: canonical_url must be an http(s) URL")
            if url in urls:
                report.errors.append(f"{name}: canonical_url duplicates {urls[url]}")
            urls.setdefault(url, name)

        _check_evidence(name, record, report)
        _check_dates(name, record, today, report)
        _check_vocabulary(name, record, vocab, report)

    validate_videos(root, {i for i in ids if i}, report)
    return report


def _check_evidence(name, record, report):
    sources = (record.get("evidence") or {}).get("primary_sources") or []
    if record.get("status") in VERIFIED_STATES and not sources:
        report.errors.append(f"{name}: status '{record['status']}' requires at least one evidence.primary_sources entry")
    for src in sources:
        if not (isinstance(src, str) and re.match(r"^https?://", src)):
            report.errors.append(f"{name}: evidence.primary_sources entry is not an http(s) URL: {src!r}")

    # A paper's open-access license is often mistaken for the dataset's license, so a verified
    # license must say where the dataset's own license was read.
    license = record.get("license") or {}
    if license.get("verified") is True and not license.get("source"):
        report.warnings.append(f"{name}: license.verified is true but license.source does not say where the dataset's license was read")


def _check_dates(name, record, today, report):
    checked = record.get("last_verified")
    if checked is None:
        if record.get("status") in VERIFIED_STATES:
            report.errors.append(f"{name}: status '{record['status']}' requires last_verified")
    else:
        try:
            when = date.fromisoformat(str(checked))
        except ValueError:
            when = None  # the schema's date format check already reports this
        if when and when > today:
            report.errors.append(f"{name}: last_verified {checked} is in the future")
        elif when and (today - when).days > STALE_AFTER_DAYS:
            report.warnings.append(f"{name}: last verified {checked}, more than {STALE_AFTER_DAYS} days ago; re-check access and license")

    start, end = record.get("collection_start_year"), record.get("collection_end_year")
    if isinstance(start, int) and isinstance(end, int) and end < start:
        report.errors.append(f"{name}: collection_end_year {end} is before collection_start_year {start}")


def _check_vocabulary(name, record, vocab, report):
    values = {
        "access.level": (record.get("access") or {}).get("level"),
        "redistribution": record.get("redistribution"),
    }
    for key, value in values.items():
        if value is not None and value not in vocab[key]:
            allowed = ", ".join(sorted(vocab[key]))
            report.errors.append(f"{name}: {key} '{value}' is not in the controlled vocabulary ({allowed})")

