# T11: Executable Code Actions Elicit Better LLM Agents

**agent · ok**

3 model calls · 2 reads · 8.76 s · $0.001215

3 decisions · 3 tool calls · 9087 input tokens (1545 cached) · 532 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.74

The paper proposes CodeAct, using executable Python as an LLM agent action space, and evaluates it against text/JSON formats before presenting a 7k-interaction instruction dataset and finetuned agents. Its central contribution is a broadly applicable action interface that supports tool composition and iterative feedback, with promising benchmark comparisons; the support inspected is strongest for the action-format comparison, while the reported benchmark breadth and practical safety remain open questions.

- **strength**: The central design insight is to use code's control/data flow and interpreter feedback to enable composed, iterative actions rather than relying on fixed-format calls.
  - Page 2 · citation: whitespace
  - Quote: "Integrated with a Python interpreter, CodeAct can execute code actions and dynamically adjust prior actions or emit new action based on observations it receives through multiple turns of interactions (code execution)."

- **strength**: The authors report a sizable improvement on their multi-tool benchmark, alongside fewer actions, although this excerpt does not establish robustness beyond that benchmark.
  - Page 3 · citation: whitespace
  - Quote: "CodeAct achieves up to a 20% absolute improvement over baselines on the success rate of solving the problems while requiring up to 30% fewer actions."

- **limitation**: The authors explicitly identify hallucination about program state as a practical limitation; this is a meaningful reliability concern for autonomous execution, not merely an unanswered question.
  - Page 10 · citation: whitespace
  - Quote: "it may suffer from hallucination commonly seen in LLMs (e.g., imagine the content of a variable without actually printing it out), suggesting the need for subsequent alignment"

Unresolved questions:

- How representative and difficult are the 82 curated benchmark tasks, and do the reported gains persist on independently constructed or real-world tasks?
- How are execution permissions, harmful code, and errors with consequential side effects managed in practical deployment?
- I inspected pages 1–3 and search excerpts from page 10, not the full experimental protocol, detailed results, or limitations discussion; those details could alter confidence in the reported gains.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 2, "end": 3}` | Inspect method and benchmark evidence beyond the abstract and introduction. | read pages [2, 3] | [event 5](trace.jsonl#L5) |
| 2 | search_paper `{"query": "limitations"}` | Check whether the paper states scope limits or caveats for interpreting its empirical claims. | 3 matches on pages [10] | [event 10](trace.jsonl#L10) |
| 3 | submit_review `{"review": {"score": 0.74, "observations": 3}}` | Evidence covers the paper's core proposed framework, benchmark claim, and an explicit limitation; submit a bounded independent assessment. | review accepted | [event 16](trace.jsonl#L16) |
