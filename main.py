import telebot
from telebot import types

TOKEN = '1507507894:AAGPVmkD9begucTC856mvXyYJOvavTFwdyA'
bot = telebot.TeleBot(TOKEN)

question_1 = 'Пара по какому предмету была нашей самой первой парой на матмехе?📝'
question_2 = 'Кому принадлежит фраза:《К концу четвёртого курса студент матмеха становится пришибленнее》? 🌝'
question_3 = 'Сколько математических предметов было у нас за всё время? 💬'
question_4 = 'Кто это? 🐱'
question_5 = 'Кто больше всех подходит Игорю Чернышеву?'
question_6 = 'Сколько вопросов задал Александр Шукстов за весь период обучения?'
question_7 = 'Кто больше всех подходит Редалю Актанову?'
question_8 = 'Какого размера рука у Алексея Прибавина?'
question_9 = 'Сколько лет Михаил Юдин является нашим старостой?'
question_10 = 'Любимый сериал Паши Солдатова?'
question_11 = 'Кто больше выпил пива?'
question_12 = 'Кто самая сладкая булочка на матмехе?'

answer = 'Поздравляю, ты выиграл! Приходи в пятницу на пары и получай приз!'


hi_keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
button_1 = types.KeyboardButton(text="ДА ✅")
button_2 = types.KeyboardButton(text="! НЕТ 🔔")
hi_keyboard.add(button_1, button_2)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
   bot.reply_to(message, f'Привет, наш дорогой одногруппник {message.from_user.first_name}!\n\n'
                          f'Поздравляем тебя с праздником и предлагаем принять участие в увлекательной викторине, '
                          f'по окончанию которой ты можешь выиграть приз!')
   bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEB6ElgM1u5cTGtBDCjlsYYrEdQeSYYtwAC110AAulVBRhTx9VuOje7yR4E')
   bot.send_message(message.chat.id,
                    "Ты готов начать?",
                    reply_markup=hi_keyboard)


keyboard_1 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
button_1 = types.KeyboardButton(text="Математический анализ 📕")
button_2 = types.KeyboardButton(text="Апелляционные системы 📗")
button_3 = types.KeyboardButton(text="Алгебра и геометрия 📘")
keyboard_1.add(button_1, button_2, button_3)

keyboard_2 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
button_1 = types.KeyboardButton(text="Александр Гейн")
button_2 = types.KeyboardButton(text="Магаз Асанов")
button_3 = types.KeyboardButton(text="Денис Березин")
keyboard_2.add(button_1, button_2, button_3)

keyboard_3 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
button_1 = types.KeyboardButton(text="Меньше 10")
button_2 = types.KeyboardButton(text="От 10 до 20")
button_3 = types.KeyboardButton(text="Больше 20")
keyboard_3.add(button_1, button_2, button_3)

keyboard_4 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
button_1 = types.KeyboardButton(text="Петрова")
button_2 = types.KeyboardButton(text="Петрова")
keyboard_4.add(button_1, button_2)

keyboard_5 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
button_1 = types.KeyboardButton(text="Редаль Актанов")
button_2 = types.KeyboardButton(text="Актан Редалев")
keyboard_5.add(button_1, button_2)

keyboard_6 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
button_1 = types.KeyboardButton(text="100")
button_2 = types.KeyboardButton(text="300")
button_3 = types.KeyboardButton(text="ты че пес")
keyboard_6.add(button_1, button_2, button_3)

keyboard_7 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
button_1 = types.KeyboardButton(text="Игорь Чернышев")
button_2 = types.KeyboardButton(text="Черныш Игорев")
keyboard_7.add(button_1, button_2)

keyboard_8 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
button_1 = types.KeyboardButton(text="простите, у меня очень большая рука, не могу набирать")
button_2 = types.KeyboardButton(text="простите, ничего не вижу,тут чья-то рука")
keyboard_8.add(button_1, button_2)

keyboard_9 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
button_1 = types.KeyboardButton(text="1 год")
button_2 = types.KeyboardButton(text="2 года")
button_3 = types.KeyboardButton(text="3 года")
keyboard_9.add(button_1, button_2, button_3)

keyboard_10 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
button_1 = types.KeyboardButton(text="Доктор Кто")
button_2 = types.KeyboardButton(text="Доктор Хаус")
button_3 = types.KeyboardButton(text="Доктор Как")
keyboard_10.add(button_1, button_2, button_3)

keyboard_11 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
button_1 = types.KeyboardButton(text="Шукстов")
button_2 = types.KeyboardButton(text="Мирон")
button_3 = types.KeyboardButton(text="Дэнчик")
button_4 = types.KeyboardButton(text="Костя")
keyboard_11.add(button_1, button_2, button_3, button_4)

keyboard_12 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
button_1 = types.KeyboardButton(text="Я 🌼")
keyboard_12.add(button_1)


@bot.message_handler(content_types=['text'])
def send_text(message):
    try:
        chatid = message.chat.id
        if message.text == 'ДА ✅' or message.text == '!НЕТ 🔔':
            bot.send_message(chatid, question_1, reply_markup=keyboard_1)

        elif message.text.lower() == 'математический анализ 📕':
            bot.send_message(chatid, 'почти)')
            bot.send_sticker(chatid, 'CAACAgIAAxkBAAEB6FVgM2ZfQbTdqnsGq3snPXSyHWdCRAACDQIAAnELQgUWFw2p54h4ER4E')
            bot.send_message(chatid, question_2, reply_markup=keyboard_2)
        elif message.text.lower() == 'апелляционные системы 📗':
            bot.send_message(chatid, 'У нас не было такого предмета, ыыы)))))')
            bot.send_sticker(chatid, 'CAACAgIAAxkBAAEB6FJgM2ZcS8DhK3tL_4u72ICrWqarPQACYwADcQtCBQytAij6PWzGHgQ')
            bot.send_message(chatid, question_2, reply_markup=keyboard_2)
        elif message.text.lower() == 'алгебра и геометрия 📘':
            bot.send_message(chatid, 'Красавчик')
            bot.send_sticker(chatid, 'CAACAgIAAxkBAAEB6FNgM2ZdWNh0MoHq-DSDk7zjcUY7GAACaQADcQtCBd_HSOqRK3qqHgQ')
            bot.send_message(chatid, question_2, reply_markup=keyboard_2)

        elif message.text == 'Александр Гейн':
            bot.send_message(chatid, 'Ты вообще на пары ходил?))')
            bot.send_sticker(chatid, 'CAACAgIAAxkBAAEB6HlgM43jPrEEduALbKgqvRZCKzwSBAACfQAD3wN7BZ_dcWmdqzYaHgQ')
            bot.send_message(chatid, question_3, reply_markup=keyboard_3)
        elif message.text == 'Магаз Асанов':
            bot.send_message(chatid, 'Тест на посещаемость пройден')
            bot.send_sticker(chatid, 'CAACAgIAAxkBAAEB6HlgM43jPrEEduALbKgqvRZCKzwSBAACfQAD3wN7BZ_dcWmdqzYaHgQ')
            bot.send_message(chatid, question_3, reply_markup=keyboard_3)
        elif message.text == 'Денис Березин':
            bot.send_message(chatid, 'Ты вообще на пары ходил?))')
            bot.send_sticker(chatid, 'CAACAgIAAxkBAAEB6HlgM43jPrEEduALbKgqvRZCKzwSBAACfQAD3wN7BZ_dcWmdqzYaHgQ')
            bot.send_message(chatid, question_3, reply_markup=keyboard_3)

        elif message.text == 'Меньше 10':
            bot.send_message(chatid, 'Нам, на самом деле, лень считать)))')
            bot.send_sticker(chatid, 'CAACAgIAAxkBAAEB6P5gM9hJdtpWp2lA3a2ZxQHqjApyMQACBAAD-NLRGolX-SGtdMrdHgQ')
            bot.send_message(chatid, question_4, reply_markup=keyboard_4)
        elif message.text == 'От 10 до 20':
            bot.send_message(chatid, 'Нам, на самом деле, лень считать)))')
            bot.send_sticker(chatid, 'CAACAgIAAxkBAAEB6P5gM9hJdtpWp2lA3a2ZxQHqjApyMQACBAAD-NLRGolX-SGtdMrdHgQ')
            bot.send_message(chatid, question_4, reply_markup=keyboard_4)
        elif message.text == 'Больше 20':
            bot.send_message(chatid, 'Нам, на самом деле, лень считать)))')
            bot.send_sticker(chatid, 'CAACAgIAAxkBAAEB6P5gM9hJdtpWp2lA3a2ZxQHqjApyMQACBAAD-NLRGolX-SGtdMrdHgQ')
            bot.send_message(chatid, question_4, reply_markup=keyboard_4)

        elif message.text == 'Петрова':
            bot.send_message(chatid, question_5, reply_markup=keyboard_5)

        elif message.text == 'Редаль Актанов':
            bot.send_sticker(chatid, 'CAACAgIAAxkBAAEB6QJgM9hTVZOz0RfaHd7wHA19blAnUQACBQAD-NLRGm0W9B8I3j3jHgQ')
            bot.send_message(chatid, question_6, reply_markup=keyboard_6)
        elif message.text == 'Актан Редалев':
            bot.send_sticker(chatid, 'CAACAgIAAxkBAAEB6QJgM9hTVZOz0RfaHd7wHA19blAnUQACBQAD-NLRGm0W9B8I3j3jHgQ')
            bot.send_message(chatid, question_6, reply_markup=keyboard_6)

        elif message.text == '100':
            bot.send_sticker(chatid, 'CAACAgQAAxkBAAEB6FxgM3Cc_eNkNWhwqyo-xYDc8prL9wACFQADUYzPAZqYy_kcac6dHgQ')
            bot.send_message(chatid, question_7, reply_markup=keyboard_7)
        elif message.text == '300':
            bot.send_sticker(chatid, 'CAACAgQAAxkBAAEB6FpgM3CX9jM3U8VeIVHT6643or2ikQACEwADUYzPAfLpWEUJdP3CHgQ')
            bot.send_message(chatid, question_7, reply_markup=keyboard_7)
        elif message.text == 'ты че пес':
            bot.send_sticker(chatid, 'CAACAgIAAxkBAAEB6GJgM3H7MCk8-Feon45PfHTRLdB7DQACFVMAAulVBRgAAfRdEhFSbTUeBA')
            bot.send_message(chatid, question_7, reply_markup=keyboard_7)

        elif message.text == 'Игорь Чернышев':
            bot.send_sticker(chatid, 'CAACAgIAAxkBAAEB6QRgM9hXIotq8hgrBwnMCXZjPUXbBQACBgAD-NLRGghz_HSoupkNHgQ')
            bot.send_message(chatid, question_9, reply_markup=keyboard_9)
        elif message.text == 'Черныш Игорев':
            bot.send_sticker(chatid, 'CAACAgIAAxkBAAEB6QRgM9hXIotq8hgrBwnMCXZjPUXbBQACBgAD-NLRGghz_HSoupkNHgQ')
            bot.send_message(chatid, question_9, reply_markup=keyboard_9)

        elif message.text == 'простите, у меня очень большая рука, не могу набирать':
            bot.send_message(chatid, 'панимаю')
            bot.send_sticker(chatid, 'CAACAgIAAxkBAAEB6IxgM52XoSYnUvF9AAE4Tq-wzKQymVQAAopeAALpVQUY0AsQo91zlKUeBA')
            bot.send_message(chatid, question_9, reply_markup=keyboard_9)
        elif message.text == 'простите, ничего не вижу,тут чья-то рука':
            bot.send_message(chatid, 'панимаю')
            bot.send_sticker(chatid, 'CAACAgIAAxkBAAEB6IxgM52XoSYnUvF9AAE4Tq-wzKQymVQAAopeAALpVQUY0AsQo91zlKUeBA')
            bot.send_message(chatid, question_9, reply_markup=keyboard_9)

        elif message.text == '1 год':
            bot.send_message(chatid, 'больше')
            bot.send_sticker(chatid, 'CAACAgIAAxkBAAEB6JBgM54L3XHeP2HMk6AIHcJY_zlJbwACTAIAAsoDBgsSVmODbCJUUh4E')
            bot.send_message(chatid, question_10, reply_markup=keyboard_10)
        elif message.text == '2 года':
            bot.send_message(chatid, 'больше')
            bot.send_sticker(chatid, 'CAACAgIAAxkBAAEB6JBgM54L3XHeP2HMk6AIHcJY_zlJbwACTAIAAsoDBgsSVmODbCJUUh4E')
            bot.send_message(chatid, question_10, reply_markup=keyboard_10)
        elif message.text == '3 года':
            bot.send_message(chatid, 'красавчик')
            bot.send_sticker(chatid, 'CAACAgIAAxkBAAEB6I5gM53GlFAwsMhaWlVhSd9IPzMOYQACSwEAAjDUnREBhYZ3NsTI6R4E')
            bot.send_message(chatid, question_10, reply_markup=keyboard_10)

        elif message.text == 'Доктор Кто':
            bot.send_sticker(chatid, 'CAACAgIAAxkBAAEB6OxgM9HK2xG8PJySjGTZvE4XE90uoAACMwIAArrAlQWc3UwCquHIDh4E')
            bot.send_message(chatid, question_11, reply_markup=keyboard_11)
        elif message.text == 'Доктор Хаус':
            bot.send_sticker(chatid, 'CAACAgIAAxkBAAEB6OxgM9HK2xG8PJySjGTZvE4XE90uoAACMwIAArrAlQWc3UwCquHIDh4E')
            bot.send_message(chatid, question_11, reply_markup=keyboard_11)
        elif message.text == 'Доктор Как':
            bot.send_message(chatid, 'хехе, такого нет)))))')
            bot.send_sticker(chatid, 'CAACAgIAAxkBAAEB6OxgM9HK2xG8PJySjGTZvE4XE90uoAACMwIAArrAlQWc3UwCquHIDh4E')
            bot.send_message(chatid, question_11, reply_markup=keyboard_11)

        elif message.text == 'Шукстов':
            bot.send_sticker(chatid, 'CAACAgIAAxkBAAEB6O5gM9LH1f0dtw5Q4uHasUjOTQImLwACAwAEa-keDA3fq4FVFA4eBA')
            bot.send_message(chatid, question_12, reply_markup=keyboard_12)
        elif message.text == 'Мирон':
            bot.send_sticker(chatid, 'CAACAgIAAxkBAAEB6O5gM9LH1f0dtw5Q4uHasUjOTQImLwACAwAEa-keDA3fq4FVFA4eBA')
            bot.send_message(chatid, question_12, reply_markup=keyboard_12)
        elif message.text == 'Дэнчик':
            bot.send_sticker(chatid, 'CAACAgIAAxkBAAEB6O5gM9LH1f0dtw5Q4uHasUjOTQImLwACAwAEa-keDA3fq4FVFA4eBA')
            bot.send_message(chatid, question_12, reply_markup=keyboard_12)
        elif message.text == 'Костя':
            bot.send_sticker(chatid, 'CAACAgIAAxkBAAEB6O5gM9LH1f0dtw5Q4uHasUjOTQImLwACAwAEa-keDA3fq4FVFA4eBA')
            bot.send_message(chatid, question_12, reply_markup=keyboard_12)

        elif message.text == 'Я 🌼':
            bot.send_message(chatid, 'Всё так и есть))', reply_markup=types.ReplyKeyboardRemove())
            bot.send_sticker(chatid, 'CAACAgIAAxkBAAEB6H1gM5GCtm1lqtSeeohMkSjJyh5OpgACKQIAAlrjiheVZYpBjeH4vx4E')
            bot.send_message(chatid, answer, reply_markup=types.ReplyKeyboardRemove())
            bot.send_sticker(chatid, 'CAACAgIAAxkBAAEB6IpgM5qrv2ZZVVuuGMhGl-udqOqZZgACiwIAAladvQr3tGImDY878x4E')
        else:
            bot.send_message(message.chat.id, "мы умеем отвечать только на предложенные варианты :)")
    except:
        pass


bot.polling(none_stop=False)
