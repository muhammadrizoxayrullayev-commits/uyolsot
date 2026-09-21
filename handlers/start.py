from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from locales import get_text
from database import get_user_language, set_user_language
from handlers.keyboards import get_language_keyboard, get_main_menu, get_regions_keyboard
from handlers.states import SearchStates

start_router = Router()

@start_router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    """Handle /start command. Show language choice first or main menu if already set."""
    await state.clear()
    user_id = message.from_user.id
    current_lang = await get_user_language(user_id)
    
    # Send language selection keyboard
    welcome_text = (
        "👋 **Xush kelibsiz! / Добро пожаловать! / Welcome!**\n\n"
        "Iltimos, o'zingizga qulay tilni tanlang:\n"
        "Пожалуйста, выберите удобный язык:\n"
        "Please choose your preferred language:"
    )
    await message.answer(
        welcome_text,
        reply_markup=get_language_keyboard(),
        parse_mode="Markdown"
    )

@start_router.callback_query(F.data.startswith("set_lang:"))
async def callback_set_language(callback: CallbackQuery, state: FSMContext):
    """Save selected language and open main menu."""
    lang = callback.data.split(":")[1]
    user_id = callback.from_user.id
    
    await set_user_language(user_id, lang)
    await callback.answer(get_text(lang, "language_saved"))
    
    # Send main menu
    welcome_msg = get_text(lang, "welcome")
    await callback.message.delete()
    await callback.message.answer(
        welcome_msg,
        reply_markup=get_main_menu(lang),
        parse_mode="Markdown"
    )

@start_router.message(F.text.in_([
    "🌐 Tilni almashtirish",
    "🌐 Сменить язык",
    "🌐 Change Language"
]))
async def handle_change_language_button(message: Message, state: FSMContext):
    """Trigger language selection from main menu."""
    await state.clear()
    user_id = message.from_user.id
    lang = await get_user_language(user_id)
    
    await message.answer(
        get_text(lang, "choose_language"),
        reply_markup=get_language_keyboard(),
        parse_mode="Markdown"
    )

@start_router.message(F.text.in_([
    "ℹ️ Yordam va OLX API",
    "ℹ️ Помощь и OLX API",
    "ℹ️ Help & OLX API"
]))
async def handle_help_button(message: Message):
    """Display Help and OLX API details."""
    user_id = message.from_user.id
    lang = await get_user_language(user_id)
    
    help_text = get_text(lang, "help_text")
    await message.answer(help_text, parse_mode="Markdown", disable_web_page_preview=True)

@start_router.callback_query(F.data == "action_main_menu")
async def callback_main_menu(callback: CallbackQuery, state: FSMContext):
    """Return to main menu from any card or step."""
    await state.clear()
    user_id = callback.from_user.id
    lang = await get_user_language(user_id)
    
    await callback.message.answer(
        get_text(lang, "welcome"),
        reply_markup=get_main_menu(lang),
        parse_mode="Markdown"
    )
    await callback.answer()
