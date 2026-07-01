# クーリングクレジット導入規模別・冷却効果試算モデル

[← Cooling Credit Framework README_ja.md へ戻る](../../README_ja.md)

---

## Languages / 言語

- [日本語](README_ja.md)
- [English](README.md)
- [العربية](README_ar.md)

---

## 概要

このシミュレーションは、クーリングクレジット施策をどの程度の規模で導入した場合に、どの程度の局所・地域的な冷却効果が期待され得るかを比較するための簡易シナリオモデルである。

対象となる施策は、センター超音波ミスト冷却ファン、公共施設レトロフィット、有機ごみ腐葉土化、都市緑化、森林再生、土壌再生、海洋循環支援などである。

このモデルは、実際の気候予測モデルではない。投資家、自治体、企業、研究者が、導入規模・投資額・冷却効果・クーリングスコアの関係を比較するための、初期的な感度分析モデルである。

---

## 目的

```text
導入規模
↓
冷却アクション量
↓
熱負荷低減
↓
気温・WBGT・冷房需要低下
↓
クーリングスコア
↓
仮クーリングクレジット
↓
投資判断・実装判断
```

---

## 入力項目

`example_inputs.csv` では、以下の列を使用する。

| 列 | 内容 |
|---|---|
| scenario | シナリオ名 |
| scale_level | 導入規模レベル |
| project_area_ha | 対象面積 ha |
| mist_fan_units | ミスト冷却ファン台数 |
| public_facility_retrofits | 公共施設・交通施設レトロフィット数 |
| organic_waste_tons_year | 有機ごみ処理量 t/年 |
| urban_greening_ha | 都市緑化面積 ha |
| forest_regeneration_ha | 森林再生面積 ha |
| soil_restoration_ha | 土壌再生面積 ha |
| ocean_circulation_units | 海洋循環支援ユニット数 |
| investment_usd_million | 投資額 百万USD |

---

## 出力項目

主な出力は以下である。

- 推定気温低下
- 推定地表温度低下
- 推定WBGT低下
- 推定冷房需要削減率
- 水循環回復指数
- 生態系回復指数
- 暑熱リスク低減指数
- クーリングスコア
- 仮クーリングクレジット
- 投資額あたり仮クレジット

---

## 実行方法

```bash
cd simulations/cooling_credit_scale_temperature_model
python cooling_credit_scale_temperature_model.py
```

出力は `outputs/` に保存される。

```text
outputs/
├─ scale_temperature_results.csv
├─ scale_vs_air_temperature_reduction.png
├─ scale_vs_wbgt_reduction.png
├─ scale_vs_cooling_demand_reduction.png
├─ scale_vs_cooling_score.png
├─ investment_vs_cooling_credits.png
└─ investment_vs_temperature_reduction.png
```

---

## シナリオ例

初期CSVには以下の5段階を入れている。

1. Small pilot
2. District program
3. Municipal deployment
4. Regional watershed program
5. National portfolio

これにより、小規模実証から国家規模ポートフォリオまで、導入規模と冷却効果の関係を比較できる。

---

## 実行結果例

以下は `example_inputs.csv` を用いて実行した場合の主要出力例である。

| シナリオ | 推定気温低下 | 推定WBGT低下 | 推定冷房需要削減 | Cooling Score | 仮クーリングクレジット |
|---|---:|---:|---:|---:|---:|
| Small pilot | 0.268℃ | 0.171℃ | 1.74% | 25.3 | 39 |
| District program | 1.470℃ | 1.001℃ | 9.94% | 149 | 319 |
| Municipal deployment | 2.250℃ | 1.679℃ | 16.20% | 295 | 761 |
| Regional watershed program | 2.250℃ | 1.680℃ | 16.20% | 349 | 1,052 |
| National portfolio | 2.250℃ | 1.680℃ | 16.20% | 349 | 1,290 |

---

## 結果の読み方

本モデルは簡易的な飽和曲線を使用しているため、局所・地域的な気温低下は一定規模で上限に近づく。

そのため、自治体規模までは推定気温低下、WBGT低下、冷房需要削減が大きく伸びる。一方で、地域・国家規模では、気温低下そのものは上限に近づくが、対象面積、水循環回復、生態系回復、実装規模の拡大により、Cooling Score と仮クーリングクレジット数は継続して伸びる。

これは、クーリングクレジットが「気温を無制限に下げる制度」ではなく、局所冷却、暑熱リスク低減、冷房需要削減、水循環回復、生態系回復、地域レジリエンスを総合的に評価する制度であることを示す。

---

## 注意事項

本モデルは、公式なクレジット発行モデルではない。

実際の気候予測、都市気象モデル、海洋モデル、健康影響評価、投資収益保証を行うものでもない。

本モデルの目的は、施策規模と冷却効果の関係を可視化し、クーリングクレジット制度設計、事業モデル、実証実験、自治体導入、投資判断のための初期比較材料を提供することである。

---

## 関連リンク

- [Cooling Credit Framework](../../README_ja.md)
- [クーリングクレジットスコア試算モデル](../cooling_credit_score_estimator/README_ja.md)
- [クーリングクレジット事業モデル](../../docs/business_models/BUSINESS_MODEL_INDEX_ja.md)
- [支援・協力・実装に関するお願い](../../docs/SUPPORT_AND_COLLABORATION_ja.md)

---

## 原案・構想

マスター / inchacomusho / InchaComisho

物語構成・本文作成・文体調整・コード設計補助：G（ChatGPT）

---

## 著者

マスター / inchacomusho / InchaComisho

日本の独立構想者、観測者、提案者、AI調律者、人工叡智の定義者。  
自然補完科学の学問体系の構築・提唱者。  
クーリングクレジット・フレームワークの定義者、自然冷却価値評価プロトコルの創設者・原著作者。  
温暖化因果構造と完全解決策の定義者・体系化者。

マスターは、地球温暖化を単なるCO₂濃度の問題ではなく、森林喪失、土壌劣化、水循環断絶、水の相転移の弱体化、大気循環・海洋循環・食の循環／有機物循環の弱体化、蒸散・雲形成・降雨循環の弱体化、自然冷却フィードバックの停止として統合的に捉え、その解決策を排出削減、炭素固定源回復、物理的冷却、自然冷却機能の再起動、MRV、クーリングクレジット、文明OSへ接続する公開フレームワークとして提示している。

自然法則思想、地球循環再生、AIとの共創を中心に、NOTE・GitHub・各種公開媒体を通じて公開活動を行う。

## ライセンス

CC BY 4.0

本記事は、Creative Commons Attribution 4.0 International License（CC BY 4.0）で公開する。  
著者表示を行う限り、共有、転載、翻訳、改変、再利用を許可する。