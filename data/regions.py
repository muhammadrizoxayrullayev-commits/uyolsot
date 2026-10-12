"""
Regions and districts data for Uzbekistan, mapped to OLX search locations.
"""

REGIONS = [
    {
        "id": "tashkent_city",
        "name_uz": "🏛 Toshkent shahri",
        "name_ru": "🏛 г. Ташкент",
        "name_en": "🏛 Tashkent City",
        "olx_slug": "tashkent",
        "districts": [
            {"id": "chilonzor", "name_uz": "Chilonzor tumani", "name_ru": "Чиланзарский район", "name_en": "Chilanzar district", "query": "чиланзар"},
            {"id": "yunusobod", "name_uz": "Yunusobod tumani", "name_ru": "Юнусабадский район", "name_en": "Yunusabad district", "query": "юнусабад"},
            {"id": "mirzo_ulugbek", "name_uz": "Mirzo Ulug'bek tumani", "name_ru": "Мирзо-Улугбекский район", "name_en": "Mirzo Ulugbek district", "query": "мирзо-улугбек"},
            {"id": "yakkasaroy", "name_uz": "Yakkasaroy tumani", "name_ru": "Яккасарайский район", "name_en": "Yakkasaray district", "query": "яккасарай"},
            {"id": "mirobod", "name_uz": "Mirobod tumani", "name_ru": "Мирабадский район", "name_en": "Mirabad district", "query": "мирабад"},
            {"id": "yashnobod", "name_uz": "Yashnobod tumani", "name_ru": "Яшнабадский район", "name_en": "Yashnabad district", "query": "яшнабад"},
            {"id": "olmazor", "name_uz": "Olmazor tumani", "name_ru": "Алмазарский район", "name_en": "Almazar district", "query": "алмазар"},
            {"id": "shayxontohur", "name_uz": "Shayxontohur tumani", "name_ru": "Шайхантахурский район", "name_en": "Shaykhantakhur district", "query": "шайхантахур"},
            {"id": "uchtepa", "name_uz": "Uchtepa tumani", "name_ru": "Учтепинский район", "name_en": "Uchtepa district", "query": "учтепа"},
            {"id": "sergeli", "name_uz": "Sergeli tumani", "name_ru": "Сергелийский район", "name_en": "Sergeli district", "query": "сергели"},
            {"id": "yangihayot", "name_uz": "Yangihayot tumani", "name_ru": "Янгихаётский район", "name_en": "Yangihayot district", "query": "янгихаёт"},
            {"id": "bektemir", "name_uz": "Bektemir tumani", "name_ru": "Бектемирский район", "name_en": "Bektemir district", "query": "бектемир"},
        ]
    },
    {
        "id": "tashkent_obl",
        "name_uz": "🌲 Toshkent viloyati",
        "name_ru": "🌲 Ташкентская область",
        "name_en": "🌲 Tashkent Region",
        "olx_slug": "toshkent-oblast",
        "districts": [
            {"id": "chirchiq", "name_uz": "Chirchiq shahar", "name_ru": "г. Чирчик", "name_en": "Chirchik city", "query": "чирчик"},
            {"id": "olmaliq", "name_uz": "Olmaliq shahar", "name_ru": "г. Алмалык", "name_en": "Almalyk city", "query": "алмалык"},
            {"id": "angren", "name_uz": "Angren shahar", "name_ru": "г. Ангрен", "name_en": "Angren city", "query": "ангрен"},
            {"id": "bekobod", "name_uz": "Bekobod shahar", "name_ru": "г. Бекабад", "name_en": "Bekabad city", "query": "бекабад"},
            {"id": "zangiota", "name_uz": "Zangiota tumani", "name_ru": "Зангиатинский р-н", "name_en": "Zangiata district", "query": "зангиота"},
            {"id": "qibray", "name_uz": "Qibray tumani", "name_ru": "Кибрайский р-н", "name_en": "Kibray district", "query": "кибрай"},
            {"id": "toshkent_t", "name_uz": "Toshkent tumani", "name_ru": "Ташкентский р-н", "name_en": "Tashkent district", "query": "ташкентский район"},
            {"id": "yangiyol", "name_uz": "Yangiyo'l shahar/tumani", "name_ru": "г. Янгиюль / р-н", "name_en": "Yangiyul city/dist", "query": "янгиюль"},
            {"id": "bostoliq", "name_uz": "Bo'stonliq tumani (Gazalkent)", "name_ru": "Бостанлыкский р-н", "name_en": "Bostanlyk district", "query": "бостанлык"},
            {"id": "yuqorichirchiq", "name_uz": "Yuqori Chirchiq tumani", "name_ru": "Верхнечирчикский р-н", "name_en": "Upper Chirchik district", "query": "юкоричирчик"},
        ]
    },
    {
        "id": "samarkand",
        "name_uz": "🕌 Samarqand viloyati",
        "name_ru": "🕌 Самаркандская область",
        "name_en": "🕌 Samarkand Region",
        "olx_slug": "samarkand",
        "districts": [
            {"id": "samarkand_sh", "name_uz": "Samarqand shahar", "name_ru": "г. Самарканд", "name_en": "Samarkand city", "query": "самарканд"},
            {"id": "kattaqorgon", "name_uz": "Kattaqo'rg'on shahar", "name_ru": "г. Каттакурган", "name_en": "Kattakurgan city", "query": "каттакурган"},
            {"id": "urgut", "name_uz": "Urgut tumani", "name_ru": "Ургутский р-н", "name_en": "Urgut district", "query": "ургут"},
            {"id": "pastdargom", "name_uz": "Pastdarg'om tumani", "name_ru": "Пастдаргомский р-н", "name_en": "Pastdargom district", "query": "пастдаргом"},
            {"id": "samarkand_t", "name_uz": "Samarqand tumani", "name_ru": "Самаркандский р-н", "name_en": "Samarkand district", "query": "самаркандский район"},
        ]
    },
    {
        "id": "fergana",
        "name_uz": "🍇 Fargʻona viloyati",
        "name_ru": "🍇 Ферганская область",
        "name_en": "🍇 Fergana Region",
        "olx_slug": "fergana",
        "districts": [
            {"id": "fergana_sh", "name_uz": "Farg'ona shahar", "name_ru": "г. Фергана", "name_en": "Fergana city", "query": "фергана"},
            {"id": "qoqon", "name_uz": "Qo'qon shahar", "name_ru": "г. Коканд", "name_en": "Kokand city", "query": "коканд"},
            {"id": "margilon", "name_uz": "Marg'ilon shahar", "name_ru": "г. Маргилан", "name_en": "Margilan city", "query": "маргилан"},
            {"id": "quvasoy", "name_uz": "Quvasoy shahar", "name_ru": "г. Кувасай", "name_en": "Kuvasay city", "query": "кувасай"},
            {"id": "rishton", "name_uz": "Rishton tumani", "name_ru": "Риштанский р-н", "name_en": "Rishtan district", "query": "риштан"},
        ]
    },
    {
        "id": "andijan",
        "name_uz": "🍎 Andijon viloyati",
        "name_ru": "🍎 Андижанская область",
        "name_en": "🍎 Andijan Region",
        "olx_slug": "andijan",
        "districts": [
            {"id": "andijan_sh", "name_uz": "Andijon shahar", "name_ru": "г. Андижан", "name_en": "Andijan city", "query": "андижан"},
            {"id": "asaka", "name_uz": "Asaka shahar", "name_ru": "г. Асака", "name_en": "Asaka city", "query": "асака"},
            {"id": "shaxrixon", "name_uz": "Shahrixon tumani", "name_ru": "Шахриханский р-н", "name_en": "Shahrikhan district", "query": "шахрихан"},
            {"id": "xonobod", "name_uz": "Xonobod shahar", "name_ru": "г. Ханабад", "name_en": "Khanabad city", "query": "ханабад"},
        ]
    },
    {
        "id": "namangan",
        "name_uz": "🌸 Namangan viloyati",
        "name_ru": "🌸 Наманганская область",
        "name_en": "🌸 Namangan Region",
        "olx_slug": "namangan",
        "districts": [
            {"id": "namangan_sh", "name_uz": "Namangan shahar", "name_ru": "г. Наманган", "name_en": "Namangan city", "query": "наманган"},
            {"id": "chust", "name_uz": "Chust tumani", "name_ru": "Чустский р-н", "name_en": "Chust district", "query": "чуст"},
            {"id": "kosonsoy", "name_uz": "Kosonsoy tumani", "name_ru": "Касансайский р-н", "name_en": "Kasansay district", "query": "касансай"},
        ]
    },
    {
        "id": "bukhara",
        "name_uz": "🏺 Buxoro viloyati",
        "name_ru": "🏺 Бухарская область",
        "name_en": "🏺 Bukhara Region",
        "olx_slug": "bukhara",
        "districts": [
            {"id": "bukhara_sh", "name_uz": "Buxoro shahar", "name_ru": "г. Бухара", "name_en": "Bukhara city", "query": "бухара"},
            {"id": "kogon", "name_uz": "Kogon shahar", "name_ru": "г. Каган", "name_en": "Kagan city", "query": "каган"},
            {"id": "gijduvon", "name_uz": "G'ijduvon tumani", "name_ru": "Гиждуванский р-н", "name_en": "Gijduvan district", "query": "гиждуван"},
        ]
    },
    {
        "id": "qashqadaryo",
        "name_uz": "🏔 Qashqadaryo viloyati",
        "name_ru": "🏔 Кашкадарьинская область",
        "name_en": "🏔 Kashkadarya Region",
        "olx_slug": "kashkadarya",
        "districts": [
            {"id": "qarshi_sh", "name_uz": "Qarshi shahar", "name_ru": "г. Карши", "name_en": "Karshi city", "query": "карши"},
            {"id": "shahrisabz", "name_uz": "Shahrisabz shahar", "name_ru": "г. Шахрисабз", "name_en": "Shahrisabz city", "query": "шахрисабз"},
            {"id": "koson", "name_uz": "Koson tumani", "name_ru": "Касанский р-н", "name_en": "Kasan district", "query": "касан"},
        ]
    },
    {
        "id": "surxondaryo",
        "name_uz": "☀️ Surxondaryo viloyati",
        "name_ru": "☀️ Сурхандарьинская область",
        "name_en": "☀️ Surkhandarya Region",
        "olx_slug": "surkhandarya",
        "districts": [
            {"id": "termiz_sh", "name_uz": "Termiz shahar", "name_ru": "г. Термез", "name_en": "Termez city", "query": "термез"},
            {"id": "denov", "name_uz": "Denov tumani", "name_ru": "Денауский р-н", "name_en": "Denau district", "query": "денау"},
            {"id": "sherobod", "name_uz": "Sherobod tumani", "name_ru": "Шерабадский р-н", "name_en": "Sherabad district", "query": "шерабад"},
        ]
    },
    {
        "id": "xorazm",
        "name_uz": "🏰 Xorazm viloyati",
        "name_ru": "🏰 Хорезмская область",
        "name_en": "🏰 Khorezm Region",
        "olx_slug": "khorezm",
        "districts": [
            {"id": "urganch_sh", "name_uz": "Urganch shahar", "name_ru": "г. Ургенч", "name_en": "Urgench city", "query": "ургенч"},
            {"id": "xiva", "name_uz": "Xiva shahar", "name_ru": "г. Хива", "name_en": "Khiva city", "query": "хива"},
            {"id": "hazarasp", "name_uz": "Hazorasp tumani", "name_ru": "Хазараспский р-н", "name_en": "Khazarasp district", "query": "хазарасп"},
        ]
    },
    {
        "id": "navoiy",
        "name_uz": "🏭 Navoiy viloyati",
        "name_ru": "🏭 Навоийская область",
        "name_en": "🏭 Navoiy Region",
        "olx_slug": "navoiy",
        "districts": [
            {"id": "navoiy_sh", "name_uz": "Navoiy shahar", "name_ru": "г. Навои", "name_en": "Navoiy city", "query": "навои"},
            {"id": "zarafshon", "name_uz": "Zarafshon shahar", "name_ru": "г. Зарафшан", "name_en": "Zarafshan city", "query": "зарафшан"},
            {"id": "karmana", "name_uz": "Karmana tumani", "name_ru": "Карманинский р-н", "name_en": "Karmana district", "query": "кармана"},
        ]
    },
    {
        "id": "jizzax",
        "name_uz": "🌾 Jizzax viloyati",
        "name_ru": "🌾 Джизакская область",
        "name_en": "🌾 Jizzakh Region",
        "olx_slug": "jizzax",
        "districts": [
            {"id": "jizzax_sh", "name_uz": "Jizzax shahar", "name_ru": "г. Джизак", "name_en": "Jizzakh city", "query": "джизак"},
            {"id": "zomin", "name_uz": "Zomin tumani", "name_ru": "Зааминский р-н", "name_en": "Zaamin district", "query": "заамин"},
            {"id": "gallaorol", "name_uz": "G'allaorol tumani", "name_ru": "Галляаральский р-н", "name_en": "Gallaorol district", "query": "галляарал"},
        ]
    },
    {
        "id": "sirdaryo",
        "name_uz": "🌊 Sirdaryo viloyati",
        "name_ru": "🌊 Сырдарьинская область",
        "name_en": "🌊 Syrdarya Region",
        "olx_slug": "sirdaryo",
        "districts": [
            {"id": "guliston_sh", "name_uz": "Guliston shahar", "name_ru": "г. Гулистан", "name_en": "Gulistan city", "query": "гулистан"},
            {"id": "shirin", "name_uz": "Shirin shahar", "name_ru": "г. Ширин", "name_en": "Shirin city", "query": "ширин"},
            {"id": "yangiyer", "name_uz": "Yangiyer shahar", "name_ru": "г. Янгиер", "name_en": "Yangiyer city", "query": "янгиер"},
        ]
    },
    {
        "id": "karakalpakstan",
        "name_uz": "🦅 Qoraqalpogʻiston Res.",
        "name_ru": "🦅 Респ. Каракалпакстан",
        "name_en": "🦅 Rep. of Karakalpakstan",
        "olx_slug": "karakalpakstan",
        "districts": [
            {"id": "nukus_sh", "name_uz": "Nukus shahar", "name_ru": "г. Нукус", "name_en": "Nukus city", "query": "нукус"},
            {"id": "beruniy", "name_uz": "Beruniy tumani", "name_ru": "Берунийский р-н", "name_en": "Beruniy district", "query": "беруний"},
            {"id": "xojayli", "name_uz": "Xo'jayli tumani", "name_ru": "Ходжейлийский р-н", "name_en": "Khojayli district", "query": "ходжейли"},
            {"id": "qongirot", "name_uz": "Qo'ng'irot tumani", "name_ru": "Кунградский р-н", "name_en": "Kungrad district", "query": "кунград"},
        ]
    }
]

def get_region_by_id(region_id: str):
    for r in REGIONS:
        if r["id"] == region_id:
            return r
    return None

def get_district_by_id(region_id: str, district_id: str):
    region = get_region_by_id(region_id)
    if not region:
        return None
    for d in region["districts"]:
        if d["id"] == district_id:
            return d
    return None

# Popular mahallas/areas for main districts to show as buttons
DISTRICT_MAHALLAS = {
    # Toshkent shahri (12 ta tuman)
    "chilonzor": [
        {"name": "Dombirobod", "icon": "🏡"},
        {"name": "Qatortol", "icon": "🏙"},
        {"name": "Novza", "icon": "🌳"},
        {"name": "Oqtepa", "icon": "⛲️"},
        {"name": "Chilonzor 1-9", "icon": "🏢"},
        {"name": "Chilonzor 16-20", "icon": "🏢"},
        {"name": "Muqimiy", "icon": "🛣"},
        {"name": "Chilonzor metro", "icon": "🚇"},
        {"name": "Algoritm", "icon": "🏬"},
        {"name": "Gavhar", "icon": "🏡"},
    ],
    "yunusobod": [
        {"name": "Bodomzor", "icon": "🌳"},
        {"name": "Shahriston", "icon": "🚉"},
        {"name": "Minor", "icon": "🕌"},
        {"name": "Oloy bozori", "icon": "🏪"},
        {"name": "Yunusobod 1-6", "icon": "🏢"},
        {"name": "Yunusobod 7-12", "icon": "🏢"},
        {"name": "Yunusobod 13-19", "icon": "🏢"},
        {"name": "Teleminora", "icon": "🗼"},
        {"name": "Hasanboy", "icon": "🏞"},
        {"name": "Ahmad Donish", "icon": "🏬"},
    ],
    "mirzo_ulugbek": [
        {"name": "Buyuk Ipak Yo'li", "icon": "🚇"},
        {"name": "Qorasuv 1-6", "icon": "🌊"},
        {"name": "TTZ", "icon": "🏭"},
        {"name": "Darxon", "icon": "🏛"},
        {"name": "Oqqo'rg'on", "icon": "🌳"},
        {"name": "Feruza", "icon": "🏙"},
        {"name": "Hamid Olimjon", "icon": "🏡"},
        {"name": "Parkent bozori", "icon": "🏘"},
        {"name": "Bo'zbozor", "icon": "🌲"},
        {"name": "C-1 / C-2", "icon": "🏢"},
    ],
    "yakkasaroy": [
        {"name": "Rakat", "icon": "🌳"},
        {"name": "Boshliq", "icon": "🏢"},
        {"name": "Qushbegi", "icon": "✈️"},
        {"name": "Bobur bog'i", "icon": "🌺"},
        {"name": "Shota Rustaveli", "icon": "🛣"},
        {"name": "Grand Mir", "icon": "🏢"},
        {"name": "Bo'rijar", "icon": "🌊"},
        {"name": "Teatralniy", "icon": "🏡"},
        {"name": "Kosmonavtlar", "icon": "🚀"},
        {"name": "O'qchi", "icon": "🏛"},
    ],
    "mirobod": [
        {"name": "Oybek", "icon": "🚇"},
        {"name": "Gospitalniy", "icon": "🏥"},
        {"name": "Shevchenko", "icon": "🏢"},
        {"name": "Chexov", "icon": "🏬"},
        {"name": "Shimoliy vokzal", "icon": "🚉"},
        {"name": "Qo'yliq", "icon": "🌊"},
        {"name": "Sariko'l", "icon": "🌳"},
        {"name": "Tong yulduzi", "icon": "🏡"},
        {"name": "Mirobod bozori", "icon": "🏢"},
        {"name": "Nukus ko'chasi", "icon": "🛣"},
    ],
    "yashnobod": [
        {"name": "Kadisheva", "icon": "🏪"},
        {"name": "Aviasozlar 1-4", "icon": "✈️"},
        {"name": "Tuzel 1-4", "icon": "🏢"},
        {"name": "Do'stlik", "icon": "🚇"},
        {"name": "Go'zal", "icon": "🌳"},
        {"name": "Panjshanba", "icon": "🏘"},
        {"name": "Farg'ona yo'li", "icon": "🛣"},
        {"name": "Ashxobod bog'i", "icon": "🏢"},
        {"name": "Olmos", "icon": "🏡"},
        {"name": "Lisunova", "icon": "🏬"},
    ],
    "olmazor": [
        {"name": "Qoraqamish 1/1-2/5", "icon": "🏢"},
        {"name": "Sebzor", "icon": "🌳"},
        {"name": "Beruniy metro", "icon": "🚇"},
        {"name": "Talabalar shaharchasi", "icon": "🎓"},
        {"name": "Chig'atoy", "icon": "🏙"},
        {"name": "Hazrati Imom", "icon": "🕌"},
        {"name": "Qorasaroy", "icon": "🏬"},
        {"name": "Chuqursoy", "icon": "🏞"},
        {"name": "G'alaba bog'i", "icon": "🏡"},
        {"name": "Forobiy", "icon": "🛣"},
    ],
    "shayxontohur": [
        {"name": "Chorsu", "icon": "🕌"},
        {"name": "Qoratosh", "icon": "🏢"},
        {"name": "Labzak", "icon": "🏬"},
        {"name": "Ibn Sino 1-2", "icon": "🏥"},
        {"name": "Sirk / Xadra", "icon": "🎪"},
        {"name": "Samarqand darvoza", "icon": "🌳"},
        {"name": "Taxtapul", "icon": "🏙"},
        {"name": "Jangoh", "icon": "🏛"},
        {"name": "Markaz-14/15", "icon": "🏢"},
        {"name": "Oqlon", "icon": "🏡"},
    ],
    "uchtepa": [
        {"name": "O'rikzor bozori", "icon": "🏪"},
        {"name": "Farhod bozori", "icon": "🏬"},
        {"name": "Algoritm", "icon": "🏢"},
        {"name": "Chilonzor 21-26", "icon": "🏢"},
        {"name": "Vatan k/t", "icon": "🌳"},
        {"name": "Katta Qani", "icon": "🛣"},
        {"name": "Cho'ponota", "icon": "🏡"},
        {"name": "Taqachi", "icon": "🏙"},
        {"name": "Shirin", "icon": "🏢"},
        {"name": "Zargarlik", "icon": "🏬"},
    ],
    "sergeli": [
        {"name": "Sputnik 1-16", "icon": "🏢"},
        {"name": "Sergeli yarmarkasi", "icon": "🏬"},
        {"name": "Yangi Sergeli", "icon": "🏗"},
        {"name": "Choshtepa", "icon": "🚇"},
        {"name": "Qo'shqo'rg'on", "icon": "🌳"},
        {"name": "Do'stlik 1-2", "icon": "🏢"},
        {"name": "Qipchoq", "icon": "🏡"},
        {"name": "Quruvchilar", "icon": "🏗"},
        {"name": "Yangi Sergeli yo'li", "icon": "🛣"},
        {"name": "Sug'diyona", "icon": "🏢"},
    ],
    "yangihayot": [
        {"name": "Yo'ldosh", "icon": "🏢"},
        {"name": "Choshtepa metro", "icon": "🌳"},
        {"name": "Yangi Darxon", "icon": "🏙"},
        {"name": "Binokor", "icon": "🏘"},
        {"name": "THAY halqa yo'li", "icon": "🛣"},
        {"name": "Yangihayot 1-5", "icon": "🏢"},
        {"name": "Oriat", "icon": "🏡"},
        {"name": "Yangi Choshtepa", "icon": "🏢"},
    ],
    "bektemir": [
        {"name": "Qo'yliq bozori", "icon": "🏪"},
        {"name": "Suvsoz 1-2", "icon": "🏢"},
        {"name": "Majnuntol", "icon": "🌳"},
        {"name": "Bektemir markaz", "icon": "🏭"},
        {"name": "Husayn Boyqaro", "icon": "🏞"},
        {"name": "Ohangaron shossesi", "icon": "🛣"},
        {"name": "Rohat ko'li", "icon": "🏡"},
        {"name": "Binokor", "icon": "🏢"},
    ],

    # Toshkent viloyati
    "chirchiq": [
        {"name": "1-4 mikrorayon", "icon": "🏢"},
        {"name": "Avezov", "icon": "🌳"},
        {"name": "Chirchiq vokzal", "icon": "🚉"},
        {"name": "Troitsk", "icon": "🏭"},
        {"name": "Barakat bozori", "icon": "🏬"},
        {"name": "Damba", "icon": "🌊"},
    ],
    "olmaliq": [
        {"name": "5-mikrorayon", "icon": "🏢"},
        {"name": "Metallurg", "icon": "🌳"},
        {"name": "Markaziy bozor", "icon": "🏬"},
        {"name": "Raduga", "icon": "🏡"},
        {"name": "Ramiz bog'i", "icon": "🌳"},
    ],
    "angren": [
        {"name": "1-5 dahalar", "icon": "🏢"},
        {"name": "Angren markaz", "icon": "🌳"},
        {"name": "Dehqon bozor", "icon": "🏬"},
        {"name": "Yangiobod", "icon": "🏡"},
        {"name": "Shaxtyor", "icon": "🏭"},
    ],
    "bekobod": [
        {"name": "1-14 mavzelar", "icon": "🏢"},
        {"name": "Bekobod markaz", "icon": "🌳"},
        {"name": "Metallurg", "icon": "🏭"},
        {"name": "Dehqon bozor", "icon": "🏬"},
    ],
    "zangiota": [
        {"name": "Eshonguzar", "icon": "🕌"},
        {"name": "Nazarbek", "icon": "🏡"},
        {"name": "Qashqarlik", "icon": "🏡"},
        {"name": "Erkin", "icon": "🏡"},
        {"name": "Keles atrofi", "icon": "🌳"},
        {"name": "O'rikzor atrofi", "icon": "🏪"},
    ],
    "qibray": [
        {"name": "Qibray markaz", "icon": "🌳"},
        {"name": "O'nqo'rg'on", "icon": "🏡"},
        {"name": "Baytqo'rg'on", "icon": "🏡"},
        {"name": "Salar", "icon": "🌳"},
        {"name": "Bo'zsuv", "icon": "🌊"},
        {"name": "ToshGres", "icon": "🏡"},
    ],
    "toshkent_t": [
        {"name": "Keles shahar", "icon": "🏡"},
        {"name": "Hasanboy atrofi", "icon": "🏡"},
        {"name": "Ko'ksaroy", "icon": "🏡"},
        {"name": "Chuqursoy atrofi", "icon": "🌳"},
        {"name": "G'ishtko'prik", "icon": "🌉"},
    ],
    "yangiyol": [
        {"name": "Yangiyo'l markaz", "icon": "🏢"},
        {"name": "Gulbahor", "icon": "🚉"},
        {"name": "Niyozbosh", "icon": "🏡"},
        {"name": "Yangiyo'l bozor", "icon": "🏬"},
        {"name": "Sho'ralisoy", "icon": "🏡"},
    ],
    "bostoliq": [
        {"name": "G'azalkent", "icon": "🏔"},
        {"name": "Chorvoq", "icon": "🌊"},
        {"name": "Chimyon", "icon": "🏔"},
        {"name": "Xumson", "icon": "🌲"},
        {"name": "Burchmulla", "icon": "🏡"},
        {"name": "Soyliq", "icon": "🏞"},
    ],
    "yuqorichirchiq": [
        {"name": "Yangibozor", "icon": "🌳"},
        {"name": "Bardanko'l", "icon": "🏡"},
        {"name": "Mirobod qishloq", "icon": "🏡"},
        {"name": "Parkent yo'li", "icon": "🌳"},
    ],

    # Samarqand viloyati
    "samarkand_sh": [
        {"name": "Registon", "icon": "🕌"},
        {"name": "Sug'diyona", "icon": "🏢"},
        {"name": "Gagarin", "icon": "🌳"},
        {"name": "Vokzal", "icon": "🚉"},
        {"name": "Siyob bozori", "icon": "🕌"},
        {"name": "Sartepo mavzesi", "icon": "🏬"},
        {"name": "Mikrorayon", "icon": "🏢"},
        {"name": "Spitamen", "icon": "🛣"},
    ],
    "kattaqorgon": [
        {"name": "Kattaqo'rg'on markaz", "icon": "🏢"},
        {"name": "Dehqon bozor", "icon": "🏬"},
        {"name": "Vokzal", "icon": "🚉"},
    ],
    "urgut": [
        {"name": "Urgut bozor", "icon": "🏬"},
        {"name": "Urgut markaz", "icon": "🌳"},
        {"name": "Pochvon", "icon": "🏡"},
    ],
    "pastdargom": [
        {"name": "Juma shahar", "icon": "🌳"},
        {"name": "Markaz", "icon": "🏡"},
    ],
    "samarkand_t": [
        {"name": "Gulobod", "icon": "🏡"},
        {"name": "Qorasuv mavzesi", "icon": "🌳"},
        {"name": "Motrid", "icon": "🏡"},
    ],

    # Farg'ona viloyati
    "fergana_sh": [
        {"name": "Farg'ona markaz", "icon": "🌳"},
        {"name": "Qirguli dahasi", "icon": "🏢"},
        {"name": "Frunzenskiy", "icon": "🏬"},
        {"name": "Al-Farg'oniy bog'i", "icon": "🌳"},
        {"name": "1-mikrorayon", "icon": "🏢"},
        {"name": "Oq-ariq", "icon": "🏬"},
    ],
    "qoqon": [
        {"name": "Xudoyorxon o'rdasi", "icon": "🏛"},
        {"name": "Charxiy", "icon": "🏢"},
        {"name": "Yangi bozor", "icon": "🏬"},
        {"name": "Qo'qon markaz", "icon": "🏡"},
    ],
    "margilon": [
        {"name": "Ipakchilar", "icon": "🧣"},
        {"name": "Xonaqa", "icon": "🕌"},
        {"name": "Vokzal bo'yi", "icon": "🏬"},
        {"name": "Buloqboshi", "icon": "🏡"},
    ],
    "quvasoy": [
        {"name": "Quvasoy markaz", "icon": "🌳"},
        {"name": "Do'stlik", "icon": "🏢"},
        {"name": "Sementchilar", "icon": "🏭"},
    ],
    "rishton": [
        {"name": "Kulollar markazi", "icon": "🏺"},
        {"name": "Rishton markaz", "icon": "🌳"},
    ],

    # Andijon viloyati
    "andijan_sh": [
        {"name": "Yangi bozor", "icon": "🏢"},
        {"name": "Eski shahar", "icon": "🏬"},
        {"name": "1-5 mikrorayonlar", "icon": "🏢"},
        {"name": "Bobur shohko'chasi", "icon": "🌳"},
        {"name": "Klara Setkin", "icon": "🏡"},
        {"name": "2-kichik daha", "icon": "🏢"},
    ],
    "asaka": [
        {"name": "Avtozavod atrofi", "icon": "🚗"},
        {"name": "Asaka markaz", "icon": "🌳"},
        {"name": "Dehqon bozor", "icon": "🏬"},
    ],
    "shaxrixon": [
        {"name": "Shahrixon markaz", "icon": "🌳"},
        {"name": "Bozor atrofi", "icon": "🏬"},
        {"name": "Shahrixonsoy", "icon": "🏡"},
    ],
    "xonobod": [
        {"name": "Suv ombori", "icon": "🌊"},
        {"name": "Xonobod markaz", "icon": "🌳"},
        {"name": "Fozilmon", "icon": "🏔"},
    ],

    # Namangan viloyati
    "namangan_sh": [
        {"name": "Chorsu", "icon": "🌳"},
        {"name": "Davlatobod dahasi", "icon": "🏢"},
        {"name": "Sardoba", "icon": "🏬"},
        {"name": "Yangi Namangan", "icon": "🌳"},
        {"name": "1-6 mikrorayonlar", "icon": "🏢"},
        {"name": "Afsonalar vodiysi", "icon": "🌸"},
    ],
    "chust": [
        {"name": "Chust markaz", "icon": "🌳"},
        {"name": "Pichoqchilar", "icon": "🔪"},
        {"name": "Bozor", "icon": "🏬"},
    ],
    "kosonsoy": [
        {"name": "Kosonsoy markaz", "icon": "🏞"},
        {"name": "Bog'ishamol", "icon": "🌳"},
    ],

    # Buxoro viloyati
    "bukhara_sh": [
        {"name": "Labihovuz", "icon": "🕌"},
        {"name": "5-6 mikrorayon", "icon": "🏢"},
        {"name": "Karvon bozor", "icon": "🏬"},
        {"name": "Shoxrux", "icon": "🌳"},
        {"name": "Ark atrofi", "icon": "🏢"},
        {"name": "Somoniylar bog'i", "icon": "🕌"},
    ],
    "gijduvon": [
        {"name": "G'ijduvon markaz", "icon": "🌳"},
        {"name": "Kulollar", "icon": "🏺"},
        {"name": "Bozor", "icon": "🏬"},
    ],
    "kogon": [
        {"name": "Kogon vokzal", "icon": "🚉"},
        {"name": "Kogon markaz", "icon": "🌳"},
        {"name": "Mikrorayon", "icon": "🏢"},
    ],

    # Qashqadaryo viloyati
    "qarshi_sh": [
        {"name": "Batumi", "icon": "🏢"},
        {"name": "Yangi bozor", "icon": "🏬"},
        {"name": "Registon", "icon": "🌳"},
        {"name": "1-8 mikrorayonlar", "icon": "🏢"},
        {"name": "Nasaf", "icon": "🛣"},
    ],
    "shahrisabz": [
        {"name": "Oqsaroy atrofi", "icon": "🏛"},
        {"name": "Shahrisabz markaz", "icon": "🌳"},
        {"name": "Dehqon bozor", "icon": "🏬"},
        {"name": "Ipak yo'li", "icon": "🛣"},
        {"name": "Chorsu", "icon": "🕌"},
    ],
    "koson": [
        {"name": "Koson markaz", "icon": "🌳"},
        {"name": "Dehqon bozor", "icon": "🏬"},
        {"name": "Pudina", "icon": "🏡"},
        {"name": "Mudin", "icon": "🏡"},
    ],

    # Surxondaryo viloyati
    "termiz_sh": [
        {"name": "Termiz markaz", "icon": "🌳"},
        {"name": "Alpomish", "icon": "🏢"},
        {"name": "Termiz bozor", "icon": "🏬"},
        {"name": "Termiziy", "icon": "🏢"},
    ],
    "denov": [
        {"name": "Denov bozor", "icon": "🏬"},
        {"name": "Denov markaz", "icon": "🌳"},
        {"name": "Qoraxon", "icon": "🏡"},
        {"name": "Yurchi", "icon": "🏡"},
    ],
    "sherobod": [
        {"name": "Sherobod markaz", "icon": "🌳"},
        {"name": "Xo'jamulki", "icon": "🏡"},
        {"name": "Bozor atrofi", "icon": "🏬"},
    ],

    # Xorazm viloyati
    "urganch_sh": [
        {"name": "Urganch markaz", "icon": "🌳"},
        {"name": "Shovot bo'yi", "icon": "🏬"},
        {"name": "Yoshlik", "icon": "🏢"},
        {"name": "1-mikrorayon", "icon": "🏢"},
    ],
    "xiva": [
        {"name": "Ichan qal'a", "icon": "🕌"},
        {"name": "Yangi shahar", "icon": "🏢"},
        {"name": "Dehqon bozor", "icon": "🏬"},
    ],
    "hazarasp": [
        {"name": "Hazorasp markaz", "icon": "🌳"},
        {"name": "Bozor atrofi", "icon": "🏬"},
        {"name": "Pitnak", "icon": "🏭"},
    ],

    # Navoiy viloyati
    "navoiy_sh": [
        {"name": "1-10 mikrorayonlar", "icon": "🏢"},
        {"name": "Navoiy parki", "icon": "🌳"},
        {"name": "Markaziy bozor", "icon": "🏬"},
        {"name": "G'alaba shohko'chasi", "icon": "🏢"},
    ],
    "zarafshon": [
        {"name": "1-mikrorayon", "icon": "🏢"},
        {"name": "2-mikrorayon", "icon": "🏢"},
        {"name": "3-4 mikrorayonlar", "icon": "🏢"},
        {"name": "Zarafshon markaz", "icon": "🌳"},
    ],
    "karmana": [
        {"name": "Karmana markaz", "icon": "🌳"},
        {"name": "Mir Said Bahrom", "icon": "🕌"},
        {"name": "Bozor", "icon": "🏬"},
    ],

    # Jizzax viloyati
    "jizzax_sh": [
        {"name": "Jizzax markaz", "icon": "🌳"},
        {"name": "Sayiljoy", "icon": "🏢"},
        {"name": "Toshkentlik", "icon": "🏬"},
        {"name": "Olmazor mavzesi", "icon": "🏢"},
    ],
    "zomin": [
        {"name": "Zomin markaz", "icon": "🌳"},
        {"name": "Zomin sanatoriy", "icon": "🏔"},
        {"name": "Dashtobod", "icon": "🏡"},
    ],
    "gallaorol": [
        {"name": "G'allaorol markaz", "icon": "🌳"},
        {"name": "Marjonbuloq", "icon": "🏡"},
        {"name": "Bozor", "icon": "🏬"},
    ],

    # Sirdaryo viloyati
    "guliston_sh": [
        {"name": "Guliston 1-4 mavzelar", "icon": "🏢"},
        {"name": "Guliston markaz", "icon": "🌳"},
        {"name": "Dehqon bozor", "icon": "🏬"},
    ],
    "shirin": [
        {"name": "Shirin markaz", "icon": "🌳"},
        {"name": "Farhod GES", "icon": "⚡️"},
        {"name": "Energetiklar", "icon": "🏢"},
    ],
    "yangiyer": [
        {"name": "Yangiyer markaz", "icon": "🏢"},
        {"name": "1-mikrorayon", "icon": "🏢"},
        {"name": "Vokzal", "icon": "🚉"},
    ],

    # Qoraqalpog'iston Respublikasi
    "nukus_sh": [
        {"name": "Nukus 22-23 mikrorayon", "icon": "🏢"},
        {"name": "Markaziy bozor", "icon": "🏬"},
        {"name": "Berdaq shohko'chasi", "icon": "🌳"},
        {"name": "Muzey atrofi", "icon": "🏛"},
    ],
    "beruniy": [
        {"name": "Beruniy markaz", "icon": "🌳"},
        {"name": "Bozor", "icon": "🏬"},
        {"name": "Do'stlik", "icon": "🏡"},
    ],
    "xojayli": [
        {"name": "Xo'jayli markaz", "icon": "🌳"},
        {"name": "Vokzal", "icon": "🚉"},
        {"name": "Bozor", "icon": "🏬"},
    ],
    "qongirot": [
        {"name": "Qo'ng'irot markaz", "icon": "🌳"},
        {"name": "Bozor", "icon": "🏬"},
        {"name": "Oltinko'l", "icon": "🏡"},
    ]
}

# Popular areas fallback for when entire region is chosen (district: "all")
REGION_POPULAR_AREAS = {
    "tashkent_city": [
        {"name": "Chilonzor", "icon": "🏡"},
        {"name": "Yunusobod", "icon": "🏙"},
        {"name": "Novza", "icon": "🌳"},
        {"name": "Qatortol", "icon": "🏙"},
        {"name": "Buyuk Ipak Yo'li", "icon": "🚇"},
        {"name": "Bodomzor", "icon": "🌳"},
        {"name": "Oybek", "icon": "🚇"},
        {"name": "Sergeli", "icon": "🏢"},
        {"name": "Qoraqamish", "icon": "🏢"},
        {"name": "TTZ", "icon": "🏭"},
        {"name": "Qorasuv", "icon": "🌊"},
        {"name": "Chorsu", "icon": "🕌"},
    ],
    "tashkent_obl": [
        {"name": "Chirchiq", "icon": "🏢"},
        {"name": "Olmaliq", "icon": "🏭"},
        {"name": "Angren", "icon": "⛏"},
        {"name": "Zangiota", "icon": "🕌"},
        {"name": "Qibray", "icon": "🌳"},
        {"name": "Yangiyo'l", "icon": "🏡"},
        {"name": "Chorvoq", "icon": "🌊"},
        {"name": "G'azalkent", "icon": "🏔"},
    ],
    "samarkand": [
        {"name": "Registon", "icon": "🕌"},
        {"name": "Sug'diyona", "icon": "🏢"},
        {"name": "Gagarin", "icon": "🌳"},
        {"name": "Sartepo", "icon": "🏬"},
        {"name": "Siyob bozori", "icon": "🕌"},
        {"name": "Kattaqo'rg'on", "icon": "🏢"},
    ],
    "fergana": [
        {"name": "Farg'ona markaz", "icon": "🌳"},
        {"name": "Qirguli", "icon": "🏢"},
        {"name": "Qo'qon", "icon": "🏛"},
        {"name": "Marg'ilon", "icon": "🧣"},
        {"name": "Quvasoy", "icon": "🏢"},
        {"name": "Rishton", "icon": "🏺"},
    ],
    "andijan": [
        {"name": "Yangi bozor", "icon": "🏢"},
        {"name": "Eski shahar", "icon": "🏬"},
        {"name": "Mikrorayon", "icon": "🏢"},
        {"name": "Asaka", "icon": "🚗"},
        {"name": "Shahrixon", "icon": "🌳"},
        {"name": "Xonobod", "icon": "🌊"},
    ],
    "namangan": [
        {"name": "Chorsu", "icon": "🌳"},
        {"name": "Davlatobod", "icon": "🏢"},
        {"name": "Sardoba", "icon": "🏬"},
        {"name": "Chust", "icon": "🔪"},
        {"name": "Afsonalar vodiysi", "icon": "🌸"},
    ],
    "bukhara": [
        {"name": "Labihovuz", "icon": "🕌"},
        {"name": "5-6 mikrorayon", "icon": "🏢"},
        {"name": "Karvon bozor", "icon": "🏬"},
        {"name": "G'ijduvon", "icon": "🏺"},
        {"name": "Kogon", "icon": "🚉"},
    ],
    "kashkadarya": [
        {"name": "Batumi", "icon": "🏢"},
        {"name": "Yangi bozor", "icon": "🏬"},
        {"name": "Shahrisabz", "icon": "🌳"},
        {"name": "Registon", "icon": "🏢"},
    ],
    "surxondaryo": [
        {"name": "Termiz markaz", "icon": "🌳"},
        {"name": "Alpomish", "icon": "🏢"},
        {"name": "Denov bozor", "icon": "🏬"},
    ],
    "khorezm": [
        {"name": "Urganch markaz", "icon": "🌳"},
        {"name": "Ichan qal'a (Xiva)", "icon": "🕌"},
        {"name": "Shovot bo'yi", "icon": "🏢"},
    ],
    "navoiy": [
        {"name": "1-10 mikrorayon", "icon": "🏢"},
        {"name": "Navoiy markaz", "icon": "🌳"},
        {"name": "Zarafshon", "icon": "🏢"},
    ],
    "jizzax": [
        {"name": "Jizzax markaz", "icon": "🌳"},
        {"name": "Sayiljoy", "icon": "🏢"},
        {"name": "Zomin sanatoriy", "icon": "🏔"},
    ],
    "sirdaryo": [
        {"name": "Guliston markaz", "icon": "🌳"},
        {"name": "1-4 mavzelar", "icon": "🏢"},
        {"name": "Yangiyer", "icon": "🚉"},
    ],
    "karakalpakstan": [
        {"name": "Nukus markaz", "icon": "🏢"},
        {"name": "Markaziy bozor", "icon": "🏬"},
        {"name": "Beruniy", "icon": "🌳"},
        {"name": "Xo'jayli", "icon": "🚉"},
    ]
}

def get_mahallas_for_district(district_id: str, region_id: str = "") -> list:
    """Get list of mahallas/areas for district or fallback to region's popular areas."""
    if district_id and district_id != "all":
        res = DISTRICT_MAHALLAS.get(district_id)
        if res:
            return res
    if region_id:
        res = REGION_POPULAR_AREAS.get(region_id)
        if res:
            return res
    return REGION_POPULAR_AREAS.get("tashkent_city", [])

