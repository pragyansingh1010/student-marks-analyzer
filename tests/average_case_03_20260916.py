def average(values):
    return sum(values) / len(values) if values else 0

assert average([10]) == 10
print('case 03 passed')