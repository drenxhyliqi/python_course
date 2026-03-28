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
