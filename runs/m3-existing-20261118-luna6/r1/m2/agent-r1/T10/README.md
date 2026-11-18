# T10: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering

**agent · ok**

4 model calls · 3 reads · 7.95 s · $0.001706

4 decisions · 4 tool calls · 19917 input tokens (9240 cached) · 583 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.77

SWE-agent makes a substantial empirical contribution by showing that an LM-oriented agent-computer interface can improve autonomous issue resolution: it reports 12.47% resolved on full SWE-bench with GPT-4 Turbo and evaluates interface components through ablations. Its useful design findings are supported on the reported benchmark, though conclusions are bounded by tested models, task distribution, and a manually informed design process.

- **strength**: The paper isolates interface design while holding the language model fixed, and combines qualitative inspection with a configuration sweep to motivate design choices.
  - Page 3 · citation: whitespace
  - Quote: "In this paper, we keep the language model fixed, and we focus on designing the ACI to achieve better performance."

- **strength**: The main results provide benchmark evidence for the system’s performance across the full and Lite test sets, with two tested models and baseline comparisons.
  - Page 6 · citation: exact
  - Quote: "w/ GPT-4 Turbo 12.47 1.59 18.00 1.67"

- **strength**: Interface ablations support the claim that editing feedback and linting matter to performance on SWE-bench Lite.
  - Page 7 · citation: whitespace
  - Quote: "Without SWE-agent’s file editor interface, performance drops to (10.3% ↓ 7.7)."

- **limitation**: The authors selected the interface partly through qualitative analysis on hand-picked easier development examples, so the design process may not establish that the selected ACI is generally optimal.
  - Page 5 · citation: whitespace
  - Quote: "through qualitative analysis of system behavior on small set of hand-picked easier examples from the development split of SWE-bench."

Unresolved questions:

- How well do the interface findings transfer to models beyond GPT-4 Turbo and Claude 3 Opus, repositories outside the benchmark, or later model generations?
- Would independently chosen or systematically broader development tasks produce similar interface choices and ablation effects?
- The review inspected pages 1 and 3–8, not the rest of the paper; additional limitations, details, and analyses may affect the overall assessment.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "limitations"}` | Locate the authors’ stated scope and limitations for fair assessment. | 4 matches on pages [3, 9, 10] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 3, "end": 5}` | Inspect method and benchmark setup, including the agent interface and evaluation design. | read pages [3, 4, 5] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 6, "end": 8}` | Inspect quantitative results, interface ablations, and stated evaluation boundaries. | read pages [6, 7, 8] | [event 15](trace.jsonl#L15) |
| 4 | submit_review `{"review": {"score": 0.77, "observations": 4}}` | Evidence covers the interface contribution, benchmark results, ablations, and some behavioral analysis; submit an assessment with remaining scope uncertainty. | review accepted | [event 20](trace.jsonl#L20) |
