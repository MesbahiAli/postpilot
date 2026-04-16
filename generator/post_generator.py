from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_linkedin_post(post):
    prompt = f"""
You are a LinkedIn content expert. Write a compelling LinkedIn post based on this trending tech article:

Title: {post['title']}
URL: {post['url']}
Score: {post['score']}

Rules:
- Start with a strong hook (no "I" as first word)
- 150-200 words maximum
- Add 3 relevant hashtags at the end
- Sound human, not robotic
- End with a question to trigger comments
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content