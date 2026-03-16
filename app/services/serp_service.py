from app.models.serp_models import SERPResult
from app.config.config import SERP_API_KEY, USE_MOCK_SERP
import requests

def get_serp_results_mock(topic: str):

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


def get_serp_results(topic):

    # Use mock results if configured
    if USE_MOCK_SERP:
        return get_serp_results_mock(topic)
    
    url = "https://serpapi.com/search"

    params = {
        "q": topic,
        "engine": "google",
        "api_key": SERP_API_KEY,
        "num": 10
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()

        data = response.json()
        results = []

        for idx, result in enumerate(data.get("organic_results", []), start=1):

            serp_object = SERPResult(
                rank=idx,
                url=result.get("link"),
                title=result.get("title"),
                snippet=result.get("snippet")
            )

            results.append(serp_object)

        return results

    except Exception as e:
        print("SERP API failed, falling back to mock data:", e)
        return get_serp_results_mock(topic)
