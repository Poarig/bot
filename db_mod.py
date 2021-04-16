# Импорт библиотеки
import sqlite3
import random


class WordsDb:
    def __init__(self):
        # Подключение к БД
        self.con = sqlite3.connect("words_db.sqlite")

        # Создание курсора
        self.cur = self.con.cursor()

    def random_word(self, table_name):
        # получение списка всех id слов и выбор одного случайного
        id_list = self.cur.execute("""SELECT id FROM ?""", (table_name,)).fetchall()
        id_word = random.choice(id_list)
        # получение слова и его переводов
        result = self.cur.execute("""SELECT word, translations FROM words
            WHERE id = ?""", (id_word, )).fetchall()
        return result
