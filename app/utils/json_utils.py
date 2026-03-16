import json
import re


def parse_llm_json(response: str):
    """
    Cleans LLM JSON responses that may include ```json code blocks.
    """

    cleaned = response.strip()

    # Remove ```json or ``` wrappers
    cleaned = re.sub(r"^```json", "", cleaned)
    cleaned = re.sub(r"^```", "", cleaned)
    cleaned = re.sub(r"```$", "", cleaned)

    cleaned = cleaned.strip()

    return json.loads(cleaned)