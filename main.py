from translate import to_cyrillic, to_latin
import telebot
import os

# TOKEN= "5656330760:AAEfAYX2cRqmCFvbG0l_N-TkxW8L0T7DwkE"

bot = telebot.TeleBot(os.getenv('BOT_TOKEN'),parse_mode=None)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    user_name = message.from_user.first_name
    
    res = f"Tuzumi {user_name} brat, anaqade hozi sho'tga krilcha yozsez lotincha qilib qaytaradide"

    bot.reply_to(message, res)
    
# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    if msg.isascii():
        javob = to_cyrillic(msg)
    else:
        javob = to_latin(msg)
    
    bot.reply_to(message, javob)    

bot.polling()