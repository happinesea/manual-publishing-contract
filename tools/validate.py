#!/usr/bin/env python3
"""Validate schemas, examples, links, encoding, and repository hygiene."""

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

from jsonschema import Draft202012Validator
from referencing import Registry, Resource


REQUIRED_FILES = (
    "README.md",
    "README.en.md",
    "README.zh-CN.md",
    "CONTRIBUTING.md",
    "CHANGELOG.md",
    "LICENSE",
    "requirements-dev.txt",
    "tools/validate.py",
    "tests/test_validate.py",
    "tests/fixtures/invalid-manual.json",
    ".github/workflows/validate.yml",
    "schema/v0.1/manual.schema.json",
    "schema/v0.1/source.schema.json",
    "schema/v0.1/section.schema.json",
    "schema/v0.1/publication.schema.json",
    "schema/v0.1/evidence.schema.json",
    "examples/v0.1/minimal/manual.json",
    "examples/v0.1/versioned-manual/v1.json",
    "examples/v0.1/versioned-manual/v2.json",
    "examples/v0.1/versioned-manual/v3.json",
    "examples/v0.1/pdf-to-web/manual.json",
)
for _language in ("ja", "en", "zh-CN"):
    REQUIRED_FILES += tuple(
        f"spec/v0.1/{_language}/{name}"
        for name in (
            "manual-publishing-contract.md",
            "source-contract.md",
            "structure-contract.md",
            "version-contract.md",
            "publishing-contract.md",
            "evidence-contract.md",
        )
    )
    REQUIRED_FILES += tuple(
        f"docs/{_language}/{name}"
        for name in ("architecture.md", "lifecycle.md", "terminology.md")
    )
TEXT_SUFFIXES = {".md", ".json", ".py", ".txt", ".yml", ".yaml"}
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
SECRET_PATTERNS = (
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
)
EN_NOTICE = "This document is a translation. The Japanese specification is canonical in case of discrepancies."
ZH_NOTICE = "本文档为翻译版本。如与日文规范存在差异，以日文规范为准。"


def _json_files(root, relative):
    directory = root / relative
    return sorted(directory.rglob("*.json")) if directory.exists() else []


def validate_manual_links(manual, label):
    """Validate references that JSON Schema cannot express."""
    errors = []
    manual_id = manual["manual_id"]
    source_id = manual["source"]["source_id"]
    sections = {}
    for section in manual["sections"]:
        section_id = section["section_id"]
        if section_id in sections:
            errors.append(f"{label}: duplicate section_id {section_id}")
        sections[section_id] = section
        if section["source"]["source_id"] != source_id:
            errors.append(f"{label}: section {section_id} has unknown source_id {section['source']['source_id']}")

    if source_id not in manual["provenance"]["source_ids"]:
        errors.append(f"{label}: provenance omits source_id {source_id}")

    evidence_ids = set()
    for evidence in manual["provenance"]["evidence"]:
        evidence_id = evidence["evidence_id"]
        if evidence_id in evidence_ids:
            errors.append(f"{label}: duplicate evidence_id {evidence_id}")
        evidence_ids.add(evidence_id)
        if evidence["manual_id"] != manual_id:
            errors.append(f"{label}: evidence {evidence_id} has unknown manual_id {evidence['manual_id']}")
        section = sections.get(evidence["section_id"])
        if section is None:
            errors.append(f"{label}: evidence {evidence_id} has unknown section_id {evidence['section_id']}")
        elif not set(evidence["source_pages"]).issubset(section["source"]["pages"]):
            errors.append(f"{label}: evidence {evidence_id} cites pages outside section {evidence['section_id']}")
        if evidence["source_id"] != source_id:
            errors.append(f"{label}: evidence {evidence_id} has unknown source_id {evidence['source_id']}")
    return errors


def validate_repository(root, required_files=REQUIRED_FILES):
    root = Path(root).resolve()
    errors = []

    for relative in required_files:
        if not (root / relative).is_file():
            errors.append(f"missing required file: {relative}")

    schemas = {}
    schema_ids = {}
    for path in _json_files(root, "schema"):
        try:
            schema = json.loads(path.read_text(encoding="utf-8"))
            Draft202012Validator.check_schema(schema)
        except Exception as error:
            errors.append(f"invalid schema {path.relative_to(root)}: {error}")
            continue
        schema_id = schema.get("$id")
        if schema_id in schema_ids:
            errors.append(f"duplicate schema ID {schema_id}: {schema_ids[schema_id]} and {path.relative_to(root)}")
        elif schema_id:
            schema_ids[schema_id] = path.relative_to(root)
        schemas[path.name] = schema

    manual_schema = schemas.get("manual.schema.json")
    if manual_schema:
        registry = Registry()
        for schema in schemas.values():
            if schema.get("$id"):
                registry = registry.with_resource(schema["$id"], Resource.from_contents(schema))
        validator = Draft202012Validator(
            manual_schema,
            registry=registry,
            format_checker=Draft202012Validator.FORMAT_CHECKER,
        )
        for path in _json_files(root, "examples"):
            try:
                instance = json.loads(path.read_text(encoding="utf-8"))
            except (UnicodeDecodeError, json.JSONDecodeError) as error:
                errors.append(f"invalid example JSON {path.relative_to(root)}: {error}")
                continue
            instance_errors = sorted(validator.iter_errors(instance), key=lambda item: list(item.path))
            for error in instance_errors:
                location = ".".join(str(part) for part in error.path) or "<root>"
                errors.append(f"invalid example {path.relative_to(root)} at {location}: {error.message}")
            if not instance_errors:
                errors.extend(validate_manual_links(instance, str(path.relative_to(root))))

    for path in sorted(root.rglob("*")):
        if not path.is_file() or ".git" in path.parts or ".venv" in path.parts:
            continue
        if path.suffix.lower() in TEXT_SUFFIXES or path.name in {"LICENSE", ".gitignore"}:
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError as error:
                errors.append(f"invalid UTF-8 {path.relative_to(root)}: {error}")
                continue
            for pattern in SECRET_PATTERNS:
                if pattern.search(text):
                    errors.append(f"possible secret in {path.relative_to(root)}")
            if path.suffix.lower() == ".md":
                relative = path.relative_to(root).as_posix()
                expected_notice = None
                if relative == "README.en.md" or relative.startswith(("spec/v0.1/en/", "docs/en/")):
                    expected_notice = EN_NOTICE
                elif relative == "README.zh-CN.md" or relative.startswith(("spec/v0.1/zh-CN/", "docs/zh-CN/")):
                    expected_notice = ZH_NOTICE
                if expected_notice and expected_notice not in text[:500]:
                    errors.append(f"missing canonical-language notice in {relative}")
                for target in LINK_RE.findall(text):
                    target = target.strip().split()[0].strip("<>")
                    if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                        continue
                    relative_target = unquote(target.split("#", 1)[0])
                    if relative_target and not (path.parent / relative_target).resolve().exists():
                        errors.append(f"broken relative link in {path.relative_to(root)}: {target}")

    return errors


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", default=Path(__file__).resolve().parents[1])
    args = parser.parse_args(argv)
    errors = validate_repository(args.root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Manual Publishing Contract validation PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
