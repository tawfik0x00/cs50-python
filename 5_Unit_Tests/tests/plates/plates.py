def main():
    # Get user input and convert it to uppercase
    plate = input("Plate: ").upper()

    if is_valid(plate):
        print("valid")
    else:
        print("Invalid")

def is_valid(s):
    # Convert it to upper
    string = s.upper()
    length = len(string)

    # Check maximum and minimum and if contain punctuation

    if (length < 2 or length > 6) or (string.isalnum() == False):
        return False
    # Check first two letters using slicing
    if not s[:2].isalpha():
        return False

    # Check if first number of plates is zero
    for c in string:
        if c.isdigit():
            if c == '0':
                return False
            else:
                break

    # Check middle of is contain a number
    mid = length // 2
    if s[mid].isdigit() and s[-1].isalpha():
        return False

    # Else
    return True

if __name__ == "__main__":
    main()