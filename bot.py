from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Votre token Telegram ici
TOKEN = '7336063002:AAGsbs_w3RRpymYBxFjII2CPI0B2d_Smcs0'


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        'Bienvenue dans le bot de minage de cryptomonnaie!')


def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
