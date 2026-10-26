# T10: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering

**baseline · ok**

1 model calls · 0 reads · 6.44 s · $0.003263

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.77

SWE-agent demonstrates that an interface tailored to language-model agents can substantially improve repository-level software issue resolution without changing the underlying model. On SWE-bench, its GPT-4 Turbo configuration resolves 12.47% of 2,294 issues, and ablations on the 300-instance Lite split provide evidence that search, editing, linting, and context choices contribute to performance. The paper also analyzes agent trajectories and recurring failure patterns. The results are meaningful, though the evaluation is bounded by the benchmark, a small set of model configurations, and development-set-driven interface design.

- **strength**: The full-test-set result provides concrete evidence of useful end-to-end capability, while the comparison against RAG establishes a sizable performance difference in the reported setup.
  - Page 5 · citation: whitespace
  - Quote: "SWE-agent with GPT-4 Turbo yields the best performance, solving 12.47% (286/2,294) of the full SWE-bench test set"

- **strength**: The Lite-set ablations support the central claim that interface design matters: removing linting, changing search, or using shell-only editing each reduced resolution in the reported experiments.
  - Page 7 · citation: exact
  - Quote: "Without Linting, 15.0% ↓ 3.0"

- **limitation**: The primary evaluation centers on a fixed set of models and Python repository issues, so the evidence does not establish comparable effectiveness across other model families, languages, or engineering tasks.
  - Page 5 · citation: whitespace
  - Quote: "We evaluate on the SWE-bench dataset, which includes 2,294 task instances from 12 different repositories of popular Python packages"

- **uncertainty**: Interface choices were informed by qualitative inspection of hand-picked easier development examples, alongside hyperparameter sweeps. The paper reports ablations, but how robust the selected design is to alternative development procedures or broader tuning remains unanswered.
  - Page 5 · citation: whitespace
  - Quote: "we arrived at the final ACI design through qualitative analysis of system behavior on small set of hand-picked easier examples"

Unresolved questions:

- How well do the ACI design findings transfer to models beyond GPT-4 Turbo and Claude 3 Opus, and to programming languages or repository tasks outside this benchmark?
- Would independently designed interfaces or a more systematic development-set methodology yield similar ablation effects and full-test performance?
- How could agents be made to recognize and recover from unproductive problem-solving trajectories, a failure pattern the paper observes?
- This assessment is based on the supplied pages; I did not inspect the underlying code, full interaction logs, or any external replication, so implementation details and reproducibility beyond the reported paper results remain unassessed.

## Evidence audit

Provisional model judgments, not human-validated accuracy.

- Observation 1: **supported** — The paper reports 12.47% resolution on the full SWE-bench test set for GPT-4 Turbo, versus RAG results of 1.31% for GPT-4 Turbo and 3.79% for Claude 3 Opus (pp. 5–6). This supports a sizable difference in the reported benchmark setup.
- Observation 2: **supported** — The Lite ablations report lower resolution without linting (15.0% versus 18.0%), with iterative rather than summarized search (12.0% versus 18.0%), and with shell-only editing (10.3% versus 18.0%) (pp. 6–7). The claim accurately describes these reported comparisons.
- Observation 3: **supported** — The evaluation uses SWE-bench, comprising issues from 12 repositories of Python packages, and reports results for GPT-4 Turbo and Claude 3 Opus (pp. 5–6). The paper does not establish comparable effectiveness across other model families, languages, or task domains; this is appropriately stated as a limit on what the evidence establishes, not as a demonstrated failure.
- Observation 4: **supported** — The paper says the final ACI design was reached through qualitative analysis of a small set of hand-picked easier development examples, while other configuration choices were tuned by sweeps (p. 5). The appendix describes a sweep on 37 randomly sampled development instances (p. 18). The qualified question about robustness to alternative development procedures remains open rather than being presented as a proven defect.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
