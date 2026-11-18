# Experiment results

Open a task to read its review, decisions, tool outcomes, and optional evidence audit. [Settings](experiment.json) · [Evaluated source](source.zip)

Completion means the workflow returned an accepted review. The agent also blocks invalid citations; the one-call baseline does not. Verified citations match source text, not necessarily the meaning of a claim. Summary rates include failed attempts.

An evidence audit is a separate model judgment of claim support; supported counts are provisional verdicts. A first submission is the review proposed before citation repair.

| Method | Completed | All citations verified | Steps/task | Tools/task | Reads/task | Calls/task | Input tokens/task | Output tokens/task | USD/task | Seconds/task |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| deliberative_review | 20/20 | 20/20 | 7.50 | 4.65 | 3.20 | 7.50 | 48172.1 | 3185.5 | $0.007604 | 42.10 |

## Repetition variation

Verified success requires both a completed review and all quotations verified. It measures citation compliance, not assessment quality. Every planned attempt, including a failed attempt, stays in the denominator. Model IDs are not pooled.

| Method | Repeat | Completed | Verified success | Calls/task | Tokens/task (in/out) | USD/task | Seconds/task |
|---|---:|---:|---:|---:|---|---:|---:|
| deliberative_review | 1 | 20/20 | 20/20 | 7.50 | 48172.1/3185.5 | $0.007604 | 42.10 |

### Reliability across repetitions

pass^k estimates success on every one of k independent attempts: mean over papers of C(s,k)/C(n,k), where s is the number of verified successes and n the number of attempts for that paper. It is not success at least once. Independence is an assumption; few repetitions give limited precision.

| Method | Always / sometimes / never verified (papers) | pass^k | Mean absolute score difference within a paper | Score pairs |
|---|---|---|---:|---:|
| deliberative_review | 20 / 0 / 0 | k=1: 1.000 | unavailable | 0 |

### Paired differences between methods

Each paper contributes its mean over observed repetitions. Differences are left minus right. The 95% percentile bootstrap intervals resample papers 2,000 times, keeping each paper's repetitions together (seed 20261118). These exploratory intervals describe this convenience sample conditional on the observed repetitions; they do not capture future API model drift. A single paper has no interval. Scores use only completed reviews from papers completed by both methods and are not validated quality labels.

| Pair | Verified success difference (95% interval) | Score difference (95% interval) | Mean absolute task score difference | USD/task difference | Seconds/task difference |
|---|---|---|---:|---:|---:|

### Per-paper consistency

Score spread excludes failed attempts; completion counts retain them. Compare within-paper score variation above with between-method differences before interpreting small gaps.

| Method | Task | Completed / attempts | Verified / attempts | Mean score | Score sample SD | Score range |
|---|---|---:|---:|---:|---:|---|
| deliberative_review | T01 | 1/1 | 1/1 | 0.6600 | unavailable | [0.66, 0.66] |
| deliberative_review | T02 | 1/1 | 1/1 | 0.6500 | unavailable | [0.65, 0.65] |
| deliberative_review | T03 | 1/1 | 1/1 | 0.6800 | unavailable | [0.68, 0.68] |
| deliberative_review | T04 | 1/1 | 1/1 | 0.7100 | unavailable | [0.71, 0.71] |
| deliberative_review | T05 | 1/1 | 1/1 | 0.6700 | unavailable | [0.67, 0.67] |
| deliberative_review | T06 | 1/1 | 1/1 | 0.7300 | unavailable | [0.73, 0.73] |
| deliberative_review | T07 | 1/1 | 1/1 | 0.6800 | unavailable | [0.68, 0.68] |
| deliberative_review | T08 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |
| deliberative_review | T09 | 1/1 | 1/1 | 0.6800 | unavailable | [0.68, 0.68] |
| deliberative_review | T10 | 1/1 | 1/1 | 0.7600 | unavailable | [0.76, 0.76] |
| deliberative_review | T11 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |
| deliberative_review | T12 | 1/1 | 1/1 | 0.7300 | unavailable | [0.73, 0.73] |
| deliberative_review | T13 | 1/1 | 1/1 | 0.7500 | unavailable | [0.75, 0.75] |
| deliberative_review | T14 | 1/1 | 1/1 | 0.7500 | unavailable | [0.75, 0.75] |
| deliberative_review | T15 | 1/1 | 1/1 | 0.6800 | unavailable | [0.68, 0.68] |
| deliberative_review | T16 | 1/1 | 1/1 | 0.5600 | unavailable | [0.56, 0.56] |
| deliberative_review | T17 | 1/1 | 1/1 | 0.7000 | unavailable | [0.7, 0.7] |
| deliberative_review | T18 | 1/1 | 1/1 | 0.6800 | unavailable | [0.68, 0.68] |
| deliberative_review | T19 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |
| deliberative_review | T20 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |

## deliberative_review

Completed papers are ordered by absolute score, then task ID; errors follow.

| Task | Status | Score | Rejected submissions | First submission verified | Evidence audit | Calls | Tokens (in/out) | USD | Seconds |
|---|---|---:|---:|---|---|---:|---|---:|---:|
| [deliberative_review-r1/T10: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](deliberative_review-r1/T10/README.md) | ok | 0.76 | 0 | yes | not audited | 8 | 52028/3301 | $0.008141 | 36.36 |
| [deliberative_review-r1/T13: Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](deliberative_review-r1/T13/README.md) | ok | 0.75 | 0 | yes | not audited | 6 | 43399/1885 | $0.006358 | 24.96 |
| [deliberative_review-r1/T14: RULER: What's the Real Context Size of Your Long-Context Language Models?](deliberative_review-r1/T14/README.md) | ok | 0.75 | 0 | yes | not audited | 6 | 41390/1718 | $0.006023 | 24.28 |
| [deliberative_review-r1/T06: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](deliberative_review-r1/T06/README.md) | ok | 0.73 | 0 | yes | not audited | 7 | 40941/3188 | $0.006702 | 68.49 |
| [deliberative_review-r1/T12: InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback](deliberative_review-r1/T12/README.md) | ok | 0.73 | 0 | yes | not audited | 7 | 51971/2900 | $0.007937 | 115.50 |
| [deliberative_review-r1/T08: $\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains](deliberative_review-r1/T08/README.md) | ok | 0.72 | 0 | yes | not audited | 7 | 53270/3133 | $0.008215 | 33.15 |
| [deliberative_review-r1/T11: Executable Code Actions Elicit Better LLM Agents](deliberative_review-r1/T11/README.md) | ok | 0.72 | 0 | yes | not audited | 7 | 75914/2916 | $0.010938 | 32.37 |
| [deliberative_review-r1/T19: A Survey on Large Language Model based Autonomous Agents](deliberative_review-r1/T19/README.md) | ok | 0.72 | 0 | yes | not audited | 7 | 43781/3235 | $0.007080 | 34.59 |
| [deliberative_review-r1/T20: RAFT: Adapting Language Model to Domain Specific RAG](deliberative_review-r1/T20/README.md) | ok | 0.72 | 0 | yes | not audited | 7 | 70547/2940 | $0.010279 | 35.05 |
| [deliberative_review-r1/T04: AgentBench: Evaluating LLMs as Agents](deliberative_review-r1/T04/README.md) | ok | 0.71 | 0 | yes | not audited | 8 | 35691/2765 | $0.005831 | 37.44 |
| [deliberative_review-r1/T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models](deliberative_review-r1/T17/README.md) | ok | 0.7 | 10 | no | not audited | 17 | 142616/12175 | $0.023904 | 107.29 |
| [deliberative_review-r1/T03: AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation Framework](deliberative_review-r1/T03/README.md) | ok | 0.68 | 0 | yes | not audited | 7 | 39367/3081 | $0.006452 | 36.11 |
| [deliberative_review-r1/T07: OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](deliberative_review-r1/T07/README.md) | ok | 0.68 | 0 | yes | not audited | 7 | 34941/2776 | $0.005746 | 30.24 |
| [deliberative_review-r1/T09: Agentless: Demystifying LLM-based Software Engineering Agents](deliberative_review-r1/T09/README.md) | ok | 0.68 | 0 | yes | not audited | 6 | 32100/1851 | $0.004928 | 41.33 |
| [deliberative_review-r1/T15: Code Generation with AlphaCodium: From Prompt Engineering to Flow Engineering](deliberative_review-r1/T15/README.md) | ok | 0.68 | 0 | yes | not audited | 7 | 54170/3029 | $0.008276 | 35.45 |
| [deliberative_review-r1/T18: Gorilla: Large Language Model Connected with Massive APIs](deliberative_review-r1/T18/README.md) | ok | 0.68 | 0 | yes | not audited | 6 | 28145/1885 | $0.004451 | 25.62 |
| [deliberative_review-r1/T05: WebArena: A Realistic Web Environment for Building Autonomous Agents](deliberative_review-r1/T05/README.md) | ok | 0.67 | 0 | yes | not audited | 7 | 26979/2838 | $0.004782 | 29.70 |
| [deliberative_review-r1/T01: ReAct: Synergizing Reasoning and Acting in Language Models](deliberative_review-r1/T01/README.md) | ok | 0.66 | 0 | yes | not audited | 8 | 24171/2794 | $0.004405 | 31.58 |
| [deliberative_review-r1/T02: Reflexion: an autonomous agent with dynamic memory and self-reflection](deliberative_review-r1/T02/README.md) | ok | 0.65 | 0 | yes | not audited | 7 | 25548/2701 | $0.004534 | 33.02 |
| [deliberative_review-r1/T16: CAMEL: Communicative Agents for "Mind" Exploration of Large Scale Language Model Society](deliberative_review-r1/T16/README.md) | ok | 0.56 | 0 | yes | not audited | 8 | 46472/2599 | $0.007096 | 29.42 |

Per-task cost/time includes unsuccessful attempts; audit cost is separate.
