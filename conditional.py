# if statment with only one condition

grade = int(input("Write your score: "))
submitted_project = True
attendance = True

# if grade >= 90:
#     if submitted_project:  # Nested if-s
#         print("A+")
#     else:
#         print("A")
if grade >= 90 and submitted_project:
    print("A+")
elif grade >= 90:
    print("A")
elif (grade >= 80):
    print("Your grade is B")
elif (grade >= 70):
    print("Your grade is C")
elif (grade >= 60 or submitted_project):
    print("Your grade is D")
else:
    print("You have failed!")

# Ternary if -  the best
print("A++" if grade >= 90 and submitted_project and attendance else "A+")

# Check if a number is even or odd
number_1 = int(input("Write your number: "))


def check_even(number):
    if number % 2 == 0:
        print("The number is even!")
    else:
        print("The number is odd!")


check_even(number_1)

number_2 = int(input("Write your second number: "))
check_even(number_2)


# Match case
# Pattern matcher
country = "Kosovo"

match country:
    case "United States" | "USA" | "US":
        print("US")
    case "India":
        print("IN")
    case "Egypt":
        print("EG")
    case "Germany" | "Deutschland":
        print("DE")
    case "Kosovo":
        print("KS")
    case _:
        print("Unknown Country")


# Challenge Email
# Validate the quailty and correctness of email values
# 1. Must not be empty
# 2. Must contain '.' and '@'
# 3. Must contain excatly one @ symbol
# 4. Must end with '.com','.org' or '.net'
# 5. Must not be longer than 254 characters
# 6. Must start and end with a letter or a digit

while True:
    email = input("Write your email: ")

    if email == "":
        print("Email can not be empty!")
    elif "." and "@" not in email:
        print("Email should have at least one . and one @")
    elif email.count("@") != 1:
        print("You can have only one @ symbol")
    elif not email.endswith(".com" or ".org" or ".net"):
        print("Email is not valid use .com, .org or .net")
    elif len(email) > 254:
        print("Email should have less than 254 characters")
    elif not email[0].isalnum() and email[-1].isalnum():
        print("Email should start with a letter or number")
    else:
        print(email)
        break

# Challenge Password
# Validate the quality and correctness of passwords
# 1. Must not be empty
# 2. Must be at least 8 characters
# 3. Must include at least 1 uppercase
# 4. Must include at least 1 lowercase
# 5. Must not be same as the email
# 6. Must not contain any spaces
# 7. Must start and end with a letter or a digit

while True:
    password = input("Write your password: ")

    if password == "":
        print("Password must not be empty!")
    elif len(password) < 8:
        print("Password must have at least 8 characters")
    elif not any(char.isupper() for char in password):
        print("Password must contain at least one uppercase")
    elif not any(char.islower() for char in password):
        print("Password must contain at least one lowercase")
    elif password == email:
        print("Password must not be same as the email")
    elif " " in password:
        print("Password must not conatin any spaces")
    elif not password[0].isalnum() or not password[-1].isalnum():
        print("Password must start and end with a letter or a digit")
    else:
        print("VALIDE")
        break

 # Challenge check if a number is even with ternary operators

check_num = int(input("Write your number: "))

result = "Even" if check_num % 2 == 0 else "Odd"
print(result)
