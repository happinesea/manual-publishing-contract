# Evidence Contract v0.1

> This document is a translation. The Japanese specification is canonical in case of discrepancies.

Evidence is independent of any RAG, vector database, LLM, or search product. Each record MUST include `evidence_id`, `manual_id`, `section_id`, `source_id`, and one or more `source_pages`. A structured claim MAY also carry `claim_id`.

The intended chain is `AI/Search Result → Structured Claim → Web Section → Manual Version → Source Document → Source Page`. Evidence MUST NOT be used to legitimize claims absent from the source. See the [evidence schema](../../../schema/v0.1/evidence.schema.json).
