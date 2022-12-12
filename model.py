"""
Import data from csv in db

12.12.2022
"""
import sqlite3
import csv


data = []
with open('Data/Export.csv', 'r', encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:                       # переписываемя данные с CSV файла
        data.append(row)


db = sqlite3.connect('server.db')            # подключаемся к файлу БД
sql = db.cursor()
# создаем 4 таблицы
sql.execute("""CREATE TABLE IF NOT EXISTS Markets (
    IDMarket INTEGER PRIMARY KEY AUTOINCREMENT, MarketName TEXT, 
    street TEXT, city TEXT, county TEXT,
    state TEXT, zip INTEGER, locX FLOAT, locY FLOAT)""")

sql.execute("""CREATE TABLE IF NOT EXISTS Media (
    IDMarket INTEGER PRIMARY KEY AUTOINCREMENT,
    Website TEXT, Facebook TEXT, Twitter TEXT,
    Youtube TEXT, OtherMedia TEXT)""")

sql.execute("""CREATE TABLE IF NOT EXISTS Season (
    IDMarket INTEGER PRIMARY KEY AUTOINCREMENT,
    Season1Date TEXT, Season1Time TEXT, Season2Date TEXT, Season2Time TEXT,
    Season3Date TEXT, Season3Time TEXT, Season4Date TEXT, Season4Time TEXT)""")

sql.execute("""CREATE TABLE IF NOT EXISTS MarketsCr (
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

db.commit()                         # подтверждение выполнения изменений в файле БД

cnt = 1                           # цикл проходит по переменной data с данныйми из CSV
for i in data[1:len(data)]:         # и добовляет данные в 4 таблицы
    sql.execute("INSERT INTO Markets VALUES (null,?,?,?,?,?,?,?,?)",
                (data[cnt][1], data[cnt][7], data[cnt][8],
                 data[cnt][9], data[cnt][10], data[cnt][11],
                 data[cnt][20], data[cnt][21]))
    sql.execute("INSERT INTO Media VALUES (null,?,?,?,?,?)",
                (data[cnt][2], data[cnt][3], data[cnt][4],
                 data[cnt][5], data[cnt][6]))
    sql.execute("INSERT INTO Season VALUES (null,?,?,?,?,?,?,?,?)",
                (data[cnt][12], data[cnt][13], data[cnt][14],
                 data[cnt][15], data[cnt][16], data[cnt][17],
                 data[cnt][18], data[cnt][19]))
    sql.execute("INSERT INTO MarketsCr VALUES (null,?,?,?,?,?,?,?,?,"
                "?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (data[cnt][23], data[cnt][24], data[cnt][25],
                 data[cnt][26], data[cnt][27], data[cnt][28],
                 data[cnt][29], data[cnt][30], data[cnt][31],
                 data[cnt][32], data[cnt][33], data[cnt][34],
                 data[cnt][35], data[cnt][36], data[cnt][37],
                 data[cnt][38], data[cnt][39], data[cnt][40],
                 data[cnt][41], data[cnt][42], data[cnt][43],
                 data[cnt][44], data[cnt][45], data[cnt][46],
                 data[cnt][47], data[cnt][48], data[cnt][49],
                 data[cnt][50], data[cnt][51], data[cnt][52],
                 data[cnt][53], data[cnt][54], data[cnt][55],
                 data[cnt][56], data[cnt][56]))
    db.commit()                    # обязательное подтверждение изменений в БД
    cnt += 1

db.close()                         # закрытие файла
