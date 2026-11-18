"""Offline checks of evidence recitation using the real native agent loop."""

from copy import deepcopy
import json

from paper_review.context_memory import EvidenceMemory, MEMORY_POLICY
from paper_review.evaluation import check_experiment
from paper_review.paper import Paper
from paper_review.runner import Config, run_review
from paper_review.trace import read_events
from test_harness import Action, Client, FIXTURE, OPENING_REVIEW, REVIEW, Response, finish


def read(start=2, end=3):
    return Response([Action("read_pages", {"start": start, "end": end,
                                           "reason": "Inspect evidence."}, "read")])


def run(tmp_path, responses, *, name="memory", config=None):
    client = Client(responses)
    folder = tmp_path / name
    result = run_review(FIXTURE, folder, config or Config(), "dev",
                        variant="evidence_memory", client=client)
    return result, client, read_events(folder / "trace.jsonl")


def packet(client, index):
    inputs = client.requests[index]["input"]
    assert len(inputs) == 1 and inputs[0]["role"] == "user"
    assert "type" not in inputs[0]  # No orphaned function-call outputs.
    return json.loads(inputs[0]["content"])


def test_rejected_draft_is_removed_but_evidence_and_repair_feedback_remain(tmp_path):
    bad = deepcopy(REVIEW)
    bad["summary"] = "DISCARD_THIS_OLD_REVIEW_DRAFT"
    bad["observations"][0]["quote"] = "THIS_QUOTATION_WAS_INVENTED"
    result, client, events = run(tmp_path, [read(), finish(bad), finish(REVIEW)])
    assert result["status"] == "ok"
    assert result["api_calls"] == result["decision_steps"] == 3
    assert result["reading_actions"] == result["rejected_submissions"] == 1
    assert result["evidence_observed"] == [True, True]
    context = packet(client, 2)
    assert "DISCARD_THIS_OLD_REVIEW_DRAFT" not in client.requests[2]["input"][0]["content"]
    assert context["latest_feedback"]["error"] == "citation_validation_failed"
    failed = context["latest_rejected_citations"]["rejected_citations"]
    assert len(failed) == 1 and failed[0]["page"] == 3
    assert failed[0]["quote"] == "THIS_QUOTATION_WAS_INVENTED"
    evidence = context["observed_evidence"]
    assert [row["page"] for row in evidence] == [1, 2, 3]
    assert all("THIS_QUOTATION_WAS_INVENTED" not in fragment["text"]
               for row in evidence for fragment in row["fragments"])
    assert context["action_ledger"] == [
        {"step": 1, "action": "read_pages", "start": 2, "end": 3, "pages": [2, 3]},
        {"step": 2, "action": "submit_review", "error": "citation_validation_failed"},
    ]
    memory_events = [event for event in events if event["event"] == "context_memory"]
    assert len(memory_events) == result["api_calls"]
    assert memory_events[-1]["evidence_pages"] == 3
    assert result["harness"]["context_policy"] == MEMORY_POLICY
    assert check_experiment(tmp_path / "memory")["passed"] == 1


def test_repeated_page_reads_keep_exact_text_once_per_page(tmp_path):
    result, client, events = run(tmp_path, [read(), read(), finish(REVIEW)])
    assert result["status"] == "ok" and result["reading_actions"] == 2
    context = packet(client, 2)
    paper = Paper.load(FIXTURE)
    assert [row["page"] for row in context["observed_evidence"]] == [1, 2, 3]
    for row in context["observed_evidence"]:
        assert row["fragments"] == [{"text": paper.pages[row["page"] - 1], "truncated": False}]
    assert len(context["action_ledger"]) == 2
    assert [event for event in events if event["event"] == "context_memory"][-1]["evidence_fragments"] == 3


def test_search_snippets_are_deduplicated_with_page_provenance():
    paper = Paper.load(FIXTURE)
    memory = EvidenceMemory(paper)
    observation = paper.search("significance test")
    for step in (1, 2):
        memory.remember(step, "search_paper", {"query": "significance test"}, observation)
    context = json.loads(memory.messages(2, 5)[0]["content"])
    assert [row["page"] for row in context["observed_evidence"]] == [1, 2]
    assert context["observed_evidence"][1]["fragments"] == [
        {"text": observation["matches"][0]["snippet"], "truncated": True}]
    assert context["action_ledger"][0]["match_count"] == 1


def test_large_initial_page_and_truncated_read_are_preserved_without_trimming():
    paper = Paper({"title": "Long fixture", "pages": ["x" * 9000]})
    memory = EvidenceMemory(paper)
    memory.remember(1, "read_pages", {"start": 1, "end": 1}, paper.read_pages(1, 1))
    context = json.loads(memory.messages(1, 5)[0]["content"])
    assert context["observed_evidence"] == [{"page": 1, "fragments": [
        {"text": "x" * 9000, "truncated": False},
        {"text": "x" * 8000, "truncated": True},
    ]}]


def test_memory_state_is_isolated_between_papers(tmp_path):
    first, first_client, _ = run(tmp_path, [read(), finish(REVIEW)], name="first")
    second, second_client, _ = run(tmp_path, [finish()], name="second")
    assert first["status"] == second["status"] == "ok"
    assert len(first_client.requests) == 2 and len(second_client.requests) == 1
    context = packet(second_client, 0)
    assert [row["page"] for row in context["observed_evidence"]] == [1]
    assert context["action_ledger"] == []
    assert context["latest_feedback"] is context["latest_rejected_citations"] is None


def test_no_action_and_bad_arguments_keep_feedback_without_counting_a_read(tmp_path):
    bad = Response([Action("read_pages", {"start": "two", "end": 3,
                                          "reason": "Inspect evidence."}, "bad")])
    result, client, _ = run(tmp_path, [Response(text="No action."), bad, finish()])
    assert result["status"] == "ok" and result["api_calls"] == 3
    assert result["reading_actions"] == 0
    assert packet(client, 1)["latest_feedback"]["error"] == "no_tool_call"
    assert packet(client, 2)["latest_feedback"]["error"] == "invalid_arguments"


def test_native_tools_instructions_and_reading_budget_are_shared(tmp_path):
    result, client, _ = run(tmp_path, [read(), finish(REVIEW)], config=Config(max_reads=1))
    native_client = Client([finish()])
    run_review(FIXTURE, tmp_path / "native", Config(max_reads=1), "dev", client=native_client)
    assert result["status"] == "ok"
    for key in ("instructions", "tools", "parallel_tool_calls", "tool_choice"):
        assert client.requests[0][key] == native_client.requests[0][key]
    assert [tool["name"] for tool in client.requests[1]["tools"]] == ["submit_review"]
    assert packet(client, 1)["reading_actions_remaining"] == 0


def test_unobserved_citations_are_rejected_under_the_same_decision_budget(tmp_path):
    result, client, _ = run(tmp_path, [finish(REVIEW)] * 3, config=Config(max_reads=0))
    assert result["status"] == "error"
    assert result["error"]["code"] == "model_decision_budget_exhausted"
    assert result["api_calls"] == result["decision_steps"] == result["rejected_submissions"] == 3
    assert len(client.requests) == 3
    context = packet(client, 2)
    assert [row["page"] for row in context["observed_evidence"]] == [1]
    assert all(not row["check"]["observed"]
               for row in context["latest_rejected_citations"]["rejected_citations"])
