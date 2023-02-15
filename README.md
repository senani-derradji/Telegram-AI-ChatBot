# AI-CHATBOT
![](https://img.shields.io/badge/BOT-%20-red)
![](https://img.shields.io/badge/CHAT-BOT%20%2B1-brightgreen)
![](https://img.shields.io/badge/Telegram-BOT%20-blue)
![](https://img.shields.io/badge/AI-BOT%20-yellowgreen)

![](https://blog-assets.freshworks.com/freshdesk/wp-content/uploads/2018/08/Header_gif_assembly-1.gif)
#
# Install and Run
```python
> pip install --upgrade pip setuptools wheel
> git clone https://github.com/u0a254/Telegram-AI-ChatBot
> cd Telegram-AI-ChatBot
> python setup.py
```
#
# Using and Create
```python
if you want to put your personal bot and openai_api_key and run the bot directly just follow this steps :
> open chatBot/const.py
> replace my telegram bot api token by your bot api token and the same thing with openai api token and SAVE it
> open chatBot/main.py 
> delete the all information of ''' Derradji Bot '''
> delete the # from #openai.api_key = cs.openai_api_token()
```
#
# Explain
```bash
you will see some modules like dotenv and functions like getenv()
the target from this module and this function is the privacy when you want to publish your key's
like openai-api-key with your project you need to secure it by create .env file and use the function getenv("api-key")
and module speedtest you can by it make a condition if (internet_speed < 2MB) => don't run the bot
that's it , i hope you like my project , thank you ^_^
```
#
# How to create Your own OpenAI API
```go
> go to : https://openai.com/api
> Signup new Account
> while you have account , you go to : https://platform.openai.com/account/api-keys
> create new secret api
========= if you want to put it tn this project =========
> go to : chatBot/const.py [ openai_api_key() ]
```
#
# How to Create a Telegram own Bot and get The Bot Token
```ruby
> open Telegram App
> Search on @botfather
> /start
> /newbot
> Choose a Bot Name
> Choose a Bot UserName like : Bot_yourname
> /setuserpic
> Choose The picture and send it to the @fatherbot
> /token
> and you will get the bot token copy it
========= if you want to put it tn this project =========
> go to : chatBot/const.py [ telegram_bot_api_token() ]
```
