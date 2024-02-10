import sqlite3 as sql

def createDB():
    conn = sql.connect("casas.db")
    conn.commit()
    conn.close()


def createTable():
    conn = sql.connect("casas.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE"""
    )
createDB()