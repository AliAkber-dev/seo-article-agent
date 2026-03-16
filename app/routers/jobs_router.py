from fastapi import APIRouter, BackgroundTasks, Form

from app.services.job_service import create_job, get_job
from app.jobs.job_runner import run_job

router = APIRouter()

@router.post("/jobs")
def create_generation_job(
    background_tasks: BackgroundTasks,
    topic: str = Form(...),
    word_count: int = Form(1500),
    language: str = Form("English")
):

    job = create_job(topic, word_count, language)

    background_tasks.add_task(
        run_job,
        job.job_id,
        topic,
        word_count,
        language
    )

    return {
        "job_id": job.job_id,
        "status": job.status
    }

@router.get("/jobs/{job_id}")
def get_job_status(job_id: str):

    job = get_job(job_id)

    if not job:
        return {"error": "job not found"}

    return job