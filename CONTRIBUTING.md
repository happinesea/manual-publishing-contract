# Contributing

typo修正、翻訳改善、schema提案、仕様提案を歓迎します。本repositoryは公開情報だけを扱います。秘密情報、private URL、実在マニュアルの無断転載、vendor内部情報を含めないでください。

変更提案には次を簡潔に記載してください。

1. **Problem** — 解決する問題
2. **Use case** — 利用場面
3. **Proposed change** — 変更内容
4. **Backward compatibility** — v0.1利用者への影響

Normativeな変更は日本語仕様を先に更新し、英語・简体中文訳を追随させてください。schema変更には架空データのexampleとvalidationを追加してください。

提出前に次を実行します。

```bash
python tools/validate.py
python -m unittest discover -s tests -v
```
