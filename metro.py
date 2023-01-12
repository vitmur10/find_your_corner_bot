import aiogram


import keybord
from Const import bot, dp, cur


@dp.callback_query_handler(lambda c: True)
async def independence_square(callback_query: aiogram.types.CallbackQuery):
    if callback_query.data == 'Next_red_branch':
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, 'Червона гілка',
                               reply_markup=keybord.keyboard_red_branch2)

    elif callback_query.data == 'Back_red_branch':
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, 'Червона гілка',
                               reply_markup=keybord.keyboard_red_branch1)

    elif callback_query.data == 'Next_blue_branch':
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, 'Синя гілка',
                               reply_markup=keybord.keyboard_blue_branch2)

    elif callback_query.data == 'Back_blue_branch':
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, 'Синя гілка',
                               reply_markup=keybord.keyboard_blue_branch1)

    elif callback_query.data == 'Next_green_branch':
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, 'Зелена гілка',
                               reply_markup=keybord.keyboard_green_branch2)

    elif callback_query.data == 'Back_green_branch':
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, 'Зелена гілка',
                               reply_markup=keybord.keyboard_green_branch1)
    else:
        await bot.answer_callback_query(callback_query.id)
        print(callback_query.data)
        for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
                "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE metro = ?",
                [callback_query.data]):
            await bot.send_photo(callback_query.from_user.id,
                                 photo,
                                 f"🫧{name}\n"
                                 f"{about}\n"
                                 f"📍Адреса - {address}\n"
                                 f"Станція метро - {metro}\n"
                                 f"Години роботи {time}\n"
                                 f"Вартість - {cost}\n"
                                 f"{fishnet}")
