from Const import bot, dp, cur, con
import aiogram, keybord



n_active = 0
active_list = []


@dp.callback_query_handler(lambda c: c.data == 'active')
async def active(callback_query: aiogram.types.CallbackQuery):
    global n_active
    global active_list
    n_active +=1
    await bot.answer_callback_query(callback_query.id)
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost FROM location WHERE type = 'Активний відпочинок' LIMIT 1 OFFSET ?",
            [n_active]):
        active_list.append(name)
        await bot.send_photo(callback_query.from_user.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}", reply_markup=keybord.keyboard_inline_active)
    if len(active_list) < n_active-1:
        await bot.send_message(callback_query.from_user.id, "На даний момент це остання локація\n"
                                                            "Ми процюємо над тим щоб їх було  більше")
        n_active = 0
        active_list.clear()


n_forgotten = 0
forgotten_list = []


@dp.callback_query_handler(lambda c: c.data == 'forgotten')
async def forgotten(callback_query: aiogram.types.CallbackQuery):
    global n_forgotten
    global forgotten_list
    n_forgotten +=1
    await bot.answer_callback_query(callback_query.id)
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE type = 'Забуті місця Києва'LIMIT 1 OFFSET ?",
            [n_forgotten]):
        forgotten_list.append(name)

        await bot.send_photo(callback_query.from_user.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}", reply_markup=keybord.keyboard_inline_forgotten)
    if len(forgotten_list) < n_forgotten-1:
        await bot.send_message(callback_query.from_user.id, "На даний момент це остання локація\n"
                                                            "Ми процюємо над тим щоб їх було  більше")
        n_forgotten = 0
        forgotten_list.clear()


n_eit = 0
eit_list= []


@dp.callback_query_handler(lambda c: c.data == 'cafe')
async def cafe(callback_query: aiogram.types.CallbackQuery):
    global n_eit, eit_list
    n_eit +=1
    await bot.answer_callback_query(callback_query.id)
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE type = 'Кафе'LIMIT 1 OFFSET ?",
        [n_eit]):
        eit_list.append(name)

        await bot.send_photo(callback_query.from_user.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}", reply_markup=keybord.keyboard_inline_forgotten)
    if len(eit_list) < n_eit-1:
        await bot.send_message(callback_query.from_user.id, "На даний момент це остання локація\n"
                                                            "Ми процюємо над тим щоб їх було  більше")
        n_eit = 0
        eit_list.clear()


n_nature = 0
nature_list = []


@dp.callback_query_handler(lambda c: c.data == 'nature')
async def nature(callback_query: aiogram.types.CallbackQuery):
    global n_nature, nature_list
    n_nature +=1
    await bot.answer_callback_query(callback_query.id)
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost FROM location WHERE type = 'Відпочинок на природі'LIMIT 1 OFFSET ?",
            [n_nature]):
        nature_list.append(name)

        await bot.send_photo(callback_query.from_user.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}", reply_markup=keybord.keyboard_inline_nature)
    if len(nature_list) < n_nature-1:
        await bot.send_message(callback_query.from_user.id, "На даний момент це остання локація\n"
                                                            "Ми процюємо над тим щоб їх було  більше")
        n_nature = 0
        nature_list.clear()


n_panoramic = 0
panoramic_list = []


@dp.callback_query_handler(lambda c: c.data == 'panoramic')
async def panoramic(callback_query: aiogram.types.CallbackQuery):
    global n_panoramic, panoramic_list
    n_panoramic +=1
    await bot.answer_callback_query(callback_query.id)
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost FROM location WHERE type = 'Панорамний вид' LIMIT 1 OFFSET ?",
            [n_panoramic]):
        panoramic_list.append(name)

        await bot.send_photo(callback_query.from_user.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}", reply_markup=keybord.keyboard_inline_panoramic)
    if len(panoramic_list) < n_panoramic-1:
        await bot.send_message(callback_query.from_user.id, "На даний момент це остання локація\n"
                                                            "Ми процюємо над тим щоб їх було  більше")
        n_panoramic = 0
        panoramic_list.clear()
n_areas = 0
areas_list = []


@dp.callback_query_handler(lambda c: c.data == 'areas')
async def areas(callback_query: aiogram.types.CallbackQuery):
    global areas_list, n_areas
    n_areas +=1
    await bot.answer_callback_query(callback_query.id)
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost FROM location WHERE type = 'Площа' LIMIT 1 OFFSET ?",
            [n_areas]):
        areas_list.append(name)

        await bot.send_photo(callback_query.from_user.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}", reply_markup=keybord.keyboard_inline_areas)
    if len(areas_list) < n_areas-1:
        await bot.send_message(callback_query.from_user.id, "На даний момент це остання локація\n"
                                                            "Ми процюємо над тим щоб їх було  більше")
        n_areas = 0
n_hotels = 0
hotels_list = []


@dp.callback_query_handler(lambda c: c.data == 'hotels')
async def hotels(callback_query: aiogram.types.CallbackQuery):
    global n_hotels, hotels_list
    n_hotels +=1
    await bot.answer_callback_query(callback_query.id)
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost FROM location WHERE type = 'Готель' LIMIT 1 OFFSET ?",
            [n_hotels]):
        hotels_list.append(name)

        await bot.send_photo(callback_query.from_user.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}", reply_markup=keybord.keyboard_inline_hotels)
    if len(hotels_list) < n_hotels-1:
        await bot.send_message(callback_query.from_user.id, "На даний момент це остання локація\n"
                                                            "Ми процюємо над тим щоб їх було  більше")
        n_hotels = 0
        hotels_list.clear()

n_museums = 0
museums_list = []


@dp.callback_query_handler(lambda c: c.data == 'museums')
async def forgotten(callback_query: aiogram.types.CallbackQuery):
    global n_museums, museums_list
    n_museums +=1
    await bot.answer_callback_query(callback_query.id)
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost FROM location WHERE type = 'Музей' LIMIT 1 OFFSET ?",
            [n_museums]):
        museums_list.append(name)

        await bot.send_photo(callback_query.from_user.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}", reply_markup=keybord.keyboard_inline_museums)
    if len(museums_list) < n_museums-1:
        await bot.send_message(callback_query.from_user.id, "На даний момент це остання локація\n"
                                                            "Ми процюємо над тим щоб їх було  більше")
        n_museums = 0
        museums_list.clear()

n_cathedrals = 0
cathedrals_list = []


@dp.callback_query_handler(lambda c: c.data == 'cathedrals')
async def cathedrals(callback_query: aiogram.types.CallbackQuery):
    global n_cathedrals, cathedrals_list
    n_cathedrals +=1
    await bot.answer_callback_query(callback_query.id)
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost FROM location WHERE type = 'Церкви, собори, монастирі' LIMIT 1 OFFSET ?",
            [n_cathedrals]):
        cathedrals_list.append(name)

        await bot.send_photo(callback_query.from_user.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}", reply_markup=keybord.keyboard_inline_cathedrals)
    if len(cathedrals_list) < n_cathedrals-1:
        await bot.send_message(callback_query.from_user.id, "На даний момент це остання локація\n"
                                                            "Ми процюємо над тим щоб їх було  більше")
        n_cathedrals = 0
        cathedrals_list.clear()

n_historical_monument = 0
historical_monument_list =[]


@dp.callback_query_handler(lambda c: c.data == 'historical_monument')
async def forgotten(callback_query: aiogram.types.CallbackQuery):
    global n_historical_monument, historical_monument_list
    n_historical_monument +=1
    await bot.answer_callback_query(callback_query.id)
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost FROM location WHERE type = 'Історична памятка' LIMIT 1 OFFSET ?",
            [n_historical_monument]):
        historical_monument_list.append(name)

        await bot.send_photo(callback_query.from_user.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}", reply_markup=keybord.keyboard_inline_historical_monument)
    if len(historical_monument_list) < n_historical_monument-1:
        await bot.send_message(callback_query.from_user.id, "На даний момент це остання локація\n"
                                                            "Ми процюємо над тим щоб їх було  більше")
        n_historical_monument = 0
        historical_monument_list.clear()

n_other = 0
other_list = []


@dp.callback_query_handler(lambda c: c.data == 'other')
async def forgotten(callback_query: aiogram.types.CallbackQuery):
    global n_other, other_list
    n_other +=1
    await bot.answer_callback_query(callback_query.id)
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost FROM location WHERE type = 'Інше' LIMIT 1 OFFSET ?",
            [n_other]):
        other_list.append(name)

        await bot.send_photo(callback_query.from_user.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}", reply_markup=keybord.keyboard_inline_other)
    if len(other_list) < n_other-1:
        await bot.send_message(callback_query.from_user.id, "На даний момент це остання локація\n"
                                                            "Ми процюємо над тим щоб їх було  більше")
        n_other = 0
        other_list.clear()