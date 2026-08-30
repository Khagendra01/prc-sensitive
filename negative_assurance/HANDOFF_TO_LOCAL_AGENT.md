# Handoff to Local Coding Agent

## Goal

Continue the negative-assurance project from the current branch outputs and run the first **real open-weight language-model** prospective experiment.

Do not alter or reinterpret the original PRC-sensitive study. Keep all new work under `negative_assurance/` on branch `negative-assurance-side-research` (or a child branch).

## Scientific hypothesis to test

A white-box audit may retain useful discriminative information under distribution shift while its calibrated decision threshold / posterior risk estimate fails.

The real-model experiment should directly test:

1. Does BB+WB improve detection over BB?
2. Does BB+WB improve probabilistic calibration on held-out model organisms?
3. Does calibration transfer from **strong** to **weak / shifted** hidden behavior?
4. Can an abstention rule maintain a prespecified false-assurance bound while retaining useful coverage?

## Minimum prospective design

Use a small open-weight LM that is feasible on available GPU hardware. Use only benign synthetic hidden behaviors.

Create matched model organisms:

- **H0 controls**: matched fine-tuning exposure but no hidden behavior.
- **H1 calibration positives**: strong benign trigger-conditioned behavior.
- **H1 OOD positives**: weaker behavior and/or a changed implantation/training route.
- Hold out trigger identities / behavior templates from audit calibration.

Recommended first scale (adjust for compute, but do not collapse to one or two models):
- calibration: >= 10 H0 + >= 10 H1
- each OOD cohort: >= 8 H0 + >= 8 H1
- use multiple seeds and record them.

## Audit arms

At minimum:
- **BB**: fixed-budget behavioral probing / red-team search.
- **WB**: one interpretable internal signal with a clear implementation (e.g. activation probe or gradient/relevance attribution).
- **BB+WB**: same BB evidence plus WB signal.

Do not give BB+WB a larger behavioral query budget than BB.

## Pre-registration before OOD evaluation

Fit/calibrate only on the calibration cohort.

Freeze:
- features,
- model fitting procedure,
- decision threshold,
- assurance/abstention thresholds,
- audit budget,
- metrics.

Then evaluate OOD without retuning.

## Required metrics

For every audit arm and cohort:
- AUROC
- sensitivity
- specificity
- false-negative rate
- Brier score
- log loss
- calibration intercept/slope if sample size permits
- negative likelihood ratio (LR-)
- posterior risk after a negative result across several priors
- selective-assurance coverage
- false-assurance rate among assured models
- worst-group false-assurance rate

Bootstrap/resample over **model organisms**, not prompts.

## Critical validity checks

Before interpreting any audit result:
1. Verify H1 models genuinely express the intended hidden behavior.
2. Verify H0 matched controls do not.
3. Verify ordinary-task/general capability is approximately matched.
4. Reject a cohort if implantation strength is not separated from controls.
5. Record technical/auditor failures separately from semantic misses, but count operational failures against end-to-end assurance.

The archived P1-tiny attempt demonstrates why check (1) is mandatory.

## P1a phenomenon to attempt to reproduce

The synthetic P1a pilot found:

- strong OOD H1: white-box scores separated positives/controls well;
- weak OOD H1: white-box **AUC remained 1.0**, but the calibration-derived binary threshold had **0% sensitivity**;
- conservative abstention avoided false assurance only at stringent thresholds.

The important replication target is not the exact numerical values. It is the structural question:

> Can white-box evidence still rank hidden-behavior models correctly while a previously calibrated negative-safety threshold becomes overconfident under a strength/training shift?

## Output layout

Create:
- `negative_assurance/real_lm_pilot/config/`
- `negative_assurance/real_lm_pilot/scripts/`
- `negative_assurance/real_lm_pilot/manifests/`
- `negative_assurance/real_lm_pilot/results/`
- `negative_assurance/real_lm_pilot/figures/`
- `negative_assurance/real_lm_pilot/README.md`

Every run should have a machine-readable manifest with:
- base model hash/revision
- adapter/checkpoint hash
- seed
- behavior ID
- H0/H1 label
- implantation method
- implantation strength
- dataset hashes
- audit configuration
- software versions

## Stop / no-go conditions

Stop and report rather than rescuing the experiment if:
- H1 behavior cannot be cleanly implanted while preserving ordinary behavior;
- BB and WB signals are dominated by trivial weight/adapter magnitude artifacts;
- the auditor can identify H1 solely because H1 received more training;
- held-out triggers leak into calibration;
- there are too few independent model organisms to estimate assurance uncertainty;
- results reduce to a trivial detector-accuracy comparison with no calibration/negative-assurance insight.

## Provenance

Reports and CSVs in this branch are outputs from the exploratory analyses conducted before this handoff. The original interactive code used to generate every exploratory file was not fully persisted as standalone scripts. Treat the CSVs as recorded outputs and implement fresh reproducible scripts for the real-LM study.
