# T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models

**baseline · ok**

1 model calls · 0 reads · 7.22 s · $0.002584

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.69

The paper proposes Plan-and-Solve prompting, a zero-shot prompting strategy that asks an LLM to devise and execute a plan, with PS+ adding instructions to extract variables and attend to intermediate calculations. Tests on ten datasets report consistent improvements over Zero-shot-CoT, with particularly strong arithmetic results. The contribution is practical and supported by broad benchmark comparisons, though the evidence is limited to one GPT-3 engine and does not establish how reliably the gains generalize.

- **strength**: The evaluation spans arithmetic, commonsense, and symbolic reasoning, and reports gains over Zero-shot-CoT across the tested datasets.
  - Page 2 · citation: whitespace
  - Quote: "We evaluate our proposed prompting on six math reasoning datasets"

- **strength**: The math results show meaningful gains for PS+, including a higher average than the listed zero-shot baselines and Auto-CoT.
  - Page 6 · citation: exact
  - Quote: "PS+ (ours) 91.8 59.3 92.2 46.0 94.7 75.7 76.7"

- **limitation**: The authors explicitly identify prompt design and model sensitivity as a practical constraint on applying the method.
  - Page 9 · citation: whitespace
  - Quote: "The GPT-3 models are sensitive to the expressions in prompts, thus we need to carefully design the prompts."

- **uncertainty**: The reported evidence is specific to text-davinci-003 in the main experiments; whether the gains transfer to other model families remains unresolved.
  - Page 5 · citation: hyphenation_ambiguous
  - Quote: "We report the results using text-davinci-003 engine for GPT-3 in the main paper."

Unresolved questions:

- Do the observed gains persist across other model families, model sizes, and current prompting interfaces?
- How sensitive are results to prompt wording and selection, particularly given the reported prompt sensitivity?
- The inspected pages describe a 100-example error analysis but provide limited detail about annotation reliability; how stable are the reported error-category differences under independent annotation or repeated samples?

## Evidence audit

Provisional model judgments, not human-validated accuracy.

- Observation 1: **supported** — The paper evaluates ten datasets across arithmetic, commonsense, and symbolic reasoning (pp. 2, 4–5). It reports PS+ outperforming Zero-shot-CoT on all ten (pp. 5–6).
- Observation 2: **supported** — Table 2 reports PS+ at a 76.7 average, above the listed Zero-shot-CoT (70.4), PoT (73.5), PS (72.9), and Auto-CoT (75.9) averages (p. 6).
- Observation 3: **supported** — The limitations section explicitly says prompt design takes effort and GPT-3 models are sensitive to prompt expressions, requiring careful design (p. 9).
- Observation 4: **supported** — The main-paper experiments report results using text-davinci-003 (p. 5). The paper does not establish transfer to other model families, so that remains unresolved.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
