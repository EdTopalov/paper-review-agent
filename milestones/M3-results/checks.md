# Trace validation

[Machine-readable stage checks](checks.json) distinguish valid recording from
successful model behavior. Sequence, identity, terminal-result, budget, and
request/response accounting checks inspect the saved traces without model calls.

The original review checker also flags malformed intermediate action arguments,
including actions followed by successful recovery. A failed argument-validity
check is retained as a protocol error; it does not remove a terminal attempt or
imply that its trace is corrupt. Completion and content scores remain separate.

Reproduce a completed M2 stage with `paper-review check <stage-directory>`.
For example, check a completed benchmark stage from the repository root with:

```shell
python -c "from paper_review.benchmark_runner import check_runs; print(check_runs('runs/m3-existing-20261118-luna6/r1/core'))"
```
