# Experiment results

Open a task to read its review, decisions, tool outcomes, and optional evidence audit. [Settings](experiment.json) · [Evaluated source](source.zip)

Completion means the workflow returned an accepted review. The agent also blocks invalid citations; the one-call baseline does not. Verified citations match source text, not necessarily the meaning of a claim. Summary rates include failed attempts.

An evidence audit is a separate model judgment of claim support; supported counts are provisional verdicts. A first submission is the review proposed before citation repair.

| Method | Completed | All citations verified | Steps/task | Tools/task | Reads/task | Calls/task | Input tokens/task | Output tokens/task | USD/task | Seconds/task |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| agent | 0/1 | 0/1 | 8.00 | 8.00 | 3.00 | 8.00 | 53859.0 | 2023.0 | $0.002833 | 28.25 |
| baseline | 1/1 | 0/1 | 1.00 | 0.00 | 0.00 | 1.00 | 18064.0 | 621.0 | $0.002568 | 11.03 |
| evidence_memory | 0/1 | 0/1 | 8.00 | 8.00 | 5.00 | 8.00 | 69536.0 | 1583.0 | $0.009458 | 25.63 |
| pyagent_react | 1/1 | 1/1 | 6.00 | 6.00 | 3.00 | 6.00 | 35901.0 | 3108.0 | $0.003004 | 32.58 |

## Repetition variation

Verified success requires both a completed review and all quotations verified. It measures citation compliance, not assessment quality. Every planned attempt, including a failed attempt, stays in the denominator. Model IDs are not pooled.

| Method | Repeat | Completed | Verified success | Calls/task | Tokens/task (in/out) | USD/task | Seconds/task |
|---|---:|---:|---:|---:|---|---:|---:|
| agent | 1 | 0/1 | 0/1 | 8.00 | 53859.0/2023.0 | $0.002833 | 28.25 |
| baseline | 1 | 1/1 | 0/1 | 1.00 | 18064.0/621.0 | $0.002568 | 11.03 |
| evidence_memory | 1 | 0/1 | 0/1 | 8.00 | 69536.0/1583.0 | $0.009458 | 25.63 |
| pyagent_react | 1 | 1/1 | 1/1 | 6.00 | 35901.0/3108.0 | $0.003004 | 32.58 |

### Reliability across repetitions

pass^k estimates success on every one of k independent attempts: mean over papers of C(s,k)/C(n,k), where s is the number of verified successes and n the number of attempts for that paper. It is not success at least once. Independence is an assumption; few repetitions give limited precision.

| Method | Always / sometimes / never verified (papers) | pass^k | Mean absolute score difference within a paper | Score pairs |
|---|---|---|---:|---:|
| agent | 0 / 0 / 1 | k=1: 0.000 | unavailable | 0 |
| baseline | 0 / 0 / 1 | k=1: 0.000 | unavailable | 0 |
| evidence_memory | 0 / 0 / 1 | k=1: 0.000 | unavailable | 0 |
| pyagent_react | 1 / 0 / 0 | k=1: 1.000 | unavailable | 0 |

### Paired differences between methods

Each paper contributes its mean over observed repetitions. Differences are left minus right. The 95% percentile bootstrap intervals resample papers 2,000 times, keeping each paper's repetitions together (seed 20261118). These exploratory intervals describe this convenience sample conditional on the observed repetitions; they do not capture future API model drift. A single paper has no interval. Scores use only completed reviews from papers completed by both methods and are not validated quality labels.

| Pair | Verified success difference (95% interval) | Score difference (95% interval) | Mean absolute task score difference | USD/task difference | Seconds/task difference |
|---|---|---|---:|---:|---:|
| agent − baseline | 0.0000 [unavailable]; n=1 | unavailable | unavailable | 0.0003 [unavailable]; n=1 | 17.2203 [unavailable]; n=1 |
| agent − evidence_memory | 0.0000 [unavailable]; n=1 | unavailable | unavailable | -0.0066 [unavailable]; n=1 | 2.6121 [unavailable]; n=1 |
| agent − pyagent_react | -1.0000 [unavailable]; n=1 | unavailable | unavailable | -0.0002 [unavailable]; n=1 | -4.3360 [unavailable]; n=1 |
| baseline − evidence_memory | 0.0000 [unavailable]; n=1 | unavailable | unavailable | -0.0069 [unavailable]; n=1 | -14.6082 [unavailable]; n=1 |
| baseline − pyagent_react | -1.0000 [unavailable]; n=1 | 0.0100 [unavailable]; n=1 | 0.0100 | -0.0004 [unavailable]; n=1 | -21.5563 [unavailable]; n=1 |
| evidence_memory − pyagent_react | -1.0000 [unavailable]; n=1 | unavailable | unavailable | 0.0065 [unavailable]; n=1 | -6.9481 [unavailable]; n=1 |

### Per-paper consistency

Score spread excludes failed attempts; completion counts retain them. Compare within-paper score variation above with between-method differences before interpreting small gaps.

| Method | Task | Completed / attempts | Verified / attempts | Mean score | Score sample SD | Score range |
|---|---|---:|---:|---:|---:|---|
| agent | T17 | 0/1 | 0/1 | unavailable | unavailable | unavailable |
| baseline | T17 | 1/1 | 0/1 | 0.6900 | unavailable | [0.69, 0.69] |
| evidence_memory | T17 | 0/1 | 0/1 | unavailable | unavailable | unavailable |
| pyagent_react | T17 | 1/1 | 1/1 | 0.6800 | unavailable | [0.68, 0.68] |

## agent

Completed papers are ordered by absolute score, then task ID; errors follow.

| Task | Status | Score | Rejected submissions | First submission verified | Evidence audit | Calls | Tokens (in/out) | USD | Seconds |
|---|---|---:|---:|---|---|---:|---|---:|---:|
| [agent-r1/T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models](agent-r1/T17/README.md) | error | — | 5 | no | not audited | 8 | 53859/2023 | $0.002833 | 28.25 |

## baseline

Completed papers are ordered by absolute score, then task ID; errors follow.

| Task | Status | Score | Rejected submissions | First submission verified | Evidence audit | Calls | Tokens (in/out) | USD | Seconds |
|---|---|---:|---:|---|---|---:|---|---:|---:|
| [baseline-r1/T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models](baseline-r1/T17/README.md) | ok | 0.69 | 0 | no | not audited | 1 | 18064/621 | $0.002568 | 11.03 |

## evidence_memory

Completed papers are ordered by absolute score, then task ID; errors follow.

| Task | Status | Score | Rejected submissions | First submission verified | Evidence audit | Calls | Tokens (in/out) | USD | Seconds |
|---|---|---:|---:|---|---|---:|---|---:|---:|
| [evidence_memory-r1/T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models](evidence_memory-r1/T17/README.md) | error | — | 3 | no | not audited | 8 | 69536/1583 | $0.009458 | 25.63 |

## pyagent_react

Completed papers are ordered by absolute score, then task ID; errors follow.

| Task | Status | Score | Rejected submissions | First submission verified | Evidence audit | Calls | Tokens (in/out) | USD | Seconds |
|---|---|---:|---:|---|---|---:|---|---:|---:|
| [pyagent_react-r1/T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models](pyagent_react-r1/T17/README.md) | ok | 0.68 | 2 | no | not audited | 6 | 35901/3108 | $0.003004 | 32.58 |

Per-task cost/time includes unsuccessful attempts; audit cost is separate.
