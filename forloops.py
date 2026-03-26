# Simple for loop
for i in range(5, 25, 2):  # start, stop, step
    print(f"Round {i}")

# Iterating with a loop inside a TUPLE
languages = ("Python", "Javascript", "JAVA", "C++")
for lang in languages:
    print(f"Language is: {lang}")

# Iterating in another data structure LISTS
grades = [9, 10, 8, 7, 6, 6, 9, "Fail"]
for g in grades:
    print(f"Grades: {g}")

# Iterating inside a string

longword = "aufwiederesehen"

for lw in longword:
    print(f"Letter: {lw}")

for i, lw in enumerate(longword):
    print(f"Letter {i + 1}: {lw}")


# Print all the even numbers from 1 to 100 dummy approach
for n in range(1, 100, 2):
    print(n)
