import aiogram
from main import bot, dp

#Кнопка почали
keyboard_start = aiogram.types.InlineKeyboardMarkup(resize_keyboard=True)
button_3 = aiogram.types.InlineKeyboardButton(text="Почали", callback_data='Start')
keyboard_start.add(button_3)

#Кнопка меню
button_forgotten = aiogram.types.KeyboardButton(text="Забуті місця Києва")
button_cafe = aiogram.types.KeyboardButton(text="Кафе")
button_nature = aiogram.types.KeyboardButton(text='Відпочинок на природі')
button_active = aiogram.types.KeyboardButton(text='Активний відпочинок')
keyboard_menu = aiogram.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_menu.add(button_forgotten).row(button_nature, button_active).add(button_cafe)

rd = [button_nature, button_active]

