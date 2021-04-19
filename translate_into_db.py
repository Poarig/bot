import sqlite3
import translators as ts


con = sqlite3.connect("words_db.sqlite")
cur = con.cursor()

f = open("eng_words.txt")
data = [i.strip() for i in f.readlines()]

for i in range(len(data)):
    t = ts.google(data[i], from_language="en", to_language='ru')
    res = cur.execute(f"""INSERT INTO english_words(id, "word", "translations") VALUES ({i+1}, "{data[i]}", "{t}")""")
    con.commit()
