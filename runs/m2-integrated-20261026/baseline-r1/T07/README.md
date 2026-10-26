# T07: OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments

**baseline · ok**

1 model calls · 0 reads · 7.62 s · $0.005099

[Structured trace](trace.jsonl). Model request inputs store only new messages; `paper_review.trace.read_events` reconstructs complete requests.

## Review · score 0.76

OSWorld contributes an executable, VM-based desktop-computer environment and a 369-task Ubuntu benchmark with task-specific initial-state setup and execution-based evaluation, plus a smaller Windows task set. Its baseline study documents a large gap between tested LLM/VLM agents and human participants and analyzes grounding, history, resolution, and interface perturbations. The work’s strongest value is its practical benchmark infrastructure and breadth; its evidence is bounded by the task set, implementation choices, and reported baseline setup.

- **strength**: The benchmark combines realistic interactive tasks, configurable intermediate states, and per-task execution checks rather than relying only on static demonstrations.
  - Page 7 · citation: not_found
  - Quote: "each example is carefully annotated with a natural language instruction, a setup configuration with corresponding files and setup actions for initialization of initial states upon our provided VM image, and a manually crafted evaluation script"

- **strength**: The paper reports both human and model results, giving a useful reference point for the benchmark’s difficulty and exposing a substantial performance gap in the tested settings.
  - Page 9 · citation: whitespace
  - Quote: "the human performance on our tasks was approximately 72.36%"

- **limitation**: The authors explicitly recognize that evaluation scripts may still produce false positives or negatives; this is a meaningful reliability caveat for execution-based scoring, not evidence that all scores are invalid.
  - Page 8 · citation: whitespace
  - Quote: "Further investment of time and a more red teaming could further reduce false positives and negatives, which we will leave to future work."

- **uncertainty**: The main benchmark is Ubuntu-centered, while the Windows set is smaller and macOS is discussed as supported by the environment rather than included in the principal benchmark evaluation. How well the reported results generalize across operating systems and broader software ecosystems remains open.
  - Page 26 · citation: whitespace
  - Quote: "we select Ubuntu, the most representative Linux desktop OS, as the foundation for the main part of our benchmark intended for public use."

Unresolved questions:

- How robust are task-specific evaluators to valid alternative outcomes, edge cases, and unintended side effects beyond the checks described?
- How representative are the selected applications and 369 tasks of computer-use needs outside the Ubuntu software and task sources used here?
- Would the agent-versus-human conclusions persist under different prompt/action interfaces, longer horizons, or newer model versions?
- I inspected the supplied pages, including benchmark methods, results, limitations, and appendices; I did not independently run the environment or verify the implementation, data, or evaluation scripts.

## Evidence audit

Provisional model judgments, not human-validated accuracy.

- Observation 1: **supported** — The paper says tasks have natural-language instructions, initial-state setup configurations, and manually crafted execution scripts (PDF pp. 7–8); it also describes intermediate states and execution-based checks (pp. 4–5).
- Observation 2: **supported** — Human performance is reported as approximately 72.36%, alongside model results, and the paper explicitly contrasts this with much lower baseline performance (PDF pp. 9–11).
- Observation 3: **supported** — The authors report further red-teaming could reduce false positives and negatives and defer that work, while describing multiple rounds of quality checks (PDF pp. 7–8). The claim appropriately presents this as a caveat rather than invalidating all scores.
- Observation 4: **supported** — The 369-task public benchmark is Ubuntu-based; the paper provides a smaller 43-task Windows set, and says macOS was not used for benchmark development due to copyright concerns (PDF pp. 6, 26–27). The stated generalization question is appropriately unresolved.

## Decisions

Expand a step for its arguments and observation. Long observations are previews; the structured trace retains complete text.

### Step 1: final_answer

Returned the final assessment.

[Event 5](trace.jsonl#L5)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": "{\"score\":0.76,\"summary\":\"OSWorld contributes an executable, VM-based desktop-computer environment and a 369-task Ubuntu benchmark with task-specific initial-state setup and execution-based evaluation, plus a smaller Windows task set. Its baseline study documents a large gap between tested LLM/VLM agents and human participants and analyzes grounding, history, resolution, and interface perturbations. The work’s strongest value is its practical benchmark infrastructure and breadth; its evidence is bounded by the task set, implementation choices, and reported baseline setup.\",\"observations\":[{\"kind\":\"strength\",\"claim\":\"The benchmark combines realistic interactive tasks, configurable intermediate states, and per-task execution checks rather than relying only on static demonstrations.\",\"page\":7,\"quote\":\"each example is carefully annotated with a natural language instruction, a setup configuration with corresponding files and setup actions for initialization of initial states upon our provided VM image, and a manually crafted evaluation script\"},{\"kind\":\"strength\",\"claim\":\"The paper reports both human and model results, giving a useful reference point for the benchmark’s difficulty and exposing a substantial performance gap in the tested settings.\",\"page\":9,\"quote\":\"the human performance on our tasks was approximately 72.36%\"},{\"kind\":\"limitation\",\"claim\":\"The authors explicitly recognize that evaluation scripts may still produce false positives or negatives; this is a meaningful reliability caveat for execution-based scoring, not evidence that all scores are invalid.\",\"page\":8,\"quote\":\"Further investment of time and a more red teaming could further reduce false positives and negatives, which we will leave to future work.\"},{\"kind\":\"uncertainty\",\"claim\":\"The main benchmark is Ubuntu-centered, while the Windows set is smaller and macOS is discussed as supported by the environment rather than included in the principal benchmark evaluation. How well the reported results generalize across operating systems and broader software ecosystems remains open.\",\"page\":26,\"quote\":\"we select Ubuntu, the most representative Linux desktop OS, as the foundation for the main part of our benchmark intended for public use.\"}],\"unresolved_questions\":[\"How robust are task-specific evaluators to valid alternative outcomes, edge cases, and unintended side effects beyond the checks described?\",\"How representative are the selected applications and 369 tasks of computer-use needs outside the Ubuntu software and task sources used here?\",\"Would the agent-versus-human conclusions persist under different prompt/action interfaces, longer horizons, or newer model versions?\",\"I inspected the supplied pages, including benchmark methods, results, limitations, and appendices; I did not independently run the environment or verify the implementation, data, or evaluation scripts.\"]}",
  "observation": {}
}
```

</details>
