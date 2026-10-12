"""
Telegram Channels Scraper & Parser for Real Estate Listings.
Extracts live public posts from channels like @realestatemalak and @uzqurilish.
"""

import re
import html
import time
import logging
import urllib.request
import asyncio
from typing import List, Dict, Any, Optional

logger = logging.getLogger(__name__)

CHANNELS = [
    "suniyintellektda_0dan_natija",
    "davronrealtor_jiloy",
    "Uy_joyim1",
    "elyor_estate",
    "raupovrealty",
    "sotildi_uy",
    "uybozortv",
    "makonrealty_group",
    "realestatemalak",
    "uzqurilish"
]

# Cache channel posts for 15 minutes
_POSTS_CACHE = {
    "timestamp": 0,
    "posts": []
}

def _parse_channel_posts(channel_name: str) -> List[dict]:
    """Fetch and parse latest posts from public Telegram channel web preview."""
    url = f"https://t.me/s/{channel_name}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Accept-Language": "ru,uz,en;q=0.9"
    }
    
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=12) as res:
            content = res.read().decode("utf-8", errors="ignore")
            
        msg_blocks = re.findall(
            r'<div class="tgme_widget_message_wrap[^"]*"[^>]*>.*?<div class="tgme_widget_message_footer',
            content,
            re.DOTALL
        )
        
        parsed_posts = []
        for block in msg_blocks:
            # Extract text
            text_match = re.search(r'<div class="tgme_widget_message_text[^>]*>(.*?)</div>', block, re.DOTALL)
            if not text_match:
                continue
                
            raw_text = text_match.group(1)
            clean_text = re.sub(r'<br\s*/?>', '\n', raw_text)
            clean_text = re.sub(r'<[^>]+>', '', clean_text)
            clean_text = html.unescape(clean_text).strip()
            
            if len(clean_text) < 15:
                continue
                
            # Extract photo
            photo_match = re.search(r'background-image:url\(\'([^\']+)\'\)', block)
            photo = photo_match.group(1) if photo_match else None
            
            # Extract post link
            link_match = re.search(r'<a class="tgme_widget_message_date" href="([^"]+)"', block)
            post_link = link_match.group(1) if link_match else f"https://t.me/{channel_name}"
            
            # Extract post ID
            msg_id_match = re.search(r'/([^/?#]+)$', post_link)
            msg_id = msg_id_match.group(1) if msg_id_match else str(hash(clean_text))
            
            # Extract title (first line)
            lines = [l.strip() for l in clean_text.split('\n') if l.strip()]
            title = lines[0] if lines else f"Uy e'loni (@{channel_name})"
            if len(title) > 90:
                title = title[:87] + "..."
                
            # Extract Area (m2 / кв.м / сот / sotix)
            area_str = "-"
            area_num = None
            area_match = re.search(r'(?:площадь|maydoni|квадрат|общая площадь)?\s*[:\-]?\s*(\d+(?:[.,]\d+)?)\s*(?:м2|м²|кв\.?\s*м|sqm)', clean_text, re.IGNORECASE)
            if area_match:
                val = area_match.group(1).replace(",", ".")
                try:
                    area_num = int(float(val))
                    area_str = f"{area_num}"
                except ValueError:
                    pass
            elif "сот" in clean_text.lower():
                sot_match = re.search(r'(\d+(?:[.,]\d+)?)\s*(?:сот|сотых|sotix)', clean_text, re.IGNORECASE)
                if sot_match:
                    try:
                        sot_val = float(sot_match.group(1).replace(",", "."))
                        area_num = int(sot_val * 100)
                        area_str = f"{sot_val} sotix (~{area_num} m²)"
                    except ValueError:
                        pass

            # Extract Price ($ or so'm)
            price_str = "Kelishilgan (Kanalda ko'ring)"
            price_num = None
            price_usd_match = re.search(r'(?:цена|narxi|стоимость|стартовая)?\s*[:\-]?\s*\$?\s*(\d{1,3}(?:[ ,]\d{3})+|\d{2,6})\s*(?:\$|usd|у\.?е|dollar)', clean_text, re.IGNORECASE)
            if price_usd_match:
                raw_p = price_usd_match.group(1).replace(" ", "").replace(",", "")
                try:
                    price_num = int(raw_p)
                    price_str = f"${price_num:,}".replace(",", " ")
                except ValueError:
                    pass
            else:
                price_uzs_match = re.search(r'(\d{1,3}(?:[ ,]\d{3})+|\d{4,9})\s*(?:сум|so\'?m|uzs)', clean_text, re.IGNORECASE)
                if price_uzs_match:
                    raw_p = price_uzs_match.group(1).replace(" ", "").replace(",", "")
                    try:
                        p_val = int(raw_p)
                        price_str = f"{p_val:,} so'm".replace(",", " ")
                    except ValueError:
                        pass
                        
            # Rooms
            rooms = "-"
            rooms_match = re.search(r'(?:комнат|xonalar|xona|комн)?\s*[:\-]?\s*(\d+)\s*(?:комн|хона|xona)?', clean_text, re.IGNORECASE)
            if rooms_match and int(rooms_match.group(1)) <= 12:
                rooms = rooms_match.group(1)
                
            # Floor
            floor = "-"
            floor_match = re.search(r'(?:этаж|qavat)?\s*[:\-]?\s*(\d+)\s*(?:из|/|\s*dan)?\s*(\d+)?\s*(?:этаж|qavat)?', clean_text, re.IGNORECASE)
            if floor_match:
                f1 = floor_match.group(1)
                f2 = floor_match.group(2)
                floor = f"{f1}/{f2}" if f2 else f1
                
            # Repair
            repair = "Mavjud"
            lower_txt = clean_text.lower()
            if any(w in lower_txt for w in ["евро", "люкс", "yevro", "дизайнер", "новый", "yangi"]):
                repair = "💎 Yevroremont / Yangi"
            elif any(w in lower_txt for w in ["чернов", "qora", "без ремонт", "remontsiz", "karobka", "коробка"]):
                repair = "🧱 Qora suvoq / Korobka"
            elif any(w in lower_txt for w in ["средн", "o'rta", "хорош", "yaxshi", "косметич"]):
                repair = "🛠 O'rtacha / Yaxshi"
                
            # Location
            location_str = f"Toshkent (@{channel_name})"
            for loc in ["Мирзо-Улугбек", "Чиланзар", "Юнусабад", "Яккасарай", "Мирабад", "Яшнабад", "Алмазар", "Шайхантахур", "Учтепа", "Сергели", "Янгихаёт", "Бектемир"]:
                if loc.lower() in lower_txt:
                    location_str = f"Toshkent, {loc} tumani"
                    break
                    
            ad = {
                "id": f"tg_{channel_name}_{msg_id}",
                "title": f"✈️ [@{channel_name}] {title}",
                "url": post_link,
                "price_str": price_str,
                "price_num": price_num,
                "location_str": location_str,
                "photo": photo,
                "photos": [photo] if photo else [],
                "area": area_str,
                "area_num": area_num,
                "rooms": rooms,
                "floor": floor,
                "repair": repair,
                "date": "Telegram kanal",
                "source": "telegram",
                "channel": channel_name,
                "full_text": clean_text
            }
            parsed_posts.append(ad)
            
        logger.info("Fetched %d posts from Telegram channel @%s", len(parsed_posts), channel_name)
        return parsed_posts
    except Exception as e:
        logger.error("Error scraping Telegram channel @%s: %s", channel_name, e)
        return []

def _get_all_cached_channel_posts() -> List[dict]:
    """Get posts with 15-minute cache."""
    now = time.time()
    if now - _POSTS_CACHE["timestamp"] < 900 and _POSTS_CACHE["posts"]:
        return _POSTS_CACHE["posts"]
        
    all_posts = []
    for ch in CHANNELS:
        posts = _parse_channel_posts(ch)
        all_posts.extend(posts)
        
    _POSTS_CACHE["timestamp"] = now
    _POSTS_CACHE["posts"] = all_posts
    return all_posts

async def search_channel_properties(
    district_query: str = "",
    district_id: str = "",
    mahalla: str = "",
    property_type: str = "any",
    area_min: Optional[int] = None,
    area_max: Optional[int] = None,
    price_min: Optional[int] = None,
    price_max: Optional[int] = None,
    repair: str = "any"
) -> List[dict]:
    """Filter Telegram channel posts based on user criteria."""
    posts = await asyncio.to_thread(_get_all_cached_channel_posts)
    if not posts:
        return []
        
    matched = []
    
    # Clean district_id for matching
    clean_district_id = district_id.replace("_", " ").lower() if district_id else ""
    
    for p in posts:
        txt = p["full_text"].lower()
        
        # Match district keywords
        if clean_district_id:
            clean_dq = district_query.lower().replace("ский", "").replace(" tumani", "").replace(" район", "") if district_query else ""
            if clean_district_id not in txt and (not clean_dq or clean_dq not in txt):
                continue
        elif district_query:
            clean_d = district_query.lower().replace("ский", "").replace(" tumani", "").replace(" район", "")
            if clean_d and clean_d not in txt:
                continue
                
        if mahalla and mahalla.lower() not in txt:
            continue
            
        # Match property type
        if property_type == "apartment" and any(k in txt for k in ["участок", "hovli", "uchastka", "дача", "dacha"]):
            continue
        elif property_type == "house" and any(k in txt for k in ["квартир", "kvartira", "этаж", "новостройк"]):
            continue
            
        # Match area
        if p["area_num"]:
            if area_min and p["area_num"] < (area_min * 0.85):
                continue
            if area_max and p["area_num"] > (area_max * 1.15):
                continue
                
        # Match price
        if p["price_num"]:
            if price_min and p["price_num"] < (price_min * 0.85):
                continue
            if price_max and p["price_num"] > (price_max * 1.15):
                continue
                
        matched.append(p)
        
    # If filtered matched nothing specific, return top recent channel posts to enrich search results
    if not matched:
        return posts[:3]
        
    return matched
