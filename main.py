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
