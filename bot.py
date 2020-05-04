# -*- coding: utf-8 -*-
import telebot
import converter
import time

url = ''
mp3_file = ''
bot = telebot.TeleBot('854466744:AAHXYY0hQmQiBNOto3dNK8734uiZUhwETro')

@bot.message_handler(commands=['start'])
def start_message(message):	
    bot.send_message(message.chat.id, 'רובוט ראשונים במוזיקה \n מוריד ועורך מיוטיוב')

#@bot.message_handler(content_types=['text'])
#def echo_message(message):
    #bot.reply_to(message, message.text)

@bot.message_handler(func=lambda message: True)
def get_url(message):
	bot.send_message(message.chat.id, 'טוען...')
	try:
		url = message.text
		mp3_file = converter.convert(url)
		#bot.send_message(message.chat.id, 'השיר\n{} \nיורד ונערך...'.format(mp3_file[6 : -4]))
		bot.reply_to(message, 'השיר\n{} \nיורד ונערך...'.format(mp3_file[6 : -4]))
		audio = open(mp3_file, 'rb')
		#bot.send_audio(message.chat.id,audio,'🎵@MusicIsrael🎧','','ראשונים במוזיקה','{}'.format(mp3_file[4:-4]))
		bot.send_audio(message.chat.id,audio,'🎵@MusicIsrael🎧','','ראשונים במוזיקה',mp3_file[4:-4])		
		converter.delete(mp3_file)
	except:
		#converter.delete(mp3_file)
		bot.send_message(message.chat.id, 'ראשונים במוזיקה!')

bot.polling()
