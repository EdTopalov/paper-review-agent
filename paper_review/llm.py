import os
import time
from openai import OpenAI





class OpenAILLM:
    def __init__(self):
        self.model = os.environ["OPENAI_MODEL"]

        self.client = OpenAI(
            api_key=os.environ["GEMINI_API_KEY"],
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
            max_retries=0,
            timeout=120,
        )

    def ask(self, messages: list[dict]) -> dict:
        started = time.perf_counter()

        completion = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            response_format={"type": "json_object"},
        )

        usage = completion.usage

        input_tokens = usage.prompt_tokens if usage else None
        output_tokens = usage.completion_tokens if usage else None

        in_price = os.environ.get("INPUT_USD_PER_1M")
        out_price = os.environ.get("OUTPUT_USD_PER_1M")

        cost = None

        if None not in (in_price, out_price, input_tokens, output_tokens):
            cost = (input_tokens * float(in_price) + output_tokens * float(out_price)) / 1_000_000

        return {
            "raw": completion.choices[0].message.content or "",
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
            "cost_usd": cost,
            "latency_s": time.perf_counter() - started,
        }