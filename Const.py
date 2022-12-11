import aiogram
import sqlite3
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import random

TOKEN = '5708514497:AAHvojl6OwJ3gAQsQdtaN9aWTYyfVpEFRCQ'
bot = aiogram.Bot(token=TOKEN)
storage = MemoryStorage()
dp = aiogram.Dispatcher(bot, storage=storage)

con = sqlite3.connect("bd")
cur = con.cursor()


region_list = ('Київ', 'Львів', 'Хмельницький')

a = ['Відпочинь', 'Все буде добре']
b = ['У тебе дуже гарна посмішка', 'Не думай про погане', 'Все буде добре']
c = ['У тебе все вийде', 'Все буде добре']
characters = {
    'z': 'Вийди отсюда розбійник🧏🧏🧏',
    'v': 'Пиздуйте нахуй отсюда йобаниє підараси👨‍🦲👨‍🦲👨‍🦲',
    'vz': 'Пиздець російській федерації⚰️⚰️⚰️',
    'Я втомився': a[random.randrange(0, len(a))],
    'Мені сумно': b[random.randrange(0, len(b))],
    'Я більше не можу': c[random.randrange(0, len(c))],
    'Я втомилася': a[random.randrange(0, len(a))],
    'Слава Україні': 'Героям Слава'
}