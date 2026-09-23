# Publishing lifecycle

```text
draft → generated → validated → published → deprecated → archived
```

- `draft`: 編集中で公開対象ではない。
- `generated`: builderが構造化成果物を生成した。
- `validated`: schemaと必要な品質gateを通過した。
- `published`: canonical URL等から読者が利用できる。
- `deprecated`: 新版等により推奨対象ではないが参照可能。
- `archived`: 履歴保存を目的として保持する。

通常は左から右へ進みますが、修正のため`generated`または`draft`へ戻せます。`supersedes`と状態遷移は別概念です。新版公開時も旧版を削除せず、deprecatedまたはarchivedとして共存させられます。
