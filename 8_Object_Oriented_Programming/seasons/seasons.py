import sys
import re
from datetime import date
import inflect

p = inflect.engine()

def main():
    # first we need to get the birthdate
    birth_date = input("Birthdate: ")
    # second we need to check if we didn't find the right format we should exit
    try:
        # extract tuple values to elements.
        year, month, day = check_birth_date(birth_date)
    except:
        sys.exit("Invalid date")

    # now we need to work the date and calculate the number of days from birth_date until today date
    # we will work with datetime module classes specificly day class

    # create object from my birth
    my_birth_date = date(year, month, day)

    # create object from today birth
    current_date = date.today()

    # we need number of days from my birth until now
    difference = current_date - my_birth_date

    # calculate minutes
    minutes = difference.days * 24 * 60
    # convert digits to words
    # we will work with inflect module
    output = p.number_to_words(minutes, andword="")
    # finall step print words
    print(output.capitalize() + " minutes")
    sys.exit(0)

# we need function to check birthdate and return year , month and day
def check_birth_date(birth_date):
    # we need to check a specific pattern
    pattern = r"^\d{4}-\d{2}-\d{2}$"

    # check if patter found return a tuple of values
    if re.search(pattern, birth_date):
        # we need to get year, month, and year
        year, month, day = birth_date.split("-")
        # return tuple of values
        return (int(year), int(month), int(day))
    else:
        return None

if __name__ == "__main__":
    main()