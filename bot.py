import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# Используем переменные окружения для безопасности
TOKEN = os.getenv("BOT_TOKEN", "7819916914:AAHuOv_6eph7IZ2OYyqq-zKz22yr_G4MIPk")
ADMIN_ID = int(os.getenv("ADMIN_ID", "445570258"))

bot = Bot(token=TOKEN)
dp = Dispatcher()

# ======== КАТАЛОГ ========
bikes = {
    "PRIMO": {
        "description": "🚴‍♂️ **PRIMO**\n\nМаневренная, универсальная модель для активного фанового катания в холмистой местности.\n\nБазовый уровень линейки — для зрелых любителей качества и современных тенденций велостроения.",
        "photo": "https://optim.tildacdn.com/tild6336-3032-4434-b935-346363326131/-/format/webp/Photo-70.webp",
        "specs": {
            "Вилка": "UDING DS HLO",
            "Передний переключатель": "SHIMANO ALTUS M315",
            "Задний переключатель": "SHIMANO ALTUS M310",
            "Шифтеры": "SHIMANO ALTUS M315 2x8s",
            "Тормоза": "SHIMANO MT 200",
            "Кассета": "SHIMANO CS-HG-41-8 11-34T",
            "Цепь": "TEC C8 16S",
            "Система": "PROWHEEL CY-10TM",
            "Картридж": "GINEYEA BB73 68mm",
            "Ротор": "SHIMANO RT-26S 160мм",
            "Втулки": "SOLON 901F/R AL",
            "Обода": "HENGTONG HLQC-GA10",
            "Покрышки": "KENDA K1162",
            "Руль": "ZOOM MTB AL 31,8 720/760мм",
            "Вынос": "ZOOM TDS-C301",
            "Грипсы": "VELO VLG-609",
            "Рулевая колонка": "GINEYEA GH-830",
            "Седло": "VELO VL-3534",
            "Подседельный штырь": "ZOOM SP-C212",
            "Педали": "FENGDE NW-430"
        }
    },
    "TERZO": {
        "description": "🚴‍♂️ **TERZO**\n\nНа треть эффективнее аналогов в этой нише.\nОтличное решение для тех, кто перерос прогулочный байк и готов для большего.",
        "photo": "https://optim.tildacdn.com/tild3531-3036-4463-b536-303235326633/-/format/webp/Photo-71.webp",
        "specs": {
            "Вилка": "UDING DS HLO",
            "Передний переключатель": "-",
            "Задний переключатель": "SHIMANO CUES 9S",
            "Шифтеры": "SHIMANO CUES 9S",
            "Тормоза": "SHIMANO MT 200",
            "Кассета": "SHIMANO CUES 11-41T 9S",
            "Цепь": "SHIMANO LG500",
            "Система": "PROWHEEL C10YNW-32T",
            "Картридж": "GINEYEA BB73 68mm",
            "Ротор": "SHIMANO RT-26M 180мм",
            "Втулки": "SOLON 901F/R AL",
            "Обода": "HENGTONG HLGC-GA10",
            "Покрышки": "KENDA K1162",
            "Руль": "ZOOM MTB AL 31,8 740/760мм",
            "Вынос": "ZOOM TDS-RD301",
            "Грипсы": "VELO VLG-609",
            "Рулевая колонка": "GINEYEA GH-830",
            "Седло": "VELO VL-3534",
            "Подседельный штырь": "ZOOM SP-C212",
            "Педали": "FENGDE NW-430"
        }
    },
    "ULTIMO": {
        "description": "🚴‍♂️ **ULTIMO**\n\nТоповый в линейке middle-сегмента трейловых велосипедов для прогрессирующих райдеров.\nПредназначен для гонок и катания на пересечённой местности со средним или существенным перепадом высот.",
        "photo": "https://optim.tildacdn.com/tild3637-6439-4237-b638-303336613863/-/format/webp/Photo-69.webp",
        "specs": {
            "Вилка": "UDING DS HLO",
            "Передний переключатель": "-",
            "Задний переключатель": "SHIMANO CUES 10S",
            "Шифтеры": "SHIMANO CUES 10S",
            "Тормоза": "SHIMANO MT 200",
            "Кассета": "SHIMANO CUES CS-LG400 11-48T 10S",
            "Цепь": "SHIMANO LG500",
            "Система": "PROWHEEL RMZ 32T",
            "Картридж": "PROWHEEL PW-MBB73 HOLOWTECH 2",
            "Ротор": "SHIMANO RT-26M 180мм",
            "Втулки": "SOLON 901F/R AL",
            "Обода": "HENGTONG HLGC-GA10",
            "Покрышки": "OBOR W3104",
            "Руль": "ZOOM MTB AL 31,8 740/760мм",
            "Вынос": "ZOOM TDS-C301",
            "Грипсы": "VELO VLG-609",
            "Рулевая колонка": "GINEYEA GH-830",
            "Седло": "VELO VL-3534",
            "Подседельный штырь": "ZOOM SP-C212",
            "Педали": "FENGDE NW-430"
        }
    },
    "TESORO": {
        "description": "🚴‍♂️ **TESORO**\n\nСбалансированный аппарат для катания в горах и холмистой местности, для техничных трасс с прыжками и виражами.",
        "photo": "https://optim.tildacdn.com/tild3932-3166-4537-b837-386365666162/-/format/webp/Photo-72.webp",
        "specs": {
            "Вилка": "ZOOM 868 AIR BOOST",
            "Передний переключатель": "-",
            "Задний переключатель": "SHIMANO CUES 115",
            "Шифтеры": "SHIMANO CUES 115",
            "Тормоза": "SHIMANO MT 200",
            "Кассета": "SHIMANO CUES CS-LG400 11-50T 11S",
            "Цепь": "SHIMANO LG500",
            "Система": "PROWHEEL RMZ 32T",
            "Картридж": "PROWHEEL PW-MB73 HOLOWITECH 2",
            "Ротор": "SHIMANO RT-26M 180мм",
            "Втулки": "SOLON 9081F/TR AL",
            "Обода": "ПИСТОНИРОВАННЫЙ STAR 32H",
            "Покрышки": "OBOR W3104",
            "Руль": "ZOOM MTB AL 31,8 740/760мм",
            "Вынос": "ZOOM TDS-RD307A",
            "Грипсы": "VELO VLG-609",
            "Рулевая колонка": "GINEYEA GH-830",
            "Седло": "VELO VLG-609",
            "Подседельный штырь": "ZOOM SP218",
            "Педали": "FENGDE NW-430"
        }
    },
    "OTTIMO": {
        "description": "🚴‍♂️ **OTTIMO**\n\nНа этом байке реально проехать кросс-кантрийный марафон, уверенно проходить сложные участки и крутые спуски.\nПозволяет чувствовать себя на равных с мировыми брендами в соревнованиях.",
        "photo": "https://optim.tildacdn.com/tild3662-3335-4362-a665-303137396364/-/format/webp/Photo-73.webp",
        "specs": {
            "Вилка": "ROCK SHOX FS RECON 29F",
            "Передний переключатель": "-",
            "Задний переключатель": "SHIMANO CUES 11S",
            "Шифтеры": "SHIMANO CUES 11S",
            "Тормоза": "SHIMANO MT 200",
            "Кассета": "SHIMANO CUES CS-LG400 11-50T 11S",
            "Цепь": "SHIMANO LG500",
            "Система": "SHIMANO CUES FC-U6000-1",
            "Картридж": "SHIMANO BB-M501 HOLOWTECH 2",
            "Ротор": "SHIMANO RT-26M 180мм",
            "Втулки": "SOLON 908TF/TR AL",
            "Обода": "ПИСТОНИРОВАННЫЙ STAR 32H",
            "Покрышки": "MAXXIS RECON M355",
            "Руль": "ZOOM MTB AL 31,8 740/760мм",
            "Вынос": "ZOOM TDS-D479",
            "Грипсы": "VELO VLG-1266-11D2",
            "Рулевая колонка": "GINEYEA GH-202",
            "Седло": "VELO 1C58",
            "Подседельный штырь": "ZOOM SP218"
        }
    }
}

# Размеры рам
frame_sizes = {
    "M (17\")": "163-177 см",
    "L (19\")": "173-187 см", 
    "XL (21\")": "182-197 см"
}

# Словарь для хранения выбранных моделей и размеров пользователей
user_selections = {}

# ======== /START ========
@dp.message(Command("start"))
async def start(msg: types.Message):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="Каталог 🚲")],
            [types.KeyboardButton(text="Позвать специалиста 👨‍💼")],
            [types.KeyboardButton(text="О нас ℹ️")]
        ],
        resize_keyboard=True
    )
    await msg.answer(
        "Привет! Я помогу выбрать велосипед 🚴‍♂️\n\nВыбери действие:",
        reply_markup=kb
    )

# ======== КНОПКА "ПОЗВАТЬ СПЕЦИАЛИСТА" ========
@dp.message(lambda m: m.text and "специалиста" in m.text.lower())
async def call_specialist(msg: types.Message):
    # Сообщение пользователю
    await msg.answer(
        "Отлично! Я уведомил специалиста о вашем запросе. "
        "С вами свяжутся в ближайшее время для консультации. ☎️\n\n"
        "Если у вас есть срочный вопрос, вы можете написать его прямо сейчас."
    )
    
    # Уведомление админу
    specialist_message = (
        "👨‍💼 **ЗАПРОС СПЕЦИАЛИСТА**\n\n"
        f"Пользователь: {msg.from_user.full_name}\n"
        f"ID: {msg.from_user.id}\n"
        f"Username: @{msg.from_user.username if msg.from_user.username else 'не указан'}\n\n"
        "⚠️ Свяжись с клиентом для консультации!"
    )
    
    await bot.send_message(ADMIN_ID, specialist_message)

# ======== КАТАЛОГ ========
@dp.message(lambda m: m.text and "Каталог" in m.text)
async def catalog(msg: types.Message):
    kb = types.InlineKeyboardMarkup(inline_keyboard=[])
    for bike in bikes:
        kb.inline_keyboard.append([types.InlineKeyboardButton(text=bike, callback_data=bike)])
    await msg.answer("Выбери модель:", reply_markup=kb)

# ======== ПОКАЗ МОДЕЛИ ========
@dp.callback_query(lambda c: c.data in bikes)
async def show_bike(callback: types.CallbackQuery):
    name = callback.data
    bike_data = bikes[name]
    text = bike_data["description"]
    photo_url = bike_data["photo"]
    
    kb = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text="📋 Спецификация", callback_data=f"specs_{name}")],
        [types.InlineKeyboardButton(text="🛒 Заказать", callback_data=f"order_{name}")],
        [types.InlineKeyboardButton(text="⬅️ Назад", callback_data="back_to_catalog")]
    ])
    
    await callback.message.answer_photo(
        photo=photo_url,
        caption=text,
        parse_mode="Markdown",
        reply_markup=kb
    )

# ======== ПОКАЗ СПЕЦИФИКАЦИИ ========
@dp.callback_query(lambda c: c.data.startswith("specs_"))
async def show_specs(callback: types.CallbackQuery):
    bike_name = callback.data.replace("specs_", "")
    bike_data = bikes[bike_name]
    specs = bike_data["specs"]
    
    # Формируем текст спецификации
    specs_text = f"🔧 **Спецификация {bike_name}**\n\n"
    for component, value in specs.items():
        specs_text += f"• **{component}:** {value}\n"
    
    kb = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text="⬅️ Назад к модели", callback_data=bike_name)],
        [types.InlineKeyboardButton(text="🛒 Заказать", callback_data=f"order_{bike_name}")]
    ])
    
    await callback.message.answer(
        specs_text,
        parse_mode="Markdown",
        reply_markup=kb
    )

# ======== ВЫБОР РАЗМЕРА РАМЫ ========
@dp.callback_query(lambda c: c.data.startswith("order_"))
async def select_frame_size(callback: types.CallbackQuery):
    bike_name = callback.data.replace("order_", "")
    
    # Сохраняем выбранную модель для пользователя
    user_selections[callback.from_user.id] = {"bike": bike_name}
    
    # Создаем клавиатуру с размерами рам
    kb = types.InlineKeyboardMarkup(inline_keyboard=[])
    for size, height_range in frame_sizes.items():
        kb.inline_keyboard.append([
            types.InlineKeyboardButton(
                text=f"{size} ({height_range})", 
                callback_data=f"size_{size}"
            )
        ])
    
    kb.inline_keyboard.append([
        types.InlineKeyboardButton(text="⬅️ Назад к модели", callback_data=bike_name)
    ])
    
    await callback.message.answer(
        f"Вы выбрали {bike_name}! 🚴‍♂️\n\n"
        "Теперь выбери размер рамы:",
        reply_markup=kb
    )

# ======== СОХРАНЕНИЕ РАЗМЕРА РАМЫ ========
@dp.callback_query(lambda c: c.data.startswith("size_"))
async def save_frame_size(callback: types.CallbackQuery):
    frame_size = callback.data.replace("size_", "")
    
    # Получаем диапазон роста для выбранного размера
    height_range = frame_sizes.get(frame_size, "")
    
    # Сохраняем размер рамы для пользователя
    user_id = callback.from_user.id
    if user_id in user_selections:
        user_selections[user_id]["frame_size"] = frame_size
        user_selections[user_id]["height_range"] = height_range
    
    bike_name = user_selections[user_id]["bike"]
    
    await callback.message.answer(
        f"Отлично! 🎯\n"
        f"Модель: {bike_name}\n"
        f"Размер рамы: {frame_size} ({height_range})\n\n"
        "Теперь напиши своё *имя и телефон*, чтобы мы связались с тобой по заказу.",
        parse_mode="Markdown"
    )

# ======== ПРИЁМ ЗАЯВКИ ========
@dp.message(lambda m: any(x.isdigit() for x in m.text) and len(m.text) > 5)
async def save_order(msg: types.Message):
    user_id = msg.from_user.id
    
    # Получаем данные пользователя
    user_data = user_selections.get(user_id, {})
    selected_bike = user_data.get("bike", "Неизвестная модель")
    frame_size = user_data.get("frame_size", "Не выбран")
    height_range = user_data.get("height_range", "")
    
    # Формируем сообщение для админа
    admin_message = (
        f"📩 Новая заявка:\n\n"
        f"👤 Пользователь: {msg.from_user.full_name}\n"
        f"🆔 ID: {user_id}\n"
        f"🚲 Модель: {selected_bike}\n"
        f"📏 Размер рамы: {frame_size} ({height_range})\n"
        f"📞 Контакты: {msg.text}"
    )
    
    await bot.send_message(ADMIN_ID, admin_message)
    await msg.answer("Спасибо! Мы свяжемся с тобой в ближайшее время!")
    
    # Очищаем выбор пользователя после отправки заявки
    if user_id in user_selections:
        del user_selections[user_id]

# ======== ВОЗВРАТ К КАТАЛОГУ ========
@dp.callback_query(lambda c: c.data == "back_to_catalog")
async def back_to_catalog(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(inline_keyboard=[])
    for bike in bikes:
        kb.inline_keyboard.append([types.InlineKeyboardButton(text=bike, callback_data=bike)])
    await callback.message.answer("Выбери модель:", reply_markup=kb)

# ======== ВОЗВРАТ К МОДЕЛИ ========
@dp.callback_query(lambda c: c.data in bikes)
async def back_to_bike(callback: types.CallbackQuery):
    name = callback.data
    bike_data = bikes[name]
    text = bike_data["description"]
    photo_url = bike_data["photo"]
    
    kb = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text="📋 Спецификация", callback_data=f"specs_{name}")],
        [types.InlineKeyboardButton(text="🛒 Заказать", callback_data=f"order_{name}")],
        [types.InlineKeyboardButton(text="⬅️ Назад", callback_data="back_to_catalog")]
    ])
    
    await callback.message.answer_photo(
        photo=photo_url,
        caption=text,
        parse_mode="Markdown",
        reply_markup=kb
    )

# ======== О НАС ========
@dp.message(lambda m: m.text and "О нас" in m.text)
async def about(msg: types.Message):
    await msg.answer(
        "Мы — команда *Velozames*, подбираем велосипеды для любых маршрутов и уровней подготовки.\n\n"
        "🌐 [Сайт](https://velozames.com)\n📞 Напиши нам прямо сюда — ответим лично!",
        parse_mode="Markdown",
        disable_web_page_preview=True
    )

# ======== ЗАПУСК ========
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    print("Бот запущен 🚴‍♂️")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
