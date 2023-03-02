import serial, numpy, pickle, random # importing necessary libraries -- serial for comms, numpy for array, and pickle for serializing data
ser = serial.Serial('COM8', 9600) # 5000000) # opening port COM8 at desired baud rate
print("Opened serial port on " + ser.name + " at " + str(ser.baudrate) + " baud") # printing name of serial port in console to confirm opening was a success

input("Press enter to continue...") # prompts user for input before sending the info over serial
print("Continuing...") # indicates to the user that the script is continuing

def countBits(x):
    bits = 0
    while(x):
        bits += x & 1
        x >>= 1
    return bits

numTries = 1000
numErrors = 0 # stores number of errors
for i in range(1, numTries + 1):
    sendByte = random.randbytes(1)
    ser.write(sendByte)
    print("Sent byte " + str(i) + "/" + str(numTries) + ": " + str(sendByte))

    recByte = ser.read(1)
    xor = numpy.bitwise_xor(recByte, sendByte)
    if (xor != 0):
        numErrors += countBits(xor)
    

errorRate = numErrors/(numTries * 8) # calculates error rate
print("\n")
print("Error rate for " + ser.baudrate + " bytes: " + str(errorRate * 100) + "%") # prints error rate to user