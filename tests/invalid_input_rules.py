def valid_mark(x):
    return 0 <= x <= 100

assert valid_mark(0)
assert valid_mark(100)
assert not valid_mark(-5)
assert not valid_mark(105)
print('Invalid input rules passed')
