from random import *
from Q1 import message

randBinList = lambda n: [randint(0, 1) for b in range(1, n + 1)]

f = open("randommessages.txt", "w")
for i in range(100):
    f.write(str(message(randBinList(randint(1, 10)))))
    f.write("\n")
f.close()

