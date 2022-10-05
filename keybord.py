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