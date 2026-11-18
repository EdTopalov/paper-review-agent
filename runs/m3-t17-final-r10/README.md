# Experiment results

Open a task to read its review, decisions, tool outcomes, and optional evidence audit. [Settings](experiment.json) · [Evaluated source](source.zip)

Completion means the workflow returned an accepted review. The agent also blocks invalid citations; the one-call baseline does not. Verified citations match source text, not necessarily the meaning of a claim. Summary rates include failed attempts.

An evidence audit is a separate model judgment of claim support; supported counts are provisional verdicts. A first submission is the review proposed before citation repair.

| Method | Completed | All citations verified | Steps/task | Tools/task | Reads/task | Calls/task | Input tokens/task | Output tokens/task | USD/task | Seconds/task |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| agent | 10/10 | 10/10 | 10.00 | 10.00 | 4.70 | 10.00 | 86543.9 | 2446.8 | $0.004332 | 29.32 |

## Repetition variation

Verified success requires both a completed review and all quotations verified. It measures citation compliance, not assessment quality. Every planned attempt, including a failed attempt, stays in the denominator. Model IDs are not pooled.

| Method | Repeat | Completed | Verified success | Calls/task | Tokens/task (in/out) | USD/task | Seconds/task |
|---|---:|---:|---:|---:|---|---:|---:|
| agent | 1 | 1/1 | 1/1 | 11.00 | 90286.0/2953.0 | $0.004845 | 34.31 |
| agent | 2 | 1/1 | 1/1 | 11.00 | 85025.0/2776.0 | $0.004569 | 31.87 |
| agent | 3 | 1/1 | 1/1 | 9.00 | 62884.0/2024.0 | $0.004028 | 24.91 |
| agent | 4 | 1/1 | 1/1 | 8.00 | 85398.0/1992.0 | $0.003566 | 21.95 |
| agent | 5 | 1/1 | 1/1 | 15.00 | 159504.0/4486.0 | $0.007091 | 49.86 |
| agent | 6 | 1/1 | 1/1 | 7.00 | 50237.0/1448.0 | $0.002436 | 17.06 |
| agent | 7 | 1/1 | 1/1 | 10.00 | 98422.0/2394.0 | $0.005193 | 30.75 |
| agent | 8 | 1/1 | 1/1 | 11.00 | 83869.0/2300.0 | $0.004020 | 27.98 |
| agent | 9 | 1/1 | 1/1 | 12.00 | 117410.0/3118.0 | $0.005877 | 39.64 |
| agent | 10 | 1/1 | 1/1 | 6.00 | 32404.0/977.0 | $0.001699 | 14.86 |

### Reliability across repetitions

pass^k estimates success on every one of k independent attempts: mean over papers of C(s,k)/C(n,k), where s is the number of verified successes and n the number of attempts for that paper. It is not success at least once. Independence is an assumption; few repetitions give limited precision.

| Method | Always / sometimes / never verified (papers) | pass^k | Mean absolute score difference within a paper | Score pairs |
|---|---|---|---:|---:|
| agent | 1 / 0 / 0 | k=1: 1.000; k=2: 1.000; k=3: 1.000; k=4: 1.000; k=5: 1.000; k=6: 1.000; k=7: 1.000; k=8: 1.000; k=9: 1.000; k=10: 1.000 | 0.0191 | 45 |

### Paired differences between methods

Each paper contributes its mean over observed repetitions. Differences are left minus right. The 95% percentile bootstrap intervals resample papers 2,000 times, keeping each paper's repetitions together (seed 20261118). These exploratory intervals describe this convenience sample conditional on the observed repetitions; they do not capture future API model drift. A single paper has no interval. Scores use only completed reviews from papers completed by both methods and are not validated quality labels.

| Pair | Verified success difference (95% interval) | Score difference (95% interval) | Mean absolute task score difference | USD/task difference | Seconds/task difference |
|---|---|---|---:|---:|---:|

### Per-paper consistency

Score spread excludes failed attempts; completion counts retain them. Compare within-paper score variation above with between-method differences before interpreting small gaps.

| Method | Task | Completed / attempts | Verified / attempts | Mean score | Score sample SD | Score range |
|---|---|---:|---:|---:|---:|---|
| agent | T17 | 10/10 | 10/10 | 0.7140 | 0.0165 | [0.69, 0.74] |

## agent

Completed papers are ordered by absolute score, then task ID; errors follow.

| Task | Status | Score | Rejected submissions | First submission verified | Evidence audit | Calls | Tokens (in/out) | USD | Seconds |
|---|---|---:|---:|---|---|---:|---|---:|---:|
| [agent-r7/T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models](agent-r7/T17/README.md) | ok | 0.74 | 4 | no | not audited | 10 | 98422/2394 | $0.005193 | 30.75 |
| [agent-r3/T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models](agent-r3/T17/README.md) | ok | 0.73 | 3 | no | not audited | 9 | 62884/2024 | $0.004028 | 24.91 |
| [agent-r10/T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models](agent-r10/T17/README.md) | ok | 0.72 | 1 | no | not audited | 6 | 32404/977 | $0.001699 | 14.86 |
| [agent-r2/T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models](agent-r2/T17/README.md) | ok | 0.72 | 5 | no | not audited | 11 | 85025/2776 | $0.004569 | 31.87 |
| [agent-r6/T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models](agent-r6/T17/README.md) | ok | 0.72 | 2 | no | not audited | 7 | 50237/1448 | $0.002436 | 17.06 |
| [agent-r8/T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models](agent-r8/T17/README.md) | ok | 0.72 | 5 | no | not audited | 11 | 83869/2300 | $0.004020 | 27.98 |
| [agent-r5/T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models](agent-r5/T17/README.md) | ok | 0.71 | 9 | no | not audited | 15 | 159504/4486 | $0.007091 | 49.86 |
| [agent-r9/T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models](agent-r9/T17/README.md) | ok | 0.7 | 6 | no | not audited | 12 | 117410/3118 | $0.005877 | 39.64 |
| [agent-r1/T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models](agent-r1/T17/README.md) | ok | 0.69 | 5 | no | not audited | 11 | 90286/2953 | $0.004845 | 34.31 |
| [agent-r4/T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models](agent-r4/T17/README.md) | ok | 0.69 | 3 | no | not audited | 8 | 85398/1992 | $0.003566 | 21.95 |

Per-task cost/time includes unsuccessful attempts; audit cost is separate.
