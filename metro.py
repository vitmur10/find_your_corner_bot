import aiogram
from aiogram.utils import callback_data

import keybord
from Const import bot, dp, cur, con


@dp.callback_query_handler()
async def independence_square(callback_query: aiogram.types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE metro = ?", callback_data):
        await bot.send_photo(callback_query.from_user.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}")


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
