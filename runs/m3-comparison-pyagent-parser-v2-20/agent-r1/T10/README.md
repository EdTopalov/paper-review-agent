# T10: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering

**agent · ok**

3 model calls · 2 reads · 15.28 s · $0.001115

3 decisions · 3 tool calls · 8532 input tokens (1512 cached) · 464 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

SWE-agent makes a substantive systems contribution by designing an agent-computer interface tailored to language-model interaction with repositories, and evaluates it on SWE-bench with comparative baselines and interface ablations. The reported full-test performance is strong for the paper’s setting, though evidence here is limited to two inspected pages and leaves broader robustness and evaluation details unresolved.

- **strength**: The paper reports an appreciable result on the full benchmark, supported by a stated resolved-task count.
  - Page 5 · citation: exact
  - Quote: "solving 12.47% (286/2,294) of the full SWE-bench test set"

- **strength**: The evaluation includes two distinct comparison setups, including an interactive shell baseline.
  - Page 5 · citation: exact
  - Quote: "The second setting, called Shell only, is adapted from the interactive coding framework"

- **limitation**: The main agent evaluation is centered on two leading language models, which bounds the inspected evidence for generality.
  - Page 5 · citation: exact
  - Quote: "All results, ablations, and analysis are based on two leading LMs"

- **limitation**: The authors state that interface design used qualitative analysis on a small set of hand-picked examples, a potential constraint on design selection evidence.
  - Page 5 · citation: exact
  - Quote: "qualitative analysis of system behavior on small set of hand-picked easier examples"

Unresolved questions:

- How do results and interface ablations vary across repositories, issue types, and model families beyond the two leading models?
- What detailed ablation results and failure analyses support the claimed causal role of ACI design? Those pages were not inspected.
- How robust are the reported outcomes to stochastic variation and alternative evaluation or cost settings?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "limitations"}` | Locate the paper’s explicit scope and limitations for balanced assessment. | 4 matches on pages [3, 9, 10] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 4, "end": 5}` | Inspect evaluation results and comparisons supporting the central performance claim. | read pages [4, 5] | [event 10](trace.jsonl#L10) |
| 3 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Evidence inspected establishes the benchmark result, experimental setup, and method; submit a calibrated review while noting inspection gaps. | review accepted | [event 16](trace.jsonl#L16) |
