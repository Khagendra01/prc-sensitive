# Preregistration Template — Confirmatory Phase

**Freeze this document and its referenced dataset hashes before opening confirmatory test topics.**

## 1. Project metadata
- Preregistration date:
- Commit hash:
- Prompt dataset version/hash:
- Annotation rubric version/hash:
- Model revisions:
- Tokenizer revisions:
- Authors/roles (private version only):

## 2. Primary research questions
- RQ1:
- RQ2:
- RQ3:
- RQ4:
- RQ5:
- RQ7:

## 3. Confirmatory hypotheses
For each H1–H6:
- exact expected direction/sign;
- model families included;
- languages included;
- primary endpoint;
- falsifying observation.

## 4. Dataset and splits
- Train topic IDs:
- Development topic IDs:
- Test topic IDs:
- Matching procedure:
- Translation verification procedure:
- Safety-control dataset and version:
- Exclusion criteria fixed before test:

**Rule:** no topic, translation or paraphrase family may appear in more than one split.

## 5. Behavioral generation
For each model:
- serialized prompt format;
- official chat template version if used;
- Qwen thinking setting;
- system prompt (prefer none);
- generation config;
- max tokens;
- seed(s);
- stopping criteria.

## 6. Primary behavioral outcomes
List exact fields and aggregation rules:
- hard_refusal
- evasion
- factual_coverage
- omission_count
- official_position_agreement
- coherence guardrail

If a composite `policy_score` is used, write the exact formula here before test runs.

## 7. Representation analysis
- activation site: last prompt token;
- residual definition: pre/post block exactly specified in code config;
- probe estimator;
- regularization/tuning rule;
- layer coordinate;
- held-out evaluation metric;
- lexical/entity masking controls.

## 8. Causal intervention analysis
- direction construction rule;
- vector normalization;
- alpha grid used on development only;
- exact layer-selection rule from development data;
- projection-ablation formula;
- activation-addition formula;
- generic refusal nuisance-control procedure;
- coherence/safety exclusion guardrail.

## 9. Primary confirmatory endpoints
Specify exactly:
1. Base→Post change in behavioral policy outcome by family.
2. Base→Post change in sensitive-probe decodability.
3. Base→Post change in causal policy effect at dev-selected layer(s).
4. Cross-family sign/replication criterion.
5. External-control contrast.
6. Target-vs-control specificity.

## 10. Statistics
- generalization unit: topic;
- confidence interval method;
- hierarchical/mixed model formula if used;
- layer multiple-comparison correction;
- alpha/layer tuning ban on test;
- missing-data handling;
- human-annotation agreement statistic.

## 11. Decision branches fixed in advance
- If representation exists in Base but causal effect appears Post:
- If representation appears only Post:
- If Base is already causal:
- If generic refusal explains the effect:
- If only one family replicates:
- If external control behaves similarly:
- If language is the main moderator:
- If no behavioral effect survives controls:

## 12. Deviations
After the preregistration is frozen, every deviation must be recorded with:
- date;
- reason;
- whether decided before or after seeing relevant outcome data;
- whether analysis is confirmatory or exploratory.
