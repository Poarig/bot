from telegram import ReplyKeyboardMarkup
from db_mod import *


def correct_translation(update, context):
    word = WordsDb().random_word()
    wrong_tr = [WordsDb().random_word()[1] for i in range(3)]
    choose_keyboard = [[word[1]] + wrong_tr]
    choose_markup = ReplyKeyboardMarkup(choose_keyboard, one_time_keyboard=True, resize_keyboard=True)

    update.message.reply_text(f"Choose the correct translation of the word {word[0]}", reply_markup=choose_markup)

    answer = update.message.text

    if answer == word[1]:
        theory_keyboard = [['/Correct_translation', '/Random_word'],
                           ['/Times_of_English']]
        theory_markup = ReplyKeyboardMarkup(theory_keyboard, one_time_keyboard=True, resize_keyboard=True)
        update.message.reply_text("Excellent, Correct answer", reply_markup=theory_markup)
    else:
        theory_keyboard = [['/Correct_translation', '/Random_word'],
                           ['/Times_of_English']]
        theory_markup = ReplyKeyboardMarkup(theory_keyboard, one_time_keyboard=True, resize_keyboard=True)
        update.message.reply_text(f"Nice try, but wrong answer.\n Correct answer is {word[1]}",
                                  reply_markup=theory_markup)


def reserve_random_word(update, context):
    # берём рандомное слово с переводом и выводим их через "-"
    words_db = WordsDb()
    update.message.reply_text(" - ".join(words_db.random_word()))


def times_of_english(update, context):
    update.message.reply_text("test3")
