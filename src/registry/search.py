from src.registry.records import load_records  # noqa: F401  (re-exported for scripts and tests)


def _values(record, keys):
    out=[]
    for key in keys:
        value=record.get(key)
        if isinstance(value, list): out.extend(str(x).lower() for x in value)
        elif value is not None: out.append(str(value).lower())
    return out


def search(records, query=None, dataset_type=None, language=None, longitudinal=None, access=None):
    q=(query or '').lower().strip()
    results=[]
    for r in records:
        hay=' '.join(_values(r,['id','title','domain','languages','therapy_modalities','clinical_topics','annotations']))
        if q and q not in hay: continue
        if dataset_type and r.get('dataset_type') != dataset_type: continue
        if language and language.lower() not in [str(x).lower() for x in r.get('languages',[])]: continue
        if longitudinal is not None and r.get('longitudinal') != longitudinal: continue
        if access and (r.get('access') or {}).get('level') != access: continue
        results.append(r)
    return results


def summarize(record):
    return {
        'id': record.get('id'),
        'title': record.get('title'),
        'type': record.get('dataset_type'),
        'sessions': record.get('sessions'),
        'languages': record.get('languages',[]),
        'longitudinal': record.get('longitudinal'),
        'access': (record.get('access') or {}).get('level'),
        'canonical_url': record.get('canonical_url'),
    }
