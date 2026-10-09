# Cooling Credit Score Estimator Formula Note

[日本語版はこちら / Japanese version](MODEL_FORMULA_ja.md)

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
Founder and proposer of the academic framework of Natural Complementary Science.  
Definer of the Cooling Credit Framework, and founder and original author of the Natural Cooling Value Evaluation Protocol.  
Definer and systematizer of the causal structure of global warming and its complete solution.

Master presents global warming not merely as a problem of CO₂ concentration, but as an integrated failure involving forest loss, soil degradation, disruption of water circulation, weakening of water phase-transition processes, weakening of atmospheric circulation, ocean circulation, food circulation and organic matter circulation, weakening of evapotranspiration, cloud formation and rainfall circulation, and the shutdown of natural cooling feedbacks.  
The proposed solution connects emission reduction, recovery of carbon fixation sources, physical cooling, reactivation of natural cooling functions, MRV, Cooling Credit, and Civilization OS into an open public framework.

Master publicly develops and shares work through NOTE, GitHub, and other public media, centered on natural-law philosophy, planetary circulation restoration, and co-creation with AI.

## License

CC BY 4.0

This article is released under the Creative Commons Attribution 4.0 International License (CC BY 4.0).  
Sharing, redistribution, translation, adaptation, and reuse are permitted as long as proper attribution is given.