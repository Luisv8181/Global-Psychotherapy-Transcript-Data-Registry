"""Print which core research fields each record has not yet established.

Usage: PYTHONPATH=. python scripts/audit_registry.py [--json]
"""
import argparse
import json
from pathlib import Path

from src.registry.audit import audit, to_markdown
from src.registry.records import load_records

p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
p.add_argument("--json", action="store_true", help="print JSON instead of Markdown tables")
args = p.parse_args()
result = audit(load_records(Path(__file__).resolve().parents[1]))
print(json.dumps(result, ensure_ascii=False, indent=2) if args.json else to_markdown(result))
