import telebot

Token = "COPY YOUR TOKEN CREATED"

bot = telebot.TeleBot(Token)
@bot.message_handler(['start'])
def start(message):
    bot.reply_to(message,"Hey,Welcome to Manav44_bot")
    
@bot.message_handler(['help'])
def custom(message):
        bot.reply_to(message,"""/start -> Greetings
        /help -> will give you all commands list 
        If you want to use it as a calculator then you can just start giving me problems
        """)

@bot.message_handler()
def custom(message):
    try:
        msg = eval(message.text.strip())
    except Exception as e:
        msg = "This cant be evaluated"
    bot.reply_to(message,msg)

bot.polling()
