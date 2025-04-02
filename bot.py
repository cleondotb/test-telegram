from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

import os

TOKEN = os.getenv("7574444976:AAHvGc1_o163C6fsX4bfoyBeQv1tTb5oLd4")

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello! I am your bot.")

updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler("start", start))

updater.start_polling()
updater.idle()
