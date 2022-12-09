# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 12:45:01 2022

@author: konst
"""

farmers = {}

# with open('Export.csv', 'r') as f:
#     for data in f:
#         data_row = data.strip().split(',')
#         #print(data_row)
#         farmers[data_row[0]] = data_row[1:]
#print(farmers)
with open('Export.csv', 'r') as f:
    for data in f:
        data_row = data.strip().split(',')
        #print(data_row)
        if data_row[11] not in farmers:
            farmers[data_row[11]] = []
        farmers[data_row[11]].append(data_row[1:])
#print(farmers)

zip_code = input('Введите почтовый индекс => ')
if zip_code in farmers:
    for market in farmers[zip_code]:
        market_proj = [market[0], market[7], market[9], market[19], market[20]]
        print(" ".join(market_proj))
else:
    print("There is no such zip code in the bd")

city = input('Введите название города => ')
state = input('Введите название штата => ')

for fm_zip in farmers:
    for market in farmers[fm_zip]:
        market_proj = [market[0], market[7], market[9], market[19], market[20]]
        if market_proj[1] == city and market_proj[2] == state:
            print(" ".join(market_proj))
