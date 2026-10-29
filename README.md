# 🎬 TikTok Video & Hashtag Scraper: Posts, Creators, Sounds & Shop Affiliates

[![TikTok Video & Hashtag Scraper](https://apify.com/actor-badge?actor=magic-scraper/tiktok-video-hashtag-scraper)](https://apify.com/magic-scraper/tiktok-video-hashtag-scraper)
![Free Tier](https://img.shields.io/badge/Apify%20Free%20Tier-$5%20Monthly%20Credit-blue?style=flat-square)
![Pay-Per-Result](https://img.shields.io/badge/Pricing-$2.00%20%2F%201K%20videos-blue?style=flat-square)
![No Cookies Required](https://img.shields.io/badge/Cookies-Not%20Required-success?style=flat-square)
![Export](https://img.shields.io/badge/Export-JSON%20|%20CSV%20|%20Excel-orange?style=flat-square)

Python and Node.js examples for the **[TikTok Video & Hashtag Scraper](https://apify.com/magic-scraper/tiktok-video-hashtag-scraper)** on Apify: TikTok videos by hashtag, keyword or URL with views, likes, comments, shares, saves, engagement rate, creator stats, music and a **TikTok Shop product flag** (`hasTikTokShopProduct`).

> ⚡ **No code needed:** 👉 **[Run it in your browser on Apify (free $5 monthly credit)](https://apify.com/magic-scraper/tiktok-video-hashtag-scraper)**

---

## 🎯 Who is this for?

- **Influencer marketing teams** — find creators by niche with follower and engagement data.
- **TikTok Shop sellers & affiliates** — find videos that promote shop products.
- **Social media analysts** — track hashtags, sounds and engagement over time.

---

## 📌 Key Facts

| | |
| :--- | :--- |
| **Pricing** | $2.00 per 1,000 videos + $0.00005 start fee (≈2,500 videos/month inside Apify's free $5 credit) |
| **Run time (measured)** | ~4–8 s for 10 videos of one hashtag |
| **Engagement rate** | `engagement_rate` = (likes + comments + shares + saves) / views × 100 |
| **Hashtags** | De-duplicated `hashtags_list` plus `hashtags` with repetition counts |
| **How it works** | HTTP requests with browser TLS impersonation, no headless browser |
| **Proxy** | Apify Proxy pinned to `countryCode` automatically (except `GLOBAL`) |
| **Login / cookies** | Not required |

---

## 🚀 Quickstart

### Python

```bash
pip install apify-client
export APIFY_TOKEN=your_token   # https://console.apify.com/settings/integrations
python example.py
```

```python
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("magic-scraper/tiktok-video-hashtag-scraper").call(run_input={
    "hashtags": ["tiktokmademebuyit"],
    "resultsPerPage": 20,
})

for v in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(f"@{v['authorMeta']['name']}", v["playCount"], v["engagement_rate"], v["hasTikTokShopProduct"])
```

### Node.js

```javascript
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('magic-scraper/tiktok-video-hashtag-scraper').call({
    searchQueries: ['skincare routine'],
    resultsPerPage: 20,
});
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);
```

---

## 📥 Input

At least one of `hashtags`, `searchQueries` or `videoUrls` is needed.

| Parameter | Type | Default | Description |
| :--- | :--- | :---: | :--- |
| `hashtags` | `array[string]` | `[]` | Hashtags without `#`. |
| `searchQueries` | `array[string]` | `[]` | Keywords to search. |
| `videoUrls` | `array[string]` | `[]` | Video URLs or numeric video IDs. |
| `resultsPerPage` | `integer` | `20` | Videos per hashtag or keyword (1–1000). |
| `countryCode` | `string` | `US` | `US`, `GB`, `DE`, `FR`, `IT`, `ES`, `BR`, `ID` or `GLOBAL`. |
| `proxyConfiguration` | `object` | `{"useApifyProxy": true}` | Apify Proxy, country set from `countryCode`. |

---

## 📤 Output

Main fields: `id`, `text`, `textLanguage`, `createTime`, `createTimeISO`, `isAd`, `hasTikTokShopProduct`, `webVideoUrl`, `authorMeta` (`id`, `name`, `nickName`, `profileUrl`, `verified`, `signature`, `bioLink`, `avatar`, `privateAccount`, `following`, `fans`, `heart`, `video`, `digg`), `musicMeta` (`musicId`, `musicName`, `musicAuthor`, `musicOriginal`, `playUrl`, `coverMediumUrl`), `videoMeta` (`height`, `width`, `duration`, `coverUrl`, `definition`, `format`, `downloadAddr`), `diggCount`, `shareCount`, `playCount`, `collectCount`, `commentCount`, `repostCount`, `hashtags`, `hashtags_list`, `engagement_rate`, `mentions`, `isSlideshow`, `isPinned`, `isSponsored`, `input`, `searchHashtag`, `scraped_at`.

### Sample record (real run, URLs shortened)

```json
{
  "id": "7106886660419259690",
  "text": "#dollartree #craftorganization #tiktokmademebuyit #paintorganization #acrylicpaint #smallbusiness #diy #fyp",
  "createTimeISO": "2022-06-08T15:09:57+00:00",
  "isAd": false,
  "hasTikTokShopProduct": false,
  "webVideoUrl": "https://www.tiktok.com/@cute.by.ke/video/7106886660419259690",
  "authorMeta": {
    "name": "cute.by.ke",
    "nickName": "Karen Yarborough",
    "verified": false,
    "following": 223,
    "fans": 43100,
    "heart": 429000,
    "video": 832
  },
  "musicMeta": {"musicName": "original sound", "musicAuthor": "Candles of Essence", "musicOriginal": true},
  "videoMeta": {"height": 1024, "width": 576, "duration": 29, "definition": "540p", "format": "mp4"},
  "diggCount": 294900,
  "shareCount": 16700,
  "playCount": 3600000,
  "collectCount": 25000,
  "commentCount": 3630,
  "hashtags_list": ["dollartree", "craftorganization", "tiktokmademebuyit", "paintorganization", "acrylicpaint", "smallbusiness", "diy", "fyp"],
  "engagement_rate": 9.45,
  "input": "tiktokmademebuyit",
  "searchHashtag": {"name": "tiktokmademebuyit", "views": 369800000000},
  "scraped_at": "2026-10-29T11:03:48.285527+00:00"
}
```

---

## 🤖 For AI Agents

Call `magic-scraper/tiktok-video-hashtag-scraper` via the [Apify MCP server](https://mcp.apify.com/) or the API with `{"hashtags": ["<tag>"], "resultsPerPage": 20}`. Filter on `hasTikTokShopProduct` to find shop-promoting videos and sort by `engagement_rate` to rank them.

---

## 🔗 Related Scrapers

- [TikTok Shop Search Scraper](https://apify.com/magic-scraper/tiktok-shop-search-scraper) — products by keyword with units sold.
- [TikTok Shop Product Scraper](https://apify.com/magic-scraper/tiktok-shop-product-scraper) — SKU variants, stock and reviews.

---

## 📄 License

MIT — see [LICENSE](LICENSE). This repository contains usage examples; the scraper itself runs on [Apify](https://apify.com/magic-scraper/tiktok-video-hashtag-scraper).
