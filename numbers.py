def sep():
    print("-" * 30)


# Checking number types
x = 5
y = 3.14
z = 2 + 3j

print(type(x))
print(type(y))
print(type(z))
sep()

# Converting a data type from string to number
d = "24"
print(type(d))  # This will print str as a data type
print(d * 3)  # it will multiply the string 3 times 242424 not the number 24 * 3 = 72

d_as_num = int(d)
print(type(d_as_num))  # Now the d is converted to an int number
print(d_as_num * 3)  # It multiplys the number
sep()


# We can also convert a number from int to float
print(float(d_as_num))
