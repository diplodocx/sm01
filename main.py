import telebot

from config import TOKEN, ADM_CHAT_ID

from db import test_conn

bot = telebot.TeleBot(TOKEN, parse_mode=None)


@bot.message_handler(commands=['test'])
def test(message):
    bot.send_message(message.from_user.id, message.from_user.username)
    res = test_conn()
    bot.send_message(message.from_user.id, f"{res[0]}")
    # message.from_user.id - ид юзера
    # message.chat.id - ид чата
    # message.from_user.username - никнейм


@bot.message_handler(commands=['fix'])
def fix(message):
    if message.chat.id != ADM_CHAT_ID:
        bot.send_message(message.chat.id, 'не поймаешь не догонишь не возьмешь')
        return
    bot.send_message(message.from_user.id, message.from_user.id)
    # message.from_user.id - ид юзера
    # message.chat.id - ид чата


bot.infinity_polling()
