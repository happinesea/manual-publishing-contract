# Publishing Contract v0.1

> 本文档为翻译版本。如与日文规范存在差异，以日文规范为准。

标准模型是`Source → Build / Transform → Validate → Publish → Static/Page Cache/CDN → Reader`。每次请求时把源文档转换为HTML不是标准模型。

状态包括`draft`、`generated`、`validated`、`published`、`deprecated`和`archived`。发布前应验证schema与内容忠实度。参见[生命周期](../../../docs/zh-CN/lifecycle.md)和[publication schema](../../../schema/v0.1/publication.schema.json)。
