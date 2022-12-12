"""

SELECT FROM

"""
import sqlite3


def all_markets():
    """select all markets"""
    with sqlite3.connect('server.db') as d_b:
        d_b.row_factory = sqlite3.Row
        sql = d_b.cursor()

        sql.execute("SELECT MarketName FROM Markets")

        for result in sql:
            print(result["MarketName"])


def all_cities():
    """select all city"""
    with sqlite3.connect('server.db') as d_b:
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
            all_markets()
            print("Next requestt (list, list city ASC, stop):")
        if request == "list city ASC":
            all_cities()
            print("Next requestt (list, list city ASC, stop):")
        if request == "stop":
            break


# main()
