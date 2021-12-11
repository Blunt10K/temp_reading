from mariadb import Date, Time
from time import localtime, strftime
from to_db import *


class Operations:
    def __init__(self):
        self.conn = Connector()

    def get_connector(self):
        return self.conn
        
    def clock(self):
        return float(strftime("%S",localtime()))
        
    def get_time(self):
        date = strftime("%Y-%m-%d",localtime()).split('-')
        time = strftime("%H:%M",localtime()).split(':')

        return date, time

    def write(self, date, time,temperature):
        d = Date(int(date[0]),int(date[1]),int(date[2]))
        t = Time(int(time[0]),int(time[1]),0)
        
        self.conn.addTemperature(d,t,temperature)

        return
