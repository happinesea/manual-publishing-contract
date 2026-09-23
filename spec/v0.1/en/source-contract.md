# Source Contract v0.1

> This document is a translation. The Japanese specification is canonical in case of discrepancies.

A source MUST include `source_id`, type, title, language, version, `published_at`, file name, and SHA-256 checksum. `uri` is optional. A URL MUST NOT be the sole artifact identity. Artifacts with the same title but a different checksum or version may coexist.

See the [source schema](../../../schema/v0.1/source.schema.json).
