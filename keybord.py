import aiogram
import button

# Метро

button_red_branch = aiogram.types.KeyboardButton(text='Червона гілка')
button_blue_branch = aiogram.types.KeyboardButton(text='Синя гілка')
button_green_branch = aiogram.types.KeyboardButton(text='Зелена гілка')
keyboard_metro = aiogram.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_metro.add(button_green_branch).add(button_blue_branch).add(button_red_branch)

keyboard_menu = aiogram.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_menu.add(button.button_forgotten).row(button.button_nature).row(button.button_cathedrals).row(
    button.button_cafe, button.button_next)
keyboard_menu_2 = aiogram.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_menu_2.row(button.button_museums, button.button_panoramic).row(button.button_hotels, button.button_areas).row(
    button.button_back, button.button_next1)
privat = aiogram.types.InlineKeyboardButton(text="Приват24",
                                            url='https://www.privat24.ua/rd/transfer_to_card/?hash=rd%2Ftransfer_to_card%2F%7B%22from%22%3A%22%22%2C%22to%22%3A%224149499392840482%22%2C%22amt%22%3A%22100%22%2C%22ccy%22%3A%22UAH%22%7D')
mono = aiogram.types.InlineKeyboardButton(text="MONOBANK", url='https://send.monobank.ua/5buFQWbT5t')
keyboard_menu_3 = aiogram.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_menu_3.row(button.button_historical_monument, button.button_active).row(button.button_search_metro,
                                                                                 button.button_other).row(
    button.button_donat, button.button_back1)
keyboard_donat = aiogram.types.InlineKeyboardMarkup(resize_keyboard=True)
keyboard_donat.add(privat, mono)

discussion = aiogram.types.InlineKeyboardButton(text="Чат", url='https://t.me/+gSVgkrJJQaw2MDgy')
keyboard_discussion = aiogram.types.InlineKeyboardMarkup(resize_keyboard=True).add(discussion)

rd = [button.button_nature, button.button_active]

# Червона гілка
akademistechko = aiogram.types.InlineKeyboardButton(text="Академмістечко", callback_data='Академмістечко')
zhytomyr = aiogram.types.InlineKeyboardButton(text="Житомирська", callback_data='Житомирська')
svyatoshyn = aiogram.types.InlineKeyboardButton(text="Святошин", callback_data='Святошин')
nykvy = aiogram.types.InlineKeyboardButton(text="Нивки", callback_data='Нивки')
beresteyska = aiogram.types.InlineKeyboardButton(text="Берестейська", callback_data='Берестейська')
shulyavska = aiogram.types.InlineKeyboardButton(text="Шулявська", callback_data='Шулявська')
polytechnic_Institute = aiogram.types.InlineKeyboardButton(text="Політехнічний інститут",
                                                           callback_data='Політехнічний інститут')
station = aiogram.types.InlineKeyboardButton(text="Вокзальна", callback_data='Вокзальна')
university = aiogram.types.InlineKeyboardButton(text="Університет", callback_data='Університет')
theatrical = aiogram.types.InlineKeyboardButton(text="Театральна", callback_data='Театральна')
threshchatyk = aiogram.types.InlineKeyboardButton(text="Хрещатик", callback_data='Хрещатик')
arsenal = aiogram.types.InlineKeyboardButton(text="Арсенальна", callback_data='Арсенальна')
dnipro = aiogram.types.InlineKeyboardButton(text="Дніпро", callback_data='Дніпро')
hydropark = aiogram.types.InlineKeyboardButton(text="Гідропарк", callback_data='Гідропарк')
left_bank = aiogram.types.InlineKeyboardButton(text="Лівобережна", callback_data='Лівобережна')
gift = aiogram.types.InlineKeyboardButton(text="Дарниця", callback_data='Дарниця')
chernihivska = aiogram.types.InlineKeyboardButton(text="Чернігівська", callback_data='Чернігівська')
lisova = aiogram.types.InlineKeyboardButton(text="Лісова", callback_data='Лісова')
button_next_red = aiogram.types.InlineKeyboardButton(text='▶️', callback_data='Next_red_branch')
button_back_red = aiogram.types.InlineKeyboardButton(text='◀️', callback_data='Back_red_branch')
keyboard_red_branch1 = aiogram.types.InlineKeyboardMarkup(resize_keyboard=True)
keyboard_red_branch1.add(akademistechko).row(zhytomyr).row(svyatoshyn).row(nykvy).row(
    beresteyska).row(shulyavska).row(polytechnic_Institute).row(station).row(university).row(button_next_red)
keyboard_red_branch2 = aiogram.types.InlineKeyboardMarkup(resize_keyboard=True)
keyboard_red_branch2.add(theatrical).row(threshchatyk).row(arsenal).row(dnipro).row(hydropark).row(
    left_bank).row(gift).row(chernihivska).row(lisova).row(button_back_red)

# Синя гілка
heroes_of_the_Dnipro = aiogram.types.InlineKeyboardButton(text="Героїв Дніпра", callback_data='Героїв Дніпра')
minsk = aiogram.types.InlineKeyboardButton(text="Мінська", callback_data='Мінська')
obolon = aiogram.types.InlineKeyboardButton(text="Оболонь", callback_data='Оболонь')
petrivka = aiogram.types.InlineKeyboardButton(text="Петрівка", callback_data='Петрівка')
taras_Shevchenko = aiogram.types.InlineKeyboardButton(text="Тараса Шевченка", callback_data='Тараса Шевченка')
contract_area = aiogram.types.InlineKeyboardButton(text="Контрактова площа", callback_data='Контрактова площа')
postal_square = aiogram.types.InlineKeyboardButton(text="Поштова площа", callback_data='Поштова площа')
independence_Square = aiogram.types.InlineKeyboardButton(text="Майдан Незалежності",
                                                         callback_data='Майдан Незалежності')
leo_Tolstoy_Square = aiogram.types.InlineKeyboardButton(text="Площа Льва Толстого", callback_data='Площа Льва Толстого')
olympic = aiogram.types.InlineKeyboardButton(text="Олімпійська", callback_data='Олімпійська')
palace_Ukraine = aiogram.types.InlineKeyboardButton(text='Палац"Україна"', callback_data='Палац"Україна')
lybidska = aiogram.types.InlineKeyboardButton(text="Либідська", callback_data='Либідська')
demyivska = aiogram.types.InlineKeyboardButton(text="Демиївська", callback_data='Демиївська')
holosiivska = aiogram.types.InlineKeyboardButton(text="Голосіївська", callback_data='Голосіївська')
vasylkivska = aiogram.types.InlineKeyboardButton(text="Васильківська", callback_data='Васильківська')
exhibition_center = aiogram.types.InlineKeyboardButton(text="Виставочний центр", callback_data='Виставочний центр')
racetrack = aiogram.types.InlineKeyboardButton(text="Іподром", callback_data='Іподром')
teremka = aiogram.types.InlineKeyboardButton(text="Теремки", callback_data='Теремки')
button_next_blue = aiogram.types.InlineKeyboardButton(text='▶️', callback_data='Next_blue_branch')
button_back_blue = aiogram.types.InlineKeyboardButton(text='◀️', callback_data='Back_blue_branch')
keyboard_blue_branch1 = aiogram.types.InlineKeyboardMarkup(resize_keyboard=True)
keyboard_blue_branch1.add(heroes_of_the_Dnipro).row(minsk).row(obolon).row(petrivka).row(taras_Shevchenko).row(
    contract_area).row(postal_square).row(independence_Square).row(leo_Tolstoy_Square).row(button_next_blue)
keyboard_blue_branch2 = aiogram.types.InlineKeyboardMarkup(resize_keyboard=True)
keyboard_blue_branch2.add(olympic).row(palace_Ukraine).row(lybidska).row(demyivska).row(holosiivska).row(
    vasylkivska).row(
    exhibition_center).row(racetrack).row(teremka).row(button_back_blue)

# Зелена гілка
red_village = aiogram.types.InlineKeyboardButton(text="Червоний хутір", callback_data='Червоний хутір')
boryspilska = aiogram.types.InlineKeyboardButton(text="Бориспільська", callback_data='Бориспільська')
vyrlitsa = aiogram.types.InlineKeyboardButton(text="Вирлиця", callback_data='Вирлиця')
kharkivska = aiogram.types.InlineKeyboardButton(text="Харківська", callback_data='Харківська')
poznyaks = aiogram.types.InlineKeyboardButton(text="Позняки", callback_data='Позняки')
slavutych = aiogram.types.InlineKeyboardButton(text="Славутич", callback_data='Славутич')
vydubychi = aiogram.types.InlineKeyboardButton(text="Видубичі", callback_data='Видубичі')
friendship_of_peoples = aiogram.types.InlineKeyboardButton(text="Дружба народів", callback_data='Дружба народів')
klovska = aiogram.types.InlineKeyboardButton(text="Кловська", callback_data='Кловська')
pecherska = aiogram.types.InlineKeyboardButton(text="Печерська", callback_data='Печерська')
palace_of_Sports = aiogram.types.InlineKeyboardButton(text="Палац спорту", callback_data='Палац спорту')
golden_Gate = aiogram.types.InlineKeyboardButton(text="Золоті ворота", callback_data='Золоті ворота')
lukyanivska = aiogram.types.InlineKeyboardButton(text="Лук'янівська", callback_data="Лук'янівська")
dear_ones = aiogram.types.InlineKeyboardButton(text="Дорогожичі", callback_data='Дорогожичі')
raw = aiogram.types.InlineKeyboardButton(text="Сирець", callback_data='Сирець')
button_next_green = aiogram.types.InlineKeyboardButton(text='▶️', callback_data='Next_green_branch')
button_back_green = aiogram.types.InlineKeyboardButton(text='◀️', callback_data='Back_green_branch')
keyboard_green_branch1 = aiogram.types.InlineKeyboardMarkup(resize_keyboard=True)
keyboard_green_branch1.add(red_village).row(boryspilska).row(vyrlitsa).row(kharkivska).row(
    poznyaks).row(slavutych).row(vydubychi).row(button_next_green)
keyboard_green_branch2 = aiogram.types.InlineKeyboardMarkup(resize_keyboard=True)
keyboard_green_branch2.add(friendship_of_peoples).row(klovska).row(pecherska).row(palace_of_Sports).row(
    golden_Gate).row(
    lukyanivska).row(dear_ones).row(raw).row(button_back_green)

button_inline_forgotten = aiogram.types.InlineKeyboardButton(callback_data='forgotten_place', text="Далі")
keyboard_inline_forgotten = aiogram.types.InlineKeyboardMarkup(resize_keyboard=True).add(button_inline_forgotten)
button_inline_cafe = aiogram.types.InlineKeyboardButton(callback_data='eit', text="Далі")
keyboard_inline_cafe = aiogram.types.InlineKeyboardMarkup(resize_keyboard=True).add(button_inline_cafe)
button_inline_nature = aiogram.types.InlineKeyboardButton(callback_data='nature', text='Далі')
keyboard_inline_nature = aiogram.types.InlineKeyboardMarkup(resize_keyboard=True).add(button_inline_nature)
button_inline_active = aiogram.types.InlineKeyboardButton(callback_data='active', text='Далі')
keyboard_inline_active = aiogram.types.InlineKeyboardMarkup(resize_keyboard=True).add(button_inline_active)
button_inline_panoramic = aiogram.types.InlineKeyboardButton(callback_data='panoramic', text='Далі')
keyboard_inline_panoramic = aiogram.types.InlineKeyboardMarkup(resize_keyboard=True).add(button_inline_panoramic)
button_inline_areas = aiogram.types.InlineKeyboardButton(callback_data='areas', text='Далі')
keyboard_inline_areas = aiogram.types.InlineKeyboardMarkup(resize_keyboard=True).add(button_inline_areas)
button_inline_hotels = aiogram.types.InlineKeyboardButton(callback_data='hotels', text='Далі')
keyboard_inline_hotels = aiogram.types.InlineKeyboardMarkup(resize_keyboard=True).add(button_inline_hotels)
button_inline_museums = aiogram.types.InlineKeyboardButton(callback_data='museums', text='Далі')
keyboard_inline_museums = aiogram.types.InlineKeyboardMarkup(resize_keyboard=True).add(button_inline_museums)
button_inline_cathedrals = aiogram.types.InlineKeyboardButton(callback_data='church', text='Далі')
keyboard_inline_cathedrals = aiogram.types.InlineKeyboardMarkup(resize_keyboard=True).add(button_inline_cathedrals)
button_inline_historical_monument = aiogram.types.InlineKeyboardButton(callback_data='historical_monument', text="Далі")
keyboard_inline_historical_monument = aiogram.types.InlineKeyboardMarkup(resize_keyboard=True).add(
    button_inline_historical_monument)
button_inline_other = aiogram.types.InlineKeyboardButton(callback_data='other', text='Далі')
keyboard_inline_other = aiogram.types.InlineKeyboardMarkup(resize_keyboard=True).add(button_inline_other)

loc_keybord = {'forgotten_place': keyboard_inline_forgotten,
               'eat': keyboard_inline_cafe,
               'nature': keyboard_inline_nature,
               'active': keyboard_inline_active,
               'hotels': keyboard_inline_hotels,
               'areas': keyboard_inline_areas,
               'museums': keyboard_inline_museums,
               'panoramic': keyboard_inline_panoramic,
               'church': keyboard_inline_cathedrals,
               'sights': keyboard_inline_historical_monument,
               'other': keyboard_inline_other
               }
