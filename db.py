import pyodbc

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
    return cur.fetchall()