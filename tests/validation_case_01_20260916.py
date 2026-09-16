def valid_marks(m):
    return 0 <= m <= 100

assert valid_marks(0)
assert valid_marks(100)
print('case 01 passed')