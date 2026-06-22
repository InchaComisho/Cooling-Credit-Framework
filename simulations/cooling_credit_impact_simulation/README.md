# Cooling Credit Impact Simulation

## Purpose

This directory contains an executable illustrative scenario model for the Cooling Credit Framework. The model compares how different levels of Cooling Credit adoption may affect heat-load reduction, water-cycle recovery, waste-heat reduction, and ecological cooling capacity over 30 years.

This is not a prediction model. It is a transparent comparison tool for exploring relative scenario behavior.

## What the Model Simulates

The simulation uses yearly time steps from year 0 to year 30. It tracks simplified indices for heat load, urban heat, surface temperature, water-cycle recovery, soil moisture, vegetation transpiration, waste heat, cooling demand, ecological cooling, and a composite Cooling Credit Score.

Cooling Credits are evaluated not as permission to emit, but as measurable contributions to heat-load reduction and natural cooling recovery.

## Scenarios

The script compares five scenarios:

- Baseline / No Cooling Credit
- Low Adoption
- Medium Adoption
- High Adoption
- Integrated Planetary Cooling Scenario

## Variables

Main intervention variables include urban cooling adoption, water-cycle restoration, soil moisture recovery, vegetation transpiration recovery, waste-heat reduction, building efficiency, rainwater reuse, treated-water reuse, organic matter restoration, and ocean cooling support.

The model also applies water stress, humidity risk, and ecological risk penalties. These penalties reduce the final score when implementation depends too heavily on water use, excessive misting, or ecological intervention without sufficient safeguards.

## Outputs

Running the script generates:

- `results/cooling_credit_scenario_summary.csv`
- `results/cooling_credit_temperature_index.png`
- `results/cooling_credit_heat_load_index.png`
- `results/cooling_credit_water_cycle_index.png`
- `results/cooling_credit_component_contribution.png`

## How to Run

From the repository root:

```bash
python simulations/cooling_credit_impact_simulation/cooling_credit_impact_simulation.py
```

The script requires Python with `pandas`, `numpy`, and `matplotlib`.

## Interpretation

Lower heat-related indices indicate lower relative heat load or heat stress. Higher water-cycle, soil moisture, vegetation transpiration, and ecological cooling indices indicate stronger recovery of natural cooling capacity.

The Cooling Credit Score is a composite index. It should be interpreted as a relative scenario score, not as a direct unit of global temperature reduction.

## Limitations

The model uses simplified relationships and assumed parameter weights. It does not resolve atmospheric physics, hydrology, ocean dynamics, biodiversity response, or economic behavior. It does not calculate actual global mean temperature change.

## Relationship with Cooling Credit Framework

The simulation supports the framework by making the difference between conceptual credit design and measurable implementation more concrete. It shows how credit evaluation can combine heat reduction, water-cycle recovery, soil and vegetation cooling, waste-heat reduction, cooling-demand reduction, and risk penalties.
