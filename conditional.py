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
