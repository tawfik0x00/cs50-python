import re
import sys


def main():
    print(convert(input("Hours: ").strip()))


def convert(s):
    match = re.search(r"(\d{1,2}):?(\d{1,2})? (AM|PM) to (\d{1,2}):?(\d{1,2})? (AM|PM)", s)

    if match:
        # tuple of our values.
        pieces = match.groups()

        # check valid hours part
        if int(pieces[0]) > 12 or int(pieces[3]) > 12:
            raise ValueError

        # check valid minutes
        if pieces[1] != None:
            if int(pieces[1]) >= 60:
                raise ValueError

        if pieces[4] != None:
            if int(pieces[4]) >= 60:
                raise ValueError

        first_part = new_format(pieces[0], pieces[1], pieces[2])
        second_part = new_format(pieces[3], pieces[4], pieces[5])

        return first_part + " to " + second_part
    else:
        raise ValueError

def new_format(hour, minute, am_pm):

    # Hours part
    if am_pm == "PM":
        if int(hour) == 12:
            new_hour = 12
        else:
            new_hour = int(hour) + 12
    else:
        if int(hour) == 12:
            new_hour = 0
        else:
            new_hour = int(hour)

    # Minutes Part
    if minute == None:
        new_minute = 0
        new_time = f"{new_hour:02}:{new_minute:02}"
    else:
        new_time = f"{new_hour:02}:{minute:02}"

    return new_time


if __name__ == "__main__":
    main()
