from telegram.bot import Bot
from telegram.user import User
from telegram.ext import Updater, Dispatcher, CommandHandler, CallbackContext
from telegram.update import Update
from settings.settings import TELEGRAM_TOKEN


# user: User = bot.get_me()
# print(user.full_name)
# print(user.link)
# print(user.id)
# print(bot.get_me())
# print(type(bot.get_me()))

updater = Updater(token=TELEGRAM_TOKEN)


def start(update: Update, context: CallbackContext):
    update.message.reply_text('Salom!')
    context.bot.send_message(chat_id=update.message.chat_id, text='Salom nima qilib yuribsan!')
    # print(update)


dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))

updater.start_polling()
updater.idle()