from src.registry.audit import CORE_FIELDS, audit, completeness, is_unknown


def test_unknown_values():
    assert is_unknown(None) and is_unknown("unknown") and is_unknown([]) and is_unknown(["unknown"])
    assert not is_unknown(False) and not is_unknown(0) and not is_unknown("not_applicable")


def test_completeness_reports_unestablished_fields():
    record = {"id": "x", "languages": ["en"], "longitudinal": False, "geography": {"countries": ["unknown"]}, "release_year": 2024}
    result = completeness(record)
    assert "languages" not in result["unknown_fields"]
    assert "longitudinal design" not in result["unknown_fields"]
    assert "geography" in result["unknown_fields"]
    assert "publication or release year" not in result["unknown_fields"]
    assert result["documented"] + len(result["unknown_fields"]) == len(CORE_FIELDS)


def test_audit_orders_least_documented_first():
    rows = audit([{"id": "full", "languages": ["en"], "sessions": 3}, {"id": "empty"}])["records"]
    assert [r["id"] for r in rows] == ["empty", "full"]
