def valid_marks(m):
    return 0 <= m <= 100

assert not valid_marks(-1)
assert not valid_marks(101)
print('case 02 passed')