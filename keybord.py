import aiogram
from main import bot, dp

#Кнопка меню
button_forgotten = aiogram.types.KeyboardButton(text="Забуті місця Києва")
button_cafe = aiogram.types.KeyboardButton(text="Поїсти")
button_nature = aiogram.types.KeyboardButton(text='Відпочинок на природі')
button_active = aiogram.types.KeyboardButton(text='Активний відпочинок')
button_donat = aiogram.types.KeyboardButton(text='Підтримати продукт')
button_panoramic = aiogram.types.KeyboardButton(text='Панорамний вид')
button_areas = aiogram.types.KeyboardButton(text='Площі')
button_hotels = aiogram.types.KeyboardButton(text='Готелі')
button_museums = aiogram.types.KeyboardButton(text='Музеї')
button_next = aiogram.types.KeyboardButton(text='▶️')
button_back = aiogram.types.KeyboardButton(text='◀️')
keyboard_menu = aiogram.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_menu.add(button_forgotten).row(button_nature, button_active).row(button_cafe, button_next)
keyboard_menu_2 = aiogram.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_menu_2.add(button_panoramic).row(button_hotels, button_areas, button_museums).row(button_donat, button_back)
privat = aiogram.types.InlineKeyboardButton(text="Приват24", url='https://www.privat24.ua/rd/transfer_to_card/?hash=rd%2Ftransfer_to_card%2F%7B%22from%22%3A%22%22%2C%22to%22%3A%224149499392840482%22%2C%22amt%22%3A%22100%22%2C%22ccy%22%3A%22UAH%22%7D')
mono = aiogram.types.InlineKeyboardButton(text="MONOBANK", url='https://send.monobank.ua/5buFQWbT5t')

keyboard_donat = aiogram.types.InlineKeyboardMarkup(resize_keyboard=True)
keyboard_donat.add(privat, mono)



rd = [button_nature, button_active]

next = aiogram.types.InlineKeyboardButton(text="Наступне", callback_data='Next')

keyboard_next = aiogram.types.InlineKeyboardMarkup(resize_keyboard=True)
keyboard_next.add(next)


# Метро

button_red_branch = aiogram.types.KeyboardButton(text='Червона гілка')
button_blue_branch = aiogram.types.KeyboardButton(text='Синя гілка')
button_green_branch = aiogram.types.KeyboardButton(text='Зелена гілка')
keyboard_metro = aiogram.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_metro.add(button_green_branch, button_blue_branch, button_red_branch)

# Червона гілка
keyboard_red_branch = aiogram.types.InlineKeyboardMarkup(resize_keyboard=True)
keyboard_red_branch.add(next)
Station = aiogram.types.InlineKeyboardButton(text="Вокзальна", callback_data='Station')
Theatrical = aiogram.types.InlineKeyboardButton(text="Театральна", callback_data='Theatrical')
University = aiogram.types.InlineKeyboardButton(text="Університет", callback_data='University')

# Синя гілка
keyboard_button_blue_branch = aiogram.types.InlineKeyboardMarkup(resize_keyboard=True)
keyboard_button_blue_branch.add(next)


# Зелена гілка
keyboard_green_branch = aiogram.types.InlineKeyboardMarkup(resize_keyboard=True)
keyboard_green_branch.add(next)
red_village = aiogram.types.InlineKeyboardButton(text="Червоний хутір", callback_data='Red_village')
Boryspilska = aiogram.types.InlineKeyboardButton(text="Бориспільська", callback_data='Boryspilska')
Vyrlitsa = aiogram.types.InlineKeyboardButton(text="Вирлиця", callback_data='Vyrlitsa')
Kharkivska = aiogram.types.InlineKeyboardButton(text="Харківська", callback_data='Kharkivska')
Poznyaks = aiogram.types.InlineKeyboardButton(text="Позняки", callback_data='Poznyaks')
Slavutych = aiogram.types.InlineKeyboardButton(text="Славутич", callback_data='Slavutych')
Vydubychi = aiogram.types.InlineKeyboardButton(text="Видубичі", callback_data='Vydubychi')
Friendship_of_peoples = aiogram.types.InlineKeyboardButton(text="Дружба народів", callback_data='Friendship_of_peoples')
Klovska = aiogram.types.InlineKeyboardButton(text="Кловська", callback_data='Klovska')
Pecherska = aiogram.types.InlineKeyboardButton(text="Печерська", callback_data='Pecherska')
Palace_of_Sports = aiogram.types.InlineKeyboardButton(text="Палац спорту", callback_data='Palace_of_Sports')
Golden_Gate = aiogram.types.InlineKeyboardButton(text="Золоті ворота", callback_data='Golden_Gate')
Lukyanivska = aiogram.types.InlineKeyboardButton(text="Лук'янівська", callback_data='Lukyanivska')
dear_ones = aiogram.types.InlineKeyboardButton(text="Дорогожичі", callback_data='dear_ones')
raw = aiogram.types.InlineKeyboardButton(text="Сирець", callback_data='raw')




