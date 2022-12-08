import sqlite3

import aiogram
from aiogram.utils import callback_data

import keybord

from Const import bot, dp, cur, region_list

region = ()

n_active = 0
active_list = []


@dp.callback_query_handler(lambda c: c.data == 'active')
async def active(callback_query: aiogram.types.CallbackQuery):
    global n_active, active_list
    await bot.answer_callback_query(callback_query.id)
    try:
        n_active += 1
        for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
                "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE region=? and type = 'active' LIMIT 1 OFFSET ?",
                (region, n_active)):
            active_list.append(name)
            await bot.send_photo(callback_query.from_user.id,
                                 photo,
                                 f"🫧{name}\n"
                                 f"{about}\n"
                                 f"📍Адреса - {address}\n"
                                 f"{'Станція метро - ' + str(metro) if city == 'Київ' else 'Як дістатися - ' + str(metro)} \n"
                                 f"Години роботи {time}\n"
                                 f"Вартість - {cost}\n"
                                 f"{fishnet}", reply_markup=keybord.keyboard_inline_active)
    except sqlite3.InterfaceError:
        await bot.send_message(callback_query.from_user.id,
                               f"""Вкажіть будь ласка ваш регіон....\n ось доступні регіони - {region_list}\n Скоро регіонів буде більше:)""")
    if len(active_list) < n_active - 1:
        await bot.send_message(callback_query.from_user.id, "На даний момент це остання локація\n"
                                                            "Ми процюємо над тим щоб їх було  більше")
        n_active = 0
        active_list.clear()


n_eit = 0
eit_list = []


@dp.callback_query_handler(lambda c: c.data == 'cafe')
async def cafe(callback_query: aiogram.types.CallbackQuery):
    global n_eit, eit_list
    await bot.answer_callback_query(callback_query.id)
    try:
        n_eit += 1

        for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
                "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost FROM location WHERE type = 'eat' and region=? LIMIT 1 OFFSET ?",
                (region, n_eit)):
            eit_list.append(name)
            await bot.send_photo(callback_query.from_user.id,
                                 photo,
                                 f"🫧{name}\n"
                                 f"{about}\n"
                                 f"📍Адреса - {address}\n"
                                 f"{'Станція метро - ' + str(metro) if city == 'Київ' else 'Як дістатися - ' + str(metro)} \n"
                                 f"Години роботи {time}\n"
                                 f"Вартість - {cost}\n"
                                 f"{fishnet}", reply_markup=keybord.keyboard_inline_cafe)
    except sqlite3.InterfaceError:
        await bot.send_message(callback_query.from_user.id,
                               f"""Вкажіть будь ласка ваш регіон....\n ось доступні регіони - {region_list}\n Скоро регіонів буде більше:)""")
    if len(eit_list) < n_eit - 1:
        await bot.send_message(callback_query.from_user.id, "На даний момент це остання локація\n"
                                                            "Ми процюємо над тим щоб їх було  більше")
        n_eit = 0
        eit_list.clear()


n_forgotten = 0
forgotten_list = []


@dp.callback_query_handler(lambda c: c.data == 'forgotten')
async def forgotten(callback_query: aiogram.types.CallbackQuery):
    global n_forgotten
    global forgotten_list
    await bot.answer_callback_query(callback_query.id)
    try:
        n_forgotten += 1
        for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
                "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE region=? and type = 'forgotten' LIMIT 1 OFFSET ?",
                (region, n_forgotten)):
            forgotten_list.append(name)
            await bot.send_photo(callback_query.from_user.id,
                                 photo,
                                 f"🫧{name}\n"
                                 f"{about}\n"
                                 f"📍Адреса - {address}\n"
                                 f"{'Станція метро - ' + str(metro) if city == 'Київ' else 'Як дістатися - ' + str(metro)} \n"
                                 f"Години роботи {time}\n"
                                 f"Вартість - {cost}\n"
                                 f"{fishnet}", reply_markup=keybord.keyboard_inline_forgotten)
    except sqlite3.InterfaceError:
        await bot.send_message(callback_query.from_user.id,
                               f"""Вкажіть будь ласка ваш регіон....\n ось доступні регіони - {region_list}\n Скоро регіонів буде більше:)""")
    if len(forgotten_list) < n_forgotten - 1:
        await bot.send_message(callback_query.from_user.id, "На даний момент це остання локація\n"
                                                            "Ми процюємо над тим щоб їх було  більше")
        n_forgotten = 0
        forgotten_list.clear()


n_nature = 0
nature_list = []


@dp.callback_query_handler(lambda c: c.data == 'nature')
async def nature(callback_query: aiogram.types.CallbackQuery):
    global n_nature, nature_list
    await bot.answer_callback_query(callback_query.id)
    try:
        n_nature += 1
        for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
                "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE region=? and type = 'nature' LIMIT 1 OFFSET ?",
                (region, n_nature)):
            nature_list.append(name)
            await bot.send_photo(callback_query.from_user.id,
                                 photo,
                                 f"🫧{name}\n"
                                 f"{about}\n"
                                 f"📍Адреса - {address}\n"
                                 f"{'Станція метро - ' + str(metro) if city == 'Київ' else 'Як дістатися - ' + str(metro)} \n"
                                 f"Години роботи {time}\n"
                                 f"Вартість - {cost}\n"
                                 f"{fishnet}", reply_markup=keybord.keyboard_inline_nature)
    except sqlite3.InterfaceError:
        await bot.send_message(callback_query.from_user.id,
                               f"""Вкажіть будь ласка ваш регіон....\n ось доступні регіони - {region_list}\n Скоро регіонів буде більше:)""")
    if len(nature_list) < n_nature - 1:
        await bot.send_message(callback_query.from_user.id, "На даний момент це остання локація\n"
                                                            "Ми процюємо над тим щоб їх було  більше")
        n_nature = 0
        nature_list.clear()


n_panoramic = 0
panoramic_list = []


@dp.callback_query_handler(lambda c: c.data == 'panoramic')
async def panoramic(callback_query: aiogram.types.CallbackQuery):
    global n_panoramic, panoramic_list
    await bot.answer_callback_query(callback_query.id)
    try:
        n_panoramic += 1
        for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
                "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE region=? and type = 'panoramic' LIMIT 1 OFFSET ?",
                (region, n_panoramic)):
            panoramic_list.append(name)
            await bot.send_photo(callback_query.from_user.id,
                                 photo,
                                 f"🫧{name}\n"
                                 f"{about}\n"
                                 f"📍Адреса - {address}\n"
                                 f"{'Станція метро - ' + str(metro) if city == 'Київ' else 'Як дістатися - ' + str(metro)} \n"
                                 f"Години роботи {time}\n"
                                 f"Вартість - {cost}\n"
                                 f"{fishnet}", reply_markup=keybord.keyboard_inline_panoramic)
    except sqlite3.InterfaceError:
        await bot.send_message(callback_query.from_user.id,
                               f"""Вкажіть будь ласка ваш регіон....\n ось доступні регіони - {region_list}\n Скоро регіонів буде більше:)""")
    if len(panoramic_list) < n_panoramic - 1:
        await bot.send_message(callback_query.from_user.id, "На даний момент це остання локація\n"
                                                            "Ми процюємо над тим щоб їх було  більше")
        n_panoramic = 0
        panoramic_list.clear()


n_areas = 0
areas_list = []


@dp.callback_query_handler(lambda c: c.data == 'areas')
async def areas(callback_query: aiogram.types.CallbackQuery):
    global areas_list, n_areas
    await bot.answer_callback_query(callback_query.id)
    try:
        n_areas += 1
        for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
                "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE region=? and type = 'areas' LIMIT 1 OFFSET ?",
                (region, n_areas)):
            areas_list.append(name)
            await bot.send_photo(callback_query.from_user.id,
                                 photo,
                                 f"🫧{name}\n"
                                 f"{about}\n"
                                 f"📍Адреса - {address}\n"
                                 f"{'Станція метро - ' + str(metro) if city == 'Київ' else 'Як дістатися - ' + str(metro)} \n"
                                 f"Години роботи {time}\n"
                                 f"Вартість - {cost}\n"
                                 f"{fishnet}", reply_markup=keybord.keyboard_inline_areas)
    except sqlite3.InterfaceError:
        await bot.send_message(callback_query.from_user.id,
                               f"""Вкажіть будь ласка ваш регіон....\n ось доступні регіони - {region_list}\n Скоро регіонів буде більше:)""")
    if len(areas_list) < n_areas - 1:
        await bot.send_message(callback_query.from_user.id, "На даний момент це остання локація\n"
                                                            "Ми процюємо над тим щоб їх було  більше")
        n_areas = 0
        areas_list.clear()


n_hotels = 0
hotels_list = []


@dp.callback_query_handler(lambda c: c.data == 'hotels')
async def hotels(callback_query: aiogram.types.CallbackQuery):
    global n_hotels, hotels_list
    await bot.answer_callback_query(callback_query.id)
    try:
        n_hotels += 1
        for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
                "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE region=? and type = 'hotels' LIMIT 1 OFFSET ?",
                (region, n_hotels)):
            hotels_list.append(name)
            await bot.send_photo(callback_query.from_user.id,
                                 photo,
                                 f"🫧{name}\n"
                                 f"{about}\n"
                                 f"📍Адреса - {address}\n"
                                 f"{'Станція метро - ' + str(metro) if city == 'Київ' else 'Як дістатися - ' + str(metro)} \n"
                                 f"Години роботи {time}\n"
                                 f"Вартість - {cost}\n"
                                 f"{fishnet}", reply_markup=keybord.keyboard_inline_hotels)
    except sqlite3.InterfaceError:
        await bot.send_message(callback_query.from_user.id,
                               f"""Вкажіть будь ласка ваш регіон....\n ось доступні регіони - {region_list}\n Скоро регіонів буде більше:)""")
    if len(hotels_list) < n_hotels - 1:
        await bot.send_message(callback_query.from_user.id, "На даний момент це остання локація\n"
                                                            "Ми процюємо над тим щоб їх було  більше")
        n_hotels = 0
        hotels_list.clear()


n_museums = 0
museums_list = []


@dp.callback_query_handler(lambda c: c.data == 'museums')
async def forgotten(callback_query: aiogram.types.CallbackQuery):
    global n_museums, museums_list
    await bot.answer_callback_query(callback_query.id)
    try:
        n_museums += 1
        for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
                "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE region=? and type = 'museums' LIMIT 1 OFFSET ?",
                (region, n_museums)):
            museums_list.append(name)
            await bot.send_photo(callback_query.from_user.id,
                                 photo,
                                 f"🫧{name}\n"
                                 f"{about}\n"
                                 f"📍Адреса - {address}\n"
                                 f"{'Станція метро - ' + str(metro) if city == 'Київ' else 'Як дістатися - ' + str(metro)} \n"
                                 f"Години роботи {time}\n"
                                 f"Вартість - {cost}\n"
                                 f"{fishnet}", reply_markup=keybord.keyboard_inline_museums)
    except sqlite3.InterfaceError:
        await bot.send_message(callback_query.from_user.id,
                               f"""Вкажіть будь ласка ваш регіон....\n ось доступні регіони - {region_list}\n Скоро регіонів буде більше:)""")
    if len(museums_list) < n_museums - 1:
        await bot.send_message(callback_query.from_user.id, "На даний момент це остання локація\n"
                                                            "Ми процюємо над тим щоб їх було  більше")
        n_museums = 0
        museums_list.clear()


n_cathedrals = 0
cathedrals_list = []


@dp.callback_query_handler(lambda c: c.data == 'cathedrals')
async def cathedrals(callback_query: aiogram.types.CallbackQuery):
    global n_cathedrals, cathedrals_list
    await bot.answer_callback_query(callback_query.id)
    try:
        n_cathedrals += 1
        for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
                "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE region=? and type = 'church' LIMIT 1 OFFSET ?",
                (region, n_cathedrals)):
            cathedrals_list.append(name)
            await bot.send_photo(callback_query.from_user.id,
                                 photo,
                                 f"🫧{name}\n"
                                 f"{about}\n"
                                 f"📍Адреса - {address}\n"
                                 f"{'Станція метро - ' + str(metro) if city == 'Київ' else 'Як дістатися - ' + str(metro)} \n"
                                 f"Години роботи {time}\n"
                                 f"Вартість - {cost}\n"
                                 f"{fishnet}", reply_markup=keybord.keyboard_inline_cathedrals)
    except sqlite3.InterfaceError:
        await bot.send_message(callback_query.from_user.id,
                               f"""Вкажіть будь ласка ваш регіон....\n ось доступні регіони - {region_list}\n Скоро регіонів буде більше:)""")
    if len(cathedrals_list) < n_cathedrals - 1:
        await bot.send_message(callback_query.from_user.id, "На даний момент це остання локація\n"
                                                            "Ми процюємо над тим щоб їх було  більше")
        n_cathedrals = 0
        cathedrals_list.clear()


n_historical_monument = 0
historical_monument_list = []


@dp.callback_query_handler(lambda c: c.data == 'historical_monument')
async def forgotten(callback_query: aiogram.types.CallbackQuery):
    global n_historical_monument, historical_monument_list
    await bot.answer_callback_query(callback_query.id)
    try:
        n_historical_monument += 1
        for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
                "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE region=? and type = 'sights' LIMIT 1 OFFSET ?",
                (region, n_historical_monument)):
            historical_monument_list.append(name)
            await bot.send_photo(callback_query.from_user.id,
                                 photo,
                                 f"🫧{name}\n"
                                 f"{about}\n"
                                 f"📍Адреса - {address}\n"
                                 f"{'Станція метро - ' + str(metro) if city == 'Київ' else 'Як дістатися - ' + str(metro)} \n"
                                 f"Години роботи {time}\n"
                                 f"Вартість - {cost}\n"
                                 f"{fishnet}", reply_markup=keybord.keyboard_inline_historical_monument)
    except sqlite3.InterfaceError:
        await bot.send_message(callback_query.from_user.id,
                               f"""Вкажіть будь ласка ваш регіон....\n ось доступні регіони - {region_list}\n Скоро регіонів буде більше:)""")
    if len(historical_monument_list) < n_historical_monument - 1:
        await bot.send_message(callback_query.from_user.id, "На даний момент це остання локація\n"
                                                            "Ми процюємо над тим щоб їх було  більше")
        n_historical_monument = 0
        historical_monument_list.clear()


n_other = 0
other_list = []


@dp.callback_query_handler(lambda c: c.data == 'other')
async def forgotten(callback_query: aiogram.types.CallbackQuery):
    global n_other, other_list
    await bot.answer_callback_query(callback_query.id)
    try:
        n_other += 1
        for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
                "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE region=? and type = 'other' LIMIT 1 OFFSET ?",
                (region, n_other)):
            other_list.append(name)
            await bot.send_photo(callback_query.from_user.id,
                                 photo,
                                 f"🫧{name}\n"
                                 f"{about}\n"
                                 f"📍Адреса - {address}\n"
                                 f"{'Станція метро - ' + str(metro) if city == 'Київ' else 'Як дістатися - ' + str(metro)} \n"
                                 f"Години роботи {time}\n"
                                 f"Вартість - {cost}\n"
                                 f"{fishnet}", reply_markup=keybord.keyboard_inline_other)
    except sqlite3.InterfaceError:
        await bot.send_message(callback_query.from_user.id,
                               f"""Вкажіть будь ласка ваш регіон....\n ось доступні регіони - {region_list}\n Скоро регіонів буде більше:)""")
    if len(other_list) < n_other - 1:
        await bot.send_message(callback_query.from_user.id, "На даний момент це остання локація\n"
                                                            "Ми процюємо над тим щоб їх було  більше")
        n_other = 0
        other_list.clear()
