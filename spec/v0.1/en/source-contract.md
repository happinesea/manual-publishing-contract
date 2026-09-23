# Source Contract v0.1

> This document is a translation. The Japanese specification is canonical in case of discrepancies.

A source MUST include `source_id`, type, title, language, version, file name, and SHA-256 checksum. `published_at` and `uri` are optional. When present, `published_at` MUST be an RFC 3339 full-date (`YYYY-MM-DD`). When the publication date is unknown, the field may be omitted and a fabricated date MUST NOT be supplied. A URL MUST NOT be the sole artifact identity. Artifacts with the same title but a different checksum or version may coexist.

See the [source schema](../../../schema/v0.1/source.schema.json).
