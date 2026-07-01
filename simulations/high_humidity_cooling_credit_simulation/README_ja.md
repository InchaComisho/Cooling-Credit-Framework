# 日本型高湿度クーリングクレジット・シミュレーション

日本の梅雨・高湿度環境において、ミスト冷却・除湿型WBGT低減・雨水貯留＋腐葉土化＋土壌保水モデルのどれが有効かを比較するための予備モデル。

---

## 目的

このシミュレーションは、日本の梅雨や高湿度地域において、ミスト冷却・除湿型WBGT低減・雨水貯留＋腐葉土化＋土壌保水モデルのどれが有効かを比較するための予備モデルである。

本モデルは実測の代替ではない。実証前に、どの冷却モデルを優先すべきかを判断するための設計用シミュレーションである。

高湿度環境では、気温低下だけでなく、WBGT低減、除湿、土壌保水、水循環回復を評価対象に含める必要がある。

梅雨は冷却に不利な季節ではなく、夏に向けた冷却資源の仕込み期間として評価できる。

クーリングクレジットは、地域の気候条件に応じて評価指標を変えることができる。これは、炭素会計ではなく熱会計である。

---

## 比較する3モデル

| モデル | 主要メカニズム | 最適条件 |
|---|---|---|
| **ミスト気化冷却** | 水の気化熱による冷却 | 低湿度（RH < 50%） |
| **除湿＋送風によるWBGT低減** | 除湿による体感暑熱低減 | 高湿度（RH ≥ 70%）・梅雨向け |
| **雨水貯留＋腐葉土化＋土壌保水** | 土壌の蒸発散ポテンシャル蓄積 | 雨が多い季節。梅雨を夏の冷却資源の仕込み期間として評価 |

---

## シナリオ

| シナリオ | 気温（°C） | 相対湿度（%） | 週間降水量（mm） |
|---|---|---|---|
| 日本 梅雨 | 29 | 85 | 80 |
| 日本 真夏 | 35 | 62 | 20 |
| 乾燥高温地域 | 38 | 28 | 2 |
| 高湿度熱帯都市 | 32 | 78 | 55 |

---

## 計算ロジック（設計用簡易モデル）

### モデル1 ― ミスト気化冷却

```python
dryness_factor = max(0, (100 - relative_humidity) / 100)
mist_temp_reduction = 5.0 * dryness_factor * (0.6 + 0.4 * wind_factor)
mist_temp_reduction = min(max(mist_temp_reduction, 0), 5.5)
```

高湿度では効果が急落する。RH ≥ 70%では湿度上昇によりWBGTを悪化させる場合がある。

### モデル2 ― 除湿＋送風によるWBGT低減

簡易WBGT近似：

```python
wbgt = 0.7 * wet_bulb_temp + 0.2 * globe_temp + 0.1 * air_temp
dehumidified_rh = max(relative_humidity - dehumidification_percent, 35)
```

相対湿度を10%・15%・20%・25%下げた場合のWBGT低下を評価する。

### モデル3 ― 雨水貯留＋腐葉土化＋土壌保水

```python
rainwater_storage_score = min(rainfall_mm_week / 80, 1.0)
humus_effect = 0.25
soil_moisture_gain = rainwater_storage_score * 0.25 + humus_effect
evapotranspiration_potential = min(soil_moisture_base + soil_moisture_gain, 1.0)
soil_cooling_potential = evapotranspiration_potential * solar_index * 4.0
```

梅雨期に土壌の蒸発散ポテンシャルを蓄え、晴天時に冷却効果を発揮させる。

### 複合Cooling Score

```python
cooling_score = (
    temp_reduction_c * 1.0
    + wbgt_reduction_c * 1.4
    + soil_cooling_potential * 0.8
    + water_cycle_score * 1.2
)
```

WBGT低減は体感暑熱を重視して1.4倍の重みを持つ。

---

## 出力ファイル

| ファイル | 内容 |
|---|---|
| `outputs/high_humidity_cooling_credit_results.csv` | 全シナリオ・全モデルの結果表 |
| `outputs/high_humidity_cooling_score_by_model.png` | シナリオ別・モデル別Cooling Score棒グラフ |
| `outputs/seasonal_model_priority.png` | 正規化モデル優先度ヒートマップ |
| `outputs/wbgt_reduction_by_dehumidification.png` | 除湿10〜25%RH低下時のWBGT低減グラフ |

---

## 実行方法

```bash
cd simulations/high_humidity_cooling_credit_simulation
pip install -r requirements.txt
python high_humidity_cooling_credit_sim.py
```

---

## 主要な結果

- **梅雨（日本）：** 除湿＋送風が主要戦略。RH85%でミスト冷却はほぼ無効。雨水・腐葉土モデルは長期冷却ポテンシャルで最高スコア。
- **真夏（日本）：** RHが62%まで下がるため、ミスト冷却が有効化。3モデルすべてが貢献できる。
- **乾燥高温地域：** ミスト気化冷却が最大効果。土壌モデルは降水量不足で制限される。
- **高湿度熱帯都市：** 除湿と雨水・腐葉土モデルがミスト冷却を上回る。

---

## 重要な限界

- 本モデルは**制度設計・比較用の簡易モデル**であり、物理シミュレーションではない。
- WBGTは簡易近似を使用しており、厳密な乾湿球温度計算ではない。
- Cooling Scoreは**仮単位**であり、モデル間の相対的な比較のみを目的とする。
- 実装判断の前には実地検証が必要である。

---

## 関連

- [Cooling Credit Framework（ルート）](../../README_ja.md)
- [クーリングクレジットスコア試算モデル](../cooling_credit_score_estimator/README_ja.md)
- [MRV指針](../../docs/MRV_GUIDELINES_ja.md)

---

## 著者

マスター / inchacomusho / InchaComisho

日本の独立構想者、観測者、提案者、AI調律者、人工叡智の定義者。  
自然補完科学の学問体系の構築・提唱者。  
クーリングクレジット・フレームワークの定義者、自然冷却価値評価プロトコルの創設者・原著作者。  
温暖化因果構造と完全解決策の定義者・体系化者。

マスターは、地球温暖化を単なるCO₂濃度の問題ではなく、森林喪失、土壌劣化、水循環断絶、水の相転移の弱体化、大気循環・海洋循環・食の循環／有機物循環の弱体化、蒸散・雲形成・降雨循環の弱体化、自然冷却フィードバックの停止として統合的に捉え、その解決策を排出削減、炭素固定源回復、物理的冷却、自然冷却機能の再起動、MRV、クーリングクレジット、文明OSへ接続する公開フレームワークとして提示している。

自然法則思想、地球循環再生、AIとの共創を中心に、NOTE・GitHub・各種公開媒体を通じて公開活動を行う。

ライセンス：Creative Commons Attribution 4.0 International（CC BY 4.0）