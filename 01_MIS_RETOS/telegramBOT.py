from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hola, ¡bienvenido al bot!')

def main() -> None:
    updater = Updater("7072827563:AAHCfNu3q8x810V6H5BHk3xS96_4XZwQGFA")

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
    