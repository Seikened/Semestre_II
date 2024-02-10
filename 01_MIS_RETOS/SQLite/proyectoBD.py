import sqlite3 as sql

def createDB():
    conn = sql.connect("casas.db")
    conn.commit()
    conn.close()


createDB()