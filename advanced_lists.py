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
