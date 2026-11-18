# Experiment results

Open a task to read its review, decisions, tool outcomes, and optional evidence audit. [Settings](experiment.json) · [Evaluated source](source.zip)

Completion means the workflow returned an accepted review. The agent also blocks invalid citations; the one-call baseline does not. Verified citations match source text, not necessarily the meaning of a claim. Summary rates include failed attempts.

An evidence audit is a separate model judgment of claim support; supported counts are provisional verdicts. A first submission is the review proposed before citation repair.

| Method | Completed | All citations verified | Steps/task | Tools/task | Reads/task | Calls/task | Input tokens/task | Output tokens/task | USD/task | Seconds/task |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| deliberative_review | 20/20 | 20/20 | 7.80 | 4.70 | 3.30 | 7.80 | 42081.3 | 3404.7 | $0.006799 | 36.66 |

## Repetition variation

Verified success requires both a completed review and all quotations verified. It measures citation compliance, not assessment quality. Every planned attempt, including a failed attempt, stays in the denominator. Model IDs are not pooled.

| Method | Repeat | Completed | Verified success | Calls/task | Tokens/task (in/out) | USD/task | Seconds/task |
|---|---:|---:|---:|---:|---|---:|---:|
| deliberative_review | 1 | 20/20 | 20/20 | 7.80 | 42081.3/3404.7 | $0.006799 | 36.66 |

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
| deliberative_review | T01 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |
| deliberative_review | T02 | 1/1 | 1/1 | 0.6800 | unavailable | [0.68, 0.68] |
| deliberative_review | T03 | 1/1 | 1/1 | 0.6500 | unavailable | [0.65, 0.65] |
| deliberative_review | T04 | 1/1 | 1/1 | 0.4800 | unavailable | [0.48, 0.48] |
| deliberative_review | T05 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |
| deliberative_review | T06 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |
| deliberative_review | T07 | 1/1 | 1/1 | 0.7100 | unavailable | [0.71, 0.71] |
| deliberative_review | T08 | 1/1 | 1/1 | 0.7400 | unavailable | [0.74, 0.74] |
| deliberative_review | T09 | 1/1 | 1/1 | 0.6800 | unavailable | [0.68, 0.68] |
| deliberative_review | T10 | 1/1 | 1/1 | 0.7400 | unavailable | [0.74, 0.74] |
| deliberative_review | T11 | 1/1 | 1/1 | 0.6800 | unavailable | [0.68, 0.68] |
| deliberative_review | T12 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |
| deliberative_review | T13 | 1/1 | 1/1 | 0.7800 | unavailable | [0.78, 0.78] |
| deliberative_review | T14 | 1/1 | 1/1 | 0.5800 | unavailable | [0.58, 0.58] |
| deliberative_review | T15 | 1/1 | 1/1 | 0.7300 | unavailable | [0.73, 0.73] |
| deliberative_review | T16 | 1/1 | 1/1 | 0.5000 | unavailable | [0.5, 0.5] |
| deliberative_review | T17 | 1/1 | 1/1 | 0.6200 | unavailable | [0.62, 0.62] |
| deliberative_review | T18 | 1/1 | 1/1 | 0.6800 | unavailable | [0.68, 0.68] |
| deliberative_review | T19 | 1/1 | 1/1 | 0.6600 | unavailable | [0.66, 0.66] |
| deliberative_review | T20 | 1/1 | 1/1 | 0.7300 | unavailable | [0.73, 0.73] |

## deliberative_review

Completed papers are ordered by absolute score, then task ID; errors follow.

| Task | Status | Score | Rejected submissions | First submission verified | Evidence audit | Calls | Tokens (in/out) | USD | Seconds |
|---|---|---:|---:|---|---|---:|---|---:|---:|
| [deliberative_review-r1/T13: Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](deliberative_review-r1/T13/README.md) | ok | 0.78 | 0 | yes | not audited | 7 | 54772/2889 | $0.008108 | 30.53 |
| [deliberative_review-r1/T08: $\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains](deliberative_review-r1/T08/README.md) | ok | 0.74 | 0 | yes | not audited | 6 | 29977/1765 | $0.004471 | 22.67 |
| [deliberative_review-r1/T10: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](deliberative_review-r1/T10/README.md) | ok | 0.74 | 0 | yes | not audited | 7 | 42331/3284 | $0.006773 | 33.20 |
| [deliberative_review-r1/T15: Code Generation with AlphaCodium: From Prompt Engineering to Flow Engineering](deliberative_review-r1/T15/README.md) | ok | 0.73 | 3 | no | not audited | 11 | 88374/5338 | $0.013524 | 54.20 |
| [deliberative_review-r1/T20: RAFT: Adapting Language Model to Domain Specific RAG](deliberative_review-r1/T20/README.md) | ok | 0.73 | 1 | no | not audited | 8 | 65915/4131 | $0.010113 | 41.47 |
| [deliberative_review-r1/T01: ReAct: Synergizing Reasoning and Acting in Language Models](deliberative_review-r1/T01/README.md) | ok | 0.72 | 0 | yes | not audited | 7 | 40036/3372 | $0.006523 | 35.29 |
| [deliberative_review-r1/T05: WebArena: A Realistic Web Environment for Building Autonomous Agents](deliberative_review-r1/T05/README.md) | ok | 0.72 | 0 | yes | not audited | 7 | 43106/2755 | $0.006614 | 33.10 |
| [deliberative_review-r1/T06: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](deliberative_review-r1/T06/README.md) | ok | 0.72 | 0 | yes | not audited | 7 | 29504/3476 | $0.005252 | 37.57 |
| [deliberative_review-r1/T12: InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback](deliberative_review-r1/T12/README.md) | ok | 0.72 | 0 | yes | not audited | 7 | 41121/2776 | $0.006375 | 29.40 |
| [deliberative_review-r1/T07: OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](deliberative_review-r1/T07/README.md) | ok | 0.71 | 0 | yes | not audited | 8 | 28577/3252 | $0.005031 | 35.40 |
| [deliberative_review-r1/T02: Reflexion: an autonomous agent with dynamic memory and self-reflection](deliberative_review-r1/T02/README.md) | ok | 0.68 | 0 | yes | not audited | 7 | 35670/3169 | $0.005891 | 33.28 |
| [deliberative_review-r1/T09: Agentless: Demystifying LLM-based Software Engineering Agents](deliberative_review-r1/T09/README.md) | ok | 0.68 | 0 | yes | not audited | 7 | 37288/2853 | $0.005931 | 31.69 |
| [deliberative_review-r1/T11: Executable Code Actions Elicit Better LLM Agents](deliberative_review-r1/T11/README.md) | ok | 0.68 | 0 | yes | not audited | 6 | 24097/1630 | $0.003663 | 20.27 |
| [deliberative_review-r1/T18: Gorilla: Large Language Model Connected with Massive APIs](deliberative_review-r1/T18/README.md) | ok | 0.68 | 1 | no | not audited | 11 | 51442/6536 | $0.009535 | 68.02 |
| [deliberative_review-r1/T19: A Survey on Large Language Model based Autonomous Agents](deliberative_review-r1/T19/README.md) | ok | 0.66 | 0 | yes | not audited | 7 | 34686/2789 | $0.005584 | 32.16 |
| [deliberative_review-r1/T03: AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation Framework](deliberative_review-r1/T03/README.md) | ok | 0.65 | 0 | yes | not audited | 7 | 32088/3047 | $0.005404 | 30.62 |
| [deliberative_review-r1/T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models](deliberative_review-r1/T17/README.md) | ok | 0.62 | 1 | no | not audited | 8 | 23566/3610 | $0.004561 | 37.25 |
| [deliberative_review-r1/T14: RULER: What's the Real Context Size of Your Long-Context Language Models?](deliberative_review-r1/T14/README.md) | ok | 0.58 | 0 | yes | not audited | 9 | 50947/3226 | $0.007812 | 35.89 |
| [deliberative_review-r1/T16: CAMEL: Communicative Agents for "Mind" Exploration of Large Scale Language Model Society](deliberative_review-r1/T16/README.md) | ok | 0.5 | 0 | yes | not audited | 9 | 56562/3620 | $0.008732 | 40.42 |
| [deliberative_review-r1/T04: AgentBench: Evaluating LLMs as Agents](deliberative_review-r1/T04/README.md) | ok | 0.48 | 2 | no | not audited | 10 | 31567/4575 | $0.006091 | 50.85 |

Per-task cost/time includes unsuccessful attempts; audit cost is separate.
