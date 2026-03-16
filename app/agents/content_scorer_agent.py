from app.services.llm_service import generate
from app.utils.json_utils import parse_llm_json

def score_content(topic, article):

    prompt = f"""
    You are an SEO content evaluator.

    Evaluate this article written about:

    {topic}

    ARTICLE:
    {article}

    Score the article from 1-100 based on:

    - SEO optimization
    - readability
    - topic coverage
    - structure

    Return JSON:

    {{
    "score": 85,
    "strengths": [],
    "improvements": []
    }}
    """
    raw_json = generate(prompt) 
    return parse_llm_json(raw_json)