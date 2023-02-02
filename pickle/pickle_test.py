import numpy, pickle

arr = numpy.array([1, 2, 3])
print (arr)

print ('\n\n')

pickled = pickle.dumps(arr)

print(pickled)

print ('\n\n')

unpickled = pickle.loads(pickled)
print(unpickled)
