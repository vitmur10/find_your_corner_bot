import sqlite3
import aiogram
import keybord
import n
from Const import bot, dp, cur, region_list, characters
from analytics import analytics


# Initialize bot and dispatcher


@dp.message_handler(commands=['start'])
@analytics
async def hello(message: aiogram.types.Message):
    await message.answer("     Hello everybody 👋\nТи єдиний, хто нас знайшов, але не останній🤗\n"
                         "Ти вже підняв економіку України, будучи тут🇺🇦 \n"
                         "Ти готовий знайти райське місце безпеки та ще й почуватися як вдома?\n"
                         "Тоді обирай свій куточок👇")
    await message.answer("Вкажіть свою область...")


@dp.message_handler(commands=['region'])
async def regio(message: aiogram.types.Message):
    await message.answer(n.region)


@dp.message_handler(
    commands=['forgotten_place', 'eat', 'nature', 'active', 'hotels', 'areas', 'museums', 'panoramic', 'church',
              'sights', 'other'])
@analytics
async def loc(message: aiogram.types.Message):
    try:
        print(n.dick_n[message.text[1:]][0])
        for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
                "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE region=? and type = ? LIMIT 1 OFFSET ?",
                (n.region, message.text[1:], n.dick_n[message.text[1:]][0])):
            await bot.send_photo(message.chat.id,
                                 photo,
                                 f"🫧{name}\n"
                                 f"{about}\n"
                                 f"📍Адреса - {address} {city}\n"
                                 f"{'Станція метро - ' + str(metro) if city == 'Київ' else 'Як дістатися - ' + str(metro)}\n"
                                 f"Години роботи {time}\n"
                                 f"Вартість - {cost}\n"
                                 f"{fishnet}", reply_markup=keybord.loc_keybord[message.text[1:]])
    except sqlite3.InterfaceError:
        print(n.region)
        await message.answer(f"""Вкажіть будь ласка ваш регіон....\n ось доступні регіони - {region_list}""")


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
    if message.text == 'Червона гілка':
        await message.answer('Червона гілка', reply_markup=keybord.keyboard_red_branch1)
    elif message.text == 'Синя гілка':
        await message.answer('Синя гілка', reply_markup=keybord.keyboard_blue_branch1)
    elif message.text == 'Зелена гілка':
        await message.answer('Зелена гілка', reply_markup=keybord.keyboard_green_branch1)

    for key in characters:
        if key == message.text:
            await message.answer(
                characters[key])
        elif set(key) == set(message.text.lower()):
            await message.answer(
                characters[key])

    for i in region_list:
        if i == message.text:
            n.region = i
            n.dick_n = {
                'active': [0, []],
                'eat': [0, []],
                'nature': [0, []],
                'panoramic': [0, []],
                'areas': [0, []],
                'hotels': [0, []],
                'museums': [0, []],
                'church': [0, []],
                'historical_monument': [0, []],
                'other': [0, []],
                'forgotten_place': [0, []]
            }
            await message.answer(f"""Ви вказали регіон {n.region}""")
    return n.region


if __name__ == '__main__':
    aiogram.executor.start_polling(dp, skip_updates=True)
