"""Deterministic, task-local evidence recitation for the native reading loop.

Related pattern: structured notes and context curation, described at
https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
This is an original implementation; no third-party code or model summary is used.
"""

from copy import deepcopy
import json


MEMORY_POLICY = "deduplicated-evidence-and-latest-feedback-v1"
MEMORY_PROMPT_VERSION = "m3-evidence-memory-v1"


class EvidenceMemory:
    """Keep every distinct observed fragment, without replaying model drafts."""

    def __init__(self, paper):
        introduction = paper.introduction()
        first_page = introduction.pop("page_1")
        self.paper = introduction
        self.fragments = {}
        self.actions = []
        self.latest_feedback = None
        self.latest_validation = None
        self._remember_fragment(1, first_page, truncated=False)

    def _remember_fragment(self, page, text, *, truncated):
        fragments = self.fragments.setdefault(page, [])
        existing = next((fragment for fragment in fragments if fragment["text"] == text), None)
        if existing is None:
            fragments.append({"text": text, "truncated": truncated})
        elif not truncated:
            existing["truncated"] = False

    def remember(self, step, name, arguments, observation):
        """Record tool facts; failed quotations remain feedback, never evidence."""
        if name == "read_pages":
            for page in observation.get("pages", []):
                self._remember_fragment(page["page"], page["text"],
                                        truncated=page.get("truncated", False))
        elif name == "search_paper":
            for match in observation.get("matches", []):
                self._remember_fragment(match["page"], match["snippet"], truncated=True)

        outcome = {"step": step, "action": name}
        if isinstance(arguments, dict):
            for key in ("query", "start", "end"):
                if key in arguments:
                    outcome[key] = arguments[key]
        if "error" in observation:
            outcome["error"] = observation["error"]
        elif name == "read_pages":
            outcome["pages"] = [page["page"] for page in observation.get("pages", [])]
        elif name == "search_paper":
            outcome["match_count"] = len(observation.get("matches", []))
            outcome["limit_reached"] = observation.get("limit_reached", False)
        self.actions.append(outcome)

        # Source excerpts already live in the evidence packet. Preserve diagnostic
        # fields, including hints, without duplicating their text here.
        self.latest_feedback = deepcopy({key: value for key, value in observation.items()
                                         if key not in ("pages", "matches")})
        if observation.get("error") == "citation_validation_failed":
            failed = []
            review = (arguments or {}).get("review", {})
            for index, (item, check) in enumerate(zip(review.get("observations", []),
                                                     observation["citation_checks"]), 1):
                if not (check["citation_verified"] and check["observed"]):
                    failed.append({"observation_index": index, "page": item["page"],
                                   "quote": item["quote"], "check": deepcopy(check)})
            self.latest_validation = {
                "error": "citation_validation_failed",
                "rejected_citations": failed,
                "hint": observation.get("hint"),
            }

    def no_action(self, step):
        self.actions.append({"step": step, "action": "no_tool_call"})
        self.latest_feedback = {"error": "no_tool_call",
                                "hint": "Choose a reading tool or submit_review."}

    def messages(self, reads, max_reads):
        packet = {
            "context_policy": MEMORY_POLICY,
            "paper": self.paper,
            "observed_evidence": [{"page": page, "fragments": fragments}
                                  for page, fragments in sorted(self.fragments.items())],
            "action_ledger": self.actions,
            "reading_actions_remaining": max(0, max_reads - reads),
            "latest_feedback": self.latest_feedback,
            "latest_rejected_citations": self.latest_validation,
        }
        return [{"role": "user", "content": json.dumps(packet, ensure_ascii=False)}]

    def statistics(self):
        return {"policy": MEMORY_POLICY, "evidence_pages": len(self.fragments),
                "evidence_fragments": sum(len(items) for items in self.fragments.values()),
                "evidence_characters": sum(len(item["text"]) for items in self.fragments.values()
                                           for item in items),
                "action_count": len(self.actions)}
