"""
OLX Partner Official API Integration (OAuth 2.0 Client Credentials).
Used if user configures OLX_CLIENT_ID and OLX_CLIENT_SECRET in .env.
"""

import httpx
import logging
from config import OLX_CLIENT_ID, OLX_CLIENT_SECRET, OLX_API_URL

logger = logging.getLogger(__name__)

class OLXApiClient:
    def __init__(self):
        self.client_id = OLX_CLIENT_ID
        self.client_secret = OLX_CLIENT_SECRET
        self.base_url = OLX_API_URL.rstrip("/")
        self.token = None

    def is_configured(self) -> bool:
        """Check whether official credentials are provided."""
        return bool(self.client_id and self.client_secret)

    async def authenticate(self) -> bool:
        """Authenticate with OLX OAuth2 to get bearer access token."""
        if not self.is_configured():
            return False
            
        token_url = f"{self.base_url}/oauth/token"
        payload = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "scope": "read write"
        }
        
        try:
            async with httpx.AsyncClient(timeout=10) as client:
                res = await client.post(token_url, json=payload)
                if res.status_code == 200:
                    data = res.json()
                    self.token = data.get("access_token")
                    logger.info("Successfully authenticated with official OLX API!")
                    return True
                else:
                    logger.warning("OLX API auth failed with status %d: %s", res.status_code, res.text)
                    return False
        except Exception as e:
            logger.error("Error connecting to OLX API: %s", e)
            return False

    async def get_my_adverts(self) -> list:
        """Fetch user adverts if partner account is active."""
        if not self.token and not await self.authenticate():
            return []
            
        url = f"{self.base_url}/api/partner/adverts"
        headers = {"Authorization": f"Bearer {self.token}", "Version": "2.0"}
        
        try:
            async with httpx.AsyncClient(timeout=10) as client:
                res = await client.get(url, headers=headers)
                if res.status_code == 200:
                    return res.json().get("data", [])
        except Exception as e:
            logger.error("Error fetching partner adverts: %s", e)
            
        return []
