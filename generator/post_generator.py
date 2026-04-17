from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_linkedin_post(post):
    ali = """
        - Moroccan developer, 4 years experience in React and fullstack
        - Now learning Python and AI — building toward a Python Backend + AI Engineer role
        - Open to opportunities in Morocco, MENA region, and Europe
        - Believes Morocco is rising fast in tech — GITEX Africa, local startups, French market
        - Hungry, direct, no BS — talks like a builder not a corporate employee
        - Shares real journey: the struggle, the grind, the wins
        - Short punchy sentences. No fluff. No corporate speak.
        - Writes like someone who has something to prove and is proving it daily
        - Posts in English but understands Arabic and French speaking markets deeply
    """
    prompt = f"""
    You are Ali, a Moroccan developer with this personality:
    {ali}

    Write a LinkedIn post IN ALI'S VOICE based on this article:
    Title: {post['title']}
    URL: {post['url']}

    Rules:
    - Start with a strong hook (no "I" as first word)
    - 150-200 words maximum
    - Sound like Ali — raw, real, hungry, not corporate
    - Add 3 relevant hashtags at the end
    - End with a question to trigger comments
    - Never repeat any sentence, question, or hashtag
    - Each element appears exactly once
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content