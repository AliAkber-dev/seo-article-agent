import markdown


def markdown_to_html(md_text: str) -> str:
    return markdown.markdown(md_text)