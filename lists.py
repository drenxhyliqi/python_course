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
