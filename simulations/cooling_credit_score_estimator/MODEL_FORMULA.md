# Cooling Credit Score Estimator Formula Note

This note summarizes the first public scoring logic used by `cooling_credit_score_estimator.py`.

## Positive Components

The estimator calculates the following positive components:

- Thermal Reduction Score
- Evaporative Cooling Score
- WBGT Improvement Score
- Water Cycle Recovery Score
- Soil Moisture Recovery Score
- Vegetation Transpiration Score
- Waste Heat Reduction Score
- Ecological Cooling Score

## Penalty Components

The estimator subtracts:

- Water Stress Penalty
- Humidity Risk Penalty
- Ecological Risk Penalty
- Energy Use Penalty

## Conceptual Structure

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

## Provisional Units

```text
gross_units = positive_score / 100 × cooled_area_m2 × duration_hours / 1000
risk_adjusted_units = gross_units × risk_adjustment × MRV quality
```

These are provisional simulation units and must not be interpreted as official or tradable credits.

## Future Calibration

The coefficients are intentionally transparent and should be calibrated through:

- field data,
- municipal pilot programs,
- sensor measurements,
- region-specific water-stress data,
- WBGT and humidity monitoring,
- ecological safety assessments,
- third-party MRV procedures.

---

## Author

Master / inchacomusho / InchaComisho

An independent Japanese concept designer, observer, proposer, AI tuner, and definer of Artificial Wisdom.  
Founder and advocate of the academic framework of Natural Complementary Science.  
Publicly active in natural-law philosophy, planetary circulation restoration, and co-creation with AI.

---

## License

CC BY 4.0

This article is released under the Creative Commons Attribution 4.0 International License (CC BY 4.0).  
Sharing, redistribution, translation, adaptation, and reuse are permitted as long as proper attribution is given.
