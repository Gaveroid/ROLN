import serial, numpy, pickle # importing necessary libraries -- serial for comms, numpy for array, and pickle for serializing data
ser = serial.Serial('COM8', 5368709120) # opening port COM8 at desired baud rate
print(ser.name) # printing name of serial port in console to confirm opening was a success

arr = numpy.array([1, 2, 3]) # initializing the numpy array
pickled = pickle.dumps(arr) + b'\n' # pickling/serializing the array to be sent over serial, with newline appended

input("Press enter to continue...") # prompts user for input before sending the info over serial
print("Continuing...") # indicates to the user that the script is continuing

ser.write(pickled) # writes the serialized array over serial