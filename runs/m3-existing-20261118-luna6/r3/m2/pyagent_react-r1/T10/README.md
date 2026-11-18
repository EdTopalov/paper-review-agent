# T10: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering

**pyagent_react · ok**

5 model calls · 3 reads · 11.78 s · $0.001866

5 decisions · 4 tool calls · 31530 input tokens (20970 cached) · 673 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.75

SWE-agent argues that language-model agents benefit substantially from interfaces designed around their interaction needs, and implements that claim in a repository-level software engineering agent. It reports strong SWE-bench performance and ablations indicating that editing, search, feedback, and context choices materially affect results. The work is a useful empirical demonstration and design framework, though the inspected evidence is chiefly benchmark- and configuration-specific.

- **strength**: The paper gives an explicit, practical rationale for the interface: tools should be easy to use, efficient, informative, and guard against error propagation.
  - Page 3 · citation: exact
  - Quote: "Environment feedback should be informative."

- **strength**: On the reported benchmark, SWE-agent with GPT-4 Turbo resolves substantially more issues than the listed RAG baselines, with a Claude 3 Opus result also reported.
  - Page 6 · citation: exact
  - Quote: "w/ GPT-4 Turbo 12.47 1.59 18.00 1.67"

- **strength**: The Lite-set ablations support the claim that interface choices matter: removing linting, changing viewer size, or using iterative search reduces resolution in reported comparisons.
  - Page 7 · citation: exact
  - Quote: "Without Linting, 15.0% ↓ 3.0"

- **limitation**: The paper reports that agents often persist with a narrow edit-and-test pattern and may not recognize dead ends, a meaningful limitation in problem-solving behavior.
  - Page 8 · citation: whitespace
  - Quote: "they rarely recognize dead ends or reset their problem solving approach."

Unresolved questions:

- How robust are these gains across other language models, repository collections, and evaluation settings beyond the reported SWE-bench configurations?
- How much of the full benchmark improvement is attributable to each interface component, given that the detailed ablations are on the Lite subset?
- I inspected the opening, interface-design pages, selected results and analysis pages, and related-work/discussion excerpts—not the complete paper, appendices, or all experimental details. Further scrutiny of implementation, statistical variability, and evaluation protocols could change the assessment.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | no_tool_call invalid arguments: `` |  | no_tool_call | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 2, "end": 4}` | Inspect the interface design and methodological claims. | read pages [2, 3, 4] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 8, "end": 10}` | Review benchmark results and interface ablations. | read pages [8, 9, 10] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 6, "end": 7}` | Check main evaluation and ablation evidence. | read pages [6, 7] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.75, "observations": 4}}` | Evidence covers interface design, benchmark results, ablations, and observed behavior; remaining scope limits are noted. | review accepted | [event 25](trace.jsonl#L25) |
