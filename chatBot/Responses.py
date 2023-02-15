# Modules : python-Telegram-Bot , OpenAI
import telegram
from telegram.ext import Updater, MessageHandler, Filters , CommandHandler
import openai

# Start Message :
def start_command(update, context):
    start = '''
assalamu alaikum , السلام عليكم
welcome to my bot
you can ask any question
this bot is working by :
openai api [chat_gpt]
so .. Enjoy '-'
    '''
    update.message.reply_text(start)

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
