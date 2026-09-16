def average(values):
    return sum(values) / len(values) if values else 0

assert average([5, 15, 25, 35]) == 20
