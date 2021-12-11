from mariadb import Date, Time
from time import strftime
import sqlalchemy
from to_db import Connector

def get_dates():

    first = input("Date? yyyy-mm-dd\n")
    last = input("\nDate? yyyy-mm-dd\n")

    ds = first.split('-')
    cs = last.split('-')

    conn = Connector()

    first = Date(int(ds[0]),int(ds[1]),int(ds[2]))
    last = Date(int(cs[0]),int(cs[1]),int(cs[2]))


    return conn.dates(first, last)

k = 0
for i in dates:
    print(i.id, i.date,i.time,i.temperature)
    k+=1

    if(k>10):
        break