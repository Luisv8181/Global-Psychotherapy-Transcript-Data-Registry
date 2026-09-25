# Contributing

This is a research registry, not a transcript mirror.

Do not upload copyrighted or controlled-access transcripts, therapy recordings, participant identifiers, credentials, or private clinical material.

Submit metadata and official source links only.

## Adding or updating a record

1. Copy `data/datasets/_TEMPLATE.yaml` to `data/datasets/<id>.yaml`. The `id` must be lowercase words joined by hyphens and match the file name.
2. Fill in only what primary sources establish. Leave everything else as `unknown` or `null`.
3. Quote any value that contains a colon followed by a space, for example `title: "HOPE: Counselling Conversations Dataset"`. Unquoted, it is invalid YAML.
4. `access.level` and `redistribution` must use a term from `data/vocabularies/access.yaml`. Put nuance (who holds the data, what the agreement requires) in `access.requirements` or `notes`.
5. A record marked `verified` or `partially-verified` needs at least one `evidence.primary_sources` URL and a `last_verified` date (`YYYY-MM-DD`).
6. Run the checks before opening a pull request:

   ```bash
   pip install -r requirements-dev.txt
   PYTHONPATH=. python scripts/validate_registry.py
   PYTHONPATH=. python -m pytest -q
   ```

CI runs the same checks on every push and pull request, and the Pages site will not deploy while they fail.
