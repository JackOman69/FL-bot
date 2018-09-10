import telebot
from config import token
from freelance_response import Response

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def handle_start(message):
		name = "Программист"
		object = Response(name)
		res = object.get_dict()
		bot.send_message(message.chat.id, "Добро пожаловать...", + 
			"\n" + "Первое объявление: " + 
			"\n" + "Название: " + res[0]["title"] + '\n' + "Описание: " + res[0]["req"] + 
    	"\n" + "Цена: " + str(res[0]["price"]) + "\n" + "Категория: " + str(res[0]["category"]) + 
    	"\n" + "Кол-во заявок на выполнение: " + res[0]["rates_num"], reply_markup=keyboard)


bot.polling(none_stop=True)