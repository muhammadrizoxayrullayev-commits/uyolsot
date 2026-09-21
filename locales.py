"""
Multilingual strings for the Real Estate Bot (Uzbek, Russian, English).
"""

TEXTS = {
    "uz": {
        "welcome": (
            "👋 **Assalomu alaykum va xush kelibsiz!**\n\n"
            "🏡 **Uy Ol-Sot** boti orqali O'zbekiston bo'ylab (12 ta viloyat va Toshkent shahri) "
            "OLX.uz dagi eng so'nggi hovli va kvartiralarni qulay filtrlar asosida topishingiz mumkin!\n\n"
            "✨ *Tugmalardan birini tanlang:*"
        ),
        "choose_language": "🌐 **Iltimos, tilni tanlang / Пожалуйста, выберите язык / Please choose language:**",
        "language_saved": "✅ Til muvaffaqiyatli saqlandi: **O'zbekcha** 🇺🇿",
        
        # Menu buttons
        "btn_search": "🔍 Uy qidirish",
        "btn_favorites": "⭐ Sevimlilar",
        "btn_settings_lang": "🌐 Tilni almashtirish",
        "btn_help": "ℹ️ Yordam va OLX API",
        "btn_back": "⬅️ Ortga",
        "btn_cancel": "❌ Bekor qilish",
        "btn_skip": "⏭ O'tkazib yuborish",
        "btn_all": "🌐 Barchasi / Farqi yo'q",
        "btn_new_search": "🔄 Yangi qidiruv",
        "btn_main_menu": "🏠 Bosh menyu",
        
        # Search steps
        "step_region": "📍 **1-Qadam: Qaysi viloyat yoki shahardan uy qidiryapsiz?**\nQuyidagi ro'yxatdan tanlang:",
        "step_district": "🏘 **2-Qadam: Qaysi tumanni tanlaysiz?**\nTanlangan hudud: **{region}**",
        "step_mahalla": (
            "📍 **3-Qadam: Mahalla yoki ko'cha nomini kiriting:**\n\n"
            "Masalan: `Dombirobod`, `Novza`, `Qatortol`, `Buyuk Ipak Yo'li`\n\n"
            "💡 *Agar muayyan mahalla muhim bo'lmasa, **⏭ O'tkazib yuborish** tugmasini bosing.*"
        ),
        "step_property_type": "🏢 **4-Qadam: Uy turini tanlang:**",
        "type_apartment": "🏢 Kvartira (Dom)",
        "type_house": "🏡 Hovli (Uchastka / Kottej)",
        "type_any": "🌐 Ikkalasi ham (Farqi yo'q)",
        
        "step_area": (
            "📐 **5-Qadam: Uyning kvadrat metrini (maydonini) tanlang:**\n\n"
            "🔘 Pastdagi tayyor tugmalardan tanlashingiz yoki\n"
            "✍️ O'zingiz xohlagan raqamni kiritishingiz mumkin:\n"
            "• `120` deb yozsangiz: bot **100 dan 140 m²** gacha qidiradi (±15%)\n"
            "• `120-150` deb yozsangiz: aynan **120 dan 150 m²** gacha qidiradi"
        ),
        "area_preset_1": "40 - 70 m²",
        "area_preset_2": "70 - 100 m²",
        "area_preset_3": "100 - 150 m²",
        "area_preset_4": "150+ m²",
        
        "step_repair": "🛠 **6-Qadam: Ta'mir holatini (Remont) tanlang:**",
        "repair_euro": "💎 Yevroremont / Yangi",
        "repair_medium": "🛠 O'rtacha / Yaxshi",
        "repair_none": "🧱 Qora suvoq / Bez remont",
        "repair_any": "🌐 Farqi yo'q (Barchasi)",
        
        "step_price": (
            "💰 **7-Qadam: Byudjetingiz (Narx oralig'i):**\n\n"
            "🔘 Pastdagi tugmalardan tanlang yoki o'zingiz yozing (masalan: `40000-80000`):"
        ),
        "price_preset_1": "💵 $35,000 gacha",
        "price_preset_2": "💵 $35,000 - $65,000",
        "price_preset_3": "💵 $65,000 - $100,000",
        "price_preset_4": "💵 $100,000 - $160,000",
        "price_preset_5": "💵 $160,000+",
        "price_preset_any": "🌐 Farqi yo'q",

        # Search Progress & Results
        "searching": "🔍 **OLX.uz dan so'rovingizga mos eng sara uylar qidirilmoqda...**\nIltimos, bir necha soniya kuting...",
        "results_found": "🎉 **Topilgan e'lonlar:** {total} ta\nNatijalar ko'rsatilmoqda ({current}/{total}):",
        "no_results": (
            "😔 **Afsuski, kiritilgan parametrlar bo'yicha hech qanday e'lon topilmadi.**\n\n"
            "💡 *Maslahat: Mahalla nomini o'chiring yoki kvadrat metr / narx oralig'ini kengaytirib qayta urinib ko'ring.*"
        ),
        "btn_prev": "⬅️ Oldingi",
        "btn_next": "Keyingi ➡️",
        "btn_open_olx": "🔗 OLX da ko'rish",
        "btn_save_fav": "⭐ Saqlash",
        "btn_remove_fav": "🗑 O'chirish",
        "saved_to_fav": "⭐ E'lon sevimlilar ro'yxatiga saqlandi!",
        "removed_from_fav": "🗑 E'lon sevimlilar ro'yxatidan olib tashlandi!",
        "favorites_empty": "⭐ **Sizda hozircha saqlangan e'lonlar yo'q.**\n\nQidiruv natijalaridagi ⭐ Saqlash tugmasi orqali o'zingizga yoqqan uylarni shu yerga yig'ishingiz mumkin!",
        "favorites_title": "⭐ **Sizning sevimlilaringiz:** ({total} ta)",

        # Card template
        "card_title": "🏠 **{title}**",
        "card_price": "💰 **Narxi:** {price}",
        "card_area": "📐 **Maydoni:** {area} m²",
        "card_rooms": "🚪 **Xonalar:** {rooms}",
        "card_floor": "🏢 **Qavat:** {floor}",
        "card_repair": "🛠 **Ta'mir:** {repair}",
        "card_location": "📍 **Manzil:** {location}",
        "card_date": "📅 **Sana:** {date}",
        
        # Help & OLX API
        "help_title": "ℹ️ **Uy Ol-Sot boti va OLX integratsiyasi haqida**",
        "help_text": (
            "🤖 **Ushbu bot sizga OLX.uz dagi uylarni tez va oson topishga yordam beradi!**\n\n"
            "🔑 **OLX API haqida ma'lumot:**\n"
            "• Bot hozirda to'g'ridan-to'g'ri `curl_cffi` drayveri orqali OLX.uz dan barcha yangi e'lonlar, rasmlar va narxlarni real vaqt rejimida avtomatik oladi.\n"
            "• Agar sizda rasmiy OLX API kaliti (`client_id` va `client_secret`) bo'lsa, uni loyihaning `.env` fayliga kiritishingiz mumkin.\n"
            "• Rasmiy OLX API kalitini olish uchun [developer.olx.uz](https://developer.olx.uz) portalida ro'yxatdan o'tishingiz yoki OLX biznes akkaunt ochishingiz kerak bo'ladi.\n\n"
            "Savol va takliflar uchun administrator bilan bog'laning."
        )
    },
    
    "ru": {
        "welcome": (
            "👋 **Здравствуйте и добро пожаловать!**\n\n"
            "🏡 С помощью бота **Uy Ol-Sot** вы можете легко искать дома и квартиры на OLX.uz "
            "по всему Узбекистану (12 областей и город Ташкент) с удобными фильтрами!\n\n"
            "✨ *Выберите нужное действие:*"
        ),
        "choose_language": "🌐 **Пожалуйста, выберите язык / Iltimos, tilni tanlang / Please choose language:**",
        "language_saved": "✅ Язык успешно сохранен: **Русский** 🇷🇺",
        
        # Menu buttons
        "btn_search": "🔍 Поиск недвижимости",
        "btn_favorites": "⭐ Избранное",
        "btn_settings_lang": "🌐 Сменить язык",
        "btn_help": "ℹ️ Помощь и OLX API",
        "btn_back": "⬅️ Назад",
        "btn_cancel": "❌ Отмена",
        "btn_skip": "⏭ Пропустить",
        "btn_all": "🌐 Все / Не важно",
        "btn_new_search": "🔄 Новый поиск",
        "btn_main_menu": "🏠 Главное меню",
        
        # Search steps
        "step_region": "📍 **Шаг 1: В каком регионе или городе вы ищете жилье?**\nВыберите из списка:",
        "step_district": "🏘 **Шаг 2: Выберите район:**\nВыбранный регион: **{region}**",
        "step_mahalla": (
            "📍 **Шаг 3: Введите махаллю, улицу или ориентир:**\n\n"
            "Например: `Домбрабад`, `Чиланзар 9`, `Новза`, `Катартал`\n\n"
            "💡 *Если конкретная махалля не важна, нажмите кнопку **⏭ Пропустить**.*"
        ),
        "step_property_type": "🏢 **Шаг 4: Выберите тип недвижимости:**",
        "type_apartment": "🏢 Квартира",
        "type_house": "🏡 Дом / Участок / Коттедж",
        "type_any": "🌐 Любой тип (Все)",
        
        "step_area": (
            "📐 **Шаг 5: Выберите площадь (кв. метры):**\n\n"
            "🔘 Выберите готовую кнопку внизу или\n"
            "✍️ Введите желаемую площадь вручную:\n"
            "• Напишите `120`: бот найдет от **100 до 140 м²** (±15%)\n"
            "• Напишите `120-150`: бот найдет точно от **120 до 150 м²**"
        ),
        "area_preset_1": "40 - 70 м²",
        "area_preset_2": "70 - 100 м²",
        "area_preset_3": "100 - 150 м²",
        "area_preset_4": "150+ м²",
        
        "step_repair": "🛠 **Шаг 6: Состояние ремонта:**",
        "repair_euro": "💎 Евроремонт / Новый",
        "repair_medium": "🛠 Средний / Хороший",
        "repair_none": "🧱 Черновая отделка / Без ремонта",
        "repair_any": "🌐 Не важно (Любой)",
        
        "step_price": (
            "💰 **Шаг 7: Ваш бюджет (Диапазон цен):**\n\n"
            "🔘 Выберите кнопку или введите сумму (например: `40000-80000`):"
        ),
        "price_preset_1": "💵 До $35,000",
        "price_preset_2": "💵 $35,000 - $65,000",
        "price_preset_3": "💵 $65,000 - $100,000",
        "price_preset_4": "💵 $100,000 - $160,000",
        "price_preset_5": "💵 $160,000+",
        "price_preset_any": "🌐 Любая цена",

        # Search Progress & Results
        "searching": "🔍 **Идет поиск подходящих объявлений на OLX.uz...**\nПожалуйста, подождите пару секунд...",
        "results_found": "🎉 **Найдено объявлений:** {total}\nПоказ ({current}/{total}):",
        "no_results": (
            "😔 **К сожалению, по данным параметрам ничего не найдено.**\n\n"
            "💡 *Совет: Попробуйте убрать название махалли или расширить диапазон цен/площади.*"
        ),
        "btn_prev": "⬅️ Назад",
        "btn_next": "Вперед ➡️",
        "btn_open_olx": "🔗 Открыть на OLX",
        "btn_save_fav": "⭐ В избранное",
        "btn_remove_fav": "🗑 Удалить из избранного",
        "saved_to_fav": "⭐ Объявление добавлено в избранное!",
        "removed_from_fav": "🗑 Объявление удалено из избранного!",
        "favorites_empty": "⭐ **У вас пока нет сохраненных объявлений.**\n\nСохраняйте понравившиеся варианты кнопкой ⭐ В избранное!",
        "favorites_title": "⭐ **Ваше избранное:** ({total})",

        # Card template
        "card_title": "🏠 **{title}**",
        "card_price": "💰 **Цена:** {price}",
        "card_area": "📐 **Площадь:** {area} м²",
        "card_rooms": "🚪 **Комнат:** {rooms}",
        "card_floor": "🏢 **Этаж:** {floor}",
        "card_repair": "🛠 **Ремонт:** {repair}",
        "card_location": "📍 **Адрес:** {location}",
        "card_date": "📅 **Дата:** {date}",
        
        # Help & OLX API
        "help_title": "ℹ️ **О боте Uy Ol-Sot и интеграции с OLX**",
        "help_text": (
            "🤖 **Этот бот помогает находить недвижимость на OLX.uz быстро и точно!**\n\n"
            "🔑 **Информация по API OLX:**\n"
            "• Бот использует встроенный современный движок `curl_cffi`, который позволяет получать свежие объявления, фотографии и параметры с OLX.uz в реальном времени без ключа API.\n"
            "• Если у вас есть официальный ключ OLX API (`client_id` и `client_secret`), укажите его в файле `.env`.\n"
            "• Официальный ключ API можно запросить на портале [developer.olx.uz](https://developer.olx.uz) для бизнес-партнеров OLX."
        )
    },

    "en": {
        "welcome": (
            "👋 **Hello and Welcome!**\n\n"
            "🏡 Welcome to **Uy Ol-Sot** bot — your smart real estate search assistant for OLX.uz "
            "across Uzbekistan (all 12 regions and Tashkent City)!\n\n"
            "✨ *Please choose an option below:*"
        ),
        "choose_language": "🌐 **Please choose your language / Iltimos, tilni tanlang / Пожалуйста, выберите язык:**",
        "language_saved": "✅ Language successfully saved: **English** 🇬🇧",
        
        # Menu buttons
        "btn_search": "🔍 Search Property",
        "btn_favorites": "⭐ Favorites",
        "btn_settings_lang": "🌐 Change Language",
        "btn_help": "ℹ️ Help & OLX API",
        "btn_back": "⬅️ Back",
        "btn_cancel": "❌ Cancel",
        "btn_skip": "⏭ Skip",
        "btn_all": "🌐 Any / All",
        "btn_new_search": "🔄 New Search",
        "btn_main_menu": "🏠 Main Menu",
        
        # Search steps
        "step_region": "📍 **Step 1: In which region or city are you looking for property?**\nSelect from the list below:",
        "step_district": "🏘 **Step 2: Choose a district:**\nSelected region: **{region}**",
        "step_mahalla": (
            "📍 **Step 3: Enter neighborhood / street / landmark:**\n\n"
            "Example: `Dombirobod`, `Novza`, `Chilanzar 9`\n\n"
            "💡 *If you don't have a specific neighborhood in mind, tap **⏭ Skip**.*"
        ),
        "step_property_type": "🏢 **Step 4: Select property type:**",
        "type_apartment": "🏢 Apartment (Flat)",
        "type_house": "🏡 House (Yard / Villa)",
        "type_any": "🌐 Any type",
        
        "step_area": (
            "📐 **Step 5: Select area (square meters):**\n\n"
            "🔘 Tap one of the presets below or\n"
            "✍️ Type your preferred size manually:\n"
            "• Type `120`: bot will search between **100 and 140 m²** (±15%)\n"
            "• Type `120-150`: bot will search exactly between **120 and 150 m²**"
        ),
        "area_preset_1": "40 - 70 m²",
        "area_preset_2": "70 - 100 m²",
        "area_preset_3": "100 - 150 m²",
        "area_preset_4": "150+ m²",
        
        "step_repair": "🛠 **Step 6: Renovation status:**",
        "repair_euro": "💎 Euro / Modern Renovation",
        "repair_medium": "🛠 Good / Medium Condition",
        "repair_none": "🧱 Shell & Core / No Renovation",
        "repair_any": "🌐 Any (Doesn't matter)",
        
        "step_price": (
            "💰 **Step 7: Your budget (Price range):**\n\n"
            "🔘 Choose a preset or type your custom range (e.g., `40000-80000`):"
        ),
        "price_preset_1": "💵 Under $35,000",
        "price_preset_2": "💵 $35,000 - $65,000",
        "price_preset_3": "💵 $65,000 - $100,000",
        "price_preset_4": "💵 $100,000 - $160,000",
        "price_preset_5": "💵 $160,000+",
        "price_preset_any": "🌐 Any price",

        # Search Progress & Results
        "searching": "🔍 **Searching best matching properties on OLX.uz...**\nPlease wait a few seconds...",
        "results_found": "🎉 **Properties found:** {total}\nShowing ({current}/{total}):",
        "no_results": (
            "😔 **Sorry, no listings found matching your criteria.**\n\n"
            "💡 *Tip: Try omitting the neighborhood name or expanding the area/budget range.*"
        ),
        "btn_prev": "⬅️ Previous",
        "btn_next": "Next ➡️",
        "btn_open_olx": "🔗 View on OLX",
        "btn_save_fav": "⭐ Save",
        "btn_remove_fav": "🗑 Remove",
        "saved_to_fav": "⭐ Saved to your favorites!",
        "removed_from_fav": "🗑 Removed from favorites!",
        "favorites_empty": "⭐ **You don't have any saved listings yet.**\n\nTap ⭐ Save on any search result to keep it here!",
        "favorites_title": "⭐ **Your Favorites:** ({total})",

        # Card template
        "card_title": "🏠 **{title}**",
        "card_price": "💰 **Price:** {price}",
        "card_area": "📐 **Area:** {area} m²",
        "card_rooms": "🚪 **Rooms:** {rooms}",
        "card_floor": "🏢 **Floor:** {floor}",
        "card_repair": "🛠 **Renovation:** {repair}",
        "card_location": "📍 **Location:** {location}",
        "card_date": "📅 **Date:** {date}",
        
        # Help & OLX API
        "help_title": "ℹ️ **About Uy Ol-Sot & OLX Integration**",
        "help_text": (
            "🤖 **This bot helps you quickly search and filter real estate on OLX.uz!**\n\n"
            "🔑 **OLX API Information:**\n"
            "• The bot includes a built-in high-performance `curl_cffi` engine that retrieves live OLX.uz offers, photos, and specs in real time without needing an API key.\n"
            "• If you have official OLX Partner API credentials (`client_id` and `client_secret`), configure them in `.env`.\n"
            "• Official API access can be obtained via [developer.olx.uz](https://developer.olx.uz) for business partners."
        )
    }
}

def get_text(lang: str, key: str, **kwargs) -> str:
    lang_dict = TEXTS.get(lang, TEXTS["uz"])
    template = lang_dict.get(key, TEXTS["uz"].get(key, key))
    if kwargs:
        return template.format(**kwargs)
    return template
