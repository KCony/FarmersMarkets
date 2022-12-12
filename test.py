"""

SELECT FROM

"""
import sqlite3


def all_markets():
    """select all markets"""
    with sqlite3.connect('server.d_b') as d_b:
        d_b.row_factory = sqlite3.Row
        sql = d_b.cursor()

        sql.execute("SELECT MarketName FROM Markets")

        for result in sql:
            print(result["MarketName"])


def all_cities():
    """select all city"""
    with sqlite3.connect('server.d_b') as d_b:
        d_b.row_factory = sqlite3.Row
        sql = d_b.cursor()

        sql.execute("SELECT city FROM Markets ORDER BY city")

        for result in sql:
            print(result["city"])


def main():
    """select"""
    while True:
        request = input(">>> ")
        if request == "list":
            return all_markets()
        if request == "list city ASC":
            return all_cities()
        if request == "stop":
            break
        else:
            print("no such command, try again ")


# main()
