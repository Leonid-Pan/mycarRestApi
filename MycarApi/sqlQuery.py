import sqlite3
import json
conn = sqlite3.connect('db.sqlite3')
file = open('cars1.txt', 'r', encoding='utf-8')
data = file.readlines()

for i in range(len(data)):

    data[i] = data[i].replace("\n", "").replace("[", "").replace("]", "").split("', '")
    data[i] = [y.replace("'", "") for y in data[i]]
    print(data[i])
for i in range(len(data)):
    cur = conn.cursor()
    conn.commit()
    print(data[i])
    cur.execute('INSERT INTO MycarApp_cars (cars_model, cars_price, cars_TKZ, cars_credit, cars_price_credit_in_month, cars_meliage, cars_date_city)  VALUES (?, ?, ?, ?, ?, ?, ?)', data[i])