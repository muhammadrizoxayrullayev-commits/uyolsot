import asyncio
import logging
from typing import List, Optional

logger = logging.getLogger(__name__)

from services.olx_service import search_olx_properties

async def search_all_properties(
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
    Aggregates properties from all available sources: OLX, Telegram Channels, Uybor, etc.
    """
    all_ads = []
    
    # 1. Fetch from OLX (which currently also fetches from Telegram channels internally)
    try:
        olx_and_channel_ads = await search_olx_properties(
            property_type=property_type,
            region_slug=region_slug,
            district_query=district_query,
            mahalla=mahalla,
            area_min=area_min,
            area_max=area_max,
            repair=repair,
            price_min=price_min,
            price_max=price_max,
            page=page
        )
        all_ads.extend(olx_and_channel_ads)
    except Exception as e:
        logger.error(f"Error fetching from OLX/Channels: {e}")

    # 2. Fetch from Uybor.uz
    try:
        from services.uybor_service import search_uybor_properties
        uybor_ads = await search_uybor_properties(
            property_type=property_type,
            region_slug=region_slug,
            district_query=district_query,
            mahalla=mahalla,
            area_min=area_min,
            area_max=area_max,
            repair=repair,
            price_min=price_min,
            price_max=price_max,
            page=page
        )
        all_ads.extend(uybor_ads)
    except Exception as e:
        logger.error(f"Error fetching from Uybor: {e}")

    # TODO: Fetch from Realt24, Realting, Hata, Tezijara, Refar, 1uy, Uya...

    return all_ads
