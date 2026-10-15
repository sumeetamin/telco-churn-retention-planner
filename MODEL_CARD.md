# Model card: customer churn baseline

## Purpose
Predict a binary churn label from historical customer data, measure holdout discrimination, and rank a bounded outreach list.

## Intended use
Portfolio demonstration and controlled, randomized retention experiments. Use only pre-contact customer features and authorized data.

## Not intended for
Automatic cancellations, pricing, eligibility decisions, or claims that contacting a person will prevent churn.

## Method and evaluation
The training CLI uses an imputed/scaled one-hot logistic regression baseline, stratified random holdout and ROC-AUC, average precision, Brier score, and optional subgroup error rates. The selected threshold and feature schema are saved. The scoring CLI requires the same features and ranks the highest-risk share.

## Limits
A churn probability is not incremental treatment effect. Run a randomized experiment to estimate intervention benefit, preserve an untouched holdout, review segment-level errors, and account for contact fatigue and customer consent. Historical labels may contain selection bias and policy artifacts.
