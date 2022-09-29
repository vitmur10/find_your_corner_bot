import aiogram
import sqlite3
import keybord
from Const import TOKEN

# Initialize bot and dispatcher
bot = aiogram.Bot(token=TOKEN)
dp = aiogram.Dispatcher(bot)

con = sqlite3.connect("bd")
cur = con.cursor()


@dp.message_handler(commands=['start'])
async def hello(message: aiogram.types.Message):
    await message.answer("     Hello everybody 👋\nТи єдиний, хто нас знайшов, але не останній🤗\n"
                         "Ти вже підняв економіку України, будучи тут🇺🇦 \n"
                         "Ти готовий знайти райське місце безпеки та ще й почуватися як вдома?\n"
                         "Тоді обирай свій куточок👇", reply_markup=keybord.keyboard_menu)


@dp.message_handler(content_types=['text'])
async def one(message: aiogram.types.Message):
    if message.text == 'Забуті місця Києва':
        await message.answer("ОСь забуті місця Києва")
        for name, city, type, address in cur.execute("SELECT Name, city, type, address  FROM location WHERE type = 'Забуті місця Києва'"):
            await message.answer(f"🫧Назва:{name}\n"
                                 f"📍Адреса:{address}")
    elif message.text == "Кафе":
        await message.answer('Ось варіанти кафе')
        for name, city, type, address in cur.execute("SELECT Name, city, type, address  FROM location WHERE type = 'Кафе'"):
            await message.answer(f"🫧Назва:{name}\n"
                                 f"📍Адреса:{address}")
    elif message.text == 'Відпочинок на природі':
        await message.answer("Ось варіанти відпочинку на природі")
        for name, city, type, address in cur.execute("SELECT Name, city, type, address  FROM location WHERE type = 'Відпочинок на природі'"):
            await message.answer(f"🫧Назва:{name}\n"
                                 f"📍Адреса:{address}")
    elif message.text == 'Активний відпочинок':
        await message.answer("Ось варіанти активного відпочинку")
        for name, city, type, address in cur.execute("SELECT Name, city, type, address  FROM location WHERE type = 'Активний відпочинок'"):
            await message.answer(f"🫧Назва:{name}\n"
                                 f"📍Адреса:{address}")


if __name__ == '__main__':
    aiogram.executor.start_polling(dp, skip_updates=True)