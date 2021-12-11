from sense_hat import SenseHat
class Temp_listener:
    def __init__(self):
        self.colours = {"cold":[0,0,255],
                        "warm":[0,255,0],
                        "hot":[255,0,0]}
        self.sense = SenseHat()
        


    def read_temp(self):

        return round(self.sense.get_temperature(),1)

    def display_temp(self, temp):
        if(temp < 16):
            self.sense.show_message(str(temp),text_colour = self.colours["cold"],scroll_speed=0.3)
        elif(temp >= 16 and temp <= 23):
            self.sense.show_message(str(temp),text_colour = self.colours["warm"],scroll_speed=0.3)
        else:
            self.sense.show_message(str(temp),text_colour = self.colours["hot"],scroll_speed=0.3)