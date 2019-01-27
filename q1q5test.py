from Q1 import message
from Q5 import dataFromMessage
from random import *

randBinList = lambda n: [randint(0, 1) for b in range(1, n + 1)]


def q1q5test():
    for i in range(100):
        data = randBinList(randint(1, 10))
        print("data: " + str(data))
        mess = message(data)
        print("message: " + str(mess))
        newdata = dataFromMessage(mess)
        print("newdata: " + str(newdata))
        assert data == newdata
    print("all tests passed")


# q1q5test()


def q5test():
    for i in range(1000):
        data = randBinList(randint(1, 10))
        print(dataFromMessage(data))

q5test()