# Cooling Credit Scale and Temperature Impact Model

[← Back to Cooling Credit Framework README](../../README.md)

---

## Languages

- [日本語](README_ja.md)
- [English](README.md)
- [العربية](README_ar.md)

---

## Overview

This simulation is a simplified scenario model for comparing how different implementation scales of Cooling Credit actions may affect local and regional cooling indicators.

The model covers center-mist ultrasonic cooling fans, public-facility retrofits, organic-waste-to-humus conversion, urban greening, forest regeneration, soil restoration, and ocean circulation support.

This is not a climate prediction model. It is an early-stage sensitivity-analysis model intended to help investors, municipalities, companies, and researchers compare implementation scale, investment, cooling impact, and Cooling Score.

---

## Purpose

```text
Implementation scale
↓
Cooling action volume
↓
Heat-load reduction
↓
Air temperature, WBGT, and cooling-demand reduction
↓
Cooling Score
↓
Provisional Cooling Credits
↓
Investment and implementation decisions
```

---

## Input Columns

`example_inputs.csv` uses the following columns.

| Column | Meaning |
|---|---|
| scenario | Scenario name |
| scale_level | Implementation scale level |
| project_area_ha | Project area in hectares |
| mist_fan_units | Number of mist cooling fan units |
| public_facility_retrofits | Number of public-facility or transport retrofits |
| organic_waste_tons_year | Organic waste processed per year |
| urban_greening_ha | Urban greening area in hectares |
| forest_regeneration_ha | Forest regeneration area in hectares |
| soil_restoration_ha | Soil restoration area in hectares |
| ocean_circulation_units | Ocean circulation support units |
| investment_usd_million | Investment in million USD |

---

## Outputs

Main outputs include:

- estimated air temperature reduction,
- estimated surface temperature reduction,
- estimated WBGT reduction,
- estimated cooling-demand reduction,
- water-cycle recovery index,
- ecosystem recovery index,
- heat-risk reduction index,
- Cooling Score,
- provisional Cooling Credits,
- provisional credits per million USD.

---

## How to Run

```bash
cd simulations/cooling_credit_scale_temperature_model
python cooling_credit_scale_temperature_model.py
```

Outputs are saved to `outputs/`.

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

## Example Scenarios

The initial CSV includes five scale levels:

1. Small pilot
2. District program
3. Municipal deployment
4. Regional watershed program
5. National portfolio

This makes it possible to compare pilot-scale, municipal-scale, regional-scale, and national-scale implementation portfolios.

---

## Example Results

The following table shows key outputs generated from `example_inputs.csv`.

| Scenario | Estimated Air Temp Reduction | Estimated WBGT Reduction | Estimated Cooling Demand Reduction | Cooling Score | Provisional Cooling Credits |
|---|---:|---:|---:|---:|---:|
| Small pilot | 0.268°C | 0.171°C | 1.74% | 25.3 | 39 |
| District program | 1.470°C | 1.001°C | 9.94% | 149 | 319 |
| Municipal deployment | 2.250°C | 1.679°C | 16.20% | 295 | 761 |
| Regional watershed program | 2.250°C | 1.680°C | 16.20% | 349 | 1,052 |
| National portfolio | 2.250°C | 1.680°C | 16.20% | 349 | 1,290 |

---

## How to Interpret These Results

This simplified model intentionally uses saturation curves. Therefore, local or regional air-temperature reduction approaches an upper bound as implementation scale increases.

Up to the municipal scale, estimated air-temperature reduction, WBGT reduction, and cooling-demand reduction increase substantially. At regional and national scales, temperature reduction itself approaches the model upper bound, while Cooling Score and provisional Cooling Credits may continue to grow through expanded project area, water-cycle recovery, ecosystem recovery, and implementation scale.

This means that Cooling Credits should not be understood as a mechanism for unlimited temperature reduction. Rather, they are a framework for evaluating local cooling, heat-risk reduction, reduced cooling demand, water-cycle recovery, ecosystem recovery, and regional resilience as a combined value system.

---

## Important Caution

This model is not an official credit issuance model.

It does not provide climate prediction, urban meteorological modeling, ocean modeling, health-impact guarantee, or investment-return guarantee.

Its purpose is to visualize the relationship between implementation scale and cooling-effect indicators, providing an early comparison tool for Cooling Credit institutional design, business models, pilot projects, municipal programs, and investment discussions.

---

## Related Links

- [Cooling Credit Framework](../../README.md)
- [Cooling Credit Score Estimator](../cooling_credit_score_estimator/README.md)
- [Cooling Credit Business Models](../../docs/business_models/BUSINESS_MODEL_INDEX.md)
- [Support, Collaboration, and Implementation Policy](../../docs/SUPPORT_AND_COLLABORATION.md)

---

## Original Concept

Master / inchacomusho / InchaComisho

Structure, documentation, and code-design support: G (ChatGPT)

---

## License

CC BY 4.0

This article is released under the Creative Commons Attribution 4.0 International License (CC BY 4.0).  
Sharing, redistribution, translation, adaptation, and reuse are permitted as long as proper attribution is given.
