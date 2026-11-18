# T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models

**pyagent_react · ok**

6 model calls · 3 reads · 17.91 s · $0.002021

6 decisions · 5 tool calls · 38826 input tokens (30398 cached) · 1328 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.69

The paper proposes zero-shot Plan-and-Solve prompting: ask an LLM to devise a plan, carry it out, and, in PS+, extract relevant variables and calculate intermediate results. Across ten reasoning datasets, it reports improvements over Zero-shot-CoT, with PS+ competitive with few-shot CoT on arithmetic tasks. This is a useful, simple prompting contribution with evidence across several task types, but the inspected experiments use GPT-3 and the paper acknowledges prompt-design sensitivity and persistent semantic errors.

- **strength**: The method is clearly specified as a two-stage prompting approach: planning and solving, followed by answer extraction.
  - Page 3 · citation: whitespace
  - Quote: "Our Zero-shot PS prompting method instead includes the instructions “ devise a plan ” and “ carry out the plan ”"

- **strength**: The reported arithmetic results show PS+ above Zero-shot-CoT on all six listed datasets, though not uniformly above other baselines.
  - Page 6 · citation: exact
  - Quote: "PS+ (ours) 91.8 59.3 92.2 46.0 94.7 75.7 76.7"

- **limitation**: The authors identify semantic misunderstanding as an error type their approach does not resolve; this is a stated scope limitation, not evidence that the entire approach fails.
  - Page 9 · citation: exact
  - Quote: "the semantic misunderstanding er-\nrors are still remain."

- **uncertainty**: The inspected implementation uses GPT-3; transfer of the results to other model families is unanswered in the inspected material.
  - Page 5 · citation: whitespace
  - Quote: "we use the public GPT-3 (Brown et al., 2020) (175B) as the backbone language model"

Unresolved questions:

- How well does PS/PS+ transfer to other model families and model sizes?
- How sensitive are the reported gains to alternative prompt wording, beyond the prompt variations shown?
- I inspected pages 3–9, including the main results and stated limitations, but not the full appendix or remaining pages; details there could qualify this assessment.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | no_tool_call invalid arguments: `` |  | no_tool_call | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 3, "end": 5}` | Inspect the proposed prompting method and experimental design. | read pages [3, 4, 5] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 6, "end": 8}` | Inspect comparative results and any reported error analysis. | read pages [6, 7, 8] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 9, "end": 9}` | Inspect the conclusion for scope boundaries and acknowledged limitations. | read pages [9] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.69, "observations": 4}}` | Submit an evidence-based assessment using the inspected method, results, and limitations pages. | citation_validation_failed; #3: hyphenation_ambiguous (pages [9]) | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.69, "observations": 4}}` | Resubmit with the limitation quote copied with its page's line-break hyphenation. | review accepted | [event 30](trace.jsonl#L30) |
