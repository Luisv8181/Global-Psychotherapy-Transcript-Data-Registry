from pathlib import Path
from src.registry.search import load_records, search


def test_search_finds_annomi():
    root=Path(__file__).resolve().parents[1]
    results=search(load_records(root),'motivational')
    assert any(r['id']=='annomi' for r in results)


def test_access_filter():
    root=Path(__file__).resolve().parents[1]
    records=load_records(root)
    for level in ('institutional', 'research-agreement', 'open'):
        expected={r['id'] for r in records if (r.get('access') or {}).get('level') == level}
        assert expected, f'no records with access level {level}'
        assert {r['id'] for r in search(records, access=level)} == expected
