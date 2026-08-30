# P0a — Retrospective Negative-Assurance Sanity Check

## What was actually run

This is a **local statistical re-analysis** of six publicly released, per-run judged AuditBench-transfer outcomes for the baseline auditor. It is not a rerun of the 70B AuditBench auditing agents.

For each hidden behavior, the release contains 16 judged investigator attempts. We extracted:
- successful detections,
- explicit judge/API failures,
- and ordinary misses.

For a fixed audit budget of **K=4**, the main descriptive statistic is the exact probability that a uniformly selected four-run subset of the 16 released attempts contains **zero successful detections**:

`C(16-s, 4) / C(16, 4)`

where `s` is the number of successful detections among the 16 released attempts.

## Main result

Across the six behaviors, the end-to-end probability that a four-attempt audit block is completely negative ranged from:

- **18.1%** to **100.0%**
- mean: **64.6%**
- quirk-bootstrap 95% interval for the mean: **40.6%–88.3%**

A simple leave-one-behavior-out pooled calibration was poor:

- mean absolute error: **32.0%**
- RMSE: **36.4%**

In other words, knowing the baseline auditor's average detection rate on the other behaviors was not enough to predict how reassuring a negative four-run audit should be on a new behavior.

## Operational-failure finding

Three of the six released JSONs contain many explicit judge/API failures. Those failures are correctly counted as end-to-end audit failures for an operational assurance claim, but they should not be confused with semantic failures of the investigator.

The three behaviors without any such recorded technical failures still had highly variable four-run negative probabilities:

- `ai_welfare_poisoning`: 75.0%
- `hallucinates_citations`: 39.3%
- `secret_loyalty`: 100.0%

Mean across these three clean behaviors: **71.4%**.

This means the heterogeneity is not *only* an artifact of the judge/API failures, although the sample is far too small for a paper-level conclusion.

## Interpretation

This P0a supports continuing the assurance-calibration question because the naive assumption

> "an audit that works at rate p on some hidden behaviors gives similarly reassuring negative evidence on a new hidden behavior"

fails badly in this small released slice.

However, this is **not yet the planned P0**:
- all examples here are positive hidden-behavior models (`H=1`), so specificity, LR-, and NPV cannot be estimated;
- this release is a KTO transfer benchmark and does not provide the original AuditBench white-box-vs-black-box training-method matrix in a directly committed per-run table;
- there are only six behavior categories here;
- several rows contain technical judge failures;
- therefore this result is a feasibility/sanity check, not evidence for the final scientific claim.

## Pilot decision

**P0a verdict: CONTINUE, but do not claim success.**

The next evidentiary threshold is a released or newly generated dataset with:
1. multiple audit modalities (black-box and white-box),
2. multiple implantation/training methods,
3. held-out behavior classes,
4. and eventually matched negative controls (`H=0`).

Only then can the proposed negative-assurance claim be tested properly.