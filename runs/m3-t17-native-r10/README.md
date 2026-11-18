# Experiment results

Open a task to read its review, decisions, tool outcomes, and optional evidence audit. [Settings](experiment.json) · [Evaluated source](source.zip)

Completion means the workflow returned an accepted review. The agent also blocks invalid citations; the one-call baseline does not. Verified citations match source text, not necessarily the meaning of a claim. Summary rates include failed attempts.

An evidence audit is a separate model judgment of claim support; supported counts are provisional verdicts. A first submission is the review proposed before citation repair.

| Method | Completed | All citations verified | Steps/task | Tools/task | Reads/task | Calls/task | Input tokens/task | Output tokens/task | USD/task | Seconds/task |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| agent | 7/10 | 7/10 | 7.80 | 7.80 | 4.60 | 7.80 | 52987.4 | 1587.8 | $0.002985 | 19.92 |

## Repetition variation

Verified success requires both a completed review and all quotations verified. It measures citation compliance, not assessment quality. Every planned attempt, including a failed attempt, stays in the denominator. Model IDs are not pooled.

| Method | Repeat | Completed | Verified success | Calls/task | Tokens/task (in/out) | USD/task | Seconds/task |
|---|---:|---:|---:|---:|---|---:|---:|
| agent | 1 | 1/1 | 1/1 | 7.00 | 40321.0/1029.0 | $0.002593 | 14.81 |
| agent | 2 | 0/1 | 0/1 | 8.00 | 60528.0/1854.0 | $0.002756 | 21.83 |
| agent | 3 | 0/1 | 0/1 | 8.00 | 67150.0/1976.0 | $0.003123 | 22.11 |
| agent | 4 | 1/1 | 1/1 | 8.00 | 56044.0/1836.0 | $0.002614 | 21.05 |
| agent | 5 | 0/1 | 0/1 | 8.00 | 50193.0/1458.0 | $0.003011 | 19.68 |
| agent | 6 | 1/1 | 1/1 | 8.00 | 58483.0/1465.0 | $0.003780 | 20.47 |
| agent | 7 | 1/1 | 1/1 | 8.00 | 56658.0/2170.0 | $0.002825 | 23.89 |
| agent | 8 | 1/1 | 1/1 | 8.00 | 51704.0/1526.0 | $0.003359 | 21.34 |
| agent | 9 | 1/1 | 1/1 | 7.00 | 40124.0/1109.0 | $0.002795 | 15.72 |
| agent | 10 | 1/1 | 1/1 | 8.00 | 48669.0/1455.0 | $0.002990 | 18.34 |

### Reliability across repetitions

pass^k estimates success on every one of k independent attempts: mean over papers of C(s,k)/C(n,k), where s is the number of verified successes and n the number of attempts for that paper. It is not success at least once. Independence is an assumption; few repetitions give limited precision.

| Method | Always / sometimes / never verified (papers) | pass^k | Mean absolute score difference within a paper | Score pairs |
|---|---|---|---:|---:|
| agent | 0 / 1 / 0 | k=1: 0.700; k=2: 0.467; k=3: 0.292; k=4: 0.167; k=5: 0.083; k=6: 0.033; k=7: 0.008; k=8: 0.000; k=9: 0.000; k=10: 0.000 | 0.0200 | 21 |

### Paired differences between methods

Each paper contributes its mean over observed repetitions. Differences are left minus right. The 95% percentile bootstrap intervals resample papers 2,000 times, keeping each paper's repetitions together (seed 20261118). These exploratory intervals describe this convenience sample conditional on the observed repetitions; they do not capture future API model drift. A single paper has no interval. Scores use only completed reviews from papers completed by both methods and are not validated quality labels.

| Pair | Verified success difference (95% interval) | Score difference (95% interval) | Mean absolute task score difference | USD/task difference | Seconds/task difference |
|---|---|---|---:|---:|---:|

### Per-paper consistency

Score spread excludes failed attempts; completion counts retain them. Compare within-paper score variation above with between-method differences before interpreting small gaps.

| Method | Task | Completed / attempts | Verified / attempts | Mean score | Score sample SD | Score range |
|---|---|---:|---:|---:|---:|---|
| agent | T17 | 7/10 | 7/10 | 0.7057 | 0.0181 | [0.68, 0.72] |

## agent

Completed papers are ordered by absolute score, then task ID; errors follow.

| Task | Status | Score | Rejected submissions | First submission verified | Evidence audit | Calls | Tokens (in/out) | USD | Seconds |
|---|---|---:|---:|---|---|---:|---|---:|---:|
| [agent-r10/T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models](agent-r10/T17/README.md) | ok | 0.72 | 2 | no | not audited | 8 | 48669/1455 | $0.002990 | 18.34 |
| [agent-r1/T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models](agent-r1/T17/README.md) | ok | 0.72 | 1 | no | not audited | 7 | 40321/1029 | $0.002593 | 14.81 |
| [agent-r8/T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models](agent-r8/T17/README.md) | ok | 0.72 | 2 | no | not audited | 8 | 51704/1526 | $0.003359 | 21.34 |
| [agent-r9/T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models](agent-r9/T17/README.md) | ok | 0.72 | 1 | no | not audited | 7 | 40124/1109 | $0.002795 | 15.72 |
| [agent-r4/T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models](agent-r4/T17/README.md) | ok | 0.69 | 3 | no | not audited | 8 | 56044/1836 | $0.002614 | 21.05 |
| [agent-r6/T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models](agent-r6/T17/README.md) | ok | 0.69 | 2 | no | not audited | 8 | 58483/1465 | $0.003780 | 20.47 |
| [agent-r7/T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models](agent-r7/T17/README.md) | ok | 0.68 | 3 | no | not audited | 8 | 56658/2170 | $0.002825 | 23.89 |
| [agent-r2/T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models](agent-r2/T17/README.md) | error | — | 4 | no | not audited | 8 | 60528/1854 | $0.002756 | 21.83 |
| [agent-r3/T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models](agent-r3/T17/README.md) | error | — | 4 | no | not audited | 8 | 67150/1976 | $0.003123 | 22.11 |
| [agent-r5/T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models](agent-r5/T17/README.md) | error | — | 3 | no | not audited | 8 | 50193/1458 | $0.003011 | 19.68 |

Per-task cost/time includes unsuccessful attempts; audit cost is separate.
