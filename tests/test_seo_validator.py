from app.agents.seo_validator_agent import validate


def test_heading_structure():

    article = """
    # Best Productivity Tools for Remote Teams

    Productivity tools help teams collaborate.

    ## Communication Tools
    Content

    ## Project Management Tools
    Content

    ## Time Tracking Tools
    Content
    """

    result = validate(article, "productivity tools")

    assert result["heading_validation"]["h1_count"] == 1
    assert result["heading_validation"]["h2_count"] >= 3
    assert result["heading_validation"]["valid_structure"] is True