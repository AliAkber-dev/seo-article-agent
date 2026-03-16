import re

def validate(article, keyword):

    result = {}

    lines = article.strip().split("\n")
    title = lines[0] if lines else ""

    # Keyword checks
    result["keyword_in_title"] = keyword.lower() in title.lower()
    result["keyword_in_intro"] = keyword.lower() in article[:200].lower()

    # Word count
    word_count = len(article.split())
    result["word_count"] = word_count
    result["word_count_ok"] = word_count >= 1000

    # Heading validation
    h1_count = len(re.findall(r"^\s*# ", article, re.MULTILINE))
    h2_count = len(re.findall(r"^\s*## ", article, re.MULTILINE))
    h3_count = len(re.findall(r"^\s*### ", article, re.MULTILINE))

    result["heading_validation"] = {
        "h1_count": h1_count,
        "h2_count": h2_count,
        "h3_count": h3_count,
        "valid_structure": h1_count == 1 and h2_count >= 3
    }

    return result