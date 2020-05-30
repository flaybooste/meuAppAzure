import pyodbc
import json

def start():
    server = 'tcp:dudu.database.windows.net'
    database = 'dudu'
    username = 'dudu'
    password = '102829Pedro%'
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
    return cnxn, cursor

def selectAll():
    con, cur = start()
    cur.execute("SELECT * FROM dbo.posts")
    listadb = cur.fetchall()
    lista = []
    for row in listadb:
        lis = {
            "id": row[0],
            "title":row[1],
            "descp":row[2],
            "author":row[3]
        }
        lista.append(lis)
    return lista

def selectOne(id):
    con, cur = start()
    cur.execute(f"SELECT * FROM dbo.posts WHERE postsid={id}")
    listadb = cur.fetchall()
    return listadb
