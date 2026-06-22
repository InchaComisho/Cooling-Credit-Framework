# Cooling Credit Score Estimator

## クーリングクレジットスコア試算モデル

このモジュールは、**Cooling Credit Score（クーリングクレジットスコア）** を予備的に試算するためのPythonシミュレーションモデルである。

企業、自治体、研究者、プロジェクト設計者が、都市冷却、ミスト冷却、土壌再生、森林再生、砂漠再生、海洋循環、排熱削減などの入力値を与えることで、冷却貢献の相対評価、リスク補正後の評価、仮のクーリングクレジット単位を算出できる。

これは正式な認証ツールではない。制度設計、事前評価、MRV設計、政策シミュレーションのための透明な試算モデルである。

---

## 目的

このモデルの目的は、クーリングクレジットの概念を、実際に試算可能な数理モデルへ変換することである。

評価対象は以下である。

- 熱負荷低減
- 気化熱冷却
- WBGT改善
- 水循環回復
- 土壌保水回復
- 植物蒸散回復
- 排熱削減
- 生態系冷却力回復

同時に、以下のリスクをペナルティとして扱う。

- 水ストレス
- 湿度・WBGT悪化リスク
- 生態系リスク
- エネルギー使用量

このモデルは、正式な制度が確立される前に、クーリングクレジットを比較可能・検証可能・拡張可能な形にするためのものである。

---

## 重要な注意点

このモデルの出力は、**予備的・非認証のシミュレーション結果** である。

法的に有効なクレジット、取引可能なクレジット、公式に認証されたクレジットを発行するものではない。

出力値は、以下の用途を想定する。

- 事前評価
- プロジェクト比較
- MRV設計支援
- 政策シミュレーション
- 研究・教育用指標

正式なクレジット発行には、制度標準、第三者検証、生態系安全性、地域別補正、長期モニタリングが必要である。

---

## ファイル構成

```text
simulations/cooling_credit_score_estimator/
  cooling_credit_score_estimator.py
  README.md
  README_ja.md
  README_ar.md
  example_inputs.csv
  example_results.csv
```

---

## 実行方法

リポジトリのルートから実行する。

```bash
python simulations/cooling_credit_score_estimator/cooling_credit_score_estimator.py \
  --input simulations/cooling_credit_score_estimator/example_inputs.csv \
  --output simulations/cooling_credit_score_estimator/results/cooling_credit_score_results.csv \
  --json-output simulations/cooling_credit_score_estimator/results/cooling_credit_score_results.json \
  --print-summary
```

外部Pythonパッケージは不要である。

---

## 入力CSVの主な項目

| 列名 | 意味 |
|---|---|
| `project_id` | プロジェクトID |
| `project_name` | プロジェクト名 |
| `technology_type` | 技術・実装カテゴリ |
| `baseline_air_temp_c` | 実装前の気温 |
| `reduced_air_temp_c` | 実装後の気温 |
| `baseline_surface_temp_c` | 実装前の地表温度 |
| `reduced_surface_temp_c` | 実装後の地表温度 |
| `baseline_wbgt_c` | 実装前のWBGT |
| `reduced_wbgt_c` | 実装後のWBGT |
| `cooled_area_m2` | 冷却対象面積 |
| `duration_hours` | 実装・稼働時間 |
| `water_used_liters` | 使用水量 |
| `evaporated_water_liters` | 蒸発した水量の推定値 |
| `recycled_water_ratio` | 雨水・再生水の利用率。0–1 または 0–100 |
| `electricity_used_kwh` | 消費電力量 |
| `soil_moisture_before_pct` | 実装前の土壌水分率 |
| `soil_moisture_after_pct` | 実装後の土壌水分率 |
| `vegetation_cover_before_pct` | 実装前の植生被覆率 |
| `vegetation_cover_after_pct` | 実装後の植生被覆率 |
| `waste_heat_reduction_kwh` | 排熱削減量の推定値 |
| `water_stress_level` | 地域の水ストレス。0–1 または 0–100 |
| `humidity_risk_level` | 湿度・WBGT悪化リスク。0–1 または 0–100 |
| `ecological_risk_level` | 生態系介入リスク。0–1 または 0–100 |
| `mrv_data_quality` | MRVデータ品質。0–1 または 0–100 |

---

## 出力指標

このモデルは以下を出力する。

- `thermal_reduction_score`
- `evaporative_cooling_score`
- `wbgt_improvement_score`
- `water_cycle_recovery_score`
- `soil_moisture_recovery_score`
- `vegetation_transpiration_score`
- `waste_heat_reduction_score`
- `ecological_cooling_score`
- `water_stress_penalty`
- `humidity_risk_penalty`
- `ecological_risk_penalty`
- `energy_use_penalty`
- `positive_score_before_penalties`
- `total_penalty`
- `cooling_credit_score`
- `gross_cooling_credit_units`
- `risk_adjusted_cooling_credit_units`
- `scenario_grade`
- `mrv_reliability_level`
- `warnings`

---

## 概念式

基本構造は以下である。

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

---

## 仮クレジット単位

このスクリプトは、仮のクレジット単位も算出する。

```text
gross_units = positive_score / 100 × cooled_area_m2 × duration_hours / 1000
risk_adjusted_units = gross_units × risk_adjustment × MRV quality
```

この単位は公式クレジットではない。プロジェクト比較、政策設計、事前検討のための相対的なシミュレーション単位である。

---

## 想定用途

この試算モデルは、以下に利用できる。

- 都市ミスト冷却プロジェクトの比較
- 土壌再生による冷却効果の推定
- 森林・植生回復プロジェクトの評価
- 砂漠再生モデルの冷却評価
- OTUや海洋冷却構想の予備評価
- 自治体クーリングクレジット実証事業の設計
- 企業の冷却貢献プロジェクトのMRV要件整理

---

## 著者

マスター / inchacomusho / InchaComisho

---

## ライセンス

Creative Commons Attribution 4.0 International（CC BY 4.0）
