cost = [10, 15, 12, 20, 30, 100]

for c in cost:
    print(f"The single cost is: {c}")

print(f"The sum of all the cost is: {sum(cost)}")

# Data structers
# List [1,3,4,5] - common
# Tuple (10,20,30)- no changes
# Set {10,20,30} - unique
# Dict {a:10, b:20, c:15} - key/value pairs

# Lists

print(type(cost))

# Putting data inside a list

# Manually putting data inside a list
letters = ['a', 'b', 'c']
print(letters)

# You can mix data inside a list
mixed = [1, 'a', True, None]
print(mixed)

# Using the list built in func we can turn any datatype into a list
data = "hello world"
print(list(data))

numbers = list(range(5))
print(numbers)


# Nested Lists
nested = [
    [1, 2, 3, 4],
    ['a', 'b', 'c', 'd'],
    [True, False]
]
print(nested)
print("-" * 30)

# Access & Read
lst = ['a', 'b', 'c', 'd']
print(lst[0])
print(lst[-1])

matrix = [
    [1, 2, 3, 4],
    ['a', 'b', 'c', 'd'],
    [True, False]
]
# print [row][column]
print(matrix[0][2])

# Slicing
sli = [1, 2, 3, 4]
print(sli[:2])
print(sli[2:])

# print(matrix[:2])
print(matrix[1][:2])

# Unpacking
person = ['Mike', 26, 'Data Engineer', 'Boston', 'USA']
# name, age, role, country = person
# print(f"Information about : {name}, {age}, {role}, {country}")

# Unpacking Asterik *
print('Asterik')
name, *details, country = person
print(f"Information about : {name}, {details}, {country}")
print(name)
print(details)
print(country)

print('-' * 30)
name, *detail = person
print(name)
print(detail)

# Skipping items
education = ['Dren', 19, 25, 231, 381, True, None, 'University of Prishtina']
# with underscore you can skip items inside the list _,_ without creating to much variables
name, *_, faculty = education

print(f"Name: {name} - faculty: {faculty}")

print('-' * 30)
# Analyzing Lists
# Functions max(), min(), sum(), len(), all(), any()
# Methods .count(), .index()
# Operators in, is, ==, >

num = [1, 2, 4, 5, 2, 2, 3, 0, 2]
# Functions
print("Max:", max(num))
print("Min:", min(num))
print("Sum:", sum(num))
print("Length:", len(num))
print("All:", all(num))
print("Any:", any(num))

# Methods
print("Number 2 apperars", num.count(2), "times")
print("The index for number 5 is ", num.index(5))

# Operators
print("Is 5 in the list: ", 5 in num)
print("Is 8 not in the list: ", 8 not in num)
print("Is 5 the list: ", 5 is num)
print("Is num the list: ", num is num)
print("Is 5 the list: ", 5 is num)
print("Is person list == num list: ", person == num)
# It checks only the first values of the 2 list if sli first value > then num first value its True else False
print("Is sli list > num list: ", sli > num)

# Dynamic adding and removing
# ADD
# REMOVE
# UPDATE
print('-' * 30)

chars = ['a', 'b', 'c', 'd']
chars.append('e')  # It always insert things at the end of the list
print(chars)

# This func insert things based on the index you provide inside the list
chars.insert(1, 'x')
chars.insert(0, 'g')
matrix.insert(0, [1, 11, 111, 111])
matrix[0].append(1111)
matrix[1].insert(0, 'P')
print(chars)
print(matrix)

print('-' * 30)
# Deleting
chars.clear()  # It deletese all the content inside that list
print(chars)

chars.append('a')
chars.append('a')
print(chars)
# You give a specific element you want to remove it removes only the first match
chars.remove('a')

print(chars)

# Deleting by position
education.pop(0)
removed = education.pop()  # It will always removes the last item but also stores it
print(education)
print("removed item: ", removed)

# We use 'remove' when we want to remove things by the value
# We use 'pop' when we want to remove things by the position
print(matrix)
matrix[1].remove('P')  # It removes the P letter from row 1
matrix[-1].pop(0)  # Remove the first item of the last row
matrix[0].pop()  # It removes the last item of the first row
print(matrix)

print('-' * 80)

# Upadting Items

up = ['a', 'b', 'c', 'd']
up_mat = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]

up[2] = 'x'  # This overwrites the value
print(up)

up_mat[-1] = ['x', 'y', 'z']
print(up_mat)
up_mat[0][0] = '~~'
up_mat[1][1] = '$$'
print(up_mat)
