from db_mod import *


def make_up_a_word(update, context):
    # берём рандомное слово с переводом
    words_db = WordsDb()
    word, translation = words_db.random_word()

    # перемешиваем слово
    shuffle_word = list(word)
    while "".join(shuffle_word) == word:
        random.shuffle(shuffle_word)

    update.message.reply_text(translation)
    update.message.reply_text("".join(shuffle_word))

    # сравниваем ответ с правельным словом и соответствующе реагируем
    if update.message.text == word:
        update.message.reply_text("Верно")
    else:
        update.message.reply_text("Неверно")
        update.message.reply_text("Правельный ответ: " + word)


def random_tongue_twister(update, context):
    update.message.reply_text("test5")
