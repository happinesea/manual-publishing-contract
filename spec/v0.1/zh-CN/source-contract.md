# Source Contract v0.1

> 本文档为翻译版本。如与日文规范存在差异，以日文规范为准。

源文档必须包含`source_id`、类型、标题、语言、版本、文件名和SHA-256 checksum。`published_at`和`uri`为可选。存在`published_at`时，其值必须是RFC 3339 full-date（`YYYY-MM-DD`）。发布日期未知时可以省略该field，不得填入虚构日期。不得只用URL作为artifact identity。标题相同但checksum或版本不同的artifact可以共存。

参见[source schema](../../../schema/v0.1/source.schema.json)。
