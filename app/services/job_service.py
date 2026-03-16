import uuid
from app.models.job_models import GenerationJob, JobStatus
from datetime import datetime

#in-memory database for now
jobs = {}


def create_job(topic, word_count, language):

    job_id = str(uuid.uuid4())

    job = GenerationJob(
        job_id=job_id,
        topic=topic,
        word_count=word_count,
        language=language,
        status=JobStatus.pending,
        created_at=datetime.utcnow()
    )

    jobs[job_id] = job

    return job


def get_job(job_id):

    return jobs.get(job_id)


def update_job_status(job_id, status):

    job = jobs[job_id]
    job.status = status


def save_job_result(job_id, result):

    job = jobs[job_id]
    job.result = result

def update_job_stage(job_id, stage):

    job = jobs[job_id]

    job.stage = stage