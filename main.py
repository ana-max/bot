import telebot
from telebot import types

TOKEN = '1639424406:AAHd229H9PNgE8CPiLqH4tYOIIoWYvAvcAA'
bot = telebot.TeleBot(TOKEN)

question_1 = 'Пара по какому предмету была нашей самой первой парой на матмехе?📝'
question_2 = 'Кому принадлежит фраза:《К концу четвёртого курса студент матмеха становится пришибленнее》?'
question_3 = 'Сколько математических предметов было у нас за всё время?'
question_4 = 'Кто это?'
question_5 = 'Кто самая сладкая булочка на матмехе?'
question_6 = 'Кто больше всех подходит Игорю?'
question_7 = 'Сколько вопросов задал Александр Шукстов за весь период обучения?'


hi_keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
button_1 = types.KeyboardButton(text="ДА")
button_2 = types.KeyboardButton(text="ДААА")
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
button_3 = types.KeyboardButton(text="Петрова")
keyboard_4.add(button_1, button_2, button_3)

keyboard_5 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
button_1 = types.KeyboardButton(text="Я")
keyboard_5.add(button_1)


keyboard_6 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
button_1 = types.KeyboardButton(text="Редаль Актанов")
button_2 = types.KeyboardButton(text="Актан Редалев")
keyboard_6.add(button_1, button_2)


keyboard_7 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
button_1 = types.KeyboardButton(text="100")
button_2 = types.KeyboardButton(text="300")
button_3 = types.KeyboardButton(text="ты че пес")
keyboard_7.add(button_1, button_2, button_3)


@bot.message_handler(content_types=['text'])
def send_text(message):
    chatid = message.chat.id
    if message.text.lower() == 'да' or message.text.lower() == 'дааа':
        bot.send_message(chatid, question_1,reply_markup=keyboard_1)

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
        bot.send_message(chatid, question_3, reply_markup=keyboard_3)
    elif message.text == 'Магаз Асанов':
        bot.send_message(chatid, 'Тест на посещаемость пройден')
        bot.send_message(chatid, question_3, reply_markup=keyboard_3)
    elif message.text == 'Денис Березин':
        bot.send_message(chatid, 'Ты вообще на пары ходил?))')
        bot.send_message(chatid, question_3, reply_markup=keyboard_3)

    elif message.text == 'Меньше 10':
        bot.send_message(chatid, 'Нам, на самом деле, лень считать)))')
        bot.send_photo(chatid, open('images/CeQr_PCiVHQ.png', 'rb'))
        bot.send_message(chatid, question_4, reply_markup=keyboard_4)
    elif message.text == 'От 10 до 20':
        bot.send_message(chatid, 'Нам, на самом деле, лень считать)))')
        bot.send_photo(chatid, open('images/CeQr_PCiVHQ.png', 'rb'))
        bot.send_message(chatid, question_4, reply_markup=keyboard_4)
    elif message.text == 'Больше 20':
        bot.send_message(chatid, 'Нам, на самом деле, лень считать)))')
        bot.send_photo(chatid, open('images/CeQr_PCiVHQ.png', 'rb'))
        bot.send_message(chatid, question_4, reply_markup=keyboard_4)

    elif message.text == 'Петрова':
        bot.send_message(chatid, question_5, reply_markup=keyboard_5)

    elif message.text == 'Я':
        bot.send_message(chatid, 'Всё так и есть))')
        bot.send_message(chatid, question_6, reply_markup=keyboard_6)
    elif message.text == 'Me':
        bot.send_message(chatid, 'Всё так и есть))')
        bot.send_message(chatid, question_6, reply_markup=keyboard_6)

    elif message.text == 'Редаль Актанов':
        bot.send_photo(chatid, open('images/cover_desktop_zip-min.png', 'rb'))
        bot.send_message(chatid, question_7, reply_markup=keyboard_7)
    elif message.text == 'Актан Редалев':
        bot.send_photo(chatid, open('images/cover_desktop_zip-min.png', 'rb'))
        bot.send_message(chatid, question_7, reply_markup=keyboard_7)

    elif message.text == '100':
        bot.send_sticker(chatid, 'CAACAgQAAxkBAAEB6FxgM3Cc_eNkNWhwqyo-xYDc8prL9wACFQADUYzPAZqYy_kcac6dHgQ')
    elif message.text == '300':
        bot.send_sticker(chatid, 'CAACAgQAAxkBAAEB6FpgM3CX9jM3U8VeIVHT6643or2ikQACEwADUYzPAfLpWEUJdP3CHgQ')
    elif message.text == 'ты че пес':
        bot.send_sticker(chatid, 'CAACAgIAAxkBAAEB6GJgM3H7MCk8-Feon45PfHTRLdB7DQACFVMAAulVBRgAAfRdEhFSbTUeBA')
    else:
        bot.send_message(message.chat.id, "да-да, взломал, поломал, тыкни на предложенные варианты :)")


bot.polling(none_stop=True)
