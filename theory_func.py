from telegram import ReplyKeyboardMarkup
from time import sleep
from db_mod import *
import random


def correct_translation(update, context):
    correct_word = WordsDb().random_word()
    wrong_words = [WordsDb().random_word()[1] for i in range(3)]

    words = wrong_words + [correct_word[1]]
    choose_keyboard = [[], []]
    while len(words) != 2:
        n = random.randint(0, len(words) - 1)
        choose_keyboard[0].append(words[n])
        del words[n]

    while len(words) != 0:
        n = random.randint(0, len(words) - 1)
        choose_keyboard[1].append(words[n])
        del words[n]
    print(choose_keyboard)
    choose_markup = ReplyKeyboardMarkup(
        choose_keyboard, one_time_keyboard=True, resize_keyboard=True)

    update.message.reply_text(
        f"Choose the correct translation of the word \"{correct_word[0]}\"",
        "\nYou have 10 seconds",
        reply_markup=choose_markup)

    sleep(10)
    theory_keyboard = [['/Correct_translation', '/Random_word'],
                       ['/Times_of_English'],
                       ['/Games']]
    theory_markup = ReplyKeyboardMarkup(
        theory_keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text(
        f"I hope you did it.\nCorrect answer is \"{correct_word[1]}\"",
        reply_markup=theory_markup)


def reserve_random_word(update, context):
    # берём рандомное слово с переводом и выводим их через "-"
    words_db = WordsDb()
    theory_keyboard = [['/Correct_translation', '/Random_word'],
                       ['/Times_of_English'],
                       ['/Games']]
    theory_markup = ReplyKeyboardMarkup(
        theory_keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text(
        " - ".join(words_db.random_word()), reply_markup=theory_markup)


def times_of_english(update, context):
    theory_keyboard = [['/Correct_translation', '/Random_word'],
                       ['/Times_of_English'],
                       ['/Games']]
    theory_markup = ReplyKeyboardMarkup(
        theory_keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text(
        "This feature is not available yet. Try again later.",
        reply_markup=theory_markup)
