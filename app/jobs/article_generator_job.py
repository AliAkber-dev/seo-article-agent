from app.agents.serp_agent import run as serp_run
from app.agents.topic_agent import extract_topics
from app.agents.outline_agent import generate_outline
from app.agents.article_agent import generate_article
from app.agents.linking_agent import suggest_internal_links, suggest_external_links
from app.agents.seo_validator_agent import validate
from app.agents.faq_agent import generate_faq
from app.agents.content_scorer_agent import score_content
from app.agents.keyword_agent import analyze_keywords
from app.models.job_models import JobStage
from app.utils.markdown_utils import markdown_to_html


def run_generation(topic, word_count, language, stage_callback=None):

    # Stage 1 — SERP Collection
    serp_results = serp_run(topic)

    if stage_callback:
        stage_callback(JobStage.serp_collected)

    # Stage 2 — Topic Extraction
    topics = extract_topics(serp_results)

    if stage_callback:
        stage_callback(JobStage.serp_analyzed)

    # Stage 3 — FAQ generation
    faq = generate_faq(topic, serp_results)

    # Stage 4 — Outline
    outline = generate_outline(topic, topics, language)

    if stage_callback:
        stage_callback(JobStage.outline_generated)

    # Stage 5 — Article
    article_md = generate_article(outline, word_count, language)
    article_html = markdown_to_html(article_md)

    if stage_callback:
        stage_callback(JobStage.article_generated)

    # Stage 6 — Linking Strategy
    internal_links = suggest_internal_links(topic, serp_results)
    external_links = suggest_external_links(topic, serp_results)

    if stage_callback:
        stage_callback(JobStage.links_generated)

    # Stage 7 — SEO Validation
    validation = validate(article_md, topic)

    if stage_callback:
        stage_callback(JobStage.validated)

    # Stage 8 - SERP
    keywords = analyze_keywords(topic, serp_results)
    if stage_callback:
        stage_callback(JobStage.keyword_analysis)
    
    # Stage 9 — Content Quality Score
    content_score = score_content(topic, article_md)

    
    
    return {
        "outline_markdown": outline,
        "article_markdown": article_md,
        "article_html": article_html,
        "keywords_analysis": keywords,
        "internal_links": internal_links,
        "external_links": external_links,
        "faq": faq,
        "validation": validation,
        "content_quality_score": content_score
    }