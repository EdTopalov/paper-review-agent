# T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models

**agent · ok**

7 model calls · 5 reads · 14.81 s · $0.002593

7 decisions · 7 tool calls · 40321 input tokens (25561 cached) · 1029 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

The paper proposes zero-shot Plan-and-Solve prompting: first ask an LLM to devise a plan, then execute it, with PS+ adding detailed instructions for variables and intermediate calculations. On ten reasoning datasets evaluated with GPT-3 text-davinci-003, it reports broad gains over Zero-shot-CoT, especially on math, while acknowledging prompt sensitivity and persistent semantic misunderstanding errors.

- **strength**: Across the six math datasets, PS+ improves aggregate accuracy over Zero-shot-CoT and is competitive with manual few-shot CoT; results also show gains on commonsense and symbolic tasks.
  - Page 6 · citation: exact
  - Quote: "PS+ (ours) 91.8 59.3 92.2 46.0 94.7 75.7 76.7"

- **strength**: The authors analyze error categories and report reduced calculation and missing-step error proportions for PS+ on their sampled GSM8K examples.
  - Page 7 · citation: exact
  - Quote: "Zero-shot-PS+ 5% 7% 27%"

- **limitation**: The authors explicitly state that prompt formulation takes effort and that semantic misunderstanding remains unaddressed.
  - Page 9 · citation: whitespace
  - Quote: "We will explore how to ad- dress semantic misunderstanding errors by prompt- ing instead of upgrading LLMs in the future."

- **uncertainty**: Evidence inspected is concentrated in the main results, one error analysis, and the limitations section; broader model and prompt robustness is not established by these passages.
  - Page 5 · citation: whitespace
  - Quote: "we use the public GPT-3 (Brown et al., 2020) (175B) as the backbone language model"

Unresolved questions:

- How well does the approach transfer to other model families, model scales, and prompt formulations?
- How stable are the reported gains across repeated runs or samples, particularly beyond the evaluated configuration?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "Experimental Results"}` | Locate evaluation results to assess empirical support and scope. | 1 matches on pages [5] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 5, "end": 7}` | Inspect tables and experimental setup for results and evaluation details. | read pages [5, 6, 7] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 11, "end": 12}` | Inspect stated limitations and discussion to identify scope boundaries and caveats. | read pages [11, 12] | [event 15](trace.jsonl#L15) |
| 4 | search_paper `{"query": "limitations"}` | Check whether the paper explicitly discusses limitations or scope caveats. | 2 matches on pages [9] | [event 20](trace.jsonl#L20) |
| 5 | read_pages `{"start": 9, "end": 9}` | Read the complete limitations section for accurate treatment of stated weaknesses. | read pages [9] | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Evidence spans method performance, error analysis, and explicit limitations; submit concise assessment with inspected-page caveat. | citation_validation_failed; #3: hyphenation_ambiguous (pages [9]) | [event 31](trace.jsonl#L31) |
| 7 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Resubmit after replacing the ambiguous hyphenated limitation quote with an exact quote from inspected page 9. | review accepted | [event 37](trace.jsonl#L37) |
