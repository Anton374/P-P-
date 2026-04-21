import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "8566867923:AAEQ3VgpLpLbvnnCVIflm2STn3I8cW5NQ6Q"
CHANNEL_LINK = "https://t.me/stakanp2p"
REVIEWS_LINK = "https://t.me/otzyvi_islamp2p"
YOUTUBE_LINK = "https://youtu.be/I6Y0yTSy1q0"

# ID канала (получи у бота @getmyid_bot)
CHANNEL_ID = -1003573202097

bot = Bot(token=TOKEN)
dp = Dispatcher()

# ===== ТЕКСТ ПРИВЕТСТВИЯ =====
WELCOME_TEXT = """Привет 🤝 классно что ты здесь!

Кто я такой и чем я занимаюсь?

- я в p2p более 2 лет
- стабильно занимаюсь в направление белого треугола ( работа без карт )
- более 50 учеников, и с каждым днем их больше
- вложил в свои знания более полумиллиона. Прошел вебинары у сильнейших специалистов
- заработал за месяц более 1.000.000 рублей в пике

Я сам начинал с нуля, не понимал в какую нишу я лезу. Я долго думал, не мог начать и в моменте решил рискнуть. И как видите у меня получилось

Я записал бесплатные уроки для новичков, забирай по кнопке 🎁."""

# ===== КЛАВИАТУРЫ =====
def get_main_keyboard():
    """Кнопки после подписки"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎬 БЕСПЛАТНЫЙ УРОК", url=YOUTUBE_LINK)],
        [InlineKeyboardButton(text="⭐ ОТЗЫВЫ УЧЕНИКОВ", url=REVIEWS_LINK)]
    ])

def get_request_keyboard():
    """Кнопка для подачи заявки"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📢 ПОДАТЬ ЗАЯВКУ", url=CHANNEL_LINK)]
    ])

# ===== ОБРАБОТЧИКИ =====
@dp.message(Command("start"))
async def start(message: types.Message):
    """Приветствие и инструкция"""
    await message.answer(
        f"{WELCOME_TEXT}\n\n"
        f"🔒 *Чтобы получить доступ к урокам:*\n\n"
        f"👇 *Нажми на кнопку и подай заявку* 👇",
        parse_mode="Markdown",
        reply_markup=get_request_keyboard()
    )

@dp.chat_join_request()
async def handle_join_request(request: types.ChatJoinRequest):
    """
    Срабатывает когда пользователь подал заявку
    Сразу одобряем и отправляем приветствие с кнопками
    """
    user_id = request.from_user.id
    
    # Одобряем заявку
    await request.approve()
    
    # Сразу отправляем приветствие и кнопки
    await bot.send_message(
        user_id,
        f"{WELCOME_TEXT}\n\n"
        f"✅ *Доступ открыт!*\n\n"
        f"👇 *Вот твои уроки и отзывы* 👇",
        parse_mode="Markdown",
        reply_markup=get_main_keyboard()
    )
    
    print(f"✅ Новый ученик: @{request.from_user.username} ({request.from_user.first_name})")

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    
    print("=" * 50)
    print("🚀 БОТ ЗАПУЩЕН!")
    print(f"📱 @{(await bot.get_me()).username}")
    print("=" * 50)
    print("💡 КАК ЭТО РАБОТАЕТ:")
    print("   1. Пользователь нажимает /start")
    print("   2. Видит приветствие и кнопку 'ПОДАТЬ ЗАЯВКУ'")
    print("   3. Нажимает и подает заявку в канал")
    print("   4. Бот ОДОБРЯЕТ заявку")
    print("   5. Бот СРАЗУ отправляет приветствие и 2 кнопки:")
    print("      - 🎬 БЕСПЛАТНЫЙ УРОК")
    print("      - ⭐ ОТЗЫВЫ УЧЕНИКОВ")
    print("=" * 50)
    
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())