def repetitionDecoder(v):
    return [] if v.count(0) == v.count(1) else [int(v.count(0) < v.count(1))]


print(repetitionDecoder([0, 1, 0]))
