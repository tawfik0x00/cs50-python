# Set a loop to take the inputs from the user

while True:
    try:
        x, y = input("Fraction: ").split("/")

        x = int(x)
        y = int(y)

        if x < 0:
            raise Exception

        if x > y:
            continue

        z  = round((x / y) * 100)

    except (ValueError, ZeroDivisionError):
        pass
    except Exception:
        print("Invalid input")
    else:
        break

if z <= 1:
    print("E")
elif z >= 99:
    print("F")
else:
    print(f"{z}%")

