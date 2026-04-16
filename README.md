# 🤖 PostPilot

AI agent that scrapes trending tech content and generates LinkedIn posts automatically.

## What it does
- Scrapes top trending posts from HackerNews
- Generates LinkedIn-optimized posts using GPT-4o-mini
- Human approval loop (approve / skip / rewrite)
- Saves approved posts to local storage

## Tech Stack
- Python 3.11
- OpenAI API (GPT-4o-mini)
- HackerNews API
- python-dotenv

## Setup
```bash
git clone https://github.com/MesbahiAli/postpilot.git
cd postpilot
pip install openai praw python-dotenv
```

Add your API key to `.env`: