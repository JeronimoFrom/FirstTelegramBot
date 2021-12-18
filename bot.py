from telebot import types
import telebot

bot = telebot.TeleBot('5010274292:AAHAPVcB9hiohiu6qja6zs6Q4Um-gnGYrwM')


@bot.message_handler(commands=['start'])
def welcome(message):

	photo = open('/home/jeronimo/Изображения/1618815701_51.jpg', 'rb')
	bot.send_photo(message.chat.id, photo)

	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

	button1 = types.KeyboardButton("жим")
	button2 = types.KeyboardButton("Byu iphone")
	markup.add(button1, button2)

	bot.send_message(message.chat.id,f"Здравствуйте, мусььЁ!", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def aswer(message):
	if message.text == "жим":
		bot.send_message(message.chat.id, 'jmi')
	elif message.text =="Byu iphone":


		markup = types.InlineKeyboardMarkup(row_width=2)

		button1 = types.InlineKeyboardButton("Iphone 11", callback_data='Iphone 11')
		button2 = types.InlineKeyboardButton("Iphone 11 Pro", callback_data='Iphone 11 Pro')
		button3 = types.InlineKeyboardButton("Iphone 12", callback_data='Iphone 12')
		button4 = types.InlineKeyboardButton("Iphone 12 Pro", callback_data='Iphone 12 Pro')
		button5 = types.InlineKeyboardButton("Iphone 13", callback_data='Iphone 13')
		button6 = types.InlineKeyboardButton("Iphone 13 Pro", callback_data='Iphone 13 Pro')

		markup.add(button1, button2, button3, button4, button5, button6)

		bot.send_message(message.chat.id,"Какой гейфон вас интересует",reply_markup=markup)

	else:
		bot.send_message(message.chat.id,"Error")

@bot.callback_query_handler(func= lambda call : True)
def callback_inline(call):
	try:
		if call.message:
			if call.data =="Iphone 11":
				bot.send_message(call.message.chat.id,'1000$')

			if call.data == "Iphone 11 Pro":
				bot.send_message(call.message.chat.id, '1100$')

			if call.data == "Iphone 12":
				bot.send_message(call.message.chat.id, '1200$')

			if call.data == "Iphone 12 Pro":
				bot.send_message(call.message.chat.id, '1250$')

			if call.data == "Iphone 13 ":
				bot.send_message(call.message.chat.id, '1300$')

			if call.data == "Iphone 13 Pro":
				bot.send_message(call.message.chat.id, '1400$')

	except:
		print('error')

bot.polling(none_stop=True)