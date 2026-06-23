#!/usr/bin/env python3
"""
Cooling Credit Scale and Temperature Impact Model

This script is a simplified scenario and sensitivity-analysis model.
It is NOT a climate prediction model.

Purpose:
- compare Cooling Credit implementation scales,
- estimate possible local/regional heat-load reduction indicators,
- translate cooling actions into a preliminary Cooling Score,
- visualize investment-scale and cooling-impact relationships.

Author concept: Master / inchacomusho / InchaComisho
Framework support: G (ChatGPT)
License: CC BY 4.0 where applicable to documentation; code may be reused with attribution.
"""

from __future__ import annotations

import argparse
import math
from pathlib import Path
from typing import Dict

import matplotlib.pyplot as plt
import pandas as pd


DEFAULT_INPUT = "example_inputs.csv"
OUTPUT_DIR = "outputs"


REQUIRED_COLUMNS = [
    "scenario",
    "scale_level",
    "project_area_ha",
    "mist_fan_units",
    "public_facility_retrofits",
    "organic_waste_tons_year",
    "urban_greening_ha",
    "forest_regeneration_ha",
    "soil_restoration_ha",
    "ocean_circulation_units",
    "investment_usd_million",
]


def saturating(value: float, scale: float, cap: float, floor: float = 0.0) -> float:
    """Simple saturating response curve."""
    value = max(float(value), 0.0)
    scale = max(float(scale), 1e-9)
    return floor + cap * (1.0 - math.exp(-value / scale))


def compute_action_index(row: pd.Series) -> float:
    """Weighted implementation index from heterogeneous Cooling Credit actions."""
    return (
        row["mist_fan_units"] * 0.0008
        + row["public_facility_retrofits"] * 0.015
        + row["organic_waste_tons_year"] * 0.00003
        + row["urban_greening_ha"] * 0.040
        + row["forest_regeneration_ha"] * 0.015
        + row["soil_restoration_ha"] * 0.020
        + row["ocean_circulation_units"] * 0.080
    )


def compute_results(df: pd.DataFrame) -> pd.DataFrame:
    """Compute simplified Cooling Credit scenario outputs."""
    df = df.copy()
    missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    numeric_cols = [col for col in REQUIRED_COLUMNS if col != "scenario"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0.0)

    df["cooling_action_index"] = df.apply(compute_action_index, axis=1)

    # Local/regional cooling indicators. These are bounded, scenario-level estimates.
    df["estimated_air_temp_reduction_c"] = df["cooling_action_index"].apply(
        lambda x: round(saturating(x, scale=3.0, cap=2.20, floor=0.05), 3)
    )
    df["estimated_surface_temp_reduction_c"] = df["cooling_action_index"].apply(
        lambda x: round(saturating(x, scale=4.0, cap=7.50, floor=0.10), 3)
    )
    df["estimated_wbgt_reduction_c"] = df["cooling_action_index"].apply(
        lambda x: round(saturating(x, scale=3.5, cap=1.65, floor=0.03), 3)
    )

    df["estimated_cooling_demand_reduction_pct"] = (
        df["estimated_air_temp_reduction_c"] * 4.5
        + df["estimated_surface_temp_reduction_c"] * 0.8
    ).clip(upper=22.0).round(2)

    # Co-benefit indices are bounded 0-100. They are intentionally simple.
    df["water_cycle_recovery_index"] = (
        (df["organic_waste_tons_year"] * 0.0002)
        + (df["urban_greening_ha"] * 0.20)
        + (df["forest_regeneration_ha"] * 0.030)
        + (df["soil_restoration_ha"] * 0.050)
    ).clip(upper=100).round(2)

    df["ecosystem_recovery_index"] = (
        (df["urban_greening_ha"] * 0.15)
        + (df["forest_regeneration_ha"] * 0.050)
        + (df["soil_restoration_ha"] * 0.035)
        + (df["ocean_circulation_units"] * 0.50)
    ).clip(upper=100).round(2)

    df["heat_risk_reduction_index"] = (
        df["estimated_wbgt_reduction_c"] * 35
        + df["estimated_air_temp_reduction_c"] * 15
        + df["public_facility_retrofits"] * 0.03
    ).clip(upper=100).round(2)

    # Composite preliminary score. This is not a formal credit issuance method.
    df["cooling_score"] = (
        df["estimated_air_temp_reduction_c"] * 25
        + df["estimated_wbgt_reduction_c"] * 25
        + df["estimated_surface_temp_reduction_c"] * 5
        + df["estimated_cooling_demand_reduction_pct"] * 2
        + df["water_cycle_recovery_index"] * 0.60
        + df["ecosystem_recovery_index"] * 0.50
        + df["heat_risk_reduction_index"] * 0.70
    ).round(2)

    scale_multiplier = (
        1
        + (df["project_area_ha"].clip(lower=0).apply(lambda x: math.log10(1 + x)) * 0.30)
        + (df["mist_fan_units"].clip(lower=0).apply(lambda x: math.log10(1 + x)) * 0.10)
        + (df["organic_waste_tons_year"].clip(lower=0).apply(lambda x: math.log10(1 + x)) * 0.10)
    )
    df["provisional_cooling_credits"] = (df["cooling_score"] * scale_multiplier).round(2)

    df["credits_per_million_usd"] = (
        df["provisional_cooling_credits"] / df["investment_usd_million"].replace(0, math.nan)
    ).round(2)

    return df


def plot_bar(df: pd.DataFrame, column: str, ylabel: str, title: str, path: Path) -> None:
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(df["scenario"], df[column])
    ax.set_title(title)
    ax.set_ylabel(ylabel)
    ax.set_xlabel("Scenario")
    ax.tick_params(axis="x", rotation=30)
    ax.grid(axis="y", linestyle="--", alpha=0.4)
    fig.tight_layout()
    fig.savefig(path, dpi=180)
    plt.close(fig)


def plot_line(df: pd.DataFrame, xcol: str, ycol: str, xlabel: str, ylabel: str, title: str, path: Path) -> None:
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df[xcol], df[ycol], marker="o")
    for _, row in df.iterrows():
        ax.annotate(row["scenario"], (row[xcol], row[ycol]), textcoords="offset points", xytext=(5, 5))
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(True, linestyle="--", alpha=0.4)
    fig.tight_layout()
    fig.savefig(path, dpi=180)
    plt.close(fig)


def make_outputs(df: pd.DataFrame, outdir: Path) -> None:
    outdir.mkdir(parents=True, exist_ok=True)
    df.to_csv(outdir / "scale_temperature_results.csv", index=False)

    plot_bar(
        df,
        "estimated_air_temp_reduction_c",
        "Estimated local / regional air temperature reduction (°C)",
        "Cooling Credit Scale vs Estimated Air Temperature Reduction",
        outdir / "scale_vs_air_temperature_reduction.png",
    )
    plot_bar(
        df,
        "estimated_wbgt_reduction_c",
        "Estimated WBGT reduction (°C)",
        "Cooling Credit Scale vs Estimated WBGT Reduction",
        outdir / "scale_vs_wbgt_reduction.png",
    )
    plot_bar(
        df,
        "estimated_cooling_demand_reduction_pct",
        "Estimated cooling demand reduction (%)",
        "Cooling Credit Scale vs Cooling Demand Reduction",
        outdir / "scale_vs_cooling_demand_reduction.png",
    )
    plot_bar(
        df,
        "cooling_score",
        "Cooling Score",
        "Scenario Cooling Score Comparison",
        outdir / "scale_vs_cooling_score.png",
    )
    plot_line(
        df,
        "investment_usd_million",
        "provisional_cooling_credits",
        "Investment (million USD)",
        "Provisional Cooling Credits",
        "Investment vs Provisional Cooling Credits",
        outdir / "investment_vs_cooling_credits.png",
    )
    plot_line(
        df,
        "investment_usd_million",
        "estimated_air_temp_reduction_c",
        "Investment (million USD)",
        "Estimated air temperature reduction (°C)",
        "Investment vs Estimated Air Temperature Reduction",
        outdir / "investment_vs_temperature_reduction.png",
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Cooling Credit scale-temperature scenario model")
    parser.add_argument("--input", default=DEFAULT_INPUT, help="Input CSV path")
    parser.add_argument("--output-dir", default=OUTPUT_DIR, help="Output directory")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    df = pd.read_csv(input_path)
    results = compute_results(df)
    make_outputs(results, Path(args.output_dir))

    print("Cooling Credit scale-temperature simulation completed.")
    print(f"Input: {input_path}")
    print(f"Output directory: {Path(args.output_dir).resolve()}")
    print(results[[
        "scenario",
        "estimated_air_temp_reduction_c",
        "estimated_wbgt_reduction_c",
        "estimated_cooling_demand_reduction_pct",
        "cooling_score",
        "provisional_cooling_credits",
    ]].to_string(index=False))


if __name__ == "__main__":
    main()
