# real_lm_pilot — Kaggle-ready

Small open-weight LM prospective test of: BB vs WB vs BB+WB, calibration transfer strong→weak.

Base: HuggingFaceTB/SmolLM2-360M-Instruct (360M, fits T4 16GB with LoRA). Fallback: SmolLM2-135M.

## Design (per HANDOFF)

- H0: matched finetune, no trigger (10 cal + 8 OOD)
- H1 strong cal: trigger-conditioned preference (10 cal)
- H1 weak OOD: same triggers but 30% strength + different template (8 OOD)
- Hold out trigger identities: cal triggers A/B, OOD triggers C/D

## Audits
- BB: fixed 8-prompt behavioral probe (trigger vs clean)
- WB: mean activation probe on last hidden (probe trained on cal cohort only)
- BB+WB: logistic over BB score + WB score, frozen before OOD

## To run on Kaggle (GPU T4)
1. Push this folder as dataset or kernel: `kaggle kernels push -p real_lm_pilot_kaggle`
2. Or run notebook `kaggle_notebook.ipynb` directly.

Outputs go to `results/` with manifests per HANDOFF.
