"""
Example: Scrape TikTok videos, hashtags, creators & Shop affiliate flags via Apify Python Client.
Requires: pip install apify-client
"""
import os
from apify_client import ApifyClient

APIFY_TOKEN = os.getenv("APIFY_TOKEN", "YOUR_APIFY_TOKEN")
client = ApifyClient(APIFY_TOKEN)

run_input = {
    "hashtags": ["tiktokmademebuyit", "amazonfinds"],
    "resultsPerPage": 20,
    "countryCode": "US"
}

print("🚀 Launching TikTok Video & Hashtag Scraper on Apify Cloud...")
run = client.actor("magic-scraper/tiktok-video-hashtag-scraper").call(run_input=run_input)

print(f"✅ Run finished with status: {run.get('status')}")
print("📊 Extracted Videos:\n")

dataset_id = run["defaultDatasetId"]
for item in client.dataset(dataset_id).iterate_items():
    author = item.get("authorMeta", {})
    print(f"Post ID: {item.get('id')}")
    print(f"  URL:       {item.get('webVideoUrl')}")
    print(f"  Creator:   @{author.get('name')} ({author.get('fans')} fans)")
    print(f"  Caption:   {item.get('text')[:70]}...")
    print(f"  Views:     {item.get('playCount')} | Likes: {item.get('diggCount')} | ER: {item.get('engagement_rate')}%")
    print(f"  Shop Cart: {'🛒 YES (TikTok Shop Affiliate)' if item.get('hasTikTokShopProduct') else '❌ None'}\n")
