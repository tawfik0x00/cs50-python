import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    # we get the match
    match = re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$",ip)

    # Check if no matches
    if not match:
        return False


    for part in match.groups():
        # Check if any part starts with zero
        if len(part) > 1 and part.startswith("0"):
            return False

        num = int(part)

        # check the range
        if num < 0 or num > 255:
            return False

    return True


if __name__ == "__main__":
    main()

