import logging
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InputMediaPhoto
from aiogram.fsm.context import FSMContext

from locales import get_text
from database import get_user_language, add_favorite, remove_favorite, is_favorite
from handlers.keyboards import get_card_keyboard

logger = logging.getLogger(__name__)
results_router = Router()

def format_card_caption(ad: dict, lang: str) -> str:
    """Format single property card text with rich emojis and data."""
    title = get_text(lang, "card_title", title=ad.get("title", ""))
    price = get_text(lang, "card_price", price=ad.get("price_str", "Kelishilgan"))
    area = get_text(lang, "card_area", area=ad.get("area", "-"))
    rooms = get_text(lang, "card_rooms", rooms=ad.get("rooms", "-"))
    floor = get_text(lang, "card_floor", floor=ad.get("floor", "-"))
    repair = get_text(lang, "card_repair", repair=ad.get("repair", "-"))
    location = get_text(lang, "card_location", location=ad.get("location_str", "-"))
    date = get_text(lang, "card_date", date=ad.get("date", "-"))
    
    caption = (
        f"{title}\n\n"
        f"{price}\n"
        f"{area}\n"
        f"{rooms} | {floor}\n"
        f"{repair}\n"
        f"{location}\n"
        f"{date}"
    )
    return caption

async def show_card_result(message: Message, results: list, current_idx: int, lang: str, user_id: int):
    """Send or edit property card."""
    if not results or current_idx >= len(results):
        return
        
    ad = results[current_idx]
    caption = format_card_caption(ad, lang)
    is_saved = await is_favorite(user_id, ad.get("id"))
    
    kb = get_card_keyboard(
        lang=lang,
        ad_id=ad.get("id"),
        url=ad.get("url"),
        current_idx=current_idx,
        total_count=len(results),
        is_saved=is_saved,
        source=ad.get("source", "olx")
    )
    
    photo_url = ad.get("photo")
    if photo_url:
        try:
            await message.answer_photo(
                photo=photo_url,
                caption=caption,
                reply_markup=kb,
                parse_mode="Markdown"
            )
            return
        except Exception as e:
            logger.warning("Could not send photo directly: %s", e)
            
    # Fallback to plain text message
    await message.answer(
        caption,
        reply_markup=kb,
        parse_mode="Markdown",
        disable_web_page_preview=False
    )

@results_router.callback_query(F.data.startswith("nav:"))
async def callback_card_navigation(callback: CallbackQuery, state: FSMContext):
    """Handle previous / next card pagination."""
    new_idx = int(callback.data.split(":")[1])
    data = await state.get_data()
    results = data.get("search_results", [])
    
    if not results or new_idx < 0 or new_idx >= len(results):
        await callback.answer()
        return
        
    user_id = callback.from_user.id
    lang = await get_user_language(user_id)
    ad = results[new_idx]
    caption = format_card_caption(ad, lang)
    is_saved = await is_favorite(user_id, ad.get("id"))
    
    kb = get_card_keyboard(
        lang=lang,
        ad_id=ad.get("id"),
        url=ad.get("url"),
        current_idx=new_idx,
        total_count=len(results),
        is_saved=is_saved,
        source=ad.get("source", "olx")
    )
    
    await state.update_data(current_index=new_idx)
    
    photo_url = ad.get("photo")
    try:
        if photo_url and callback.message.photo:
            # Edit existing photo message
            media = InputMediaPhoto(media=photo_url, caption=caption, parse_mode="Markdown")
            await callback.message.edit_media(media=media, reply_markup=kb)
        elif not photo_url and callback.message.photo:
            # Switch from photo to text message
            await callback.message.delete()
            await callback.message.answer(caption, reply_markup=kb, parse_mode="Markdown")
        else:
            await callback.message.edit_text(caption, reply_markup=kb, parse_mode="Markdown")
    except Exception as e:
        logger.info("Re-sending card due to edit limitation: %s", e)
        try:
            await callback.message.delete()
        except Exception:
            pass
        await show_card_result(callback.message, results, new_idx, lang, user_id)
        
    await callback.answer()

@results_router.callback_query(F.data.startswith("fav_add:"))
async def callback_add_favorite(callback: CallbackQuery, state: FSMContext):
    """Save ad to favorites."""
    parts = callback.data.split(":")
    ad_id = parts[1]
    current_idx = int(parts[2])
    
    data = await state.get_data()
    results = data.get("search_results", [])
    
    user_id = callback.from_user.id
    lang = await get_user_language(user_id)
    
    ad = None
    for item in results:
        if str(item.get("id")) == str(ad_id):
            ad = item
            break
            
    if ad:
        await add_favorite(user_id, ad)
        await callback.answer(get_text(lang, "saved_to_fav"), show_alert=False)
        
        # Update button to remove button
        kb = get_card_keyboard(
            lang=lang,
            ad_id=ad_id,
            url=ad.get("url"),
            current_idx=current_idx,
            total_count=len(results),
            is_saved=True,
            source=ad.get("source", "olx")
        )
        try:
            await callback.message.edit_reply_markup(reply_markup=kb)
        except Exception:
            pass
    else:
        await callback.answer()

@results_router.callback_query(F.data.startswith("fav_del:"))
async def callback_remove_favorite(callback: CallbackQuery, state: FSMContext):
    """Remove ad from favorites."""
    parts = callback.data.split(":")
    ad_id = parts[1]
    current_idx = int(parts[2])
    
    data = await state.get_data()
    results = data.get("search_results", [])
    
    user_id = callback.from_user.id
    lang = await get_user_language(user_id)
    
    await remove_favorite(user_id, ad_id)
    await callback.answer(get_text(lang, "removed_from_fav"), show_alert=False)
    
    ad = next((item for item in results if str(item.get("id")) == str(ad_id)), None)
    url = ad.get("url") if ad else "https://www.olx.uz"
    
    kb = get_card_keyboard(
        lang=lang,
        ad_id=ad_id,
        url=url,
        current_idx=current_idx,
        total_count=len(results),
        is_saved=False,
        source=ad.get("source", "olx") if ad else "olx"
    )
    try:
        await callback.message.edit_reply_markup(reply_markup=kb)
    except Exception:
        pass

@results_router.callback_query(F.data == "noop")
async def callback_noop(callback: CallbackQuery):
    """Dummy callback for counter button."""
    await callback.answer()
