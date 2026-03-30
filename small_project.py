# * Project:
# * 1. Receive an email from the user
# * 2. Validate the email
# * 3. If it is invalid, log an erorr in a file
# * 4. If it is valid, clean and structure the email
# * 5. Log each step of the program

def is_email_valid(email):
    return '@' in email and '.' in email


def write_log(email):
    with open("email_info.log", "a") as file:
        file.write(email + "\n")


def clean_email(email):
    cleaned = email.strip().lower()
    username, domain = cleaned.split('@')
    return {
        "Username": username,
        "domain": domain
    }


def process_user_email(email):
    if is_email_valid(email):
        cleaned = clean_email(email)
        write_log(f"Email is valid: {cleaned}")
        print(cleaned)
        print(f"Email is valid: {email}")
    else:
        write_log(f"This email is invalid: {email}")
        print("Invalid email!")


email = input("Write your email: ")
process_user_email(email)
