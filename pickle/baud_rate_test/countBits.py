import numpy

a = 105
b = 109
xor = numpy.bitwise_xor(a, b)

def countBits(x):
    bits = 0
    while(x):
        bits += x & 1
        x >>= 1
    return bits

print(countBits(xor))