from pathlib import Path
import json
import yaml
ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'data'/'datasets'
OUT=ROOT/'site'/'data'
OUT.mkdir(parents=True,exist_ok=True)
records=[]
for path in sorted(DATA.glob('*.yaml')):
    with path.open(encoding='utf-8') as f:
        record=yaml.safe_load(f)
    if isinstance(record,dict):
        record['_source_file']=str(path.relative_to(ROOT))
        records.append(record)
with (OUT/'datasets.json').open('w',encoding='utf-8') as f:
    json.dump(records,f,ensure_ascii=False,indent=2,sort_keys=True)
print(f'Built {len(records)} dataset records')
