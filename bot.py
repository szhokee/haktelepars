import telebot
from my_token import token
from telebot import types
from parsing import main

data = main()

bot = telebot.TeleBot(token)

inline_keyboard = types.ReplyKeyboardMarkup()
btn1 = types.KeyboardButton("1")
btn2 = types.KeyboardButton("2")
btn3 = types.KeyboardButton("3")
btn4 = types.KeyboardButton("4")
btn5 = types.KeyboardButton("5")
btn6 = types.KeyboardButton("6")
btn7 = types.KeyboardButton("7")
btn8 = types.KeyboardButton("8")
btn9 = types.KeyboardButton("9")
btn10 = types.KeyboardButton("10")
btn11 = types.KeyboardButton("11")
btn12 = types.KeyboardButton("12")
btn13 = types.KeyboardButton("13")
btn14 = types.KeyboardButton("14")
btn15 = types.KeyboardButton("15")
btn16 = types.KeyboardButton("16")
btn17 = types.KeyboardButton("17")
btn18 = types.KeyboardButton("18")
btn19 = types.KeyboardButton("19")
btn20 = types.KeyboardButton("20")

income_keyboard = types.ReplyKeyboardMarkup()
k1 = types.KeyboardButton('Description')
k2 = types.KeyboardButton('Photo')
k3 = types.KeyboardButton('Quit')

inline_keyboard.add(btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9,btn10,btn11,btn12,btn13,btn14,btn15,btn16,btn17,btn18,btn19,btn20)
income_keyboard.add(k1,k2,k3)


@bot.message_handler(commands=['start'])
def start(message):
    data = main()

    bot.send_message(message.chat.id,"Привет, парсим категорию - ВСЕ НОВОСТИ: ")
    
    if len(data) == 0:
         bot.send_message(message.chat.id,"На сегодняшний день пока новостей еще нет")
         return

    c = 0
    for i in data:
        c += 1
        bot.send_message(message.chat.id, str(c) + '. ' + i[0])

    bot.send_message(message.chat.id, "Какую новость показать подробней? ", reply_markup=inline_keyboard)
    bot.register_next_step_handler(message, check_answer, data)


def check_answer(message, data):
    number = int(message.text) - 1
    if number > len(data):
        bot.send_message(message.chat.id,"таких новостей пока нет")
        return

    bot.send_message(message.chat.id, "Выбери что хочешь: ",reply_markup=income_keyboard)
    bot.register_next_step_handler(message, get_info, number, data)


def get_info(message, number, data):
    if message.text == "Description":
        bot.send_message(message.chat.id, data[number][2])

    elif message.text == "Photo":
        bot.send_photo(message.chat.id, data[number][1])

    else:
        bot.send_message(message.chat.id, "До свидания")


bot.polling()