"""

DATA BASE SQLite3
Class Model
В качестве экземпляра класса выступает база данных

"""
import sqlite3
from math import radians, cos, sin, asin, sqrt


class Model:
    """The database acts as an instance of the class"""
    def __init__(self, f_name):            # Подключение к базе данных
        """init"""
        self.db_conn = sqlite3.connect(f_name)
        self.db_curs = self.db_conn.cursor()

    def close_conn(self):            # Закрытие базы данных
        """close connect"""
        self.db_curs.close()
        self.db_conn.close()

    def list_markets(self):          # Список всех рынков
        """select all name of market"""
        markets_list = []
        self.db_curs.execute("SELECT Name FROM Markets")

        for result in self.db_curs:
            markets_list.append(result[0])
        return markets_list

    def all_cities(self):            # Список всех городов рынков
        """select all cities"""
        cities_list = []
        self.db_curs.execute("SELECT city FROM Cities ORDER BY city")
        for result in self.db_curs:
            cities_list.append(result[0])
        return cities_list

    def find_by_zip(self, zip_code):         # Поиск рынка по ZIP-коду
        """searching name of Market by ZIP code"""
        self.db_curs.execute("""SELECT Name FROM Markets WHERE
        ID = (SELECT idMarket FROM Addresses WHERE ZIP = ?)""", (zip_code, ))
        name_by_zip = self.db_curs.fetchone()
        return name_by_zip

    def find_by_city(self, city, state):         # Поиск рынка по городу и штату
        """searching name of Market by city and state"""
        id_market = []
        self.db_curs.execute("""SELECT idMarket FROM Addresses WHERE City =
        (SELECT ID FROM Cities WHERE City = ?) AND State =
        (SELECT ID FROM States WHERE State = ?)""", (city, state))
        for result in self.db_curs:
            id_market.append(result)
        list_by = []
        for ID in id_market:
            self.db_curs.execute("""SELECT Name FROM Markets WHERE ID = ? """, ID)
            list_by.append(self.db_curs.fetchone())

        return list_by

    def detailed_data(self, name_market):            # Детали о рынке
        """shows details about Market"""
        found_id = []
        self.db_curs.execute("""SELECT ID FROM Markets WHERE Name = ? """, (name_market, ))
        for result in self.db_curs:
            found_id.append(result)
        found_street = []
        for ID in found_id:
            self.db_curs.execute(f"""SELECT City FROM Addresses
                            WHERE idMarket = {ID[0]}""")
            city = self.db_curs.fetchone()
            self.db_curs.execute(f"""SELECT State FROM Addresses
                            WHERE idMarket = {ID[0]}""")
            state = self.db_curs.fetchone()
            self.db_curs.execute(f"""SELECT County FROM Addresses
                            WHERE idMarket = {ID[0]}""")
            county = self.db_curs.fetchone()

            self.db_curs.execute(f"""SELECT addresses.*, cities.city, states.state,
            counties.county, media.* FROM Addresses, Cities, states, counties,
            media WHERE addresses.idmarket = {ID[0]} and cities.id = {city[0]}
            AND states.id = {state[0]} AND counties.id = {county[0]}
            AND media.idMarket = {ID[0]}""")
            found_street.append(self.db_curs.fetchone())

        return found_street

    def comments(self, comment, id_market):     # Добавление комментария в БД
        """Adding a comment to market"""
        self.db_curs.execute("""INSERT INTO Comments VALUES (?,?)""", (comment, id_market))
        self.db_conn.commit()

    def rating(self, rating_m, id_market):   # Добавление рейтинга в БД
        """Adding a rating to market"""
        self.db_curs.execute("""INSERT INTO Ratings VALUES (?,?)""", (rating_m, id_market))
        self.db_conn.commit()

    def dist_btwn_m(self, market1, market2):     # расчет дистанции между рынками
        """determining the distance between markets"""
        self.db_curs.execute("""SELECT LocX, LocY FROM Addresses WHERE
        idMarket = (SELECT ID FROM Markets WHERE Name = ?)""", (market1, ))
        mrkt1 = self.db_curs.fetchone()
        self.db_curs.execute("""SELECT LocX, LocY FROM Addresses WHERE
        idMarket = (SELECT ID FROM Markets WHERE Name = ?)""", (market2, ))
        mrkt2 = self.db_curs.fetchone()

        lo1 = radians(float(mrkt1[0]))
        lo2 = radians(float(mrkt2[0]))
        la1 = radians(float(mrkt1[1]))
        la2 = radians(float(mrkt2[1]))

        d_lo = lo2 - lo1
        d_la = la2 - la1
        d_p = sin(d_la / 2) ** 2 + cos(la1) * cos(la2) * sin(d_lo / 2) ** 2
        result = ((2 * asin(sqrt(d_p))) * 3959)
        return result

    def comm_market(self, idmarket):         # коммнтарии магазина
        """add comments about the market"""
        cmnts = []
        self.db_curs.execute("""SELECT Comment FROM Comments WHERE idMarket = ?""", (idmarket, ))
        for comment in self.db_curs:
            cmnts.append(comment)
        return cmnts

    def rating_market(self, idmarket):         # средний рейтинг магазина
        """add rating about the market"""
        self.db_curs.execute("""SELECT AVG(Rating) FROM Ratings WHERE idMarket = ?""", (idmarket, ))
        rating = self.db_curs.fetchall()
        return rating
