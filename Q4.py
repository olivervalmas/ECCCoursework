def is_power_of_two(n):
    """Return True if n is a power of two."""
    if n < 0:
        return False
    else:
        return n & (n - 1) == 0


def messageFromCodeword(c):
    if not is_power_of_two(len(c)+1):
        return []
    c.reverse()
    c = [v for i, v in enumerate(c) if is_power_of_two(i)]
    c.reverse()
    return c


print(messageFromCodeword([1, 1, 1, 0, 0, 0, 0]))

