from random import random

import telebot


with open('bot_auth.txt', 'r') as file:
    bot_token = str(file.read())
bot = telebot.TeleBot(bot_token)



@bot.message_handler()
def get_message(message):
    print(message.chat.id)


@bot.channel_post_handler()
def a(message):
    print(message.chat.id)



bot.infinity_polling()

'''
bot.send_message('-1001914064521', 'test')
'''