from app.services.job_service import update_job_status, create_job, get_job
from app.models.job_models import JobStatus


def test_update_job_status():

    job = create_job("topic", 1000, "English")

    update_job_status(job.job_id, JobStatus.running)

    updated = get_job(job.job_id)

    assert updated.status == JobStatus.running