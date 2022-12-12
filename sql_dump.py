"""

Creating file dump

12.12.2022
"""
import sqlite3


with sqlite3.connect("server.db") as con:
    cur = con.cursor()

    with open("sql_dump.sql", "w", encoding="utf-8") as f:
        for sql in con.iterdump():
            f.write(sql)
