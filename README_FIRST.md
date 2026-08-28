# START HERE — Research Operating Pack

This package is the source-of-truth bundle for the project **From Representation to Response Policy: paired Base→post-training mechanisms for PRC-sensitive behavior in open-weight LLMs**.

## Use the files in this order

1. **00_master_research_blueprint.md** — complete scientific plan, novelty boundary, hypotheses, dataset, causal methods, statistics, decision tree, timeline, reviewer attacks, ethics and venue branches.
2. **01_coding_agent_handoff.md** — direct implementation/run-order contract for a coding agent.
3. **02_implementation_spec.yaml** — machine-readable project configuration and decision logic.
4. **03_experiment_tracker.json** — GitHub-native status/dependency/gate/venue tracker export.
5. **05_annotation_rubric.md** — response-label definitions and human-validation protocol.
6. **06_preregistration_template.md** — freeze this before confirmatory test-set generation/interventions.
7. **07_ai_use_log_template.csv** — record every substantive generative-AI use from ideation through submission.
8. **schemas/** — JSON Schemas for prompts, annotations and run manifests.
9. **04_references_seed.bib** — verified starter references; independently verify final metadata before publication.

## First execution sequence

- Assign an owner and compute environment in the tracker.
- Implement **E001 Qwen3 smoke adapter** and **E002 Llama smoke adapter**.
- Build human-reviewed dataset v0.1 under **E010**.
- Run Qwen3 Base/Post behavioral pilot **E020**.
- Make Gate **G1** decision before large activation caching.
- Do not add GLM-4 until the three core families are functioning.

## Core scientific invariant

The project is not asking whether a model merely *contains information about* a sensitive topic. It asks whether post-training changes the **causal connection** from that representation to response policy.

The central pattern of interest is:

```text
Decodability(Base) ≈ Decodability(Post)
while
|CausalPolicyEffect(Base)| << |CausalPolicyEffect(Post)|
```

Other outcomes have explicit pivots in the master plan and YAML. Do not force the preferred hypothesis.

## Ordered dual-venue strategy

- **One canonical scientific paper/results package.** Do not run separate FAccT and COLM projects.
- **First submission:** FAccT 2027, if the scientific/venue gates are met.
- **Fallback/revision submission:** COLM 2027 only if the work is no longer under review at or committed to FAccT and the COLM 2027 rules permit submission.
- If archival FAccT accepts the paper, the same/substantially similar paper does **not** go to COLM. A later COLM paper must be materially distinct.
- Experiments, result tables, hypotheses, and core causal claims stay identical. Venue-specific changes are framing, page compression, emphasis, ethics/context, and supplementary organization.
- FAccT 2027: abstract 2026-10-27; paper 2026-11-03; first decision 2026-12-22; final decision 2027-03-23; 14-page main-text limit.
- COLM 2027: CFP not yet confirmed. COLM 2026 used a 9-page main-text limit and prohibited double submission; these are planning assumptions only.

## Publication-policy warning

As of 2026-08-28, the FAccT 2027 Author Guide prohibits LLM-generated publication text and requires a Generative AI Usage Statement. These planning artifacts are **not manuscript prose**. Authors must draft any FAccT paper themselves and disclose allowed AI assistance. Verify COLM 2027 rules when its CFP is released.
