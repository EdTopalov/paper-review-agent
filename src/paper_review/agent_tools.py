"""Evidence bookkeeping shared by the M2 and PyAgent reading loops."""

from .citations import check_quote


class PaperEvidence:
    def __init__(self, paper):
        self.paper = paper
        self.observed = {1: [paper.pages[0]]}

    def remember(self, name, observation):
        if name == "search_paper":
            fragments = ((row["page"], row["snippet"])
                         for row in observation.get("matches", []))
        else:
            fragments = ((row["page"], row["text"])
                         for row in observation.get("pages", []))
        for page, text in fragments:
            self.observed.setdefault(page, []).append(text)

    def check(self, review):
        checks = self.paper.check_citations(review)
        for observation, check in zip(review["observations"], checks):
            check["observed"] = any(
                check_quote([fragment], 1, observation["quote"])["citation_verified"]
                for fragment in self.observed.get(observation["page"], [])
            )
        return checks
