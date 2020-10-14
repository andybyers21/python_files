import datetime


def one_hundred():
    """ Calculate date when a user will be 100 years old.

    Ask user for thier name and age.
    Check validty of user input.
    Perform calculations.
    Return result.
    """
    name = input("What is your name? ")
    age = input("How old are you? ")
    try:
        clac = 100 - int(age)
        year_calc = datetime.date.today().year + clac
        print(f"Hi {name} you will be 100 years old in {year_calc}")
    except:
        print("Please enter a valid age")


one_hundred()
