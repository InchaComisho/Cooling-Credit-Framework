"""Cooling Credit Impact Simulation.

This is an illustrative scenario simulation, not a climate prediction model.
It is intended to compare relative effects of Cooling Credit adoption scenarios
on heat-load reduction, water-cycle recovery, and ecological cooling capacity.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


YEARS = np.arange(0, 31)
BASE_DIR = Path(__file__).resolve().parent
RESULTS_DIR = BASE_DIR / "results"


@dataclass(frozen=True)
class Scenario:
    name: str
    urban_cooling_adoption: float
    water_cycle_restoration: float
    soil_moisture_recovery: float
    vegetation_transpiration_recovery: float
    waste_heat_reduction: float
    building_efficiency: float
    rainwater_reuse: float
    treated_water_reuse: float
    organic_matter_restoration: float
    ocean_cooling_support: float
    water_stress_penalty: float
    humidity_risk_penalty: float
    ecological_risk_penalty: float


SCENARIOS = [
    Scenario("Baseline / No Cooling Credit", 0.03, 0.02, 0.02, 0.02, 0.01, 0.03, 0.01, 0.01, 0.02, 0.00, 0.02, 0.01, 0.01),
    Scenario("Low Adoption", 0.22, 0.18, 0.16, 0.18, 0.14, 0.20, 0.16, 0.12, 0.16, 0.04, 0.05, 0.04, 0.04),
    Scenario("Medium Adoption", 0.48, 0.42, 0.38, 0.42, 0.34, 0.42, 0.36, 0.30, 0.36, 0.12, 0.07, 0.06, 0.06),
    Scenario("High Adoption", 0.72, 0.66, 0.62, 0.66, 0.56, 0.64, 0.58, 0.52, 0.60, 0.24, 0.10, 0.08, 0.08),
    Scenario("Integrated Planetary Cooling Scenario", 0.86, 0.86, 0.82, 0.84, 0.72, 0.76, 0.76, 0.72, 0.80, 0.64, 0.12, 0.10, 0.12),
]


def adoption_curve(year: int, target: float) -> float:
    """Smooth adoption path that starts slowly and approaches the scenario target."""
    if target <= 0:
        return 0.0
    midpoint = 13.0
    steepness = 0.24
    initial = 1 / (1 + np.exp(steepness * midpoint))
    value = 1 / (1 + np.exp(-steepness * (year - midpoint)))
    normalized = (value - initial) / (1 - initial)
    return float(np.clip(target * normalized, 0, target))


def simulate_scenario(scenario: Scenario) -> pd.DataFrame:
    rows = []
    for year in YEARS:
        urban = adoption_curve(year, scenario.urban_cooling_adoption)
        water = adoption_curve(year, scenario.water_cycle_restoration)
        soil = adoption_curve(year, scenario.soil_moisture_recovery)
        vegetation = adoption_curve(year, scenario.vegetation_transpiration_recovery)
        waste = adoption_curve(year, scenario.waste_heat_reduction)
        building = adoption_curve(year, scenario.building_efficiency)
        rainwater = adoption_curve(year, scenario.rainwater_reuse)
        treated = adoption_curve(year, scenario.treated_water_reuse)
        organic = adoption_curve(year, scenario.organic_matter_restoration)
        ocean = adoption_curve(year, scenario.ocean_cooling_support)

        background_heat_pressure = year * 0.42
        heat_reduction = 17 * urban + 11 * water + 9 * vegetation + 7 * soil + 8 * waste + 4 * ocean
        heat_load_index = 100 + background_heat_pressure - heat_reduction
        urban_heat_index = 100 + year * 0.35 - (18 * urban + 8 * vegetation + 6 * building + 5 * rainwater)
        surface_temperature_index = 100 + year * 0.30 - (14 * urban + 9 * soil + 9 * vegetation + 5 * water)
        water_cycle_index = 100 - year * 0.10 + (12 * water + 8 * rainwater + 7 * treated + 6 * soil + 5 * vegetation)
        soil_moisture_index = 100 - year * 0.12 + (14 * soil + 8 * organic + 4 * rainwater)
        vegetation_transpiration_index = 100 - year * 0.08 + (13 * vegetation + 7 * soil + 5 * water + 3 * organic)
        waste_heat_index = 100 + year * 0.24 - (15 * waste + 12 * building)
        cooling_demand_index = 100 + year * 0.28 - (10 * urban + 9 * building + 5 * vegetation + 4 * waste)
        ecological_cooling_index = 100 - year * 0.08 + (11 * soil + 12 * vegetation + 8 * organic + 7 * water + 4 * ocean)

        water_stress_penalty = scenario.water_stress_penalty * (rainwater + treated + water) * 16
        humidity_risk_penalty = scenario.humidity_risk_penalty * max(urban + rainwater - 0.45, 0) * 18
        ecological_risk_penalty = scenario.ecological_risk_penalty * max(vegetation + ocean - 0.55, 0) * 16

        cooling_credit_score = (
            (100 - heat_load_index) * 0.24
            + (100 - urban_heat_index) * 0.15
            + (water_cycle_index - 100) * 0.16
            + (soil_moisture_index - 100) * 0.11
            + (vegetation_transpiration_index - 100) * 0.11
            + (100 - waste_heat_index) * 0.12
            + (100 - cooling_demand_index) * 0.08
            + (ecological_cooling_index - 100) * 0.13
            - water_stress_penalty
            - humidity_risk_penalty
            - ecological_risk_penalty
        )

        rows.append(
            {
                "scenario": scenario.name,
                "year": year,
                "urban_cooling_adoption": urban,
                "water_cycle_restoration": water,
                "soil_moisture_recovery": soil,
                "vegetation_transpiration_recovery": vegetation,
                "waste_heat_reduction": waste,
                "building_efficiency": building,
                "rainwater_reuse": rainwater,
                "treated_water_reuse": treated,
                "organic_matter_restoration": organic,
                "ocean_cooling_support": ocean,
                "heat_load_index": heat_load_index,
                "urban_heat_index": urban_heat_index,
                "surface_temperature_index": surface_temperature_index,
                "water_cycle_index": water_cycle_index,
                "soil_moisture_index": soil_moisture_index,
                "vegetation_transpiration_index": vegetation_transpiration_index,
                "waste_heat_index": waste_heat_index,
                "cooling_demand_index": cooling_demand_index,
                "ecological_cooling_index": ecological_cooling_index,
                "water_stress_penalty": water_stress_penalty,
                "humidity_risk_penalty": humidity_risk_penalty,
                "ecological_risk_penalty": ecological_risk_penalty,
                "cooling_credit_score": cooling_credit_score,
            }
        )
    return pd.DataFrame(rows)


def plot_lines(data: pd.DataFrame, column: str, title: str, ylabel: str, filename: str) -> None:
    fig, ax = plt.subplots(figsize=(10, 6))
    for scenario, group in data.groupby("scenario"):
        ax.plot(group["year"], group[column], label=scenario, linewidth=2)
    ax.set_title(title)
    ax.set_xlabel("Year")
    ax.set_ylabel(ylabel)
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(RESULTS_DIR / filename, dpi=160)
    plt.close(fig)


def plot_component_contribution(data: pd.DataFrame) -> None:
    final_year = data[data["year"] == YEARS[-1]].copy()
    final_year["heat_reduction_component"] = 100 - final_year["heat_load_index"]
    final_year["water_recovery_component"] = final_year["water_cycle_index"] - 100
    final_year["ecological_recovery_component"] = final_year["ecological_cooling_index"] - 100
    final_year["waste_heat_component"] = 100 - final_year["waste_heat_index"]

    components = [
        "heat_reduction_component",
        "water_recovery_component",
        "ecological_recovery_component",
        "waste_heat_component",
    ]
    labels = ["Heat reduction", "Water-cycle recovery", "Ecological recovery", "Waste-heat reduction"]

    fig, ax = plt.subplots(figsize=(11, 6))
    bottom = np.zeros(len(final_year))
    x = np.arange(len(final_year))
    for component, label in zip(components, labels):
        values = final_year[component].to_numpy()
        ax.bar(x, values, bottom=bottom, label=label)
        bottom += values
    ax.set_title("Year 30 Component Contribution by Scenario")
    ax.set_xticks(x)
    ax.set_xticklabels(final_year["scenario"], rotation=25, ha="right")
    ax.set_ylabel("Relative index-point contribution")
    ax.grid(True, axis="y", alpha=0.3)
    ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(RESULTS_DIR / "cooling_credit_component_contribution.png", dpi=160)
    plt.close(fig)


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    data = pd.concat([simulate_scenario(scenario) for scenario in SCENARIOS], ignore_index=True)
    csv_path = RESULTS_DIR / "cooling_credit_scenario_summary.csv"
    data.to_csv(csv_path, index=False)

    plot_lines(
        data,
        "surface_temperature_index",
        "Illustrative Surface Temperature Index by Scenario",
        "Surface temperature index",
        "cooling_credit_temperature_index.png",
    )
    plot_lines(
        data,
        "heat_load_index",
        "Illustrative Heat Load Index by Scenario",
        "Heat load index",
        "cooling_credit_heat_load_index.png",
    )
    plot_lines(
        data,
        "water_cycle_index",
        "Illustrative Water-Cycle Recovery Index by Scenario",
        "Water-cycle index",
        "cooling_credit_water_cycle_index.png",
    )
    plot_component_contribution(data)

    final = data[data["year"] == YEARS[-1]][["scenario", "heat_load_index", "water_cycle_index", "cooling_credit_score"]]
    print("Cooling Credit illustrative scenario simulation complete.")
    print("This is not a climate prediction model.")
    print(final.to_string(index=False, formatters={
        "heat_load_index": "{:.2f}".format,
        "water_cycle_index": "{:.2f}".format,
        "cooling_credit_score": "{:.2f}".format,
    }))
    print(f"\nSaved CSV: {csv_path}")
    print(f"Saved PNG files in: {RESULTS_DIR}")


if __name__ == "__main__":
    main()
