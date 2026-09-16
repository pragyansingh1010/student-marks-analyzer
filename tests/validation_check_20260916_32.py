def valid_mark(x):
    return isinstance(x, int) and 0 <= x <= 100

assert valid_mark(100)
