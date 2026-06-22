#!/usr/bin/env python3
"""
Cooling Credit Score Estimator

A preliminary, non-certification simulation model for estimating Cooling Credit
Score and provisional cooling-credit units from project-level input data.

This script is intended for:
- pre-feasibility evaluation,
- MRV design support,
- comparison between project scenarios,
- educational and policy-design simulations.

It is NOT an official certification engine and does not assign legally valid or
tradable credits.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, Iterable, List


LATENT_HEAT_KWH_PER_LITER = 2.45 / 3.6

REQUIRED_COLUMNS = [
    "project_id",
    "project_name",
    "technology_type",
    "baseline_air_temp_c",
    "reduced_air_temp_c",
    "baseline_surface_temp_c",
    "reduced_surface_temp_c",
    "baseline_wbgt_c",
    "reduced_wbgt_c",
    "cooled_area_m2",
    "duration_hours",
    "water_used_liters",
    "evaporated_water_liters",
    "recycled_water_ratio",
    "electricity_used_kwh",
    "soil_moisture_before_pct",
    "soil_moisture_after_pct",
    "vegetation_cover_before_pct",
    "vegetation_cover_after_pct",
    "waste_heat_reduction_kwh",
    "water_stress_level",
    "humidity_risk_level",
    "ecological_risk_level",
    "mrv_data_quality",
]


@dataclass
class ScoreBreakdown:
    project_id: str
    project_name: str
    technology_type: str
    thermal_reduction_score: float
    evaporative_cooling_score: float
    wbgt_improvement_score: float
    water_cycle_recovery_score: float
    soil_moisture_recovery_score: float
    vegetation_transpiration_score: float
    waste_heat_reduction_score: float
    ecological_cooling_score: float
    water_stress_penalty: float
    humidity_risk_penalty: float
    ecological_risk_penalty: float
    energy_use_penalty: float
    positive_score_before_penalties: float
    total_penalty: float
    cooling_credit_score: float
    gross_cooling_credit_units: float
    risk_adjusted_cooling_credit_units: float
    scenario_grade: str
    mrv_reliability_level: str
    estimated_evaporative_cooling_kwh_th: float
    net_air_temp_reduction_c: float
    net_surface_temp_reduction_c: float
    net_wbgt_reduction_c: float
    warnings: str


def clamp(value: float, minimum: float = 0.0, maximum: float = 100.0) -> float:
    return max(minimum, min(maximum, value))


def safe_float(row: Dict[str, str], key: str, default: float = 0.0) -> float:
    value = row.get(key, "")
    if value is None or value == "":
        return default
    try:
        return float(value)
    except ValueError:
        return default


def safe_text(row: Dict[str, str], key: str, default: str = "") -> str:
    value = row.get(key, default)
    return default if value is None else str(value)


def percent_to_ratio(value: float) -> float:
    if value > 1:
        return clamp(value, 0, 100) / 100
    return clamp(value, 0, 1)


def area_duration_factor(area_m2: float, duration_hours: float) -> float:
    area_factor = clamp(math.log1p(max(area_m2, 0.0)) / math.log1p(10000.0), 0.0, 1.0)
    duration_factor = clamp(math.log1p(max(duration_hours, 0.0)) / math.log1p(720.0), 0.0, 1.0)
    return 0.5 + 0.5 * ((area_factor + duration_factor) / 2.0)


def mrv_reliability(mrv_data_quality: float, warning_count: int) -> str:
    q = percent_to_ratio(mrv_data_quality)
    if warning_count >= 4:
        return "Low"
    if q >= 0.80 and warning_count <= 1:
        return "High"
    if q >= 0.50 and warning_count <= 3:
        return "Medium"
    return "Low"


def grade(score: float) -> str:
    if score >= 80:
        return "A"
    if score >= 65:
        return "B"
    if score >= 50:
        return "C"
    if score >= 35:
        return "D"
    return "E"


def evaluate_row(row: Dict[str, str]) -> ScoreBreakdown:
    project_id = safe_text(row, "project_id", "unknown")
    project_name = safe_text(row, "project_name", "Unnamed project")
    technology_type = safe_text(row, "technology_type", "unspecified")

    baseline_air = safe_float(row, "baseline_air_temp_c")
    reduced_air = safe_float(row, "reduced_air_temp_c")
    baseline_surface = safe_float(row, "baseline_surface_temp_c")
    reduced_surface = safe_float(row, "reduced_surface_temp_c")
    baseline_wbgt = safe_float(row, "baseline_wbgt_c")
    reduced_wbgt = safe_float(row, "reduced_wbgt_c")

    area_m2 = max(0.0, safe_float(row, "cooled_area_m2"))
    duration_hours = max(0.0, safe_float(row, "duration_hours"))

    water_used_liters = max(0.0, safe_float(row, "water_used_liters"))
    evaporated_water_liters = max(0.0, safe_float(row, "evaporated_water_liters"))
    recycled_water_ratio = percent_to_ratio(safe_float(row, "recycled_water_ratio"))

    electricity_used_kwh = max(0.0, safe_float(row, "electricity_used_kwh"))

    soil_before = safe_float(row, "soil_moisture_before_pct")
    soil_after = safe_float(row, "soil_moisture_after_pct")
    vegetation_before = safe_float(row, "vegetation_cover_before_pct")
    vegetation_after = safe_float(row, "vegetation_cover_after_pct")

    waste_heat_reduction_kwh = max(0.0, safe_float(row, "waste_heat_reduction_kwh"))

    water_stress_level = percent_to_ratio(safe_float(row, "water_stress_level"))
    humidity_risk_level = percent_to_ratio(safe_float(row, "humidity_risk_level"))
    ecological_risk_level = percent_to_ratio(safe_float(row, "ecological_risk_level"))
    mrv_data_quality = percent_to_ratio(safe_float(row, "mrv_data_quality", 0.5))

    warnings: List[str] = []

    air_drop = max(0.0, baseline_air - reduced_air)
    surface_drop = max(0.0, baseline_surface - reduced_surface)
    wbgt_drop = max(0.0, baseline_wbgt - reduced_wbgt)

    if baseline_air and reduced_air and reduced_air > baseline_air:
        warnings.append("air_temperature_increased")
    if baseline_surface and reduced_surface and reduced_surface > baseline_surface:
        warnings.append("surface_temperature_increased")
    if baseline_wbgt and reduced_wbgt and reduced_wbgt > baseline_wbgt:
        warnings.append("wbgt_increased")
    if water_used_liters > 0 and recycled_water_ratio < 0.2 and water_stress_level > 0.6:
        warnings.append("high_water_use_in_water_stressed_context")
    if evaporated_water_liters > 0 and humidity_risk_level > 0.7 and wbgt_drop <= 0:
        warnings.append("humidity_risk_without_wbgt_improvement")
    if ecological_risk_level > 0.7:
        warnings.append("high_ecological_risk_requires_stop_conditions")
    if mrv_data_quality < 0.5:
        warnings.append("low_mrv_data_quality")

    scale_factor = area_duration_factor(area_m2, duration_hours)

    thermal_reduction_score = clamp((air_drop * 18.0 + surface_drop * 7.0) * scale_factor)

    evap_cooling_kwh_th = evaporated_water_liters * LATENT_HEAT_KWH_PER_LITER
    thermal_density = evap_cooling_kwh_th / max(area_m2 * duration_hours, 1.0)
    evaporative_cooling_score = clamp(thermal_density / 0.05 * 100.0)

    wbgt_improvement_score = clamp(wbgt_drop * 25.0)

    water_efficiency_component = 100.0 if water_used_liters <= 0 else clamp((evaporated_water_liters / water_used_liters) * 100.0)
    recycled_component = recycled_water_ratio * 100.0
    water_cycle_recovery_score = clamp(0.65 * recycled_component + 0.35 * water_efficiency_component)

    soil_delta = max(0.0, soil_after - soil_before)
    soil_moisture_recovery_score = clamp(soil_delta * 5.0)

    vegetation_delta = max(0.0, vegetation_after - vegetation_before)
    vegetation_transpiration_score = clamp(vegetation_delta * 3.0)

    waste_heat_density = waste_heat_reduction_kwh / max(area_m2 * duration_hours, 1.0)
    waste_heat_reduction_score = clamp(waste_heat_density / 0.03 * 100.0)

    ecological_cooling_score = clamp(
        0.40 * soil_moisture_recovery_score
        + 0.40 * vegetation_transpiration_score
        + 0.20 * water_cycle_recovery_score
    )

    positive_score = clamp(
        0.20 * thermal_reduction_score
        + 0.12 * evaporative_cooling_score
        + 0.18 * wbgt_improvement_score
        + 0.12 * water_cycle_recovery_score
        + 0.10 * soil_moisture_recovery_score
        + 0.10 * vegetation_transpiration_score
        + 0.10 * waste_heat_reduction_score
        + 0.08 * ecological_cooling_score
    )

    water_use_intensity = water_used_liters / max(area_m2 * duration_hours, 1.0)
    water_stress_penalty = clamp(water_stress_level * (1.0 - recycled_water_ratio) * water_use_intensity / 0.5 * 20.0)

    evap_intensity = evaporated_water_liters / max(area_m2 * duration_hours, 1.0)
    humidity_risk_penalty = clamp(humidity_risk_level * evap_intensity / 0.3 * 15.0)
    if wbgt_drop > 0:
        humidity_risk_penalty *= 0.5

    ecological_risk_penalty = clamp(ecological_risk_level * 25.0)

    useful_cooling_kwh = evap_cooling_kwh_th + waste_heat_reduction_kwh
    energy_use_penalty = clamp((electricity_used_kwh / max(useful_cooling_kwh, 1.0)) * 10.0)

    total_penalty = clamp(
        water_stress_penalty + humidity_risk_penalty + ecological_risk_penalty + energy_use_penalty,
        0.0,
        100.0,
    )
    final_score = clamp(positive_score - total_penalty)

    gross_units = (positive_score / 100.0) * (area_m2 * duration_hours / 1000.0)
    risk_adjustment = (final_score / max(positive_score, 1.0)) * mrv_data_quality
    risk_adjusted_units = max(0.0, gross_units * risk_adjustment)

    reliability = mrv_reliability(mrv_data_quality, len(warnings))

    return ScoreBreakdown(
        project_id=project_id,
        project_name=project_name,
        technology_type=technology_type,
        thermal_reduction_score=round(thermal_reduction_score, 3),
        evaporative_cooling_score=round(evaporative_cooling_score, 3),
        wbgt_improvement_score=round(wbgt_improvement_score, 3),
        water_cycle_recovery_score=round(water_cycle_recovery_score, 3),
        soil_moisture_recovery_score=round(soil_moisture_recovery_score, 3),
        vegetation_transpiration_score=round(vegetation_transpiration_score, 3),
        waste_heat_reduction_score=round(waste_heat_reduction_score, 3),
        ecological_cooling_score=round(ecological_cooling_score, 3),
        water_stress_penalty=round(water_stress_penalty, 3),
        humidity_risk_penalty=round(humidity_risk_penalty, 3),
        ecological_risk_penalty=round(ecological_risk_penalty, 3),
        energy_use_penalty=round(energy_use_penalty, 3),
        positive_score_before_penalties=round(positive_score, 3),
        total_penalty=round(total_penalty, 3),
        cooling_credit_score=round(final_score, 3),
        gross_cooling_credit_units=round(gross_units, 3),
        risk_adjusted_cooling_credit_units=round(risk_adjusted_units, 3),
        scenario_grade=grade(final_score),
        mrv_reliability_level=reliability,
        estimated_evaporative_cooling_kwh_th=round(evap_cooling_kwh_th, 3),
        net_air_temp_reduction_c=round(air_drop, 3),
        net_surface_temp_reduction_c=round(surface_drop, 3),
        net_wbgt_reduction_c=round(wbgt_drop, 3),
        warnings=";".join(warnings),
    )


def load_rows(input_csv: Path) -> List[Dict[str, str]]:
    with input_csv.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        missing = [col for col in REQUIRED_COLUMNS if col not in (reader.fieldnames or [])]
        if missing:
            raise ValueError(f"Missing required columns: {', '.join(missing)}")
        return list(reader)


def write_csv(results: Iterable[ScoreBreakdown], output_csv: Path) -> None:
    rows = [asdict(result) for result in results]
    output_csv.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        return
    with output_csv.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def write_json(results: Iterable[ScoreBreakdown], output_json: Path) -> None:
    rows = [asdict(result) for result in results]
    output_json.parent.mkdir(parents=True, exist_ok=True)
    with output_json.open("w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)


def summarize(results: List[ScoreBreakdown]) -> str:
    if not results:
        return "No results."

    avg_score = sum(r.cooling_credit_score for r in results) / len(results)
    total_gross = sum(r.gross_cooling_credit_units for r in results)
    total_risk_adjusted = sum(r.risk_adjusted_cooling_credit_units for r in results)
    grades: Dict[str, int] = {}
    for result in results:
        grades[result.scenario_grade] = grades.get(result.scenario_grade, 0) + 1

    grade_summary = ", ".join(f"{k}:{v}" for k, v in sorted(grades.items()))
    return (
        f"Projects evaluated: {len(results)}\n"
        f"Average Cooling Credit Score: {avg_score:.3f}\n"
        f"Total gross preliminary units: {total_gross:.3f}\n"
        f"Total risk-adjusted preliminary units: {total_risk_adjusted:.3f}\n"
        f"Grade distribution: {grade_summary}\n"
        "\nDisclaimer: These are preliminary, non-certified simulation results."
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Estimate preliminary Cooling Credit Scores and provisional credit units from a CSV input file."
    )
    parser.add_argument("--input", required=True, help="Path to input CSV file.")
    parser.add_argument("--output", default="results/cooling_credit_score_results.csv", help="Path to output CSV file.")
    parser.add_argument("--json-output", default=None, help="Optional path to output JSON file.")
    parser.add_argument("--print-summary", action="store_true", help="Print summary metrics to stdout.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    rows = load_rows(Path(args.input))
    results = [evaluate_row(row) for row in rows]
    write_csv(results, Path(args.output))
    if args.json_output:
        write_json(results, Path(args.json_output))
    if args.print_summary:
        print(summarize(results))


if __name__ == "__main__":
    main()
