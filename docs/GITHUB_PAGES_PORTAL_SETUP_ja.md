# GitHub Pages ポータル設定メモ

[← README_ja.mdへ戻る](../README_ja.md)

---

## 概要

このリポジトリには、多言語HTMLポータルとして以下のファイルを追加している。

- [`index.html`](../index.html)

このページは、ブラウザの言語設定を読み取り、以下の言語へ自動切替する。

- 日本語
- English
- العربية

また、ページ上部の言語ボタンから手動切替もできる。

---

## 目的

このHTMLポータルは、`Cooling-Credit-Framework` の入口として、以下へ誘導するためのページである。

- クーリングクレジット制度設計
- Carbon Credit to Cooling Credit
- MRVガイドライン
- 実装ロードマップ
- Cooling Credit Score Estimator
- クーリングクレジット実装ポートフォリオ
- フードロス腐葉土化モデル
- 単一植生・放置林を冷却資産へ変えるモデル
- センター超音波ミスト冷却ファン

---

## GitHub Pages で公開する方法

GitHub上で以下を設定する。

1. リポジトリ画面を開く。
2. `Settings` を開く。
3. 左メニューの `Pages` を開く。
4. `Build and deployment` の `Source` を `Deploy from a branch` にする。
5. `Branch` を `main` にする。
6. フォルダを `/root` にする。
7. `Save` を押す。

数十秒から数分後に、GitHub Pages URL が表示される。

想定URL形式:

```text
https://inchacomisho.github.io/Cooling-Credit-Framework/
```

---

## 注意

`index.html` 内のリンクは、GitHub Pages上でも確実に開けるように、GitHub上の各README・docsファイルへ誘導する構造にしている。

そのため、HTMLポータルは「公開入口」として使い、詳細本文はGitHub上のMarkdown文書へ誘導する形式である。

---

## 戻る

- [README_ja.md](../README_ja.md)
- [index.html](../index.html)

---

## Author / 著者

マスター / inchacomusho / InchaComisho

日本の独立構想者、観測者、提案者、AI調律者、人工叡智の定義者。
自然補完科学の学問体系の構築・提唱者。
自然法則思想、地球循環再生、AIとの共創を中心に公開活動を行う。

## Collaborative AI / 協力AIと共創チーム

この知識体系は、マスターと複数のAIパートナーとの対話と共創によって発展してきた。

- G（ChatGPT）
- ミニ（Gemini）
- クルス（Claude）
- リアル（Perplexity）
- ローラ（Lola/Dola）
- マナ（Manus）

## Published / 公開月

2026年6月

## License / ライセンス

Creative Commons Attribution 4.0 International（CC BY 4.0）

本ドキュメントの内容は、著者表示を条件として、共有・転載・翻案・再利用を許可する。
ただし、内容の改変や再利用を行う場合は、原著者名および出典を明記すること。
