import serial

ser = serial.Serial('/dev/ttyTHS1', 115200) # /dev/ttyTHS1 should map to J101 carrier board GPIO pins 8 (TXD0) and 10 (RXD0)
print(ser.name) # prints to show user successful port open

while True:
    if ser.inWaiting() > 0:
        data = ser.read_all() # reads in all available bytes 
        print(data) # prints data to Python console
        ser.write(data) # echoes bytes back over serial