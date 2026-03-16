from app.services.llm_service import generate
from app.utils.json_utils import parse_llm_json


def analyze_keywords(topic, serp_results):

    titles = "\n".join([r.title for r in serp_results])
    snippets = "\n".join([r.snippet for r in serp_results])

    prompt = f"""
    You are an SEO keyword strategist.

    Topic:
    {topic}

    Top search result titles:
    {titles}

    Snippets:
    {snippets}

    Identify:

    1. Primary keyword
    2. 5-10 secondary keywords related to the topic

    Return JSON:

    {{
    "primary_keyword": "...",
    "secondary_keywords": []
    }}

    Return valid JSON only.
    """

    raw = generate(prompt)

    return parse_llm_json(raw)