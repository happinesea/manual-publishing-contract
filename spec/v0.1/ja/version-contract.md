# Version Contract v0.1

`family_id`は同一manual系列、`manual_id`は言語と版を含む個別manual、`version`はその版を表します。product identityとmanual identityを同一視してはなりません（MUST NOT）。

`supersedes`は直前または置き換え対象の`manual_id`を参照できます（MAY）。この関係は削除指示ではありません。同一familyの複数versionは同時に公開・deprecated・archivedとして保持できます。
