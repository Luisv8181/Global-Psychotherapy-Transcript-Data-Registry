from pathlib import Path

from src.registry.validator import validate_registry

root = Path(__file__).resolve().parents[1]
report = validate_registry(root)
for warning in report.warnings:
    print(f"warning: {warning}")
for error in report.errors:
    print(f"error: {error}")
if not report.ok:
    raise SystemExit(f"Registry validation failed: {len(report.errors)} error(s) in {report.checked} readable file(s).")
print(f"Registry validation passed: {report.checked} file(s), {len(report.warnings)} warning(s).")
