from pathlib import Path
from src.registry.search import load_records, search


def test_search_finds_annomi():
    root=Path(__file__).resolve().parents[1]
    results=search(load_records(root),'motivational')
    assert any(r['id']=='annomi' for r in results)


def test_access_filter():
    root=Path(__file__).resolve().parents[1]
    results=search(load_records(root),access='institutional')
    assert {r['id'] for r in results} >= {'alexander-street-cpt-volume-1','avatar-therapy-dialogue-corpus'}
