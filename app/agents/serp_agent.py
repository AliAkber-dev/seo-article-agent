from app.services.serp_service import get_serp_results


def run(topic: str):

    results = get_serp_results(topic)

    return results