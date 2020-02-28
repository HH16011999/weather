import telebot
import pyowm

owm = pyowm.OWM('6d00d1d4e704068d70191bad2673e0cc', language = "ru")
bot = telebot.TeleBot("810378630:AAGlmhfW35e43GoA9raal6L6lj_tDjPCdBE")

@bot.message_handler(content_types=['text'])
def send_echo(message):
	observation = owm.weather_at_place(message.text)
	w = observation.get_weather()
	temp = w.get_temperature('celsius')["temp"]
	answer = "В городе " + message.text + " " + w.get_detailed_status() + "\n"
	answer += "Температура " + str(temp) + " градусов \n\n"

	bot.send_message(message.chat.id, answer)

bot.polling(none_stop = True)