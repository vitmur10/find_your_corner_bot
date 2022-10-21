import random
import aiogram
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

import keybord, n
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




@dp.message_handler(content_types=['text'])
@analytics
async def loc(message: aiogram.types.Message):
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

    if message.text == "Підтримати продукт":
        await message.answer('Реквізити👇', reply_markup=keybord.keyboard_donat)
    elif message.text == 'Пошук по метро':
        await message.answer('Гілки метро', reply_markup=keybord.keyboard_metro)
    elif message.text == 'Червона гілка':
        await message.answer('Червона гілка', reply_markup=keybord.keyboard_red_branch1)
    elif message.text == 'Синя гілка':
        await message.answer('Синя гілка', reply_markup=keybord.keyboard_blue_branch1)
    elif message.text == 'Зелена гілка':
        await message.answer('Зелена гілка', reply_markup=keybord.keyboard_green_branch1)


@dp.message_handler(commands=['forgotten_place'])
async def forgotten_place(message: aiogram.types.Message):
    await bot.send_message(message.chat.id,"Ось забуті місця Києва")
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
async def eat(message: aiogram.types.Message):
    await bot.send_message(message.chat.id,'Ось варіанти де можна поїсти')
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
async def nature(message: aiogram.types.Message):
    await bot.send_message(message.chat.id,"Ось варіанти відпочинку на природі")
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
async def active(message: aiogram.types.Message):
    await bot.send_message(message.chat.id,"Ось варіанти активного відпочинку")
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
async def hotels(message: aiogram.types.Message):
    await bot.send_message(message.chat.id,'Ось варіанти готелів')
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
async def areas(message: aiogram.types.Message):
    await bot.send_message(message.chat.id,'Ось варіанти площів')
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
async def museums(message: aiogram.types.Message):
    await bot.send_message(message.chat.id,'Ось варіанти музеїв')
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
async def panoramic(message: aiogram.types.Message):
    await bot.send_message(message.chat.id,'Ось варіанти місць із панорамним видом')
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
async def church(message: aiogram.types.Message):
    await bot.send_message(message.chat.id, 'Ось варіанти церквів, соборів, монастирів')
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
async def sights(message: aiogram.types.Message):
    await bot.send_message(message.chat.id, "Ось варіанти історичних пам'яток")
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
async def other(message: aiogram.types.Message):
    await bot.send_message(message.chat.id, 'Ось інші локації')
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


@dp.callback_query_handler(lambda c: c.data == 'Independence_Square')
async def independence_square(callback_query: aiogram.types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE metro = 'Майдан Незалежності'"):
        await bot.send_photo(callback_query.from_user.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}")


@dp.callback_query_handler(lambda c: c.data == 'Heroes_of_the_Dnipro')
async def heroes_of_the_dnipro(callback_query: aiogram.types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE metro = 'Героїв Дніпра'"):
        await bot.send_photo(callback_query.from_user.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}")


@dp.callback_query_handler(lambda c: c.data == 'Minsk')
async def minsk(callback_query: aiogram.types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE metro = 'Мінська'"):
        await bot.send_photo(callback_query.from_user.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}")


@dp.callback_query_handler(lambda c: c.data == 'Obolon')
async def obolon(callback_query: aiogram.types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE metro = 'Оболонь'"):
        await bot.send_photo(callback_query.from_user.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}")


@dp.callback_query_handler(lambda c: c.data == 'Petrivka')
async def petrivka(callback_query: aiogram.types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE metro = 'Петрівка'"):
        await bot.send_photo(callback_query.from_user.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}")


@dp.callback_query_handler(lambda c: c.data == 'Taras_Shevchenko')
async def taras_Shevchenko(callback_query: aiogram.types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE metro = 'Тараса Шевченка'"):
        await bot.send_photo(callback_query.from_user.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}")


@dp.callback_query_handler(lambda c: c.data == 'Contract_area')
async def contract_area(callback_query: aiogram.types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE metro = 'Контрактова площа'"):
        await bot.send_photo(callback_query.from_user.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}")


@dp.callback_query_handler(lambda c: c.data == 'Postal_square')
async def postal_square(callback_query: aiogram.types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE metro = 'Поштова площа'"):
        await bot.send_photo(callback_query.from_user.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}")


@dp.callback_query_handler(lambda c: c.data == 'Leo_Tolstoy_Square')
async def leo_tolstoy_square(callback_query: aiogram.types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE metro = 'Площа Льва Толстого'"):
        await bot.send_photo(callback_query.from_user.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}")


@dp.callback_query_handler(lambda c: c.data == 'Olympic')
async def olympic(callback_query: aiogram.types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE metro = 'Олімпійська'"):
        await bot.send_photo(callback_query.from_user.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}")


@dp.callback_query_handler(lambda c: c.data == 'Palace_Ukraine')
async def palace_Ukraine(callback_query: aiogram.types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE metro = 'Палац Україна'"):
        await bot.send_photo(callback_query.from_user.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}")


@dp.callback_query_handler(lambda c: c.data == 'Lybidska')
async def lybidska(callback_query: aiogram.types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE metro = 'Либідська'"):
        await bot.send_photo(callback_query.from_user.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}")


@dp.callback_query_handler(lambda c: c.data == 'Demyivska')
async def holosiivska(callback_query: aiogram.types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE metro = 'Демиївська'"):
        await bot.send_photo(callback_query.from_user.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}")


@dp.callback_query_handler(lambda c: c.data == 'Holosiivska')
async def next1(callback_query: aiogram.types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE metro = 'Голосіївська'"):
        await bot.send_photo(callback_query.from_user.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}")


@dp.callback_query_handler(lambda c: c.data == 'Vasylkivska')
async def vasylkivska(callback_query: aiogram.types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE metro = 'Васильківська'"):
        await bot.send_photo(callback_query.from_user.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}")


@dp.callback_query_handler(lambda c: c.data == 'Exhibition_center')
async def exhibition_center(callback_query: aiogram.types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE metro = 'Виставочний центр'"):
        await bot.send_photo(callback_query.from_user.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}")


@dp.callback_query_handler(lambda c: c.data == 'Racetrack')
async def racetrack(callback_query: aiogram.types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE metro = 'Іподром'"):
        await bot.send_photo(callback_query.from_user.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}")


@dp.callback_query_handler(lambda c: c.data == 'Teremka')
async def teremka(callback_query: aiogram.types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE metro = 'Теремки'"):
        await bot.send_photo(callback_query.from_user.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}")


@dp.callback_query_handler(lambda c: c.data == 'Red_village')
async def red_village(callback_query: aiogram.types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE metro = 'Червоний хутір'"):
        await bot.send_photo(callback_query.from_user.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}")


@dp.callback_query_handler(lambda c: c.data == 'Boryspilska')
async def boryspilska(callback_query: aiogram.types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE metro = 'Бориспільська'"):
        await bot.send_photo(callback_query.from_user.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}")


@dp.callback_query_handler(lambda c: c.data == 'Vyrlitsa')
async def vyrlitsa(callback_query: aiogram.types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE metro = 'Вирлиця'"):
        await bot.send_photo(callback_query.from_user.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}")


@dp.callback_query_handler(lambda c: c.data == 'Kharkivska')
async def kharkivska(callback_query: aiogram.types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE metro = 'Харківська'"):
        await bot.send_photo(callback_query.from_user.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}")


@dp.callback_query_handler(lambda c: c.data == 'Poznyaks')
async def poznyaks(callback_query: aiogram.types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE metro = 'Позняки'"):
        await bot.send_photo(callback_query.from_user.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}")


@dp.callback_query_handler(lambda c: c.data == 'Slavutych')
async def slavutych(callback_query: aiogram.types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE metro = 'Славутич'"):
        await bot.send_photo(callback_query.from_user.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}")


@dp.callback_query_handler(lambda c: c.data == 'Vydubychi')
async def vydubychi(callback_query: aiogram.types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE metro = 'Видубичі'"):
        await bot.send_photo(callback_query.from_user.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}")


@dp.callback_query_handler(lambda c: c.data == 'Friendship_of_peoples')
async def friendship_of_peoples(callback_query: aiogram.types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE metro = 'Дружба народів'"):
        await bot.send_photo(callback_query.from_user.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}")


@dp.callback_query_handler(lambda c: c.data == 'Klovska')
async def klovska(callback_query: aiogram.types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE metro = 'Кловська'"):
        await bot.send_photo(callback_query.from_user.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}")


@dp.callback_query_handler(lambda c: c.data == 'Pecherska')
async def pecherska(callback_query: aiogram.types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE metro = 'Печерська'"):
        await bot.send_photo(callback_query.from_user.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}")


@dp.callback_query_handler(lambda c: c.data == 'Palace_of_Sports')
async def palace_of_sports(callback_query: aiogram.types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE metro = 'Палац спорту'"):
        await bot.send_photo(callback_query.from_user.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}")


@dp.callback_query_handler(lambda c: c.data == 'Golden_Gate')
async def golden_Gate(callback_query: aiogram.types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE metro = 'Золоті ворота'"):
        await bot.send_photo(callback_query.from_user.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}")


@dp.callback_query_handler(lambda c: c.data == 'Lukyanivska')
async def lukyanivska(callback_query: aiogram.types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE metro = 'Лукянівська'"):
        await bot.send_photo(callback_query.from_user.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}")


@dp.callback_query_handler(lambda c: c.data == 'dear_ones')
async def dear_ones(callback_query: aiogram.types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE metro = 'Дорогожичі'"):
        await bot.send_photo(callback_query.from_user.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}")


@dp.callback_query_handler(lambda c: c.data == 'raw')
async def raw(callback_query: aiogram.types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE metro = 'Сирець'"):
        await bot.send_photo(callback_query.from_user.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}")


@dp.callback_query_handler(lambda c: c.data == 'Akademistechko')
async def akademistechko(callback_query: aiogram.types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE metro = 'Академмістечко'"):
        await bot.send_photo(callback_query.from_user.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}")


@dp.callback_query_handler(lambda c: c.data == 'Zhytomyr')
async def zhytomyr(callback_query: aiogram.types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE metro = 'Житомирська'"):
        await bot.send_photo(callback_query.from_user.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}")


@dp.callback_query_handler(lambda c: c.data == 'Svyatoshyn')
async def svyatoshyn(callback_query: aiogram.types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE metro = 'Святошин'"):
        await bot.send_photo(callback_query.from_user.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}")


@dp.callback_query_handler(lambda c: c.data == 'Nykvy')
async def nykvy(callback_query: aiogram.types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE metro = 'Нивки'"):
        await bot.send_photo(callback_query.from_user.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}")


@dp.callback_query_handler(lambda c: c.data == 'Beresteyska')
async def beresteyska(callback_query: aiogram.types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE metro = 'Берестейська'"):
        await bot.send_photo(callback_query.from_user.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}")


@dp.callback_query_handler(lambda c: c.data == 'Shulyavska')
async def shulyavska(callback_query: aiogram.types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE metro = 'Шулявська'"):
        await bot.send_photo(callback_query.from_user.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}")


@dp.callback_query_handler(lambda c: c.data == 'Polytechnic_Institute')
async def polytechnic_Institute(callback_query: aiogram.types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE metro = 'Політехнічний інститут'"):
        await bot.send_photo(callback_query.from_user.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}")


@dp.callback_query_handler(lambda c: c.data == 'Svyatoshyn')
async def svyatoshyn(callback_query: aiogram.types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE metro = 'Святошин'"):
        await bot.send_photo(callback_query.from_user.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}")


@dp.callback_query_handler(lambda c: c.data == 'Station')
async def station(callback_query: aiogram.types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE metro = 'Вокзальна'"):
        await bot.send_photo(callback_query.from_user.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}")


@dp.callback_query_handler(lambda c: c.data == 'University')
async def university(callback_query: aiogram.types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE metro = 'Університет'"):
        await bot.send_photo(callback_query.from_user.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}")


@dp.callback_query_handler(lambda c: c.data == 'Theatrical')
async def theatrical(callback_query: aiogram.types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE metro = 'Театральна'"):
        await bot.send_photo(callback_query.from_user.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}")


@dp.callback_query_handler(lambda c: c.data == 'Khreshchatyk')
async def khreshchatyk(callback_query: aiogram.types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE metro = 'Хрещатик'"):
        await bot.send_photo(callback_query.from_user.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}")


@dp.callback_query_handler(lambda c: c.data == 'Arsenal')
async def arsenal(callback_query: aiogram.types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE metro = 'Арсенальна'"):
        await bot.send_photo(callback_query.from_user.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}")


@dp.callback_query_handler(lambda c: c.data == 'Dnipro')
async def dnipro(callback_query: aiogram.types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE metro = 'Дніпро'"):
        await bot.send_photo(callback_query.from_user.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}")


@dp.callback_query_handler(lambda c: c.data == 'Hydropark')
async def hydropark(callback_query: aiogram.types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE metro = 'Гідропарк'"):
        await bot.send_photo(callback_query.from_user.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}")


@dp.callback_query_handler(lambda c: c.data == 'Left_bank')
async def left_bank(callback_query: aiogram.types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE metro = 'Лівобережна'"):
        await bot.send_photo(callback_query.from_user.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}")


@dp.callback_query_handler(lambda c: c.data == 'Gift')
async def gift(callback_query: aiogram.types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE metro = 'Дарниця'"):
        await bot.send_photo(callback_query.from_user.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}")


@dp.callback_query_handler(lambda c: c.data == 'Chernihivska')
async def chernihivska(callback_query: aiogram.types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE metro = 'Чернігівська'"):
        await bot.send_photo(callback_query.from_user.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}")


@dp.callback_query_handler(lambda c: c.data == 'Lisova')
async def lisova(callback_query: aiogram.types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE metro = 'Лісова'"):
        await bot.send_photo(callback_query.from_user.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}")


@dp.callback_query_handler(lambda c: c.data == 'Next_red_branch')
async def next_red_branch(callback_query: aiogram.types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Червона гілка', reply_markup=keybord.keyboard_red_branch2)


@dp.callback_query_handler(lambda c: c.data == 'Back_red_branch')
async def back_red_branch(callback_query: aiogram.types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Червона гілка', reply_markup=keybord.keyboard_red_branch1)


@dp.callback_query_handler(lambda c: c.data == 'Next_blue_branch')
async def next_blue_branch(callback_query: aiogram.types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Синя гілка', reply_markup=keybord.keyboard_blue_branch2)


@dp.callback_query_handler(lambda c: c.data == 'Back_blue_branch')
async def back_blue_branch(callback_query: aiogram.types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Синя гілка', reply_markup=keybord.keyboard_blue_branch1)


@dp.callback_query_handler(lambda c: c.data == 'Next_green_branch')
async def next_green_branch(callback_query: aiogram.types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Зелена гілка', reply_markup=keybord.keyboard_green_branch2)


@dp.callback_query_handler(lambda c: c.data == 'Back_green_branch')
async def back_green_branch(callback_query: aiogram.types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Зелена гілка', reply_markup=keybord.keyboard_green_branch1)


if __name__ == '__main__':
    aiogram.executor.start_polling(dp, skip_updates=True)
