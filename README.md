# Telco Churn Retention Planner

A reproducible churn-ranking prototype that turns model probabilities into a capacity-limited outreach list, with a holdout subgroup error audit.

## Dataset and provenance

Uses the [UCI Iranian Churn dataset (ID 563)](https://archive.ics.uci.edu/dataset/563/iranian%2Bchurn%2Bdatase). It contains 3,150 telecom customer records. UCI documents that the predictors aggregate the first nine months and the churn state is recorded at month 12, leaving a three-month planning gap. The source is a single-company sample, not a representative benchmark of current telecom customers.

## Reproduce

Download the UCI CSV to a private local path. Install dependencies and run:

```bash
python -m pip install -r requirements.txt
python main.py --input "Customer Churn.csv" --target Churn --positive-label 1 --group "Age Group" --contact-share 0.10
```

The runner writes aggregate metrics, holdout probabilities, a local outreach queue, and a serialized model under `outputs/`. Raw data and row-level outputs are ignored by Git.

## Holdout results

Seed-42 stratified random 75/25 split; 2,362 train and 788 holdout records. Threshold 0.50, positive label 1.

| ROC-AUC | Average precision | Brier score | Balanced accuracy |
|---:|---:|---:|---:|
| 0.922 | 0.731 | 0.113 | 0.843 |

At a 10% contact capacity, the score-ranked queue captured 70.5% of the holdout churners. This is a single split and not an intervention or uplift estimate.

## Group audit and limits

Age-group rates are descriptive only. Holdout groups 1 and 5 have 26 and 42 records and no positive outcomes, so their TPR estimates are not informative. Do not use this as a fairness certification, automated customer action, or evidence that an outreach campaign works. Validate calibration and contact policy on newer, representative data and a randomized intervention before deployment.

Aggregate metrics, split details, and the input SHA-256 are in [`reports/benchmark.json`](reports/benchmark.json).
