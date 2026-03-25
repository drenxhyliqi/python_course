import math


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

sep()

# Numeric Operators
print(2 + 3)
print(9 - 3)
print(5 * 5)
print(10 / 2)
print(10 // 3)  # It rounds the number
print(7 % 3)  # It prints the leftovers after the number is divided
print(2 ** 10)  # It prints the first number on the power of the second power

sep()

# Math functions
print(abs(2 - 10))  # The abs function removes the negative sign
# Rounding Numbers
price = 321.3841
print(round(price))
print(round(price, 2))
# This is not a built in function you have to import the math python library
print(math.floor(price))
print(math.ceil(price))

# Math trunc removes the other numbers does not round the number
print(math.trunc(price))
