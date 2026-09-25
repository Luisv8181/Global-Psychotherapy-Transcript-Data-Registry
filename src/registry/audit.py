"""Evidence-completeness audit.

For each record, lists which core research fields the reviewed evidence has
not yet established. This is a to-do list for verification, not a quality
score for the dataset itself: an unknown field means "not yet documented
here", never "absent from the dataset".
"""

from collections import Counter

# (label, path into the record). Order is the order shown to reviewers.
CORE_FIELDS = [
    ("source context", ("source_context",)),
    ("languages", ("languages",)),
    ("geography", ("geography", "countries")),
    ("therapy modalities", ("therapy_modalities",)),
    ("sessions", ("sessions",)),
    ("longitudinal design", ("longitudinal",)),
    ("transcript availability", ("transcript", "available")),
    ("access level", ("access", "level")),
    ("redistribution", ("redistribution",)),
    ("license", ("license", "type")),
    ("de-identification", ("privacy", "deidentified")),
    ("publication or release year", ("publication_year", "release_year")),
]


def _get(record, path):
    value = record
    for key in path:
        if not isinstance(value, dict):
            return None
        value = value.get(key)
    return value


def is_unknown(value):
    if value is None:
        return True
    if isinstance(value, str):
        return value.strip().lower() in {"", "unknown"}
    if isinstance(value, (list, tuple)):
        return all(is_unknown(v) for v in value)
    return False


def unknown_fields(record):
    missing = []
    for label, path in CORE_FIELDS:
        if label == "publication or release year":
            known = any(not is_unknown(record.get(k)) for k in path)
        else:
            known = not is_unknown(_get(record, path))
        if not known:
            missing.append(label)
    return missing


def completeness(record):
    missing = unknown_fields(record)
    documented = len(CORE_FIELDS) - len(missing)
    return {
        "documented": documented,
        "total": len(CORE_FIELDS),
        "ratio": round(documented / len(CORE_FIELDS), 3),
        "unknown_fields": missing,
    }


def audit(records):
    rows = sorted(
        ({"id": r.get("id"), "title": r.get("title"), "status": r.get("status"), **completeness(r)} for r in records),
        key=lambda row: (row["ratio"], row["id"] or ""),
    )
    gaps = Counter(label for row in rows for label in row["unknown_fields"])
    return {"records": rows, "field_gaps": [[label, gaps.get(label, 0)] for label, _ in CORE_FIELDS]}


def to_markdown(result):
    lines = [
        "| Record | Status | Documented | Not yet established |",
        "|---|---|---|---|",
    ]
    for row in result["records"]:
        gaps = ", ".join(row["unknown_fields"]) or "—"
        lines.append(f"| {row['id']} | {row['status']} | {row['documented']}/{row['total']} | {gaps} |")
    lines += ["", "| Field | Records where it is not yet established |", "|---|---|"]
    lines += [f"| {label} | {count} |" for label, count in result["field_gaps"]]
    return "\n".join(lines)
