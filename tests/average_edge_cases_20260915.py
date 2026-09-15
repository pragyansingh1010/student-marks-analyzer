def average(values):
    return sum(values) / len(values) if values else 0

assert average([0, 0, 0]) == 0
assert average([1, 2]) == 1.5
print('Average edge cases passed')
