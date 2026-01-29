def main():
    percent = convert(input("Fraction: "))
    print(gauge(percent))

def convert(fraction):
    while True:
        try:
            # we need to remove all white spaces and split it to two variables
            x, y = fraction.strip().split('/')
            # convert to decimal values
            x = int(x)
            y = int(y)
            # get the percentage
            z = x / y

            if z <= 1:
                # Multiply percentage by 100
                p = int(z * 100)
                return p
            else:
                fraction = input("Fraction: ")
                pass

        except (ValueError,ZeroDivisionError):
            raise

def gauge(percentage):

    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()