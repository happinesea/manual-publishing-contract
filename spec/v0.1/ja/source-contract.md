# Source Contract v0.1

Source Contractは変化し得るURLとartifact identityを分離します。

原典は`source_id`、type、title、language、version、`published_at`、file name、SHA-256 checksumを持たなければなりません（MUST）。`uri`は任意です（MAY）。URIだけをidentityとして扱ってはなりません（MUST NOT）。同じtitleでもchecksumまたはversionが異なるartifactは別sourceとして保持できます。

適合データは[source schema](../../../schema/v0.1/source.schema.json)を満たします。
