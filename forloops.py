def sep():
    print("-" * 30)


# Simple for loop
for i in range(5, 15, 2):  # start, stop, step
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
# for n in range(1, 100, 2):
#     print(n)

sep()
# Real world use cases of for loops

# Challenge find the total score
scores = [90, 100, 39, 159]
total = 0

for sc in scores:
    total += sc
    print(f"Current total: {total}")

print(f"the total is: {total}")

sep()

# Challenge Data cleaning
# First clean data then do data manipulation
files = ['  Report.csv  ', 'DATA.csv ', 'final.TXT ']
for c in files:
    c = c.strip().lower().replace('txt', 'csv')
    print(f"Cleaned file: {c}")

sep()
# Challenge print the 7-times table from 1 to 10 usgin a for loop
for i in range(1, 11):
    print(f"7 x {i} = {7 * i}")

sep()

# Challenge print a left-aligned pyramid of stars with 6 rows using a for loop
for i in range(1, 7):
    print(f"{"*" * i}")

sep()

# Break inside loops
for i in range(5, 20):
    if i > 10:
        break
    print(i)

sep()

names = ['john', 'mike', '', 'casey']

# Pass
for n in names:
    if n == '':
        pass  # todo: Handle Empty Value
    print(f"Name = {n}")

sep()

# Continue inside loops
for name in names:
    if name == '':
        continue  # Continue, continues the loop so it skips one loop cycle when that condition is met, it does not stop the loop
    print(name)

sep()

for n in names:
    if n == '':
        print("Empty value detected!")
        break  # The break, breaks the loop when the condition is met
    print(n)

sep()

# Challenge : loop through a list of days and print only the working days, skipping the weekends

days = ['monday', 'Tuesday  ', 'SaTurday  ',
        'Monday', 'WEDNESDAY', '  sunday  ', 'thursday']

for d in days:
    d = d.strip().lower()
    if d in ['saturday', 'sunday']:
        continue
    print(f"Working days: {d}")

sep()

# Challenge : scan emails to block unsafe data from entering your system
emails = [
    'data@gmail.com',
    'python@outlook.com',
    'DROP TABLE USERS;',
    'dren@gmail.eu'
]

for email in emails:
    if ';' in email:
        print("SQL INJECTION DETECTED")
        break
    print(email)
