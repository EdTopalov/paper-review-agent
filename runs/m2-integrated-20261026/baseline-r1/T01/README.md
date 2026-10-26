# T01: ReAct: Synergizing Reasoning and Acting in Language Models

**baseline · ok**

1 model calls · 0 reads · 8.51 s · $0.004118

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.79

ReAct presents a simple few-shot prompting paradigm that interleaves language-model reasoning with actions and environment feedback. Across knowledge-intensive QA and fact verification and interactive ALFWorld and WebShop tasks, the paper reports gains over action-only prompting and competitive or improved results against reasoning and task-specific baselines. Its analyses also expose meaningful trade-offs: grounding can reduce hallucinations, while retrieval failures and reasoning loops remain weaknesses. Evidence is promising across varied benchmarks, though the method is manually prompted and several evaluations are limited in scale.

- **strength**: The paper gives a clear and reusable formulation: language thoughts augment the action space, letting the model update plans and use observations in subsequent reasoning. The experiments span retrieval-based reasoning and interactive decision-making.
  - Page 3 · citation: wrong_page
  - Quote: "ReAct prompts LLMs to generate both verbal reasoning traces and actions pertaining to a task in an interleaved manner"

- **strength**: The reported results support the approach across distinct settings: the combined methods improve over CoT-SC on both QA benchmarks, while ReAct improves success on WebShop and ALFWorld over action-only prompting in the reported trials.
  - Page 6 · citation: not_found
  - Quote: "CoT-SC→ ReAct 34.2 64.6"

- **limitation**: The paper’s own error analysis shows a real trade-off: ReAct has more reasoning errors than CoT, and unhelpful search results can derail trajectories. This qualifies claims of robustness and groundedness.
  - Page 6 · citation: exact
  - Quote: "For ReAct, successfully retrieving informative knowledge via search is critical."

- **uncertainty**: Evidence for generalization and robustness is bounded by manually authored few-shot prompts, a small ALFWorld evaluation set, and reported best-of-multiple-trial results. The paper describes prompt permutations, but the supplied pages do not establish broader performance across annotators, models, or deployment conditions.
  - Page 7 · citation: normalized
  - Quote: "we evaluate on 134 unseen evaluation games in a task-specific setup"

Unresolved questions:

- How sensitive are results to who writes the demonstrations, their wording, and the prompt-selection procedure?
- Do the reported gains persist across a broader range of base models and larger or less curated interactive tasks?
- Can retrieval quality, recovery from uninformative results, and repetitive action loops be improved without sacrificing the grounding advantage?
- How do reasoning traces affect reliability and user trust in systematic human evaluations? The paper presents interpretability and human-in-the-loop examples, but leaves systematic study as future work (p. 9).

## Evidence audit

Provisional model judgments, not human-validated accuracy.

- Observation 1: **supported** — Page 3 defines ReAct as augmenting the action space with language thoughts that update context and support later reasoning or action; pages 3–4 describe using observations and applying the method across reasoning and decision-making tasks.
- Observation 2: **overstated** — The combined ReAct/CoT-SC methods exceed CoT-SC on both QA benchmarks (page 6, Table 1). But standalone ReAct does not improve success on WebShop over Act: WebShop success is 40.0% versus 30.1% (page 8, Table 4), while the ALFWorld comparison is reported across six trials and includes best-of-six figures. The claim incorrectly groups both interactive tasks as reported “trials” improvements.
- Observation 3: **supported** — The sampled HotpotQA error analysis reports a higher reasoning-error proportion for ReAct than CoT (47% vs. 16%) and says non-informative search results account for 23% of ReAct error cases and can derail reasoning (page 6, Table 2 and discussion). The stated trade-off is grounded in the paper.
- Observation 4: **overstated** — Manual few-shot demonstrations are documented (pages 3–5), and ALFWorld evaluation covers 134 unseen games with six prompt permutations (page 7). However, “best-of-multiple-trial results” applies to some reported ALFWorld comparisons, not the reported WebShop result; the paper also reports ALFWorld averages and six controlled trials (pages 7–8). The caveat about broader annotator, model, and deployment coverage is a reasonable boundary on the evidence, not a demonstrated defect.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
