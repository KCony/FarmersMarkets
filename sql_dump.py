import sqlite3


with sqlite3.connect("server.db") as con:
    cur = con.cursor()

    with open("sql_dump.sql", "w") as f:
        for sql in con.iterdump():
            f.write(sql)
