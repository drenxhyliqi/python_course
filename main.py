import random
# First program with variables, data types, inputs and an simple if statement
password = input("Enter your password: ")
if len(password) < 8:
    print("Password should have 8 or more characters")
else:
    print("Passowrd is the right length!")

# Filter and find only the number without any operators
phone = "+383-49-211-199"

print(
    f"The phone number filtered is: {phone[phone.find('+'):].replace('-', '').strip('+')}"
)

# Generate a random number from 1-100 and check if that number is even
random_num = random.randint(1, 100)
print(random_num)

if random_num % 2 == 0:
    print(f"The number {random_num} is even")
else:
    print(f"The number {random_num} is odd")
