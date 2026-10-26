"""Frozen paper snapshots and deterministic reading tools."""

from hashlib import sha256
import json
from pathlib import Path
import re

from .citations import check_quote, normalize

def file_hash(path):
    return sha256(Path(path).read_bytes()).hexdigest()


class Paper:
    def __init__(self, snapshot):
        self.snapshot = snapshot
        self.pages = snapshot["pages"]
        if not self.pages or not any(page.strip() for page in self.pages):
            raise ValueError("paper_has_no_extractable_text")

    @classmethod
    def load(cls, path):
        path = Path(path)
        if path.suffix.lower() == ".pdf":
            # pypdf is BSD-3-Clause: https://pypdf.readthedocs.io/en/stable/
            from pypdf import PdfReader
            reader = PdfReader(path)
            return cls({"title": path.stem, "pdf_sha256": file_hash(path),
                        "pages": [page.extract_text() or "" for page in reader.pages]})
        return cls(json.loads(path.read_text(encoding="utf-8")))

    def introduction(self):
        return {"title": self.snapshot.get("title"), "page_count": len(self.pages),
                "source_url": self.snapshot.get("source_url"), "page_1": self.pages[0]}

    def full_text(self):
        return "\n\n".join(f"=== PDF PAGE {i} ===\n{text}"
                            for i, text in enumerate(self.pages, 1))

    def read_pages(self, start, end):
        if type(start) is not int or type(end) is not int or not (1 <= start <= end <= len(self.pages)) or end - start > 2:
            return {"error": "invalid_page_range", "page_count": len(self.pages),
                    "hint": "Use 1-based pages and request at most 3 pages."}
        # Each excerpt carries its own page identity, as in the team's read_page
        # tool. Never concatenate multiple pages into one unstructured string.
        return {"pages": [{"page": i, "text": self.pages[i-1][:8000],
                           "truncated": len(self.pages[i-1]) > 8000}
                          for i in range(start, end + 1)]}

    def search(self, query):
        if not query.strip():
            return {"error": "empty_query", "hint": "Supply a literal keyword or phrase."}
        query = normalize(query).casefold()
        matches = []
        for number, page in enumerate(self.pages, 1):
            text = normalize(page)
            for match in re.finditer(re.escape(query), text.casefold()):
                matches.append({"page": number,
                                "snippet": text[max(0, match.start()-180):match.end()+400]})
                if len(matches) == 8:
                    return {"matches": matches, "limit_reached": True}
        result = {"matches": matches, "limit_reached": False}
        if not matches:
            result["hint"] = "Literal phrase not found. Try one keyword or a shorter exact phrase, or read pages."
        return result

    def check_citations(self, review):
        return [check_quote(self.pages, observation["page"], observation["quote"])
                for observation in review["observations"]]
