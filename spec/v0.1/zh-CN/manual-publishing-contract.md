# Manual Publishing Contract v0.1

> 本文档为翻译版本。如与日文规范存在差异，以日文规范为准。

## 定位和术语

本Contract定义了在保留源文档追踪关系的前提下，以build-time方式生成、验证和发布版本化技术手册的边界。Contract本身不是解析器、翻译器、builder、publisher、CMS、搜索引擎或AI服务。

MUST/必须表示符合规范所必需，SHOULD/建议表示只有具备明确理由时才可省略，MAY/可选表示由实现者选择。

## 范围

v0.1涵盖源文档与手册标识、版本、源页映射、章节、表格和插图引用、网页映射、发布生命周期、来源追踪、证据、缓存metadata、validation和多版本共存。解析器、OCR、翻译引擎、LLM/RAG实现、CMS API、广告、认证、计费和厂商产品schema不在范围内。

## 五个核心Contract

1. [Source](source-contract.md)：不只依赖URL，而以checksum识别artifact。
2. [Structure](structure-contract.md)：将每个Web章节映射到一个或多个源页。
3. [Version](version-contract.md)：分离产品、手册系列和手册版本。
4. [Publishing](publishing-contract.md)：描述构建、验证、发布和缓存状态。
5. [Evidence](evidence-contract.md)：从claim或结果追溯到源页。

符合规范的手册必须满足[manual schema](../../../schema/v0.1/manual.schema.json)。建议使用稳定且人类可读的ID，但不强制厂商命名方式。

## 忠实度和版本共存

Web内容必须保留含义、标题层级、表格、警告、数值、插图引用和页码来源。无需像素级还原PDF分页，一个Web章节可以映射多个源页。

同一系列的V1、V2、V3可同时存在。`supersedes`不表示删除。发布新版本不得使旧版本失去可检索性。

厂商特定profile可以实现本Contract，但不得把private data、credentials、专有手册或厂商资产加入本repository。
