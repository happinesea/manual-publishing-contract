import json
import shutil
import tempfile
import unittest
from pathlib import Path

from tools.validate import validate_manual_links, validate_repository


ROOT = Path(__file__).resolve().parents[1]


class RepositoryValidationTest(unittest.TestCase):
    def validate_manual_example(self, manual):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shutil.copytree(ROOT / "schema", root / "schema")
            (root / "examples/v0.1/test").mkdir(parents=True)
            (root / "examples/v0.1/test/manual.json").write_text(
                json.dumps(manual), encoding="utf-8"
            )
            return validate_repository(root, required_files=())

    def test_repository_is_valid(self):
        self.assertEqual([], validate_repository(ROOT))

    def test_required_contract_artifacts_are_enforced(self):
        with tempfile.TemporaryDirectory() as directory:
            errors = validate_repository(Path(directory))
            self.assertIn("missing required file: schema/v0.1/source.schema.json", errors)
            self.assertIn("missing required file: spec/v0.1/en/evidence-contract.md", errors)
            self.assertIn("missing required file: examples/v0.1/pdf-to-web/manual.json", errors)

    def test_ci_cache_uses_the_declared_dependency_file(self):
        workflow = (ROOT / ".github/workflows/validate.yml").read_text(encoding="utf-8")
        self.assertIn("cache-dependency-path: requirements-dev.txt", workflow)

    def test_invalid_example_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "schema/v0.1").mkdir(parents=True)
            (root / "examples/v0.1/minimal").mkdir(parents=True)
            (root / "schema/v0.1/manual.schema.json").write_text(
                json.dumps(
                    {
                        "$schema": "https://json-schema.org/draft/2020-12/schema",
                        "$id": "https://manualpublishing.org/schema/v0.1/manual.schema.json",
                        "type": "object",
                        "required": ["manual_id"],
                    }
                ),
                encoding="utf-8",
            )
            (root / "examples/v0.1/minimal/manual.json").write_text(
                (ROOT / "tests/fixtures/invalid-manual.json").read_text(encoding="utf-8"),
                encoding="utf-8",
            )
            errors = validate_repository(root, required_files=())
            self.assertTrue(any("manual_id" in error for error in errors), errors)

    def test_source_without_published_at_is_valid(self):
        manual = json.loads((ROOT / "examples/v0.1/minimal/manual.json").read_text(encoding="utf-8"))
        self.assertNotIn("published_at", manual["source"])
        self.assertEqual([], self.validate_manual_example(manual))

    def test_published_at_format_is_enforced_when_present(self):
        manual = json.loads((ROOT / "examples/v0.1/minimal/manual.json").read_text(encoding="utf-8"))
        manual["source"]["published_at"] = "not-a-date"
        errors = self.validate_manual_example(manual)
        self.assertTrue(any("not a 'date'" in error for error in errors), errors)

    def test_duplicate_schema_ids_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "schema/v0.1").mkdir(parents=True)
            schema = {
                "$schema": "https://json-schema.org/draft/2020-12/schema",
                "$id": "https://example.invalid/duplicate.schema.json",
            }
            for name in ("first.schema.json", "second.schema.json"):
                (root / "schema/v0.1" / name).write_text(json.dumps(schema), encoding="utf-8")
            errors = validate_repository(root, required_files=())
            self.assertTrue(any("duplicate schema ID" in error for error in errors), errors)

    def test_broken_relative_markdown_link_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "README.md").write_text("[missing](docs/missing.md)", encoding="utf-8")
            errors = validate_repository(root, required_files=())
            self.assertTrue(any("broken relative link" in error for error in errors), errors)

    def test_translation_requires_canonical_language_notice(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "README.en.md").write_text("# Translation without notice", encoding="utf-8")
            errors = validate_repository(root, required_files=())
            self.assertTrue(any("canonical-language notice" in error for error in errors), errors)

    def test_manual_cross_references_must_resolve(self):
        manual = json.loads((ROOT / "examples/v0.1/pdf-to-web/manual.json").read_text(encoding="utf-8"))
        manual["sections"][0]["source"]["source_id"] = "missing-source"
        manual["provenance"]["evidence"][0]["section_id"] = "missing-section"

        errors = validate_manual_links(manual, "example.json")

        self.assertTrue(any("unknown source_id" in error for error in errors), errors)
        self.assertTrue(any("unknown section_id" in error for error in errors), errors)


if __name__ == "__main__":
    unittest.main()
