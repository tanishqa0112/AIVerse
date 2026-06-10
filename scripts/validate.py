#!/usr/bin/env python3
"""Validate AIVerse data files against JSON Schema."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import jsonschema
import yaml

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_ENTITY = ROOT / "schema" / "entity.schema.json"
SCHEMA_PULSE = ROOT / "schema" / "market-pulse.schema.json"
ENTITY_DIRS = [ROOT / "data" / "tools", ROOT / "data" / "llms", ROOT / "data" / "agents"]
PULSE_DIR = ROOT / "data" / "market-pulse"


def load_schema(path: Path) -> dict:
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def validate_entities() -> list[str]:
    schema = load_schema(SCHEMA_ENTITY)
    validator = jsonschema.Draft202012Validator(schema)
    errors: list[str] = []
    seen_ids: dict[str, Path] = {}

    for folder in ENTITY_DIRS:
        if not folder.is_dir():
            errors.append(f"Missing directory: {folder.relative_to(ROOT)}")
            continue
        for path in sorted(folder.glob("*.json")):
            with path.open(encoding="utf-8") as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError as e:
                    errors.append(f"{path.relative_to(ROOT)}: invalid JSON ({e})")
                    continue
            eid = data.get("id")
            if isinstance(eid, str):
                if eid in seen_ids:
                    errors.append(
                        f"Duplicate id {eid!r}: {path.relative_to(ROOT)} and {seen_ids[eid].relative_to(ROOT)}"
                    )
                else:
                    seen_ids[eid] = path
            stem = path.stem
            if isinstance(eid, str) and eid != stem:
                errors.append(
                    f"{path.relative_to(ROOT)}: id {eid!r} must match filename stem {stem!r}"
                )

            for err in validator.iter_errors(data):
                loc = ".".join(str(p) for p in err.absolute_path) or "(root)"
                errors.append(f"{path.relative_to(ROOT)}: [{loc}] {err.message}")

    return errors


def validate_market_pulse() -> list[str]:
    schema = load_schema(SCHEMA_PULSE)
    validator = jsonschema.Draft202012Validator(schema)
    errors: list[str] = []
    seen_ids: dict[str, Path] = {}

    if not PULSE_DIR.is_dir():
        return [f"Missing directory: {PULSE_DIR.relative_to(ROOT)}"]

    for path in sorted(PULSE_DIR.glob("*.yml")) + sorted(PULSE_DIR.glob("*.yaml")):
        with path.open(encoding="utf-8") as f:
            try:
                data = yaml.safe_load(f)
            except yaml.YAMLError as e:
                errors.append(f"{path.relative_to(ROOT)}: invalid YAML ({e})")
                continue
        if data is None:
            errors.append(f"{path.relative_to(ROOT)}: empty file")
            continue
        if not isinstance(data, list):
            errors.append(f"{path.relative_to(ROOT)}: root must be a YAML list")
            continue

        for err in validator.iter_errors(data):
            loc = ".".join(str(p) for p in err.absolute_path) or "(root)"
            errors.append(f"{path.relative_to(ROOT)}: [{loc}] {err.message}")

        for item in data:
            if isinstance(item, dict) and "id" in item:
                eid = item["id"]
                if isinstance(eid, str):
                    if eid in seen_ids:
                        errors.append(
                            f"Duplicate market-pulse id {eid!r}: {path.relative_to(ROOT)} and {seen_ids[eid].relative_to(ROOT)}"
                        )
                    else:
                        seen_ids[eid] = path

    return errors


def main() -> int:
    all_errors = validate_entities() + validate_market_pulse()
    if all_errors:
        print("Validation failed:\n", file=sys.stderr)
        for line in all_errors:
            print(f"  - {line}", file=sys.stderr)
        return 1
    print("OK: all data files validate.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
