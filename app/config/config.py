import os
from dotenv import load_dotenv

# Load .env once when module initializes
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ENV = os.getenv("ENV", "development")
SERP_API_KEY = os.getenv("SERP_API_KEY")
USE_MOCK_SERP = os.getenv("USE_MOCK_SERP", "1") == "1"

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is not set in environment variables")