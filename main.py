import logging
from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from constants import *
from theory_func import *
from games_func import *


logging.captureWarnings(True)


def start(update, context):
    start_keyboard = [['/Theory', '/Games']]
    start_markup = ReplyKeyboardMarkup(
        start_keyboard, one_time_keyboard=False, resize_keyboard=True)
    if update.message.text == "/start":
        update.message.reply_text(
            "Hey! I am a bot for learning English.\nСhoose a way to study.",
            reply_markup=start_markup)
    elif update.message.text == "/menu":
        update.message.reply_text("Сhoose a way to study.",
                                  reply_markup=start_markup)


def close_keyboard(update, context):
    update.message.reply_text(
        "What would you like to do next?\nTo reopen the menu, enter /menu",
        reply_markup=ReplyKeyboardRemove()
    )


def helper(update, context):
    # Добавить описание всех кнопок в помощник
    update.message.reply_text("Sorry, but I can't help you right now.")
    pass


def theory(update, context):
    theory_keyboard = [['/Correct_translation', '/Random_word'],
                       ['/Times_of_English', '/menu']]
    theory_markup = ReplyKeyboardMarkup(theory_keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text("Nice choice!", reply_markup=theory_markup)


def games(update, context):
    games_keyboard = [['/Make_up_a_word'],
                      ['/Random_tongue_twister'],
                      ['/menu']]
    games_markup = ReplyKeyboardMarkup(games_keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text("Good luck!", reply_markup=games_markup)


def main():
    updater = Updater(TOKEN, use_context=True,
                      request_kwargs=REQUEST_KWARGS)
    dp = updater.dispatcher

    text_handler_start = CommandHandler(["start", "menu"], start)
    text_handler_close = CommandHandler("close", close_keyboard)
    text_handler_help = CommandHandler("help", helper)
    text_handler_theory = CommandHandler("Theory", theory)
    text_handler_games = CommandHandler("Games", games)
    text_handler_correct_translation = CommandHandler(
        "Correct_translation", correct_translation)
    text_handler_random_word = CommandHandler(
        "Random_word", reserve_random_word)
    text_handler_times_of_english = CommandHandler(
        "Times_of_English", times_of_english)
    text_handler_make_up_a_word = CommandHandler(
        "Make_up_a_word", make_up_a_word)
    text_handler_random_tongue_twister = CommandHandler(
        "Random_tongue_twister", random_tongue_twister)

    dp.add_handler(text_handler_start)
    dp.add_handler(text_handler_close)
    dp.add_handler(text_handler_help)
    dp.add_handler(text_handler_theory)
    dp.add_handler(text_handler_games)
    dp.add_handler(text_handler_correct_translation)
    dp.add_handler(text_handler_random_word)
    dp.add_handler(text_handler_times_of_english)
    dp.add_handler(text_handler_make_up_a_word)
    dp.add_handler(text_handler_random_tongue_twister)

    updater.start_polling()
    # Ждём завершения приложения.
    # (например, получения сигнала SIG_TERM при нажатии клавиш Ctrl+C)
    updater.idle()


if __name__ == '__main__':
    main()
