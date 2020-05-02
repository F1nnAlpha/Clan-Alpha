import telebot


#___________________________________________MAIN_KEYBOARD______________________________________________________________



bot = telebot.TeleBot('1024124364:AAEN82KlmmYOKg82c4UaF1trPnH9e6U-poM')
keyboard1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard1.row('Вартість страхування')
keyboard1.row('БАЗА ПОЛІЦІЇ','ДОВІДНИК')
keyboard1.row('КОНТАКТИ')



#_____________________________________VARTIST_STRAHUVANNYA_KEYBOARD____________________________________________________


#null

keyboard0 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard0.row('UNIQA КАСКО').add('ПОВНЕ КАСКО')
keyboard0.row('МІНІ КАСКО').add('Назад')

keyboard01 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard01.row('ПЗУ').add('ОБЕРІГ')
keyboard01.row('Назад')




#first_stage

keyboard2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard2.row('АВТОЦИВІЛКА','КАСКО').add('Медичне страхування за кордон')
keyboard2.row('Назад')


#second_stage

keyboard3 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard3.row('АСКО ДС', 'VUSO').add('ІНГО','УПСК')
keyboard3.row('PZU Ukraine','ВСІ ЦІНИ')
keyboard3.row('Назад')



#vsi_zony_stage

keyboard4 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard4.row('Зона 4').add('Зона 5')
keyboard4.row('Зона 6').add('Назад')




#VUSO_stage

keyboard5 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard5.row('Фізичні особи').add('Юридичні особи')
keyboard5.row('Назад')




#asko_stage

keyboard6 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard6.row('ФІЗИЧНІ ТА ЮРИДИЧНІ ОСОБИ').add('ТАКСІ')
keyboard6.row('ДЦВ і ДЦВ+')
keyboard6.row('Назад')




#UPSK_stage

keyboard7 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard7.row('УПСК фізичні особи').add('УПСК юридичні особи')
keyboard7.row('Назад')




#medstrahZAkordonn_stage

keyboard9 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard9.row('Подача в посольство. Роботча віза').add('По БЕЗВІЗУ')
keyboard9.row('Назад')



#____________________________________DOVIDNYK_KEYBOARD_____________________________________________________




#first_main_buttons

keyboard8 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard8.row('Довідник типів ТЗ').add('МРЕВ')
keyboard8.row('Пряме врегулювання').add('Довідник зони')
keyboard8.row('ELECTROCAR').add('Назад')




#_____________________________________KONTAKTY_KEYBOARD_______________________________________________________________



keyboard10 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard10.row('BotDeveloper').add('Копаниця Антон')
keyboard10.row('Копаниця Ніна').add('Назад')








@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Бот запущенно командою /start', reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'вартість страхування':
        bot.send_message(message.chat.id, 'Клавіатура оновлена',  reply_markup=keyboard2)

    elif message.text.lower() == 'botdeveloper':
    	bot.send_message(message.chat.id, 'Telegram: @F1nnAlpha', reply_markup=keyboard10)
    	bot.send_message(message.chat.id, 'Steam: https://steamcommunity.com/id/finnalpha2281337', reply_markup=keyboard10)

    elif message.text.lower() == 'копаниця антон':
        bot.send_message(message.chat.id, 'Vodafone: +380951314527', reply_markup=keyboard10)
        bot.send_message(message.chat.id, 'Київстар: +380978309749', reply_markup=keyboard10)

    elif message.text.lower() == 'копаниця ніна':
        bot.send_message(message.chat.id, 'Київсатр: +380971122479', reply_markup=keyboard10)

    elif message.text.lower() == 'медичне страхування за кордон':
    	bot.send_message(message.chat.id, 'Оберіть потрібний варіант', reply_markup=keyboard9)

    elif message.text.lower() == 'контакти':
    	bot.send_message(message.chat.id, 'Всі контакти', reply_markup=keyboard10)

    elif message.text.lower() == 'uniqa каско':
    	bot.send_message(message.chat.id, 'Перейдіть за посиланням: https://goo.gl/Ad6L5i', reply_markup=keyboard0)

    elif message.text.lower() == 'повне каско':
    	bot.send_message(message.chat.id, 'ПОВНЕ КАСКО', reply_markup=keyboard0)

    elif message.text.lower() == 'подача в посольство. роботча віза':
    	bot.send_photo(message.chat.id, 'https://imbt.ga/RNDWzdG7b8', reply_markup=keyboard9)
    	bot.send_photo(message.chat.id, 'https://imbt.ga/HwsAYXW8b4', reply_markup=keyboard9)
    	bot.send_photo(message.chat.id, 'https://imbt.ga/5WrxQbKWHv', reply_markup=keyboard9)

    elif message.text.lower() == 'по безвізу':
    	bot.send_photo(message.chat.id, 'https://imbt.ga/DAWB7tppG7', reply_markup=keyboard9)
    	bot.send_photo(message.chat.id, 'https://imbt.ga/x2J9WvMGfZ', reply_markup=keyboard9)

    elif message.text.lower() == 'міні каско':
    	bot.send_message(message.chat.id, 'Виберіть потрібний варіант', reply_markup=keyboard01)

    elif message.text.lower() == 'пзу':
    	bot.send_photo(message.chat.id, 'https://imbt.ga/m1kdg3sHae', reply_markup=keyboard01)

    elif message.text.lower() == 'оберіг':
    	bot.send_photo(message.chat.id, 'https://imbt.ga/Jn9eSWY7XI', reply_markup=keyboard01)

    elif message.text.lower() == 'каско':
    	bot.send_message(message.chat.id, 'Виберіть потрібний варіант', reply_markup=keyboard0)

    elif message.text.lower() == 'мрев':
    	bot.send_message(message.chat.id, 'https://drive.google.com/open?id=17bqyM7rvnjpBPrApY08sKWiqT6SNLG-_', reply_markup=keyboard8)

    elif message.text.lower() == 'довідник зони':
    	bot.send_photo(message.chat.id, 'https://imbt.ga/wDiVLEeXGt', reply_markup=keyboard8)

    elif message.text.lower() == 'electrocar':
    	bot.send_photo(message.chat.id, 'https://imbt.ga/QcNljlvvwm', reply_markup=keyboard8)

    elif message.text.lower() == 'пряме врегулювання':
    	bot.send_photo(message.chat.id, 'https://imbt.ga/Zb8i5ea8eX', reply_markup=keyboard8)

    elif message.text.lower() == 'довідник типів тз':
    	bot.send_message(message.chat.id, 'https://drive.google.com/open?id=1i7Q5mihG4isiIFDqlTZRT5SyXPn0kRN4', reply_markup=keyboard8)

    elif message.text.lower() == 'база поліції':
    	bot.send_message(message.chat.id, 'Офіційна база-данних Поліції', reply_markup=keyboard1)
    	bot.send_message(message.chat.id, 'https://baza-gai.com.ua', reply_markup=keyboard1)

    elif message.text.lower() == 'довідник':
    	bot.send_message(message.chat.id, 'Оберіть потрібний варіант', reply_markup=keyboard8)

    elif message.text.lower() == 'упск':
    	bot.send_message(message.chat.id, 'Оберіть потрібний варіант', reply_markup=keyboard7)

    elif message.text.lower() == 'pzu ukraine':
    	bot.send_photo(message.chat.id, 'https://imbt.ga/vHiDzxttUH', reply_markup=keyboard3)

    elif message.text.lower() == 'упск фізичні особи':
    	bot.send_photo(message.chat.id, 'https://imbt.ga/urhLQwuESN', reply_markup=keyboard7)

    elif message.text.lower() == 'упск юридичні особи':
    	bot.send_photo(message.chat.id, 'https://imbt.ga/DL6DlxiNw6', reply_markup=keyboard7)

    elif message.text.lower() == 'фізичні та юридичні особи':
    	bot.send_photo(message.chat.id, 'https://imbt.ga/pP1ymgk7Bq', reply_markup=keyboard6)

    elif message.text.lower() == 'таксі':
    	bot.send_photo(message.chat.id, 'https://imbt.ga/dED6OmcKCT', reply_markup=keyboard6)

    elif message.text.lower() == 'дцв і дцв+':
    	bot.send_photo(message.chat.id, 'https://imbt.ga/cSKvZJlzUY', reply_markup=keyboard6)
    	bot.send_photo(message.chat.id, 'https://imbt.ga/oDqVuT9Tbl', reply_markup=keyboard6)

    elif message.text.lower() == 'аско дс':
    	bot.send_message(message.chat.id, 'Оберіть потрібний варіант', reply_markup=keyboard6)

    elif message.text.lower() == 'vuso':
    	bot.send_message(message.chat.id, 'Оберіть особу', reply_markup=keyboard5)

    elif message.text.lower() == 'фізичні особи':
    	bot.send_photo(message.chat.id, 'https://imbt.ga/JUMeDFc6Lg', reply_markup=keyboard5)

    elif message.text.lower()== 'юридичні особи':
    	bot.send_photo(message.chat.id, 'https://imbt.ga/K4kZ8ztAtn', reply_markup=keyboard5)

    elif message.text.lower() == 'інго':
    	bot.send_message(message.chat.id, 'Заборонено укладання договорів на автобуси D1, D2, ТАКСІ та пільгові категорії громадян.',  reply_markup=keyboard3)
    	bot.send_photo(message.chat.id, 'https://imbt.ga/JUMeDFc6Lg', reply_markup=keyboard3)
    	bot.send_photo(message.chat.id, 'https://imbt.ga/6flVAMQr3z', reply_markup=keyboard3)

    elif message.text.lower() == 'автоцивілка':
        bot.send_message(message.chat.id, 'Клавіатура оновлена',  reply_markup=keyboard3)

    elif message.text.lower() == 'всі ціни':
        bot.send_message(message.chat.id, 'Оберіть зону',  reply_markup=keyboard4)

    elif message.text.lower() == 'зона 4':
        bot.send_photo(message.chat.id, 'https://imbt.ga/EbdkP9vCuC',  reply_markup=keyboard4)

    elif message.text.lower() == 'зона 5':
        bot.send_photo(message.chat.id, 'https://imbt.ga/uZ1IpPDAhb',  reply_markup=keyboard4)

    elif message.text.lower() == 'зона 6':
        bot.send_photo(message.chat.id, 'https://imbt.ga/aAPpVNL0Dn',  reply_markup=keyboard4)

    elif message.text.lower() == 'назад':
        bot.send_message(message.chat.id, 'Клавіатура оновлена',  reply_markup=keyboard1)











bot.polling()