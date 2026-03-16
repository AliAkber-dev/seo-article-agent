from app.services.llm_service import generate
from app.utils.json_utils import parse_llm_json


def suggest_internal_links(topic, serp_results):

    titles = "\n".join([r.title for r in serp_results])
    snippets = "\n".join([r.snippet for r in serp_results])

    prompt = f"""
    You are an SEO strategist.

    The article topic is:

    {topic}

    Here are top Google search result titles and snippets:

    Titles:
    {titles}

    Snippets:
    {snippets}

    Identify 3-5 internal linking opportunities for related content
    that could exist on the same website.

    Return JSON with:

    - anchor_text
    - target_topic
    - placement_hint

    Example format:

    [
    {{
        "anchor_text": "remote collaboration tools",
        "target_topic": "guide to remote collaboration tools",
        "placement_hint": "communication tools section"
    }}
    ]
    """

    raw_json = generate(prompt)
    return parse_llm_json(raw_json)

def suggest_external_links(topic, serp_results):

    titles = "\n".join([r.title for r in serp_results])
    snippets = "\n".join([r.snippet for r in serp_results])

    prompt = f"""
    You are an SEO content strategist.

    Topic:
    {topic}

    Top search result titles:
    {titles}

    Snippets:
    {snippets}

    Suggest 2-4 authoritative external sources that would improve
    the credibility of the article.

    Sources should be things like:
    - research reports
    - well-known publications
    - academic or industry studies
    - official documentation

    Return JSON with:

    - source_name
    - url
    - citation_reason
    - suggested_article_section

    Example format:

    [
    {{
        "source_name": "Google SEO Starter Guide",
        "url": "https://developers.google.com/search/docs/fundamentals/seo-starter-guide",
        "citation_reason": "official SEO documentation",
        "suggested_article_section": "SEO best practices section"
    }}
    ]
    """

    raw_json = generate(prompt)
    return parse_llm_json(raw_json)

    