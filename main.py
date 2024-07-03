import telebot
import config
import api

bot = telebot.TeleBot(config.token, parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, text="""
    💵Данный бот переводит одну валюту в другую.

Пример сообщения боту - 
GBPUSD 150       (британский фунт стерлингов к доллару США)
        или
QAREGP 100       (катарский риал к египитским фунтам)

Список достпуных валют - /values
    """)


@bot.message_handler(commands=['values'])
def send_welcome(message):
    msg = api.values()
    bot.send_message(message.chat.id, text=msg)


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    end_value = api.get_value(message.text.upper())
    bot.send_message(message.chat.id, text=end_value)


bot.infinity_polling()
