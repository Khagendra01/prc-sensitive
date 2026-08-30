#!/usr/bin/env python3
"""Regenerate the four exploratory figures from committed CSV artifacts.

These plots are derived artifacts. The original PNG byte hashes are recorded in
FIGURE_CHECKSUMS.md. Because the ChatGPT GitHub connector used for the handoff
accepts UTF-8 writes only, the original PNG binaries were not directly uploaded.
Run this after cloning to recreate the figures, then commit them normally.
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent

# P0a
df = pd.read_csv(ROOT / "p0a" / "p0a_extracted_counts_and_metrics.csv")
fig, ax = plt.subplots(figsize=(10, 5.5))
ax.bar(df["quirk"], df["P_negative_fixed_budget_K4_end_to_end"])
ax.set_ylabel("Probability a 4-run audit block is negative")
ax.set_xlabel("Held-out behavior / quirk")
ax.set_ylim(0, 1.05)
ax.set_title("P0a: fixed-budget negative-audit probability from released runs")
ax.tick_params(axis="x", rotation=35)
fig.tight_layout()
fig.savefig(ROOT / "p0a" / "p0a_negative_probability_by_quirk.png", dpi=180)
plt.close(fig)

# P0b
df = pd.read_csv(ROOT / "p0b_pando" / "p0b_cell_level_results.csv")
labels = [f"{r.condition}-d{r.depth}" for _, r in df.iterrows()]
x = range(len(labels))
width = 0.36
fig, ax = plt.subplots(figsize=(11, 5.8))
xx = list(x)
ax.bar([v-width/2 for v in xx], df["relp_uplift_pp"], width, label="BB + RelP vs BB")
ax.bar([v+width/2 for v in xx], df["gradient_uplift_pp"], width, label="BB + Gradient vs BB")
ax.axhline(0, linewidth=1)
ax.set_ylabel("Accuracy uplift over black-box (percentage points)")
ax.set_xlabel("Held-out condition cell")
ax.set_xticks(xx)
ax.set_xticklabels(labels, rotation=45, ha="right")
ax.set_title("P0b: incremental value of white-box evidence varies by condition")
ax.legend()
fig.tight_layout()
fig.savefig(ROOT / "p0b_pando" / "p0b_whitebox_uplift_by_condition.png", dpi=180)
plt.close(fig)

# P0c
df = pd.read_csv(ROOT / "p0c_ood" / "p0c_ood_cell_results.csv")
fig, ax = plt.subplots(figsize=(7.5, 6.2))
for agent, marker in [("blackbox", "o"), ("relp", "s")]:
    sub = df[df.agent == agent]
    ax.scatter(sub.predicted_failure, sub.observed_failure, label=agent, marker=marker)
ax.plot([0, 0.45], [0, 0.45], linestyle="--")
ax.set_xlim(0, 0.45)
ax.set_ylim(0, 0.45)
ax.set_xlabel("Predicted OOD failure from in-distribution calibration")
ax.set_ylabel("Observed OOD failure")
ax.set_title("P0c: Does negative-audit risk transfer under distribution shift?")
ax.legend()
fig.tight_layout()
fig.savefig(ROOT / "p0c_ood" / "p0c_predicted_vs_observed_failure.png", dpi=180)
plt.close(fig)

# P1a
df = pd.read_csv(ROOT / "p1a_prospective" / "selective_assurance_curve.csv")
fig, ax = plt.subplots(figsize=(9.5, 5.8))
for (split, auditor), sub in df.groupby(["split", "auditor"]):
    ax.plot(sub["coverage"], sub["false_assurance_rate"], marker="o",
            label=f"{split} / {auditor}")
ax.set_xlabel("Assurance coverage")
ax.set_ylabel("False-assurance rate")
ax.set_title("P1a: selective-assurance coverage vs false assurance")
ax.set_ylim(bottom=0)
ax.legend(fontsize=8)
fig.tight_layout()
fig.savefig(ROOT / "p1a_prospective" / "selective_assurance.png", dpi=180)
plt.close(fig)

print("Regenerated four figures.")
