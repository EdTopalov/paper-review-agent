# T10: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering

**pyagent_react · ok**

4 model calls · 2 reads · 16.01 s · $0.002572

4 decisions · 4 tool calls · 25619 input tokens (11327 cached) · 1345 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

SWE-agent argues that language-model agents benefit from an interface designed for agent interaction rather than a human-oriented shell. It introduces specialized search, file viewing and editing, and context management, and reports improved SWE-bench performance alongside interface ablations. The benchmark results and behavioral analysis support a substantial, practically relevant contribution, though the inspected evidence leaves questions about generality and the influence of development-set design choices.

- **strength**: The paper reports strong results over the listed baselines on the full benchmark, with a second model and Lite-split results also reported.
  - Page 5 · citation: whitespace
  - Quote: "SWE-agent with GPT-4 Turbo yields the best performance, solving 12.47% (286/2,294) of the full SWE-bench test set and 18.00% (54/300) of the Lite split."

- **strength**: Interface ablations provide evidence that specific interface choices affect task performance.
  - Page 7 · citation: whitespace
  - Quote: "Without SWE-agent’s file editor interface, performance drops to (10.3% ↓ 7.7)."

- **limitation**: The final interface design was informed by qualitative analysis on a small, selected set of easier development examples; this is a potential selection concern, not proof that the evaluation is invalid.
  - Page 5 · citation: whitespace
  - Quote: "we arrived at the final ACI design through qualitative analysis of system behavior on small set of hand-picked easier examples from the development split of SWE-bench."

- **uncertainty**: The inspected experiments focus on two leading models. Although additional models were tried, the extent of their results is not reported in this passage, leaving generality unresolved.
  - Page 5 · citation: whitespace
  - Quote: "We experimented with a number of additional closed and open source models, including Llama 3 and DeepSeek Coder, but found their performance in the agent setting to be subpar."

Unresolved questions:

- How well does the interface approach generalize to other model families and smaller context windows?
- How sensitive are results to the hand-picked examples used during interface design and to different repositories or task distributions?
- I inspected the abstract and pages 5–7 and 15–16, not the complete paper; detailed failure analyses, other experiments, and implementation discussion elsewhere remain unassessed.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 5, "end": 7}` | Inspect benchmark results and the ACI comparison evidence. | read pages [5, 6, 7] | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 15, "end": 16}` | Inspect the paper’s stated limitations and concluding claims. | read pages [15, 16] | [event 11](trace.jsonl#L11) |
| 3 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Submit a balanced assessment based on the inspected abstract, results, interface analysis, and appendix pages. | citation_validation_failed; #4: not_found | [event 17](trace.jsonl#L17) |
| 4 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Correct the citation that did not match by using an exact quote observed on page 5. | review accepted | [event 23](trace.jsonl#L23) |
