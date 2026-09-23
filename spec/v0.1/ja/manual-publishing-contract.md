# Manual Publishing Contract v0.1

## 1. 位置付け

本書は日本語のNormativeな正本です。Manual Publishing Contractは、versioned technical manualを、原典への追跡可能性を保った構造化コンテンツとしてbuild-timeに生成・検証・公開するための境界仕様です。Contract自身はparser、translator、builder、publisher、CMS、検索engine、AI serviceではありません。

本書の「必須（MUST）」は適合に必要、「推奨（SHOULD）」は合理的理由がある場合のみ省略可能、「任意（MAY）」は実装者が選択可能を意味します。

## 2. Scope

v0.1はsource document identity、manual identity、versioning、source page mapping、section structure、table/figure reference、Web content mapping、publishing lifecycle、provenance、evidence chain、cache metadata、validation、複数版共存を対象とします。

PDF parser、OCR、翻訳engine、LLM provider、RAG/vector database、CMS-specific API、WordPress plugin、広告、認証、課金、vendor-specific product schemaは対象外です。

## 3. Core Contract

1. [Source Contract](source-contract.md): URLだけに依存せず、checksumを含む原典identityを保持する。
2. [Structure Contract](structure-contract.md): Web sectionと1ページ以上のsource pageを対応付ける。
3. [Version Contract](version-contract.md): product、manual family、manual versionを分離し、旧版共存を許す。
4. [Publishing Contract](publishing-contract.md): build、validate、publish、cacheの状態を表す。
5. [Evidence Contract](evidence-contract.md): claimまたは検索結果からsource pageへ逆引きできるようにする。

適合manualは[manual schema](../../../schema/v0.1/manual.schema.json)を満たさなければなりません（MUST）。human-readableでstableなIDを推奨します（SHOULD）が、vendor namingは強制しません。

## 4. Fidelity

Web版は原典の意味、heading hierarchy、表構造、warning、安全上の注意、数値、figure reference、page provenanceを保持しなければなりません（MUST）。これはsemantic fidelityです。

PDFのvisual paginationをpixel-perfectに再現する必要はありません。visual fidelityはWeb accessibilityとusabilityを損なわない範囲で任意です（MAY）。PDF 1ページとWeb 1ページの一致を要求しません。1つのWeb sectionが複数source pageへ対応しても構いません。

## 5. Version coexistence

同一manual familyのV1、V2、V3は同時に保持できます。`supersedes`は置換関係を表しますが、旧版の削除を意味しません。最新版の公開が旧版のarchiveや参照可能性を失わせてはなりません（MUST NOT）。

## 6. Vendor neutrality

Contract実装はvendor-specific profileを定義できます（MAY）が、そのproduct data、private URL、credentials、非公開資料、著作権で保護されたmanual本文や画像を本仕様repositoryへ含めてはなりません（MUST NOT）。
