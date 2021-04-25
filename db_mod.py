# Импорт библиотеки
import sqlite3
import random


class WordsDb:
    def __init__(self):
        # Подключение к БД
        self.con = sqlite3.connect("words_db.sqlite")

        # Создание курсора
        self.cur = self.con.cursor()

    def random_word(self):
        # получение списка всех id слов и выбор одного случайного
        id_list = self.cur.execute("""SELECT id FROM 'english_words'""").fetchall()
        id_word = random.choice(id_list)
        # получение слова и его переводов
        result = self.cur.execute("""SELECT word, translations FROM "english_words"
            WHERE id = ?""", (*id_word, )).fetchone()
        return result
