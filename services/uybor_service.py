import asyncio
import logging
import urllib.parse
from typing import List, Optional
from curl_cffi import requests

logger = logging.getLogger(__name__)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Accept": "application/json"
}

def _extract_ad(ad_raw: dict) -> dict:
    """Convert raw Uybor ad object into standardized bot property model."""
    ad_id = str(ad_raw.get("id", ""))
    
    # Title from address and room count
    rooms = str(ad_raw.get("room") or "-")
    address = ad_raw.get("address") or ""
    title = f"{rooms} xona, {address}".strip(" ,") if address else f"{rooms} xonali uy e'loni"
    
    url = f"https://uybor.uz/uz/listings/{ad_id}"
    
    # Price
    price_val = ad_raw.get("price")
    currency = str(ad_raw.get("priceCurrency", "")).upper()
    if price_val:
        formatted_val = f"{int(price_val):,}".replace(",", " ")
        if currency == "USD":
            price_str = f"${formatted_val}"
        elif currency == "UZS":
            price_str = f"{formatted_val} so'm"
        else:
            price_str = f"{formatted_val} {currency}"
    else:
        price_str = "Kelishilgan"
        
    # Photos
    media = ad_raw.get("media", [])
    photo_urls = [m.get("url") for m in media if m.get("url")]
    main_photo = photo_urls[0] if photo_urls else None
    
    # Area
    area = str(ad_raw.get("square") or "Ko'rsatilmagan")
    
    # Floor
    floor = ad_raw.get("floor") or "-"
    floor_total = ad_raw.get("floorTotal") or ""
    floor_str = f"{floor}/{floor_total}" if floor_total else f"{floor}"
    
    # Repair
    repair_raw = ad_raw.get("repair", "")
    repair_clean = "Mavjud"
    if repair_raw in ["custom", "euro"]:
        repair_clean = "💎 Yevroremont / Yangi"
    elif repair_raw in ["no", "karobka", "rough"]:
        repair_clean = "🧱 Qora suvoq / Korobka"
    elif repair_raw:
        repair_clean = "🛠 O'rtacha / Yaxshi"
        
    created_time = ad_raw.get("createdAt", "")[:10] if ad_raw.get("createdAt") else ""
    
    return {
        "id": f"uybor_{ad_id}",
        "title": f"🔵 [Uybor.uz] {title}",
        "url": url,
        "price_str": price_str,
        "location_str": address,
        "photo": main_photo,
        "photos": photo_urls,
        "area": area,
        "rooms": rooms,
        "floor": floor_str,
        "repair": repair_clean,
        "date": created_time,
        "raw_params": {}
    }

def _sync_fetch_uybor(
    property_type: str = "any",
    region_slug: str = "tashkent",
    district_query: str = "",
    district_id: str = "",
    mahalla: str = "",
    area_min: Optional[int] = None,
    area_max: Optional[int] = None,
    price_min: Optional[int] = None,
    price_max: Optional[int] = None,
    page: int = 1
) -> List[dict]:
    # Determine base category
    if property_type == "house":
        category = "sale-houses"
    elif property_type == "apartment":
        category = "sale-apartments"
    else:
        # Defaults to apartments if any
        category = "sale-apartments"

    query_params = {
        "category": category,
        "page": page
    }
    
    if area_min:
        query_params["squareFrom"] = area_min
    if area_max:
        query_params["squareTo"] = area_max
    if price_min:
        query_params["priceFrom"] = price_min
    if price_max:
        query_params["priceTo"] = price_max

    url = "https://api.uybor.uz/api/v1/listings?" + urllib.parse.urlencode(query_params)
    logger.info("Fetching Uybor API URL: %s", url)
    
    try:
        response = requests.get(url, impersonate="chrome120", headers=HEADERS, timeout=18)
        if response.status_code != 200:
            logger.warning("Uybor returned status code: %s", response.status_code)
            return []
            
        data = response.json()
        results_raw = data.get("results", [])
        
        results = []
        for ad_raw in results_raw:
            try:
                ad = _extract_ad(ad_raw)
                
                # Filter by text (district/mahalla) client side if provided
                if district_id or district_query or mahalla:
                    desc = ad_raw.get("description") or ""
                    text_content = (ad.get("location_str", "") + " " + desc).lower()
                    
                    if district_id or district_query:
                        clean_did = district_id.replace("_", " ").lower() if district_id else ""
                        clean_dq = district_query.lower().replace("ский", "").replace(" tumani", "").replace(" район", "") if district_query else ""
                        
                        match_found = False
                        if clean_did and clean_did in text_content:
                            match_found = True
                        if not match_found and clean_dq and clean_dq in text_content:
                            match_found = True
                            
                        if not match_found:
                            continue

                    if mahalla and mahalla.lower() not in text_content:
                        continue

                results.append(ad)
            except Exception as ex:
                logger.error("Error extracting Uybor ad: %s", ex)
                continue
                
        return results
    except Exception as e:
        logger.error("Error fetching Uybor data: %s", e)
        return []

async def search_uybor_properties(
    property_type: str = "any",
    region_slug: str = "tashkent",
    district_query: str = "",
    district_id: str = "",
    mahalla: str = "",
    area_min: Optional[int] = None,
    area_max: Optional[int] = None,
    repair: str = "any",
    price_min: Optional[int] = None,
    price_max: Optional[int] = None,
    page: int = 1
) -> List[dict]:
    """
    Fetch properties from Uybor.uz using their public API.
    """
    ads = await asyncio.to_thread(
        _sync_fetch_uybor,
        property_type=property_type,
        region_slug=region_slug,
        district_query=district_query,
        district_id=district_id,
        mahalla=mahalla,
        area_min=area_min,
        area_max=area_max,
        price_min=price_min,
        price_max=price_max,
        page=page
    )
    
    # Client side filtering for repair type
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
                if any(k in repair_str for k in ["чернов", "qora", "без ремонт", "remontsiz", "требует", "korobka"]):
                    filtered.append(ad)
            else:
                filtered.append(ad)
        if filtered:
            ads = filtered
            
    return ads
