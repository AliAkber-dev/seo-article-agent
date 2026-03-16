import os
from openai import OpenAI
from app.config.config import OPENAI_API_KEY 
from tenacity import retry, stop_after_attempt
client = OpenAI(api_key=OPENAI_API_KEY)

@retry(stop=stop_after_attempt(3))
def generate(prompt: str):

    response = client.chat.completions.create(
        model="gpt-5-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response.choices[0].message.content