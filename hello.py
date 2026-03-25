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

# Working with strings

# Type
name = "Dren"
age = 20
print(type(name))
print(type(age))

# str
print("Your age is: " + str(age))

# Math
password = "123a"
print(len(password))
# If statment just for testing
if len(password) < 8:
    print("Password should have 8 or more characters")
else:
    print("Passowrd is the right length")

text = """
python is easy to learn and python is 
one of the most used languages in 2026
python is also used in data, web, ai etc
"""
print(text.count("python")
      )  # This shows how many times the python word is repeated *it's case sensitive*

# Replace function challenge
phone = "+49 (176) 123-4567"
print(phone.replace("+", "").replace("(", "").replace(")",
      "").replace("-", "").replace(" ", ""))


# f strings
print(f"my name is {name} and my age is {age}")

# Spliting strings
stamp = "2026-03-25"
csv_file = "123,Max,USA, 1970-10-2026,Male"
print(stamp.split("-"))
print(csv_file.split(","))

# The * operator
print("ha" * 3)

# Functions in Python


def seperator():
    print("-" * 40)


# Calling the function
seperator()

# Data extraction indexing and slicing
# [start:end:step]

text = "Python"

# Extracting the first character
print(text[0])
# You can also use the negative indexing but it always starts from -1
print(text[-6])

# Extracting the last character (the indexing starts from 0)
print(text[5])
print(text[-1])

date = "2026-09-20"
print(date[0:4])
print(date[:4])
print(date[5:7])

# Removing spaces
surname = " Hardy"
city = "###London###"
print(surname.lstrip())  # Removes the spaces from the left side
print(surname.rstrip())  # Removes the spaces from the right side
print(surname.strip())  # Removes the spaces from both sides

# Giving an symbol as a parameter removes that symbol from both sides
print(city.strip("#"))

# How to see if you have blank spaces in your data
print(len(surname))
print(len(surname.strip()))
nr_of_spaces = len(surname) - len(surname.strip())
is_clean = len(surname) == len(surname.strip())
print(f"Number of spaces : {nr_of_spaces}")
print(f"The word is clean : {nr_of_spaces == is_clean}")

seperator()

# Case Conversion
lang = "python PROGRAMMING"
print(lang.lower())  # Converts everything to lowercase
print(lang.upper())  # Converts everything to uppercase

# We made the search and the data the same case and removed any possible non nesseccary spaces
search = "Email ".lower().strip()
data = " emAIl".lower().strip()
print(f"The data is clean: {search == data} ")

seperator()

todays_date = "2026-Mar-03"
phone_num = "+383-49-123-567"
pers_email = "info@gmail.com"
office_num = "383-49-175-642"

# Searching
# startswith(), endswith(), "Feb" in
# find ( "Feb")

print(f"The phone number start with 383 : {phone_num.startswith("+383")}")
print(f"The phone number start with 383 : {phone_num.startswith("+386")}")
print(f"The domain is gmail.com : {pers_email.endswith("gmail.com")}")
print(f"You have an @ in email : {"@" in pers_email}")

# Extrating only the number with find()
print(
    f"This prints the index of the deired character we are looking: {phone_num.find("-")}")
print(
    f"This is dynamic finding: {phone_num[phone_num.find("-"):]} it finds the numbers after the - sign")
print(
    f"If we want oly the number we also add the replace func: {phone_num[phone_num.find('-'):].replace('-', '')} it finds the numbers after the - sign without including the -")
seperator()


# Validation
country = "USA"
city = "Bost0n#"
postal = "03249"
radio_hz = "129.2"
# This check if everything stored in country variable is alphabetic (no numbers)
print(f"The country var is all letters : {country.isalpha()}")
print(f"The city var is all letters : {city.isalpha()}")
print(f"The postal var is all numbers : {postal.isnumeric()}")
print(
    f"For radio_hz var the isnumeric() does not work because is an decimal number : {radio_hz.isnumeric()}")
