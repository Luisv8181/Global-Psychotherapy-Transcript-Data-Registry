import argparse
from pathlib import Path
from src.registry.search import load_records, search, summarize

p=argparse.ArgumentParser(description='Search the psychotherapy dataset registry')
p.add_argument('query', nargs='?', default='')
p.add_argument('--type', dest='dataset_type')
p.add_argument('--language')
p.add_argument('--longitudinal', action='store_true')
p.add_argument('--access')
args=p.parse_args()
root=Path(__file__).resolve().parents[1]
records=load_records(root)
for record in search(records,args.query,args.dataset_type,args.language,True if args.longitudinal else None,args.access):
    print(summarize(record))
