# Quickstart

Run from the repository root:

```bash
python simulations/cooling_credit_score_estimator/cooling_credit_score_estimator.py \
  --input simulations/cooling_credit_score_estimator/example_inputs.csv \
  --output simulations/cooling_credit_score_estimator/results/cooling_credit_score_results.csv \
  --json-output simulations/cooling_credit_score_estimator/results/cooling_credit_score_results.json \
  --print-summary
```

Expected summary:

```text
Projects evaluated: 4
Average Cooling Credit Score: 30.443
Total gross preliminary units: 3900.263
Total risk-adjusted preliminary units: 2172.396
Grade distribution: D:2, E:2

Disclaimer: These are preliminary, non-certified simulation results.
```
