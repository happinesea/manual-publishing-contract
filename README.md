# Manual Publishing Contract

[English](README.en.md) | [简体中文](README.zh-CN.md)

## 解決する問題

技術マニュアルがPDFだけで公開されると、旧版が上書きされ、個別の操作を検索しにくくなり、WebページやAI回答から原典ページへ戻れないことがあります。CMSごとの形式差や、表・図・注意事項・ページ番号の来歴消失も再利用を難しくします。

Manual Publishing Contractは、バージョン付き技術マニュアルを、意味と原典への追跡可能性を維持したままWeb公開・検索・機械利用できる構造へ変換するためのvendor-neutralなオープン仕様です。

```text
Source Manual
    ↓
Versioned Structured Manual
    ↓
Published Web Content
    ↓
Machine-readable Evidence
```

## 価値

- 旧版を保存し、異なる版の混同を避ける
- 技術情報の検索性とWeb accessibilityを改善する
- Web section、manual version、source document、source pageを結ぶ
- AIや検索結果の根拠を原典まで追跡可能にする
- CMS、vendor、AI providerへのロックインを減らす
- 中小規模の組織でも再利用できる最小限の共通形式を提供する

本仕様は「業界標準」や特定実装の品質保証を主張しません。

## v0.1

- [日本語仕様（正本）](spec/v0.1/ja/manual-publishing-contract.md)
- [JSON Schema](schema/v0.1/manual.schema.json)
- [架空データによるexamples](examples/v0.1/)
- [Architecture](docs/ja/architecture.md)
- [Lifecycle](docs/ja/lifecycle.md)
- [Terminology](docs/ja/terminology.md)

日本語仕様だけがNormativeです。英語と简体中文は公式翻訳ですが、差異がある場合は日本語仕様を優先します。

## Scope

v0.1はsource identity、manual/version identity、sectionとsource pageの対応、表・図の参照、公開状態、provenance、evidence chain、cache metadata、validation、複数版の共存を対象にします。PDF parser、OCR、翻訳engine、LLM、RAG/vector database、CMS API、WordPress plugin、広告、認証、課金、vendor固有product schemaは対象外です。

## Validation

```bash
python -m venv .venv
.venv/Scripts/python -m pip install -r requirements-dev.txt  # Windows
python tools/validate.py
python -m unittest discover -s tests -v
```

macOS/Linuxでは仮想環境の実行パスを `.venv/bin/` に読み替えてください。

## Repository description（推奨）

`An open specification for converting versioned technical manuals into traceable, web-publishable, AI-ready structured content.`

## License

[Apache License 2.0](LICENSE)
