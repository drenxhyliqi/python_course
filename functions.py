# Functions
def make_coffee():
    print("Start Machine")
    print("Make Coffee")
    print("Add Milk")
    print("Enyoy it")


def clean_up(first_name, last_name, country="Not Known"):  # Default Parameters
    if not name:
        return None
    else:
        cleaned = name.strip().lower()
        return cleaned


def double_return(position):
    position_lo = position.strip().lower()
    position_up = position.strip().upper()
    return position_lo, position_up


# *args and **kwargs allow functions to accpet a unknown number of arguments

# * Tupple


def total(*args):  # * We use the 1 star args when we pass similiar values into the function
    print(sum(args))

# * Dict


def create_user(**kwargs):
    print(kwargs)


print("Wake up")
make_coffee()
print("Working for a while")
make_coffee()

# Params and arguments
name = "  MariA  "
print(name.strip().lower())

clean_up("  LarRrED ", " JacKSon  ", "DE")  # Positional Argument
clean_up("  SaaDerr ", "  KoldAn  ", "USA")
clean_up("  DreN ", "  XhyLIQI  ")

total(1, 2)
total(1, 2, 3)
total(10, 12, 341, 931)

create_user(first_name="Mo",
            last_name="Salah",
            age=33,
            country="Egypt"
            )

create_user(name="Lionel",
            country="Argentina"
            )

print(double_return("Software EnginEEr   "))


# * Task: store application log messages in a file

def write_log(message):
    with open(r"app.log", "a") as file:
        file.write(message + "\n")


write_log("App started")
write_log("User Logged In")


# Transformation Function
# * Task : Clean email addreses and split them into structered data
def clean_and_split(email):
    cl_email = email.strip().lower()
    # drenxh@gmail.com
    username, domain = cl_email.split("@")
    return {"Username": username, "Domain": domain}


print(clean_and_split("  tesTEmAil@gmail.com"))
