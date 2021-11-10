from listener import Temp_listener
from time import localtime, strftime


class Visuals:
    def __init__(self):
        self.serial = Temp_listener()
        self.ops = Operations()

    def current_temp(self):
        temp = self.serial.read_bytes()

        # include code for graphics
        return

    def hourly_temp(self):
        today = strftime("%Y-%m-%d",localtime()).split('-')
        hours = self.ops.hourly(today)

        return
    
    def min_max(self):