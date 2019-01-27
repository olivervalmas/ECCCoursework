from hammingGeneratorMatrix import hammingGeneratorMatrix
from numpy import *

def hammingEncoder(m):

    r = 2

    while len(m) > 2**r - r - 1:
        r += 1

    if len(m) != 2**r - r - 1:
        return []

    G = hammingGeneratorMatrix(r)
    raw_output = matmul(m, G)
    output = [x%2 for x in raw_output]

    return output


print(hammingEncoder([1,0,0,0]))
