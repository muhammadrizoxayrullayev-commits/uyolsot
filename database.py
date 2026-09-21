import aiosqlite
import logging
from config import DB_PATH

logger = logging.getLogger(__name__)

async def init_db():
    """Initialize SQLite database tables."""
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                language TEXT DEFAULT 'uz',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        await db.execute("""
            CREATE TABLE IF NOT EXISTS favorites (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                ad_id TEXT NOT NULL,
                title TEXT,
                price TEXT,
                url TEXT,
                photo TEXT,
                area TEXT,
                location TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(user_id, ad_id)
            );
        """)
        await db.commit()
    logger.info("Database initialized successfully at %s", DB_PATH)

async def get_user_language(user_id: int) -> str:
    """Get preferred language for a user, defaults to 'uz'."""
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("SELECT language FROM users WHERE user_id = ?", (user_id,)) as cursor:
            row = await cursor.fetchone()
            if row and row[0]:
                return row[0]
    return "uz"

async def set_user_language(user_id: int, language: str):
    """Set or update preferred language for a user."""
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
            INSERT INTO users (user_id, language) VALUES (?, ?)
            ON CONFLICT(user_id) DO UPDATE SET language = excluded.language
        """, (user_id, language))
        await db.commit()

async def add_favorite(user_id: int, ad_data: dict) -> bool:
    """Add property to user's favorites list."""
    ad_id = str(ad_data.get("id"))
    async with aiosqlite.connect(DB_PATH) as db:
        try:
            await db.execute("""
                INSERT OR IGNORE INTO favorites (user_id, ad_id, title, price, url, photo, area, location)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                user_id,
                ad_id,
                ad_data.get("title", ""),
                ad_data.get("price_str", ""),
                ad_data.get("url", ""),
                ad_data.get("photo", ""),
                str(ad_data.get("area", "")),
                ad_data.get("location_str", "")
            ))
            await db.commit()
            return True
        except Exception as e:
            logger.error("Error adding favorite: %s", e)
            return False

async def remove_favorite(user_id: int, ad_id: str) -> bool:
    """Remove property from user's favorites list."""
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("DELETE FROM favorites WHERE user_id = ? AND ad_id = ?", (user_id, str(ad_id)))
        await db.commit()
        return True

async def is_favorite(user_id: int, ad_id: str) -> bool:
    """Check if property is already in user's favorites."""
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("SELECT 1 FROM favorites WHERE user_id = ? AND ad_id = ?", (user_id, str(ad_id))) as cursor:
            row = await cursor.fetchone()
            return row is not None

async def get_favorites(user_id: int) -> list:
    """Get all favorites saved by the user."""
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute(
            "SELECT ad_id as id, title, price as price_str, url, photo, area, location as location_str FROM favorites WHERE user_id = ? ORDER BY id DESC",
            (user_id,)
        ) as cursor:
            rows = await cursor.fetchall()
            return [dict(r) for r in rows]
