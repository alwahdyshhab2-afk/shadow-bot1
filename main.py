import telebot
from telebot import types
import requests

# التوكن الخاص بك (المستخرج من BotFather)
TOKEN = '8468154462:AAHkVqMSAqxBQ6iq-TaSYSVH3B-rZkyQKD8'
bot = telebot.TeleBot(TOKEN)

# قائمة الأزرار كما في الصورة التي أرسلتها أول مرة
def main_menu():
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btns = [
        '📸 اختراق الكاميرا', '📍 اختراق الموقع', 
        '🎤 تسجيل صوت', '🚫 إنشاء فيروس', 
        '👁️ صفحات تصيد', '⚠️ تلغيم روابط'
    ]
    markup.add(*(types.KeyboardButton(b) for b in btns))
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "💀 **نظام SHΔDØW CORE نشط** 💀\nبانتظار أوامرك للسيطرة..", reply_markup=main_menu())

@bot.message_handler(func=lambda m: True)
def handle(m):
    if m.text == '📍 اختراق الموقع':
        bot.reply_to(m, "🎯 جاري توليد رابط سحب الإحداثيات.. أرسله للضحية.")
    elif m.text == '📸 اختراق الكاميرا':
        bot.reply_to(m, "📸 جاري تجهيز ثغرة الكاميرا الأمامية..")

bot.polling()
