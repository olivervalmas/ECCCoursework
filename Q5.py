def dataFromMessage(m):

    r = 2

    while len(m) > 2**r - r - 1:
        r += 1

    # checks whether m is of length 2^r - r -1
    if len(m) != 2**r - r - 1:
        # print("m is not of length 2^r - r - 1")
        return []

    # isolates bits representing l
    bits = m[:r]
    # calculates l from bits
    l = int(''.join(str(e) for e in bits), 2)
    # print("l: %d" % l)

    if r+l > len(m):
        # print("r+l > len(m)")
        return []

    output = m[r:r+l]

    return output


# print(dataFromMessage([1, 0, 0, 1, 0, 1, 1, 0, 1, 0]))
# print(dataFromMessage([1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0]))
# print(dataFromMessage([0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0]))
