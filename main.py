from flask import Flask
from threading import Thread
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os

TOKEN = os.environ.get("TOKEN")

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot aktivdir"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

def start(update, context):
    update.message.reply_text("Salam! Mən aktivəm.")

def salam(update, context):
    if 'salam' in update.message.text.lower():
        update.message.reply_text("Aleykum salam")

def main():
    keep_alive()
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, salam))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
