from telegram.bot import Bot
from telegram.user import User
from telegram.ext import Updater, Dispatcher, CommandHandler, CallbackContext, MessageHandler
from telegram.update import Update
from settings.settings import TELEGRAM_TOKEN
import requests
from telegram.ext.filters import Filters

# user: User = bot.get_me()
# print(user.full_name)
# print(user.link)
# print(user.id)
# print(bot.get_me())
# print(type(bot.get_me()))

updater = Updater(token=TELEGRAM_TOKEN)


def start(update: Update, context: CallbackContext):
    update.message.reply_text('Assalomu alaykum! Wikepediya maʼlumotlar saytidan maʼlumot qidiruvchi botga xush kelibsiz! Biron bir maʼlumot olish uchun /search va maʼlumot nomini yozing! Masalan /search Amir Temur.')
    # context.bot.send_message(chat_id=update.message.chat_id, text='Salom nima qilib yuribsan!')
    # print(update)


def search(update: Update, context: CallbackContext):
    args = context.args
    if len(args) == 0:
        update.message.reply_text('Hech bo‘lmaganda biron so‘z kiriting! Masalan /search Amir Temur.')
    else:
        search_text = ' '.join(args)
        response = requests.get('https://uz.wikipedia.org/w/api.php', {
            'action': 'opensearch',
            'search': search_text,
            'limit': 3,
            'namespace': 0,
            'format': 'json'
        })
        result = response.json()
        link = result[3]
        if len(link):
            update.message.reply_text('Sizning so‘ragan maʼlumotingiz quyidagi havolada!' + link[0])
        else:
            update.message.reply_text('Sizning so‘ragan maʼlumotingiz bo‘yicha hech nima topilmadi!')


dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('search', search))
dispatcher.add_handler(MessageHandler(Filters.all, start))

updater.start_polling()
updater.idle()