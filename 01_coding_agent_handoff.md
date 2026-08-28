# Coding Agent Handoff — PRC-Sensitive Post-Training Mechanisms

**Status date:** 2026-08-28  
**Ordered venue strategy:** FAccT 2027 first; COLM 2027 fallback/revision route if the work remains eligible (CFP not yet confirmed)  
**Machine-readable source of truth:** `02_implementation_spec.yaml`  
**Progress / experiment registry:** `03_experiment_tracker.xlsx`

> **Important publication-policy note:** The current FAccT 2027 Author Guide prohibits using LLMs to generate publication text. This file is a research/engineering planning artifact, not manuscript prose. Do not paste it into a FAccT submission. Maintain an AI-use log and verify the final COLM 2027 policy when released.

## 1. Research contract

The project tests whether **post-training changes the causal mapping from PRC-sensitive semantic representations to response policy** across multiple independently developed Chinese open-weight model families. It must not start from the assumption that a model contains “propaganda.” Refusal, evasion, omission, factual error, and agreement with official PRC positions are separate dependent variables.

### Non-negotiable non-claims

- Never label a direction/neuron “propaganda” based only on probe or steering behavior.
- Never infer intent of developers, regulators, or governments from weights.
- Never generalize from the sampled families to all Chinese models.
- Never treat a high probe AUROC as causal localization.
- Never compare raw layer numbers across architectures; use normalized depth plus within-model layer IDs.
- Never pick the best layer on the final test topics.

## 2. Core model panel

| Family | Base | Post-trained | Role |
|---|---|---|---|
| Qwen3 | `Qwen/Qwen3-8B-Base` | `Qwen/Qwen3-8B` with thinking disabled for primary runs | Core #1; paired extension of prior Qwen findings |
| DeepSeek LLM | `deepseek-ai/deepseek-llm-7b-base` | `deepseek-ai/deepseek-llm-7b-chat` | Core #2; clean official Base→Chat relation |
| Yi-1.5 | `01-ai/Yi-1.5-9B` | `01-ai/Yi-1.5-9B-Chat` | Core #3 |
| Llama 3.1 | `meta-llama/Llama-3.1-8B` | `meta-llama/Llama-3.1-8B-Instruct` | External control only |
| GLM-4 | `zai-org/glm-4-9b` | `zai-org/glm-4-9b-chat-hf` | Optional P1 replication after core panel works |

## 3. Repository skeleton

```text
repo/
  README.md
  pyproject.toml
  uv.lock or requirements.lock
  configs/
    models/
    datasets/
    experiments/
  data/
    raw/                 # immutable human-authored source prompts
    processed/           # versioned, hashed datasets
    annotations/         # human and automatic labels
  src/
    models/              # adapters, chat serialization, hook names
    data/                # validation, matching, topic-group splits
    generate/            # behavior inference
    activations/         # residual/component caches
    probes/              # linear probes/directions
    steering/            # addition, ablation, direction transfer
    eval/                # refusal/evasion/coverage/framing metrics
    stats/               # CIs, hierarchical models, tests
    figures/             # deterministic plots from result tables
  tests/
  runs/                   # immutable run manifests; gitignored bulky tensors
  results/
    tables/
    figures/
    prereg/
```

## 4. Build order — do not skip ahead

### Phase 0 — environment and adapters

**Deliverable:** every P0 model loads, generates 32 tokens, returns residual stream activations from every block, and records model/tokenizer revisions.

Required tests:
1. `test_model_load_<family>`
2. `test_tokenizer_roundtrip_<family>`
3. `test_hook_shapes_<family>`
4. `test_base_and_post_share_expected_dimensions_<family>`
5. `test_qwen3_thinking_disabled`

**Gate G0:** if a family cannot expose reliable hooks after a bounded engineering effort, replace that family rather than redesigning the whole pipeline.

### Phase 1 — behavioral dataset and baseline

Build a versioned bilingual dataset with topic-group splits. Target at least:
- 18 PRC-sensitive topics × 4 templates × 2 languages = 144 prompts.
- 18 matched non-PRC political topics × 4 × 2 = 144.
- 10 neutral-China topics × 4 × 2 = 80.
- 10 general-political topics × 4 × 2 = 80.
- Separate generic harmful/harmless subset for refusal-direction controls.

Minimum core political set = **448 prompts** before safety controls and robustness paraphrases.

Each prompt record must contain:

```json
{
  "prompt_id": "prc_tiananmen_factual_zh_01",
  "topic_id": "tiananmen_1989",
  "stratum": "prc_sensitive",
  "language": "zh-Hans",
  "template_id": "direct_factual",
  "matched_topic_id": "...",
  "prompt_text": "...",
  "author_source": "human",
  "dataset_version": "v0.1"
}
```

**Do not split at prompt level. Split at topic level.** Paraphrases and translations of a topic stay in one split.

Behavior tracks:
- **Ecological track:** official chat template for post-trained model; fixed `Question: ...
Answer:` completion format for Base.
- **Matched representation track:** identical serialized plain text fed to both Base and post-trained checkpoints to isolate weight differences.

Output schema must retain raw text, tokens, exact generation config, seed, model revision, prompt dataset hash, and run ID.

### Phase 2 — annotation and behavioral effects

Never collapse everything into “censorship.” Score separately:
- hard refusal (binary)
- evasion (0–2)
- directness (0–2)
- factual coverage (0–1 or checklist proportion)
- omissions (count / checklist misses)
- agreement with a curated official-PRC proposition set (ordinal)
- unsupported factual claims
- coherence
- response length

Automatic evaluation can assist, but final validity requires blinded human adjudication of a stratified sample and all important judge disagreements. The model under test must never judge itself.

**Gate G1:** if the Base→post-trained behavioral effect is weak across all three core families, test language/template robustness before spending heavily on activation work. A persistent null is a result, but the mechanistic scope should be reduced.

### Phase 3 — activation cache and probes

Primary cache: **last prompt-token residual vector at every layer**, float16 on disk. Do not cache all tokens for all prompts.

For each layer `l`:

```text
v_sensitive(l) = mean(h_l | PRC-sensitive) - mean(h_l | matched political control)
```

Also fit an L2 logistic probe using training topics only. Evaluate on held-out topics with AUROC/AUPRC/balanced accuracy.

Mandatory lexical leakage controls:
- entity-masked prompt variant
- topic-name removed/abstracted variant
- neutral-China controls
- matched non-PRC sensitive events

Estimate separately:

```text
v_refusal(l)  = harmful/refusal contrast
v_policy(l)   = direction predicting annotated refusal/evasion/omission behavior
```

Report cosine similarity and projection overlap, but do not treat low cosine as proof of functional independence.

**Gate G2:** a linear probe must generalize across held-out topics before using its direction for the primary steering claim. If it fails, nonlinear probes are diagnostic only; escalate to SAE/crosscoder on a narrow subset rather than declaring the concept absent.

### Phase 4 — causal steering / ablation

Use development topics to select candidate layers. Never tune alpha or layer on the final test set.

Normalize each direction and scale intervention by median residual norm at that layer. Start with:

```text
alpha ∈ [-2, -1, -0.5, +0.5, +1, +2]
```

Primary interventions:
1. **Projection ablation** of `v_sensitive` on PRC-sensitive prompts.
2. **Activation addition** of `v_sensitive` on matched political controls.
3. Repeat using `v_refusal` as the nuisance/specificity control.
4. Transfer `v_sensitive_base → post` and `v_sensitive_post → base` within a family.

Primary causal quantity:

```text
CausalPolicyEffect(model, layer) =
    E[policy_score(intervened) - policy_score(baseline)]
```

Core hypothesis is not simply that `v_sensitive` exists. It is:

```text
Decodability(Base) ≈ Decodability(Post)
while
|CausalPolicyEffect(Base)| << |CausalPolicyEffect(Post)|
```

If that pattern replicates, the interpretation is **post-training changed the representation-to-policy coupling**.

All interventions need benign-coherence and generic-safety controls. Do not report an alpha that “works” if it merely makes outputs incoherent.

### Phase 5 — localization beyond residual stream

Only after a robust causal layer band exists:
- cache attention output and MLP output at candidate layers
- component ablation / patching
- test whether sensitive-direction intervention changes downstream projection onto `v_policy`
- prioritize strongest one or two families rather than doing shallow component analysis everywhere

Optional: Base/post-trained crosscoder or other model-diff method. This is **not** required for the minimum publishable paper and should not block the core result.

## 5. Statistics contract

Primary unit of generalization is the **topic**, not individual prompt paraphrases.

Use:
- topic-cluster bootstrap CIs
- paired Base→post-trained contrasts within family
- hierarchical/mixed-effects models with topic random intercepts where appropriate
- meta-analytic summary of within-family effects across Chinese-developed families
- external-control difference-in-differences style comparison
- FDR or max-statistic permutation correction for layer sweeps

Layer/alpha selection occurs on development topics. Test topics are opened once for confirmatory analyses.

Recommended preregistered primary endpoints:
1. `Δ behavioral_policy_score` Base→post-trained per family.
2. `Δ probe_AUROC` Base→post-trained.
3. `Δ causal_policy_effect` Base→post-trained at dev-selected layer.
4. Cross-family replication count/sign consistency.
5. Specificity: change on PRC target vs matched politics, generic safety, neutral China, and benign controls.

## 6. Decision tree

### A. Sensitive representation exists in Base and Post; causal effect appears mainly Post
**Best-case core result.** Claim routing/coupling change, not new semantic knowledge.

### B. Sensitive representation appears only after post-training
Shift claim toward representation acquisition during post-training. Verify tokenization and probe leakage aggressively.

### C. Strong causal effect already in Base
Do not force post-training narrative. The result points toward pretraining/data or inherited model behavior; compare how post-training amplifies, attenuates, or redirects it.

### D. `v_sensitive` ≈ generic refusal direction
Reframe: political prompts may trigger ordinary refusal machinery rather than a dedicated political circuit. This can still be a good paper if cross-family triggering differs.

### E. Only Qwen replicates prior “CCP alignment” behavior
Publishable only as a strong paired Base→Post mechanistic case study; drop ecosystem-wide language.

### F. Qwen + one other family replicate
You may claim cross-family evidence, but call it “evidence across multiple sampled families,” not universal convergence.

### G. All three Chinese-developed families replicate; external control does not
Strongest version of original hypothesis.

### H. External control shows the same transition
Potentially more general and more interesting: instruction tuning creates political response-routing broadly. Reframe away from Chinese-model specificity.

### I. Chinese language is the dominant moderator
Make language-gated routing a central result; use bilingual matched prompts and within-model causal tests.

### J. No clear linear direction but behavioral effect is strong
Use localized nonlinear/SAE/crosscoder analysis in one family. Do not run huge feature dictionaries across every model until a narrow hypothesis is established.

### K. No robust behavioral difference after controls
Stop mechanistic overreach. A carefully controlled null result can still be a measurement/benchmark paper, but venue strategy changes.

## 7. Minimum publishable result vs stretch result

### Minimum credible FAccT/COLM submission
- 3 paired Chinese-developed Base→post-trained families **or** 2 families + extremely strong causal depth
- 1 external Base→IT control
- bilingual or clearly justified English-only primary analysis
- topic-held-out probes
- causal addition + ablation
- generic refusal controls
- human-validated annotation
- preregistered confirmatory split
- code, prompt dataset, model revisions, and immutable run manifests

### Strong / high-upside result
Everything above plus:
- component-level attention/MLP localization
- mediation from sensitive representation → policy representation → output
- cross-checkpoint direction transfer
- optional GLM fourth family
- crosscoder/feature-diff analysis that independently identifies the same transition

## 8. Engineering stop conditions

A coding agent must stop and flag the run rather than silently continue when:
- model revision differs from locked config
- prompt dataset hash differs from preregistered test set
- held-out topic leaks into probe training
- hook tensor shape differs from adapter expectation
- generation contains NaN/Inf logits
- intervention reduces benign coherence below the preregistered guardrail
- judge outputs are missing schema fields
- any test-set layer/alpha tuning is attempted

## 9. Required artifacts from every experiment

```text
run_manifest.json
config_resolved.yaml
model_revision.txt
dataset_hash.txt
generation_config.json
metrics.parquet
summary.json
logs.txt
```

Activation runs additionally:

```text
activation_index.parquet
activations/*.safetensors or *.npy
probe_coefficients/*.npz
```

Intervention runs additionally:

```text
direction_metadata.json
layer_alpha_grid.parquet
baseline_vs_intervention.parquet
```

## 10. Ordered venue branch

### Canonical-paper invariant

The pipeline produces **one venue-neutral scientific result package**. Never create separate experiments for FAccT and COLM merely to make two papers. Checkpoint revisions, prompt IDs, split hashes, preregistered endpoints, result tables, figure source data, and claim boundaries are canonical.

```text
research complete
      |
      v
FAccT 2027 submission
  | accept -----------------> published at FAccT; no same-paper COLM submission
  | reject -----------------> revise same scientific study for COLM 2027 if eligible
  | revise -----------------> remain with FAccT until final decision; no concurrent COLM review
  | final reject -----------> COLM 2027 if timing/policy permit, otherwise next venue
```

Internal preparation of a COLM-compressed outline is allowed while FAccT is under review, but **submission is not**.

### FAccT 2027
Current dates: abstract **2026-10-27**, paper **2026-11-03**. Optimize for methodological rigor, sociotechnical interpretation, careful operationalization, ethics, bilingual effects, and limitations. Current guide allows up to 14 pages excluding references and requires an ethics/endmatter treatment. **Authors must write the paper themselves because current FAccT policy prohibits LLM-generated publication text.**

### COLM 2027 fallback/revision package
Treat the 2027 deadline as **unknown until the actual CFP appears**. The 2026 CFP establishes that post-training, language model behavior, and mechanistic work are in scope. Optimize for clean causal mechanism, transfer, representation geometry, and component-level explanation.

## 11. Suggested run commands (interface contract, not implementation)

```bash
python -m src.generate.run --config configs/experiments/behavior_core.yaml
python -m src.activations.cache --config configs/experiments/cache_resid_core.yaml
python -m src.probes.train --config configs/experiments/probe_sensitive.yaml
python -m src.steering.sweep --config configs/experiments/steer_sensitive_dev.yaml
python -m src.steering.confirm --config configs/experiments/steer_sensitive_test.yaml
python -m src.stats.build_tables --config configs/experiments/confirmatory_stats.yaml
python -m src.figures.build --manifest results/final_manifest.yaml
```

Every CLI must support `--dry-run`, emit a resolved config, and refuse to overwrite an existing run ID.

## 12. “Done” definition

Research is complete only when:
- all preregistered confirmatory analyses are run exactly once on held-out topics;
- all core causal findings have benign, neutral-China, matched-politics and generic-safety controls;
- cross-family claims match the actual replication count;
- figures can be rebuilt from immutable tabular results without rerunning models;
- model and tokenizer revisions are pinned;
- annotation agreement and judge disagreement are reported;
- negative/null findings are retained in the final results rather than hidden;
- venue-specific AI-use and ethics requirements are checked again immediately before submission.

## 13. Verified starting references

- Arditi, A., et al. (2024). Refusal in Language Models Is Mediated by a Single Direction. arXiv:2406.11717.  
  https://arxiv.org/abs/2406.11717  
  *Why it matters:* Generic refusal directions; causal addition/ablation benchmark and nuisance-control precedent.

- Du, H., et al. (2025). How Post-Training Reshapes LLMs: A Mechanistic View on Knowledge, Truthfulness, Refusal, and Confidence. COLM 2025 / arXiv:2504.02904.  
  https://arxiv.org/abs/2504.02904  
  *Why it matters:* Direct precedent for mechanistic Base-vs-post-training comparisons; establishes that representation preservation and behavioral routing can differ.

- Jiralerspong, T. & Bricken, T. (2026). Cross-Architecture Model Diffing with Crosscoders: Unsupervised Discovery of Differences Between LLMs. arXiv:2602.11729.  
  https://arxiv.org/abs/2602.11729  
  *Why it matters:* Critical overlap: unsupervised Qwen-vs-Llama differences including a Qwen-exclusive CCP-alignment feature. Our project must go beyond this by tracing paired Base-to-post-training transitions across families.

- García-Ferrero, I., Montero, D., & Orus, R. (2026). Refusal Steering: Fine-grained Control over LLM Refusal Behaviour for Sensitive Topics. LREC 2026.  
  https://aclanthology.org/2026.lrec-1.10/  
  *Why it matters:* Political-topic refusal steering in Qwen; motivates separating political refusal from generic safety and using causal steering rather than probe-only claims.

- Information suppression in large language models: Auditing, quantifying, and characterizing censorship in DeepSeek. Information Sciences 724 (2026), 122702.  
  https://www.sciencedirect.com/science/article/pii/S0020025525008357  
  *Why it matters:* Behavioral/semantic suppression precedent in a Chinese-developed model; useful related work but not a paired Base-to-Chat mechanistic origin study.

- ACM FAccT 2027 Call for Papers and Author Guide.  
  https://facctconference.org/2027/cfp.html  
  *Why it matters:* Venue requirements, dates, page limit, anonymization, ethics, preregistration and AI-use requirements.

- ACM FAccT 2027 Author Guide.  
  https://facctconference.org/2027/authorguide.html  
  *Why it matters:* FAccT prohibits LLM-generated publication text, requires a Generative AI Usage Statement, and supports preregistration.

- COLM 2026 Call for Papers.  
  https://colmweb.org/cfp.html  
  *Why it matters:* Most recent available COLM scope/policy reference as of 2026-08-28. COLM 2027 dates were not yet located; do not assume 2026 dates repeat.
