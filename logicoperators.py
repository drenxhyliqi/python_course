def sep():
    print("-" * 30)


# Boolean functions True - False
print(bool(12))  # True if the value is non-empty or non-zero
print(bool("Hi"))
print(bool())  # False if the value is empty or zero
print(bool(0))
print(bool(""))
print(bool(None))

sep()

# The "any" function, it takes 2,3 or more values and if at least one of them is True returns True
# The "all" function returns True if all the values are True


# Allow registration of the user if any field is fillet (at least one )
email = ""
phone = "02135-1245"
username = ""

# This prints True because the values are false,true,false so one of them is true
print(any([email, phone, username]))
# This print false because it requires all of the values to be true
print(all([email, phone, username]))

sep()

# Comparison Operators ==, != , <, <=, >, >= | Its only True and False
num1 = 8
num2 = 10
numr3 = 8
print(num1 < num2)
print(num2 - num1 != 2)
print("\n")

# We can also compare letters (string values)
print("a" < "b")
print("d" > "z")
print("a" == "A")  # Python is case sensitive so this prints false

# The "=" operator assigns values to a variable
# The "==" compares to values
sep()

# Check if the age is between 18 and 30
age_input = int(input())
print(18 <= age_input <= 30)

sep()

# Logical Operators or - and
# The "or" operator need one of the conditions to be true
print(5 > 10 or 5 != 10)
# The "and" operator needs both of the conditions to be true for it to be true
print(100 > 10 and 60 == 60)
print(100 < 99 and 5 == 5)  # This will print false
# The "and" operator has higher priority than "or" operator
sep()
# Challenge if the system is under pressure
cpu_usage = int(input())
memory_usage = int(input())
# The system is under pressure when both the cpu_usage and the memory_usage are above 85 so >= 85
print(
    f"Is the system under pressure: {cpu_usage >= 85 and memory_usage >= 85}")

# The system is under pressure when at least one of the components is above >= 95
print(f"Is the system under pressure: {cpu_usage >= 95 or memory_usage >= 95}")

sep()
# Challenge check user credentials before login
email2 = True
password = False

print(f"User's credentials are correct: {email2 and password}")
print(f"User's credentials are incorrect: {email2 or password}")

sep()

# NOT operator !
print(not 5 == 10)
print(5 != 2)

sep()
# Excecution Order challenge
# Allow access only if the user is logged in or they are guest but they must not be banned
print("Execution order challenge")
is_logged_in = False
is_guest = True
is_banned = True

print(
    f"Does the user has access: {(is_logged_in or is_guest) and is_banned}")

sep()
# Challenge
# Validate that the domain is not on the banned list
print("Domain challnge validation")
banned_domains = ".com", ".eu", ".org"
user_domain = input()

print(
    f"Is my domain banned from this site: {user_domain not in banned_domains}")
