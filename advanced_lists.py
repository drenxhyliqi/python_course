# In real world projects we dont actually modify the data inside the lists,
# we make a copy of the original list and modify that
# If things go wrng we always have the original list

import copy

original = ['a', 'b', 'c', 'd']

# Here we use the assignmnet = to only refere to the original list, and not actually make a coppy of it
copy_list = original
# So both variables are referencing in the same list in memory
print(copy_list)

copy_list = original.copy()  # This will make a copy of the original list

copy_list.append('e')
print("This is the uptaed copy list: ", copy_list)
print("This is the original list unchanged: ", original)


# DeepCopy
matrix = [
    ['a', 'b'],
    ['x', 'z']
]
matrix_cp = copy.deepcopy(matrix)
print('Original: ', matrix)
matrix_cp[0].append('c')
print('Copy: ', matrix_cp)


list1 = [
    ['a', 'b'],
    ['c', 'd']
]

# Assigment
copy1 = list1  # They refer to the same object
print("Same object: ", list1 is copy1)
# Shallow Copy
# With copy they dont refer to the same object but it does not affect deep in the layers of the list
copy2 = list1.copy()
print("Same object: ", list1 is copy2)
print("Shared Lists?: ", list1[0] is copy2[0])  # They share the same children

# Deep Copy
deepcopy = copy.deepcopy(list1)
print("Same referencing: ", list1 is deepcopy)
print("Shared Lists for deep copy?: ", list1[0] is deepcopy[0])


# Combining Lists
letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
comb = letters + numbers  # With the + operator
print("The combined list:", comb)

print(letters * 2)  # You can multiply lists

comb2 = [letters, numbers]  # Building a nested list
print(comb2)

# This extends the list but without changing the original
letters.extend(numbers)
print(letters)

# Zip Function for pairing lists in tuples
# The outcome is a list of tuples

char = ['x', 'z', 'y', 'g']
num = [5, 6, 7]
# If we only use the list we are going to get the iterator object, so we use the list to change the data type
combined = list(zip(char, num, "car"))
# The list stops at the shortest list so the letter g will not be paired with anything
print(combined)

# Example
ids = [101, 102, 103]
names = ['Ali', 'Sarah', 'John']
# It makes the relationship with ids and the names
employee = list(zip(ids, names))
print(employee)


# Enamurate - retruns the index and the value
iteratable = ['a', 'b', 'c', 'd']

# print(list(enumerate(iteratable, start = 1)))
for index, value in enumerate(letters):
    print(index, value)

print(list(reversed(iteratable)))

for index2, value2 in enumerate(employee):
    print(index2, value2)  # Iterating in tupples


# The map iterator
fruits = ['banana', 'kiwi', 'apple', 'pineapple', 'watermelon']
# The map function will make changes to our list without the need of a for loop,
# it just needs 2 parameters function/iteratable
print(list(map(str.upper, fruits)))

messy_names = ['  Kevin  ', ' Adam  ', 'Leo  ']
print(list(map(str.strip, messy_names)))  # Cleaning lists from unwanted spaces

for n in map(str.strip, messy_names):
    print(n)


# FIltering Data
mixed = ['DREN', '18', '499912', 'ABBY', 'CANE', '24']
for f in filter(str.isalpha, mixed):
    print(f)


# Lambda - for creating your own logic (anonymous function)
# lambda input : expression
print('lambda')
def multiply(x): return x*4
def sum(x, y): return x + y


# Multiply var is holding this formula
print(multiply(10))
print(sum(10, 90))


def check(i): return i in "python"


print(check('n'))
prices = ['12.50$', '6.66$', '100$', '9.99$']
# First the data transformation p.replace('$','')
# Assigned to lambda p: p.replace('$','')
# Use the map for the logic and iterable
print(list(map(lambda p: float(p.replace('$', '')), prices)))

# Lambda + filter
prices = [120, 30, 300, 80]
print(list(filter(lambda p: p >= 100, prices)))

students = [
    ['Maria', 95],
    ['John', 70],
    ['Mike', 68],
    ['Lamar', 98]
]
# For nested list we always give lambda the row
print(list(filter(lambda row: row[1] >= 80, students)))
print('\n')
print(list(filter(lambda row: row[0].startswith('M'), students)))


# Comprehension
domains = [
    'www.google.com',
    'www.openai.com',
    'localhost3000',
    'WWW.CHATGPT.COM',
]

cleaned = [
    # Data transformation
    d.lower().replace('www', '').strip('.')
    # For loop
    for d in domains
    # Data filtering
    if '.' in d  # Remove the localhost3000 from the list
]

print(cleaned)


# Sets
# It holds unique values so no duplicate values

my_set = {10, 30, 20, 10}
print(my_set)

print(type(my_set))
my_set.remove(20)
print(my_set)  # Set is mutable


# Set methods
a = {10, 20, 30, 40}
b = {30, 40, 50, 60}

# ADDING AN ITEM
a.add(90)  # If its not there it adds it so only new values
print(a)

a.update("Hi")
a.update([1, 2, 0])
a |= {9, 19, 2}

# Removing items
a.remove(10)
a.discard(78)
print(a)

# Set math operations

# Combine 2 sets
print(a.union(b))  # Does not change the original sets it just merges them
print(a | b)  # Same but with the operator

# Intersection (te perbashketat)
print(a.intersection(b))
print(a & b)

# Only in A not in B
print(a.difference(b))
print(b - a)

# The unique values, only non shared items
print(a.symmetric_difference(b))
print(a ^ b)


# Set relationship methods True/False
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60}
set3 = {20, 30, 50}

# If all items in A exist in B
print(set1.issubset(set2))
print(set3.issubset(set1))

# Are the sets unique, you dont  have overlapping
print(set1.isdisjoint(set2))
print(set3.isdisjoint(set2))

# Dictionaries, its ordered, not indexed, mutable, duplicates only in values (not keyes)
names = ['alex', 'kumar', 'maria']
ages = [33, 21, 20]
countries = ['USA', 'India', 'Albania']

# pairs of keyvalues
# Keyes are unique
# Vlues allow duplicates
my_dict = {
    'a': 10,
    'b': 20,
    'c': 30,
    'a': 40
}
# DIctionarie is not indexed, here we use keyes
print(my_dict)
print(my_dict['b'])  # Its keyed
my_dict['c'] = 80  # Its mutable
print(my_dict)

# Dict methods
user = {"id": 1, "age": 30, "city": "Berlin"}

# How to acces
print(user['city'])
# If you dont know if the key exist you use the get method
print(user.get('name', "Unknown"))

# Check the keyes
print("age" in user)
print("name" in user)

# View Objects
print(user.keys())
print(user.values())

# Keys + values
print(user.items())

# Looping in dicts
for key, value in user.items():
    print(key, value)


# Add, Remove, Update key / values

# Adding
user["name"] = "John"
print(user)

# Updating
user["age"] = 15
# Update multiple values
user.update({"age": 20, "name": "Dren", "city": "Paris"})
print(user)

# Removing
item_removed = user.pop("age")
user.pop("Salary", "Not found")
print(user)
print(item_removed)

# Creation
users = dict.fromkeys(["relegion", "gender", "height", "weight"], None)
print(users)
