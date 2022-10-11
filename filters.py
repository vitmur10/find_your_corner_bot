from Const import bot, storage, dp, cur, con
import aiogram


def forgotten(message: aiogram.types.Message) -> object:
    """

    :rtype: object
    """
    bot.send_message(message.chat.id, "Ось забуті місця Києва")
    for name, city, type, address, fishnet, about, photo, metro, tim, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE type = 'Забуті місця Києва'"):
        bot.send_photo(message.chat.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {tim}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}")


def cafe(message: aiogram.types.Message):
    bot.send_message(message.chat.id, 'Ось варіанти де можна поїсти')
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE type = 'Кафе'"):
        bot.send_photo(message.chat.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}")


def nature(message: aiogram.types.Message):
    """

    :rtype: object
    """
    bot.send_message(message.chat.id, "Ось варіанти відпочинку на природі")
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE type = 'Відпочинок на природі'"):
        bot.send_photo(message.chat.id, photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}")


def active(message: aiogram.types.Message):
    bot.send_message(message.chat.id, "Ось варіанти активного відпочинку")
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost    FROM location WHERE type = 'Активний відпочинок'"):
        bot.send_photo(message.chat.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}"
                             f"{fishnet}")


def hotels(message: aiogram.types.Message):
    bot.send_message(message.chat.id, 'Ось варіанти готелів')
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE type = 'Готель'"):
        bot.send_photo(message.chat.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}")


def areas(message: aiogram.types.Message):
    bot.send_message(message.chat.id, 'Ось варіанти площів')
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE type = 'Площа'"):
        bot.send_photo(message.chat.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}")


async def museums(message: aiogram.types.Message) -> object:
    bot.send_message(message.chat.id, 'Ось варіанти музеїв')
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE type = 'Музей'"):
        bot.send_photo(message.chat.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}")


def panoramic(message: aiogram.types.Message):
    bot.send_message(message.chat.id,'Ось варіанти місць із панорамним видом')
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE type = 'Панорамний вид'"):
        bot.send_photo(message.chat.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}")


def cathedrals(message: aiogram.types.Message):
    bot.send_message(message.chat.id,'Ось варіанти церквів, соборів, монастирів')
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE type = 'Церкви, собори, монастирі'"):
        bot.send_photo(message.chat.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}")


def historical_monument(message: aiogram.types.Message):
    bot.send_message(message.chat.id,"Ось варіанти історичних пам'яток")
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE type = 'Історична памятка'"):
         bot.send_photo(message.chat.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}")


def other(message: aiogram.types.Message):
    bot.send_message(message.chat.id,'Ось інші локації')
    for name, city, type, address, fishnet, about, photo, metro, time, cost in cur.execute(
            "SELECT name, city, type, address, fishnet, about, photo, metro, time, cost  FROM location WHERE type = 'Інше'"):
         bot.send_photo(message.chat.id,
                             photo,
                             f"🫧{name}\n"
                             f"{about}\n"
                             f"📍Адреса - {address}\n"
                             f"Станція метро - {metro}\n"
                             f"Години роботи {time}\n"
                             f"Вартість - {cost}\n"
                             f"{fishnet}")