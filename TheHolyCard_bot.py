import telebot
import random


def telegram_bot(token):
    bot = telebot.TeleBot(token)


    @bot.message_handler(content_types=['text'])
    def send_text(message):
        def card(a):
            bot.send_message(
                person,
                f'{dict[a]}'
            )
            bot.send_message(
                947467861,
                f'Была команда /{a} от: {person}'
            )

        try:
            person = message.chat.id

            if message.text.lower() == '/start':
                bot.send_message(
                    person,
                    f"Привет! Меня зовут Как карта ляжет! "
                    f"А легла она сегодня явно благосклонно к тебе, раз ты осмелился(ась) написать мне)))"
                    f"\n"
                    f"\nЯ профессиональный таролог; могу разглядеть судьбу любого во тьме вселенной, "
                    f"для того чтобы узнать свою сегодняшнюю судьбу тебе нужно лишь выполнить эту команду —> /card"
                    f"\n"
                    f'\nА вообще, это не всё на что я способен. Команда /exam поможет тебе узнать, получишь ли ты '
                    f'сегодня зачёт по экзамену, что тебя ждёт. А при помощи команд ниже ты можешь узнать значение '
                    f"каждой карты Таро, которая тебя интересует (ну как каждой, только десяти, дальше разрабу "
                    f"было лень, но и этих карт мне хватит чтобы сделать точное предсказание):"
                    f"\n/The_Fool"
                    f"\n/The_Magician"
                    f"\n/The_Empress"
                    f"\n/The_Emperor"
                    f"\n/The_Hierophant"
                    f'\n/The_Lovers'
                    f'\n/The_Fortune'
                    f'\n/The_Hanged_Man'
                    f'\n/The_Death'
                    f'\n/The_Devil'
                    f"\n"
                    f"\n❗ Более того, если я увижу незнакомое мне сообщение, то я его незамедлительно передам "
                    f"разработчику. Через меня от передаст вам свой ответ по мере своей загруженности"
                    f"\n"
                    f"\nКхм, кхм, и вот ещё что... Не мог бы ты поддержать разработчика копеечкой? 👉👈"
                    f" Он у меня голодает периодически("
                    f"\nОтправить можно на карту Сбер:"
                    f"\n2202203292922111"
                    f"\nИли Тинькофф:"
                    f"\n5536913999164045"
                )
                bot.send_message(
                    person,
                    f'🔮'
                )
                bot.send_message(
                    947467861,
                    f'Была команда /start от: {person}'
                )

            elif message.text.lower() == '/card':
                card_random = random.randint(1, 10)
                bot.send_message(
                    person,
                    f"Выпала карта: {dict[card_random]}"
                )
                bot.send_message(
                    947467861,
                    f'Была команда /card от: {person}'
                )

            elif message.text.lower() == '/exam':
                exam_random = random.randint(1, 100)
                a = 4
                if 1 <= exam_random <= 30:
                    a = 1
                elif 31 <= exam_random <= 79:
                    a = 2
                elif 80 <= exam_random <= 99:
                    a = 3
                bot.send_message(
                    person,
                    f'\n{dict2[a]}'
                )
                bot.send_message(
                    947467861,
                    f'Была команда /exam от: {person}'
                )

            elif message.text.lower() == '/the_fool':
                card(1)

            elif message.text.lower() == '/the_magician':
                card(2)

            elif message.text.lower() == '/the_empress':
                card(3)

            elif message.text.lower() == '/the_emperor':
                card(4)

            elif message.text.lower() == '/the_hierophant':
                card(5)

            elif message.text.lower() == '/the_lovers':
                card(6)

            elif message.text.lower() == '/the_fortune':
                card(7)

            elif message.text.lower() == '/the_hanged_man':
                card(8)

            elif message.text.lower() == '/the_death':
                card(9)

            elif message.text.lower() == '/the_devil':
                card(10)

            else:
                st = str(message.text)
                try:
                    recipient_id, text = st.split("\n9092\n", 1)     # Пароль для отправки сообщения разработчиком пользователю
                    bot.send_message(
                        recipient_id,
                        f'Вам сообщение от моего разработчика:\n\n{text}'
                    )
                except:
                    bot.send_message(
                        person,
                        'Извините, ваше сообщение мне не знакомо и даже звёзды тут в замешательстве. '
                        'Я передам ваше сообщение разработчику, '
                        'когда у него будет возможность — он ответит здесь от моего лица.'
                    )
                    bot.send_message(
                        947467861,
                        f'❗'
                    )
                    bot.send_message(
                        947467861,
                        f'{person}'
                    )
                    bot.send_message(
                        947467861,
                        f'{st}'
                    )
        except Exception as ex:
            print(ex)

    bot.polling()


dict = {
    1: 'Шут.'
       '\nКарта обозначает беззаботность, легкомыслие, вдохновение, творчество',
    2: 'Маг.'
       '\nСимволизирует сильного и уверенного в себе человека, который имеет возможность реализовать свои планы',
    3: 'Императрица.\nОлицетворяет гармонию, процветание и рост. '
       'В любом раскладе она символизирует стабильность и позитивное развитие событий',
    4: 'Император.\nОбозначает власть, авторитет и защиту. '
       'Карта гласит, что у того, кому гадают, есть надежный защитник или же он в нем нуждается',
    5: 'Иерофант.'
       '\nОбозначает порабощение или необходимость получения знаний, процесс обучения, а также недостатки',
    6: 'Влюбленные.\nБлизкие отношения, дружба, любовь (иногда к себе). '
       'А также наслаждение, красота, соблазн, стабильность, союз, успех',
    7: 'Фортуна.'
       '\nЧаще всего означает: подарок свыше, успех, перемены, резкий поворот судьбы',
    8: 'Повешенный.\nОбозначает интуицию, испытание, самопожертвование, отказ от чего-то. '
       'А также бесперспективное будущее, тяжелая работа и рамки, которых придется придерживаться',
    9: 'Смерть.\nОзначает конец какого-то периода жизни, в том числе окончание черной полосы. '
       'А также может обозначать потерю и разлуку',
    10: 'Дьявол.'
        '\nОбозначает жадность, страсть, неспособность остановиться, чувство вины и несбалансированность'
}
dict2 = {
    1: 'К сожалению, этот экзамен окажется трудным для вас. Думаю, это не проблема ведь та вчерашняя катка в Доте '
       'точно стоила потраченного на неё времени. А экзамен?.. Его можно будет и пересдать',
    2: 'Экзамен потребует от вас серьёзных усилий, вам попадётся действительно сложный вариант, но карты уверяют '
       'что вы должны справиться и получить свой законный зачёт, ведь вы так усердно готовились всю ночь',
    3: 'Вау, карты говорят что ты очень хорошо потрудился вчера и сегодня на экзамене будешь во всеоружии. '
       'Этот экзамен точно тебе будет по плечу, ведь вкупе с лёгким вариантом, ты гарантированно получишь зачёт',
    4: 'Ты сегодня мило выглядишь ❤'
       '\nУ тебя всё получится шикарно. Карты верят в тебя'
}
print('Start')
telegram_bot('token')
