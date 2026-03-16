import os
from openai import OpenAI
from app.config.config import OPENAI_API_KEY 

client = OpenAI(api_key=OPENAI_API_KEY)

def generate(prompt: str):

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response.choices[0].message.content