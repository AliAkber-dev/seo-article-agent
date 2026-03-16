from app.services.job_service import create_job, get_job, update_job_status
from app.models.job_models import JobStatus


def test_update_job_status():

    job = create_job("topic", 1000, "English")

    update_job_status(job.job_id, JobStatus.running)

    updated = get_job(job.job_id)

    assert updated.status == JobStatus.running

def test_create_job():

    job = create_job("productivity tools", 1500, "English")

    assert job.topic == "productivity tools"
    assert job.status == "pending"