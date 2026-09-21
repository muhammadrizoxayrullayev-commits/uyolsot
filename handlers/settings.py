import logging
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from locales import get_text
from database import get_user_language, get_favorites
from handlers.results import show_card_result
from handlers.keyboards import get_language_keyboard

logger = logging.getLogger(__name__)
settings_router = Router()

@settings_router.message(Command("favorites"))
@settings_router.message(F.text.in_([
    "⭐ Sevimlilar",
    "⭐ Избранное",
    "⭐ Favorites"
]))
async def handle_favorites_button(message: Message, state: FSMContext):
    """Display user's saved favorite ads."""
    await state.clear()
    user_id = message.from_user.id
    lang = await get_user_language(user_id)
    
    favs = await get_favorites(user_id)
    if not favs:
        await message.answer(
            get_text(lang, "favorites_empty"),
            parse_mode="Markdown"
        )
        return
        
    await message.answer(
        get_text(lang, "favorites_title", total=len(favs)),
        parse_mode="Markdown"
    )
    
    # Store in state so pagination works
    await state.update_data(search_results=favs, current_index=0)
    await show_card_result(message, favs, 0, lang, user_id)

@settings_router.message(Command("help"))
async def cmd_help(message: Message):
    user_id = message.from_user.id
    lang = await get_user_language(user_id)
    await message.answer(
        get_text(lang, "help_text"),
        parse_mode="Markdown",
        disable_web_page_preview=True
    )

@settings_router.message(Command("language"))
async def cmd_language(message: Message):
    user_id = message.from_user.id
    lang = await get_user_language(user_id)
    await message.answer(
        get_text(lang, "choose_language"),
        reply_markup=get_language_keyboard(),
        parse_mode="Markdown"
    )
