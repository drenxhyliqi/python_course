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
