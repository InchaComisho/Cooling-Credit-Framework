"""
High-Humidity Cooling Credit Simulation
日本型高湿度クーリングクレジット・シミュレーション

Purpose: Pre-verification comparison of cooling models for humid climates
         (mist evaporative, dehumidification+airflow, rainwater+humus+soil)
Note: This is a design-level simplified model, not a substitute for field measurement.
"""

import csv
import math
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)

SCENARIOS = [
    {
        "name": "Japan rainy season / 梅雨",
        "air_temp_c": 29.0,
        "relative_humidity": 85,
        "wind_speed_m_s": 1.0,
        "solar_index": 0.45,
        "rainfall_mm_week": 80,
        "soil_moisture_base": 0.55,
    },
    {
        "name": "Japan midsummer / 真夏",
        "air_temp_c": 35.0,
        "relative_humidity": 62,
        "wind_speed_m_s": 1.4,
        "solar_index": 0.85,
        "rainfall_mm_week": 20,
        "soil_moisture_base": 0.28,
    },
    {
        "name": "Dry hot region / 乾燥高温地域",
        "air_temp_c": 38.0,
        "relative_humidity": 28,
        "wind_speed_m_s": 2.0,
        "solar_index": 0.95,
        "rainfall_mm_week": 2,
        "soil_moisture_base": 0.12,
    },
    {
        "name": "Humid tropical city / 高湿度熱帯都市",
        "air_temp_c": 32.0,
        "relative_humidity": 78,
        "wind_speed_m_s": 1.1,
        "solar_index": 0.75,
        "rainfall_mm_week": 55,
        "soil_moisture_base": 0.48,
    },
]

DEHUMIDIFICATION_LEVELS = [10, 15, 20, 25]


# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------

def wind_factor(wind_speed_m_s: float) -> float:
    return min(1.0, 0.5 + wind_speed_m_s * 0.25)


def approx_wet_bulb(air_temp_c: float, rh: float) -> float:
    """Simplified wet-bulb approximation (Stull 2011 formula variant)."""
    return (
        air_temp_c * math.atan(0.151977 * (rh + 8.313659) ** 0.5)
        + math.atan(air_temp_c + rh)
        - math.atan(rh - 1.676331)
        + 0.00391838 * rh ** 1.5 * math.atan(0.023101 * rh)
        - 4.686035
    )


def approx_wbgt(air_temp_c: float, rh: float, solar_index: float) -> float:
    """Simplified WBGT: 0.7*Tw + 0.2*Tg + 0.1*Ta"""
    wet_bulb = approx_wet_bulb(air_temp_c, rh)
    globe_temp = air_temp_c + solar_index * 6.0
    return 0.7 * wet_bulb + 0.2 * globe_temp + 0.1 * air_temp_c


# ---------------------------------------------------------------------------
# Model 1: Mist Evaporative Cooling
# ---------------------------------------------------------------------------

def model_mist(scenario: dict) -> dict:
    rh = scenario["relative_humidity"]
    ws = scenario["wind_speed_m_s"]
    si = scenario["solar_index"]

    dryness_factor = max(0.0, (100 - rh) / 100)
    wf = wind_factor(ws)
    mist_temp_reduction = 5.0 * dryness_factor * (0.6 + 0.4 * wf)
    mist_temp_reduction = min(max(mist_temp_reduction, 0.0), 5.5)

    # WBGT: mist slightly raises humidity, so WBGT benefit is less than temp reduction
    new_temp = scenario["air_temp_c"] - mist_temp_reduction
    humidity_rise = dryness_factor * 8.0
    new_rh = min(rh + humidity_rise, 100)
    wbgt_before = approx_wbgt(scenario["air_temp_c"], rh, si)
    wbgt_after = approx_wbgt(new_temp, new_rh, si)
    wbgt_reduction = max(wbgt_before - wbgt_after, 0.0)

    water_cycle_score = dryness_factor * 0.6

    cooling_score = (
        mist_temp_reduction * 1.0
        + wbgt_reduction * 1.4
        + 0.0  # no soil cooling
        + water_cycle_score * 1.2
    )

    recommended = (
        "High effectiveness in dry conditions"
        if rh < 50
        else "Limited by high humidity; consider dehumidification supplement"
    )
    limitations = (
        "Effectiveness drops sharply above 70% RH; may worsen WBGT in humid climates"
        if rh >= 70
        else "Requires consistent water supply"
    )

    return {
        "model": "Mist Evaporative Cooling",
        "estimated_temp_reduction_c": round(mist_temp_reduction, 2),
        "estimated_wbgt_reduction_c": round(wbgt_reduction, 2),
        "soil_cooling_potential_c": 0.0,
        "water_cycle_score": round(water_cycle_score, 2),
        "cooling_score": round(cooling_score, 2),
        "recommended_use": recommended,
        "limitations": limitations,
    }


# ---------------------------------------------------------------------------
# Model 2: Dehumidification + Airflow Cooling
# ---------------------------------------------------------------------------

def model_dehumidification(scenario: dict, dehumidification_pct: float = 18.0) -> dict:
    rh = scenario["relative_humidity"]
    air_temp = scenario["air_temp_c"]
    si = scenario["solar_index"]
    ws = scenario["wind_speed_m_s"]

    dehumidified_rh = max(rh - dehumidification_pct, 35)
    wbgt_before = approx_wbgt(air_temp, rh, si)
    wbgt_after = approx_wbgt(air_temp, dehumidified_rh, si)
    wbgt_reduction = max(wbgt_before - wbgt_after, 0.0)

    # Small sensible cooling via airflow
    wf = wind_factor(ws)
    temp_reduction = wf * 0.8

    # Dehumidification benefit is highest when baseline humidity is high
    humidity_benefit_factor = min(rh / 100, 1.0)
    water_cycle_score = humidity_benefit_factor * 0.5

    cooling_score = (
        temp_reduction * 1.0
        + wbgt_reduction * 1.4
        + 0.0
        + water_cycle_score * 1.2
    )

    recommended = (
        "Primary strategy for rainy season / high-humidity WBGT reduction"
        if rh >= 70
        else "Useful supplement; most effective above 70% RH"
    )
    limitations = "Energy cost of dehumidification; less effective in dry regions"

    return {
        "model": "Dehumidification + Airflow Cooling",
        "estimated_temp_reduction_c": round(temp_reduction, 2),
        "estimated_wbgt_reduction_c": round(wbgt_reduction, 2),
        "soil_cooling_potential_c": 0.0,
        "water_cycle_score": round(water_cycle_score, 2),
        "cooling_score": round(cooling_score, 2),
        "recommended_use": recommended,
        "limitations": limitations,
    }


# ---------------------------------------------------------------------------
# Model 3: Rainwater + Humus + Soil Moisture Cooling Potential
# ---------------------------------------------------------------------------

def model_soil_moisture(scenario: dict) -> dict:
    si = scenario["solar_index"]
    rainfall = scenario["rainfall_mm_week"]
    soil_base = scenario["soil_moisture_base"]
    air_temp = scenario["air_temp_c"]
    rh = scenario["relative_humidity"]

    rainwater_storage_score = min(rainfall / 80.0, 1.0)
    humus_effect = 0.25
    soil_moisture_gain = rainwater_storage_score * 0.25 + humus_effect
    evapotranspiration_potential = min(soil_base + soil_moisture_gain, 1.0)
    soil_cooling_potential = evapotranspiration_potential * si * 4.0

    # Minimal direct temp reduction (indirect via ET)
    temp_reduction = soil_cooling_potential * 0.3

    # WBGT: cooling comes from long-term ET; near-term WBGT change is modest
    wbgt_before = approx_wbgt(air_temp, rh, si)
    new_temp = air_temp - temp_reduction
    wbgt_after = approx_wbgt(new_temp, rh, si)
    wbgt_reduction = max(wbgt_before - wbgt_after, 0.0)

    water_cycle_score = rainwater_storage_score * 0.9 + humus_effect * 0.5

    cooling_score = (
        temp_reduction * 1.0
        + wbgt_reduction * 1.4
        + soil_cooling_potential * 0.8
        + water_cycle_score * 1.2
    )

    recommended = (
        "Rainy season is a resource-loading period; primes summer cooling via soil moisture"
        if rainfall >= 40
        else "Supplemental value in low-rainfall season; depends on prior soil preparation"
    )
    limitations = (
        "Effect is indirect and delayed; requires ecosystem preparation (humus, ground cover)"
    )

    return {
        "model": "Rainwater + Humus + Soil Moisture",
        "estimated_temp_reduction_c": round(temp_reduction, 2),
        "estimated_wbgt_reduction_c": round(wbgt_reduction, 2),
        "soil_cooling_potential_c": round(soil_cooling_potential, 2),
        "water_cycle_score": round(water_cycle_score, 2),
        "cooling_score": round(cooling_score, 2),
        "recommended_use": recommended,
        "limitations": limitations,
    }


# ---------------------------------------------------------------------------
# WBGT reduction by dehumidification level
# ---------------------------------------------------------------------------

def wbgt_by_dehumidification(scenario: dict) -> dict:
    results = {}
    base_wbgt = approx_wbgt(
        scenario["air_temp_c"], scenario["relative_humidity"], scenario["solar_index"]
    )
    for pct in DEHUMIDIFICATION_LEVELS:
        new_rh = max(scenario["relative_humidity"] - pct, 35)
        new_wbgt = approx_wbgt(scenario["air_temp_c"], new_rh, scenario["solar_index"])
        results[pct] = round(max(base_wbgt - new_wbgt, 0.0), 3)
    return results


# ---------------------------------------------------------------------------
# Run all scenarios and collect results
# ---------------------------------------------------------------------------

def run_simulation():
    rows = []
    for s in SCENARIOS:
        for model_fn in [model_mist, model_dehumidification, model_soil_moisture]:
            r = model_fn(s)
            row = {
                "scenario": s["name"],
                "air_temp_c": s["air_temp_c"],
                "relative_humidity": s["relative_humidity"],
            }
            row.update(r)
            rows.append(row)
    return rows


# ---------------------------------------------------------------------------
# CSV export
# ---------------------------------------------------------------------------

CSV_FIELDS = [
    "scenario",
    "model",
    "air_temp_c",
    "relative_humidity",
    "estimated_temp_reduction_c",
    "estimated_wbgt_reduction_c",
    "soil_cooling_potential_c",
    "water_cycle_score",
    "cooling_score",
    "recommended_use",
    "limitations",
]


def save_csv(rows: list, path: str):
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_FIELDS)
        writer.writeheader()
        writer.writerows(rows)
    print(f"CSV saved: {path}")


# ---------------------------------------------------------------------------
# Plot 1: Cooling Score by Model (grouped bar)
# ---------------------------------------------------------------------------

def plot_cooling_score_by_model(rows: list, path: str):
    scenario_names = [s["name"] for s in SCENARIOS]
    models = ["Mist Evaporative Cooling", "Dehumidification + Airflow Cooling", "Rainwater + Humus + Soil Moisture"]
    colors = ["#4ECDC4", "#45B7D1", "#96CEB4"]

    x = np.arange(len(scenario_names))
    width = 0.25

    fig, ax = plt.subplots(figsize=(13, 6))
    for i, (model, color) in enumerate(zip(models, colors)):
        scores = [r["cooling_score"] for r in rows if r["model"] == model]
        bars = ax.bar(x + i * width, scores, width, label=model, color=color, edgecolor="white", linewidth=0.8)
        for bar, score in zip(bars, scores):
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height() + 0.05,
                f"{score:.1f}",
                ha="center", va="bottom", fontsize=8
            )

    ax.set_xlabel("Scenario", fontsize=11)
    ax.set_ylabel("Cooling Score (composite, arb. units)", fontsize=11)
    ax.set_title("High-Humidity Cooling Credit Simulation\nCooling Score by Scenario and Model", fontsize=13)
    ax.set_xticks(x + width)
    scenario_labels = [s.replace(" / ", "\n") for s in scenario_names]
    ax.set_xticklabels(scenario_labels, fontsize=9)
    ax.legend(fontsize=9, loc="upper right")
    ax.set_ylim(0, max(r["cooling_score"] for r in rows) * 1.3)
    ax.grid(axis="y", alpha=0.3)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)
    print(f"PNG saved: {path}")


# ---------------------------------------------------------------------------
# Plot 2: Seasonal model priority (heatmap)
# ---------------------------------------------------------------------------

def plot_seasonal_model_priority(rows: list, path: str):
    scenario_names = [s["name"] for s in SCENARIOS]
    models = ["Mist Evaporative Cooling", "Dehumidification + Airflow Cooling", "Rainwater + Humus + Soil Moisture"]
    short_models = ["Mist\nEvaporative", "Dehum +\nAirflow", "Rainwater\n+Humus+Soil"]

    matrix = np.zeros((len(models), len(scenario_names)))
    for j, sname in enumerate(scenario_names):
        scenario_rows = [r for r in rows if r["scenario"] == sname]
        max_score = max(r["cooling_score"] for r in scenario_rows)
        for i, model in enumerate(models):
            score = next(r["cooling_score"] for r in scenario_rows if r["model"] == model)
            matrix[i, j] = score / max_score if max_score > 0 else 0

    fig, ax = plt.subplots(figsize=(11, 4.5))
    im = ax.imshow(matrix, cmap="YlOrRd", aspect="auto", vmin=0, vmax=1)

    ax.set_xticks(range(len(scenario_names)))
    ax.set_xticklabels([s.replace(" / ", "\n") for s in scenario_names], fontsize=9)
    ax.set_yticks(range(len(models)))
    ax.set_yticklabels(short_models, fontsize=10)

    for i in range(len(models)):
        for j in range(len(scenario_names)):
            val = matrix[i, j]
            label = "★ BEST" if val == 1.0 else f"{val:.2f}"
            color = "white" if val > 0.75 else "black"
            ax.text(j, i, label, ha="center", va="center", fontsize=9, color=color, fontweight="bold" if val == 1.0 else "normal")

    plt.colorbar(im, ax=ax, label="Relative Priority (1.0 = highest score in scenario)")
    ax.set_title("Seasonal Model Priority\n(Normalized Cooling Score per Scenario)", fontsize=12)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)
    print(f"PNG saved: {path}")


# ---------------------------------------------------------------------------
# Plot 3: WBGT reduction by dehumidification level
# ---------------------------------------------------------------------------

def plot_wbgt_reduction_by_dehumidification(path: str):
    scenario_names = [s["name"] for s in SCENARIOS]
    colors = ["#2E86AB", "#A23B72", "#F18F01", "#C73E1D"]

    fig, ax = plt.subplots(figsize=(10, 6))
    x = np.arange(len(DEHUMIDIFICATION_LEVELS))
    width = 0.2

    for i, (s, color) in enumerate(zip(SCENARIOS, colors)):
        reductions = wbgt_by_dehumidification(s)
        vals = [reductions[pct] for pct in DEHUMIDIFICATION_LEVELS]
        bars = ax.bar(x + i * width, vals, width, label=s["name"].replace(" / ", "\n"), color=color, edgecolor="white")
        for bar, v in zip(bars, vals):
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height() + 0.005,
                f"{v:.2f}",
                ha="center", va="bottom", fontsize=7.5
            )

    ax.set_xlabel("Dehumidification Applied (%RH reduction)", fontsize=11)
    ax.set_ylabel("WBGT Reduction (°C)", fontsize=11)
    ax.set_title("WBGT Reduction by Dehumidification Level\nAcross Scenarios", fontsize=12)
    ax.set_xticks(x + width * 1.5)
    ax.set_xticklabels([f"−{p}% RH" for p in DEHUMIDIFICATION_LEVELS], fontsize=10)
    ax.legend(fontsize=8, loc="upper left")
    ax.set_ylim(0, max(
        wbgt_by_dehumidification(s)[pct]
        for s in SCENARIOS for pct in DEHUMIDIFICATION_LEVELS
    ) * 1.35)
    ax.grid(axis="y", alpha=0.3)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)
    print(f"PNG saved: {path}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("=" * 60)
    print("High-Humidity Cooling Credit Simulation")
    print("日本型高湿度クーリングクレジット・シミュレーション")
    print("=" * 60)

    rows = run_simulation()

    # --- summary to stdout ---
    for s in SCENARIOS:
        print(f"\n[Scenario] {s['name']}")
        print(f"  Temp={s['air_temp_c']}°C  RH={s['relative_humidity']}%  "
              f"Wind={s['wind_speed_m_s']}m/s  Solar={s['solar_index']}")
        scenario_rows = [r for r in rows if r["scenario"] == s["name"]]
        for r in scenario_rows:
            print(f"  {r['model'][:38]:38s}  CoolingScore={r['cooling_score']:.2f}  "
                  f"ΔTemp={r['estimated_temp_reduction_c']:.2f}°C  "
                  f"ΔWBGT={r['estimated_wbgt_reduction_c']:.2f}°C")

    # --- CSV ---
    csv_path = os.path.join(OUTPUT_DIR, "high_humidity_cooling_credit_results.csv")
    save_csv(rows, csv_path)

    # --- Plots ---
    plot_cooling_score_by_model(
        rows,
        os.path.join(OUTPUT_DIR, "high_humidity_cooling_score_by_model.png"),
    )
    plot_seasonal_model_priority(
        rows,
        os.path.join(OUTPUT_DIR, "seasonal_model_priority.png"),
    )
    plot_wbgt_reduction_by_dehumidification(
        os.path.join(OUTPUT_DIR, "wbgt_reduction_by_dehumidification.png"),
    )

    print("\nSimulation complete.")
    print(f"Outputs: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
