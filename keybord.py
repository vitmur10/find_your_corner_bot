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
keyboard_menu = aiogram.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_menu.add(button_forgotten).row(button_nature, button_active, button_museums, button_hotels, button_panoramic, button_areas, button_donat ).add(button_cafe)

rd = [button_nature, button_active]

next = aiogram.types.InlineKeyboardButton(text="Наступне", callback_data='Next')

keyboard_next = aiogram.types.InlineKeyboardMarkup(resize_keyboard=True)
keyboard_next.add(next)