from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from Const import bot, dp, cur, con
import aiogram



class Location(StatesGroup):
    name = State()
    city = State()
    type = State()
    address = State()
    fishnet = State()


@dp.message_handler(commands=['add_loc'], commands_prefix='/')
async def add_location(message: aiogram.types.Message):
    await Location.name.set()
    await message.answer("тип")


@dp.message_handler(state=Location.name)  # Принимаем состояние
async def name(message: aiogram.types.Message, state: FSMContext):
    async with state.proxy() as data:  # Устанавливаем состояние ожидания
        data['name'] = message.text
    await message.answer("Місто і тип")
    await Location.next()


@dp.message_handler(state=Location.city)
async def type(message: aiogram.types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['city'] = message.text
    await message.answer("Адрес")
    await Location.next()


@dp.message_handler(state=Location.type)
async def type(message: aiogram.types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['type'] = message.text
    await message.answer("Адрес")
    await Location.next()


@dp.message_handler(state=Location.address)
async def address(message: aiogram.types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['address'] = message.text
    await message.answer('Надішліть силку')
    await Location.next()


@dp.message_handler(state=Location.fishnet)
async def fishnet(message: aiogram.types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['fishnet'] = message.text
    await state.finish()
    print(data)
    data = [
        (Location.name, Location.city, Location.type, Location.address, Location.fishnet)
    ]
    await message.answer(data)
    cur.executemany("INSERT INTO location VALUES(?, ?, ?, ?, ?)", data)
    con.commit()
    await message.answer(
        f' Локацію {Location.name} було додано\n'
        f'Місто:{Location.city}\n'
        f'Адрес:{Location.address}\n'
        f'Силка:{Location.fishnet}')