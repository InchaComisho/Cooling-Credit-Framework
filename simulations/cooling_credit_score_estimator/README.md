# Cooling Credit Score Estimator

## Preliminary Python Simulation Model for Cooling Credit Scoring

This module provides a preliminary, non-certification Python estimator for the **Cooling Credit Score**.

It allows companies, municipalities, researchers, and project designers to input project-level values and obtain a simulated score for cooling contribution, risk-adjusted performance, and provisional cooling-credit units.

This is not an official certification tool. It is a transparent pre-feasibility and MRV design model.

---

## Purpose

The Cooling Credit Score Estimator translates the conceptual Cooling Credit model into a practical numerical simulation.

It evaluates:

- thermal reduction
- evaporative cooling
- WBGT improvement
- water-cycle recovery
- soil moisture recovery
- vegetation transpiration recovery
- waste-heat reduction
- ecological cooling recovery

It also applies penalties for:

- water stress
- humidity risk
- ecological risk
- energy use

The goal is to make the Cooling Credit concept testable, comparable, and extensible before any formal crediting system is established.

---

## Important Disclaimer

This model produces **preliminary, non-certified simulation results**.

It does not create legally valid, tradable, or officially recognized credits.

The output values should be interpreted as:

- pre-feasibility estimates
- project comparison indicators
- MRV design support
- policy simulation outputs
- research and educational indicators

Formal credit issuance would require an institutional standard, third-party verification, ecological safeguards, regional calibration, and long-term monitoring.

---

## File Structure

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

## How to Run

From the repository root:

```bash
python simulations/cooling_credit_score_estimator/cooling_credit_score_estimator.py \
  --input simulations/cooling_credit_score_estimator/example_inputs.csv \
  --output simulations/cooling_credit_score_estimator/results/cooling_credit_score_results.csv \
  --json-output simulations/cooling_credit_score_estimator/results/cooling_credit_score_results.json \
  --print-summary
```

No external Python packages are required.

---

## Input Columns

The input CSV must include the following columns:

| Column | Meaning |
|---|---|
| `project_id` | Project identifier |
| `project_name` | Project name |
| `technology_type` | Technology or implementation category |
| `baseline_air_temp_c` | Air temperature before implementation |
| `reduced_air_temp_c` | Air temperature after implementation |
| `baseline_surface_temp_c` | Surface temperature before implementation |
| `reduced_surface_temp_c` | Surface temperature after implementation |
| `baseline_wbgt_c` | WBGT before implementation |
| `reduced_wbgt_c` | WBGT after implementation |
| `cooled_area_m2` | Area affected by cooling |
| `duration_hours` | Duration of the intervention |
| `water_used_liters` | Total water used |
| `evaporated_water_liters` | Estimated evaporated water |
| `recycled_water_ratio` | Ratio of recycled/rainwater used, 0–1 or 0–100 |
| `electricity_used_kwh` | Electricity consumed |
| `soil_moisture_before_pct` | Soil moisture before intervention |
| `soil_moisture_after_pct` | Soil moisture after intervention |
| `vegetation_cover_before_pct` | Vegetation cover before intervention |
| `vegetation_cover_after_pct` | Vegetation cover after intervention |
| `waste_heat_reduction_kwh` | Estimated waste-heat reduction |
| `water_stress_level` | Regional water-stress level, 0–1 or 0–100 |
| `humidity_risk_level` | Humidity/WBGT risk level, 0–1 or 0–100 |
| `ecological_risk_level` | Ecological intervention risk, 0–1 or 0–100 |
| `mrv_data_quality` | MRV data quality, 0–1 or 0–100 |

---

## Output Metrics

The estimator outputs:

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

## Conceptual Formula

The model follows this conceptual structure:

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

## Provisional Credit Units

The script also calculates provisional units:

```text
gross_units = positive_score / 100 × cooled_area_m2 × duration_hours / 1000
risk_adjusted_units = gross_units × risk_adjustment × MRV quality
```

These units are not official credits. They are relative simulation units for comparison and policy design.

---

## Example Use Cases

This estimator can be used for:

- comparing urban mist cooling projects
- estimating soil regeneration cooling benefits
- evaluating forest or vegetation recovery projects
- assessing desert regeneration cooling models
- pre-screening OTU or ocean cooling concepts
- designing municipal cooling-credit pilot programs
- preparing MRV requirements for corporate cooling projects

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

## License

Creative Commons Attribution 4.0 International (CC BY 4.0)