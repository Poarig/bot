from telegram import ReplyKeyboardMarkup

from db_mod import *
import sqlite3
import random


def make_up_a_word(update, context):
    pass


def random_tongue_twister(update, context):
    con = sqlite3.connect("words_db.sqlite")
    cur = con.cursor()
    n = random.randint(1, 76)
    twist = cur.execute(f"""SELECT twisters FROM tongue_twisters WHERE id={n}""").fetchone()

    games_keyboard = [['/Make_up_a_word'],
                       ['/Random_tongue_twister'],
                      ['/menu']]
    games_markup = ReplyKeyboardMarkup(games_keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text(twist[0], reply_markup=games_markup)