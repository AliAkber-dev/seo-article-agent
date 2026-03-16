from pydantic import BaseModel
from enum import Enum
from typing import Optional
from datetime import datetime

class JobStage(str, Enum):

    serp_collected = "serp_collected"

    serp_analyzed = "serp_analyzed"

    outline_generated = "outline_generated"

    article_generated = "article_generated"

    links_generated = "links_generated"

    validated = "validated"

    keyword_analysis = "keyword_analysis_generated"

class JobStatus(str, Enum):
    pending = "pending"
    running = "running"
    completed = "completed"
    failed = "failed"


class GenerationJob(BaseModel):

    job_id: str
    topic: str
    word_count: int
    language: str
    stage: Optional[JobStage] = None
    status: JobStatus
    result: Optional[dict] = None
    created_at: datetime