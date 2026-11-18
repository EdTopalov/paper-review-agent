# T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models

**baseline · ok**

1 model calls · 0 reads · 8.35 s · $0.000528

1 decisions · 0 tool calls · 18064 input tokens (18061 cached) · 694 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.71

The paper proposes zero-shot Plan-and-Solve (PS) prompting, which asks an LLM to devise and execute a plan, and PS+, which adds instructions such as extracting variables and calculating intermediate results. On ten reasoning datasets using GPT-3, the reported results generally improve on Zero-shot-CoT, with PS+ approaching few-shot CoT on the arithmetic benchmarks. The evidence is useful across several task types, though it is limited to one model family and the reported experiments do not establish how robust the gains are to prompt or run variation. Assessment is based on the supplied pages 1–24.

- **strength**: The evaluation spans ten datasets across arithmetic, commonsense, and symbolic reasoning, and reports comparisons with zero-shot and few-shot prompting baselines.
  - Page 2 · citation: whitespace
  - Quote: "We evaluate our proposed prompting on six math reasoning datasets"

- **strength**: The reported arithmetic results show PS+ outperforming Zero-shot-CoT on all six listed datasets, and the paper reports a higher average than the few-shot baselines shown.
  - Page 6 · citation: exact
  - Quote: "PS+ (ours) 91.8 59.3 92.2 46.0 94.7 75.7 76.7"

- **limitation**: The authors explicitly identify semantic misunderstanding as an error category that their prompting method does not resolve.
  - Page 9 · citation: hyphenation_ambiguous
  - Quote: "the semantic misunderstanding errors are still remain."

- **uncertainty**: The main comparison reports a single GPT-3 setup and accuracy values, without uncertainty estimates in the supplied results; the stability and statistical significance of the gains therefore remain unclear.
  - Page 5 · citation: hyphenation_ambiguous
  - Quote: "We set the temperature to 0 (argmax sampling) throughout our experiments"

Unresolved questions:

- Do the reported gains persist across repeated runs, model families, or newer LLMs, and how large are the associated uncertainties?
- How much of PS+’s benefit comes from planning specifically versus its added variable-extraction and calculation instructions?
- Can a prompting approach reduce semantic misunderstanding errors, which the paper identifies as persisting?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
