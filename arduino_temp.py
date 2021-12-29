import serial

def read_bytes(ser):
    bytes = ser.readline()
    decoded = bytes[0:len(bytes)-2].decode("utf-8")
    decoded = float(decoded)
    return decoded

ser = serial.Serial('/dev/ttyACM0')
ser.flushInput()

temp = read_bytes(ser)

print(temp)