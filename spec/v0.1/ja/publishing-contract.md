# Publishing Contract v0.1

標準モデルは次のbuild-time flowです。

```text
Source → Build / Transform → Validate → Publish → Static/Page Cache/CDN → Reader
```

runtimeで毎回sourceをHTMLへ変換する方式は標準モデルではありません。statusは`draft`、`generated`、`validated`、`published`、`deprecated`、`archived`のいずれかです。公開物は生成時刻、generator、canonical URL、cache modeを必要に応じて保持できます。

`published`へ遷移する前にschemaとcontent fidelityを検証すべきです（SHOULD）。状態遷移は[Lifecycle](../../../docs/ja/lifecycle.md)に定義します。適合データは[publication schema](../../../schema/v0.1/publication.schema.json)を満たします。
