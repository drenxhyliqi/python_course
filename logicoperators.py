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
banned_domains = [".com", ".eu", ".org"]
user_domain = input("Shkruaj domainen: ")

# Lopping inside the list
# Lopping inside the array, eachbanned is iteratation in the array
is_banned = any(eachbanned in user_domain for eachbanned in banned_domains)
print(f"My doamin is banned form this site: {is_banned} ")
# print(
#     f"My domain is not banned from the site: {user_domain not in banned_domains}")

sep()

# Identity Operators "is" and "is not"
# Checks if two variables refer to the same object in memory
# The == operator compares the values
# The "is" operator instead compares the id's of the values that are stored in the memory

# Example
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)
u_email = None
print(u_email is not None and u_email != "")

sep()

# End Section Challenges

# 1 Check if a user's name is not empty and the age is >= 18
u_name = str(input("Write your name: "))
valid_name = u_name != ""

u_age = int(input("Write your age: "))
valid_age = u_age >= 18

print(
    f"User's name is valid: {valid_name} - and the user's age is valid:  {valid_age}")


# 2 Check if the password is at least 8 characters long and does not contain spaces

u_password = input("Write your password: ")
valid_pass = len(u_password) >= 8 and " " not in u_password
print(f"Password is valide: {valid_pass}")

# 3 Check if users email is not empty, contains '@', and ends with '.com'
user_email = input("Write you email again: ")
valid_email = user_email != "" and "@" in user_email and user_email.endswith(
    '.com')

print(f"Your email is valide: {valid_email}")


# 4 Check if the user is either an admin or a moderator, and either they are not banned or thet have verified their email
is_admin = False
is_moderator = True
baned = True
is_verified = True

can_access = (is_admin or is_moderator) and (not baned or is_verified)

print(f"User can access: {can_access}")
