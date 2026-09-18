#!/usr/bin/env python3
"""Validate AIVE Finding Records against the v3 schema.

Usage:
    python validate.py path/to/record.json [more.json ...]
    python validate.py examples/*.json

Exit status is 0 if every file validates, 1 otherwise.
"""
import json
import sys
from pathlib import Path

try:
    from jsonschema import Draft7Validator, FormatChecker
except ImportError:  # pragma: no cover
    sys.exit("jsonschema is required: pip install jsonschema")

SCHEMA_PATH = Path(__file__).parent / "aive.schema.v3.json"


def main(paths):
    schema = json.loads(SCHEMA_PATH.read_text())
    Draft7Validator.check_schema(schema)
    validator = Draft7Validator(schema, format_checker=FormatChecker())

    failed = 0
    for p in paths:
        record = json.loads(Path(p).read_text())
        errors = sorted(validator.iter_errors(record), key=lambda e: list(e.path))
        if errors:
            failed += 1
            print(f"FAIL {p}")
            for e in errors:
                loc = "/".join(str(x) for x in e.path) or "<root>"
                print(f"  {loc}: {e.message}")
        else:
            print(f"OK   {p}  ({record.get('aive_id', '?')})")
    return 1 if failed else 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1:]))
