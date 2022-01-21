from sense_hat import SenseHat
import serial
from numpy import median


BLUE = [0,0,255]
GREEN = [0,255,0]
RED = [255,0,0]

ROTATION = 0
NUM_READINGS = 20

WARM_MIN = 16
WARM_MAX = 28

class Temp_listener:
    def __init__(self):
        self.colours = {"cold": BLUE,
                        "warm": GREEN,
                        "hot": RED}


        self.sense = SenseHat()
        self.sense.set_rotation(ROTATION)
        self.sense._init_humidity()
        self.sense._init_pressure()


        self.ser = serial.Serial('/dev/ttyACM0')
        self.ser.flushInput()


        self.last = None



    def read_temp(self):
        while True:
            readings = []
            try:
                for i in range(NUM_READINGS):
                    bytes = self.ser.readline()
                    decoded = bytes[0:len(bytes)-2].decode("utf-8")
                    decoded = float(decoded)
                    readings.append(decoded)
                break
            except:
                pass

        return median(decoded)

    def read_humidity(self):
        return self.sense.get_humidity()

    def read_pressure(self):
        return self.sense.get_pressure()

    def last_reading(self):
        self.sense.low_light = True
        self.sense.clear(self.last)
        return


    def display_temp(self, temp):
        self.sense.low_light = False

        if(temp < WARM_MIN):
            self.sense.show_message(str(temp),text_colour = self.colours["cold"],scroll_speed=0.3)
            self.last = self.colours["cold"]
        elif(temp >= WARM_MIN and temp <= WARM_MAX):
            self.sense.show_message(str(temp),text_colour = self.colours["warm"],scroll_speed=0.3)
            self.last = self.colours["warm"]
        else:
            self.sense.show_message(str(temp),text_colour = self.colours["hot"],scroll_speed=0.3)
            self.last = self.colours["hot"]