import sys
sys.path.append("./")
from app.agents.serp_agent import run


def test_serp():

    results = run("productivity tools")

    assert len(results) > 0