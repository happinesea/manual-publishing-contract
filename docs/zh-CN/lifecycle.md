# 发布生命周期

> 本文档为翻译版本。如与日文规范存在差异，以日文规范为准。

`draft → generated → validated → published → deprecated → archived`

- `draft`：编辑中，不对外公开。
- `generated`：已生成结构化成果物。
- `validated`：已通过schema和质量gate。
- `published`：读者可以访问。
- `deprecated`：仍可访问，但不再推荐。
- `archived`：为历史保存而保留。

修正时可返回`generated`或`draft`。`supersedes`与生命周期状态是不同概念。旧版可作为deprecated或archived与新版共存，而不是被删除。
