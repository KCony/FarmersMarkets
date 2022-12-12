"""

SELECT FROM

"""
import sqlite3


def all_markets():
    with sqlite3.connect('server.db') as db:
        db.row_factory = sqlite3.Row
        sql = db.cursor()

        sql.execute("SELECT MarketName FROM Markets")

        for result in sql:
            print(result["MarketName"])


def all_cities():
    with sqlite3.connect('server.db') as db:
        db.row_factory = sqlite3.Row
        sql = db.cursor()

        sql.execute("SELECT city FROM Markets ORDER BY city")

        for result in sql:
            print(result["city"])


def main():
    while True:
        request = input(">>> ")
        if request == "list":
            return all_markets()
        elif request == "list city ASC":
            return all_cities()
        elif request == "stop":
            break
        else:
            print("no such command, try again ")


main()
