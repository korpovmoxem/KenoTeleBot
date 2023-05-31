from random import random

import telebot


with open('bot_auth.txt', 'r') as file:
    bot_token = str(file.read())
bot = telebot.TeleBot(bot_token)



@bot.message_handler()
def get_message(message):
    print(message.chat.id)


bot.infinity_polling()