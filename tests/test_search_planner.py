from src.registry.search_planner import (
    _log_channels,
    _log_queries,
    candidate_keys,
    detect_duplicates,
    normalize_name,
    normalize_url,
    plan_queries,
    score_query,
    summarize_search_outcomes,
)


def test_normalize_url_drops_tracking_and_fragment():
    assert normalize_url("HTTPS://WWW.Example.org/data/?utm_source=mail#part") == "https://example.org/data"


def test_normalize_name_is_case_and_punctuation_insensitive():
    assert normalize_name("Psychotherapy: Dataset (2026)") == "psychotherapy dataset 2026"


def test_duplicate_detection_is_review_only_and_matches_doi_url_title():
    rows = [
        {"id": "alpha", "title": "Shared Corpus", "canonical_url": "https://example.org/data?x=1", "doi": "10.1234/ABC"},
        {"id": "beta", "title": "shared corpus", "canonical_url": "https://www.example.org/data#details", "doi": "https://doi.org/10.1234/abc"},
    ]
    matches = detect_duplicates(rows)
    assert {match["matched_on"] for match in matches} == {
        "canonical_url:https://example.org/data",
        "doi:10.1234/abc",
        "title:shared corpus",
    }
    assert rows[0]["id"] == "alpha" and rows[1]["id"] == "beta"


def test_query_scoring_penalizes_repetition_and_rewards_coverage():
    prior = ["psychotherapy transcripts english dataset"]
    common = {
        "gap_tokens": ["German", "psychotherapy", "dataset"],
        "channel": "institutional archive",
        "primary_source_likely": 2,
        "lineage_likely": 1,
    }
    novel = score_query({"query": "German psychotherapy corpus data availability", "undercovered": True, **common}, set(), prior)
    repeated = score_query({"query": "psychotherapy transcripts english dataset", "undercovered": False, **common}, set(), prior)
    assert novel["score"] > repeated["score"]
    assert novel["interpretation"].startswith("research priority only")


def test_invalid_query_scores_fail_closed():
    try:
        score_query({"query": "test", "primary_source_likely": 3}, set(), [])
    except ValueError as exc:
        assert "0, 1, or 2" in str(exc)
    else:
        raise AssertionError("invalid likelihood score should fail")


def test_outcome_summary_keeps_raw_counts_and_uses_smoothed_rates():
    summary = summarize_search_outcomes([{
        "screened": 8, "unique_leads": 2, "primary_opened": 1,
        "scope_passed": 1, "blocked": 1, "duplicate_or_derivative": 2,
        "out_of_scope": 3,
    }])
    assert summary["screened"] == 8
    assert summary["unique_leads"] == 2
    assert summary["unique_lead_yield_smoothed"] == 0.3
    assert summary["primary_open_rate_smoothed"] == 0.5
    assert summary["rates_are_planning_estimates_only"] is True


def test_outcome_summary_rejects_negative_counts():
    try:
        summarize_search_outcomes([{"screened": -1}])
    except ValueError as exc:
        assert "non-negative integer" in str(exc)
    else:
        raise AssertionError("negative outcome counts should fail")


def test_search_log_parser_extracts_exact_query_and_channel():
    log = """| Date | Channel | Query (exact) | Language | Screened | Relevant hits | By |
|---|---|---|---|---|---|---|
| 2026-10-10 | Hub | German therapy corpus | de | 3 | lead | Agent |
| 2026-10-10 | Archive | none | en | 0 | none | Agent |
"""
    assert _log_queries(log) == ["German therapy corpus", "none"]
    assert dict(_log_channels(log)) == {"Hub": 1, "Archive": 1}


def test_plan_queries_is_deterministic_and_does_not_mutate_records():
    records = [{"id": "x", "title": "Known corpus", "canonical_url": "https://example.org"}]
    proposals = [
        {"query": "new undercovered resource", "gap_tokens": ["undercovered"], "channel": "archive", "undercovered": True, "primary_source_likely": 2, "lineage_likely": 1},
    ]
    report_a = plan_queries(proposals, records, "| Date | Channel | Query (exact) | Language | Screened | Relevant hits | By |\n|---|---|---|---|---|---|---|")
    report_b = plan_queries(proposals, records, "| Date | Channel | Query (exact) | Language | Screened | Relevant hits | By |\n|---|---|---|---|---|---|---|")
    assert report_a == report_b
    assert records == [{"id": "x", "title": "Known corpus", "canonical_url": "https://example.org"}]


def test_plan_flags_exact_canonical_url_and_doi_as_review_hints():
    records = [
        {"id": "known", "title": "Known Resource", "canonical_url": "https://example.org/resource", "doi": "10.1000/xyz"},
    ]
    proposals = [
        {"query": "https://www.example.org/resource?utm_source=search", "gap_tokens": ["resource"], "channel": "web", "primary_source_likely": 1, "lineage_likely": 1},
        {"query": "10.1000/xyz", "gap_tokens": ["resource"], "channel": "paper", "primary_source_likely": 1, "lineage_likely": 1},
    ]
    report = plan_queries(proposals, records, "")
    matches = {row["query"]: row["possible_registry_match_fields"] for row in report["ranked_queries"]}
    assert matches["https://www.example.org/resource?utm_source=search"] == ["canonical_url"]
    assert matches["10.1000/xyz"] == ["doi"]
    assert all("human review only" in row["match_policy"] for row in report["ranked_queries"])
