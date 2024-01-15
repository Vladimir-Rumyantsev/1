import telebot
from telebot import types


def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(content_types=['text'])
    def send_text(message):
        try:
            person = message.chat.id

            if ((message.text.lower() == '/start') or (message.text.lower() == 'привет') or
                    (message.text.lower() == 'привет!')):
                bot.send_message(
                    person,
                    f'🇷🇺\nПривет! Меня зовут "Всё по полочкам"!\n'
                    f'Я Telegram-бот для поиска мест раздельного сбора мусора или сдачи батареек в крупных городах '
                    f'Пермского края. Моя миссия - забота об экологии и совершенствование мира в нашем регионе.\n'
                    f'С помощью кнопок ниже выбери язык, на котором ты предпочитаешь получать сообщения от меня\n\n'
                    f'🇬🇧\nHi! My name is "Everything on the shelves"!\n'
                    f'I am a Telegram-bot for searching for places for separate garbage collection or battery '
                    f'collection in large cities of the Perm Region. My mission is to take care of the environment '
                    f'and improve the peace in our region.\nUse the buttons below to select the language in which you '
                    f'prefer to receive messages from me', reply_markup=language
                )

            elif message.text.lower() == '🇬🇧 english':
                bot.send_message(
                    person,
                    f"Okay, I'll use English to communicate with you\n\nTo find out the information you are "
                    f"interested in about your city, use the buttons below. And the central button will tell you "
                    f"about the important to sort your rubbish and recycle batteries", reply_markup=markup_en
                )

            elif message.text.lower() == '🇷🇺 русский':
                bot.send_message(
                    person,
                    f'Хорошо, я буду использовать русский язык для общения с тобой\n\nЧтобы узнать '
                    f'интересующую информацию о твоём городе - воспользуйся кнопками ниже. А центральная кнопка '
                    f'расскажет тебе о важности сортировки мусора и правильной утилизации батареек',
                    reply_markup=markup_ru
                )

            elif message.text.lower() == 'о важности сортировки':
                bot.send_message(
                    person,
                    f'Почему важно сортировать мусор?\nРаздельный сбор отходов позволяет решить сразу несколько '
                    f'проблем. Во-первых, благодаря этому меньше мусора захоранивают на полигонах. Старые свалки '
                    f'растут медленнее, новые открываются реже. Кроме того, разлагаясь под открытым небом на '
                    f'полигонах, вещи могут выделять ядовитые вещества в атмосферу, грунт или воду. Чем больше '
                    f'отходов перерабатывается, тем меньше подобных вредных выбросов.\nВторой аргумент в пользу '
                    f'раздельного сбора — возможность сократить потребление природных ресурсов за счет вторсырья. '
                    f'До половины (а иногда и больше) мусора составляют перерабатываемые отходы. Огромный объем '
                    f'материалов можно и нужно использовать повторно. Например, изготавливая бумагу из макулатуры, '
                    f'мы спасаем от вырубки деревья, которые идут на производство целлюлозы с нуля.\n\n'
                    f'Почему важно сдавать батарейки?\nОтработанные батарейки трансформируются в опасные токсичные '
                    f'отходы. Вещества, которые в них содержатся, отравляют землю, воду и воздух. Одна брошенная на '
                    f'землю батарейка – это химическое загрязнение до 20 м² почвы. А если она попадет в огонь, то '
                    f'выделяются еще более токсичные вещества, опасные для людей. Всего этого удастся избежать, если '
                    f'утилизировать элементы питания правильно. Так же в ходе утилизации извлекают цветные металлы и '
                    f'другие вещества, у которых нет никаких отличий от тех, что добываются из природных '
                    f'месторождений.', reply_markup=markup_ru
                )

            elif message.text.lower() == 'the importance of sorting':
                bot.send_message(
                    person,
                    f'Why is it so important to sort your rubbish?\nSeparate waste collection solves several '
                    f'problems at once. Firstly, thanks to it, less rubbish is buried in landfills. Old landfills '
                    f'grow slower and new ones are opened less often. In addition, decomposing in the open air in '
                    f'landfills, things can release toxic substances into the atmosphere, soil or water. The more '
                    f'waste is recycled, the less such harmful emissions.\nThe second argument in favour of separate '
                    f'collection is the possibility to reduce the consumption of natural resources through recycled '
                    f'materials. Up to half (and sometimes more) of rubbish is recyclable waste. A huge amount of '
                    f'materials can and should be reused. For example, by making paper from waste paper, we save trees '
                    f'from being cut down, which are used for pulp production from scratch.\n\n'
                    f'Why is it important to recycle batteries?\nUsed batteries become hazardous toxic waste. The '
                    f'substances they contain poison the land, water and air. One battery thrown on the ground is a '
                    f'chemical contamination of up to 20 m² of soil. And if it gets into a fire, it releases even more '
                    f'toxic substances that are dangerous for people. All this can be avoided if the batteries are '
                    f'disposed of correctly. Non-ferrous metals and other substances are also recovered during '
                    f'disposal, which are no different from those extracted from natural deposits.',
                    reply_markup=markup_en
                )

            elif message.text.lower() == 'пермь':
                bot.send_message(
                    person,
                    f'В Перми можно раздельно сдать мусор по адресам:\n'
                    f'• ул. Строителей, 12 (Дзержинский район)\n'
                    f'• ул. Свиязева, 58 (Индустриальный район)\n'
                    f'• ул. Буксирная, 6 (Кировский район)\n'
                    f'• ул. Нейвинская, 14 (Свердловский район)\n'
                    f'• ул. Целинная, 31/3 (Мотовилихинский район)\n\n'
                    f'А батарейки по адресам:\n'
                    f'• ул. Лянгасова, 139/1\n'
                    f'• ул. Подлесная, 43Б, этаж 1, магазин Эльдорадо\n'
                    f'• ул. Братская, 137А\n'
                    f'• ул. Уинская, 15А, этаж 2, магазин М.Видео\n'
                    f'• ул.1905 года, 4А, эт. 1\n'
                    f'• шос. Космонавтов, дом 393, Metro Cash & Carry\n'
                    f'• ул. Мира, 41/1, Столица, магазин М.Видео'
                )

            elif message.text.lower() == 'березники':
                bot.send_message(
                    person,
                    f'В Березниках можно раздельно сдать мусор по адресам:\n'
                    f'• ул. Льва Толстого, 100\n'
                    f'• ул. Пятилетки, 35\n'
                    f'• ул. Загородная, 1\n\n'
                    f'А батарейки по адресам:\n'
                    f'• ул. Олега Кошевого, 9а\n'
                    f'• ул. Карла Маркса, 53, в магазине «Hi-Fi звук»\n'
                    f'• ул. Ломоносова, 113, во Дворце спорта «Темп»\n'
                    f'• ул. Веры Бирюковой, 9, в Центре детского (юношеского) научно-технического творчества'
                )

            elif message.text.lower() == 'соликамск':
                bot.send_message(
                    person,
                    f'В Соликамске раздельно сдать мусор можно только по адресу:\n• Юбилейный просп., 10\n\n'
                    f'А батарейки по адресам:\n'
                    f'• ул. Урицкого,42, в будни в рабочее время в ДЭБЦ\n'
                    f'• ул. 20-лет Победы, 121, 3 этаж, в отдел по экологии\n'
                    f'• ул. Советская, 56/4, 20 кабинет, в редакцию газеты «Наш Соликамск»'
                )

            elif message.text.lower() == 'чайковский':
                bot.send_message(
                    person,
                    f'В Чайковском раздельно сдать мусор можно только по адресу:\n• ул. Азина, 11\n\n'
                    f'А батарейки по адресам:\n'
                    f'• ул. Промышленная 4\n'
                    f'• ул. Советская, 1/13'
                )

            elif message.text.lower() == 'кунгур':
                bot.send_message(
                    person,
                    f'В Кунгуре раздельно сдать мусор можно только по адресу:\n• ул. Нефтяников, 2\n\n'
                    f'А батарейки по адресам:\n'
                    f'• ул. Пролетарская, 112А\n'
                    f'• ул. Полетаевская ул., 26'
                )

            elif message.text.lower() == 'лысьва':
                bot.send_message(
                    person,
                    f'В Лысьве можно раздельно сдать мусор по адресам:\n'
                    f'• ул. Кошевого, 7\n'
                    f'• ул. Смышляева, 40А\n'
                    f'• ул. Суворова, 7\n\n'
                    f'А батарейки по адресам:\n'
                    f'• ул. Революции, 27\n'
                    f'• ул. Лермонтова, 93Б\n'
                    f'• ул. Лермонтова, 93В\n'
                    f'• ул. Пожарского, 12А'
                )

            elif message.text.lower() == 'краснокамск':
                bot.send_message(
                    person,
                    f'В Краснокамске можно раздельно сдать мусор по адресам:\n'
                    f'• ул. Сосновая Горка, 3/2\n'
                    f'• ул. Коммунистическая, 23, корп. 2\n'
                    f'• просп. Мира, 6\n\n'
                    f'А батарейки по адресам:\n'
                    f'• ул. Коммунистическая, 23, корп. 2\n'
                    f'• ул. Сосновая Горка, 3/2\n'
                    f'• ул. Геофизиков, 1Б\n'
                    f'• ул. Шоссейная, 31\n'
                    f'• ул. Коммунистическая, 42\n'
                    f'• Дорожный пер., 2\n'
                    f'• ул. Промышленная, 13\n'
                    f'• ул. Карла Маркса, 4/1\n'
                    f'• ул. Энергетиков, 43'
                )

            elif message.text.lower() == 'чусовой':
                bot.send_message(
                    person,
                    f'В Чусовом раздельно сдать мусор можно только по адресу:\n• ул. Чайковского, 23\n\n'
                    f'А батарейки по адресам:\n'
                    f'• ул. Юности, 1\n'
                    f'• ул. Южная, 7'
                )

            elif message.text.lower() == 'perm':
                bot.send_message(
                    person,
                    f'In Perm, you can separately hand over garbage at the following addresses:\n'
                    f'• 12 Stroiteley str. (Dzerzhinsky district)\n'
                    f'• 58 Sviyazeva str. (Industrial district)\n'
                    f'• 6 Bugsirnaya str. (Kirovsky district)\n'
                    f'• 14 Neivinskaya str. (Sverdlovsk district)\n'
                    f'• 31/3 Tselinnaya str. (Motovilikhinsky district)\n\n'
                    f'And the batteries are at the addresses:\n'
                    f'• 139/1 Lyangasova str.\n'
                    f'• 43B Podlesnaya str., floor 1, Eldorado store\n'
                    f'• 137A Bratskaya str.\n'
                    f'• 15A Uinskaya str., floor 2, M.Video store\n'
                    f'• 4A 1905 str., floor 1\n'
                    f'• 393 Kosmonavtov Highway, Metro Cash & Carry\n'
                    f'• 41/1 Mira str., Stolitsa shopping mall, M.Video store'
                )

            elif message.text.lower() == 'berezniki':
                bot.send_message(
                    person,
                    f'In Berezniki, you can separately hand over garbage at the following addresses:\n'
                    f'• 100 Lva Tolstogo str.\n'
                    f'• 35 Pyatiletki str.\n'
                    f'• 1 Zagorodnaya str.\n\n'
                    f'And the batteries are at the addresses:\n'
                    f'• 9a Oleg Koshevoy str.\n'
                    f'• 53 Karl Marx str., in the Hi-Fi sound store\n'
                    f'• 113 Lomonosov str., at the Temp Sports Palace\n'
                    f"• 9 Vera Biryukova str., at the Center for Children's (Youth) Scientific and Technical Creativity"
                )

            elif message.text.lower() == 'solikamsk':
                bot.send_message(
                    person,
                    f'In Solikamsk, it is possible to hand over garbage separately only at the address:\n'
                    f'• 10 Jubilee Ave.\n\n'
                    f'And the batteries are at the addresses:\n'
                    f'• 42 Uritskogo str., on weekdays during business hours\n'
                    f'• 121, 20th Anniversary of Victory str., 3rd floor, to the Department of Ecology\n'
                    f'• 56/4 Sovetskaya str., 20 office, to the editorial office of the newspaper "Nash Solikamsk"'
                )

            elif message.text.lower() == 'chaikovsky':
                bot.send_message(
                    person,
                    f'In Chaikovsky, it is possible to hand over garbage separately only at the address:\n'
                    f'• 11 Azina str.\n\n'
                    f'And the batteries are at the addresses:\n'
                    f'• 4 Promyshlennaya str.\n'
                    f'• 1/13 Sovetskaya str.'
                )

            elif message.text.lower() == 'kungur':
                bot.send_message(
                    person,
                    f'In Kungur, it is possible to hand over garbage separately only at the address:\n'
                    f'• 2 Neftyanikov str.\n\n'
                    f'And the batteries are at the addresses:\n'
                    f'• 112A Proletarskaya str.\n'
                    f'• 26 Poletaevskaya str.'
                )

            elif message.text.lower() == 'lysva':
                bot.send_message(
                    person,
                    f'In Lysva, you can separately hand over garbage at the following addresses:\n'
                    f'• 7 Koshevoy str.\n'
                    f'• 40A Smyshlyaev str.\n'
                    f'• 7 Suvorov str.\n\n'
                    f'And the batteries are at the addresses:\n'
                    f'• 27 Revolyutsii str.\n'
                    f'• 93B Lermontov str.\n'
                    f'• 93C Lermontov str.\n'
                    f'• 12A Pozharsky str.'
                )

            elif message.text.lower() == 'krasnokamsk':
                bot.send_message(
                    person,
                    f'In Krasnokamsk, you can separately hand over garbage at the following addresses:\n'
                    f'• 3/2 Sosnovaya Gorka str.\n'
                    f'• 23 Kommunisticheskaya str., building 2\n'
                    f'• 6 avenue Mira\n\n'
                    f'And the batteries are at the addresses:\n'
                    f'• 23 Kommunisticheskaya str., building 2\n'
                    f'• 3/2 Sosnovaya Gorka str.\n'
                    f'• 1B Geophysicists str.\n'
                    f'• 31 Shosseynaya str.\n'
                    f'• 42 Kommunisticheskaya str.\n'
                    f'• 2 Dorozhny lane\n'
                    f'• 13 Promyshlennaya str.\n'
                    f'• 4/1 Karl Marx str.\n'
                    f'• 43 Energetikov str.'
                )

            elif message.text.lower() == 'chusovoy':
                bot.send_message(
                    person,
                    f'In Chusovoye, you can hand over garbage separately only at the address:\n'
                    f'• 23 Tchaikovsky str.\n\n'
                    f'And the batteries are at the addresses:\n'
                    f'• 1 Yunosti str.\n'
                    f'• 7 Yuzhnaya str.'
                )

            else:
                bot.send_message(
                    person,
                    f'🇷🇺 Извините, но я вас не понял\nСделаю вид, будто вы ввели команду /start\n'
                    f'Привет! Меня зовут "Всё по полочкам"!\n'
                    f'Я Telegram-бот для поиска мест раздельного сбора мусора или сдачи батареек в крупных городах '
                    f'Пермского края. Моя миссия - забота об экологии и совершенствование мира в нашем регионе.\n'
                    f'С помощью кнопок ниже выбери язык, на котором ты предпочитаешь получать сообщения от меня\n\n'
                    f"🇬🇧 I'm sorry, but I didn't understand you\nI'll pretend that you entered the /start command\n"
                    f'Hi! My name is "Everything on the shelves"!\n'
                    f'I am a Telegram-bot for searching for places for separate garbage collection or battery '
                    f'collection in large cities of the Perm Region. My mission is to take care of the environment '
                    f'and improve the peace in our region.\nUse the buttons below to select the language in which you '
                    f'prefer to receive messages from me', reply_markup=language
                )

        except Exception as ex:
            print(ex)

    bot.polling()


language = types.ReplyKeyboardMarkup(resize_keyboard=True)
Eng = types.KeyboardButton('🇬🇧 English')
Rus = types.KeyboardButton('🇷🇺 Русский')
language.add(Eng, Rus)

markup_ru = types.ReplyKeyboardMarkup(resize_keyboard=True)
Ru_why = types.KeyboardButton('О важности сортировки')
Perm_ru = types.KeyboardButton('Пермь')
Berezniki_ru = types.KeyboardButton('Березники')
Solikamsk_ru = types.KeyboardButton('Соликамск')
Chaikovsky_ru = types.KeyboardButton('Чайковский')
Kungur_ru = types.KeyboardButton('Кунгур')
Lysva_ru = types.KeyboardButton('Лысьва')
Krasnokamsk_ru = types.KeyboardButton('Краснокамск')
Chusovoy_ru = types.KeyboardButton('Чусовой')
markup_ru.add(Perm_ru, Berezniki_ru, Solikamsk_ru, Chaikovsky_ru, Ru_why, Kungur_ru, Lysva_ru, Krasnokamsk_ru,
              Chusovoy_ru)

markup_en = types.ReplyKeyboardMarkup(resize_keyboard=True)
En_why = types.KeyboardButton('The importance of sorting')
Perm_en = types.KeyboardButton('Perm')
Berezniki_en = types.KeyboardButton('Berezniki')
Solikamsk_en = types.KeyboardButton('Solikamsk')
Chaikovsky_en = types.KeyboardButton('Chaikovsky')
Kungur_en = types.KeyboardButton('Kungur')
Lysva_en = types.KeyboardButton('Lysva')
Krasnokamsk_en = types.KeyboardButton('Krasnokamsk')
Chusovoy_en = types.KeyboardButton('Chusovoy')
markup_en.add(Perm_en, Berezniki_en, Solikamsk_en, Chaikovsky_en, En_why, Kungur_en, Lysva_en, Krasnokamsk_en,
              Chusovoy_en)

while True:
    try:
        print('Start')
        telegram_bot('token')
    except:
        print('Not internet connection!')
