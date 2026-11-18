# Trace validation

[Machine-readable checks](checks.json) cover only complete final-policy stage grids.
Checked 37 stages and 1664 terminal attempts: 1630 pass every checker flag, 34 have only intermediate argument flags, and 0 have other checker failures.

Malformed intermediate arguments are recorded protocol errors, including errors followed
by successful recovery. They do not imply corrupt traces or remove terminal attempts.
Model failures remain valid recorded outcomes; completion and content accuracy are separate.

| Stage | Traces | All flags pass | Argument-only flags | Other failures |
|---|---:|---:|---:|---:|---:|
| [runs/m3-final-agent-20261118-luna6/r1/core](../../runs/m3-final-agent-20261118-luna6/r1/core) | 64 | 64 | 0 | 0 |
| [runs/m3-final-agent-20261118-luna6/r1/m2](../../runs/m3-final-agent-20261118-luna6/r1/m2) | 20 | 20 | 0 | 0 |
| [runs/m3-final-agent-20261118-luna6/r1/selection](../../runs/m3-final-agent-20261118-luna6/r1/selection) | 12 | 12 | 0 | 0 |
| [runs/m3-final-agent-20261118-luna6/r2/core](../../runs/m3-final-agent-20261118-luna6/r2/core) | 64 | 64 | 0 | 0 |
| [runs/m3-final-agent-20261118-luna6/r2/m2](../../runs/m3-final-agent-20261118-luna6/r2/m2) | 20 | 20 | 0 | 0 |
| [runs/m3-final-agent-20261118-luna6/r2/selection](../../runs/m3-final-agent-20261118-luna6/r2/selection) | 12 | 12 | 0 | 0 |
| [runs/m3-final-agent-20261118-luna6/r3/core](../../runs/m3-final-agent-20261118-luna6/r3/core) | 64 | 64 | 0 | 0 |
| [runs/m3-final-agent-20261118-luna6/r3/m2](../../runs/m3-final-agent-20261118-luna6/r3/m2) | 20 | 20 | 0 | 0 |
| [runs/m3-final-agent-20261118-luna6/r3/selection](../../runs/m3-final-agent-20261118-luna6/r3/selection) | 12 | 12 | 0 | 0 |
| [runs/m3-final-baseline-recovery-20261118-luna6/r1/core](../../runs/m3-final-baseline-recovery-20261118-luna6/r1/core) | 64 | 64 | 0 | 0 |
| [runs/m3-final-baseline-recovery-20261118-luna6/r1/m2](../../runs/m3-final-baseline-recovery-20261118-luna6/r1/m2) | 20 | 20 | 0 | 0 |
| [runs/m3-final-baseline-recovery-20261118-luna6/r1/selection](../../runs/m3-final-baseline-recovery-20261118-luna6/r1/selection) | 12 | 12 | 0 | 0 |
| [runs/m3-final-baseline-recovery-20261118-luna6/r2/core](../../runs/m3-final-baseline-recovery-20261118-luna6/r2/core) | 64 | 64 | 0 | 0 |
| [runs/m3-final-baseline-recovery-20261118-luna6/r2/m2](../../runs/m3-final-baseline-recovery-20261118-luna6/r2/m2) | 20 | 20 | 0 | 0 |
| [runs/m3-final-baseline-recovery-20261118-luna6/r2/selection](../../runs/m3-final-baseline-recovery-20261118-luna6/r2/selection) | 12 | 12 | 0 | 0 |
| [runs/m3-final-baseline-recovery-20261118-luna6/r3/core](../../runs/m3-final-baseline-recovery-20261118-luna6/r3/core) | 64 | 64 | 0 | 0 |
| [runs/m3-final-baseline-recovery-20261118-luna6/r3/m2](../../runs/m3-final-baseline-recovery-20261118-luna6/r3/m2) | 20 | 20 | 0 | 0 |
| [runs/m3-final-baseline-recovery-20261118-luna6/r3/selection](../../runs/m3-final-baseline-recovery-20261118-luna6/r3/selection) | 12 | 12 | 0 | 0 |
| [runs/m3-final-deliberative_review-20261118-luna6/r1/core](../../runs/m3-final-deliberative_review-20261118-luna6/r1/core) | 64 | 64 | 0 | 0 |
| [runs/m3-final-deliberative_review-20261118-luna6/r1/m2](../../runs/m3-final-deliberative_review-20261118-luna6/r1/m2) | 20 | 20 | 0 | 0 |
| [runs/m3-final-deliberative_review-20261118-luna6/r1/selection](../../runs/m3-final-deliberative_review-20261118-luna6/r1/selection) | 12 | 12 | 0 | 0 |
| [runs/m3-final-deliberative_review-20261118-luna6/r2/core](../../runs/m3-final-deliberative_review-20261118-luna6/r2/core) | 64 | 64 | 0 | 0 |
| [runs/m3-final-deliberative_review-20261118-luna6/r2/m2](../../runs/m3-final-deliberative_review-20261118-luna6/r2/m2) | 20 | 20 | 0 | 0 |
| [runs/m3-final-deliberative_review-20261118-luna6/r2/selection](../../runs/m3-final-deliberative_review-20261118-luna6/r2/selection) | 12 | 12 | 0 | 0 |
| [runs/m3-final-extra-r4-20261118-luna6/r4/core](../../runs/m3-final-extra-r4-20261118-luna6/r4/core) | 256 | 256 | 0 | 0 |
| [runs/m3-final-extra-r4-20261118-luna6/r4/selection](../../runs/m3-final-extra-r4-20261118-luna6/r4/selection) | 48 | 48 | 0 | 0 |
| [runs/m3-final-extra-r5-20261118-luna6/r5/core](../../runs/m3-final-extra-r5-20261118-luna6/r5/core) | 256 | 256 | 0 | 0 |
| [runs/m3-final-extra-r5-20261118-luna6/r5/selection](../../runs/m3-final-extra-r5-20261118-luna6/r5/selection) | 48 | 48 | 0 | 0 |
| [runs/m3-final-pyagent_react-20261118-luna6/r1/core](../../runs/m3-final-pyagent_react-20261118-luna6/r1/core) | 64 | 64 | 0 | 0 |
| [runs/m3-final-pyagent_react-20261118-luna6/r1/m2](../../runs/m3-final-pyagent_react-20261118-luna6/r1/m2) | 20 | 11 | 9 | 0 |
| [runs/m3-final-pyagent_react-20261118-luna6/r1/selection](../../runs/m3-final-pyagent_react-20261118-luna6/r1/selection) | 12 | 12 | 0 | 0 |
| [runs/m3-final-pyagent_react-20261118-luna6/r2/core](../../runs/m3-final-pyagent_react-20261118-luna6/r2/core) | 64 | 64 | 0 | 0 |
| [runs/m3-final-pyagent_react-20261118-luna6/r2/m2](../../runs/m3-final-pyagent_react-20261118-luna6/r2/m2) | 20 | 6 | 14 | 0 |
| [runs/m3-final-pyagent_react-20261118-luna6/r2/selection](../../runs/m3-final-pyagent_react-20261118-luna6/r2/selection) | 12 | 12 | 0 | 0 |
| [runs/m3-final-pyagent_react-20261118-luna6/r3/core](../../runs/m3-final-pyagent_react-20261118-luna6/r3/core) | 64 | 64 | 0 | 0 |
| [runs/m3-final-pyagent_react-20261118-luna6/r3/m2](../../runs/m3-final-pyagent_react-20261118-luna6/r3/m2) | 20 | 9 | 11 | 0 |
| [runs/m3-final-pyagent_react-20261118-luna6/r3/selection](../../runs/m3-final-pyagent_react-20261118-luna6/r3/selection) | 12 | 12 | 0 | 0 |

3 planned stages are incomplete or not yet created and are excluded; 0 validator exceptions remain.

Checks inspect sequence, identity, terminal results, budgets and request/response accounting.
Completed stages are checked once. Reproduce with paper-review check <M2-stage> or:

    python -c "from paper_review.benchmark_runner import check_runs; print(check_runs('runs/m3-final-agent-20261118-luna6/r1/core'))"
