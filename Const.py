import aiogram
import sqlite3
from aiogram.contrib.fsm_storage.memory import MemoryStorage


TOKEN = '5708514497:AAHvojl6OwJ3gAQsQdtaN9aWTYyfVpEFRCQ'
bot = aiogram.Bot(token=TOKEN)
storage = MemoryStorage()
dp = aiogram.Dispatcher(bot, storage=storage)

con = sqlite3.connect("bd")
cur = con.cursor()



