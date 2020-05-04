# -*- coding: utf-8 -*-
import telebot
import converter
import time

url = ''
mp3_file = ''
bot = telebot.TeleBot('1290380316:AAFDcVwSopL5XvxkWFSbOEsTW7iBfuYfkyI')

@bot.message_handler(commands=['start'])
def start_message(message):	
    bot.send_message(message.chat.id, 'רובוט ראשונים במוזיקה\nמוריד ועורך שירים מיוטיוב')

#@bot.message_handler(content_types=['text'])
#def echo_message(message):
    #bot.reply_to(message, message.text)

@bot.message_handler(func=lambda message: True)
def get_url(message):
	
	try:
		dele = bot.reply_to(message,'טוען...')
		url = message.text
		mp3_file = converter.convert(url)
		#bot.edit_message_text('ממיר ל - mp3...',message.chat.id,dele.message_id)
		#delee = bot.reply_to(message,'h...')
                audio = open(mp3_file, 'rb')
		bot.edit_message_text('מעלה את הקובץ לטלגרם....',message.chat.id,dele.message_id)
		bot.send_audio(message.chat.id,audio,'🎵@MusicIsrael🎧','','ראשונים במוזיקה',mp3_file[6:-4])		
		bot.delete_message(message.chat.id,dele.message_id)		
		converter.delete(mp3_file)
	except:
		#converter.delete(mp3_file)
                bot.delete_message(message.chat.id,dele.message_id)
                #bot.delete_message(message.chat.id,delee.message_id)
		bot.send_message(message.chat.id, 'טעות בקישור,נסה שוב')
		#bot.delete_message(message.chat.id,dele.message_id)
# -*- coding: utf-8 -*-
import telebot
import converter
import time

url = ''
mp3_file = ''
bot = telebot.TeleBot('1290380316:AAFDcVwSopL5XvxkWFSbOEsTW7iBfuYfkyI')

@bot.message_handler(commands=['start'])
def start_message(message):	
    bot.send_message(message.chat.id, 'רובוט ראשונים במוזיקה\nמוריד ועורך שירים מיוטיוב')

#@bot.message_handler(content_types=['text'])
#def echo_message(message):
    #bot.reply_to(message, message.text)

@bot.message_handler(func=lambda message: True)
def get_url(message):
	
	try:
		dele = bot.reply_to(message,'טוען...')
		url = message.text
		mp3_file = converter.convert(url)
		#bot.edit_message_text('ממיר ל - mp3...',message.chat.id,dele.message_id)
		audio = open(mp3_file, 'rb')
		bot.edit_message_text('מעלה את הקובץ לטלגרם....',message.chat.id,dele.message_id)
		bot.send_audio(message.chat.id,audio,'🎵@MusicIsrael🎧','','ראשונים במוזיקה',mp3_file[6:-4])		
		bot.delete_message(message.chat.id,dele.message_id)		
		converter.delete(mp3_file)
	except:
		#converter.delete(mp3_file)
		bot.send_message(message.chat.id, 'טעות בקישור,נסה שוב')
		bot.delete_message(message.chat.id,dele.message_id)

bot.polling()
bot.polling()
