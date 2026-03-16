from app.utils.markdown_utils import markdown_to_html


def test_markdown_conversion():

    md = "# Title"

    html = markdown_to_html(md)

    assert "<h1>" in html