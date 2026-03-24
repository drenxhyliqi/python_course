print("Hello World!")
print("Welcome to Python programming.")
print("Setting Up Python enviroment")

# This is a comment in python
# Comments are used to explain code and make it more readable
# Comments are ignored by the Python interpreter


# Printing multiple lines
print("This is the first line.")
print("This is the second line.")
print("This is the third line.")

# Special Characters in Python
print("This is an escape double quote \"Python\"")
print('You can use also this "format" with single quotes')
print("This is when you have to print a path: C:\\Users\\Test\\testDoc")
print("-------------------------------")
print("You can also use new lines \nto print a new line")
print("-------------------------------")
print("You can also use tabs \t to print a tab space between words")

# Python print challenge
print("Your Learning Path: \n\t - Python Basics \n\t - Data Engineering \n\t - AI")
print("""With Triple quotes 
      you can print multiple lines
      without using the new line character""")


# Variables in Python
x = 1  # This is a variable assignment
print(x)
x = 2  # You can reassign a variable
print(x)
y = x + 3  # You can perform operations with variables
print(y)
print(x + y)  # You can also perform operations directly in the print statement

name = "Dren"  # You can also assign string values to variables
print("Hello my name is", name)  # You can print variables along with strings
# You can also use f-strings for formatted printing
print(f"Hello my name is {name}")
# You can also concatenate strings and variables using the + operator
print("Hello my name is " + name)


# Input built in function of Python
# This will prompt the user to enter a value and return it as a string
userValue1 = input("Enter the first value: ")
# This will prompt the user to enter a value and return it as a string
userValue2 = input("Enter the second value: ")
# This will print the values entered by the user
print("You entered:", userValue1, "and ", userValue2)
# This will convert the input strings to integers and calculate their sum
sum = int(userValue1) + int(userValue2)
print("The sum of the two values is:", sum)  # This will print the sum of


# Challenge2
name = "xhyliqidren"
sub = "com"

print(f"Info@{name}.{sub}")
print(f"support@{name}.{sub}")
print(f"www@{name}.{sub} \n")

# Challenge 3 - Data Types
age = 20
height = 1.76
name = "Dren"
isStudent = True
graduate = None
print("---------------------------------------")
# Data value
print("Data values of the variables:")
print(age)
print(height)
print(name)
print(isStudent)
print(graduate)
print("\n")

# Data types
print("Data types of the variables:")
print(type(age))
print(type(height))
print(type(name))
print(type(isStudent))
print(type(graduate))
print("\n")

# Data lengths
print("Data lengths of the variables:")
print(len(name))
print(age.bit_length())
print("---------------------------------------")
