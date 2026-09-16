def average(values):
    return sum(values) / len(values) if values else 0

assert average([2, 4, 6, 8]) == 5
print('case 04 passed')