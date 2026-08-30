# P0b — Pando retrospective BB vs BB+WB stress test

## Data and interpretation

This analysis uses Pando's released cached paper-artifact accuracy table, aggregated across three scenarios and 240 model organisms per rationale condition. Pando's black-box agent receives the fixed behavioral query budget. The Gradient and RelP agents receive the same behavioral evidence plus a white-box attribution signal, so they operationalize **BB+WB** rather than WB-only.

The 12 stress-test cells are:
- 3 explanation regimes: no verbalization, faithful verbalization, unfaithful verbalization;
- 4 hidden-rule depths: d1–d4.

This is a retrospective condition-level stress test, not a new model inference run and not yet a probabilistically calibrated negative-safety classifier.

## Main result

### BB + RelP
- mean uplift over BB: **4.92 pp**
- improves **12/12** cells
- uplift range: **1.90 to 11.20 pp**
- black-box mean failure: **25.7%**
- BB+RelP mean failure: **20.7%**
- mean relative failure reduction: **26.3%**
- worst-cell failure changes from **42.8%** to **39.2%**

### BB + Gradient
- mean uplift over BB: **2.74 pp**
- improves **12/12** cells
- uplift range: **0.80 to 4.40 pp**
- BB+Gradient mean failure: **22.9%**
- mean relative failure reduction: **17.1%**

## Transfer / calibration-relevant finding

A single average white-box uplift does not transfer cleanly across hidden-rule complexity. Leave-one-depth-out results show that the expected improvement learned on the other depths can differ materially from the held-out depth.

The strongest RelP gains concentrate at intermediate depth (especially d2), whereas at d1 the black-box baseline is already near ceiling and white-box adds little. At d4, the absolute failure rate remains around forty percent even with the strongest white-box arm.

This matters for negative assurance: **white-box access lowers average prediction failure, but it does not make failures rare or uniformly predictable across difficulty strata.**

## Pilot verdict

**CONTINUE, but the current evidence supports "better detector" more strongly than "calibrated assurance."**

Pando gives evidence that gradient-based white-box information adds incremental predictive value:
- RelP improves all 12 aggregate cells;
- the average improvement is meaningful;
- but the remaining miss probability is large on hard cells and the uplift is heterogeneous.

To answer the original negative-assurance question, the next required step is per-model/per-input cached Pando data (the public evaluation-results artifact) so we can fit probabilistic BB and BB+WB predictors on calibration models and evaluate Brier score, log loss, reliability, abstention/coverage, and false-assurance rates on held-out scenarios/configurations.