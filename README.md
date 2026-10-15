# 🎬 TikTok Video & Hashtag Scraper: Posts, Creators, Sounds & Shop Affiliates

[![TikTok Video & Hashtag Scraper](https://apify.com/actor-badge?actor=magic-scraper/tiktok-video-hashtag-scraper)](https://apify.com/magic-scraper/tiktok-video-hashtag-scraper)
![Free Tier](https://img.shields.io/badge/Apify%20Free%20Tier-$5%20Monthly%20Credit-blue?style=flat-square)
![Pay-Per-Result](https://img.shields.io/badge/Pricing-$2.00%20%2F%201K%20videos-blue?style=flat-square)
![No Cookies Required](https://img.shields.io/badge/Cookies-Not%20Required-success?style=flat-square)
![Speed](https://img.shields.io/badge/Speed-~1.5s%20per%20page-brightgreen?style=flat-square)
![Export](https://img.shields.io/badge/Export-JSON%20|%20CSV%20|%20Excel-orange?style=flat-square)

Extract trending TikTok videos, creator statistics, hashtag feeds, music metadata, calculated engagement rates, and **TikTok Shop affiliate product indicators** at scale.

> ⚡ **Try it directly in your browser without code:**  
> 👉 **[Run TikTok Video & Hashtag Scraper on Apify (Free $5 Monthly Credits)](https://apify.com/magic-scraper/tiktok-video-hashtag-scraper)**

---

## 🎯 Who is this for?

- **Influencer Marketing & Talent Agencies:** Track creator engagement rates, follower growth, and campaign performance.
- **DTC Brands & E-Commerce Sellers:** Detect winning affiliate product marketing hooks via the `hasTikTokShopProduct` flag.
- **Content Creators & Social Media Managers:** Research viral audio tracks, trending hashtags, and top video formats.
- **Brand Protection & PR Teams:** Monitor brand mentions, user sentiment, and viral UGC campaigns.

---

## ⚡ Why Choose This Scraper Over Competitors?

| Feature | **Our TikTok Video Scraper** | Competing Scrapers (Clockworks, etc.) |
| :--- | :---: | :---: |
| **Pricing** | 💰 **$2.00 / 1,000 videos** ($0.002/item) | 💸 $3.70 – $10.00 / 1,000 videos |
| **Minimal Start Fee** | 🏷️ **$0.001** | 💸 $0.05 – $0.10 |
| **Clean Data & Deduplication** | ✅ **100% Unique tags + repetition counts** | ❌ Raw duplicate spam tags (often 200+ repeats) |
| **Speed** | ⚡ **~1.5 seconds per request** | 🐢 5–15 seconds |
| **TikTok Shop Product Flag** | ✅ **`hasTikTokShopProduct` included** | ❌ Missing or charged as extra add-on |
| **Engagement Rate Metric** | ✅ **Calculated `engagement_rate` %** | ❌ Manual calculation required |
| **Creator Stats** | ✅ Followers, total likes, video count | 💸 Often charged extra ($0.004/creator) |
| **Music / Audio Details** | ✅ Title, author, original audio, CDN URL | ❌ Basic title only |
| **Architecture** | ✅ Native TLS impersonation (No browser overhead) | ❌ Heavy browser memory crashes |

---

## 📖 How to Scrape TikTok Videos & Hashtags (Step-by-Step)

1. **Choose Your Target:**
   - Enter one or more **Hashtags** (e.g. `fyp`, `fitness`, `dropshipping`).
   - Or enter **Search Queries** (e.g. `home decor hacks`, `red light mask`).
   - Or paste specific **Video URLs or numeric IDs** (e.g. `https://www.tiktok.com/@user/video/7695950482107305247`).
2. **Set Limit:** Choose `resultsPerPage` (default: 20, prefilled with 5 for quick testing).
3. **Run & Export:** Click **Start**. Export your clean structured dataset to **CSV, Excel, JSON, Google Sheets**, or integrate directly via API.

---

## 📥 Input Parameters

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `hashtags` | `array[string]` | No | `["fyp"]` | List of hashtags to extract (without `#`). |
| `searchQueries` | `array[string]` | No | `[]` | List of keywords or phrases to search on TikTok. |
| `videoUrls` | `array[string]` | No | `[]` | Direct video URLs or numeric video IDs. |
| `resultsPerPage` | `integer` | No | `20` | Max videos to extract per hashtag or search query (1–1,000). |
| `countryCode` | `string` | No | `"US"` | Market region for localized recommendations (`"US"`, `"GB"`, `"GLOBAL"`). |
| `proxyConfiguration` | `object` | No | Datacenter | Proxy configuration. Apify Datacenter or Residential proxy. |

---

## 📤 Sample Output (JSON)

```json
{
  "id": "7695950482107305247",
  "text": "Top 5 must-have Amazon home gadgets! #amazonfinds #homehacks #fyp",
  "textLanguage": "en",
  "createTime": 1791853117,
  "createTimeISO": "2026-10-13T00:58:37.000Z",
  "isAd": false,
  "hasTikTokShopProduct": true,
  "webVideoUrl": "https://www.tiktok.com/@gadget_review/video/7695950482107305247",
  "authorMeta": {
    "id": "7066463778688123950",
    "name": "gadget_review",
    "nickName": "Gadget Reviews Daily",
    "verified": false,
    "following": 184,
    "fans": 85200,
    "heart": 1250000,
    "video": 240
  },
  "musicMeta": {
    "musicId": "7182930491823",
    "musicName": "Original Sound - Trending Beats",
    "musicAuthor": "BeatMaster"
  },
  "diggCount": 24900,
  "shareCount": 1420,
  "playCount": 380000,
  "commentCount": 385,
  "collectCount": 4200,
  "engagement_rate": 8.13,
  "hashtags": [
    { "name": "amazonfinds", "count": 1 },
    { "name": "homehacks", "count": 1 },
    { "name": "fyp", "count": 1 }
  ]
}
```

---

## 💻 Developer Quickstart (Python & Node.js)

### Python (`apify-client`)

```bash
pip install apify-client
```

```python
import os
from apify_client import ApifyClient

client = ApifyClient(os.getenv("APIFY_TOKEN", "YOUR_APIFY_TOKEN"))

run_input = {
    "hashtags": ["tiktokmademebuyit", "dropshipping"],
    "resultsPerPage": 25,
    "countryCode": "US"
}

run = client.actor("magic-scraper/tiktok-video-hashtag-scraper").call(run_input=run_input)

for video in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(f"Video: {video['webVideoUrl']}")
    print(f"  Creator: @{video['authorMeta']['name']} ({video['authorMeta']['fans']} fans)")
    print(f"  Views: {video['playCount']} | Likes: {video['diggCount']} | ER: {video.get('engagement_rate')}%")
    print(f"  TikTok Shop Product: {video.get('hasTikTokShopProduct')}\n")
```

---

## 💳 Pricing & Free Tier ($5 Monthly Credit)

This Actor uses Apify's **Pay-Per-Result** model:
- **$2.00 per 1,000 video records** ($0.002 per video).
- **$0.001 minimal start fee**.
- Every Apify user receives **$5.00 in free usage credits every month** — scrape up to **2,500 viral videos free each month**!

👉 **[Start Scraping Free on Apify](https://apify.com/magic-scraper/tiktok-video-hashtag-scraper)**
