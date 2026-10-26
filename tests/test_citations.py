"""Adversarial checks: PDF typography must not hide changed scientific content."""

import pytest

from paper_review.citations import check_quote


@pytest.mark.parametrize("source,quote,status", [
    ("An exact quotation.", "exact quotation", "exact"),
    ("An\nexact   quotation.", "An exact quotation.", "whitespace"),
    ("A signiﬁcant result.", "A significant result.", "normalized"),
    ("A re\u00adtrieval method.", "A retrieval method.", "normalized"),
    ("A non-\ninformative result.", "A non-informative result.", "normalized"),
    ("A signif-\nicant result.", "A significant result.", "hyphenation_ambiguous"),
    ("We re-\ncover the sample.", "We recover the sample.", "hyphenation_ambiguous"),
    ("An agent-assisted method.", "An agentassisted method.", "not_found"),
    ("Model A beats model B.", "Model a beats model B.", "not_found"),
    ("Accuracy is 1.0%.", "Accuracy is 10%.", "not_found"),
    ("x² = 4", "x2 = 4", "not_found"),
    ("x₂ = 4", "x2 = 4", "not_found"),
    ("The change is −2.", "The change is +2.", "not_found"),
    ("Range: 1-\n2", "Range: 12", "not_found"),
])
def test_matching_preserves_meaningful_differences(source, quote, status):
    result = check_quote([source], 1, quote)
    assert result["status"] == status
    assert result["citation_verified"] == (status in ("exact", "whitespace", "normalized"))


def test_wrong_page_reports_actual_location():
    result = check_quote(["A different page.", "The signiﬁcant result."], 1, "The significant result.")
    assert result["status"] == "wrong_page"
    assert result["matching_pages"] == [2]
    assert not result["citation_verified"]


@pytest.mark.parametrize("page,quote", [(True, "text"), (0, "text"), (2, "text"), (1, ""), (1, "  "), (1, None)])
def test_invalid_citations_never_pass(page, quote):
    assert not check_quote(["text"], page, quote)["citation_verified"]
