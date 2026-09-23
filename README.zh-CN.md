# Manual Publishing Contract

> 本文档为翻译版本。如与日文规范存在差异，以日文规范为准。

[日本語](README.md) | [English](README.en.md)

## 要解决的问题

仅以PDF发布的技术手册容易被覆盖，难以按操作内容检索，并且转换为网页时常丢失页码级来源追踪。CMS专有格式也会妨碍表格、插图、警告、版本和证据的复用。

Manual Publishing Contract是一项vendor-neutral开放规范，用于在保持语义忠实度和原文可追溯性的前提下，将带版本的技术手册转换为结构化内容。

```text
Source Manual → Versioned Structured Manual → Published Web Content → Machine-readable Evidence
```

它支持旧版保存、可访问性与可检索性、AI/搜索答案的证据追踪、降低平台锁定，以及中小组织复用。本项目不宣称自己是行业标准，也不保证任何实现的质量。

## v0.1

- [日文规范（正本）](spec/v0.1/ja/manual-publishing-contract.md)
- [中文翻译](spec/v0.1/zh-CN/manual-publishing-contract.md)
- [JSON Schema](schema/v0.1/manual.schema.json)
- [虚构示例](examples/v0.1/)
- [架构](docs/zh-CN/architecture.md)、[生命周期](docs/zh-CN/lifecycle.md)、[术语](docs/zh-CN/terminology.md)

v0.1涵盖源文档、手册和版本标识，章节与源页映射，表格和插图引用，发布生命周期，来源追踪，证据，缓存metadata，validation及多版本共存。解析器、OCR、翻译、LLM/RAG、CMS API、广告、认证、计费和厂商产品schema均不在范围内。

## Validation

安装`requirements-dev.txt`后，运行`python tools/validate.py`和`python -m unittest discover -s tests -v`。

## License

[Apache License 2.0](LICENSE)
