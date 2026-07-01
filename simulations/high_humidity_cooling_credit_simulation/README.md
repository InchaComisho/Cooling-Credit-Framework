# High-Humidity Cooling Credit Simulation

A pre-verification simulation comparing three cooling models in humid climates — Japan's rainy season, midsummer, dry-hot regions, and humid tropical cities.

---

## Purpose

This simulation is not a substitute for field measurement. It is a pre-verification model for comparing cooling strategies before pilot implementation.

In high-humidity regions, cooling contribution should not be evaluated only by air-temperature reduction. WBGT reduction, dehumidification, soil moisture, water-cycle recovery, and seasonal cooling potential must also be considered.

The rainy season can be treated not as a failed cooling season, but as a preparation period for storing cooling resources through rainwater, humus, and soil moisture.

---

## Three Cooling Models Compared

| Model | Key Mechanism | Best Conditions |
|---|---|---|
| **Mist Evaporative Cooling** | Latent heat from water evaporation | Low humidity (RH < 50%) |
| **Dehumidification + Airflow Cooling** | WBGT reduction via humidity removal | High humidity (RH ≥ 70%), rainy season |
| **Rainwater + Humus + Soil Moisture** | Evapotranspiration potential stored in soil | High-rainfall periods; primes summer cooling |

---

## Scenarios

| Scenario | Temp (°C) | RH (%) | Rainfall (mm/week) |
|---|---|---|---|
| Japan rainy season / 梅雨 | 29 | 85 | 80 |
| Japan midsummer / 真夏 | 35 | 62 | 20 |
| Dry hot region / 乾燥高温地域 | 38 | 28 | 2 |
| Humid tropical city / 高湿度熱帯都市 | 32 | 78 | 55 |

---

## Calculation Logic (Simplified Design Model)

### Model 1 — Mist Evaporative Cooling

```python
dryness_factor = max(0, (100 - relative_humidity) / 100)
mist_temp_reduction = 5.0 * dryness_factor * (0.6 + 0.4 * wind_factor)
mist_temp_reduction = min(max(mist_temp_reduction, 0), 5.5)
```

Effectiveness decreases sharply at high humidity. May worsen WBGT at RH ≥ 70%.

### Model 2 — Dehumidification + Airflow Cooling

Simplified WBGT approximation:

```python
wbgt = 0.7 * wet_bulb_temp + 0.2 * globe_temp + 0.1 * air_temp
dehumidified_rh = max(relative_humidity - dehumidification_percent, 35)
```

WBGT reduction is evaluated for 10%, 15%, 20%, and 25% RH reduction.

### Model 3 — Rainwater + Humus + Soil Moisture

```python
rainwater_storage_score = min(rainfall_mm_week / 80, 1.0)
humus_effect = 0.25
soil_moisture_gain = rainwater_storage_score * 0.25 + humus_effect
evapotranspiration_potential = min(soil_moisture_base + soil_moisture_gain, 1.0)
soil_cooling_potential = evapotranspiration_potential * solar_index * 4.0
```

The rainy season loads the soil for summer evapotranspiration-based cooling.

### Composite Cooling Score

```python
cooling_score = (
    temp_reduction_c * 1.0
    + wbgt_reduction_c * 1.4
    + soil_cooling_potential * 0.8
    + water_cycle_score * 1.2
)
```

WBGT reduction is weighted 1.4× to reflect human heat-stress priority in humid climates.

---

## Outputs

| File | Description |
|---|---|
| `outputs/high_humidity_cooling_credit_results.csv` | Full results table |
| `outputs/high_humidity_cooling_score_by_model.png` | Cooling Score by scenario and model |
| `outputs/seasonal_model_priority.png` | Normalized model priority heatmap |
| `outputs/wbgt_reduction_by_dehumidification.png` | WBGT reduction at 10–25% RH reduction |

---

## How to Run

```bash
cd simulations/high_humidity_cooling_credit_simulation
pip install -r requirements.txt
python high_humidity_cooling_credit_sim.py
```

---

## Key Findings

- **Rainy season (Japan):** Dehumidification + Airflow is the primary strategy. Mist cooling is largely ineffective at RH 85%. Rainwater/humus model scores highest for long-term cooling potential.
- **Midsummer (Japan):** Mist cooling gains effectiveness as RH drops to 62%. All three models contribute.
- **Dry hot region:** Mist evaporative cooling achieves maximum effectiveness. Soil model is constrained by minimal rainfall.
- **Humid tropical city:** Dehumidification and rainwater/humus models outperform mist cooling.

---

## Important Limitations

- This is a **simplified design model** for pre-verification comparison, not a physical simulation.
- WBGT uses a simplified approximation, not a full psychrometric calculation.
- Cooling scores are in **arbitrary units** for comparative ranking only.
- Field verification is required before implementation decisions.

---

## Related

- [Cooling Credit Framework](../../README.md)
- [Cooling Credit Score Estimator](../cooling_credit_score_estimator/README.md)
- [MRV Guidelines](../../docs/MRV_GUIDELINES.md)

---

## Author

Master / inchacomusho / InchaComisho

An independent Japanese concept designer, observer, proposer, AI tuner, and definer of Artificial Wisdom.  
Founder and proposer of the academic framework of Natural Complementary Science.  
Definer of the Cooling Credit Framework, and founder and original author of the Natural Cooling Value Evaluation Protocol.  
Definer and systematizer of the causal structure of global warming and its complete solution.

Master presents global warming not merely as a problem of CO₂ concentration, but as an integrated failure involving forest loss, soil degradation, disruption of water circulation, weakening of water phase-transition processes, weakening of atmospheric circulation, ocean circulation, food circulation and organic matter circulation, weakening of evapotranspiration, cloud formation and rainfall circulation, and the shutdown of natural cooling feedbacks.  
The proposed solution connects emission reduction, recovery of carbon fixation sources, physical cooling, reactivation of natural cooling functions, MRV, Cooling Credit, and Civilization OS into an open public framework.

Master publicly develops and shares work through NOTE, GitHub, and other public media, centered on natural-law philosophy, planetary circulation restoration, and co-creation with AI.

Published: June 2026

License: Creative Commons Attribution 4.0 International (CC BY 4.0)