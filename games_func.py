from telegram import ReplyKeyboardMarkup
from db_mod import *
from time import sleep


def make_up_a_word(update, context):
    # берём рандомное слово с переводом
    words_db = WordsDb()
    word, translation = words_db.random_word()

    # перемешиваем слово
    shuffle_word = list(word)
    while "".join(shuffle_word) == word:
        random.shuffle(shuffle_word)

    update.message.reply_text(translation)
    update.message.reply_text(
        "Rearrange the letters correctly \"" +
        "".join(shuffle_word) + "\" You have 10 seconds")

    sleep(10)
    games_keyboard = [['/Make_up_a_word'],
                      ['/Random_tongue_twister'],
                      ['/Theory']]
    games_markup = ReplyKeyboardMarkup(
        games_keyboard, one_time_keyboard=True,
        resize_keyboard=True)
    update.message.reply_text(
        f"I hope you did it.\nCorrect answer is \"{word}\"",
        reply_markup=games_markup)


def random_tongue_twister(update, context):
    games_keyboard = [['/Make_up_a_word'],
                      ['/Random_tongue_twister'],
                      ['/Theory']]
    games_markup = ReplyKeyboardMarkup(
        games_keyboard, one_time_keyboard=True,
        resize_keyboard=True)
    update.message.reply_text(
        "This feature is not available yet. Try again later.",
        reply_markup=games_markup)
