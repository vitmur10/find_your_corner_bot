import aiogram
import sqlite3
import random

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

import keybord
from Const import TOKEN

# Initialize bot and dispatcher
bot = aiogram.Bot(token=TOKEN)
storage = MemoryStorage()
dp = aiogram.Dispatcher(bot, storage=storage)

con = sqlite3.connect("bd")
cur = con.cursor()


@dp.message_handler(commands=['start'])
async def hello(message: aiogram.types.Message):
    await message.answer("     Hello everybody 👋\nТи єдиний, хто нас знайшов, але не останній🤗\n"
                         "Ти вже підняв економіку України, будучи тут🇺🇦 \n"
                         "Ти готовий знайти райське місце безпеки та ще й почуватися як вдома?\n"
                         "Тоді обирай свій куточок👇", reply_markup=keybord.keyboard_menu)


class Location(StatesGroup):
    name = State()
    city = State()
    type = State()
    address = State()
    fishnet = State()


@dp.message_handler(commands=['add_loc'], commands_prefix='/')
async def add_location(message: aiogram.types.Message):
    await Location.name.set()
    await message.answer("тип")


@dp.message_handler(state=Location.name)  # Принимаем состояние
async def name(message: aiogram.types.Message, state: FSMContext):
    async with state.proxy() as data:  # Устанавливаем состояние ожидания
        data['name'] = message.text
    await message.answer("Місто і тип")
    await Location.next()


@dp.message_handler(state=Location.city)
async def type(message: aiogram.types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['city'] = message.text
    await message.answer("Адрес")
    await Location.next()


@dp.message_handler(state=Location.type)
async def type(message: aiogram.types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['type'] = message.text
    await message.answer("Адрес")
    await Location.next()


@dp.message_handler(state=Location.address)
async def address(message: aiogram.types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['address'] = message.text
    await message.answer('Надішліть силку')
    await Location.next()


@dp.message_handler(state=Location.fishnet)
async def fishnet(message: aiogram.types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['fishnet'] = message.text
    await state.finish()
    print(data)
    data = [
        (Location.name, Location.city, Location.type, Location.address, Location.fishnet)
    ]
    await message.answer(data)
    cur.executemany("INSERT INTO location VALUES(?, ?, ?, ?, ?)", data)
    con.commit()
    await message.answer(
        f' Локацію {Location.name} було додано\n'
        f'Місто:{Location.city}\n'
        f'Адрес:{Location.address}\n'
        f'Силка:{Location.fishnet}')


@dp.message_handler(content_types=['text'])
async def one(message: aiogram.types.Message):
    if message.text == 'Забуті місця Києва':
        await message.answer("Ось забуті місця Києва")
        for name, city, type, address, fishnet, about, photo in cur.execute(
                "SELECT name, city, type, address, fishnet, about, photo  FROM location WHERE type = 'Забуті місця Києва'"):
            """            await message.answer(f"🫧Назва:{name}\n"
                                     f"{about}\n"
                                     f"📍Адреса:{address}\n"
                                     f"{fishnet}")"""
            await bot.send_photo(message.chat.id,
                                 photo,
                                 f"🫧Назва:{name}\n"
                                 f"{about}\n"
                                 f"📍Адреса:{address}\n"
                                 f"{fishnet}")

    elif message.text == "Кафе":
        await message.answer('Ось варіанти кафе')
        for name, city, type, address, fishnet, about, photo in cur.execute(
                "SELECT name, city, type, address, fishnet, about, photo  FROM location WHERE type = 'Кафе'"):
            """            await message.answer(f"🫧Назва:{name}\n"
                                 f"{about}\n"
                                 f"📍Адреса:{address}\n"
                                 f"{fishnet}")"""
            await bot.send_photo(message.chat.id, photo,
                                 f"🫧Назва:{name}\n"
                                 f"{about}\n"
                                 f"📍Адреса:{address}\n"
                                 f"{fishnet}")

    elif message.text == 'Відпочинок на природі':
        await message.answer("Ось варіанти відпочинку на природі")
        for name, city, type, address, fishnet, about, photo in cur.execute(
                "SELECT name, city, type, address, fishnet, about, photo  FROM location WHERE type = 'Відпочинок на природі'"):
            """            await message.answer(f"🫧Назва:{name}\n"
                                     f"{about}\n"
                                     f"📍Адреса:{address}\n"
                                     f"{fishnet}")"""
            await bot.send_photo(message.chat.id,
                                 photo,
                                 f"🫧Назва:{name}\n"
                                 f"{about}\n"
                                 f"📍Адреса:{address}\n"
                                 f"{fishnet}")
    elif message.text == 'Активний відпочинок':
        await message.answer("Ось варіанти активного відпочинку")
        for name, city, type, address, fishnet, about, photo in cur.execute(
                "SELECT name, city, type, address, fishnet, about, photo  FROM location WHERE type = 'Активний відпочинок'"):
            """ await message.answer(f"🫧Назва:{name}\n"
                                     f"{about}\n"
                                     f"📍Адреса:{address}\n"
                                     f"{fishnet}")"""
            await bot.send_photo(message.chat.id,
                                 photo,
                                 f"🫧Назва:{name}\n"
                                 f"{about}\n"
                                 f"📍Адреса:{address}\n"
                                 f"{fishnet}")

@dp.message_handler(content_types=['text'])
async def filter_messages(message: types.Message):

    a = ['Відпочинь', 'Все буде добре']
    b = ['У тебе дуже гарна посмішка', 'Не думай про погане', 'Все буде добре']
    c = ['У тебе все вийде', 'Все буде добре']
    characters = {
        'z': 'Вийди отсюда розбійник🧏🧏🧏',
        'v': 'Пиздуйте нахуй отсюда йобаниє підараси👨‍🦲👨‍🦲👨‍🦲',
        'vz': 'Пиздець російській федерації⚰️⚰️⚰️',
        'Я втомився': a[random.randrange(0, len(a))],
        'Мені сумно': b[random.randrange(0, len(b))],
        'Я більше не можу': c[random.randrange(0, len(c))],
        'Я втомилася': a[random.randrange(0, len(a))]
    }
    for key in characters:
        if key == message.text:
            await message.reply(
                characters[key])
        elif set(key) == set(message.text.lower()):
            await message.reply(
                characters[key])

if __name__ == '__main__':
    aiogram.executor.start_polling(dp, skip_updates=True)
