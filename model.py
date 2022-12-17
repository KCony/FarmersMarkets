"""

DATA BASE SQLite3

"""
import sqlite3
import csv
import tests_model as tm


def create_table():
    """Creating table"""
    db_conn = sqlite3.connect('server2.db')
    db_curs = db_conn.cursor()

    db_curs.execute("""CREATE TABLE IF NOT EXISTS `Markets` (
  `ID` INTEGER NOT NULL PRIMARY KEY,
  `Name` VARCHAR(255),
  `Comments` VARCHAR(255),
  `Rating` INT,
  `UpdateTime` VARCHAR(255))""")

    db_curs.execute("""CREATE TABLE IF NOT EXISTS `Addresses` (
  `Street` VARCHAR(255),
  `City` INT,
  `County` INT,
  `State` INT,
  `ZIP` INT,
  `LocX` VARCHAR(45),
  `LocY` VARCHAR(45),
  `idMarket` INT NOT NULL,
    FOREIGN KEY (`idMarket`) REFERENCES `Markets` (`ID`),
    FOREIGN KEY (`City`) REFERENCES `Cities` (`ID`),
    FOREIGN KEY (`County`) REFERENCES `Counties` (`ID`),
    FOREIGN KEY (`State`) REFERENCES `States` (`ID`))""")

    db_curs.execute("""CREATE TABLE IF NOT EXISTS `Media` (
  `Website` VARCHAR(255) NULL,
  `Facebook` VARCHAR(255) NULL,
  `Twitter` VARCHAR(255) NULL,
  `Youtube` VARCHAR(255) NULL,
  `OtherMedia` VARCHAR(255) NULL,
  `idMarket` INT NOT NULL,
    FOREIGN KEY (`idMarket`) REFERENCES `Markets` (`ID`))""")

    db_curs.execute("""CREATE TABLE IF NOT EXISTS `Cities` (
  `ID` INTEGER NOT NULL PRIMARY KEY,
  `City` VARCHAR(255))""")

    db_curs.execute("""CREATE TABLE IF NOT EXISTS `Counties` (
  `ID` INTEGER NOT NULL PRIMARY KEY,
  `County` VARCHAR(45))""")

    db_curs.execute("""CREATE TABLE IF NOT EXISTS `States` (
  `ID` INTEGER NOT NULL PRIMARY KEY,
  `State` VARCHAR(45))""")

    db_curs.execute("""CREATE TABLE IF NOT EXISTS `Seasons` (
  `Season1Date` VARCHAR(45),
  `Season1Time` VARCHAR(45),
  `Season2Date` VARCHAR(45),
  `Season2Time` VARCHAR(45),
  `Season3Date` VARCHAR(45),
  `Season3Time` VARCHAR(45),
  `Season4Date` VARCHAR(45),
  `Season4Time` VARCHAR(45),
  `idMarket` INT NOT NULL,
    FOREIGN KEY (`idMarket`) REFERENCES `Markets` (`ID`))""")

    db_curs.execute("""CREATE TABLE IF NOT EXISTS `PaymentMethods` (
  `Credit` VARCHAR(45),
  `WIC` VARCHAR(45),
  `WICcash` VARCHAR(45),
  `SFMNP` VARCHAR(45),
  `SNAP` VARCHAR(45),
  `idMarket` INT NOT NULL,
    FOREIGN KEY (`idMarket`) REFERENCES `Markets` (`ID`))""")

    db_curs.execute("""CREATE TABLE IF NOT EXISTS `Categories` (
  `Organic` VARCHAR(45),
  `Bakedgoods` VARCHAR(45),
  `Cheese` VARCHAR(45),
  `Crafts` VARCHAR(45),
  `Flowers` VARCHAR(45),
  `Eggs` VARCHAR(45),
  `Seafood` VARCHAR(45),
  `Herbs` VARCHAR(45),
  `Vegetables` VARCHAR(45),
  `Honey` VARCHAR(45),
  `Jams` VARCHAR(45),
  `Maple` VARCHAR(45),
  `Meat` VARCHAR(45),
  `Nursery` VARCHAR(45),
  `Nuts` VARCHAR(45),
  `Plants` VARCHAR(45),
  `Poultry` VARCHAR(45),
  `Prepared` VARCHAR(45),
  `Soap` VARCHAR(45),
  `Trees` VARCHAR(45),
  `Wine` VARCHAR(45),
  `Coffee` VARCHAR(45),
  `Beans` VARCHAR(45),
  `Fruits` VARCHAR(45),
  `Grains` VARCHAR(45),
  `Juices` VARCHAR(45),
  `Mushrooms` VARCHAR(45),
  `PetFood` VARCHAR(45),
  `Tofu` VARCHAR(45),
  `WildHarvested` VARCHAR(45),
  `idMarket` INT NOT NULL,
    FOREIGN KEY (`idMarket`) REFERENCES `Markets` (`ID`))""")

    db_conn.commit()
    db_curs.close()
    db_conn.close()


def insert_from_csv():
    """filling tables with data"""
    data = []
    with open('Data/Export.csv', 'r', encoding="utf-8") as f:
        reader = csv.reader(f, skipinitialspace=True)
        for row in reader:
            data.append(row)

    db_conn = sqlite3.connect('server2.db')
    db_curs = db_conn.cursor()

    cnt = 1
    for i in data[1:]:
        db_curs.execute("INSERT INTO Markets VALUES (null,?,null,null,null)", (i[1],))
        db_curs.execute("INSERT INTO Addresses VALUES (?,null,null,null,?,?,?,?)", (i[7], i[11], i[20], i[21], cnt))
        db_curs.execute("INSERT INTO Media VALUES (?,?,?,?,?,?)", (i[2], i[3], i[4], i[5], i[6], cnt))
        db_curs.execute("INSERT INTO Seasons VALUES (?,?,?,?,?,?,?,?,?)",
                        (i[12], i[13], i[14], i[15], i[16], i[17], i[17], i[19], cnt))
        db_curs.execute("INSERT INTO PaymentMethods VALUES (?,?,?,?,?,?)",
                        (i[23], i[24], i[25], i[26], i[27], cnt))
        db_curs.execute("INSERT INTO Categories VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                        (i[28], i[29], i[30], i[31], i[32], i[33], i[34], i[35], i[36], i[37],
                         i[38], i[39], i[40], i[41], i[42], i[43], i[44], i[45], i[46], i[47],
                         i[48], i[49], i[50], i[51], i[52], i[53], i[54], i[55], i[56], i[57], cnt))
        db_conn.commit()
        cnt += 1

    city = []
    with open('Data/Export.csv', 'r', encoding="utf-8") as f:
        reader = csv.reader(f, skipinitialspace=True)
        for row in reader:
            city.append(row[8])
    city_uniq = set(city)

    for city in city_uniq:
        db_curs.execute("INSERT INTO Cities VALUES (null,?)", (city,))
        db_conn.commit()

    county = []
    with open('Data/Export.csv', 'r', encoding="utf-8") as f:
        reader = csv.reader(f, skipinitialspace=True)
        for row in reader:
            county.append(row[9])
    county_uniq = set(county)

    for county in county_uniq:
        db_curs.execute("INSERT INTO Counties VALUES (null,?)", (county,))
        db_conn.commit()

    state = []
    with open('Data/Export.csv', 'r', encoding="utf-8") as f:
        reader = csv.reader(f, skipinitialspace=True)
        for row in reader:
            state.append(row[10])
    state_uniq = set(state)

    for state in state_uniq:
        db_curs.execute("INSERT INTO States VALUES (null,?)", (state,))
        db_conn.commit()

    db_curs.close()
    db_conn.close()


def insert_city():
    """unique cities"""
    db_conn = sqlite3.connect('server2.db')
    db_curs = db_conn.cursor()

    db_curs.execute("""SELECT * FROM Cities""")
    x = db_curs.fetchall()
    city_list = []
    for i in x:
        city_list.append(i)

    city = []
    with open('Data/Export.csv', 'r', encoding="utf-8") as f:
        reader = csv.reader(f, skipinitialspace=True)
        for row in reader:
            city.append(row[8])

    in_table = []
    for i in city[1:]:
        for j in city_list:
            if i in j:
                in_table.append(j[0])

    countrow = 1
    for idCity in in_table:
        db_curs.execute("UPDATE Addresses SET City = ? WHERE idMarket = ?", (idCity, countrow))
        countrow += 1

    db_conn.commit()
    db_curs.close()
    db_conn.close()


def insert_county():
    """unique counties"""
    db_conn = sqlite3.connect('server2.db')
    db_curs = db_conn.cursor()

    db_curs.execute("""SELECT * FROM Counties""")
    x = db_curs.fetchall()
    county_list = []
    for i in x:
        county_list.append(i)

    county = []
    with open('Data/Export.csv', 'r', encoding="utf-8") as f:
        reader = csv.reader(f, skipinitialspace=True)
        for row in reader:
            county.append(row[9])

    in_table = []
    for i in county[1:]:
        for k in county_list:
            if i in k:
                in_table.append(k[0])

    countrow = 1
    for idCounty in in_table:
        db_curs.execute("UPDATE Addresses SET County = ? WHERE idMarket = ?", (idCounty, countrow))
        countrow += 1

    db_conn.commit()
    db_curs.close()
    db_conn.close()


def insert_state():
    """unique states"""
    db_conn = sqlite3.connect('server2.db')
    db_curs = db_conn.cursor()

    db_curs.execute("""SELECT * FROM States""")
    x = db_curs.fetchall()
    state_list = []
    for i in x:
        state_list.append(i)

    state = []
    with open('Data/Export.csv', 'r', encoding="utf-8") as f:
        reader = csv.reader(f, skipinitialspace=True)
        for row in reader:
            state.append(row[10])

    in_table = []
    for i in state[1:]:
        for k in state_list:
            if i in k:
                in_table.append(k[0])

    countrow = 1
    for idState in in_table:
        db_curs.execute("UPDATE Addresses SET State = ? WHERE idMarket = ?", (idState, countrow))
        countrow += 1

    db_conn.commit()
    db_curs.close()
    db_conn.close()


def init():
    """init"""
    db_conn = sqlite3.connect('server2.db')
    db_curs = db_conn.cursor()
    return db_conn, db_curs


def close(db_conn, db_curs):
    """close connect"""
    db_curs.close()
    db_conn.close()


def list_markets(db_curs):
    """select all name of market"""
    markets_list = []
    db_curs.execute("SELECT Name FROM Markets")

    for result in db_curs:
        markets_list.append(result[0])
    return markets_list


def all_cities(db_curs):
    """select all cities"""
    cities_list = []
    db_curs.execute("SELECT city FROM Cities ORDER BY city")
    for result in db_curs:
        cities_list.append(result[0])
    return cities_list


def find_by_zip(db_curs, zip_code):
    """searching name of Market by ZIP code"""
    db_curs.execute("""SELECT Name, comments, rating FROM Markets WHERE 
    ID = (SELECT idMarket FROM Addresses WHERE ZIP = ?)""", (zip_code, ))
    name_by_zip = db_curs.fetchone()
    return name_by_zip

def find_by_city(db_curs, city, state):
    """searching name of Market by city and state"""
    xc = []
    db_curs.execute("""SELECT idMarket FROM Addresses WHERE City = 
    (SELECT ID FROM Cities WHERE City = ?) AND State = 
    (SELECT ID FROM States WHERE State = ?)""", (city, state))
    for result in db_curs:
        xc.append(result)
    list_by = []
    for i in xc:
        db_curs.execute("""SELECT Name, comments, rating FROM Markets WHERE ID = ? """, i)
        list_by.append(db_curs.fetchone())

    return list_by

if __name__ == '__main__':
    tm.run_all_tests()
