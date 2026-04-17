import requests
import re

keywordsList = [
    "AI", "Python", "Claude", "LLM", "Machine Learning",
    "Deep Learning", "FastAPI", "Data Science", "GenAI",
    "Generative AI", "AI Agents", "Neural Network",
    "Computer Vision", "NLP", "Robotics", "Blockchain",
    "Quantum Computing", "AI Safety", "AI Ethics","MCP"
]


def filter_posts(postsFromHack):
    posts = []
    for post in postsFromHack:
        for keyword in keywordsList:
            if re.search(rf'\b{re.escape(keyword)}\b', post['title'], re.IGNORECASE):
                posts.append(post)
                break
    return posts
               

def get_trending_posts_hackNews(limit=20):
    top_stories_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
    
    response = requests.get(top_stories_url)
    story_ids = response.json()[:limit]
    
    posts = []
    for story_id in story_ids:
        story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
        story = requests.get(story_url).json()    
        posts.append({
            "title": story.get("title", ""),
            "score": story.get("score", 0),
            "url": story.get("url", ""),
            "source": "HackerNews"
        })
    
    return filter_posts(posts)


def get_trending_posts_DEVto(limit=3):
    top_stories_url = "https://dev.to/api/articles?top=1"
    
    response = requests.get(top_stories_url)
    story = response.json()[:limit]
    posts = []
    for article in story:
        posts.append({
                "title": article.get("title", ""),
                "score": article.get("public_reactions_count", 0),
                "url": article.get("url", ""),
                "source": "DevTo"
            })
    
    return filter_posts(posts)

    



postFinal=get_trending_posts_hackNews(limit=20)+get_trending_posts_DEVto(limit=20)
