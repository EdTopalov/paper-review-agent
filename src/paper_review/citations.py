"""Conservative citation matching; matching text does not prove a claim is true.

# Extends the team's normalize_evidence/check_quote implementation:
# https://github.com/EdTopalov/paper-review-agent/blob/39d760f2e47b66d074de34397101dcc66e53ead1/paper_review/paper.py
# Preserve meaningful case, hyphens, digits, signs, and mathematical notation.
"""

import re
import unicodedata


CHECKER_VERSION = "m2-citations-v2"
LIGATURES = str.maketrans({"ﬀ": "ff", "ﬁ": "fi", "ﬂ": "fl", "ﬃ": "ffi",
                          "ﬄ": "ffl", "ﬅ": "st", "ﬆ": "st", "‐": "-", "‑": "-"})
LINE_HYPHEN = re.compile(r"(?<=[^\W\d_])-[ \t]*\r?\n[ \t]*(?=[^\W\d_])")


def normalize(text):
    """The original strict metric permits whitespace changes only."""
    return " ".join(text.split())


def normalize_pdf(text, *, remove_line_hyphens=False):
    # NFC + explicit ligatures, rather than NFKC: x² must not become x2.
    text = unicodedata.normalize("NFC", text).translate(LIGATURES).replace("\u00ad", "")
    text = LINE_HYPHEN.sub("" if remove_line_hyphens else "-", text)
    return normalize(text)


def check_quote(pages, page, quote):
    valid_page = type(page) is int and 1 <= page <= len(pages)
    nonempty = isinstance(quote, str) and bool(quote.strip())
    result = {"checker_version": CHECKER_VERSION, "page_valid": valid_page,
              "quote_nonempty": nonempty, "quote_matches": False,
              "citation_verified": False, "matching_pages": [], "candidate_pages": []}
    if not valid_page or not nonempty:
        return {**result, "status": "invalid_page" if not valid_page else "invalid_quote"}
    source = pages[page - 1]
    strict = normalize(quote) in normalize(source)
    result["quote_matches"] = strict
    if quote in source:
        status = "exact"
    elif strict:
        status = "whitespace"
    elif normalize_pdf(quote) in normalize_pdf(source):
        status = "normalized"
    else:
        normalized = normalize_pdf(quote)
        matching = [i for i, text in enumerate(pages, 1) if normalized in normalize_pdf(text)]
        if matching:
            return {**result, "status": "wrong_page", "matching_pages": matching}
        # A line-end hyphen might be a word wrap OR a meaningful hyphen. Offer
        # candidates for inspection; never silently verify by deleting hyphens.
        candidate = normalize_pdf(quote, remove_line_hyphens=True)
        possible = [i for i, text in enumerate(pages, 1)
                    if candidate in normalize_pdf(text, remove_line_hyphens=True)]
        return {**result, "status": "hyphenation_ambiguous" if possible else "not_found",
                "candidate_pages": possible}
    return {**result, "status": status, "citation_verified": True, "matching_pages": [page]}
