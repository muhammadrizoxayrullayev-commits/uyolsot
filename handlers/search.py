import re
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from locales import get_text
from database import get_user_language
from data.regions import get_region_by_id, get_district_by_id
from handlers.states import SearchStates
from handlers.keyboards import (
    get_regions_keyboard,
    get_districts_keyboard,
    get_skip_keyboard,
    get_mahalla_keyboard,
    get_property_type_keyboard,
    get_area_keyboard,
    get_repair_keyboard,
    get_price_keyboard,
    get_main_menu
)
from services.aggregator_service import search_all_properties
from handlers.results import show_card_result

search_router = Router()

@search_router.message(Command("search"))
@search_router.message(F.text.in_([
    "🔍 Uy qidirish",
    "🔍 Поиск недвижимости",
    "🔍 Search Property"
]))
async def start_search_flow(message: Message, state: FSMContext):
    """Start multi-step search wizard."""
    await state.clear()
    user_id = message.from_user.id
    lang = await get_user_language(user_id)
    
    await state.set_state(SearchStates.waiting_for_region)
    await message.answer(
        get_text(lang, "step_region"),
        reply_markup=get_regions_keyboard(lang),
        parse_mode="Markdown"
    )

@search_router.callback_query(F.data == "action_new_search")
async def callback_new_search(callback: CallbackQuery, state: FSMContext):
    """Restart search from any card."""
    await state.clear()
    user_id = callback.from_user.id
    lang = await get_user_language(user_id)
    
    await state.set_state(SearchStates.waiting_for_region)
    await callback.message.answer(
        get_text(lang, "step_region"),
        reply_markup=get_regions_keyboard(lang),
        parse_mode="Markdown"
    )
    await callback.answer()

@search_router.callback_query(F.data == "cancel_search")
async def callback_cancel_search(callback: CallbackQuery, state: FSMContext):
    """Cancel active search."""
    await state.clear()
    user_id = callback.from_user.id
    lang = await get_user_language(user_id)
    
    await callback.message.edit_text(
        f"❌ {get_text(lang, 'btn_cancel')}",
        reply_markup=None
    )
    await callback.message.answer(
        get_text(lang, "welcome"),
        reply_markup=get_main_menu(lang),
        parse_mode="Markdown"
    )
    await callback.answer()

# --- Step 1: Region Selection ---
@search_router.callback_query(SearchStates.waiting_for_region, F.data.startswith("reg:"))
async def process_region_selection(callback: CallbackQuery, state: FSMContext):
    region_id = callback.data.split(":")[1]
    region = get_region_by_id(region_id)
    if not region:
        await callback.answer("Region not found", show_alert=True)
        return
        
    user_id = callback.from_user.id
    lang = await get_user_language(user_id)
    
    await state.update_data(
        region_id=region_id,
        region_slug=region["olx_slug"],
        region_name=region.get(f"name_{lang}", region["name_uz"])
    )
    
    await state.set_state(SearchStates.waiting_for_district)
    text = get_text(lang, "step_district", region=region.get(f"name_{lang}", region["name_uz"]))
    await callback.message.edit_text(
        text,
        reply_markup=get_districts_keyboard(region_id, lang),
        parse_mode="Markdown"
    )
    await callback.answer()

@search_router.callback_query(F.data == "back_to_regions")
async def back_to_regions(callback: CallbackQuery, state: FSMContext):
    user_id = callback.from_user.id
    lang = await get_user_language(user_id)
    
    await state.set_state(SearchStates.waiting_for_region)
    await callback.message.edit_text(
        get_text(lang, "step_region"),
        reply_markup=get_regions_keyboard(lang),
        parse_mode="Markdown"
    )
    await callback.answer()

# --- Step 2: District Selection ---
@search_router.callback_query(SearchStates.waiting_for_district, F.data.startswith("dist:"))
async def process_district_selection(callback: CallbackQuery, state: FSMContext):
    district_val = callback.data.split(":")[1]
    data = await state.get_data()
    region_id = data.get("region_id", "tashkent_city")
    user_id = callback.from_user.id
    lang = await get_user_language(user_id)
    
    if district_val == "all":
        district_query = ""
        district_name = get_text(lang, "btn_all")
    else:
        district = get_district_by_id(region_id, district_val)
        district_query = district["query"] if district else ""
        district_name = district.get(f"name_{lang}", district["name_uz"]) if district else ""
        
    await state.update_data(
        district_id=district_val,
        district_query=district_query,
        district_name=district_name
    )
    
    await state.set_state(SearchStates.waiting_for_mahalla)
    await callback.message.edit_text(
        get_text(lang, "step_mahalla"),
        reply_markup=get_mahalla_keyboard(district_val, lang, region_id=region_id, back_callback="back_to_district"),
        parse_mode="Markdown"
    )
    await callback.answer()

@search_router.callback_query(F.data == "back_to_district")
async def back_to_district(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    region_id = data.get("region_id", "tashkent_city")
    region_name = data.get("region_name", "")
    user_id = callback.from_user.id
    lang = await get_user_language(user_id)
    
    await state.set_state(SearchStates.waiting_for_district)
    text = get_text(lang, "step_district", region=region_name)
    await callback.message.edit_text(
        text,
        reply_markup=get_districts_keyboard(region_id, lang),
        parse_mode="Markdown"
    )
    await callback.answer()

# --- Step 3: Mahalla / Landmark ---
@search_router.message(SearchStates.waiting_for_mahalla)
async def process_mahalla_text(message: Message, state: FSMContext):
    mahalla = message.text.strip()
    await state.update_data(mahalla=mahalla)
    
    user_id = message.from_user.id
    lang = await get_user_language(user_id)
    
    await state.set_state(SearchStates.waiting_for_property_type)
    await message.answer(
        get_text(lang, "step_property_type"),
        reply_markup=get_property_type_keyboard(lang),
        parse_mode="Markdown"
    )

@search_router.callback_query(SearchStates.waiting_for_mahalla, F.data.startswith("mahalla:"))
async def process_mahalla_selection(callback: CallbackQuery, state: FSMContext):
    mahalla = callback.data.split(":", 1)[1]
    await state.update_data(mahalla=mahalla)
    
    user_id = callback.from_user.id
    lang = await get_user_language(user_id)
    
    await state.set_state(SearchStates.waiting_for_property_type)
    await callback.message.edit_text(
        get_text(lang, "step_property_type"),
        reply_markup=get_property_type_keyboard(lang),
        parse_mode="Markdown"
    )
    await callback.answer()

@search_router.callback_query(SearchStates.waiting_for_mahalla, F.data == "skip_step")
async def skip_mahalla_step(callback: CallbackQuery, state: FSMContext):
    await state.update_data(mahalla="")
    user_id = callback.from_user.id
    lang = await get_user_language(user_id)
    
    await state.set_state(SearchStates.waiting_for_property_type)
    await callback.message.edit_text(
        get_text(lang, "step_property_type"),
        reply_markup=get_property_type_keyboard(lang),
        parse_mode="Markdown"
    )
    await callback.answer()

@search_router.callback_query(F.data == "back_to_mahalla")
async def back_to_mahalla(callback: CallbackQuery, state: FSMContext):
    user_id = callback.from_user.id
    lang = await get_user_language(user_id)
    
    data = await state.get_data()
    district_id = data.get("district_id", "")
    region_id = data.get("region_id", "tashkent_city")
    await state.set_state(SearchStates.waiting_for_mahalla)
    await callback.message.edit_text(
        get_text(lang, "step_mahalla"),
        reply_markup=get_mahalla_keyboard(district_id, lang, region_id=region_id, back_callback="back_to_district"),
        parse_mode="Markdown"
    )
    await callback.answer()

# --- Step 4: Property Type ---
@search_router.callback_query(SearchStates.waiting_for_property_type, F.data.startswith("prop_type:"))
async def process_property_type(callback: CallbackQuery, state: FSMContext):
    prop_type = callback.data.split(":")[1]
    await state.update_data(property_type=prop_type)
    
    user_id = callback.from_user.id
    lang = await get_user_language(user_id)
    
    await state.set_state(SearchStates.waiting_for_area)
    await callback.message.edit_text(
        get_text(lang, "step_area"),
        reply_markup=get_area_keyboard(lang),
        parse_mode="Markdown"
    )
    await callback.answer()

@search_router.callback_query(F.data == "back_to_prop_type")
async def back_to_prop_type(callback: CallbackQuery, state: FSMContext):
    user_id = callback.from_user.id
    lang = await get_user_language(user_id)
    
    await state.set_state(SearchStates.waiting_for_property_type)
    await callback.message.edit_text(
        get_text(lang, "step_property_type"),
        reply_markup=get_property_type_keyboard(lang),
        parse_mode="Markdown"
    )
    await callback.answer()

# --- Step 5: Area (Kvadrat metr) ---
def parse_area_input(text: str):
    """
    Parses user input:
    - '120' -> min 102, max 138 (±15%)
    - '120-150' -> min 120, max 150
    """
    cleaned = re.sub(r"[^\d\-]", "", text)
    if "-" in cleaned:
        parts = cleaned.split("-")
        try:
            p1 = int(parts[0]) if parts[0] else 0
            p2 = int(parts[1]) if len(parts) > 1 and parts[1] else 0
            return min(p1, p2), max(p1, p2)
        except ValueError:
            return None, None
    elif cleaned.isdigit():
        val = int(cleaned)
        # Calculate +-15%
        min_v = int(val * 0.85)
        max_v = int(val * 1.15)
        return min_v, max_v
    return None, None

@search_router.callback_query(SearchStates.waiting_for_area, F.data.startswith("area:"))
async def process_area_preset(callback: CallbackQuery, state: FSMContext):
    val = callback.data.split(":")[1]
    if val == "any":
        area_min, area_max = None, None
    else:
        parts = val.split("-")
        area_min = int(parts[0]) if parts[0].isdigit() else None
        area_max = int(parts[1]) if len(parts) > 1 and parts[1].isdigit() else None
        
    await state.update_data(area_min=area_min, area_max=area_max)
    
    user_id = callback.from_user.id
    lang = await get_user_language(user_id)
    
    await state.set_state(SearchStates.waiting_for_repair)
    await callback.message.edit_text(
        get_text(lang, "step_repair"),
        reply_markup=get_repair_keyboard(lang),
        parse_mode="Markdown"
    )
    await callback.answer()

@search_router.message(SearchStates.waiting_for_area)
async def process_area_custom_text(message: Message, state: FSMContext):
    min_v, max_v = parse_area_input(message.text)
    if min_v is None and max_v is None:
        user_id = message.from_user.id
        lang = await get_user_language(user_id)
        await message.answer(
            "⚠️ Kvadrat metrni to'g'ri kiriting (masalan: `120` yoki `120-150`):",
            parse_mode="Markdown"
        )
        return
        
    await state.update_data(area_min=min_v, area_max=max_v)
    user_id = message.from_user.id
    lang = await get_user_language(user_id)
    
    await state.set_state(SearchStates.waiting_for_repair)
    await message.answer(
        get_text(lang, "step_repair"),
        reply_markup=get_repair_keyboard(lang),
        parse_mode="Markdown"
    )

@search_router.callback_query(F.data == "back_to_area")
async def back_to_area(callback: CallbackQuery, state: FSMContext):
    user_id = callback.from_user.id
    lang = await get_user_language(user_id)
    
    await state.set_state(SearchStates.waiting_for_area)
    await callback.message.edit_text(
        get_text(lang, "step_area"),
        reply_markup=get_area_keyboard(lang),
        parse_mode="Markdown"
    )
    await callback.answer()

# --- Step 6: Renovation (Ta'mir) ---
@search_router.callback_query(SearchStates.waiting_for_repair, F.data.startswith("repair:"))
async def process_repair_selection(callback: CallbackQuery, state: FSMContext):
    repair_val = callback.data.split(":")[1]
    await state.update_data(repair=repair_val)
    
    user_id = callback.from_user.id
    lang = await get_user_language(user_id)
    
    await state.set_state(SearchStates.waiting_for_price)
    await callback.message.edit_text(
        get_text(lang, "step_price"),
        reply_markup=get_price_keyboard(lang),
        parse_mode="Markdown"
    )
    await callback.answer()

@search_router.callback_query(F.data == "back_to_repair")
async def back_to_repair(callback: CallbackQuery, state: FSMContext):
    user_id = callback.from_user.id
    lang = await get_user_language(user_id)
    
    await state.set_state(SearchStates.waiting_for_repair)
    await callback.message.edit_text(
        get_text(lang, "step_repair"),
        reply_markup=get_repair_keyboard(lang),
        parse_mode="Markdown"
    )
    await callback.answer()

# --- Step 7: Price & Execute Search ---
@search_router.callback_query(SearchStates.waiting_for_price, F.data.startswith("price:"))
async def process_price_preset(callback: CallbackQuery, state: FSMContext):
    val = callback.data.split(":")[1]
    if val == "any":
        price_min, price_max = None, None
    else:
        parts = val.split("-")
        price_min = int(parts[0]) if parts[0].isdigit() and int(parts[0]) > 0 else None
        price_max = int(parts[1]) if len(parts) > 1 and parts[1].isdigit() and int(parts[1]) > 0 else None
        
    await state.update_data(price_min=price_min, price_max=price_max)
    await execute_search_and_show(callback.message, state, callback.from_user.id)
    await callback.answer()

@search_router.message(SearchStates.waiting_for_price)
async def process_price_custom_text(message: Message, state: FSMContext):
    cleaned = re.sub(r"[^\d\-]", "", message.text)
    price_min, price_max = None, None
    if "-" in cleaned:
        parts = cleaned.split("-")
        if parts[0].isdigit():
            price_min = int(parts[0])
        if len(parts) > 1 and parts[1].isdigit():
            price_max = int(parts[1])
    elif cleaned.isdigit():
        price_max = int(cleaned)
        
    await state.update_data(price_min=price_min, price_max=price_max)
    await execute_search_and_show(message, state, message.from_user.id)

async def execute_search_and_show(message: Message, state: FSMContext, user_id: int):
    """Fetch search criteria, trigger OLX query, and render first card."""
    lang = await get_user_language(user_id)
    search_data = await state.get_data()
    
    loader_msg = await message.answer(
        get_text(lang, "searching"),
        parse_mode="Markdown"
    )
    
    results = await search_all_properties(
        property_type=search_data.get("property_type", "any"),
        region_slug=search_data.get("region_slug", "tashkent"),
        district_query=search_data.get("district_query", ""),
        district_id=search_data.get("district_id", ""),
        mahalla=search_data.get("mahalla", ""),
        area_min=search_data.get("area_min"),
        area_max=search_data.get("area_max"),
        repair=search_data.get("repair", "any"),
        price_min=search_data.get("price_min"),
        price_max=search_data.get("price_max"),
        page=1
    )
    
    await loader_msg.delete()
    
    if not results:
        no_res_kb = get_price_keyboard(lang)
        await message.answer(
            get_text(lang, "no_results"),
            reply_markup=no_res_kb,
            parse_mode="Markdown"
        )
        return
        
    # Store results in state for pagination
    await state.update_data(search_results=results, current_index=0)
    await show_card_result(message, results, 0, lang, user_id)
