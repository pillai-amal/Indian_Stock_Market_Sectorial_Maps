import requests
import pandas as pd 
import sqlite3
import datetime as dt 

con = sqlite3.connect('indindices.db')
cur = con.cursor()
ticker_lis, price_lis, chg_lis = [], [], []

request = requests.get('https://www.bloombergquint.com/feapi/markets/indices/indian-indices?duration=1D&tab=all').json()

date = dt.date.today()
date = date.strftime('%Y/%m/%d').replace(" ", "")
print(date)
#uncomment what ever I've commented if you are running this for the first time and comment what ever I've not commented
#if you just need the DB file which I have contact me at amalmpillai7@gmail.com 
for i in range(0, len(request['data'])-6):
    # cur.execute(f" CREATE TABLE {request['data'][i]['name'].replace(' ', '')} (date TEXT, price DECIMAL, change DECIMAL);")
    cur.execute(f"INSERT INTO {request['data'][i]['name'].replace(' ', '')} VALUES ('{date}', '{request['data'][i]['price-movement']['current-price']}', '{request['data'][i]['price-movement']['chgp']}')")
    con.commit()
    # ticker_lis.append(request['data'][i]['name'])
    # price_lis.append(request['data'][i]['price-movement']['current-price'])
    # chg_lis.append(request['data'][i]['price-movement']['chgp'])
    # cur.execute(f" CREATE TABLE {request['data'][i]['name'].replace(' ', '')} (date TEXT, price DECIMAL, change DECIMAL);")


