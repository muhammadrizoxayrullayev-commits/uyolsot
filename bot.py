import sys
import asyncio
import logging

# Ensure UTF-8 output encoding on Windows consoles
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import BotCommand

from config import BOT_TOKEN
from database import init_db
from handlers.start import start_router
from handlers.search import search_router
from handlers.results import results_router
from handlers.settings import settings_router

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(name)s - %(message)s"
)
logger = logging.getLogger(__name__)

async def set_bot_commands(bot: Bot):
    """Set bot commands list in Telegram menu."""
    commands = [
        BotCommand(command="start", description="🔄 Botni qayta ishga tushirish / Запуск"),
        BotCommand(command="search", description="🔍 Uy qidirish / Поиск недвижимости"),
        BotCommand(command="favorites", description="⭐ Sevimlilar / Избранное"),
        BotCommand(command="language", description="🌐 Tilni almashtirish / Сменить язык"),
        BotCommand(command="help", description="ℹ️ Yordam va OLX API / Помощь"),
    ]
    await bot.set_my_commands(commands)

async def main():
    logger.info("Initializing Uy Ol-Sot Telegram Bot...")
    
    # Initialize SQLite database
    await init_db()
    
    # Initialize Bot & Dispatcher
    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN)
    )
    dp = Dispatcher(storage=MemoryStorage())
    
    # Register routers
    dp.include_router(start_router)
    dp.include_router(search_router)
    dp.include_router(results_router)
    dp.include_router(settings_router)
    
    # Set bot commands menu
    await set_bot_commands(bot)
    
    # Check bot connection
    me = await bot.get_me()
    logger.info("Bot successfully authenticated as: @%s (%s)", me.username, me.first_name)
    print(f"\n==========================================")
    print(f"🚀 Uy Ol-Sot Bot ishga tushdi: @{me.username}")
    print(f"==========================================\n")
    
    # Start polling
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot stopped.")
