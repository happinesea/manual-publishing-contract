# Architecture

> This document is a translation. The Japanese specification is canonical in case of discrepancies.

The contract is a data boundary, not a transformation or delivery system.

```mermaid
flowchart TD
    A[Source Manual] --> B[Parser / Translator / Builder]
    B --> C[Manual Publishing Contract]
    C --> D[Validator]
    D --> E[Publisher Adapter]
    E --> F[CMS / Static Site / Headless CMS]
    F --> G[Cache / CDN]
    G --> H[User / Search / AI]
```

Converters produce contract-conforming data, validators inspect it, and publisher adapters map it to delivery systems. Every implementation can be replaced; no vendor, CMS, or AI provider is required. Build-time artifacts retain source identity, manual version, section/page mappings, publication metadata, and evidence.
