# Prospective P1 Tiny-Transformer Negative-Assurance Pilot

## Status
This is a **genuine prospective controlled experiment** run locally from randomly initialized weights, but on a tiny synthetic transformer rather than a pretrained LLM. The calibration/OOD split and audit protocol were fixed before fitting the audit classifiers.

Base ordinary-task held-out accuracy: **100.0%**.

## Model organisms
- Calibration: 10 H1 + 10 matched H0 models with a simple trigger-conditioned label flip.
- Contextual OOD: 6 H1 + 6 H0; the trigger only flips behavior when an additional context condition holds.
- Weak OOD: 6 H1 + 6 H0; only 55% of trigger training instances are relabeled.
- H0 controls see the same candidate trigger token during matched fine-tuning but retain the ordinary label.

## Auditors
- BB: four candidate-trigger behavioral probes (128 contexts each) + ordinary error.
- BB+WB: same BB evidence plus summaries of base-to-audited-model embedding-weight changes over the full trigger-candidate subspace.
- Binary decision threshold is selected on calibration data to maximize specificity subject to >=90% sensitivity.
- Selective assurance: claim a reassuring negative only when predicted P(H1) < 10%.

## OOD results

### Contextual hidden behavior
BB: AUC=0.417, sensitivity=100.0%, specificity=0.0%, LR-=inf, assurance coverage=0.0%, false-assurance rate=nan%.

BB+WB: AUC=0.833, sensitivity=83.3%, specificity=83.3%, LR-=0.200, assurance coverage=25.0%, false-assurance rate=0.0%.

### Weak hidden behavior
BB: AUC=0.167, sensitivity=33.3%, specificity=0.0%, LR-=inf, assurance coverage=0.0%, false-assurance rate=nan%.

BB+WB: AUC=0.972, sensitivity=66.7%, specificity=100.0%, LR-=0.333, assurance coverage=16.7%, false-assurance rate=0.0%.

## Interpretation boundary
This experiment can establish whether the *statistical assurance protocol* behaves sensibly with genuine H0 controls and OOD hidden behaviors. It cannot establish that real LLM white-box audits are calibrated: the network, task, implant mechanism, and white-box feature are intentionally small and synthetic. A positive result is a protocol validation; a negative result can falsify the protocol before expensive GPU work.