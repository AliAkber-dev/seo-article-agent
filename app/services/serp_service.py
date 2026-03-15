from app.models.serp_models import SERPResult


def get_serp_results(topic: str):

    return [
        SERPResult(
            rank=1,
            url="https://zapier.com/blog/remote-team-productivity-tools/",
            title="15 Best Productivity Tools for Remote Teams in 2025",
            snippet="Discover collaboration and productivity tools used by remote teams."
        ),
        SERPResult(
            rank=2,
            url="https://asana.com/resources/remote-work-tools",
            title="Top Tools for Remote Teams",
            snippet="Explore software that improves productivity for distributed teams."
        ),
        SERPResult(
            rank=3,
            url="https://trello.com/blog/remote-team-tools",
            title="Best Remote Collaboration Tools",
            snippet="Remote teams need communication, task management and automation tools."
        )
    ]