from db_mod import *


def correct_translation(update, context):
    update.message.reply_text("test1")


def random_word(update, context):
    # берём рандомное слово с переводом и выводим их через "-"
    words_db = WordsDb()
    update.message.reply_text(" - ".join(words_db.random_word()))


def times_of_english(update, context):
    update.message.reply_text("test3")
