# Manual Publishing Contract v0.1

> This document is a translation. The Japanese specification is canonical in case of discrepancies.

## Status and terminology

This contract defines the boundary for build-time generation, validation, and publication of versioned technical manuals while preserving source traceability. The contract is not a parser, translator, builder, publisher, CMS, search engine, or AI service.

MUST is required for conformance, SHOULD may be omitted only for a documented reason, and MAY is optional.

## Scope

v0.1 covers source and manual identity, versions, page mapping, sections, table/figure references, Web mapping, publication lifecycle, provenance, evidence, cache metadata, validation, and coexistence of versions. Parsers, OCR, translation engines, LLM/RAG implementations, CMS APIs, advertising, authentication, billing, and vendor product schemas are out of scope.

## Core contracts

1. [Source](source-contract.md): identify artifacts with checksums rather than URLs alone.
2. [Structure](structure-contract.md): map each Web section to one or more source pages.
3. [Version](version-contract.md): separate products, manual families, and manual versions.
4. [Publishing](publishing-contract.md): describe build, validation, publication, and cache state.
5. [Evidence](evidence-contract.md): trace a claim or result back to source pages.

Conforming manuals MUST satisfy the [manual schema](../../../schema/v0.1/manual.schema.json). Stable human-readable IDs are recommended, but vendor naming is not mandated.

## Fidelity and coexistence

Web content MUST preserve meaning, heading hierarchy, tables, warnings, numeric values, figure references, and page provenance. Pixel-perfect visual pagination is optional. A Web section may map to multiple source pages.

V1, V2, and V3 of a family may coexist. `supersedes` does not mean deletion. Publishing a newer version MUST NOT remove the retrievability of an older version.

Vendor-specific profiles MAY implement this contract, but private data, credentials, proprietary manuals, and vendor assets MUST NOT be added to this repository.
