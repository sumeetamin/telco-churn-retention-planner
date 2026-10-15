# Telco Churn Retention Planner

A churn probability model that produces a capacity-limited outreach queue and holdout metrics.

> **Portfolio prototype.** Code is provided; no benchmark results are claimed until you run it on the cited data and record the output.

## Use case

A churn probability model that produces a capacity-limited outreach queue and holdout metrics. The command below reads a local data export, applies a transparent baseline, writes holdout or decision-support outputs, and saves the fitted model where applicable.

## Data and provenance

[UCI Iranian Churn Dataset](https://archive.ics.uci.edu/dataset/563/iranian+churn+dataset). A CSV with one customer per row and a binary churn label. Pass its exact label column name with `--target`; optionally supply a segment with `--group`. Dataset files are not bundled. Respect the source terms and cite the dataset when publishing results.

## Quick start

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
# Download/prepare the source data locally, then run:
python main.py --input data/churn.csv --target Churn --positive-label 1 --group Sex --contact-share 0.10
```

## Outputs

The `outputs/` directory contains the model-specific results (metrics and/or ranked CSV) and a serialized estimator where applicable. Outputs are reproducible with the same input, package versions, and random seed. The repository intentionally excludes downloaded data and generated artifacts.

## Evaluation and operating notes

A predicted churn probability is not a treatment effect. Contacting high-risk customers may not reduce churn; run a randomized campaign and measure incremental retention before claiming value.

For a production review, preserve a time-based, untouched holdout; compare against a simple business baseline; inspect calibration and subgroup error; document data lineage; and monitor drift. The included baseline is not a production service.

## License

Code: MIT. Third-party datasets remain subject to their original terms.
