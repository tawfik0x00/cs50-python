def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # first remove our $ from leading left side of our number
     return float(d.lstrip('$'))

def percent_to_float(p):
    # r mean right remove % from right side of our number
    return float(p.rstrip('%')) / 100


main()
