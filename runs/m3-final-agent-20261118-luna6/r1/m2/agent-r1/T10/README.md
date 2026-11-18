# T10: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering

**agent · ok**

6 model calls · 4 reads · 16.29 s · $0.001944

6 decisions · 6 tool calls · 28925 input tokens (19756 cached) · 1238 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.74

SWE-agent’s central contribution is to treat the agent-computer interface as a design variable and build LM-oriented repository navigation, editing, feedback, and history tools. On SWE-bench, it reports 12.47% resolution on the full test set and 18% on SWE-bench Lite, with interface ablations showing meaningful differences from less tailored alternatives. This is a substantial, empirically supported systems contribution, bounded by the models and benchmark inspected.

- **strength**: The paper reports benchmark results over the full test set and a separate Lite split.
  - Page 5 · citation: exact
  - Quote: "solving 12.47% (286/2,294) of the full SWE-bench test set and 18.00% (54/300) of the Lite split."

- **strength**: The authors report a substantial improvement over a shell-only baseline, supported by interface ablations.
  - Page 2 · citation: whitespace
  - Quote: "SWE-agent solves 10.7 percentage points more issues than the baseline agent that uses just the default Linux shell."

- **limitation**: The principal analysis is limited to two leading models, so performance across a broader range of model families is not established here.
  - Page 5 · citation: whitespace
  - Quote: "All results, ablations, and analysis are based on two leading LMs, GPT- 4 Turbo ( gpt-4-1106-preview) (OpenAI et al., 2023) and Claude 3 Opus (claude-3-opus-20240229) (Chiang et al., 2024)."

- **uncertainty**: Interface design choices were informed by qualitative analysis of selected easier development examples; I have not inspected the later discussion, appendix, or full limitations, leaving uncertainty about sensitivity to these choices.
  - Page 5 · citation: whitespace
  - Quote: "we arrived at the final ACI design through qualitative analysis of system behavior on small set of hand-picked easier examples from the development split of SWE-bench."

Unresolved questions:

- How robust are the ACI gains across a broader range of open and smaller language models?
- How well do the results transfer beyond the Python repositories and task framing represented in SWE-bench?
- What do the later discussion and appendix establish about failure modes, evaluation variance, and generalization beyond the pages inspected?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "12.5"}` | Locate the paper’s benchmark results and supporting evaluation details. | 2 matches on pages [1, 2] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 2, "end": 3}` | Inspect the system design and experiment setup/results for evidence and scope. | read pages [2, 3] | [event 10](trace.jsonl#L10) |
| 3 | search_paper `{"query": "300"}` | Find ablation table/results to assess how strongly interface claims are tested. | 3 matches on pages [2, 5] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 5, "end": 6}` | Inspect exact full-benchmark and ablation evidence, including evaluation protocol and caveats. | read pages [5, 6] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.74, "observations": 4}}` | Submit an evidence-based assessment from the abstract, design discussion, and results/setup pages inspected. | citation_validation_failed; #3: not_found | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.74, "observations": 4}}` | Correct the unsupported model-scope quote using exact observed wording and resubmit the review. | review accepted | [event 30](trace.jsonl#L30) |
