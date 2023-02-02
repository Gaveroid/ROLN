import serial, numpy, pickle # importing necessary libraries -- serial for comms, numpy for array, and pickle for serializing data
ser = serial.Serial('COM9', 5368709120) # opening port COM8 at desired baud rate
print(ser.name) # printing name of serial port in console to confirm opening was a success

data = ser.readline() # reading line of serialized array data

arr = pickle.loads(data) # un-pickling serialized data into numpy array
print(arr) # printing numpy array to verify successful transmission and decoding