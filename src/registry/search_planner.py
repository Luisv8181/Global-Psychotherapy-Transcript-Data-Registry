"""Deterministic search planning helpers for the psychotherapy registry.

The ranking guides research effort only. It does not infer evidence, scope,
provenance, access rights, or licensing and never modifies registry records.
"""
from __future__ import annotations

import re
from collections import Counter
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit


def normalize_url(value: object) -> str:
    """Normalize a URL for duplicate detection, preserving meaningful paths."""
    raw = str(value or "").strip()
    if not raw:
        return ""
    parts = urlsplit(raw)
    if not parts.scheme or not parts.netloc:
        return raw.casefold().rstrip("/")
    host = parts.netloc.casefold()
    if host.startswith("www."):
        host = host[4:]
    path = re.sub(r"/+", "/", parts.path).rstrip("/")
    return urlunsplit((parts.scheme.casefold(), host, path, "", "")).casefold()


def normalize_name(value: object) -> str:
    """A conservative title key; do not use it as proof of identity."""
    text = str(value or "").casefold()
    text = re.sub(r"https?://\S+", " ", text)
    return " ".join(re.findall(r"[a-z0-9]+", text))


def candidate_keys(record: dict) -> set[str]:
    keys: set[str] = set()
    for field in ("canonical_url", "doi", "id", "title"):
        value = record.get(field)
        if not value:
            continue
        if field == "canonical_url":
            key = normalize_url(value)
        elif field == "doi":
            key = str(value).casefold().replace("https://doi.org/", "").replace("http://doi.org/", "").strip()
        elif field == "title":
            key = normalize_name(value)
        else:
            key = str(value).casefold().strip()
        if key:
            keys.add(f"{field}:{key}")
    return keys


def detect_duplicates(candidates: list[dict]) -> list[dict]:
    """Return pairs sharing a canonical URL, DOI, ID, or normalized title.

    This is a review queue. Similarity is never enough to merge records
    automatically; title collisions can be legitimate and require inspection.
    """
    seen: dict[str, list[int]] = {}
    pairs: list[dict] = []
    for index, record in enumerate(candidates):
        keys = candidate_keys(record)
        for key in sorted(keys):
            for previous in seen.get(key, []):
                pairs.append({
                    "left_index": previous,
                    "right_index": index,
                    "matched_on": key,
                    "left_id": candidates[previous].get("id"),
                    "right_id": record.get("id"),
                })
            seen.setdefault(key, []).append(index)
    return pairs


def _tokenize(value: object) -> set[str]:
    return set(normalize_name(value).split())


def _markdown_table_rows(search_log: str, header_name: str) -> list[list[str]]:
    lines = search_log.splitlines()
    header_index = next((i for i, line in enumerate(lines) if header_name in line), None)
    if header_index is None:
        return []
    rows: list[list[str]] = []
    for line in lines[header_index + 1:]:
        if not line.strip().startswith("|"):
            break
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if cells and set(cells[0]) <= {"-", ":", " "}:
            continue
        if cells and cells[0].casefold() == "date":
            continue
        rows.append(cells)
    return rows


def _log_queries(search_log: str) -> list[str]:
    """Extract exact queries from the current pipe-delimited Markdown log."""
    return [row[2] for row in _markdown_table_rows(search_log, "Query (exact)") if len(row) >= 7 and row[2]]

def _log_channels(search_log: str) -> Counter:
    """Count logged searches per channel for a transparent diversity nudge."""
    counts: Counter = Counter()
    for row in _markdown_table_rows(search_log, "Query (exact)"):
        if len(row) >= 7 and row[1]:
            counts[row[1]] += 1
    return counts

def score_query(query: dict, covered_tokens: set[str], prior_queries: list[str],
                channel_counts: Counter | None = None) -> dict:
    """Score a proposed query on explicit 0-2 dimensions.

    Required fields: query, gap_tokens, channel, undercovered (bool),
    primary_source_likely (0, 1, or 2), lineage_likely (0, 1, or 2).
    """
    raw_query = str(query.get("query", "")).strip()
    if not raw_query:
        raise ValueError("query must be a non-empty string")
    tokens = _tokenize(raw_query)
    gap_tokens = _tokenize(" ".join(query.get("gap_tokens", [])))
    if not gap_tokens:
        gap_tokens = tokens
    # Keep integer values and the rubric explicit for agents to audit.
    gap_fit = 2 if len(tokens & gap_tokens) >= 3 else 1 if tokens & gap_tokens else 0
    max_prior_overlap = 0.0
    for previous in prior_queries:
        old = _tokenize(previous)
        if not old:
            continue
        overlap = len(tokens & old) / max(1, len(tokens | old))
        max_prior_overlap = max(max_prior_overlap, overlap)
    novelty = 0 if max_prior_overlap >= 0.65 else 1 if max_prior_overlap >= 0.35 else 2
    inspectability = int(query.get("primary_source_likely", 1))
    lineage = int(query.get("lineage_likely", 1))
    if inspectability not in (0, 1, 2) or lineage not in (0, 1, 2):
        raise ValueError("primary_source_likely and lineage_likely must be 0, 1, or 2")
    coverage = 2 if query.get("undercovered", False) else 1
    channel = str(query.get("channel", "unspecified"))
    penalty = 0
    channel_counts = channel_counts or Counter()
    if query.get("known_failure", False):
        penalty -= 2
    if max_prior_overlap >= 0.65:
        penalty -= 1
    # A channel that dominates past searches gets a small diversity penalty.
    if channel_counts and channel in channel_counts and channel_counts[channel] >= max(channel_counts.values()):
        penalty -= 1
    score = gap_fit + novelty + inspectability + lineage + coverage + penalty
    return {
        "query": raw_query,
        "channel": channel,
        "score": score,
        "dimensions": {
            "gap_fit": gap_fit,
            "novelty": novelty,
            "primary_source_likelihood": inspectability,
            "lineage_value": lineage,
            "coverage_balance": coverage,
            "penalty": penalty,
            "max_prior_token_jaccard": round(max_prior_overlap, 3),
        },
        "interpretation": "research priority only; not evidence, probability, scope, provenance, or license",
    }


def plan_queries(proposals: list[dict], records: list[dict], search_log: str) -> dict:
    """Rank queries and flag exact known-identity matches as review hints."""
    prior = _log_queries(search_log)
    channels = _log_channels(search_log)
    known_keys: set[str] = set()
    for record in records:
        known_keys.update(candidate_keys(record))
    ranked = [score_query(item, _tokenize(" ".join(item.get("gap_tokens", []))), prior, channels) for item in proposals]
    ranked.sort(key=lambda item: (-item["score"], item["query"].casefold()))
    return {
        "algorithm_version": "1.0",
        "records_examined": len(records),
        "prior_queries_found": len(prior),
        "channels_seen": dict(sorted(channels.items())),
        "ranked_queries": ranked,
        "known_identity_keys": len(known_keys),
        "duplicate_detection": "use detect_duplicates on candidate metadata; exact matches are review-only",
    }


def summarize_search_outcomes(outcomes: list[dict]) -> dict:
    """Report raw counts and smoothed planning rates for one search batch."""
    required = ("screened", "unique_leads", "primary_opened", "scope_passed",
                "blocked", "duplicate_or_derivative", "out_of_scope")
    totals = {name: 0 for name in required}
    for row in outcomes:
        for name in required:
            value = row.get(name, 0)
            if not isinstance(value, int) or value < 0:
                raise ValueError(f"{name} must be a non-negative integer")
            totals[name] += value
    totals["unique_lead_yield_smoothed"] = round(
        (totals["unique_leads"] + 1) / (totals["screened"] + 2), 4
    )
    totals["primary_open_rate_smoothed"] = round(
        (totals["primary_opened"] + 1) / (totals["unique_leads"] + 2), 4
    )
    totals["rates_are_planning_estimates_only"] = True
    return totals
