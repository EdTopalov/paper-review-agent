"""Shared review format for the loop, baseline, and evaluator."""

REVIEW_SCHEMA = {
    "type": "object", "additionalProperties": False,
    "properties": {
        "score": {"type": "number", "minimum": 0, "maximum": 1},
        "summary": {"type": "string"},
        "observations": {
            "type": "array", "minItems": 2, "maxItems": 4,
            "items": {
                "type": "object", "additionalProperties": False,
                "properties": {
                    "kind": {"type": "string", "enum": ["strength", "limitation", "uncertainty"]},
                    "claim": {"type": "string"},
                    "page": {"type": "integer", "minimum": 1},
                    "quote": {"type": "string"},
                },
                "required": ["kind", "claim", "page", "quote"],
            },
        },
        "unresolved_questions": {"type": "array", "items": {"type": "string"}},
    },
    "required": ["score", "summary", "observations", "unresolved_questions"],
}


def function(name, description, properties):
    return {"type": "function", "name": name, "description": description, "strict": True,
            "parameters": {"type": "object", "properties": properties,
                           "required": list(properties), "additionalProperties": False}}


TOOLS = [
    function("search_paper", "Search the paper text. Empty matches are a normal result.", {
        "query": {"type": "string"}, "reason": {"type": "string"},
    }),
    function("read_pages", "Read 1 to 3 consecutive pages, using 1-based PDF page numbers.", {
        "start": {"type": "integer"}, "end": {"type": "integer"},
        "reason": {"type": "string"},
    }),
    function("submit_review", "Finish when the evidence suffices; report remaining uncertainty.", {
        "reason": {"type": "string"}, "review": REVIEW_SCHEMA,
    }),
]
