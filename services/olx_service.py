import asyncio
import json
import logging
import urllib.parse
from typing import List, Dict, Any, Optional
from curl_cffi import requests

logger = logging.getLogger(__name__)

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "ru-RU,ru;q=0.9,uz;q=0.8,en;q=0.7",
    "Sec-Ch-Ua": '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
}

def _parse_prerendered_state(html: str) -> Optional[dict]:
    """Extract and parse window.__PRERENDERED_STATE__ JSON safely from OLX HTML."""
    prefix = 'window.__PRERENDERED_STATE__= "'
    idx = html.find(prefix)
    if idx == -1:
        prefix = 'window.__PRERENDERED_STATE__="'
        idx = html.find(prefix)
    if idx == -1:
        return None

    start = idx + len(prefix)
    end_idx = html.find('";\n', start)
    if end_idx == -1:
        end_idx = html.find('";', start)
    if end_idx == -1:
        return None

    raw_json_str = html[start:end_idx]
    try:
        unescaped = json.loads('"' + raw_json_str + '"')
        data = json.loads(unescaped)
        return data
    except Exception as e:
        logger.error("Error decoding PRERENDERED_STATE: %s", e)
        return None

def _format_price(price_data: dict) -> str:
    """Format price dictionary into a readable human string."""
    if not price_data:
        return "Kelishilgan (Договорная)"
    
    regular = price_data.get("regularPrice", {})
    if regular and regular.get("value"):
        val = regular.get("value", 0)
        curr = regular.get("currencyCode", "")
        # Format with spaces: 120 000
        formatted_val = f"{val:,}".replace(",", " ")
        if curr == "USD":
            return f"${formatted_val}"
        elif curr == "UZS":
            return f"{formatted_val} so'm"
        return f"{formatted_val} {curr}"
        
    display = price_data.get("displayValue")
    if display:
        return display.replace("", "so'm").strip()
        
    return "Kelishilgan"

def _extract_ad(ad_raw: dict) -> dict:
    """Convert raw OLX ad object into standardized bot property model."""
    ad_id = str(ad_raw.get("id", ""))
    title = ad_raw.get("title", "Uy e'loni")
    url = ad_raw.get("url", "")
    if url and not url.startswith("http"):
        url = "https://www.olx.uz" + url
        
    price_str = _format_price(ad_raw.get("price", {}))
    
    # Location
    loc = ad_raw.get("location", {})
    city = loc.get("cityName", "")
    district = loc.get("districtName", "")
    loc_parts = [p for p in [city, district] if p and p != ""]
    location_str = ", ".join(loc_parts) if loc_parts else (loc.get("pathName") or "O'zbekiston")
    # Clean any replacement characters
    location_str = location_str.replace("", "").strip(" ,")
    
    # Photos
    photos = ad_raw.get("photos", [])
    photo_urls = []
    for p in photos:
        if isinstance(p, str):
            photo_urls.append(p)
        elif isinstance(p, dict) and p.get("link"):
            clean_link = p.get("link").replace(";s={width}x{height}", "")
            photo_urls.append(clean_link)
    
    main_photo = photo_urls[0] if photo_urls else None
    
    # Params
    params_list = ad_raw.get("params", [])
    params = {}
    for item in params_list:
        if isinstance(item, dict) and "key" in item:
            val = item.get("value")
            norm_val = item.get("normalizedValue")
            params[item["key"]] = {"value": val, "normalized": norm_val}
            
    # Area
    area = params.get("total_area", {}).get("value") or params.get("total_area", {}).get("normalized")
    if not area:
        area = "Ko'rsatilmagan"
        
    # Rooms
    rooms = params.get("number_of_rooms", {}).get("value") or params.get("number_of_rooms", {}).get("normalized") or "-"
    
    # Floor
    floor = params.get("floor", {}).get("value") or "-"
    total_floors = params.get("total_floors", {}).get("value") or ""
    floor_str = f"{floor}/{total_floors}" if total_floors and total_floors != "-" else f"{floor}"
    
    # Repair
    repair_val = params.get("repairs", {}).get("value") or params.get("repairs", {}).get("normalized") or "Ko'rsatilmagan"
    repair_clean = str(repair_val).replace("", "").strip()
    if not repair_clean:
        repair_clean = "Mavjud"
        
    # Date
    created_time = ad_raw.get("createdTime", "")[:10] if ad_raw.get("createdTime") else ""
    
    return {
        "id": ad_id,
        "title": title.replace("", "").strip(),
        "url": url,
        "price_str": price_str,
        "location_str": location_str,
        "photo": main_photo,
        "photos": photo_urls,
        "area": area,
        "rooms": rooms,
        "floor": floor_str,
        "repair": repair_clean,
        "date": created_time,
        "raw_params": params
    }

def _sync_fetch_olx(
    property_type: str = "any",
    region_slug: str = "tashkent",
    district_query: str = "",
    mahalla: str = "",
    area_min: Optional[int] = None,
    area_max: Optional[int] = None,
    price_min: Optional[int] = None,
    price_max: Optional[int] = None,
    page: int = 1
) -> List[dict]:
    """Synchronous worker that performs requests with curl_cffi."""
    # Determine base category
    if property_type == "house":
        category_path = "nedvizhimost/doma/prodazha"
    elif property_type == "apartment":
        category_path = "nedvizhimost/kvartiry/prodazha"
    else:
        # General real estate
        category_path = "nedvizhimost"

    url = f"https://www.olx.uz/{category_path}/{region_slug}/"
    
    query_params = {}
    
    # Build text search query (combine district and mahalla if provided)
    search_terms = []
    if district_query:
        search_terms.append(district_query)
    if mahalla:
        search_terms.append(mahalla)
        
    if search_terms:
        query_params["q"] = " ".join(search_terms)
        
    if area_min is not None and area_min > 0:
        query_params["search[filter_float_total_area:from]"] = area_min
    if area_max is not None and area_max > 0:
        query_params["search[filter_float_total_area:to]"] = area_max
        
    if price_min is not None and price_min > 0:
        query_params["search[filter_float_price:from]"] = price_min
    if price_max is not None and price_max > 0:
        query_params["search[filter_float_price:to]"] = price_max
        
    if page > 1:
        query_params["page"] = page
        
    if query_params:
        url += "?" + urllib.parse.urlencode(query_params)
        
    logger.info("Fetching OLX search URL: %s", url)
    
    try:
        response = requests.get(url, impersonate="chrome120", headers=HEADERS, timeout=18)
        if response.status_code != 200:
            logger.warning("OLX returned status code: %s", response.status_code)
            return []
            
        data = _parse_prerendered_state(response.text)
        if not data:
            logger.warning("Could not parse PRERENDERED_STATE from page")
            return []
            
        listing = data.get("listing", {}).get("listing", {})
        ads_raw = listing.get("ads", [])
        
        results = []
        for ad_raw in ads_raw:
            try:
                ad = _extract_ad(ad_raw)
                results.append(ad)
            except Exception as ex:
                logger.error("Error extracting ad: %s", ex)
                continue
                
        return results
    except Exception as e:
        logger.error("Error fetching OLX data: %s", e)
        return []

async def search_olx_properties(
    property_type: str = "any",
    region_slug: str = "tashkent",
    district_query: str = "",
    mahalla: str = "",
    area_min: Optional[int] = None,
    area_max: Optional[int] = None,
    repair: str = "any",
    price_min: Optional[int] = None,
    price_max: Optional[int] = None,
    page: int = 1
) -> List[dict]:
    """
    Asynchronous wrapper that runs the scraper in a threadpool to prevent blocking the event loop.
    Applies post-filtering for repair and area tolerances.
    """
    ads = await asyncio.to_thread(
        _sync_fetch_olx,
        property_type=property_type,
        region_slug=region_slug,
        district_query=district_query,
        mahalla=mahalla,
        area_min=area_min,
        area_max=area_max,
        price_min=price_min,
        price_max=price_max,
        page=page
    )
    
    # If repair filter is applied, perform intelligent filtering
    if repair and repair != "any":
        filtered = []
        for ad in ads:
            repair_str = ad.get("repair", "").lower()
            if repair == "euro":
                if any(k in repair_str for k in ["евро", "yevro", "люкс", "дизайнер", "новый", "yangi"]):
                    filtered.append(ad)
            elif repair == "medium":
                if any(k in repair_str for k in ["средн", "o'rta", "хорош", "yaxshi", "косметич"]):
                    filtered.append(ad)
            elif repair == "none":
                if any(k in repair_str for k in ["чернов", "qora", "без ремонт", "remontsiz", "требует"]):
                    filtered.append(ad)
            else:
                filtered.append(ad)
        # If strict repair filter resulted in 0 ads, keep all ads rather than showing nothing
        if filtered:
            return filtered
            
    return ads
