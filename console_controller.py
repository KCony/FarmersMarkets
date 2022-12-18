import model
from math import radians, cos, sin, asin, sqrt


conn, curs = model.init()

def list_market():
    all_name = model.list_markets(curs)
    for i in all_name:
        print(i)


def list_city():
    all_city = model.all_cities(curs)
    for i in all_city:
        print(i)


def distance(La1, La2, Lo1, Lo2):

    # The math module contains the function name "radians" which is used for converting the degrees value into radians.
    Lo1 = radians(Lo1)
    Lo2 = radians(Lo2)
    La1 = radians(La1)
    La2 = radians(La2)

    # Using the "Haversine formula"
    D_Lo = Lo2 - Lo1
    D_La = La2 - La1
    P = sin(D_La / 2)**2 + cos(La1) * cos(La2) * sin(D_Lo / 2)**2

    Q = 2 * asin(sqrt(P))
    # The radius of earth in Miles.
    R_Mi = 3959

    # Then, we will calculate the result
    return(Q * R_Mi)


def name_by_zip(db_curs, zip_code):
    x = model.find_by_zip(db_curs, zip_code)
    j = 0
    for i in x:
        if j == 0:
            print(f'name of Markets ==> {i}')
        if j == 1:
            print(f'comments about market ==> {i}')
        if j == 2:
            print(f'rating of market ==>  {i}')
        j += 1


def name_by_city(db_curs, city, state):
    found_market = model.find_by_city(db_curs, city, state)
    print('found markets: ')
    for i in found_market:
        cnt = 0
        for j in i:
            if cnt == 0:
                print(f'name of Markets ==> {j}')
            if cnt == 1:
                print(f'comments about market ==> {j}')
            if cnt == 2:
                print(f'rating of market ==> {j}')
            cnt += 1


def details(db_curs, name):
    found_market = model.detailed_data(db_curs, name)
    for i in found_market:
        print(i)


# ПРИМЕРЫ КОМАНД НИЖЕ

# list_market()
# list_city()
# details(curs, "HAPI Fresh Farmers' Market ")
# name_by_city(curs, 'Akron', 'Ohio')
# name_by_zip(curs, 5828)

model.close(conn, curs)
