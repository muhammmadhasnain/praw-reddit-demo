
import praw # type: ignore
from config import CLIENT_ID, CLIENT_SECRET, USER_AGENT





reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    user_agent=USER_AGENT,
)

def fetch_latest_posts(subreddit_name:str , limit:int):

    try:

        subreddit = reddit.subreddit(subreddit_name)

        print(f"\n📥 Latest {limit} posts from r/{subreddit_name}:\n")

        for post in subreddit.new(limit=limit):
            print(f"🧵 Title: {post.title}")
            print(f"👤 author: {post.author}")
            print(f"⬆️ Upvotes: {post.score}")

            print("-" * 40)
    


    except Exception as e:
        print("❌ Error occurred:", e)



if __name__ == "__main__":
    fetch_latest_posts("python", 5)