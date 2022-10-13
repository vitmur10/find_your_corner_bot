import aiogram
from main import bot, dp




# Метро

button_red_branch = aiogram.types.KeyboardButton(text='Червона гілка')
button_blue_branch = aiogram.types.KeyboardButton(text='Синя гілка')
button_green_branch = aiogram.types.KeyboardButton(text='Зелена гілка')
button_menu = aiogram.types.KeyboardButton(text='Меню')
keyboard_metro = aiogram.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_metro.add(button_green_branch, button_blue_branch).add(button_menu, button_red_branch)
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
button_cathedrals = aiogram.types.KeyboardButton(text='Церкви, собори, монастирі')
button_historical_monument = aiogram.types.KeyboardButton(text="Історичні пам'ятки")
button_other = aiogram.types.KeyboardButton(text='Інше')
button_search_metro = aiogram.types.KeyboardButton(text='Пошук по метро')
button_next = aiogram.types.KeyboardButton(text='▶️')
button_back = aiogram.types.KeyboardButton(text='◀️')
keyboard_menu = aiogram.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_menu.add(button_forgotten).row(button_nature).row(button_cathedrals).row(button_historical_monument, button_active).row(button_cafe, button_next)
keyboard_menu_2 = aiogram.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_menu_2.add(button_panoramic).row(button_hotels, button_areas).row(button_other, button_museums).row(button_search_metro).row(button_donat, button_back)
privat = aiogram.types.InlineKeyboardButton(text="Приват24", url='https://www.privat24.ua/rd/transfer_to_card/?hash=rd%2Ftransfer_to_card%2F%7B%22from%22%3A%22%22%2C%22to%22%3A%224149499392840482%22%2C%22amt%22%3A%22100%22%2C%22ccy%22%3A%22UAH%22%7D')
mono = aiogram.types.InlineKeyboardButton(text="MONOBANK", url='https://send.monobank.ua/5buFQWbT5t')

keyboard_donat = aiogram.types.InlineKeyboardMarkup(resize_keyboard=True)
keyboard_donat.add(privat, mono)



rd = [button_nature, button_active]

next = aiogram.types.InlineKeyboardButton(text="Наступне", callback_data='Next')

keyboard_next = aiogram.types.InlineKeyboardMarkup(resize_keyboard=True)
keyboard_next.add(next)




# Червона гілка
akademistechko = aiogram.types.InlineKeyboardButton(text="Академмістечко", callback_data='Akademistechko')
zhytomyr = aiogram.types.InlineKeyboardButton(text="Житомирська", callback_data='Zhytomyr')
svyatoshyn = aiogram.types.InlineKeyboardButton(text="Святошин", callback_data='Svyatoshyn')
nykvy = aiogram.types.InlineKeyboardButton(text="Нивки", callback_data='Nykvy')
beresteyska = aiogram.types.InlineKeyboardButton(text="Берестейська", callback_data='Beresteyska')
shulyavska = aiogram.types.InlineKeyboardButton(text="Шулявська", callback_data='Shulyavska')
polytechnic_Institute = aiogram.types.InlineKeyboardButton(text="Політехнічний інститут", callback_data='Polytechnic_Institute')
station = aiogram.types.InlineKeyboardButton(text="Вокзальна", callback_data='Station')
university = aiogram.types.InlineKeyboardButton(text="Університет", callback_data='University')
theatrical = aiogram.types.InlineKeyboardButton(text="Театральна", callback_data='Theatrical')
threshchatyk = aiogram.types.InlineKeyboardButton(text="Хрещатик", callback_data='Khreshchatyk')
arsenal = aiogram.types.InlineKeyboardButton(text="Арсенальна", callback_data='Arsenal')
dnipro = aiogram.types.InlineKeyboardButton(text="Дніпро", callback_data='Dnipro')
hydropark = aiogram.types.InlineKeyboardButton(text="Гідропарк", callback_data='Hydropark')
left_bank = aiogram.types.InlineKeyboardButton(text="Лівобережна", callback_data='Left_bank')
gift = aiogram.types.InlineKeyboardButton(text="Дарниця", callback_data='Gift')
chernihivska = aiogram.types.InlineKeyboardButton(text="Чернігівська", callback_data='Chernihivska')
lisova = aiogram.types.InlineKeyboardButton(text="Лісова", callback_data='Lisova')
button_next_red = aiogram.types.InlineKeyboardButton(text='▶️', callback_data='Next_red_branch')
button_back_red = aiogram.types.InlineKeyboardButton(text='◀️', callback_data='Back_red_branch')
keyboard_red_branch1 = aiogram.types.InlineKeyboardMarkup(resize_keyboard=True)
keyboard_red_branch1.add(akademistechko).row(zhytomyr).row(svyatoshyn).row(nykvy).row(
    beresteyska).row(shulyavska).row(polytechnic_Institute).row(station).row(university).row(button_next_red)
keyboard_red_branch2 = aiogram.types.InlineKeyboardMarkup(resize_keyboard=True)
keyboard_red_branch2.add(theatrical).row(threshchatyk).row(arsenal).row(dnipro).row(hydropark).row(
    left_bank).row(gift).row(chernihivska).row(lisova).row(button_back_red)





# Синя гілка
heroes_of_the_Dnipro = aiogram.types.InlineKeyboardButton(text="Героїв Дніпра", callback_data='Heroes_of_the_Dnipro')
minsk = aiogram.types.InlineKeyboardButton(text="Мінська", callback_data='Minsk')
obolon = aiogram.types.InlineKeyboardButton(text="Оболонь", callback_data='Obolon')
petrivka = aiogram.types.InlineKeyboardButton(text="Петрівка", callback_data='Petrivka')
taras_Shevchenko = aiogram.types.InlineKeyboardButton(text="Тараса Шевченка", callback_data='Taras_Shevchenko')
contract_area = aiogram.types.InlineKeyboardButton(text="Контрактова площа", callback_data='Contract_area')
postal_square = aiogram.types.InlineKeyboardButton(text="Поштова площа", callback_data='Postal_square')
independence_Square = aiogram.types.InlineKeyboardButton(text="Майдан Незалежності", callback_data='Independence_Square')
leo_Tolstoy_Square = aiogram.types.InlineKeyboardButton(text="Площа Льва Толстого", callback_data='Leo_Tolstoy_Square')
olympic = aiogram.types.InlineKeyboardButton(text="Олімпійська", callback_data='Olympic')
palace_Ukraine = aiogram.types.InlineKeyboardButton(text='Палац"Україна"', callback_data='Palace_Ukraine')
lybidska = aiogram.types.InlineKeyboardButton(text="Либідська", callback_data='Lybidska')
demyivska = aiogram.types.InlineKeyboardButton(text="Демиївська", callback_data='Demyivska')
holosiivska = aiogram.types.InlineKeyboardButton(text="Голосіївська", callback_data='Holosiivska')
vasylkivska = aiogram.types.InlineKeyboardButton(text="Васильківська", callback_data='Vasylkivska')
exhibition_center = aiogram.types.InlineKeyboardButton(text="Виставочний центр", callback_data='Exhibition_center')
racetrack = aiogram.types.InlineKeyboardButton(text="Іподром", callback_data='Racetrack')
teremka = aiogram.types.InlineKeyboardButton(text="Теремки", callback_data='Teremka')
button_next_blue = aiogram.types.InlineKeyboardButton(text='▶️', callback_data='Next_blue_branch')
button_back_blue = aiogram.types.InlineKeyboardButton(text='◀️', callback_data='Back_blue_branch')
keyboard_blue_branch1 = aiogram.types.InlineKeyboardMarkup(resize_keyboard=True)
keyboard_blue_branch1.add(heroes_of_the_Dnipro).row(minsk).row(obolon).row(petrivka).row(taras_Shevchenko).row(
    contract_area).row(postal_square).row(independence_Square).row(leo_Tolstoy_Square).row(button_next_blue)
keyboard_blue_branch2 = aiogram.types.InlineKeyboardMarkup(resize_keyboard=True)
keyboard_blue_branch2.add(olympic).row(palace_Ukraine).row(lybidska).row(demyivska).row(holosiivska).row(vasylkivska).row(
    exhibition_center).row(racetrack).row(teremka).row(button_back_blue)


# Зелена гілка
red_village = aiogram.types.InlineKeyboardButton(text="Червоний хутір", callback_data='Red_village')
boryspilska = aiogram.types.InlineKeyboardButton(text="Бориспільська", callback_data='Boryspilska')
vyrlitsa = aiogram.types.InlineKeyboardButton(text="Вирлиця", callback_data='Vyrlitsa')
kharkivska = aiogram.types.InlineKeyboardButton(text="Харківська", callback_data='Kharkivska')
poznyaks = aiogram.types.InlineKeyboardButton(text="Позняки", callback_data='Poznyaks')
slavutych = aiogram.types.InlineKeyboardButton(text="Славутич", callback_data='Slavutych')
vydubychi = aiogram.types.InlineKeyboardButton(text="Видубичі", callback_data='Vydubychi')
friendship_of_peoples = aiogram.types.InlineKeyboardButton(text="Дружба народів", callback_data='Friendship_of_peoples')
klovska = aiogram.types.InlineKeyboardButton(text="Кловська", callback_data='Klovska')
pecherska = aiogram.types.InlineKeyboardButton(text="Печерська", callback_data='Pecherska')
palace_of_Sports = aiogram.types.InlineKeyboardButton(text="Палац спорту", callback_data='Palace_of_Sports')
golden_Gate = aiogram.types.InlineKeyboardButton(text="Золоті ворота", callback_data='Golden_Gate')
lukyanivska = aiogram.types.InlineKeyboardButton(text="Лук'янівська", callback_data='Lukyanivska')
dear_ones = aiogram.types.InlineKeyboardButton(text="Дорогожичі", callback_data='dear_ones')
raw = aiogram.types.InlineKeyboardButton(text="Сирець", callback_data='raw')
button_next_green = aiogram.types.InlineKeyboardButton(text='▶️', callback_data='Next_green_branch')
button_back_green = aiogram.types.InlineKeyboardButton(text='◀️', callback_data='Back_green_branch')
keyboard_green_branch1 = aiogram.types.InlineKeyboardMarkup(resize_keyboard=True)
keyboard_green_branch1.add(red_village).row(boryspilska).row(vyrlitsa).row(kharkivska).row(
    poznyaks).row(slavutych).row(vydubychi).row(button_next_green)
keyboard_green_branch2 = aiogram.types.InlineKeyboardMarkup(resize_keyboard=True)
keyboard_green_branch2.add(friendship_of_peoples).row(klovska).row(pecherska).row(palace_of_Sports).row(golden_Gate).row(
    lukyanivska).row(dear_ones).row(raw).row(button_back_green)




