from scrapers.reddit_scraper import get_trending_posts
from generator.post_generator import generate_linkedin_post
import json
import os
from datetime import datetime

def save_post(post, generated_content):
    storage_path = "storage/posts.json"
    
    if os.path.exists(storage_path):
        with open(storage_path, "r") as f:
            content = f.read()
            data = json.loads(content) if content.strip() else []
    else:
        data = []

    data.append({
        "source_title": post["title"],
        "source_url": post["url"],
        "content": generated_content,
        "approved_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "status": "approved"
    })

    with open(storage_path, "w") as f:
        json.dump(data, f, indent=2)

    print("✅ Post saved to storage/posts.json")

def run_agent():
    print("\n🤖 PostPilot Agent Starting...\n")
    posts = get_trending_posts(limit=5)

    for post in posts:
        print(f"\n📰 SOURCE: {post['title']}")
        print(f"🔗 URL: {post['url']}")
        print("-" * 50)

        linkedin_post = generate_linkedin_post(post)
        print("\n📝 GENERATED POST:")
        print(linkedin_post)
        print("-" * 50)

        decision = input("\n➡️  Post this? (y=yes / n=skip / r=rewrite): ").strip().lower()

        if decision == "y":
            save_post(post, linkedin_post)
        elif decision == "r":
            print("\n🔄 Rewriting...")
            linkedin_post = generate_linkedin_post(post)
            print(linkedin_post)
            decision2 = input("\n➡️  Save this version? (y/n): ").strip().lower()
            if decision2 == "y":
                save_post(post, linkedin_post)
        else:
            print("⏭️  Skipped.")

    print("\n✅ PostPilot session complete.")

run_agent()