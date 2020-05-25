import sqlite3

con = sqlite3.connect("database/main.db")
cur = con.cursor()

def criarTbl():
    cur.execute('''CREATE TABLE posts(
        id INTEGER PRIMARY KEY,
        desc TEXT,
        user TEXT
    )''')
    cur.fetchall()
    con.commit()
    return print("sucesso")

def inserirTeste():
    cur.execute("INSERT INTO posts VALUES (1,'TESTE','luis')")
    cur.fetchone()
    con.commit()


def selecionarTbl():
    cur.execute("SELECT * FROM posts")
    return cur.fetchone()