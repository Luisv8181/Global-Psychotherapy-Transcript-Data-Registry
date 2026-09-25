# Registry Search

The registry includes a small local search layer over canonical YAML records.

Examples:

```bash
python scripts/search_registry.py motivational
python scripts/search_registry.py --language en
python scripts/search_registry.py --type real
python scripts/search_registry.py --access institutional
python scripts/search_registry.py --longitudinal
```

Search is intentionally conservative. It only searches fields present in registry records and does not pretend to search transcript contents that the registry does not store.
