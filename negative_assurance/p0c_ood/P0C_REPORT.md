# P0c — OOD Negative-Assurance Transfer Test

## Question

If an audit method has an empirically low failure rate in one distribution, does that failure rate remain calibrated after a distribution shift? And does adding white-box RelP evidence improve **selective negative assurance**, not just mean accuracy?

## Data

This analysis uses only committed Pando paper artifacts with **held-out accuracy**:
1. **Training-data shift:** car-purchase/freeform/no-verbalization models calibrated on standard training and tested after 25% Dolci or FineWeb data mixing, depths d1–d3.
2. **Input-format shift:** car-purchase models calibrated on freeform inputs and tested on natural or structured input formats, across no/faithful/unfaithful verbalization regimes.

For every matched stratum, the in-distribution failure rate is treated as the predicted OOD audit-failure risk. The target distribution's held-out failure rate is the observed risk.

This is a **group-level calibration experiment**, not a per-model probability model.

## Aggregate calibration

Black-box:
- mean predicted failure: **23.5%**
- mean observed OOD failure: **22.9%**
- MAE calibration: **3.1%**
- RMSE calibration: **4.3%**
- maximum cell error: **10.7%**

BB + RelP:
- mean predicted failure: **16.9%**
- mean observed OOD failure: **18.4%**
- MAE calibration: **2.4%**
- RMSE calibration: **2.8%**
- maximum cell error: **5.7%**

Paired target-cell difference in absolute calibration error (RelP - BB):
- mean: **-0.7%**
- target-cell bootstrap 95% interval: **[-2.4%, +0.8%]**

Paired difference in actual OOD failure (RelP - BB):
- mean: **-4.5%**
- bootstrap 95% interval: **[-6.6%, -2.7%]**

## Selective assurance

An auditor is allowed to say "negative result is reassuring" only when its calibrated source failure risk is below a threshold; otherwise it abstains.

shift_family    agent  risk_threshold  coverage_cells  coverage_fraction  predicted_failure_mean_assured  observed_failure_mean_assured  worst_observed_failure_assured  false_assurance_gap
         all blackbox            0.10               2           0.166667                          0.0130                         0.0710                           0.120              -0.0290
         all blackbox            0.15               2           0.166667                          0.0130                         0.0710                           0.120              -0.0790
         all blackbox            0.20               2           0.166667                          0.0130                         0.0710                           0.120              -0.1290
         all blackbox            0.25               4           0.333333                          0.1250                         0.1240                           0.191              -0.1260
         all     relp            0.10               4           0.333333                          0.0475                         0.0570                           0.084              -0.0430
         all     relp            0.15               4           0.333333                          0.0475                         0.0570                           0.084              -0.0930
         all     relp            0.20               6           0.500000                          0.0960                         0.1160                           0.236              -0.0840
         all     relp            0.25              10           0.833333                          0.1474                         0.1638                           0.244              -0.0862

The important quantities are:
- coverage: how often the method is willing to provide assurance;
- actual OOD failure among those assured cells;
- worst OOD failure among assured cells.

## Interpretation

This stress test separates two claims:
1. **Detection benefit:** RelP lowers OOD error compared with black-box.
2. **Assurance calibration:** source-measured risk accurately predicts target risk.

The results show whether white-box evidence improves one, both, or neither under two concrete distribution shifts.

Because the inputs are aggregate Pando cells rather than per-model confidences, this is a strong P0c screening test but not the final per-model assurance experiment.