def bounds(values):
    return min(values), max(values)

assert bounds([10, 20, 30]) == (10, 30)
assert bounds([50]) == (50, 50)
assert bounds([-1, 0, 5]) == (-1, 5)
print('Marks min/max rules passed')
