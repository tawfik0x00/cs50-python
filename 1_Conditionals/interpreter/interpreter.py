# split our expression to three variables
x , operator, y = input("Expression: ").strip().lower().split(" ", 2)

# convert our numbers to float
x = float(x)
y = float(y)

# check operator and print result
match operator:
    case '+':
        print(x + y)
    case '-':
        print(x - y)
    case '/':
        print(x / y)
    case '*':
        print(x * y)
    case _:
        print("invalid operator")
