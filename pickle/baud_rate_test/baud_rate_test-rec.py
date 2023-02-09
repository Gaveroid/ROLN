import serial, numpy, pickle # importing necessary libraries -- serial for comms, numpy for array, and pickle for serializing data
ser = serial.Serial('COM9', 9600) # 5000000) # opening port COM8 at desired baud rate
print("Opened serial port on: " + ser.name) # printing name of serial port in console to confirm opening was a success

numErrors = 0 # stores number of errors
numTries = 1000 # desired number of tries
for i in range(1, numTries + 1): # executes as many times as desired
    try: # attempts to read and unpickle the array
        data = ser.readline() # reading line of serialized array data
        arr = pickle.loads(data) # un-pickling serialized data into numpy array
        print(arr) # printing numpy array to verify successful transmission and decoding
    except: # if an error occured, increments the error counter
        numErrors+=1
        print("Whoops! Error number " + str(numErrors) + " has just occurred.")

errorRate = numErrors/numTries # calculates error rate
print("\n")
print("There were " + str(numErrors) + " errors out of " + str(numTries) + " tries.\n") # prints error count to user
print("Error rate: " + str(errorRate * 100) + "%") # prints error rate to user






    

