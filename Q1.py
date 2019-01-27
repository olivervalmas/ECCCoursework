from hammingGeneratorMatrix import decimalToVector


def message(a):
    l = len(a)
    r = 2

    while not (2**r-2*r-1 >= l):
        r += 1

    k = 2**r - r - 1

    one = decimalToVector(l, r)
    two = a
    three = [0]*(k-r-l)

    output = one + two + three
    return output


def q1test():
    assert message([1]) == [0,0,1,1]
    assert message([0,0,1]) == [0,0,1,1,0,0,1,0,0,0,0]
    assert message([0,1,1,0]) == [0,1,0,0,0,1,1,0,0,0,0]
    assert message([1,1,1,1,0,1]) == [0,1,1,0,1,1,1,1,0,1,0]
    assert message([0,1,1,0,1]) == [0,1,0,1,0,1,1,0,1,0,0]
    print("all tests passed")
