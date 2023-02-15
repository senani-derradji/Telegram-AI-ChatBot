# Modules : python-Telegram-Bot , OpenAI
import telegram
from telegram.ext import Updater, MessageHandler, Filters , CommandHandler
import openai
from os import system

# Start Message :
def start_command(update, context):
    start = '''
Asalam Alaykum , السلام عليكم
Welcome to my BOT
You can GET ALL the Answers About :
EveryThings You Want to Know it
This BOT is Working With :
ChatGPT Platform Using Openai API
So .. Enjoy Brother ^_^
    '''
    update.message.reply_text(start)

# Stop Message :
def stop_command(update, context):
    
    stop = '''
Thank You For Using My BOT
See You ...
    '''
    update.message.reply_text(stop)
    

# Define a function to generate a response to a user message using ChatGPT :
def generate_response(message):
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=message.text,
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response["choices"][0]["text"].strip()

# Define a function that is called whenever the bot receives a new message :
def handle_message(update, context):
    message = update.message
    response_text = generate_response(message)
    message.reply_text(response_text)
