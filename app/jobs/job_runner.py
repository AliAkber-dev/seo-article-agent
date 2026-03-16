from app.services.job_service import update_job_status, update_job_stage, save_job_result
from app.jobs.article_generator_job import run_generation
from app.models.job_models import JobStatus


def run_job(job_id, topic, word_count, language):

    try:

        update_job_status(job_id, JobStatus.running)

        def stage_callback(stage):
            update_job_stage(job_id, stage)

        result = run_generation(
            topic,
            word_count,
            language,
            stage_callback=stage_callback
        )

        save_job_result(job_id, result)

        update_job_status(job_id, JobStatus.completed)

    except Exception as e:
        print("Job failed:", e)
        update_job_status(job_id, JobStatus.failed)