from time import sleep
import serial
from listener import Temp_listener
from operations import Operations


listener = Temp_listener()
listener.flush_serial()

ops = Operations()


while True:
    sleep(60-ops.clock())

    temperature = listener.read_bytes()
    date, time = ops.get_time()

    ops.write(date, time, temperature)