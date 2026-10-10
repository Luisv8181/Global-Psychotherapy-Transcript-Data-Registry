"""Plan the next discovery queries using registry and search-log evidence.

Example:
  PYTHONPATH=. python scripts/plan_search.py --gap "German real-world psychotherapy dialogue" \
      --channel "institutional repositories" --undercovered \
      --primary-source-likely 2 --lineage-likely 1 \
      --query "Psychotherapie echte Beratungsgespräche Korpus Datensatz" \
      --json

Multiple --query and related options can be supplied as JSON proposal files using
--proposals. The tool only ranks research effort; it never verifies or modifies
dataset records.
"""
import argparse
import json
from pathlib import Path

from src.registry.records import load_records
from src.registry.search_planner import plan_queries


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--gap", default="", help="coverage gap this query targets")
    parser.add_argument("--channel", default="unspecified")
    parser.add_argument("--undercovered", action="store_true")
    parser.add_argument("--primary-source-likely", type=int, choices=(0, 1, 2), default=1)
    parser.add_argument("--lineage-likely", type=int, choices=(0, 1, 2), default=1)
    parser.add_argument("--known-failure", action="store_true")
    parser.add_argument("--query", action="append", default=[], help="proposed exact query; repeatable")
    parser.add_argument("--proposals", type=Path, help="JSON file containing an array of proposal objects")
    parser.add_argument("--log", type=Path, default=Path("docs/search-log.md"))
    parser.add_argument("--json", action="store_true", help="print machine-readable JSON")
    return parser.parse_args()


def main():
    args = parse_args()
    root = Path(__file__).resolve().parents[1]
    log_path = args.log if args.log.is_absolute() else root / args.log
    if not log_path.is_file():
        raise SystemExit(f"Search log not found: {log_path}")
    proposals = []
    if args.proposals:
        proposal_path = args.proposals if args.proposals.is_absolute() else root / args.proposals
        try:
            proposals = json.loads(proposal_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            raise SystemExit(f"Unable to read proposal JSON: {exc}") from exc
        if not isinstance(proposals, list) or any(not isinstance(row, dict) for row in proposals):
            raise SystemExit("Proposal JSON must be an array of objects")
    for query in args.query:
        proposals.append({
            "query": query,
            "gap_tokens": args.gap.split(),
            "channel": args.channel,
            "undercovered": args.undercovered,
            "primary_source_likely": args.primary_source_likely,
            "lineage_likely": args.lineage_likely,
            "known_failure": args.known_failure,
        })
    if not proposals:
        raise SystemExit("Supply at least one --query or --proposals JSON file")
    records = load_records(root)
    report = plan_queries(proposals, records, log_path.read_text(encoding="utf-8"))
    ranked = report["ranked_queries"]
    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        print(f"Registry records examined: {report['records_examined']}")
        print(f"Prior logged queries parsed: {report['prior_queries_found']}")
        for index, row in enumerate(ranked, 1):
            dims = row["dimensions"]
            print(f"{index}. [{row['score']}] {row['query']}")
            print(f"   channel={row['channel']} gap={dims['gap_fit']} novelty={dims['novelty']} "
                  f"source={dims['primary_source_likelihood']} lineage={dims['lineage_value']} "
                  f"coverage={dims['coverage_balance']} penalty={dims['penalty']}")
            print(f"   {row['interpretation']}")


if __name__ == "__main__":
    main()
