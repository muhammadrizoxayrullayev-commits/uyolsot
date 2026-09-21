from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButton
)
from locales import get_text
from data.regions import REGIONS

def get_language_keyboard() -> InlineKeyboardMarkup:
    """Keyboard for selecting bot language."""
    buttons = [
        [
            InlineKeyboardButton(text="🇺🇿 O'zbekcha", callback_data="set_lang:uz"),
            InlineKeyboardButton(text="🇷🇺 Русский", callback_data="set_lang:ru"),
            InlineKeyboardButton(text="🇬🇧 English", callback_data="set_lang:en")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def get_main_menu(lang: str) -> ReplyKeyboardMarkup:
    """Main menu reply keyboard."""
    btn_search = KeyboardButton(text=get_text(lang, "btn_search"))
    btn_fav = KeyboardButton(text=get_text(lang, "btn_favorites"))
    btn_lang = KeyboardButton(text=get_text(lang, "btn_settings_lang"))
    btn_help = KeyboardButton(text=get_text(lang, "btn_help"))
    
    keyboard = [
        [btn_search],
        [btn_fav, btn_lang],
        [btn_help]
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)

def get_regions_keyboard(lang: str) -> InlineKeyboardMarkup:
    """Grid of 13 regions/administrative divisions."""
    keyboard = []
    row = []
    
    for r in REGIONS:
        name_key = f"name_{lang}"
        label = r.get(name_key, r["name_uz"])
        # Keep short labels for 2 columns
        btn = InlineKeyboardButton(text=label, callback_data=f"reg:{r['id']}")
        row.append(btn)
        if len(row) == 2:
            keyboard.append(row)
            row = []
            
    if row:
        keyboard.append(row)
        
    # Cancel button
    keyboard.append([
        InlineKeyboardButton(text=get_text(lang, "btn_cancel"), callback_data="cancel_search")
    ])
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def get_districts_keyboard(region_id: str, lang: str) -> InlineKeyboardMarkup:
    """Districts keyboard for chosen region."""
    from data.regions import get_region_by_id
    region = get_region_by_id(region_id)
    keyboard = []
    
    if region and "districts" in region:
        row = []
        name_key = f"name_{lang}"
        for d in region["districts"]:
            label = d.get(name_key, d["name_uz"])
            btn = InlineKeyboardButton(text=label, callback_data=f"dist:{d['id']}")
            row.append(btn)
            if len(row) == 2:
                keyboard.append(row)
                row = []
        if row:
            keyboard.append(row)
            
    # Add option for all districts
    keyboard.append([
        InlineKeyboardButton(text=f"🌐 {get_text(lang, 'btn_all')}", callback_data="dist:all")
    ])
    
    # Back and Cancel buttons
    keyboard.append([
        InlineKeyboardButton(text=get_text(lang, "btn_back"), callback_data="back_to_regions"),
        InlineKeyboardButton(text=get_text(lang, "btn_cancel"), callback_data="cancel_search")
    ])
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def get_skip_keyboard(lang: str, back_callback: str = "back_to_district") -> InlineKeyboardMarkup:
    """Keyboard with Skip, Back and Cancel options."""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=get_text(lang, "btn_skip"), callback_data="skip_step")],
        [
            InlineKeyboardButton(text=get_text(lang, "btn_back"), callback_data=back_callback),
            InlineKeyboardButton(text=get_text(lang, "btn_cancel"), callback_data="cancel_search")
        ]
    ])

def get_property_type_keyboard(lang: str) -> InlineKeyboardMarkup:
    """Keyboard for selecting apartment, house or any."""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=get_text(lang, "type_apartment"), callback_data="prop_type:apartment")],
        [InlineKeyboardButton(text=get_text(lang, "type_house"), callback_data="prop_type:house")],
        [InlineKeyboardButton(text=get_text(lang, "type_any"), callback_data="prop_type:any")],
        [
            InlineKeyboardButton(text=get_text(lang, "btn_back"), callback_data="back_to_mahalla"),
            InlineKeyboardButton(text=get_text(lang, "btn_cancel"), callback_data="cancel_search")
        ]
    ])

def get_area_keyboard(lang: str) -> InlineKeyboardMarkup:
    """Area presets keyboard."""
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=get_text(lang, "area_preset_1"), callback_data="area:40-70"),
            InlineKeyboardButton(text=get_text(lang, "area_preset_2"), callback_data="area:70-100")
        ],
        [
            InlineKeyboardButton(text=get_text(lang, "area_preset_3"), callback_data="area:100-150"),
            InlineKeyboardButton(text=get_text(lang, "area_preset_4"), callback_data="area:150-500")
        ],
        [
            InlineKeyboardButton(text=f"🌐 {get_text(lang, 'btn_all')}", callback_data="area:any")
        ],
        [
            InlineKeyboardButton(text=get_text(lang, "btn_back"), callback_data="back_to_prop_type"),
            InlineKeyboardButton(text=get_text(lang, "btn_cancel"), callback_data="cancel_search")
        ]
    ])

def get_repair_keyboard(lang: str) -> InlineKeyboardMarkup:
    """Renovation status selection keyboard."""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=get_text(lang, "repair_euro"), callback_data="repair:euro")],
        [InlineKeyboardButton(text=get_text(lang, "repair_medium"), callback_data="repair:medium")],
        [InlineKeyboardButton(text=get_text(lang, "repair_none"), callback_data="repair:none")],
        [InlineKeyboardButton(text=get_text(lang, "repair_any"), callback_data="repair:any")],
        [
            InlineKeyboardButton(text=get_text(lang, "btn_back"), callback_data="back_to_area"),
            InlineKeyboardButton(text=get_text(lang, "btn_cancel"), callback_data="cancel_search")
        ]
    ])

def get_price_keyboard(lang: str) -> InlineKeyboardMarkup:
    """Price presets selection keyboard."""
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=get_text(lang, "price_preset_1"), callback_data="price:0-35000"),
            InlineKeyboardButton(text=get_text(lang, "price_preset_2"), callback_data="price:35000-65000")
        ],
        [
            InlineKeyboardButton(text=get_text(lang, "price_preset_3"), callback_data="price:65000-100000"),
            InlineKeyboardButton(text=get_text(lang, "price_preset_4"), callback_data="price:100000-160000")
        ],
        [
            InlineKeyboardButton(text=get_text(lang, "price_preset_5"), callback_data="price:160000-0"),
            InlineKeyboardButton(text=get_text(lang, "price_preset_any"), callback_data="price:any")
        ],
        [
            InlineKeyboardButton(text=get_text(lang, "btn_back"), callback_data="back_to_repair"),
            InlineKeyboardButton(text=get_text(lang, "btn_cancel"), callback_data="cancel_search")
        ]
    ])

def get_card_keyboard(
    lang: str,
    ad_id: str,
    url: str,
    current_idx: int,
    total_count: int,
    is_saved: bool = False
) -> InlineKeyboardMarkup:
    """Navigation and action keyboard for property cards."""
    nav_row = []
    if current_idx > 0:
        nav_row.append(InlineKeyboardButton(text=get_text(lang, "btn_prev"), callback_data=f"nav:{current_idx - 1}"))
    
    # Counter in middle
    nav_row.append(InlineKeyboardButton(text=f"📌 {current_idx + 1}/{total_count}", callback_data="noop"))
    
    if current_idx < total_count - 1:
        nav_row.append(InlineKeyboardButton(text=get_text(lang, "btn_next"), callback_data=f"nav:{current_idx + 1}"))
        
    fav_btn_text = get_text(lang, "btn_remove_fav") if is_saved else get_text(lang, "btn_save_fav")
    fav_callback = f"fav_del:{ad_id}:{current_idx}" if is_saved else f"fav_add:{ad_id}:{current_idx}"
    
    keyboard = [
        nav_row,
        [InlineKeyboardButton(text=get_text(lang, "btn_open_olx"), url=url)],
        [
            InlineKeyboardButton(text=fav_btn_text, callback_data=fav_callback),
            InlineKeyboardButton(text=get_text(lang, "btn_new_search"), callback_data="action_new_search")
        ],
        [InlineKeyboardButton(text=get_text(lang, "btn_main_menu"), callback_data="action_main_menu")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)
