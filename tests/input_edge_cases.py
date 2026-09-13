def validate_marks(values):
    return all(0 <= value <= 100 for value in values)

assert validate_marks([0, 40, 100])
assert not validate_marks([-1, 50])
assert not validate_marks([50, 101])
print("Marks input edge cases passed")
