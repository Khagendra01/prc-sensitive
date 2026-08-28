# Master Research Blueprint — GitHub Text Export

> Source: generated from the canonical planning artifact `00_master_research_blueprint.docx`.
> This is a research-planning artifact, not manuscript prose.

<PARSED TEXT FOR PAGE: 1 / 16>

PRC-sensitive post-training mechanisms — research planning artifact — v1.0 — 2026-08-28
MASTER RESEARCH BLUEPRINT
From Representation to Response Policy
Paired Base Post-Training Mechanistic Study of PRC-Sensitive Behavior Across Open- →
Weight LLM Families
Research operating document • implementation handoff • decision tree • venue plan
Version 1.0 — 28 August 2026
Publication-policy warning: This is a planning and implementation artifact. The current FAccT 2027 
Author Guide prohibits LLM-generated publication text. Do not paste wording from this document into a 
FAccT paper. Authors should write the manuscript themselves and maintain a Generative AI usage log.
0. One-page operating summary
Research objective: determine whether post-training changes how existing PRC-sensitive semantic 
representations are causally routed into refusal, evasion, omission, or politically aligned framing, and 
whether that transition functionally converges across independently developed Chinese open-weight 
model families.
 Core families: Qwen3, DeepSeek LLM, Yi-1.5; optional GLM-4 replication.
 External control: one matched Llama 3.1 Base Instruct pair, used to test whether the phenomenon is →
merely generic instruction tuning.
 Primary design: paired within-family Base post-trained contrasts; cross-family replication is a second →
level of evidence.
 Primary mechanistic distinction: semantic detection/decodability versus causal response-policy 
coupling.
 Primary causal methods: activation addition, projection ablation, within-family direction transfer, then
component-level localization if justified.
 Primary generalization unit: political topic, not prompt paraphrase.
 Ordered venue strategy: maintain one canonical scientific study and result package; submit first to 
FAccT 2027 if the scientific gates are met, then use COLM 2027 as the planned fallback/revision route 
only if the work is no longer under review at or committed to FAccT.
1. Venue targets and hard constraints
Venue Current status Key dates / limits Best story
ACM FAccT 2027 CFP and Author Guide live Abstract Oct 27, 2026; paper 
Nov 3, 2026; up to 14 pages 
excluding references
Sociotechnical transparency 
+ causal audit + 
bilingual/cross-family 
evidence + ethics
COLM 2027 2027 CFP not confirmed as 
of Aug 28, 2026
Do not infer dates from 
2026. 2026 CFP: 9-page main 
text and explicit LM/post￾training scope.
Mechanistic post-training 
story + causal routing + 
transfer/component analysis

<PARSED TEXT FOR PAGE: 2 / 16>

PRC-sensitive post-training mechanisms — research planning artifact — v1.0 — 2026-08-28
 FAccT 2027 requires anonymization and has a revise/re-review process. Current guide explicitly 
supports preregistration.
 FAccT 2027 requires a Generative AI Usage Statement and currently prohibits LLM-generated 
publication text, while allowing limited assistance such as grammar/formatting when disclosed.
 COLM 2027 dates and policies are not yet confirmed. The latest COLM rules (2026) prohibited 
concurrent archival submission and used a 9-page main-text limit; use those only as planning 
assumptions and re-check the 2027 CFP when released.
 Maintain an AI-use log starting now. Record planning assistance, any LLM-assisted prompt generation, 
judging, code generation, figure generation, and manuscript assistance separately.
1.1 Ordered FAccT → COLM submission strategy
 Canonical-paper rule: maintain one frozen scientific core—research questions, preregistered 
hypotheses, model panel, datasets, experiment IDs, result tables, statistical analyses and causal 
conclusions. Venue versions may reorganize or compress this material but must not silently change the
science.
 First target: submit an archival FAccT 2027 paper if Gates G1–G5 and the venue gate are satisfied. 
FAccT 2027 abstract deadline is 2026-10-27 and paper deadline is 2026-11-03; first-round decisions are 
2026-12-22 and final decisions are 2027-03-23.
 Fallback target: if FAccT rejects the paper, or otherwise leaves the work eligible for another archival 
conference, revise the same scientific study for COLM 2027 once its CFP is released. Do not run a new 
research project merely to change venues.
 Revise branch: if FAccT returns a major/minor revision, remain in the FAccT review process through 
final resolution. A COLM version may be prepared internally but must not be concurrently submitted.
 Acceptance branch: if the archival FAccT paper is accepted, the same or substantially similar paper is 
not subsequently submitted to COLM. A later COLM submission would require a materially distinct 
contribution, such as a new method or substantial mechanistic extension.
 Non-archival FAccT is not a workaround for a planned later archival conference submission: the 
current FAccT guide says this option is not intended for a later archival conference version.
 Parallel preparation is internal only: maintain venue-neutral result tables/figures plus FAccT and 
COLM packaging checklists, without simultaneous archival review.
2. Exact novelty target and prior-work boundary
The project is not novel merely because it finds political refusal in Qwen, a PRC-alignment direction in 
Qwen, or a generic Base post-training refusal change. Those pieces already have close precedents. The →
defensible gap is the paired, cross-family origin story: what changes from Base to post-trained checkpoints, 
whether semantic representation and behavioral routing change differently, and whether the same 
functional transition replicates across independent Chinese-developed families.
Prior result What is already known What this project must add
Generic refusal direction Single/low-dimensional refusal-mediated 
behavior can be causally manipulated 
across many chat models.
Treat generic refusal as a 
nuisance/control direction and show 
whether political routing is separable.
Base vs post-training mechanics Post-training can preserve some 
representations while changing refusal 
directions and transferability.
Apply this logic to PRC-sensitive political 
response policy, not generic safety.
Qwen vs Llama model diffing A 2026 crosscoder study reported a Trace Qwen Base post-training and →

<PARSED TEXT FOR PAGE: 3 / 16>

PRC-sensitive post-training mechanisms — research planning artifact — v1.0 — 2026-08-28
Qwen-exclusive CCP-alignment feature 
relative to Llama.
replicate functionally across other 
families; do not make Qwen-vs-Llama the
main contribution.
Political refusal steering in Qwen Political refusal can be manipulated and 
may concentrate in later layers.
Explain when/where the causal policy 
connection emerges relative to Base and 
whether it replicates.
DeepSeek suppression audits Behavioral and semantic suppression has
been documented.
Use a paired DeepSeek Base Chat design →
and causal activation interventions.
3. Research questions
ID Question Priority
RQ1 Behavior emergence — Does post￾training change refusal, evasion, 
omission, factual coverage, or PRC￾official-position agreement on PRC￾sensitive prompts within each family?
Primary
RQ2 Representation vs policy — Is PRC 
sensitivity already linearly decodable in 
Base models, while post-training mainly 
changes the causal mapping from that 
representation to response policy?
Primary
RQ3 Causal localization — At which 
normalized depths does manipulating a 
PRC-sensitive representation alter 
downstream response policy, and does 
that causal profile differ between Base 
and post-trained checkpoints?
Primary
RQ4 Cross-family convergence — Do 
independent Chinese-developed families 
show functionally convergent Base-to￾post-training changes, even when their 
internal vectors are not geometrically 
homologous?
Primary
RQ5 External control — Does a matched non￾Chinese Base-to-Instruct pair show the 
same PRC-specific transition, a generic 
political transition, or neither?
Secondary / control
RQ6 Language gating — Are the same 
representations and causal effects 
stronger, weaker, or qualitatively 
different in Simplified Chinese versus 
English?
Secondary
RQ7 Generic refusal separation — Can PRC￾sensitive routing be dissociated from 
generic harmful-content refusal 
geometrically and causally?
Primary control
4. Hypotheses and falsifiers
ID Hypothesis Why it matters If false / branch
H1 PRC-sensitive topic identity is 
decodable above matched 
political controls in both Base 
and post-trained checkpoints.
Supports semantic detection 
existing before policy 
alignment.
If absent in Base but present in 
post-trained, representation 
acquisition becomes the finding.
H2 Post-training increases the 
causal effect of the PRC-sensitive
direction on 
refusal/evasion/framing more 
than it increases topic 
decodability.
Core “knowledge-to-policy” 
hypothesis.
If causal effect is equally strong 
in Base, emphasize 
pretraining/data effects or 
continuity rather than post￾training routing.
H3 The post-training increase in Supports cross-family functional If one family only, report model-

<PARSED TEXT FOR PAGE: 4 / 16>

PRC-sensitive post-training mechanisms — research planning artifact — v1.0 — 2026-08-28
causal policy effect replicates in 
at least two independent 
Chinese-developed families.
convergence. specific mechanism; do not 
generalize ecosystem-wide.
H4 The PRC-sensitive direction is 
not reducible to the generic 
refusal direction.
Needed to claim specialized 
political routing.
If highly aligned, reframe as 
context-specific triggering of 
generic refusal machinery.
H5 The external Llama control 
shows a smaller or qualitatively 
different PRC-specific Base-to￾Instruct transition.
Supports specificity beyond 
generic instruction tuning.
If Llama shows same transition, 
pivot to general post-training 
political routing rather than 
China-specific mechanism.
H6 Chinese-language prompts 
change either representation 
strength or downstream causal 
coupling within Chinese￾developed models.
Tests language as a 
gate/modulator.
If no language effect, simplify 
paper and treat bilingual 
replication as robustness.
5. Claims we are allowed to make — and claims we are not
5.1 Allowed if supported
 “Within these sampled model families, post-training increased/decreased a causal response-policy 
effect associated with PRC-sensitive prompts.”
 “A PRC-sensitive representation was linearly decodable before post-training, but its downstream 
behavioral influence changed after post-training.”
 “The transition replicated functionally across N independently developed Chinese model families.”
 “The effect was/was not distinguishable from generic refusal under our geometric and causal controls.”
 “The effect was stronger/weaker in Simplified Chinese under matched bilingual prompts.”
5.2 Prohibited overclaims
 Do not call a vector a “propaganda neuron” or “censorship neuron” solely from activation correlations.
 Do not infer the intentions of Alibaba, DeepSeek, 01.AI, Z.ai, Meta, the PRC government, regulators, or 
individual engineers.
 Do not claim that any observed feature arose from a particular regulation unless training provenance 
directly supports that claim.
 Do not say “Chinese models do X” when the sample contains only a few model families.
 Do not merge refusal, omission, factual error and agreement with official positions into one political 
label without reporting the components.
6. Model panel and selection rules
Family Base Post-trained Size/layers Role Priority
Qwen3 Qwen/Qwen3-8B-Base Qwen/Qwen3-8B 8.2B / 36 Core family #1 / 
replication of prior 
Qwen finding with 
paired base
P0
DeepSeek LLM deepseek-ai/deepseek￾llm-7b-base
deepseek-ai/deepseek￾llm-7b-chat
7B / 30 Core family #2; 
official card states 
Chat initialized from 
Base
P0
Yi-1.5 01-ai/Yi-1.5-9B 01-ai/Yi-1.5-9B-Chat 9B / 48 Core family #3; 
matched Base/Chat 
release
P0
GLM-4 zai-org/glm-4-9b zai-org/glm-4-9b-chat￾hf
9B / verify adapter Optional cross￾architecture 
replication; custom 
architecture increases
P1

<PARSED TEXT FOR PAGE: 5 / 16>

PRC-sensitive post-training mechanisms — research planning artifact — v1.0 — 2026-08-28
engineering cost
Llama 3.1 meta-llama/
Llama-3.1-8B
meta-llama/
Llama-3.1-8B-Instruct
8B / 32 External Base-to￾Instruct control; not a
co-equal research 
target
P0 control
Core model-pair inclusion criteria: (1) publicly available weights; (2) clearly identified Base and post￾trained/Chat checkpoints from the same family; (3) same or directly corresponding architecture/tokenizer 
where possible; (4) approximately 7–9B scale for compute comparability; (5) sufficient Chinese/English 
ability for the target prompts; (6) hookable transformer internals.
Scope guardrail: GLM-4 is optional because cross-architecture/custom-code engineering can consume 
disproportionate time. Complete Qwen3 + DeepSeek + Yi + external control before adding it.
7. Dataset design
The dataset must separate topic identity from response policy. Its purpose is not to maximize sensational 
refusals; it is to support matched contrasts and held-out-topic generalization.
Stratum Target topics Templates/topic/language Purpose
PRC-sensitive 18 4 Target semantic/political 
condition
Matched non-PRC political 18 4 Controls for political 
sensitivity, protest, 
sovereignty, leader criticism, 
historical violence, etc.
Neutral China 10 4 Controls for China-related 
lexical/entity content without 
sensitive politics
General politics 10 4 Controls generic political 
discourse
Generic harmful/harmless 
safety
benchmark subset n/a Estimate generic refusal 
direction and intervention 
specificity
7.1 Topic matching
 Match sensitive PRC topics to non-PRC topics by discourse function where possible: protest protest, ↔
sovereignty sovereignty, historical state violence historical state violence, leader criticism ↔ ↔ ↔
leader criticism.
 Include neutral China topics so a “China entity detector” cannot masquerade as political sensitivity.
 Keep issue names balanced across train/dev/test; topic families, translations and paraphrases never 
cross split boundaries.
 Human-author or human-verify the core prompts. If an LLM proposes paraphrases, log and disclose it; 
never allow unreviewed model-generated prompts into the confirmatory test set.
7.2 Prompt templates
Template Example functional intent Reason
Direct factual Ask what happened / what policy says Tests basic answering and omission
Historical explanation Ask causes, sequence, aftermath Tests narrative coverage
Compare claims Present two conflicting accounts and 
ask for evaluation
Tests attribution and balancing
Critical analysis Ask for criticisms and 
counterarguments
Tests willingness to discuss adverse 
claims

<PARSED TEXT FOR PAGE: 6 / 16>

PRC-sensitive post-training mechanisms — research planning artifact — v1.0 — 2026-08-28
7.3 Language design
 Primary languages: English and Simplified Chinese for Chinese-developed families.
 Translations must be meaning-matched, not literal word-for-word if that changes pragmatics.
 Use bilingual reviewers or professional-quality human verification for confirmatory prompts.
 The external Llama control can be primary in English and secondary in Chinese if language 
competence creates a floor effect; do not interpret poor Chinese competence as political behavior.
7.4 Data schema
{
 "prompt_id": "prc_tiananmen_factual_zh_01",
 "topic_id": "tiananmen_1989",
 "stratum": "prc_sensitive",
 "language": "zh-Hans",
 "template_id": "direct_factual",
 "matched_topic_id": "control_topic_x",
 "prompt_text": "...",
 "author_source": "human",
 "dataset_version": "v0.1"
}
8. Prompting and generation protocol
Track Base checkpoint Post-trained checkpoint Interpretation
Behavior/ecological Fixed completion template: 
Question: {prompt}\nAnswer:
Official chat template; no 
system prompt unless 
preregistered
Measures real user-facing 
behavior, accepts formatting 
differences
Matched representation Identical serialized plain text Same identical serialized plain
text without chat-only special 
instructions
Better isolates weight/post￾training effects in hidden 
states
 Qwen3 primary post-trained condition: disable thinking. Thinking mode becomes a secondary 
robustness study after the core result.
 Primary decoding should minimize variance while remaining valid for each model; record any family￾specific exception. Add a sampled multi-seed robustness subset rather than making every run 
stochastic.
 Pin exact model and tokenizer revisions. Store exact serialized prompt and token IDs.
 Never silently change chat templates or system prompts between runs.
9. Response measurement and annotation
Metric Type Operationalization
Hard refusal binary Explicit inability/unwillingness to answer
Evasion 0–2 ordinal 0 direct; 1 partial/hedged deflection; 2 
largely avoids requested content
Directness 0–2 ordinal Whether answer addresses the user 
question without diversion
Factual coverage proportion Fraction of human-curated issue-specific 
reference facts covered
Omission count/proportion Missing expected reference facts, 
reported separately from falsehood
Official-position agreement ordinal Agreement with a curated set of PRC 
official-position propositions; not itself 
treated as truth/falsity

<PARSED TEXT FOR PAGE: 7 / 16>

PRC-sensitive post-training mechanisms — research planning artifact — v1.0 — 2026-08-28
Unsupported claims count Claims not supported by the curated 
reference packet
Coherence ordinal Guardrail against intervention-induced 
nonsense
Length tokens Control/diagnostic
 Use a deterministic rule-based refusal detector as one measure, not the ground truth.
 If LLM judges are used, use at least two heterogeneous judge families and keep the studied model 
family out of its own judging pipeline.
 Blind human annotators to model identity/checkpoint and intervention status wherever practical.
 Adjudicate all high-stakes judge disagreements and a stratified random sample; report inter-annotator 
agreement.
 If paid external annotators are recruited, seek institutional ethics/IRB guidance and plan fair 
compensation and content warnings.
10. Mechanistic pipeline
10.1 Activation cache
 Primary cache: last prompt-token residual vector at every transformer block for every prompt.
 Store float16/bfloat16-derived arrays with metadata; full-token activations are prohibited for the whole
dataset because storage explodes and most are unnecessary.
 Only after layer localization, cache selected token spans, attention outputs and MLP outputs for a 
narrow confirmatory subset.
 Use normalized layer coordinate r = layer_index / number_of_layers for cross-architecture plots, while 
always retaining exact layer IDs.
10.2 Sensitive, refusal and policy directions
v_sensitive^(l) = mean(h_l | PRC-sensitive) - mean(h_l | matched political control)
v_refusal^(l) = mean(h_l | harmful/refusal-eliciting) - mean(h_l | harmless)
v_policy^(l) = regularized linear direction predicting annotated response-policy score
 Fit difference-in-means and L2-logistic directions independently; convergence increases confidence.
 Train only on training topics. Evaluate on dev/test topics never used to construct the vector.
 Report cosine similarity and subspace overlap between sensitive and refusal directions, plus 
residualized sensitive direction after removing the refusal projection.
 A probe is evidence of accessible information, not evidence of causal use.
10.3 Lexical leakage tests
 Entity-mask or abstract salient proper nouns.
 Remove topic names while preserving discourse structure.
 Contrast against neutral China content containing the same country/leader/entity names where 
possible.
 Use topic-held-out test sets so a probe cannot memorize a few events.

<PARSED TEXT FOR PAGE: 8 / 16>

PRC-sensitive post-training mechanisms — research planning artifact — v1.0 — 2026-08-28
10.4 Causal intervention
Normalize v to unit norm. Let s_l be the median residual norm at layer l.
Addition: h'_l = h_l + alpha * s_l * v
Ablation: h'_l = h_l - <h_l, v> v
Initial dev alpha grid: {-2, -1, -0.5, +0.5, +1, +2}
 Select candidate layers and alpha on development topics only.
 Primary target test: ablate v_sensitive on PRC-sensitive prompts and measure response-policy change.
 Induction test: add v_sensitive to matched non-PRC political prompts and test whether a policy 
response is induced.
 Specificity controls: identical procedures with v_refusal, neutral China prompts, generic benign 
prompts, and harmful-content safety prompts.
 Within-family transfer: apply the Base-derived direction to the post-trained checkpoint and vice versa; 
same-architecture transfer is particularly informative.
 Reject settings that materially degrade coherence or benign loss/perplexity.
10.5 Core routing metric
CausalPolicyEffect(model, l) = E[ policy_score(intervened) - policy_score(baseline) ]
Core pattern of interest:
ProbeDecodability(Base) ProbeDecodability(Post) ≈
BUT
|CausalPolicyEffect(Base)| << |CausalPolicyEffect(Post)|
That pattern supports a representation-to-policy coupling change. If the sensitive representation only 
appears after post-training, the story becomes representation acquisition. If causal effects are already 
strong in Base, the story shifts toward pretraining or continuity rather than post-training origin.
11. Component-level localization (stretch, gated)
 Run only after a robust residual-stream causal band is confirmed.
 Decompose attention output versus MLP output at the candidate band.
 Patch/ablate candidate components and measure downstream projection onto v_policy plus output 
behavior.
 Prefer deep analysis of one or two strongest families over shallow analysis of five families.
 Optional crosscoder/model-diff analysis is a corroborating extension, not the core dependency.
12. Statistical analysis plan
Analysis Rule
Generalization unit Topic. Cluster prompts/paraphrases/translations by topic.
Splits Group train/dev/test by topic; test is sealed until confirmatory 
stage.
Behavior Paired within-family Base Post contrasts; bootstrap CIs →
clustered by topic; hierarchical regression where useful.
Cross-family Report family-specific effects first; then meta-analytic or 
hierarchical summary.
External control Difference-in-differences style contrast: (Chinese-family 
Post Base) vs (control Post Base). − −
Layer sweeps Candidate layers selected on dev; use FDR or max-statistic 
permutation if inferential claims span many layers.

<PARSED TEXT FOR PAGE: 9 / 16>

PRC-sensitive post-training mechanisms — research planning artifact — v1.0 — 2026-08-28
Robustness Replicate sign/effect under at least one alternate decoding 
seed/config on a subset.
 Pre-register primary endpoints and confirmatory splits before full test generation/intervention.
 Do not use test-set results to redefine the political policy score.
 Report standardized effect sizes and uncertainty, not only p-values.
 Retain all negative families/layers in reported results; do not present only the most dramatic model.
13. Decision tree: if/else branches that prevent research drift
Branch Observed result Required pivot
A Representation in Base+Post; causal effect
mainly Post
Core routing result. Proceed to 
replication and component localization.
B Representation only Post Representation-acquisition story. Double￾check leakage/tokenization; test whether 
Base nonlinear representation exists.
C Causal effect already strong in Base Pretraining/continuity result. Measure 
amplification/attenuation by post￾training instead of claiming origin.
D Sensitive direction overlaps generic 
refusal
Reframe as political triggering of generic 
refusal; compare trigger sensitivity 
across families/languages.
E Only Qwen works Model-specific paired Qwen mechanistic 
study; explicitly position as 
extension/replication of 2026 model-diff 
work.
F Two Chinese families work Cross-family evidence is permissible, but 
no universal language.
G Three Chinese families work; control 
differs
Strongest original hypothesis; proceed 
with careful ecosystem-level 
interpretation.
H Control shows same transition Broader result: instruction/post-training 
creates political response routing 
generally. This may be more important 
than a China-specific paper.
I Chinese language dominates Language-gated response policy becomes 
central; deepen bilingual causal analysis.
J Behavior strong, linear direction weak Escalate to SAE/crosscoder/nonlinear 
representation on one family; do not run 
feature discovery everywhere.
K Behavioral difference disappears under 
controls
Stop mechanistic overreach. Consider 
measurement/null-result paper only if 
the benchmark contribution is strong.
14. Predefined project gates
Gate When Pass condition Fail action
G0 Adapter smoke tests All P0 checkpoints load, 
generate and expose residual 
hooks
Replace only failing family; no 
custom-engineering sinkhole
G1 Behavioral pilot Stable target-vs-control signal or
meaningful Base Post change →
in 1 core family ≥
Check language/templates; if 
persistent null, reduce 
mechanistic scope
G2 Probe stage Topic-held-out linear signal 
above preregistered minimum 
and lexical controls pass
Nonlinear diagnostics / narrow 
feature method; no causal linear
claim
G3 Intervention stage Targeted causal effect with 
coherence/safety specificity
Revisit direction definition, 
layer, or conclude decodability ≠
causal use
G4 Replication Same qualitative transition in 
≥2 independent Chinese 
Model-specific paper if one; no 
ecosystem claim

<PARSED TEXT FOR PAGE: 10 / 16>

PRC-sensitive post-training mechanisms — research planning artifact — v1.0 — 2026-08-28
families
G5 External control Control characterizes generic 
post-training baseline
Use whichever result occurs to 
set claim specificity
15. Coding-agent implementation contract
15.1 Repository modules
configs/
 models/ datasets/ experiments/
src/
 models/ data/ generate/ activations/ probes/ steering/ eval/ stats/ figures/
tests/
runs/
results/
 tables/ figures/ prereg/
Module Responsibility
src/models Adapters, tokenizer/chat serialization, block enumeration, hook 
registry, model revision capture
src/data Prompt schema, bilingual validation, topic matching, group 
splits, dataset hashing
src/generate Deterministic behavior generation + robustness sampling
src/activations Memory-safe residual cache and later component cache
src/probes Difference-in-means, logistic probes, held-out evaluation, 
direction metadata
src/steering Forward hooks for addition, ablation, transfer; layer/alpha grid
src/eval Rule metrics, judge adapters, annotation ingestion, schema 
validation
src/stats Bootstrap/hierarchical models, multiple-comparison controls, 
effect tables
src/figures Build figures only from immutable final tables/manifests
15.2 Mandatory CLI behavior
 Every command supports --dry-run.
 Every run writes a fully resolved config and immutable run_manifest.json.
 No run may overwrite an existing run ID.
 Every model run records exact model/tokenizer revision, dependency versions, GPU/CUDA details, 
seeds and dataset hash.
 Test-set configs are read-only/sealed after preregistration; code should refuse a layer/alpha sweep 
against a test split.
 All generated tables include prompt_id/topic_id/model/checkpoint/language/intervention metadata.
15.3 Required run artifacts
run_manifest.json
config_resolved.yaml
model_revision.txt
dataset_hash.txt
generation_config.json
metrics.parquet
summary.json
logs.txt
# activation runs

<PARSED TEXT FOR PAGE: 11 / 16>

PRC-sensitive post-training mechanisms — research planning artifact — v1.0 — 2026-08-28
activation_index.parquet
activations/*
probe_coefficients/*
# intervention runs
direction_metadata.json
layer_alpha_grid.parquet
baseline_vs_intervention.parquet
15.4 Suggested command interface
python -m src.generate.run --config configs/experiments/behavior_core.yaml
python -m src.activations.cache --config configs/experiments/cache_resid_core.yaml
python -m src.probes.train --config configs/experiments/probe_sensitive.yaml
python -m src.steering.sweep --config configs/experiments/steer_sensitive_dev.yaml
python -m src.steering.confirm --config configs/experiments/steer_sensitive_test.yaml
python -m src.stats.build_tables --config configs/experiments/confirmatory_stats.yaml
python -m src.figures.build --manifest results/final_manifest.yaml
16. Compute and storage strategy
 Do not start by caching token-level activations. Last-token residuals at every layer keep storage 
tractable and are sufficient for the first localization pass.
 Run one model pair end-to-end (Qwen3 Base/Post) before launching the full panel. This validates 
schemas, judge logic and intervention hooks.
 Use inference batching sized to GPU memory; activation caching is often bandwidth/storage bound 
rather than compute bound.
 Separate generation jobs from activation jobs so a failed judge or annotation pipeline never requires 
repeating expensive model inference.
 Store bulky activation tensors outside Git; version only manifests, hashes, metadata and small derived 
direction files.
Budgeting rule: Exact GPU-hour estimates should be generated after the Qwen3 smoke/pilot because 
throughput depends strongly on hardware, attention implementation, sequence length and whether 
post-trained reasoning is enabled. The tracker includes a place to log empirical tokens/s and derive the 
full budget.
17. Preregistration, research integrity and ethics
 Create an anonymizable preregistration snapshot before confirmatory test-set runs: research 
questions, topic splits, primary metrics, causal interventions, layer-selection rule, statistical tests and 
exclusion criteria.
 Keep a frozen test-set hash in the repository and tracker.
 Do not collect identities of activists, dissidents or private individuals. This study needs public 
historical/political topics and public model weights only.
 If human annotators are recruited, seek institutional IRB/ethics guidance, obtain appropriate consent, 
minimize exposure to disturbing political content, and compensate fairly.

<PARSED TEXT FOR PAGE: 12 / 16>

PRC-sensitive post-training mechanisms — research planning artifact — v1.0 — 2026-08-28
 Use neutral operational vocabulary in data files: prc_sensitive, matched_politics, 
official_position_agreement, refusal, evasion. Avoid provocative labels that bake conclusions into the 
pipeline.
 Separate empirical observation from causal explanations about training data, regulations or developer 
intent.
 For personal/researcher safety: use ordinary account security, keep the work reproducible and public￾source-based, and obtain institution-specific legal/travel advice if authors have exposure to 
jurisdictions where publication of politically sensitive work may have different risks.
18. Accelerated FAccT 2027 timeline (67 days to paper deadline)
Window Target Exit criterion
Aug 28–Sep 3 Freeze protocol v1; repo skeleton; Qwen3 
+ Llama adapters; prompt v0.1
G0 smoke tests pass for first pair; dataset 
schema frozen
Sep 4–Sep 10 Behavior pilot Qwen3 pair; annotation 
rubric pilot
G1 decision; rubric agreement acceptable
Sep 11–Sep 17 DeepSeek + Yi adapters; full behavioral 
baseline
Core three families have baseline result 
tables
Sep 18–Sep 24 Residual caches + topic-held-out probes G2 decision; candidate layer bands 
selected on dev
Sep 25–Oct 1 Causal steering/ablation Qwen3 + 
strongest second family
G3; specificity controls pass or pivot is 
declared
Oct 2–Oct 8 Third-family replication + external Llama
control
G4/G5; final claim scope known
Oct 9–Oct 15 Confirmatory test runs; human 
adjudication; statistics
Test set opened once; primary tables 
frozen
Oct 16–Oct 22 Figures, limitations, ethics, 
reproducibility package; venue go/no-go
Decision: FAccT submit vs continue for 
COLM
Oct 23–Oct 27 Authors draft abstract/manuscript 
themselves; register abstract
FAccT abstract registered by Oct 27 if 
pursuing
Oct 28–Nov 3 Author-written final paper, checks, 
anonymization, artifact packaging
Submit by Nov 3 if all scientific gates 
passed
No-rush rule: Do not force a FAccT submission just because a deadline exists. If G3/G4 are unresolved by
the Oct 16–22 venue gate, continue the mechanistic work and target COLM 2027 instead.
19. Venue-specific contribution packages
Shared scientific core: identical experiments, checkpoint revisions, prompt/data splits, annotation outputs, 
preregistered endpoints, statistical tables, mechanistic interventions and claim boundaries. Target roughly 
80–90% overlap in scientific evidence, not necessarily in prose.
FAccT changes emphasis and uses the larger main-text budget for audit validity, sociotechnical context and
ethics; COLM compresses the same evidence around post-training mechanism, causal localization and 
transfer. Canonical source tables and figures remain unchanged.
19.1 FAccT version
 Lead with transparency/auditing question and why behavior-only censorship benchmarks cannot 
identify where policy enters the model.
 Make operationalization and matched controls prominent.
 Show bilingual effects and the risks of conflating language competence with political policy.

<PARSED TEXT FOR PAGE: 13 / 16>

PRC-sensitive post-training mechanisms — research planning artifact — v1.0 — 2026-08-28
 Emphasize uncertainty, non-attribution of developer/government intent, and potential societal 
implications.
 Include ethics/adverse impacts and preregistration details.
 Paper prose must be author-written under current FAccT policy.
19.2 COLM version
 Lead with mechanistic question: how post-training changes representation-to-policy coupling.
 Make Base Post direction transfer, causal layer curves and component-level mechanism central. →
 Treat political domain as the controlled case study that reveals a more general post-training 
mechanism.
 Reduce sociopolitical narrative that is not required for the causal argument, while preserving careful 
terminology and ethics.
 Keep a COLM-ready compressed structure in parallel, but do not submit it while FAccT review or 
publication status makes the work ineligible. Verify COLM 2027 dates, page limits, dual-submission 
rules and LLM-use policy when the CFP is released.
20. Planned figures and tables
ID Artifact Question answered
Fig 1 Study design schematic: Base Post pairs →
across Qwen/DeepSeek/Yi + control
What is the causal comparison?
Fig 2 Behavioral Base Post effect by family, →
language and outcome component
Does post-training change policy 
behavior?
Fig 3 Probe AUROC vs normalized depth for 
Base/Post
Where is PRC sensitivity decodable?
Fig 4 Causal policy effect vs normalized depth 
for Base/Post
Where is the representation behaviorally 
used?
Fig 5 Decodability change vs causal-effect 
change scatter
Representation acquisition or routing 
change?
Fig 6 Sensitive vs generic refusal direction 
overlap and intervention specificity
Dedicated routing or generic refusal?
Fig 7 Cross-family summary + external-control 
contrast
Does the transition replicate?
Fig 8 optional Attention/MLP component localization in 
strongest family
What component implements the 
routing?
Table 1 Model pairs, revisions, architecture and 
licenses
Reproducibility
Table 2 Dataset strata, topics, matching and 
languages
Measurement validity
Table 3 Confirmatory effect estimates and CIs Main statistical result
21. Reviewer-attack checklist
Likely criticism Required defense
“You just detected words like Tiananmen/Taiwan.” Topic-held-out splits, entity masking, neutral-China controls, 
matched political events.
“This is generic refusal.” Independent v_refusal, overlap analysis, residualization, and 
differential causal interventions.
“Base and Chat prompts are not comparable.” Separate ecological behavior track from identical-serialization 
representation track.
“Your judge encodes Western/Chinese political bias.” Reference-fact checklists, heterogeneous judges, blinded human
validation, report disagreement.
“Layer 20 in Qwen is not layer 20 in Yi.” Normalize depth; within-family inference first; cross-family 
comparison is functional unless homology is demonstrated.

<PARSED TEXT FOR PAGE: 14 / 16>

PRC-sensitive post-training mechanisms — research planning artifact — v1.0 — 2026-08-28
“You chose the best layer after seeing the test set.” Dev-only layer/alpha selection and sealed confirmatory topics.
“You are inferring state causation.” Explicit non-claim; no causal attribution beyond model post￾training transition.
“One model drives everything.” Family-specific results first; replication threshold defined 
before cross-family claim.
“Steering just breaks the model.” Coherence/perplexity guardrail and neutral/benign controls.
22. Definition of done
 All P0 model pairs use pinned revisions and reproduce from locked configs.
 Core dataset and topic splits are versioned and hashed.
 Behavioral outcomes are separated into refusal/evasion/coverage/framing components.
 At least one human-validated annotation study is completed and agreement reported.
 Probe analyses generalize to held-out topics and pass leakage controls.
 Causal interventions include addition and ablation with benign/safety specificity controls.
 Primary test-set analyses were run only after preregistration/freeze.
 Cross-family claim is exactly proportional to number of families that replicate.
 Null results are retained.
 Final figures rebuild from immutable result tables.
 FAccT/COLM policies are rechecked immediately before each submission, especially concurrent 
submission, prior-publication, page-limit and AI-use rules.
 The paper is authored in compliance with venue rules rather than copied from this planning artifact.
23. Verified starting references and source links
Arditi, A., et al. (2024). Refusal in Language Models Is Mediated by a Single Direction. 
arXiv:2406.11717.
https://arxiv.org/abs/2406.11717
Relevance: Generic refusal directions; causal addition/ablation benchmark and nuisance-control 
precedent.
Du, H., et al. (2025). How Post-Training Reshapes LLMs: A Mechanistic View on Knowledge, 
Truthfulness, Refusal, and Confidence. COLM 2025 / arXiv:2504.02904.
https://arxiv.org/abs/2504.02904
Relevance: Direct precedent for mechanistic Base-vs-post-training comparisons; establishes that 
representation preservation and behavioral routing can differ.
Jiralerspong, T. & Bricken, T. (2026). Cross-Architecture Model Diffing with Crosscoders: 
Unsupervised Discovery of Differences Between LLMs. arXiv:2602.11729.
https://arxiv.org/abs/2602.11729
Relevance: Critical overlap: unsupervised Qwen-vs-Llama differences including a Qwen-exclusive CCP￾alignment feature. Our project must go beyond this by tracing paired Base-to-post-training transitions 
across families.

<PARSED TEXT FOR PAGE: 15 / 16>

PRC-sensitive post-training mechanisms — research planning artifact — v1.0 — 2026-08-28
García-Ferrero, I., Montero, D., & Orus, R. (2026). Refusal Steering: Fine-grained Control over LLM 
Refusal Behaviour for Sensitive Topics. LREC 2026.
https://aclanthology.org/2026.lrec-1.10/
Relevance: Political-topic refusal steering in Qwen; motivates separating political refusal from generic 
safety and using causal steering rather than probe-only claims.
Information suppression in large language models: Auditing, quantifying, and characterizing 
censorship in DeepSeek. Information Sciences 724 (2026), 122702.
https://www.sciencedirect.com/science/article/pii/S0020025525008357
Relevance: Behavioral/semantic suppression precedent in a Chinese-developed model; useful related work
but not a paired Base-to-Chat mechanistic origin study.
ACM FAccT 2027 Call for Papers and Author Guide.
https://facctconference.org/2027/cfp.html
Relevance: Venue requirements, dates, page limit, anonymization, ethics, preregistration and AI-use 
requirements.
ACM FAccT 2027 Author Guide.
https://facctconference.org/2027/authorguide.html
Relevance: FAccT prohibits LLM-generated publication text, requires a Generative AI Usage Statement, 
and supports preregistration.
COLM 2026 Call for Papers.
https://colmweb.org/cfp.html
Relevance: Most recent available COLM scope/policy reference as of 2026-08-28. COLM 2027 dates were not
yet located; do not assume 2026 dates repeat.
Appendix A. Model source links
Family Base URL Post-trained URL License / notes
Qwen3 https://huggingface.co/Qwen/
Qwen3-8B-Base
https://huggingface.co/Qwen/
Qwen3-8B
Apache-2.0
DeepSeek LLM https://huggingface.co/deepseek￾ai/deepseek-llm-7b-base
https://huggingface.co/deepseek￾ai/deepseek-llm-7b-chat
DeepSeek license
Yi-1.5 https://huggingface.co/01-ai/
Yi-1.5-9B
https://huggingface.co/01-ai/
Yi-1.5-9B-Chat
Apache-2.0
GLM-4 https://huggingface.co/zai-org/
glm-4-9b
https://huggingface.co/zai-org/
glm-4-9b-chat-hf
GLM-4
Llama 3.1 https://huggingface.co/meta￾llama/Llama-3.1-8B
https://huggingface.co/meta￾llama/Llama-3.1-8B-Instruct
Llama 3.1 Community

<PARSED TEXT FOR PAGE: 16 / 16>

PRC-sensitive post-training mechanisms — research planning artifact — v1.0 — 2026-08-28
Appendix B. Implementation handoff files
 `01_coding_agent_handoff.md` — direct engineering/run-order brief.
 `02_implementation_spec.yaml` — machine-readable source of truth for models, datasets, gates, 
experiments and repository layout.
 `03_experiment_tracker.xlsx` — editable research operations tracker, experiment registry, decisions, 
risks, timeline and venue readiness.
 `04_references_seed.bib` — starter bibliography for verified mechanistic references; authors must 
independently verify final bibliographic metadata.
