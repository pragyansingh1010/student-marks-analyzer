import numpy as np
import pandas as pd

# Input marks
marks = list(map(int, input("Enter marks: ").split()))

# Convert to NumPy array
a = np.array(marks)

# Basic calculations
total_students = len(a)
total_marks = np.sum(a)
average = np.mean(a)
median = np.median(a)
highest = np.max(a)
lowest = np.min(a)
range_marks = highest - lowest
variance = np.var(a)
std = np.std(a)

# Mode
s = pd.Series(a)
mode = s.mode()

if len(mode) == len(a):
    mode_result = "No Mode"
else:
    mode_result = " ".join(map(str, mode.tolist()))

# Passed and failed
passed = np.sum(a >= 40)
failed = np.sum(a < 40)

# Above 90
above_90 = np.sum(a > 90)

# Above and below average
above_average = np.sum(a > average)
below_average = np.sum(a < average)

# Pass percentage
pass_percentage = (passed / total_students) * 100

# Highest and lowest scorer positions
highest_scorer = np.where(a == highest)[0] + 1
lowest_scorer = np.where(a == lowest)[0] + 1

# Display result
print("\n========== STUDENT MARKS ANALYZER ==========")

print("Total Students     :", total_students)
print("Total Marks        :", total_marks)
print("Average            :", format(average, ".2f"))
print("Median             :", format(median, ".2f"))
print("Mode               :", mode_result)
print("Highest Marks      :", highest)
print("Lowest Marks       :", lowest)
print("Range              :", range_marks)
print("Variance           :", format(variance, ".2f"))
print("Standard Deviation :", format(std, ".2f"))

print("\nPassed Students    :", passed)
print("Failed Students    :", failed)
print("Above 90           :", above_90)
print("Above Average      :", above_average)
print("Below Average      :", below_average)
print("Pass Percentage    :", format(pass_percentage, ".2f"), "%")

print("Highest Scorer     : Student", *highest_scorer)
print("Lowest Scorer      : Student", *lowest_scorer)

print("============================================")