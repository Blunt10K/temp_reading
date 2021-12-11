from time import sleep
from listener import Temp_listener
from operations import Operations


listener = Temp_listener()

ops = Operations()


while True:
    sleep(60-ops.clock())

    temperature = listener.read_temp()
    date, time = ops.get_time()

    ops.write(date, time, temperature)

    listener.display_temp(temperature)