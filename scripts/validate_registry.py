from pathlib import Path
from src.registry.validator import load_records, validate_records
root=Path(__file__).resolve().parents[1]
errors=validate_records(load_records(root))
if errors:
    print('\n'.join(errors)); raise SystemExit(1)
print('Registry validation passed.')
