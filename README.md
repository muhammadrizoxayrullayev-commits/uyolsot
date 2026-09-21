# 🏡 Uy Ol-Sot — Zamonaviy Telegram Bot & OLX Integratsiyasi

Ushbu loyiha O'zbekiston bo'ylab (12 ta viloyat va Toshkent shahri) ko'chmas mulk (hovli va kvartiralar) sotib olish, qidirish va filtrlash uchun yaratilgan zamonaviy, rang-barang va o'ta qulay Telegram botdir.

---

## ✨ Asosiy Imkoniyatlar

1. **🌐 3 xil tilda to'liq interfeys:**
   - 🇺🇿 O'zbekcha
   - 🇷🇺 Русский
   - 🇬🇧 English
2. **📍 To'liq geografik qamrov:**
   - 12 ta viloyat, Toshkent shahri va Qoraqalpog'iston Respublikasi.
   - Tanlangan viloyatga mos tumanlar ro'yxati (masalan, Toshkent shahri tanlansa: Chilonzor, Yunusobod, Mirzo Ulug'bek, Sergeli va b.).
3. **🏘 Mahalla va ko'cha bo'yicha qidiruv:**
   - Foydalanuvchi o'ziga kerakli mahallani kiritishi mumkin (masalan: `Dombirobod`, `Novza`, `Qatortol`) yoki butun tuman bo'yicha qidirish uchun `⏭ O'tkazib yuborish` tugmasini bosishi mumkin.
4. **🏢 Uy turi filtri:**
   - `🏢 Kvartira (Dom)`
   - `🏡 Hovli (Uchastka / Kottej)`
   - `🌐 Farqi yo'q (Barchasi)`
5. **📐 Kvadrat metr (Maydon) hisoblash:**
   - Tayyor oraliq tugmalari: `40-70 m²`, `70-100 m²`, `100-150 m²`, `150+ m²`
   - Erkin kiritish: agar `120` deb kiritilsa, bot avtomatik ravishda **±15%** (102 dan 138 m² gacha) oraliqni hisoblaydi! Yoki to'g'ridan-to'g'ri `120-150` deb kiritish mumkin.
6. **🛠 Ta'mir holati (Remont):**
   - 💎 Yevroremont / Yangi ta'mir
   - 🛠 O'rtacha ta'mir / Yaxshi
   - 🧱 Qora suvoq / Bez remont
   - 🌐 Farqi yo'q
7. **💰 Narx (Byudjet) filtrlari:**
   - Tayyor narx tugmalari yoki erkin summa kiritish.
8. **🖼 Rang-barang va qulay vizual kartochkalar:**
   - Sifatli rasmlar, sarlavha, narx ($ va so'mda), xonalar, qavat, ta'mir, manzil va sana.
   - `⬅️ Oldingi` / `Keyingi ➡️` varoqlash.
   - `🔗 OLX da ko'rish` to'g'ridan-to'g'ri havolasi.
   - `⭐ Sevimlilar` (yoqqan uylarni saqlab qo'yish va keyinchalik ko'rish).

---

## 🔑 OLX dan API Kalit Olish Bo'yicha Qo'llanma

### 1. Bot hoziroq ishlaydimi?
**HA!** Bot ichida zamonaviy `curl_cffi` drayveri o'rnatilgan. U OLX.uz serverlariga xuddi Google Chrome brauzeri kabi murojaat qilib, barcha yangi e'lonlar, rasmlar va narxlarni **hech qanday API kalitsiz ham hoziroq 100% aniqlikda** tortib bera oladi.

### 2. Rasmiy OLX API kalitini qanday olish mumkin?
Agar siz OLX ning rasmiy biznes hamkori (Partner API) kalitini olmoqchi bo'lsangiz, quyidagi bosqichlarni bajaring:

1. **OLX Developer Portaliga kiring:**
   - Havola: [https://developer.olx.uz](https://developer.olx.uz) (yoki mintaqaviy [https://developer.olx.ua](https://developer.olx.ua))
2. **Akkaunt yarating / Tizimga kiring:**
   - OLX akkauntingiz (telefon raqam yoki email) orqali kiring.
3. **Yangi Ilova (Application) yarating:**
   - `Applications` bo'limiga o'ting va `Create New Application` tugmasini bosing.
   - **App Name:** Masalan, `UyOlSotBot`
   - **Description:** Ko'chmas mulk qidirish va boshqarish boti.
   - **Redirect URI:** Agar veb-saytingiz bo'lmasa `http://localhost` yoki `https://t.me/your_bot_username` deb kiriting.
4. **Kalitlarni oling:**
   - Ilova yaratilgach, sizga quyidagi 2 ta maxfiy kalit beriladi:
     - `Client ID` (masalan: `200145`)
     - `Client Secret` (masalan: `a8f9b7c6d5e4f3a2...`)
5. **Kalitlarni `.env` faylga joylang:**
   Loyiha papkasidagi `.env` faylini ochib, quyidagilarni yozing:
   ```env
   OLX_CLIENT_ID=sizning_client_id
   OLX_CLIENT_SECRET=sizning_client_secret
   ```

---

## 🚀 Botni Ishga Tushirish

### 1. Kutubxonalarni o'rnatish:
```bash
pip install -r requirements.txt
```

### 2. Botni ishga tushirish:
```bash
python bot.py
```

### 3. Telegramda tekshirish:
Telegram qidiruvidan botingizni toping (yoki tokeningizga biriktirilgan bot nomiga o'ting) va `/start` buyrug'ini yuboring.

---

## 📁 Loyiha Strukturasi

```
uyolsot/
├── .env                  # Telegram token va OLX sozlamalari
├── requirements.txt      # Kutubxonalar ro'yxati
├── config.py             # Sozlamalar va yo'llar
├── database.py           # SQLite ma'lumotlar bazasi (foydalanuvchilar va sevimlilar)
├── locales.py            # 3 tildagi (UZ, RU, EN) matnlar
├── bot.py                # Asosiy ishga tushiruvchi fayl
├── data/
│   ├── regions.py        # 12 ta viloyat, Toshkent shahri va tumanlar ro'yxati
│   └── bot.db            # Ma'lumotlar bazasi fayli
├── services/
│   ├── olx_service.py    # OLX scraper va qidiruv filtrlash tizimi
│   └── olx_api.py        # Rasmiy OLX OAuth2 mijozi
└── handlers/
    ├── states.py         # Qadamma-qadam holatlar (FSM)
    ├── keyboards.py      # Rang-barang inline va menyu tugmalari
    ├── start.py          # /start va til tanlash
    ├── search.py         # 7 bosqichli qidiruv sehrgari
    ├── results.py        # Natijalar kartochkasi, varoqlash va saqlash
    └── settings.py       # Sevimlilar va sozlamalar
```
