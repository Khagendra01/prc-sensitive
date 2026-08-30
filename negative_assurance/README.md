# Negative-Assurance Side Research

This directory is an **independent side-research track** created on branch `negative-assurance-side-research`. It does not replace or reinterpret the original PRC-sensitive project on `main`.

## Current research question

**When does absence of white-box/mechanistic evidence become calibrated evidence of absence?**

Operationally: can an auditor turn a negative result into a quantitatively trustworthy reduction in risk, especially under distribution shift? The key distinction is between:

- **detection/discrimination**: can the audit rank or detect positive hidden-behavior models?
- **negative assurance/calibration**: after the audit is negative, how much should belief in the hidden behavior actually fall?
- **selective assurance**: can the auditor abstain when its negative result is not trustworthy?

## Artifact status

### `p0a/` — retrospective AuditBench-transfer sanity check
Status: **valid screening analysis; small and limited**

Main finding: fixed-budget negative-audit probability varied dramatically across hidden behaviors, and naive leave-one-behavior-out calibration was poor.

### `p0b_pando/` — retrospective BB vs BB+WB
Status: **valid aggregate stress test**

Main finding: RelP/gradient white-box evidence improved average prediction over black-box, but improvement was heterogeneous and hard conditions retained large miss rates.

### `p0c_ood/` — OOD group-level assurance transfer
Status: **valid screening analysis; group-level, not per-model calibration**

Main finding: RelP lowered OOD failure and descriptively improved aggregate calibration under data-mixing and format shifts, but selective-assurance safety depended strongly on the risk threshold.

### `p1a_prospective/` — prospective controlled model-organism pilot
Status: **valid protocol-validation experiment; synthetic neural model, not an LLM**

Main finding: a white-box auditor could have perfect OOD ranking (AUC 1.0) while a threshold calibrated on strong hidden behaviors missed every weak positive. This is the clearest current demonstration that **discrimination is not assurance calibration**.

### `archive/invalid_p1_tiny/`
Status: **INVALID FOR SCIENTIFIC INFERENCE**

The first tiny-transformer prospective attempt did not implant the hidden behavior strongly enough. It is retained only for provenance and debugging. Do not use its attractive audit metrics as evidence.

## What has NOT been established

Nothing in this branch establishes that a real LLM is safe, that mechanistic interpretability can certify absence of dangerous behavior, or that the synthetic P1a effect will replicate in pretrained language models.

The next decisive step is a small real open-weight LM experiment with matched H0/H1 model organisms and a preregistered calibration/OOD split.

See `HANDOFF_TO_LOCAL_AGENT.md`.
