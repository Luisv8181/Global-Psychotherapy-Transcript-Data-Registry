"""Build site/data/*.json from the canonical records.

Usage: PYTHONPATH=. python scripts/build_site.py
Refuses to build when validation fails, so a broken record never ships.
"""
import json
from pathlib import Path

from src.registry.audit import audit, completeness
from src.registry.records import load_record, record_paths
from src.registry.validator import validate_registry

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "site" / "data"

report = validate_registry(ROOT)
if not report.ok:
    raise SystemExit("Validation failed; run scripts/validate_registry.py for details.\n" + "\n".join(report.errors))

records = []
for path in record_paths(ROOT):
    record = load_record(path)
    record["_source_file"] = str(path.relative_to(ROOT))
    record["_completeness"] = completeness(record)
    records.append(record)

OUT.mkdir(parents=True, exist_ok=True)
with (OUT / "datasets.json").open("w", encoding="utf-8") as f:
    json.dump(records, f, ensure_ascii=False, indent=2, sort_keys=True)
with (OUT / "audit.json").open("w", encoding="utf-8") as f:
    json.dump(audit(records), f, ensure_ascii=False, indent=2)
print(f"Built {len(records)} dataset records")
