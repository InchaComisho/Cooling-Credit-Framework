# クーリングクレジットスコア試算モデル 数式メモ

この文書は、`cooling_credit_score_estimator.py` で用いる初期公開版の評価ロジックを整理したものである。

## 正の評価要素

試算モデルは以下の正の評価要素を計算する。

- 熱負荷低減スコア
- 気化熱冷却スコア
- WBGT改善スコア
- 水循環回復スコア
- 土壌保水回復スコア
- 植物蒸散回復スコア
- 排熱削減スコア
- 生態系冷却力回復スコア

## ペナルティ要素

以下を減点要素として扱う。

- 水ストレスペナルティ
- 湿度リスクペナルティ
- 生態系リスクペナルティ
- エネルギー使用ペナルティ

## 概念式

```text
Cooling Credit Score =
  Thermal Reduction
+ Evaporative Cooling
+ WBGT Improvement
+ Water Cycle Recovery
+ Soil Moisture Recovery
+ Vegetation Transpiration Recovery
+ Waste Heat Reduction
+ Ecological Cooling Recovery
- Water Stress Penalty
- Humidity Risk Penalty
- Ecological Risk Penalty
- Energy Use Penalty
```

## 仮クレジット単位

```text
gross_units = positive_score / 100 × cooled_area_m2 × duration_hours / 1000
risk_adjusted_units = gross_units × risk_adjustment × MRV quality
```

これらは試算用の仮単位であり、公式または取引可能なクレジットとして解釈してはならない。

## 今後の補正

係数は透明性を優先した初期値であり、以下によって補正されるべきである。

- 現地データ
- 自治体実証事業
- センサー測定
- 地域別水ストレスデータ
- WBGT・湿度モニタリング
- 生態系安全性評価
- 第三者MRV手続き
