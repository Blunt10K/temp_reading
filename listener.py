import serial

class Temp_listener:
    def __init__(self):
        self.serial = serial.Serial('/dev/ttyACM0')


    def flush_serial(self):
        self.serial.flushInput()
        return

    def read_bytes(self):
        while True:
            try:
                ser_bytes = self.serial.readline()
                decoded = ser_bytes[0:len(ser_bytes)-2].decode("utf-8")
                decoded = float(decoded)

                return decoded
            except:
                pass

        return 
