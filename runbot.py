from os import listdir
from os.path import isfile, join
import random

import telebot


with open('bot_auth.txt', 'r') as file:
    bot_token = str(file.read())
bot = telebot.TeleBot(bot_token)


pics = [f for f in listdir('wednesday_pics') if isfile(join('wednesday_pics', f))]
#-1001532546328
rand_int = random.randrange(len(pics))
pic_path = '/root/KenoTeleBot/wednesday_pics/' + pics[rand_int]

with open(pic_path, 'rb') as pic:
    pic_file = pic.read()
bot.send_photo('-1001914064521', pic_file)

