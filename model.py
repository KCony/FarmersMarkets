"""
Import data from csv in db

12.12.2022
"""
import sqlite3
import csv
import tests.tests_model as tm


def etl():
    data = []
    with open('Data/Export.csv', 'r', encoding="utf-8") as f:
        reader = csv.reader(f, skipinitialspace=True)
        for row in reader:  # переписываем данные с CSV файла
            data.append(row)
    db_conn, db_curs = init()
    # создаем 4 таблицы
    db_curs.execute("""CREATE TABLE IF NOT EXISTS Markets (
        IDMarket INTEGER PRIMARY KEY AUTOINCREMENT, MarketName TEXT, 
        street TEXT, city TEXT, county TEXT,
        state TEXT, zip INTEGER, locX FLOAT, locY FLOAT)""")

    db_curs.execute("""CREATE TABLE IF NOT EXISTS Media (
        IDMarket INTEGER PRIMARY KEY AUTOINCREMENT,
        Website TEXT, Facebook TEXT, Twitter TEXT,
        Youtube TEXT, OtherMedia TEXT)""")

    db_curs.execute("""CREATE TABLE IF NOT EXISTS Season (
        IDMarket INTEGER PRIMARY KEY AUTOINCREMENT,
        Season1Date TEXT, Season1Time TEXT, Season2Date TEXT, Season2Time TEXT,
        Season3Date TEXT, Season3Time TEXT, Season4Date TEXT, Season4Time TEXT)""")

    db_curs.execute("""CREATE TABLE IF NOT EXISTS MarketsCr (
        IDMarket INTEGER PRIMARY KEY AUTOINCREMENT,
        Credit TEXT, WIC TEXT, WICcash TEXT, SFMNP TEXT,
        SNAP TEXT, Organic TEXT, Bakedgoods TEXT, Cheese TEXT, 
        Crafts TEXT, Flowers TEXT, Eggs TEXT, Seafood TEXT,
        Herbs TEXT, Vegetables TEXT, Honey TEXT, Jams TEXT, 
        Maple TEXT, Meat TEXT, Nursery TEXT,
        Nuts TEXT, Plants TEXT, Poultry TEXT, Prepared TEXT,
        Soap TEXT, Trees TEXT, Wine TEXT, Coffee TEXT, 
        Beans TEXT, Fruits TEXT, Grains TEXT,
        Juices TEXT, Mushrooms TEXT, PetFood TEXT, Tofu TEXT,
        WildHarvested TEXT)""")

    db_conn.commit()                         # подтверждение выполнения изменений в файле БД

    CNT = 1                           # цикл проходит по переменной data с данными из CSV
    for i in data[1:len(data)]:         # и добавляет данные в 4 таблицы
        db_curs.execute("INSERT INTO Markets VALUES (null,?,?,?,?,?,?,?,?)",
                    (data[CNT][1], data[CNT][7], data[CNT][8],
                     data[CNT][9], data[CNT][10], data[CNT][11],
                     data[CNT][20], data[CNT][21]))
        db_curs.execute("INSERT INTO Media VALUES (null,?,?,?,?,?)",
                    (data[CNT][2], data[CNT][3], data[CNT][4],
                     data[CNT][5], data[CNT][6]))
        db_curs.execute("INSERT INTO Season VALUES (null,?,?,?,?,?,?,?,?)",
                    (data[CNT][12], data[CNT][13], data[CNT][14],
                     data[CNT][15], data[CNT][16], data[CNT][17],
                     data[CNT][18], data[CNT][19]))
        db_curs.execute("INSERT INTO MarketsCr VALUES (null,?,?,?,?,?,?,?,?,"
                    "?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                    (data[CNT][23], data[CNT][24], data[CNT][25],
                     data[CNT][26], data[CNT][27], data[CNT][28],
                     data[CNT][29], data[CNT][30], data[CNT][31],
                     data[CNT][32], data[CNT][33], data[CNT][34],
                     data[CNT][35], data[CNT][36], data[CNT][37],
                     data[CNT][38], data[CNT][39], data[CNT][40],
                     data[CNT][41], data[CNT][42], data[CNT][43],
                     data[CNT][44], data[CNT][45], data[CNT][46],
                     data[CNT][47], data[CNT][48], data[CNT][49],
                     data[CNT][50], data[CNT][51], data[CNT][52],
                     data[CNT][53], data[CNT][54], data[CNT][55],
                     data[CNT][56], data[CNT][56]))
        db_curs.commit()                    # обязательное подтверждение изменений в БД
        CNT += 1


def init():
    db_conn = sqlite3.connect('server.db')  # подключаемся к файлу БД
    db_curs = db_conn.cursor()
    return db_conn, db_curs


def close(db_conn, db_curs):
    db_curs.close()
    db_conn.close()                         # закрытие файла


def list_markets(db_curs, cmd_line):
    # Пока реализуется функция — показать список всех рынков. Потом параметры будут передаваться через список - cmd_line
    markets_list = []
    db_curs.execute("SELECT MarketName FROM Markets")

    for result in db_curs:
        markets_list.append(result[0])
    return markets_list


def find_market(db_curs, market_name):
    #  Ищем рынок по названию. Рынков с одним названием может быть несколько?
    found_markets_list = []
    db_curs.execute("SELECT MarketName FROM Markets")
    for m_Name in db_curs:
        found_markets_list.append(m_Name)  # Добавляем рынок в список найденных
    return found_markets_list


def all_cities(db_curs):
    cities_list = []
    db_curs.execute("SELECT city FROM Markets ORDER BY city")

    for result in db_curs:
        cities_list.append(result[0])
    return cities_list


if __name__ == '__main__':
    tm.run_all_tests()
