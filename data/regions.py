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
