# Evidence Contract v0.1

> 本文档为翻译版本。如与日文规范存在差异，以日文规范为准。

Evidence不依赖任何RAG、vector database、LLM或搜索产品。每条记录必须包含`evidence_id`、`manual_id`、`section_id`、`source_id`以及一个或多个`source_pages`。结构化claim还可以包含`claim_id`。

目标chain为`AI/搜索结果 → Structured Claim → Web章节 → 手册版本 → 源文档 → 源页`。不得用Evidence为源文档中不存在的推测提供正当性。参见[evidence schema](../../../schema/v0.1/evidence.schema.json)。
