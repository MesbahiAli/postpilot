import requests

def get_trending_posts(limit=5):
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