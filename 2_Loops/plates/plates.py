def main():
    #Get user input and convert
    plate = input("Plate: ")

    if (is_valid(plate)):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):

    # Convert to upper and get the length
    s = s.upper()

    # rule 1: length between 1 and 6
    if len(s) < 2 or len(s) > 6:
        return False

    # rule 2: only alphanumeric characters
    if not s.isalnum():
        return False

    # rule 3: first two characters must be letters
    if not s[:2].isalpha():
        return False

    # check if the first digit is 0
    starting_number = False
    for c in s:
        # if is digit
        if c.isdigit():

            if not starting_number:

                # if is 0 return false
                if c == '0':
                    return False

                starting_number = True
        else:
            if starting_number:
                return False


    return True

if __name__ == "__main__":
    main()

