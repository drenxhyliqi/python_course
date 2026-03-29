# Functions
def make_coffee():
    print("Start Machine")
    print("Make Coffee")
    print("Add Milk")
    print("Enyoy it")

# *args and **kwargs allow functions to accpet a unknown number of arguments


def clean_up(first_name, last_name, country="Not Known"):  # Default Parameters
    first = first_name.strip().lower()
    last = last_name.strip().lower()
    full_name = first + " " + last
    print(full_name, "From: ", country)


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
