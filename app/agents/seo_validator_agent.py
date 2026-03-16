def validate(article, keyword):

    result = {}

    title = article.split("\n")[0]

    result["keyword_in_title"] = keyword.lower() in title.lower()
    result["keyword_in_intro"] = keyword.lower() in article[:200].lower()

    word_count = len(article.split())
    result["word_count"] = word_count
    result["word_count_ok"] = word_count >= 1000

    return result