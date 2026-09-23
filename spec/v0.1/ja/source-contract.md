# Source Contract v0.1

Source Contractは変化し得るURLとartifact identityを分離します。

原典は`source_id`、type、title、language、version、file name、SHA-256 checksumを持たなければなりません（MUST）。`published_at`と`uri`は任意です（MAY）。`published_at`が存在する場合はRFC 3339 full-date（`YYYY-MM-DD`）でなければなりません。発行日が不明な場合はfieldを省略でき、架空の日付を補完してはなりません（MUST NOT）。URIだけをidentityとして扱ってはなりません（MUST NOT）。同じtitleでもchecksumまたはversionが異なるartifactは別sourceとして保持できます。

適合データは[source schema](../../../schema/v0.1/source.schema.json)を満たします。
