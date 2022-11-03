import random
import aiogram
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

import Const
import keybord, n, metro
from Const import bot, dp, cur, con

# Initialize bot and dispatcher


def analytics(func: callable):
    total_messages = 0
    users = set()
    total_users = 0

    def analytics_wrapper(message):
        nonlocal total_messages, total_users
        total_messages += 1

        if message.chat.id not in users:
            users.add(message.chat.id)
            total_users += 1
        data = [
            (
                total_users, message.text, total_messages
            )
        ]
        cur.executemany("INSERT INTO analytics VALUES(?, ?, ?)", data)
        con.commit()
        return func(message)

    return analytics_wrapper


@dp.message_handler(commands=['start'])
@analytics
async def hello(message: aiogram.types.Message):
    await message.answer("     Hello everybody 👋\nТи єдиний, хто нас знайшов, але не останній🤗\n"
                         "Ти вже підняв економіку України, будучи тут🇺🇦 \n"
                         "Ти готовий знайти райське місце безпеки та ще й почуватися як вдома?\n"
                         "Тоді обирай свій куточок👇")
    """await message.answer("Який регіон?")"""


@dp.message_handler(commands=['forgotten_place'])
@analytics
async def forgotten_place(message: aiogram.types.Message):
    await message.answer("Ось забуті місця Києва")
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE type = 'Забуті місця Києва'LIMIT 1 OFFSET ?", [n.n_forgotten]):
        await bot.send_photo(message.chat.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}", reply_markup=keybord.keyboard_inline_forgotten)


@dp.message_handler(commands=['eat'])
@analytics
async def eat(message: aiogram.types.Message):
    await message.answer('Ось варіанти де можна поїсти')
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE type = 'Кафе'LIMIT 1 OFFSET ?",
            [n.n_eit]):
        await bot.send_photo(message.chat.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}", reply_markup=keybord.keyboard_inline_cafe)


@dp.message_handler(commands=['nature'])
@analytics
async def nature(message: aiogram.types.Message):
    await message.answer("Ось варіанти відпочинку на природі")
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost FROM location WHERE type = 'Відпочинок на природі' LIMIT 1 OFFSET ?",
            [n.n_nature]):
        await bot.send_photo(message.chat.id, photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}", reply_markup=keybord.keyboard_inline_nature)


@dp.message_handler(commands=['active'])
@analytics
async def active(message: aiogram.types.Message):
    await message.answer("Ось варіанти активного відпочинку")
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost FROM location WHERE type = 'Активний відпочинок' LIMIT 1 OFFSET ?", [n.n_active]):
        await bot.send_photo(message.chat.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}"
                             f"{fishnet}", reply_markup=keybord.keyboard_inline_active)


@dp.message_handler(commands=['hotels'])
@analytics
async def hotels(message: aiogram.types.Message):
    await message.answer('Ось варіанти готелів')
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost FROM location WHERE type = 'Готель' LIMIT 1 OFFSET ?",
            [n.n_hotels]):
        await bot.send_photo(message.chat.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}", reply_markup=keybord.keyboard_inline_hotels)


@dp.message_handler(commands=['areas'])
@analytics
async def areas(message: aiogram.types.Message):
    await message.answer('Ось варіанти площів')
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost FROM location WHERE type = 'Площа' LIMIT 1 OFFSET ?",
            [n.n_areas]):
        await bot.send_photo(message.chat.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}", reply_markup=keybord.keyboard_inline_areas)


@dp.message_handler(commands=['museums'])
@analytics
async def museums(message: aiogram.types.Message):
    await message.answer('Ось варіанти музеїв')
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost FROM location WHERE type = 'Музей' LIMIT 1 OFFSET ?",
            [n.n_museums]):
        await bot.send_photo(message.chat.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}", reply_markup=keybord.keyboard_inline_museums)


@dp.message_handler(commands=['panoramic'])
@analytics
async def panoramic(message: aiogram.types.Message):
    await message.answer('Ось варіанти місць із панорамним видом')
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost FROM location WHERE type = 'Панорамний вид' LIMIT 1 OFFSET ?",
            [n.n_panoramic]):
        await bot.send_photo(message.chat.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}", reply_markup=keybord.keyboard_inline_panoramic)


@dp.message_handler(commands=['church'])
@analytics
async def church(message: aiogram.types.Message):
    await message.answer( 'Ось варіанти церквів, соборів, монастирів')
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost FROM location WHERE type = 'Церкви, собори, монастирі' LIMIT 1 OFFSET ?",
            [n.n_cathedrals]):
        await bot.send_photo(message.chat.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}", reply_markup=keybord.keyboard_inline_cathedrals)


@dp.message_handler(commands=['sights'])
@analytics
async def sights(message: aiogram.types.Message):
    await message.answer( "Ось варіанти історичних пам'яток")
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost FROM location WHERE type = 'Історична памятка' LIMIT 1 OFFSET ?",
            [n.n_historical_monument]):
        await bot.send_photo(message.chat.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}", reply_markup=keybord.keyboard_inline_historical_monument)


@dp.message_handler(commands=['other'])
@analytics
async def other(message: aiogram.types.Message):
    await message.answer( 'Ось інші локації')
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
        "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost FROM location WHERE type = 'Інше' LIMIT 1 OFFSET ?",
        [n.n_other]):
        await bot.send_photo(message.chat.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}", reply_markup=keybord.keyboard_inline_other)


@dp.message_handler(commands=['Support_the_product'])
@analytics
async def other(message: aiogram.types.Message):
    await message.answer('Реквізити👇', reply_markup=keybord.keyboard_donat)


@dp.message_handler(commands=['discussion'])
@analytics
async def discussion(message: aiogram.types.Message):
    await message.answer('Обговорення👇', reply_markup=keybord.keyboard_discussion)


@dp.message_handler(commands=['Search_by_subway'])
@analytics
async def other(message: aiogram.types.Message):
    await message.answer('Гілки метро', reply_markup=keybord.keyboard_metro)


@dp.message_handler(content_types=['text'])
@analytics
async def loc(message: aiogram.types.Message):
    global table
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
            await message.answer(
                characters[key])
        elif set(key) == set(message.text.lower()):
            await message.answer(
                characters[key])

    if message.text == 'Червона гілка':
        await message.answer('Червона гілка', reply_markup=keybord.keyboard_red_branch1)
    elif message.text == 'Синя гілка':
        await message.answer('Синя гілка', reply_markup=keybord.keyboard_blue_branch1)
    elif message.text == 'Зелена гілка':
        await message.answer('Зелена гілка', reply_markup=keybord.keyboard_green_branch1)




if __name__ == '__main__':
    aiogram.executor.start_polling(dp, skip_updates=True)
