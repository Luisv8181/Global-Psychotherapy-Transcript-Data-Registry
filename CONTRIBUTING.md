# Contributing

This is a research registry, not a transcript mirror.

Do not upload copyrighted or controlled-access transcripts, therapy recordings, participant identifiers, credentials, or private clinical material.

Submit metadata and official source links only.

**AI agents and automated contributors must follow `AGENTS.md`.** People are encouraged to read it too; it records the evidence and licensing mistakes this registry has already made.

## Adding videos

Video catalog entries hold metadata and links only. Read `docs/video-catalog.md` first, especially the rules for videos that show real clients.

## Adding or updating a record

1. Copy `data/datasets/_TEMPLATE.yaml` to `data/datasets/<id>.yaml`. The `id` must be lowercase words joined by hyphens and match the file name.
2. Fill in only what primary sources establish. Leave everything else as `unknown` or `null`.
3. Quote any value that contains a colon followed by a space, for example `title: "HOPE: Counselling Conversations Dataset"`. Unquoted, it is invalid YAML.
4. `access.level` and `redistribution` must use a term from `data/vocabularies/access.yaml`. Put nuance (who holds the data, what the agreement requires) in `access.requirements` or `notes`.
5. Record the **dataset's** license, not the paper's. A journal article's open-access license (often CC BY) says nothing about the data. Set `license.source` to the page where you read the dataset's own license: a repository LICENSE file, a dataset card, or a data repository record. Validation warns when `license.verified: true` has no `license.source`.
6. A record marked `verified` or `partially-verified` needs at least one `evidence.primary_sources` URL and a `last_verified` date (`YYYY-MM-DD`).
7. Run the checks before opening a pull request:

   ```bash
   pip install -r requirements-dev.txt
   PYTHONPATH=. python scripts/validate_registry.py
   PYTHONPATH=. python -m pytest -q
   ```

CI runs the same checks on every push and pull request, and the Pages site will not deploy while they fail.
