import logging
from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler
import db_mod

WORDS_DB = db_mod.WordsDb()
TOKEN = "1761635851:AAFkWG9yyhCoKtwpjuEwKth8Fp6QC_sQsvY"
REQUEST_KWARGS = {
    'proxy_url': 'socks5://t3.learn.python.ru:443',    # t3 можно менять на t1 или t2
    'urllib3_proxy_kwargs': {
        'assert_hostname': 'False',
        'cert_reqs': 'CERT_NONE',
        'username': 'learn',
        'password': 'python'
    }
}
logging.captureWarnings(True)


def start(update, context):
    update.message.reply_text(
        "Привет! Я эхо-бот. Напишите мне что-нибудь, и я пришлю это назад!")


def help(update, context):
    update.message.reply_text(
        "Я пока не умею помогать... Я только ваше эхо.")


def random_word_game(update, context):
    run = True
    while run:
        word, translations = WORDS_DB.random_word("english_words")
        update.message.reply_text(word)
        if update.message.text.lower() == "/stop":
            run = False
        else:
            if update.message.text.lower() in translations.split(", "):
                update.message.reply_text("Верно")
            else:
                update.message.reply_text("Неверно")
            update.message.reply_text(word)


def main():
    updater = Updater(TOKEN, use_context=True,
                      request_kwargs=REQUEST_KWARGS)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    dp.add_handler(CommandHandler("random_word", random_word_game))
    updater.start_polling()

    # Ждём завершения приложения.
    # (например, получения сигнала SIG_TERM при нажатии клавиш Ctrl+C)
    updater.idle()


if __name__ == '__main__':
    main()
