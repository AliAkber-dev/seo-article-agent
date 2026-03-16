from app.services.llm_service import generate
from app.utils.json_utils import parse_llm_json

def generate_faq(topic, serp_results):

    titles = "\n".join([r.title for r in serp_results])
    snippets = "\n".join([r.snippet for r in serp_results])

    prompt = f"""
    You are an SEO strategist.

    Based on the topic:

    {topic}

    And these search results:

    Titles:
    {titles}

    Snippets:
    {snippets}

    Generate 3-5 frequently asked questions users might search for.

    Return JSON like:

    [
    {{
        "question": "...",
        "answer": "..."
    }}
    ]
    """
    raw_json = generate(prompt) 
    return parse_llm_json(raw_json)