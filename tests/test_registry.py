from pathlib import Path
from src.registry.validator import load_records, validate_records

def test_registry_records_validate():
    root=Path(__file__).resolve().parents[1]
    assert validate_records(load_records(root)) == []
