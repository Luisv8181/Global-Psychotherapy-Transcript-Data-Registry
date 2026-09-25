"""Load canonical dataset records from data/datasets/.

Every script and test reads records through this module so that parsing
behaves the same everywhere (site build, validation, search, audit).
"""

from pathlib import Path

import yaml

TIMESTAMP_TAG = "tag:yaml.org,2002:timestamp"


class _RecordLoader(yaml.SafeLoader):
    """SafeLoader that keeps dates as ISO strings.

    PyYAML turns `2026-09-24` into a datetime.date, which neither JSON nor the
    JSON Schema `string`/`date` type accept. Records store dates as text.
    """


_RecordLoader.yaml_implicit_resolvers = {
    first: [(tag, regexp) for tag, regexp in resolvers if tag != TIMESTAMP_TAG]
    for first, resolvers in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


class RecordLoadError(Exception):
    def __init__(self, path, message):
        super().__init__(f"{path}: {message}")
        self.path = path


def datasets_dir(root):
    return Path(root) / "data" / "datasets"


def is_template(path):
    return Path(path).name.startswith("_")


def record_paths(root, include_templates=False):
    paths = sorted(datasets_dir(root).glob("*.yaml"))
    return [p for p in paths if include_templates or not is_template(p)]


def load_record(path):
    path = Path(path)
    try:
        record = yaml.load(path.read_text(encoding="utf-8"), Loader=_RecordLoader)
    except yaml.YAMLError as exc:
        # Keep the first line; PyYAML's full message repeats the file contents.
        raise RecordLoadError(path.name, f"invalid YAML: {str(exc).splitlines()[0]} ({_location(exc)})") from exc
    if not isinstance(record, dict):
        raise RecordLoadError(path.name, "record must be a YAML mapping")
    return record


def load_records(root, include_templates=False):
    return [load_record(p) for p in record_paths(root, include_templates)]


def _location(exc):
    mark = getattr(exc, "problem_mark", None)
    return f"line {mark.line + 1}, column {mark.column + 1}" if mark else "unknown location"
