import telebot
from config import token

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def handle_start(message):
