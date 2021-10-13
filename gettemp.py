import serial
from time import localtime, strftime, sleep
import pandas as pd
from to_db import *
from mariadb import Date, Time


def read_bytes(ser):
    go = True
    while go:
        try:
            ser_bytes = ser.readline()
            decoded = ser_bytes[0:len(ser_bytes)-2].decode("utf-8")
            decoded = float(decoded)

            return decoded
        except:
            pass

    return 

def get_time():
    date = strftime("%Y-%m-%d",localtime()).split('-')
    time = strftime("%H:%M:%S",localtime()).split(':')
    return date, time

def write(date, time,temperature):
    d = Date(int(date[0]),int(date[1]),int(date[2]))
    t = Time(int(time[0]),int(time[1]),int(time[2]))
    
    addTemperature(d,t,temperature)

    return



ser = serial.Serial('/dev/ttyACM0')
ser.flushInput()


while True:
    sleep(60-float(strftime("%S",localtime())))

    temperature = read_bytes(ser)
    date, time = get_time()

    write(date, time, temperature)