from app.services.llm_service import generate


def generate_outline(topic, subtopics, language):

    prompt = f"""
    You are an SEO strategist.

    Create a structured SEO article outline in {language}.

    TOPIC:
    {topic}

    SUBTOPICS TO COVER:
    {subtopics}

    STRICT REQUIREMENTS:

    1. Use Markdown headings only.
    2. Use EXACTLY one H1 (#).
    3. Use 5-7 H2 sections (##).
    4. H3 subsections (###) are optional but recommended where helpful.
    5. Do NOT include bullet points or explanations.
    6. Do NOT include any text outside the headings.
    7. The output must be ONLY the outline.

    Example format:

    # Article Title

    ## Section One

    ### Subsection

    ### Subsection

    ## Section Two

    ## Section Three

    Generate the outline now.
    """
    outline = generate(prompt)

    return outline