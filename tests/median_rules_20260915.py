def median(values):
    values = sorted(values)
    n = len(values)
    if n % 2:
        return values[n // 2]
    return (values[n // 2 - 1] + values[n // 2]) / 2

assert median([1, 3, 5]) == 3
assert median([1, 3, 5, 7]) == 4
