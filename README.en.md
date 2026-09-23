# Manual Publishing Contract

> This document is a translation. The Japanese specification is canonical in case of discrepancies.

[日本語](README.md) | [简体中文](README.zh-CN.md)

## Problem

PDF-only technical manuals are easily overwritten, difficult to search by task, and often lose page-level provenance when converted for the Web. CMS-specific formats also make tables, figures, warnings, versions, and evidence hard to reuse.

Manual Publishing Contract is a vendor-neutral open specification for converting versioned technical manuals into structured content without losing semantic fidelity or traceability to the source.

```text
Source Manual → Versioned Structured Manual → Published Web Content → Machine-readable Evidence
```

It supports preservation of old versions, better accessibility and searchability, traceable AI/search answers, reduced platform lock-in, and reuse by small organizations. It does not claim to be an industry standard or guarantee implementation quality.

## v0.1

- [Canonical Japanese specification](spec/v0.1/ja/manual-publishing-contract.md)
- [English translation](spec/v0.1/en/manual-publishing-contract.md)
- [JSON Schema](schema/v0.1/manual.schema.json)
- [Fictional examples](examples/v0.1/)
- [Architecture](docs/en/architecture.md), [lifecycle](docs/en/lifecycle.md), and [terminology](docs/en/terminology.md)

v0.1 covers source/manual/version identity, section-to-page mapping, table and figure references, publication lifecycle, provenance, evidence, cache metadata, validation, and coexistence of versions. Parsers, OCR, translation, LLM/RAG systems, CMS APIs, advertising, authentication, billing, and vendor product schemas are out of scope.

## Validation

Install `requirements-dev.txt`, then run `python tools/validate.py` and `python -m unittest discover -s tests -v`.

## License

[Apache License 2.0](LICENSE)
