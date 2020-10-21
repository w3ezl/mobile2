import telebot #подключаем библиотеку pyTelegramBotAPI
from telebot import types #подключение библиотеки клавиатуры тг
import str_data #подключаем наши файлы
import config #подключаем наши файлы

def kbd_main():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    for btn in str_data.btns_main:
        keyboard.add(btn)
    return keyboard

bot = telebot.TeleBot(config.token , parse_mode="Markdown") #подключаем бота

@bot.message_handler(commands=['start']) #действия бота при команде старт
def send_welcome(message):
    bot.send_message(message.chat.id, str_data.startText, reply_markup=kbd_main()) #отправка сообщения ботом

@bot.message_handler(content_types=['text']) #действие бота при текстовом сообщении от пользователя
def send_messageText(message):
    for i in range(len(str_data.btns_main)): #цикл который считает кол-во кнопок прописанных в str_data
        if message.text == str_data.btns_main[i]: #условие ответа на определенную кнопку
            bot.send_message(message.chat.id, str_data.answ_main[i], reply_markup=kbd_main()) #Отправка сообщения

bot.polling() #закрытие бота