import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env file
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

BOT_TOKEN = os.getenv("BOT_TOKEN", "8714802274:AAFWVAzqNjzkFPBOk5FY9hzD_Y4J0WRxFgM")
DB_PATH = str(BASE_DIR / os.getenv("DB_PATH", "data/bot.db"))

OLX_CLIENT_ID = os.getenv("OLX_CLIENT_ID", "")
OLX_CLIENT_SECRET = os.getenv("OLX_CLIENT_SECRET", "")
OLX_API_URL = os.getenv("OLX_API_URL", "https://www.olx.uz/api/open")
