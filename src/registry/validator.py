from pathlib import Path
import yaml

REQUIRED_KEYS = {'id','title','canonical_url','status','dataset_type'}

def load_records(root):
    root = Path(root)
    return [yaml.safe_load(p.read_text(encoding='utf-8')) for p in sorted((root/'data/datasets').glob('*.yaml'))]

def validate_records(records):
    errors=[]; seen=set()
    for r in records:
        if not REQUIRED_KEYS.issubset(r or {}):
            errors.append(f"missing required keys: {sorted(REQUIRED_KEYS-set(r or {}))}")
        rid=(r or {}).get('id')
        if rid in seen: errors.append(f'duplicate id: {rid}')
        seen.add(rid)
    return errors
