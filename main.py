from flask import Flask
from threading import Thread
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import os

# ========================
# Flask Server
# ========================
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot aktivdir"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# ========================
# Telegram Bot
# ========================

TOKEN = os.environ.get("TOKEN")  # Tokeni mühit dəyişəni kimi saxlayırsan

def start(update, context):
    update.message.reply_text("Salam! Mən aktivəm.")

def salam(update, context):
    if 'salam' in update.message.text.lower():
        update.message.reply_text("Aleykum salam")

def main():
    keep_alive()  # Flask serveri işə salır

    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, salam))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
