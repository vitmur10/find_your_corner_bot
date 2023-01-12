import sqlite3
import aiogram
import keybord
from Const import bot, dp, cur, region_list

region = ()

dick_n = {
    'active': [0, []],
    'eat': [0, []],
    'nature': [0, []],
    'panoramic': [0, []],
    'areas': [0, []],
    'hotels': [0, []],
    'museums': [0, []],
    'church': [0, []],
    'sights': [0, []],
    'other': [0, []],
    'forgotten_place': [0, []]
}


@dp.callback_query_handler(lambda c: True)
async def active(callback_query: aiogram.types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    try:
        dick_n[callback_query.data][0] += 1
        print(dick_n[callback_query.data][0])
        print(dick_n[callback_query.data][1])
        for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
                "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE region=? and type = ? LIMIT 1 OFFSET ?",
                (region, callback_query.data, dick_n[callback_query.data][0])):
            dick_n[callback_query.data][1].append(name)
            await bot.send_photo(callback_query.from_user.id,
                                 photo,
                                 f"🫧{name}\n"
                                 f"{about}\n"
                                 f"📍Адреса - {address} {city}\n"
                                 f"{'Станція метро - ' + str(metro) if city == 'Київ' else 'Як дістатися - ' + str(metro)} \n"
                                 f"Години роботи {time}\n"
                                 f"Вартість - {cost}\n"
                                 f"{fishnet}", reply_markup=keybord.loc_keybord[callback_query.data])
    except sqlite3.InterfaceError:
        await bot.send_message(callback_query.from_user.id,
                               f"""Вкажіть будь ласка ваш регіон....\n ось доступні регіони - {region_list}\n Скоро регіонів буде більше:)""")
    if len(dick_n[callback_query.data][1]) == dick_n[callback_query.data][0] - 1:
        await bot.send_message(callback_query.from_user.id, "На даний момент це остання локація\n"
                                                            "Ми процюємо над тим щоб їх було  більше")
        dick_n[callback_query.data][0] = 0
        dick_n[callback_query.data][1].clear()
