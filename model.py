"""
pylint на строку докуемнтации ругается?

09.12.2022
"""
import sqlite3
import csv


data = []
with open('Data\Export.csv', 'r') as f:
    y = csv.reader(f)
    for row in y:
        data.append(row)


db = sqlite3.connect('server.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS Markets (
    MarketName TEXT, street TEXT, city TEXT, county TEXT,
    state TEXT, zip INT, locX FLOAT, locY FLOAT)""")

sql.execute("""CREATE TABLE IF NOT EXISTS Media (
    Website TEXT, Facebook TEXT, Twitter TEXT,
    Youtube TEXT, OtherMedia TEXT)""")

sql.execute("""CREATE TABLE IF NOT EXISTS Season (
    Season1Date TEXT, Season1Time TEXT, Season2Date TEXT, Season2Time TEXT,
    Season3Date TEXT, Season3Time TEXT, Season4Date TEXT, Season4Time TEXT)""")

sql.execute("""CREATE TABLE IF NOT EXISTS MarketsCr (
    Credit TEXT, WIC TEXT, WICcash TEXT, SFMNP TEXT,
    SNAP TEXT, Organic TEXT, Bakedgoods TEXT, Cheese TEXT, 
    Crafts TEXT, Flowers TEXT, Eggs TEXT, Seafood TEXT,
    Herbs TEXT, Vegetables TEXT, Honey TEXT, Jams TEXT, 
    Maple TEXT, Meat TEXT, Nursery TEXT,
    Nuts TEXT, Plants TEXT, Poultry TEXT, Prepared TEXT
    Soap TEXT, Trees TEXT, Wine TEXT, Coffee TEXT, 
    Beans TEXT, Fruits TEXT, Grains TEXT,
    Juices TEXT, Mushrooms TEXT, PetFood TEXT, Tofu TEXT,
    WildHarvested TEXT)""")

db.commit()

count = 1
for i in data[1:len(data)]:
    sql.execute("INSERT INTO Markets VALUES (?,?,?,?,?,?,?,?)",
                (data[count][1], data[count][7], data[count][8],
                 data[count][9], data[count][10], data[count][11],
                 data[count][20], data[count][21]))
    sql.execute("INSERT INTO Media VALUES (?,?,?,?,?)",
                (data[count][2], data[count][3], data[count][4],
                 data[count][5], data[count][6]))
    sql.execute("INSERT INTO Season VALUES (?,?,?,?,?,?,?,?)",
                (data[count][12], data[count][13], data[count][14],
                 data[count][15], data[count][16], data[count][17],
                 data[count][18], data[count][19]))
    sql.execute("INSERT INTO MarketsCr VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (data[count][23], data[count][24], data[count][25],
                 data[count][26], data[count][27], data[count][28],
                 data[count][29], data[count][30], data[count][31],
                 data[count][32], data[count][33], data[count][34],
                 data[count][35], data[count][36], data[count][37],
                 data[count][38], data[count][39], data[count][40],
                 data[count][41], data[count][42], data[count][43],
                 data[count][44], data[count][45], data[count][46],
                 data[count][47], data[count][48], data[count][49],
                 data[count][50], data[count][51], data[count][52],
                 data[count][53], data[count][54], data[count][55],
                 data[count][56]))
    db.commit()
    count += 1

db.close()