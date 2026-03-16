from app.services.llm_service import generate


def extract_topics(serp_results):

    titles = "\n".join([r.title for r in serp_results])
    snippets = "\n".join([r.snippet for r in serp_results])

    prompt = f"""
    You are an SEO analyst.

    Analyze the following search results and identify common topics
    covered by high-ranking articles.

    Titles:
    {titles}

    Snippets:
    {snippets}

    Return a list of 5-8 key topics that should be covered in an article.
    """

    topics = generate(prompt)

    return topics