# Simulation Model

## Conceptual Background

The Cooling Credit Framework evaluates measurable cooling contribution in addition to conventional carbon accounting. Many climate impacts are experienced as accumulated heat: urban heat islands, surface heating, water-cycle disruption, soil drying, vegetation stress, waste heat, ocean warming, and rising cooling demand.

This model does not directly predict global mean temperature. It is an illustrative scenario model for comparing how Cooling Credit adoption may affect heat load, urban heat stress, water-cycle recovery, soil moisture, vegetation transpiration, waste-heat reduction, and ecological cooling capacity.

## Why Carbon-Only Accounting Is Insufficient

Carbon reduction remains essential, but carbon-only accounting cannot fully represent local and regional heat dynamics. A city can reduce emissions while still intensifying surface heat through pavement, building exhaust, reduced vegetation, and broken water circulation. Agricultural land can store carbon while losing water retention and cooling capacity. Cooling Credits therefore require a complementary evaluation layer focused on measurable thermal and hydrological outcomes.

## Why Heat-Load Reduction Needs Simulation

Cooling interventions interact. Rainwater reuse can support vegetation; vegetation can improve transpiration; soil moisture can reduce surface heating; building efficiency can reduce waste heat and cooling demand. A scenario model helps compare these interactions without claiming predictive certainty.

## Model Structure

The executable model uses yearly time steps from year 0 to year 30. Each scenario has target adoption levels for cooling interventions. Adoption follows a smooth curve, then indices are calculated from simplified relationships between interventions, heat-load reduction, water-cycle recovery, ecological cooling, and penalties.

## Scenario Definitions

- Baseline / No Cooling Credit: minimal implementation and continuing heat pressure.
- Low Adoption: limited pilots and partial local adoption.
- Medium Adoption: wider municipal and building-level adoption.
- High Adoption: broad urban, agricultural, and water-cycle implementation.
- Integrated Planetary Cooling Scenario: coordinated urban, soil, vegetation, waste-heat, water-cycle, and ocean-cooling support.

## Index Definitions

- `heat_load_index`: relative total heat-load pressure. Lower is better.
- `urban_heat_index`: relative urban heat stress. Lower is better.
- `surface_temperature_index`: relative surface temperature pressure. Lower is better.
- `water_cycle_index`: relative recovery of water circulation. Higher is better.
- `soil_moisture_index`: relative recovery of soil water retention. Higher is better.
- `vegetation_transpiration_index`: relative vegetation transpiration recovery. Higher is better.
- `waste_heat_index`: relative artificial waste-heat pressure. Lower is better.
- `cooling_demand_index`: relative cooling-energy demand pressure. Lower is better.
- `ecological_cooling_index`: relative ecological cooling capacity. Higher is better.
- `cooling_credit_score`: composite illustrative score after penalties.

## Intervention Variables

The model includes urban cooling adoption, water-cycle restoration, soil moisture recovery, vegetation transpiration recovery, waste-heat reduction, building efficiency, rainwater reuse, treated-water reuse, organic matter restoration, and ocean cooling support.

## Penalty Variables

The score is reduced by:

- `water_stress_penalty`: risk from unsustainable water use.
- `humidity_risk_penalty`: risk that misting or evaporation worsens WBGT.
- `ecological_risk_penalty`: risk from ecological intervention without monitoring.

## Example Interpretation

If a scenario lowers the heat-load index while raising the water-cycle and ecological cooling indices, it represents stronger relative alignment with Cooling Credit principles. If a scenario gains cooling through heavy water use or risky ecological intervention, the penalty terms reduce the score.

## Limitations

The model does not calculate actual global temperature reduction, regional weather change, or verified credit quantities. It uses stylized index relationships and assumed weights. It should be treated as a transparent educational and planning model, not as evidence of real-world climate effect.

## Future Extensions

Future versions could add regional climate parameters, WBGT equations, measured baseline data, uncertainty ranges, remote-sensing inputs, local water availability constraints, cost curves, biodiversity safeguards, and third-party verification datasets.
