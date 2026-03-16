from app.services.llm_service import generate


def generate_article(outline, word_count, language):

    prompt = f"""
        You are an expert SEO writer.

        Write a {word_count} word article in {language}.

        Follow this outline EXACTLY:

        {outline}

        Formatting rules:

        - Use Markdown headings
        - Use exactly one # H1 title
        - Use ## for main sections
        - Use ### for subsections
        - Write paragraphs under each heading
        - Do not add headings not present in the outline
        - Ensure natural SEO friendly writing

        Example structure:

        # Article Title

        Intro paragraph.

        ## Section Title

        Paragraph text.

        ### Subsection Title

        Paragraph text.
    """

    return generate(prompt)