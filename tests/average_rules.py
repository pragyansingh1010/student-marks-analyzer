def average(values):
    return sum(values) / len(values) if values else 0

assert average([]) == 0
assert average([10, 20, 30]) == 20
assert average([100]) == 100
print('Average rules passed')
