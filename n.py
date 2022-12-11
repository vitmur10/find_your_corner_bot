import sqlite3

import aiogram
from aiogram.utils import callback_data

import keybord

from Const import bot, dp, cur, region_list

region = ()

n_active = 0
active_list = []
n_eit = 0
eit_list = []

n_forgotten = 0
forgotten_list = []

n_nature = 0
nature_list = []

n_panoramic = 0
panoramic_list = []

n_areas = 0
areas_list = []

n_hotels = 0
hotels_list = []

n_museums = 0
museums_list = []

n_cathedrals = 0
cathedrals_list = []

n_historical_monument = 0
historical_monument_list = []

n_other = 0
other_list = []

dick_n = {
    'active': [0, []],
    'eit': [],
    'forgotten': [],
    'nature': [],
    'panoramic': [],
    'areas': [],
    'hotels': [],
    'museums': [],
    'cathedrals': [],
    'historical_monument': [],
    'other': []
}


@dp.callback_query_handler(lambda сall: True)
async def active(callback_query: aiogram.types.CallbackQuery):
    global n_active, active_list
    await bot.answer_callback_query(callback_query.id)
    try:
        dick_n[callback_query.data][0] += 1
        print(dick_n[callback_query.data][0])
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
                                 f"{fishnet}", reply_markup=keybord.keyboard_inline_active)
    except sqlite3.InterfaceError:
        await bot.send_message(callback_query.from_user.id,
                               f"""Вкажіть будь ласка ваш регіон....\n ось доступні регіони - {region_list}\n Скоро регіонів буде більше:)""")
    if len(dick_n[callback_query.data][1]) == dick_n[callback_query.data][0] - 1:
        await bot.send_message(callback_query.from_user.id, "На даний момент це остання локація\n"
                                                            "Ми процюємо над тим щоб їх було  більше")
        dick_n[callback_query.data][0] = 0
        dick_n[callback_query.data][1].clear()
