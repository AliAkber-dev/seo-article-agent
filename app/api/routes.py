from fastapi import APIRouter, Form
from app.jobs.article_generator_job import run_generation

router = APIRouter()


@router.post("/generate")
def generate_article(
    topic: str = Form(...),
    word_count: int = Form(1500),
    language: str = Form("English")
):

    result = run_generation(
        topic=topic,
        word_count=word_count,
        language=language
    )

    return result