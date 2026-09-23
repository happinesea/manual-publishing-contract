# Evidence Contract v0.1

Evidenceは特定のRAG、vector database、LLM、検索engineに依存しません。各evidenceは`evidence_id`、`manual_id`、`section_id`、`source_id`、1件以上の`source_pages`を持たなければなりません（MUST）。structured claimがある場合は`claim_id`を保持できます（MAY）。

```text
AI / Search Result → Structured Claim → Web Section → Manual Version → Source Document → Source Page
```

Evidenceは原典に存在しない推測を正当化するために使用してはなりません。適合データは[evidence schema](../../../schema/v0.1/evidence.schema.json)を満たします。
