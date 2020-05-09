# -*- coding: utf-8 -*-
import telebot
import converter
import time
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot import types

url = ''
mp3_file = ''
startm = 'רובוט יוטיוב - ראשונים במוזיקה🎵\nמוריד ועורך שירים מיוטיוב\nלמדריך - /help\n\n💻מפתח הבוט: @rap_ap\nצוות ראשונים במוזיקה✨'
menu = types.ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True)  # create the image selection keyboard
menu.row('🎵 לקבוצה', '🎧 לערוץ')
menu.row('📖 מדריך')
bot = telebot.TeleBot('1290380316:AAFDcVwSopL5XvxkWFSbOEsTW7iBfuYfkyI')

def findat(msg):
    for i in msg:
        if 'https://' in i:
            return i

@bot.message_handler(commands=['start'])
def start_message(message):	
    bot.send_message(message.chat.id, startm,reply_markup=menu)
    bot.send_message(-1001234561658, message.chat.first_name +' נוסף לרובוט\n @'+ message.chat.username)

@bot.message_handler(commands=['help'])
def help_message(message):	
    bot.send_message(message.chat.id, 'הדבר היחיד שאתה צריך זה לשלוח את ה-URL של הסרטון ביוטיוב שאתה רוצה להוריד כמו זה למשל:\nhttps://youtu.be/mQiTfvht20I',disable_web_page_preview=True)

#@bot.message_handler(content_types=['text'])
#def echo_message(message):
    #bot.reply_to(message, message.text)

@bot.message_handler(func=lambda msg: msg.text is not None and 'https://' in msg.text)
def get_url(message):
	
	try:
		dele = bot.reply_to(message,'טוען...')
		texts = message.text.split()
		at_text = findat(texts)
		url = at_text
		mp3_file = converter.convert(url)
		#bot.edit_message_text('ממיר ל - mp3...',message.chat.id,dele.message_id)
		audio = open(mp3_file, 'rb')
		bot.edit_message_text('מעלה את הקובץ לטלגרם....',message.chat.id,dele.message_id)
		bot.send_audio(message.chat.id,audio,'🎵@MusicIsrael🎧','','ראשונים במוזיקה',mp3_file[6:-4],thumb=open('rsz_img_20200510_015426_839.jpg', 'rb'),)	 	
		bot.delete_message(message.chat.id,dele.message_id)
		converter.delete(mp3_file)
                #,reply_to_message_id=message.message_id
	except:
		#converter.delete(mp3_file)
		#bot.send_message(message.chat.id, 'טעות בקישור,נסה שוב')
		bot.delete_message(message.chat.id,dele.message_id)
@bot.message_handler(func=lambda message:True)
def buttons(message):
	if message.text == '📖 מדריך':
		bot.send_message(message.chat.id, 'הדבר היחיד שאתה צריך זה לשלוח את ה-URL של הסרטון ביוטיוב שאתה רוצה להוריד כמו זה למשל:\nhttps://youtu.be/mQiTfvht20I',disable_web_page_preview=True)
	elif message.text == '🎧 לערוץ':
		bot.send_message(message.chat.id, 'https://t.me/MUSICISRAEL')
	elif message.text == '🎵 לקבוצה':
		bot.send_message(message.chat.id, 'https://t.me/joinchat/Bws6sDwdW8nOjVADfQ8gIQ')

bot.polling()
