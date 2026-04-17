import requests
import re

keywordsList = [
    "AI", "Python", "Claude", "LLM", "Machine Learning",
    "Deep Learning", "FastAPI", "Data Science", "GenAI",
    "Generative AI", "AI Agents", "Neural Network",
    "Computer Vision", "NLP", "Robotics", "Blockchain",
    "Quantum Computing", "AI Safety", "AI Ethics"
]
def get_trending_posts(limit=20):
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
    
    return posts

    
postsFromHack=get_trending_posts(limit=20)


def filter_posts(postsFromHack):
    posts = []
    for post in postsFromHack:
        for keyword in keywordsList:
            if re.search(rf'\b{re.escape(keyword)}\b', post['title'], re.IGNORECASE):
                posts.append(post)
                break
    return posts
               

postFinal=filter_posts(postsFromHack)
