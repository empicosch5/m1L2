import telebot
from bot_logic import gen_pass
from coinflip import coin1


# Замени 'TOKEN' на токен твоего бота
# Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot("7896634459:AAEzdxiT-uwTxx4AHl_SJB4I7boaMApJkHM")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['gen_pass'])
def send_pas(message):
    bot.reply_to(message, gen_pass(8))

@bot.message_handler(commands=['coin'])
def send_coin(message):
    bot.reply_to(message, coin1())

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
