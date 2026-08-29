# PRC-Sensitive LLM Post-Training Mechanisms

Research repository for **From Representation to Response Policy: paired Base→post-training mechanisms for PRC-sensitive behavior in open-weight LLMs**.

The project studies whether post-training changes the **causal connection** between representations of PRC-sensitive political topics and model response policy, and whether that transition replicates across independently developed Chinese open-weight model families.

## Core design

Primary within-family comparisons:

- Qwen3 Base → post-trained
- DeepSeek LLM Base → Chat
- Yi-1.5 Base → Chat

External control:

- Llama 3.1 Base → Instruct

Optional replication after the core panel:

- GLM-4 Base → Chat

The central mechanistic distinction is:

```text
Decodability(Base) ≈ Decodability(Post)
while
|CausalPolicyEffect(Base)| << |CausalPolicyEffect(Post)|
```

This is a hypothesis, **not an assumed conclusion**. Null and alternative-result branches are defined in the research blueprint and implementation spec.

## Start here

1. [README_FIRST.md](README_FIRST.md) — operating-pack orientation.
2. [00_master_research_blueprint.md](00_master_research_blueprint.md) — complete scientific protocol.
3. [01_coding_agent_handoff.md](01_coding_agent_handoff.md) — implementation contract and execution order.
4. [02_implementation_spec.yaml](02_implementation_spec.yaml) — machine-readable experiment specification.
5. [03_experiment_tracker.json](03_experiment_tracker.json) — live experiment/gate/venue tracker.
6. [05_annotation_rubric.md](05_annotation_rubric.md) — response annotation protocol.
7. [06_preregistration_template.md](06_preregistration_template.md) — confirmatory-study freeze template.
8. [08_dual_venue_strategy.md](08_dual_venue_strategy.md) — ordered FAccT → COLM publication strategy.
9. [09_publication_strength_and_risks.md](09_publication_strength_and_risks.md) — publication-strength gate, residual reviewer risks, and stretch generalization criteria.
10. [schemas/](schemas/) — schemas for prompts, annotations, and run manifests.

## Execution order

The coding implementation should follow the experiment IDs and gates defined in the handoff/spec.

Initial path:

```text
E001 Qwen3 smoke adapter
E002 Llama smoke adapter
        ↓
E010 dataset v0.1
        ↓
E020 Qwen3 Base/Post behavioral pilot
        ↓
G1 behavioral gate
        ↓
activation caching → probes → causal interventions
        ↓
cross-family replication + external control
        ↓
sealed confirmatory test
```

Do not begin expensive full-panel activation caching before the corresponding gates pass.

## Scientific rules

- Topic groups, not paraphrases, are the generalization unit.
- A linear probe is evidence of decodability, **not causal use**.
- Mechanistic claims require interventions such as activation addition/ablation/patching.
- Separate PRC-sensitive routing from generic harmful-content refusal.
- Keep hard refusal, evasion, factual coverage, omission, unsupported claims, and official-position agreement as distinct behavioral measurements.
- Do not describe a latent direction as a "propaganda neuron" or infer developer/government intent from model internals.
- Keep negative and null results.
- Never choose layers, alphas, or hypotheses using the sealed confirmatory test topics.

## Publication strategy

This is **one canonical scientific project**, not separate FAccT and COLM projects.

- First target: **FAccT 2027**, if scientific and venue gates pass.
- Planned fallback/revision route: **COLM 2027** only if the work is no longer under review at or committed to FAccT and COLM 2027 rules permit submission.
- If archival FAccT accepts the paper, the same or substantially similar paper does not subsequently go to COLM.
- The experimental core, frozen result tables, primary analyses, and claim boundaries stay the same across venue packaging.

See [08_dual_venue_strategy.md](08_dual_venue_strategy.md) for the state machine.

## Reproducibility

Every run should record:

- exact model and tokenizer revision
- code commit
- prompt-set hash
- random seeds
- generation configuration
- hardware/software environment
- intervention layer/direction/strength
- dataset split
- output paths and checksums

Do not overwrite run directories.

## Current state

Planning/protocol package initialized on **2026-08-28**. Experimental implementation has not yet been claimed as complete.

