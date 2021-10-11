import serial
from time import localtime, strftime, sleep
import pandas as pd


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
    date = strftime("%m-%d-%Y",localtime())
    time = strftime("%H:%M:%S",localtime())
    row = [date]
    row.append(time)
    return row

def write(row):
    columns = ['Date','Time','Temperature(Celsius)']
    df =  pd.DataFrame(columns=columns)
    df.loc[0] = row
    df.to_csv('data.csv', mode='a', header=False,index=False)

    return
    # with open('data.csv','a',newline = '') as file:
    #     filewriter = csv.writer(file,delimiter=',')
    #     filewriter.writerow(row)



ser = serial.Serial('/dev/ttyACM0')
ser.flushInput()


while True:
    sleep(60-float(strftime("%S",localtime())))

    temperature = read_bytes(ser)
    row = get_time()

    row.append(temperature)

    write(row)