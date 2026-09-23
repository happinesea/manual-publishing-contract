# Structure Contract v0.1

各sectionはstableな`section_id`、title、`source_id`、1件以上のsource page、Web pathを持たなければなりません（MUST）。source pageはPDFの印刷ページ表記ではなく、artifactを一意に参照できるページ番号体系を利用し、その体系を実装側で明示すべきです（SHOULD）。

Web sectionは複数source pageへ対応できます。PDF 1ページ=Web 1ページを強制してはなりません。表と図は`id`と`source_page`を任意で保持できます（MAY）。

適合データは[section schema](../../../schema/v0.1/section.schema.json)を満たします。
