# Publication Strength Gate and Residual Risk Register

This file defines what counts as a **strong publication result** after the core experiments succeed. It exists to prevent the project from stopping at a result that is statistically clean but scientifically unsurprising.

## Why this exists

A Base→post-training behavioral gap is necessary for the main story, but it is not sufficient. Reviewers may reasonably say that post-training changing output policy is expected. The contribution therefore depends on identifying **how the causal mapping changes**, showing specificity, and establishing whether that mechanism generalizes across model families or policy domains.

## Strength hierarchy

| Result obtained | Internal assessment |
|---|---|
| Behavioral Base/Post difference only | Weak / incremental |
| + PRC-sensitive linear representation | Still incremental |
| + causal activation addition or ablation | Interesting |
| + separation from generic refusal | Stronger |
| + layer-localized emergence of causal coupling | Strong |
| + replication in at least two independent Chinese-developed families | Very strong |
| + external Base→IT control differs qualitatively | Strong specificity evidence |
| + attention/MLP/component localization or mediation | Potential top-tier centerpiece |
| + same representation→policy mechanism generalizes to unrelated policy domains | Broadest / strongest version |

## Publication-strength gate

The project does **not** consider the central hypothesis sufficient for a strong paper merely because Base and Post differ.

A strong-paper claim should require, at minimum:

1. a robust Base→Post behavioral change on preregistered held-out topics;
2. topic-held-out evidence that the sensitive representation is decodable;
3. causal intervention showing that manipulating the representation changes response policy;
4. benign, neutral-China, matched-politics and generic-refusal controls demonstrating specificity;
5. replication in at least two independently developed model families, or one exceptionally deep mechanistic case study;
6. an explicit result on whether the external Base→IT control shows the same transition;
7. claim language that matches the actual replication count and does not infer developer/government intent.

The preferred centerpiece is stronger:

> Post-training leaves much of the sensitive semantic representation intact while changing the causal coupling from that representation to response policy, localized to a reproducible layer/component band.

That statement is a hypothesis to test, not a conclusion to assume.

## Residual publication risks even with clean results

### R12 — Effect size / interestingness
**Risk:** The causal gap is real but small, diffuse, or obvious enough that reviewers regard it as confirmation that post-training changes behavior.

**Mitigation:**
- prioritize causal depth/component localization over behavioral effect size alone;
- quantify representation change separately from policy-coupling change;
- test direction transfer Base↔Post;
- test mediation into a downstream policy/refusal representation;
- preserve effect sizes and uncertainty rather than optimizing for visually dramatic examples.

**Pivot:** If the gap is small but the mechanism is clean, frame around localization/method. If both effect and mechanism are weak, do not force a top-venue claim.

### R13 — Novelty vs refusal/safety mechanism literature
**Risk:** Reviewers view the study as an incremental application of known RLHF/refusal-direction methods to China-sensitive prompts.

**Mitigation:**
- make paired Base→Post **origin/localization** the primary novelty, not steering alone;
- directly compare the PRC-sensitive direction to generic refusal directions;
- emphasize cross-family replication and checkpoint transfer;
- explicitly position against Arditi-style refusal directions, mechanistic post-training work, political refusal steering, and Qwen-vs-Llama model-diff work;
- keep a living prior-work matrix that records what each paper already establishes and what this project uniquely tests.

**Failure condition:** If prior work is found that already performs the same paired cross-family Base→Post causal localization with the same controls, revise the contribution before continuing expensive runs.

### R14 — Political framing / construct validity
**Risk:** Reviewers believe the benchmark encodes the conclusion through topic choice, reference framing or annotation criteria.

**Mitigation:**
- use matched non-PRC political controversies;
- use neutral-China controls;
- use bilingual English/Chinese pairs;
- blind annotators to model/checkpoint/intervention;
- separate refusal, evasion, factual coverage, omission, unsupported claims and official-position agreement;
- preregister topic groups and primary outcomes;
- define official-position agreement descriptively and independently from factual correctness;
- report nulls and cases that run against the motivating hypothesis.

### R15 — Venue-fit variance
**Risk:** The same technically solid result reads as narrow to one venue or insufficiently sociotechnical/mechanistic to another.

**Mitigation:** Maintain one canonical scientific core and package it differently only at the framing level:
- **FAccT:** audit methodology, construct validity, bilingual effects, transparency, ethics and implications.
- **COLM:** post-training mechanism, causal depth, direction transfer, component localization and generalization.
- **ICLR:** not a primary target; reconsider only if the result becomes a general method/mechanism of representation→policy coupling beyond the PRC-sensitive domain.

### R16 — Reviewer variance
**Risk:** Strong mechanistic work still receives divergent scores due to perceived narrowness, downstream significance or interpretability standards.

**Mitigation:** Ensure the paper has three independent reasons to care:
1. **Mechanistic:** identifies where/how Base→Post policy coupling changes.
2. **Methodological:** distinguishes semantic representation from causal response routing across checkpoints/families.
3. **Sociotechnical:** demonstrates why behavior-only political audits can misidentify the origin of model behavior.

## Stretch generalization experiment

This is **P1**, not part of the minimum confirmatory design.

After the core PRC-sensitive mechanism is discovered and frozen, test one or two unrelated policy domains to answer:

> Is the observed Base→Post representation-to-policy transition PRC-specific, or an instance of a more general post-training routing mechanism?

Candidate domains must be selected before seeing their mechanistic outcomes and should not simply reuse generic harmful-content refusal.

Possible examples:
- a non-China geopolitical sensitivity domain;
- a provider-policy / contested social-topic domain with matched Base/Post behavior;
- another non-safety response-policy domain where post-training changes willingness, framing or disclosure.

### Interpretations
- **Same mechanism across unrelated domains:** strongest generalization; political setting becomes a case study of general post-training policy routing.
- **Different domain-specific mechanisms:** supports specialized routing rather than one universal post-training circuit.
- **No analogous transition:** strengthens specificity of the PRC-sensitive result if controls remain strong.

Do not add this experiment until the core causal result and confirmatory plan are stable.

## Stop/go rule for submission

Before labeling the project “submission ready,” answer:

- Is the result more than “post-training changes behavior”?
- Can we causally identify a representation→policy change?
- Is the effect specific rather than generic degradation/refusal?
- Does it replicate, or is the one-family mechanism deep enough to stand alone?
- Does the paper clearly state what prior work already did?
- Would the main contribution remain scientifically interesting if the political labels were anonymized?

If the answer to the last question is **no**, the mechanism is probably not yet strong enough for COLM-level framing.
