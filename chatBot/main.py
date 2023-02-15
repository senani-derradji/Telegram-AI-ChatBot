# Modules
import telegram
from telegram.ext import Updater, MessageHandler, Filters , CommandHandler
import openai
import Responses as rp
import const as cs
#from os import getenv, system
#from dotenv import load_dotenv
from time import sleep
#import speedtest


###############
#load_dotenv()#
###############

####################################################
''' Derradji Bot '''
#print ("put here your the telegram API Token")
#telegram_api_token_bot = str(input("╰─>"))
print ("put here your the OpenAI API Token")
openai_api_key = str(input("╰─>"))
####################################################


#####################################################
''' Personal Bot '''
telegram_api_token_bot = cs.telegram_bot_token()
#openai.api_key = cs.openai_api_key()
######################################################

sleep(1)
# Set up the Telegram bot using the python-telegram-bot library
print("Starting The Bot ...")
def main():

    updater = Updater(token=telegram_api_token_bot, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", rp.start_command))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, rp.handle_message))

    # Start the bot
    updater.start_polling()
    sleep(1)
    print("Done ...\tap @derradjichatbot in telegram search-bar\BOT is running ....")
    updater.idle()

main()
