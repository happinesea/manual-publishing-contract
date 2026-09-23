# Publishing Contract v0.1

> This document is a translation. The Japanese specification is canonical in case of discrepancies.

The standard model is `Source → Build / Transform → Validate → Publish → Static/Page Cache/CDN → Reader`. Converting the source to HTML on every request is not the standard model.

Allowed states are `draft`, `generated`, `validated`, `published`, `deprecated`, and `archived`. Implementations SHOULD validate schema and content fidelity before publication. See [lifecycle](../../../docs/en/lifecycle.md) and the [publication schema](../../../schema/v0.1/publication.schema.json).
