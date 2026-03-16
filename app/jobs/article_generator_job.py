from app.agents.serp_agent import run as serp_run
from app.agents.topic_agent import extract_topics
from app.agents.outline_agent import generate_outline
from app.agents.article_agent import generate_article
from app.agents.linking_agent import suggest_internal_links, suggest_external_links
from app.agents.seo_validator_agent import validate


def run_generation(topic, word_count=1500, language="English"):

    serp_results = serp_run(topic)

    topics = extract_topics(serp_results)

    outline = generate_outline(topic, topics, language)

    article = generate_article(outline, word_count, language)

    internal_links = suggest_internal_links(topic, serp_results)
    external_links = suggest_external_links(topic, serp_results)

    validation = validate(article, topic)

    return {
        "outline": outline,
        "article": article,
        "internal_links": internal_links,
        "external_links": external_links,
        "validation": validation
    }