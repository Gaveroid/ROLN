import serial, numpy, pickle, random # importing necessary libraries -- serial for comms, numpy for array, and pickle for serializing data
ser = serial.Serial('COM8', 9600) # 5000000) # opening port COM8 at desired baud rate
print("Opened serial port on: " + ser.name) # printing name of serial port in console to confirm opening was a success


input("Press enter to continue...") # prompts user for input before sending the info over serial
print("Continuing...") # indicates to the user that the script is continuing

numTries = 1000
for i in range(1, numTries + 1):
    arr = numpy.array([random.randint(1,999), random.randint(1,999), random.randint(1,999)]) # initializing the numpy array with 3 random ints
    pickled = pickle.dumps(arr) + b'\n' # pickling/serializing the array to be sent over serial, with newline appended
    ser.write(pickled) # writes the serialized array over serial
    print("Sent array " + str(i) + "/" + str(numTries) + ": " + str(arr))
